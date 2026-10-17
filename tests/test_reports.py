"""Reports through real CLI processes: preservation, isolation and filesystem failures."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ENTRY = Path(__file__).resolve().parents[1] / "adapters/codex/reports.py"


class ReportContractTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="mentor-reports-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.data = self.root / "data with spaces"

    def invoke(self, *args, kind="review", project="a" * 64, text="", data=None):
        return subprocess.run([sys.executable, str(ENTRY), "--data-root", str(data or self.data),
            "--project-id", project, "--kind", kind, *args], input=text,
            cwd=self.root, capture_output=True, text=True)

    def create(self, kind="review"):
        result = self.invoke("create", "--task", "May / boundaries", kind=kind)
        self.assertEqual(result.returncode, 0, result.stderr)
        return Path(json.loads(result.stdout)["path"])

    def test_collisions_and_categories_preserve_completed_reports(self):
        for kind, category, filename in (("review", "reviews", "review.md"),
                ("feedback", "feedback", "feedback.md"), ("pr-check", "pr-checks", "pr-check.md")):
            with self.subTest(kind=kind):
                first, second = self.create(kind), self.create(kind)
                self.assertNotEqual(first, second)
                self.assertEqual(first.parent, self.data.resolve() / "projects" / ("a" * 64) / category)
                content = "# Evidence\nActual observation: café, `$(unchanged)`\n"
                saved = self.invoke("save", "--directory", str(first), kind=kind, text=content)
                self.assertEqual(saved.returncode, 0, saved.stderr)
                self.assertTrue(json.loads(saved.stdout)["persisted"])
                self.assertEqual((first / filename).read_text(), content)
                duplicate = self.invoke("save", "--directory", str(first), kind=kind, text="Replacement")
                self.assertNotEqual(duplicate.returncode, 0)
                self.assertEqual(duplicate.stdout, "")
                self.assertEqual((first / filename).read_text(), content)
                self.assertFalse((second / filename).exists())
        self.assertFalse((self.data / "projects" / ("a" * 64) / "preferences.json").exists())

    def test_wrong_project_unreserved_paths_and_redirects_are_rejected(self):
        directory = self.create()
        outside = self.root / "outside"
        outside.mkdir()
        redirected = directory.parent / "redirected"
        redirected.symlink_to(outside, target_is_directory=True)
        unreserved = directory.parent / "unreserved"
        unreserved.mkdir()
        for path, project, text in ((directory, "b" * 64, "Report"),
                (outside, "a" * 64, "Report"), (redirected, "a" * 64, "Report"),
                (unreserved, "a" * 64, "Report"), (directory, "a" * 64, " ")):
            result = self.invoke("save", "--directory", str(path), project=project, text=text)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
        (directory / "review.md").symlink_to(outside / "report.md")
        result = self.invoke("save", "--directory", str(directory), text="Report")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertEqual(self.invoke("create", "--task", "", data="relative").stdout, "")

    def test_real_write_failure_has_no_success_and_allows_retry(self):
        blocked = self.root / "blocked"
        blocked.write_text("Preserve")
        result = self.invoke("create", "--task", "Cannot save", data=blocked)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertEqual(blocked.read_text(), "Preserve")
        if os.geteuid() == 0:
            self.skipTest("OS permission denial requires a non-root user")
        directory = self.create()
        directory.chmod(0o500)
        try:
            failed = self.invoke("save", "--directory", str(directory), text="# Findings")
            self.assertNotEqual(failed.returncode, 0)
            self.assertEqual(failed.stdout, "")
            self.assertFalse((directory / "review.md").exists())
        finally:
            directory.chmod(0o700)
        recovered = self.invoke("save", "--directory", str(directory), text="# Findings")
        self.assertEqual(recovered.returncode, 0, recovered.stderr)


if __name__ == "__main__":
    unittest.main()
