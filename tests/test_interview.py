"""Executable skill context and artifact contracts; conduct needs native evidence."""

import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

from runtime.preferences import PreferenceStore, resolve_project


REPOSITORY = Path(__file__).resolve().parents[1]


class InterviewContractTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="mentor-interview-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.checkout = self.root / "Mentor's $checkout"
        for folder in ("core", "runtime", "adapters"):
            shutil.copytree(REPOSITORY / folder, self.checkout / folder)
        self.workspace = self.root / "learner workspace"
        self.workspace.mkdir()
        self.data = self.root / "local $data"
        self.project_id = resolve_project(str(self.workspace))
        self.skill = self.workspace / ".agents" / "skills" / "mentor-interview"
        self.skill.parent.mkdir(parents=True)
        self.skill.symlink_to(self.checkout / "adapters/codex/skills/mentor-interview", target_is_directory=True)

    def context(self, session=None, data=None):
        return subprocess.run([
            sys.executable, str(self.skill / "scripts/context.py"),
            "--workspace", str(self.workspace), "--data-root", str(data or self.data),
            "--session", json.dumps(session if session is not None else {}),
        ], cwd=self.root, capture_output=True, text=True)

    def artifacts(self, *arguments, text="", check=True, command=None):
        if command is None:
            command = json.loads(self.context().stdout)["artifact_command"]
        result = subprocess.run(shlex.split(command) + list(arguments),
                                cwd=self.root, input=text, capture_output=True, text=True)
        if check:
            self.assertEqual(result.returncode, 0, result.stderr)
            return Path(json.loads(result.stdout)["path"])
        return result

    def test_symlinked_native_entry_preserves_session_and_saved_state_without_writes(self):
        # Saved defaults differ from session overrides: invocation must not flatten them.
        self.assertEqual(self.context().returncode, 0)
        self.assertFalse(self.data.exists())
        preferences = PreferenceStore(str(self.data), self.project_id)
        preferences.write({"level": "junior", "coaching_enabled": True, "coding_mode": "assisted"})
        saved = preferences.path.read_bytes()
        session = {"overrides": {"level": "senior", "coaching_enabled": False,
                                 "coding_mode": "manual"}, "unsaved": []}
        workflow = self.checkout / "core/workflows/interview.md"
        workflow.write_text("Current relocated workflow: café", encoding="utf-8")
        result = self.context(session)
        self.assertEqual(result.returncode, 0, result.stderr)
        context = json.loads(result.stdout)
        self.assertEqual(Path(context["workflow_path"]).read_text(), "Current relocated workflow: café")
        self.assertEqual(context["status"]["session"], session)
        self.assertEqual(context["status"]["effective"], {"level": "senior", "coaching_enabled": False,
                                                        "coding_mode": "manual"})
        self.assertEqual(preferences.path.read_bytes(), saved)
        self.assertFalse((preferences.path.parent / "plans").exists())
        # Execute the shell-quoted command from another cwd with no hook environment.
        result = subprocess.run(context["control_command"] + " --session '{}' status",
                                shell=True, cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["effective"], {"level": "junior", "coaching_enabled": True,
                                                               "coding_mode": "assisted"})

    def test_context_resource_and_configuration_failures_supply_no_success_result(self):
        for name in ("core/policy.md", "core/workflows/interview.md"):
            resource = self.checkout / name
            original = resource.read_bytes()
            for content in (None, b"  \n", b"\xff"):
                with self.subTest(resource=name, content=content):
                    resource.unlink(missing_ok=True)
                    if content is not None:
                        resource.write_bytes(content)
                    result = self.context()
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, "")
                    self.assertIn("failed", result.stderr)
            resource.write_bytes(original)
        for result in (self.context(data="relative"), self.context(session={"overrides": {"level": "automatic"}})):
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
        self.assertFalse(self.data.exists())

    def test_artifacts_reserve_collisions_append_answers_and_finalize_a_confirmed_plan(self):
        first = self.artifacts("create", "--task", "Net spending / May")
        second = self.artifacts("create", "--task", "Net spending / May")
        self.assertNotEqual(first, second)
        self.assertEqual(first.parent, self.data.resolve() / "projects" / self.project_id / "plans")
        initial = (first / "interview.md").read_bytes()
        self.artifacts("append", "--directory", str(first), text="Original: `--slim` 30 min\nQuestion: refunds?\nAnswer: net spending.")
        record = (first / "interview.md").read_text()
        self.assertTrue(record.startswith(initial.decode()))
        self.assertIn("Answer: net spending.", record)
        plan = "# Confirmed plan\nScope: calculation only.\nChecks: next month excluded.\nInterview: [record](interview.md)\n"
        output = self.artifacts("finalize", "--directory", str(first), "--confirmation", "Yes, calculation only.", text=plan)
        self.assertEqual(output.read_text(), plan)
        self.assertIn("Yes, calculation only.", (first / "interview.md").read_text())
        self.assertEqual((second / "interview.md").read_bytes(), initial)
        self.assertFalse((first.parent.parent / "preferences.json").exists())

    def test_failed_writes_and_cross_project_paths_do_not_report_saved_artifacts(self):
        directory = self.artifacts("create", "--task", "Failures")
        initial = (directory / "interview.md").read_bytes()
        for args, content in [
            (("append", "--directory", str(directory)), " "),
            (("finalize", "--directory", str(directory), "--confirmation", ""), "# Plan"),
            (("append", "--directory", str(self.workspace)), "Outside project"),
        ]:
            with self.subTest(args=args):
                result = self.artifacts(*args, text=content, check=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("failed", result.stderr)
        self.assertEqual((directory / "interview.md").read_bytes(), initial)
        # A real filesystem failure after transcript persistence leaves no success claim.
        (directory / "plan.md").mkdir()
        result = self.artifacts("finalize", "--directory", str(directory),
                                "--confirmation", "Approved", text="# Plan", check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("Approved", (directory / "interview.md").read_text())
        (directory / "plan.md").rmdir()
        self.artifacts("finalize", "--directory", str(directory),
                       "--confirmation", "Approved", text="# Recovered plan")
        self.assertEqual((directory / "plan.md").read_text(), "# Recovered plan")
        blocked = self.root / "blocked-data"
        blocked.write_text("existing file")
        command = json.loads(self.context(data=blocked).stdout)["artifact_command"]
        result = self.artifacts("create", "--task", "Cannot save", check=False, command=command)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertEqual(blocked.read_text(), "existing file")


if __name__ == "__main__":
    unittest.main()
