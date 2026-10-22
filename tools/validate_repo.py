"""Offline checks for cookbook structure, local Markdown targets, and reference metadata."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "dist", ".venv", "node_modules", "__pycache__"}
# A deliberately small inline-link checker, not a complete Markdown parser.
# Supports angle-bracket destinations (including spaces) and optional titles.
# Reference-style links, nested labels, and escaped/nested parentheses are out of scope.
INLINE_LINK = re.compile(
    r"\[[^\]\n]*\]\(\s*"
    r"(?:<(?P<angle>[^>\n]+)>|(?P<plain>[^\s()]+))"
    r"""(?:\s+(?:"[^"\n]*"|'[^'\n]*'|\([^)\n]*\)))?\s*\)"""
)


def validate(root: Path = ROOT) -> list[str]:
    errors = []
    try:
        catalog = json.loads((root / "references/catalog.json").read_text(encoding="utf-8"))
        if not isinstance(catalog, list):
            raise ValueError("catalog must be a list")
        seen = set()
        for entry in catalog:
            ref_id = entry["id"]
            if not isinstance(ref_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ref_id):
                raise ValueError("reference IDs must be lowercase slugs")
            if ref_id in seen:
                errors.append(f"Duplicate reference ID: {ref_id}")
            seen.add(ref_id)
            for key in ("name", "url", "origin", "status", "study", "reviewed_at"):
                if not isinstance(entry[key], str) or not entry[key].strip():
                    raise ValueError(f"{ref_id}: {key} must be nonempty text")
            if entry["origin"] not in {"user", "discovered"}:
                errors.append(f"{ref_id}: unsupported origin")
            if entry["status"] not in {"visual-reviewed", "content-reviewed", "unavailable"}:
                errors.append(f"{ref_id}: unsupported evidence status")
            url = urlparse(entry["url"])
            if url.scheme != "https" or not url.netloc:
                errors.append(f"{ref_id}: expected an HTTPS source URL")
            dt.date.fromisoformat(entry["reviewed_at"])
            study = (root / entry["study"]).resolve()
            if not study.is_relative_to(root.resolve()) or not study.is_file():
                errors.append(f"{ref_id}: study missing or outside repository")
            if not isinstance(entry["tags"], list) or not entry["tags"] or not all(isinstance(t, str) and t.strip() for t in entry["tags"]):
                errors.append(f"{ref_id}: tags must be a nonempty list of strings")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid reference catalog: {exc}")

    # Scope: inline Markdown file links, not external HTTP reachability or heading anchors.
    for file in root.rglob("*.md"):
        if any(part in SKIP for part in file.relative_to(root).parts):
            continue
        try:
            content = file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{file.relative_to(root)}: cannot read Markdown: {exc}")
            continue
        content = re.sub(r"```.*?```", "", content, flags=re.S)
        for match in INLINE_LINK.finditer(content):
            raw = match.group("angle") or match.group("plain")
            target = raw.split("#", 1)[0]
            if not target:
                continue
            try:
                if urlparse(target).scheme:
                    continue
            except ValueError:
                errors.append(f"{file.relative_to(root)}: malformed link {raw}")
                continue
            destination = (file.parent / unquote(target)).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                errors.append(f"{file.relative_to(root)}: missing local link {raw}")
    try:
        tasks = json.loads((root / "evals/tasks.json").read_text(encoding="utf-8"))
        if not isinstance(tasks, list) or not tasks:
            raise ValueError("tasks must be a nonempty list")
        task_ids = set()
        for task in tasks:
            if not isinstance(task, dict):
                raise ValueError("each task must be an object")
            task_id = task.get("id")
            if not isinstance(task_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", task_id):
                raise ValueError("evaluation task IDs must be lowercase slugs")
            if task_id in task_ids:
                errors.append("Duplicate evaluation task IDs")
            task_ids.add(task_id)
            prompt = task.get("prompt")
            checks = task.get("checks")
            if (
                task.get("track") not in ("web", "python")
                or not isinstance(prompt, str)
                or not prompt.strip()
                or not isinstance(checks, list)
                or not checks
                or not all(isinstance(check, str) and check.strip() for check in checks)
            ):
                errors.append(f"Invalid evaluation task: {task_id}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid evaluation tasks: {exc}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: reference catalog, evaluation tasks, and local Markdown file links")
    print("Not checked: external URLs, heading anchors, reference-style/complex Markdown links, browser accessibility, or visual quality")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
