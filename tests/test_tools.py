"""Contract tests for context export and offline repository validation."""

from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_context  # noqa: E402
import validate_repo  # noqa: E402


class RepositoryFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.parent = Path(self.temp.name)
        self.root = self.parent / "repo"
        self.root.mkdir()
        for relative, content in {
            "AGENTS.md": "Agent guidance",
            "docs/START-HERE.md": "Starting guidance",
            "evals/rubric.md": "Evaluation rubric",
            "recipes/web/02-layout.md": "WEB_LAYOUT",
            "recipes/web/01-type.md": "WEB_TYPE",
            "recipes/python/01-types.md": "PYTHON_TYPES",
            "references/studies/alpha.md": "ALPHA_STUDY",
            "references/studies/beta.md": "BETA_STUDY",
        }.items():
            self.write(relative, content)
        self.catalog = [
            {
                "id": ref_id,
                "name": ref_id.title(),
                "url": f"https://{ref_id}.example/",
                "origin": "user",
                "status": "content-reviewed",
                "study": f"references/studies/{ref_id}.md",
                "reviewed_at": "2026-10-21",
                "tags": ["editorial"],
            }
            for ref_id in ("alpha", "beta")
        ]
        self.tasks = [{
            "id": "web-layout",
            "track": "web",
            "prompt": "Build a responsive layout.",
            "checks": ["No overflow"],
        }]
        self.write_json("references/catalog.json", self.catalog)
        self.write_json("evals/tasks.json", self.tasks)

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_json(self, relative: str, value: object) -> Path:
        return self.write(relative, json.dumps(value))

    def cli(self, script: str, *args: str) -> subprocess.CompletedProcess[str]:
        # Copy the entry point so its __file__-derived ROOT is the isolated fixture.
        destination = self.root / "tools" / script
        destination.parent.mkdir(exist_ok=True)
        shutil.copy2(ROOT / "tools" / script, destination)
        return subprocess.run(
            [sys.executable, str(destination), *args],
            cwd=self.root, text=True, capture_output=True, check=False, timeout=10,
        )


class BuildContextTests(RepositoryFixture):
    def test_selected_track_only_and_deterministic_recipe_order(self) -> None:
        result = build_context.build("web", [], self.root)
        self.assertIn("Partial bundle", result)
        self.assertIn("does not satisfy full repository bootstrap", result)
        self.assertIn("Agent guidance", result)
        self.assertIn("Starting guidance", result)
        self.assertIn("Evaluation rubric", result)
        self.assertLess(result.index("WEB_TYPE"), result.index("WEB_LAYOUT"))
        self.assertNotIn("PYTHON_TYPES", result)
        self.assertNotIn("ALPHA_STUDY", result)
        python_result = build_context.build("python", [], self.root)
        self.assertIn("PYTHON_TYPES", python_result)
        self.assertNotIn("WEB_TYPE", python_result)

    def test_all_includes_both_tracks_examples_and_bootstrap_inventory_in_order(self) -> None:
        for relative, content in {
            "README.md": "ROOT_README",
            "BOOTSTRAP.md": "BOOTSTRAP_GUIDANCE",
            "FILE_TREE.md": "TREE_GUIDANCE",
            ".gitignore": "dist/",
            "examples/web/index.html": "<main>WEB_EXAMPLE</main>",
            "examples/python/app.py": "print('PYTHON_EXAMPLE')",
            "tests/check.py": "TEST_SOURCE",
        }.items():
            self.write(relative, content)
        result = build_context.build("all", [], self.root)
        included = [line.removeprefix("## Source: ") for line in result.splitlines() if line.startswith("## Source: ")]
        expected = list(build_context.BOOTSTRAP_ORDER)
        self.assertEqual(included[:len(expected)], expected)
        self.assertEqual(included[len(expected):], sorted(included[len(expected):]))
        for marker in ("WEB_TYPE", "PYTHON_TYPES", "ALPHA_STUDY", "BETA_STUDY", "WEB_EXAMPLE", "PYTHON_EXAMPLE", "TEST_SOURCE"):
            self.assertIn(marker, result)
        inventory = result.split("## Included file inventory\n\n", 1)[1].split("\n---", 1)[0]
        self.assertEqual([line[3:-1] for line in inventory.splitlines() if line.startswith("- `")], included)
        self.assertIn(f"Includes {len(included)} maintained", result)
        self.assertEqual(build_context.build("all", [], self.root), result)

    def test_all_excludes_outputs_environments_secrets_holdouts_and_binary(self) -> None:
        for relative in (
            "dist/previous.md", ".git/config", "__pycache__/cache.txt",
            ".venv/lib/private.txt", "node_modules/package/index.js", "venv/local.txt",
            "examples/.env.local", ".env.example", "credentials/account.json",
            "secrets.json", ".credentials", "training/holdouts/private.md",
            "training/private_holdout.json", ".aws/config", "key.pem",
            ".pytest_cache/state.txt",
        ):
            self.write(relative, "DO_NOT_EXPORT")
        (self.root / "binary.bin").write_bytes(b"\xff\xfe")
        (self.root / "null.bin").write_bytes(b"binary\x00content")
        result = build_context.build("all", [], self.root)
        self.assertNotIn("DO_NOT_EXPORT", result)
        self.assertNotIn("## Source: binary.bin", result)
        self.assertNotIn("## Source: null.bin", result)
        self.assertIn("WEB_TYPE", result)

    def test_all_rejects_reference_filter(self) -> None:
        with self.assertRaisesRegex(ValueError, "all studies are already included"):
            build_context.build("all", ["alpha"], self.root)

    def test_all_rejects_file_symlink_escaping_repository(self) -> None:
        outside = self.parent / "outside.md"
        outside.write_text("OUTSIDE", encoding="utf-8")
        try:
            (self.root / "linked.md").symlink_to(outside)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Symlink creation unavailable: {exc}")
        with self.assertRaisesRegex(ValueError, "escapes repository"):
            build_context.build("all", [], self.root)

    def test_all_does_not_traverse_directory_symlinks(self) -> None:
        outside = self.parent / "external"
        outside.mkdir()
        (outside / "private.md").write_text("OUTSIDE", encoding="utf-8")
        try:
            (self.root / "external").symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Symlink creation unavailable: {exc}")
        result = build_context.build("all", [], self.root)
        self.assertNotIn("OUTSIDE", result)
        self.assertNotIn("## Source: external/", result)

    def test_repeated_reference_ids_are_deduplicated_in_request_order(self) -> None:
        result = build_context.build("web", ["beta", "alpha", "beta"], self.root)
        self.assertEqual(result.count("ALPHA_STUDY"), 1)
        self.assertEqual(result.count("BETA_STUDY"), 1)
        self.assertLess(result.index("BETA_STUDY"), result.index("ALPHA_STUDY"))

    def test_different_references_to_same_study_do_not_duplicate_content(self) -> None:
        self.catalog[1]["study"] = self.catalog[0]["study"]
        self.write_json("references/catalog.json", self.catalog)
        result = build_context.build("web", ["alpha", "beta"], self.root)
        self.assertEqual(result.count("ALPHA_STUDY"), 1)

    def test_unknown_reference_and_track_fail(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown reference"):
            build_context.build("web", ["unknown"], self.root)
        with self.assertRaisesRegex(ValueError, "Track"):
            build_context.build("rust", [], self.root)

    def test_missing_source_fails_instead_of_emitting_partial_bundle(self) -> None:
        (self.root / "AGENTS.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing file"):
            build_context.build("python", [], self.root)

    def test_relative_and_absolute_paths_cannot_escape_root(self) -> None:
        outside = self.parent / "outside.md"
        outside.write_text("OUTSIDE", encoding="utf-8")
        for target in ("../outside.md", str(outside)):
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "escapes repository"):
                build_context.within_root(target, self.root)

    def test_catalog_study_traversal_is_rejected(self) -> None:
        (self.parent / "outside.md").write_text("OUTSIDE", encoding="utf-8")
        self.catalog[0]["study"] = "../outside.md"
        self.write_json("references/catalog.json", self.catalog)
        with self.assertRaisesRegex(ValueError, "escapes repository"):
            build_context.build("web", ["alpha"], self.root)

    def test_cli_refuses_overwrite_and_preserves_existing_content(self) -> None:
        existing = self.write("export.md", "KEEP_THIS")
        result = self.cli("build_context.py", "--track", "web", "--out", str(existing))
        self.assertEqual(result.returncode, 2)
        self.assertEqual(existing.read_text(encoding="utf-8"), "KEEP_THIS")
        self.assertNotIn("Wrote", result.stdout)
        self.assertIn("error:", result.stderr)

    def test_cli_writes_requested_new_file(self) -> None:
        output = self.root / "generated" / "context.md"
        result = self.cli("build_context.py", "--track", "python", "--out", str(output))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PYTHON_TYPES", output.read_text(encoding="utf-8"))
        self.assertNotIn("WEB_TYPE", output.read_text(encoding="utf-8"))

    def test_cli_all_exports_complete_context_and_refuses_reference_filter(self) -> None:
        output = self.root / "dist" / "context.md"
        result = self.cli("build_context.py", "--track", "all", "--out", str(output))
        self.assertEqual(result.returncode, 0, result.stderr)
        content = output.read_text(encoding="utf-8")
        self.assertIn("WEB_TYPE", content)
        self.assertIn("PYTHON_TYPES", content)
        self.assertIn("ALPHA_STUDY", content)
        self.assertNotIn("## Source: dist/context.md", content)
        rejected = self.cli("build_context.py", "--track", "all", "--reference", "alpha")
        self.assertEqual(rejected.returncode, 2)
        self.assertIn("all studies are already included", rejected.stderr)


class ValidateRepositoryTests(RepositoryFixture):
    def test_complete_fixture_passes(self) -> None:
        self.assertEqual(validate_repo.validate(self.root), [])

    def test_duplicate_reference_id_is_reported(self) -> None:
        self.catalog.append(copy.deepcopy(self.catalog[0]))
        self.write_json("references/catalog.json", self.catalog)
        errors = validate_repo.validate(self.root)
        self.assertTrue(any("Duplicate reference ID" in error for error in errors))

    def test_bad_reference_fields_and_shapes_are_reported(self) -> None:
        for key, value in (
            ("id", "Bad ID"), ("name", ""), ("url", "http://example.com"),
            ("origin", "guess"), ("status", "verified"),
            ("reviewed_at", "not-a-date"), ("tags", "editorial"),
        ):
            catalog = copy.deepcopy(self.catalog)
            catalog[0][key] = value
            self.write_json("references/catalog.json", catalog)
            with self.subTest(key=key):
                self.assertTrue(validate_repo.validate(self.root))
        for catalog in ({}, None, [None]):
            self.write_json("references/catalog.json", catalog)
            with self.subTest(catalog=catalog):
                self.assertTrue(validate_repo.validate(self.root))

    def test_missing_or_outside_studies_are_reported(self) -> None:
        (self.parent / "outside.md").write_text("OUTSIDE", encoding="utf-8")
        for target in ("references/missing.md", "../outside.md"):
            self.catalog[0]["study"] = target
            self.write_json("references/catalog.json", self.catalog)
            with self.subTest(target=target):
                self.assertTrue(any("study missing or outside" in error for error in validate_repo.validate(self.root)))

    def test_missing_local_links_and_traversal_are_reported(self) -> None:
        (self.parent / "outside.md").write_text("OUTSIDE", encoding="utf-8")
        self.write("README.md", "[missing](missing.md)\n[outside](../outside.md)")
        errors = validate_repo.validate(self.root)
        self.assertTrue(any("missing.md" in error for error in errors))
        self.assertTrue(any("../outside.md" in error for error in errors))

    def test_valid_local_fragment_and_url_links_pass(self) -> None:
        self.write("notes with spaces.md", "# Notes")
        self.write("README.md", (
            "[local](AGENTS.md#instructions)\n"
            "[encoded](notes%20with%20spaces.md)\n"
            "[angle](<notes with spaces.md>)\n"
            "[titled](AGENTS.md \"Agent instructions\")\n"
            "[web](https://example.com/missing)\n"
            "[heading](#heading)\n"
            "```md\n[code-example](not-a-real-file.md)\n```"
        ))
        self.assertEqual(validate_repo.validate(self.root), [])

    def test_missing_angle_bracket_target_with_spaces_is_reported(self) -> None:
        self.write("README.md", "[missing](<missing file.md>)")
        self.assertTrue(any("missing file.md" in error for error in validate_repo.validate(self.root)))

    def test_missing_link_with_title_is_reported(self) -> None:
        for title in ('"Title"', "'Title'", "(Title)"):
            self.write("README.md", f"[missing](missing.md {title})")
            with self.subTest(title=title):
                self.assertTrue(any("missing.md" in error for error in validate_repo.validate(self.root)))

    def test_duplicate_evaluation_task_ids_are_reported(self) -> None:
        self.tasks.append(copy.deepcopy(self.tasks[0]))
        self.write_json("evals/tasks.json", self.tasks)
        self.assertTrue(any("Duplicate evaluation task IDs" in error for error in validate_repo.validate(self.root)))

    def test_unreadable_markdown_is_reported_instead_of_crashing(self) -> None:
        (self.root / "README.md").write_bytes(b"\xff\xfe")
        self.assertTrue(any("cannot read Markdown" in error for error in validate_repo.validate(self.root)))

    def test_malformed_link_is_reported_instead_of_crashing(self) -> None:
        self.write("README.md", "[bad](https://[invalid)")
        self.assertTrue(any("malformed link" in error for error in validate_repo.validate(self.root)))

    def test_evaluation_task_container_and_fields_are_validated(self) -> None:
        cases = ({}, None, [], [{"id": "x", "track": "web", "prompt": 42, "checks": "yes"}])
        for value in cases:
            self.write_json("evals/tasks.json", value)
            with self.subTest(value=value):
                self.assertTrue(validate_repo.validate(self.root))
        for key, value in (("id", ""), ("prompt", "  "), ("checks", [""]), ("checks", [42])):
            tasks = copy.deepcopy(self.tasks)
            tasks[0][key] = value
            self.write_json("evals/tasks.json", tasks)
            with self.subTest(key=key, value=value):
                self.assertTrue(validate_repo.validate(self.root))

    def test_cli_reports_validation_failure_on_stderr(self) -> None:
        self.write("README.md", "[missing](absent.md)")
        result = self.cli("validate_repo.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("absent.md", result.stderr)
        self.assertNotIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
