"""Behavioral checks for the cookbook's dependency-free Python example."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
# This is a standalone example, not a package installed into the environment.
sys.path.insert(0, str(ROOT / "examples" / "python"))
import asset_budget as budget  # noqa: E402


def payload(byte_count: object = 40) -> dict[str, object]:
    return {
        "budget_bytes": 100,
        "assets": [{"path": "assets/app.js", "kind": "script", "bytes": byte_count}],
    }


class ManifestTests(unittest.TestCase):
    def test_valid_data_becomes_domain_records(self) -> None:
        manifest = budget.parse_manifest(payload())
        self.assertEqual(manifest.assets, (budget.Asset("assets/app.js", "script", 40),))

    def test_invalid_byte_counts_are_not_coerced(self) -> None:
        for value in (True, False, "40", 40.0, -1, None, budget.MAX_DECLARED_BYTES + 1):
            with self.subTest(value=value), self.assertRaisesRegex(budget.InvalidManifest, r"assets\[0\].bytes"):
                budget.parse_manifest(payload(value))

    def test_zero_byte_asset_and_empty_manifest_are_valid(self) -> None:
        self.assertEqual(budget.summarize(budget.parse_manifest(payload(0))).total_bytes, 0)
        empty = budget.parse_manifest({"budget_bytes": 1, "assets": []})
        self.assertEqual(budget.summarize(empty).largest, ())

    def test_missing_and_unknown_fields_fail(self) -> None:
        cases = (
            {},
            {"budget_bytes": 100, "assets": [], "typo": True},
            {"budget_bytes": 100, "assets": [{"path": "x", "kind": "other"}]},
            {"budget_bytes": 100, "assets": [{"path": "x", "kind": "other", "bytes": 0, "size": 0}]},
        )
        for value in cases:
            with self.subTest(value=value), self.assertRaises(budget.InvalidManifest):
                budget.parse_manifest(value)

    def test_invalid_shapes_and_kinds_fail(self) -> None:
        cases = (
            None,
            [],
            {"budget_bytes": 100, "assets": {}},
            {"budget_bytes": 100, "assets": [None]},
            {"budget_bytes": 100, "assets": [{"path": "x", "kind": "video", "bytes": 0}]},
        )
        for value in cases:
            with self.subTest(value=value), self.assertRaises(budget.InvalidManifest):
                budget.parse_manifest(value)

    def test_budget_must_be_a_positive_integer(self) -> None:
        for value in (0, -1, True, 1.5, "100", None):
            with self.subTest(value=value), self.assertRaisesRegex(budget.InvalidManifest, "budget_bytes"):
                budget.parse_manifest({"budget_bytes": value, "assets": []})

    def test_path_contract_rejects_ambiguous_or_control_paths(self) -> None:
        for path in ("", "/absolute", "../secret", "a/../b", "./a", "a//b", "a/", "C:/a", "a\\b", "a\nb", "a\x1bb", "x" * 513):
            row = {"path": path, "kind": "other", "bytes": 0}
            with self.subTest(path=path), self.assertRaisesRegex(budget.InvalidManifest, "relative POSIX path"):
                budget.parse_manifest({"budget_bytes": 1, "assets": [row]})

    def test_duplicate_asset_paths_fail(self) -> None:
        row = {"path": "a.js", "kind": "script", "bytes": 1}
        with self.assertRaisesRegex(budget.InvalidManifest, "duplicate asset path"):
            budget.parse_manifest({"budget_bytes": 100, "assets": [row, row]})

    def test_asset_count_is_bounded(self) -> None:
        with self.assertRaisesRegex(budget.InvalidManifest, "at most"):
            budget.parse_manifest({"budget_bytes": 100, "assets": [None] * (budget.MAX_ASSETS + 1)})


class FileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "manifest.json"

    def test_malformed_json_reports_location(self) -> None:
        self.path.write_text('{\n"assets": [}', encoding="utf-8")
        with self.assertRaisesRegex(budget.InvalidManifest, "line 2, column"):
            budget.load_manifest(self.path)

    def test_duplicate_json_keys_are_not_silently_overwritten(self) -> None:
        for source in (
            '{"budget_bytes":1,"budget_bytes":2,"assets":[]}',
            '{"budget_bytes":1,"assets":[{"path":"a","kind":"other","bytes":0,"bytes":1}]}',
        ):
            self.path.write_text(source, encoding="utf-8")
            with self.subTest(source=source), self.assertRaisesRegex(budget.InvalidManifest, "duplicate JSON object key"):
                budget.load_manifest(self.path)

    def test_non_finite_json_numbers_fail(self) -> None:
        for constant in ("NaN", "Infinity", "-Infinity"):
            self.path.write_text('{"budget_bytes":' + constant + ',"assets":[]}', encoding="utf-8")
            with self.subTest(constant=constant), self.assertRaisesRegex(budget.InvalidManifest, "non-finite"):
                budget.load_manifest(self.path)

    def test_invalid_encoding_fails(self) -> None:
        self.path.write_bytes(b"\xff\xfe")
        with self.assertRaisesRegex(budget.InvalidManifest, "UTF-8"):
            budget.load_manifest(self.path)

    def test_oversize_file_fails_before_decoding(self) -> None:
        self.path.write_bytes(b" " * (budget.MAX_INPUT_BYTES + 1))
        with self.assertRaisesRegex(budget.InvalidManifest, "exceeds"):
            budget.load_manifest(self.path)

    def test_excessive_nesting_becomes_input_error(self) -> None:
        self.path.write_text("[" * 2000 + "]" * 2000, encoding="utf-8")
        with self.assertRaises(budget.InvalidManifest):
            budget.load_manifest(self.path)

    def test_missing_file_preserves_io_error(self) -> None:
        with self.assertRaises(FileNotFoundError):
            budget.load_manifest(self.path)


class ReportTests(unittest.TestCase):
    def test_exact_budget_passes_and_one_extra_byte_fails(self) -> None:
        self.assertFalse(budget.summarize(budget.parse_manifest(payload(100))).over_budget)
        self.assertTrue(budget.summarize(budget.parse_manifest(payload(101))).over_budget)

    def test_totals_tie_breaking_and_top_limit(self) -> None:
        manifest = budget.parse_manifest({
            "budget_bytes": 200,
            "assets": [
                {"path": "b.js", "kind": "script", "bytes": 50},
                {"path": "a.css", "kind": "style", "bytes": 50},
                {"path": "c.js", "kind": "script", "bytes": 30},
            ],
        })
        report = budget.summarize(manifest, top=2)
        self.assertEqual(report.total_bytes, 130)
        self.assertEqual(dict(report.by_kind), {"script": 80, "style": 50, "image": 0, "font": 0, "other": 0})
        self.assertEqual([asset.path for asset in report.largest], ["a.css", "b.js"])
        self.assertEqual(report.as_dict()["remaining_bytes"], 70)

    def test_top_contract_is_also_enforced_for_library_callers(self) -> None:
        manifest = budget.parse_manifest(payload())
        for top in (0, 101, True, 1.5):
            with self.subTest(top=top), self.assertRaises(ValueError):
                budget.summarize(manifest, top=top)


class CliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "examples" / "python" / "asset_budget.py"), *args],
            text=True, capture_output=True, check=False, timeout=10,
        )

    def test_sample_json_output_and_success_status(self) -> None:
        result = self.run_cli(str(ROOT / "examples" / "python" / "assets.sample.json"), "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        report = json.loads(result.stdout)
        self.assertEqual(report["total_bytes"], 216000)
        self.assertEqual(report["remaining_bytes"], 34000)
        self.assertFalse(report["over_budget"])

    def test_over_budget_status_still_produces_a_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "over.json"
            path.write_text(json.dumps(payload(101)), encoding="utf-8")
            result = self.run_cli(str(path), "--format", "json")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr, "")
        self.assertTrue(json.loads(result.stdout)["over_budget"])

    def test_invalid_input_uses_stderr_and_status_two(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps(payload(True)), encoding="utf-8")
            result = self.run_cli(str(path))
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("assets[0].bytes", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_bad_cli_option_is_rejected_before_opening_file(self) -> None:
        result = self.run_cli("nonexistent.json", "--top", "0")
        self.assertEqual(result.returncode, 2)
        self.assertIn("--top", result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
