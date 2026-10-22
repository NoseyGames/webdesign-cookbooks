"""Validate a local asset manifest and report its declared byte budget.

Python 3.11+, standard library only. This module never fetches URLs, scans
directories, or opens any path named inside the manifest.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, NoReturn, cast


MAX_INPUT_BYTES = 1_048_576
MAX_ASSETS = 10_000
MAX_DECLARED_BYTES = 1_000_000_000_000
KINDS = ("script", "style", "image", "font", "other")
AssetKind = Literal["script", "style", "image", "font", "other"]


class InvalidManifest(ValueError):
    """Input violates the manifest format; safe to display at the CLI boundary."""


@dataclass(frozen=True, slots=True)
class Asset:
    path: str
    kind: AssetKind
    bytes: int


@dataclass(frozen=True, slots=True)
class Manifest:
    budget_bytes: int
    assets: tuple[Asset, ...]


@dataclass(frozen=True, slots=True)
class Report:
    budget_bytes: int
    total_bytes: int
    asset_count: int
    by_kind: tuple[tuple[str, int], ...]
    largest: tuple[Asset, ...]

    @property
    def over_budget(self) -> bool:
        return self.total_bytes > self.budget_bytes

    def as_dict(self) -> dict[str, object]:
        return {
            "budget_bytes": self.budget_bytes,
            "total_bytes": self.total_bytes,
            "remaining_bytes": self.budget_bytes - self.total_bytes,
            "asset_count": self.asset_count,
            "over_budget": self.over_budget,
            "by_kind": dict(self.by_kind),
            "largest": [
                {"path": asset.path, "kind": asset.kind, "bytes": asset.bytes}
                for asset in self.largest
            ],
        }


def _require_fields(value: object, expected: set[str], where: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise InvalidManifest(f"{where}: expected an object")
    if set(value) != expected:
        raise InvalidManifest(f"{where}: expected exactly {', '.join(sorted(expected))}")
    return cast(dict[str, object], value)


def _require_int(value: object, minimum: int, where: str) -> int:
    # bool is an int subclass, but true is not a meaningful byte count.
    if type(value) is not int or not minimum <= value <= MAX_DECLARED_BYTES:
        raise InvalidManifest(
            f"{where}: expected an integer from {minimum} to {MAX_DECLARED_BYTES}"
        )
    return value


def _require_path(value: object, where: str) -> str:
    if (
        not isinstance(value, str)
        or not 1 <= len(value) <= 512
        or not value.isprintable()
        or "\\" in value
        or ":" in value
        or any(part in ("", ".", "..") for part in value.split("/"))
    ):
        raise InvalidManifest(f"{where}: expected a printable relative POSIX path")
    return value


def parse_manifest(payload: object) -> Manifest:
    """Validate untrusted decoded data; do not coerce or silently discard fields."""
    root = _require_fields(payload, {"budget_bytes", "assets"}, "manifest")
    budget = _require_int(root["budget_bytes"], 1, "budget_bytes")
    rows = root["assets"]
    if not isinstance(rows, list) or len(rows) > MAX_ASSETS:
        raise InvalidManifest(f"assets: expected an array with at most {MAX_ASSETS} items")

    assets: list[Asset] = []
    seen: set[str] = set()
    for index, raw in enumerate(rows):
        where = f"assets[{index}]"
        row = _require_fields(raw, {"path", "kind", "bytes"}, where)
        path = _require_path(row["path"], f"{where}.path")
        if path in seen:
            raise InvalidManifest(f"{where}.path: duplicate asset path")
        kind = row["kind"]
        if not isinstance(kind, str) or kind not in KINDS:
            raise InvalidManifest(f"{where}.kind: expected one of {', '.join(KINDS)}")
        byte_count = _require_int(row["bytes"], 0, f"{where}.bytes")
        assets.append(Asset(path, cast(AssetKind, kind), byte_count))
        seen.add(path)
    return Manifest(budget, tuple(assets))


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise InvalidManifest("duplicate JSON object key")
        result[key] = value
    return result


def _reject_constant(value: str) -> NoReturn:
    raise InvalidManifest("non-finite JSON numbers are not allowed")


def load_manifest(path: Path) -> Manifest:
    """Read a bounded UTF-8 JSON file. Filesystem errors remain OSError instances."""
    with path.open("rb") as stream:
        data = stream.read(MAX_INPUT_BYTES + 1)
    if len(data) > MAX_INPUT_BYTES:
        raise InvalidManifest(f"manifest exceeds {MAX_INPUT_BYTES} bytes")
    try:
        source = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise InvalidManifest("manifest must be UTF-8") from exc
    try:
        payload = json.loads(
            source, object_pairs_hook=_unique_object, parse_constant=_reject_constant
        )
    except InvalidManifest:
        raise
    except json.JSONDecodeError as exc:
        raise InvalidManifest(f"invalid JSON at line {exc.lineno}, column {exc.colno}") from exc
    except (ValueError, RecursionError) as exc:
        raise InvalidManifest("JSON number or nesting exceeds parser limits") from exc
    return parse_manifest(payload)


def summarize(manifest: Manifest, *, top: int = 5) -> Report:
    """Pure calculation on validated domain data; ties sort by path."""
    if type(top) is not int or not 1 <= top <= 100:
        raise ValueError("top must be an integer from 1 to 100")
    totals = {kind: 0 for kind in KINDS}
    for asset in manifest.assets:
        totals[asset.kind] += asset.bytes
    largest = tuple(sorted(manifest.assets, key=lambda item: (-item.bytes, item.path))[:top])
    return Report(
        manifest.budget_bytes,
        sum(totals.values()),
        len(manifest.assets),
        tuple(totals.items()),
        largest,
    )


def format_text(report: Report) -> str:
    status = "OVER BUDGET" if report.over_budget else "WITHIN BUDGET"
    lines = [
        f"{status}: {report.total_bytes:,} / {report.budget_bytes:,} bytes",
        f"Assets: {report.asset_count}; remaining: {report.budget_bytes - report.total_bytes:,} bytes",
        "By kind: " + ", ".join(f"{kind}={count:,}" for kind, count in report.by_kind),
        "Largest assets:",
    ]
    # ascii() keeps arbitrary filenames portable on terminals with legacy encodings.
    lines.extend(f"  {asset.bytes:>12,}  {ascii(asset.path)}" for asset in report.largest)
    return "\n".join(lines)


def _top_argument(value: str) -> int:
    try:
        count = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected an integer from 1 to 100") from exc
    if not 1 <= count <= 100:
        raise argparse.ArgumentTypeError("expected an integer from 1 to 100")
    return count


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="path to a UTF-8 asset manifest")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--top", type=_top_argument, default=5, help="largest assets to show (1-100)")
    args = parser.parse_args(argv)
    try:
        manifest = load_manifest(args.manifest)
    except (OSError, InvalidManifest) as exc:
        print(f"asset-budget: {exc}", file=sys.stderr)
        return 2
    report = summarize(manifest, top=args.top)
    output = json.dumps(report.as_dict(), indent=2) if args.format == "json" else format_text(report)
    print(output)
    return 1 if report.over_budget else 0


if __name__ == "__main__":
    raise SystemExit(main())
