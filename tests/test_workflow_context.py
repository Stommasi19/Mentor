"""Native wrapper process boundaries, including relocation and preserved state."""

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


class WorkflowContextTests(unittest.TestCase):
    def test_relocated_symlink_wrappers_retain_preferences_and_deliver_usable_commands(self):
        with tempfile.TemporaryDirectory(prefix='mentor-workflows-') as tmp:
            root = Path(tmp).resolve()
            checkout = root / "Mentor's $checkout"
            for folder in ('core', 'runtime', 'adapters'):
                shutil.copytree(REPOSITORY / folder, checkout / folder)
            workspace = root / 'learner workspace'
            workspace.mkdir()
            data = root / 'data'
            project_id = resolve_project(str(workspace))
            store = PreferenceStore(str(data), project_id)
            store.write({'level': 'junior', 'coaching_enabled': True})
            original = store.path.read_bytes()
            session = {'overrides': {'level': 'senior', 'coaching_enabled': False}, 'unsaved': []}
            for name, kind, filename in (('mentor-review', 'review', 'review.md'),
                    ('mentor-feedback', 'feedback', 'feedback.md'),
                    ('mentor-pr-check', 'pr-check', 'pr-understanding.md')):
                with self.subTest(name=name):
                    skill = root / name
                    skill.symlink_to(checkout / 'adapters/codex/skills' / name, target_is_directory=True)
                    command = [sys.executable, str(skill / 'scripts/context.py'), '--workspace', str(workspace),
                               '--data-root', str(data), '--session', json.dumps(session)]
                    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    context = json.loads(result.stdout)
                    self.assertEqual(context['status']['session'], session)
                    self.assertEqual(context['status']['saved']['level'], 'junior')
                    self.assertEqual(Path(context['workflow_path']), checkout / 'core/workflows' / filename)
                    created = subprocess.run(shlex.split(context['report_command']) + ['create', '--task', 'Native context'],
                                             cwd=root, capture_output=True, text=True)
                    self.assertEqual(created.returncode, 0, created.stderr)
                    directory = json.loads(created.stdout)['path']
                    saved = subprocess.run(shlex.split(context['report_command']) + ['save', '--directory', directory],
                                           input='# Actual evidence\n', cwd=root, capture_output=True, text=True)
                    self.assertEqual(saved.returncode, 0, saved.stderr)
                    self.assertEqual(store.path.read_bytes(), original)
                    # Missing workflow must fail before a session can act on stale guidance.
                    (checkout / 'core/workflows' / filename).unlink()
                    failed = subprocess.run(command, cwd=root, capture_output=True, text=True)
                    self.assertNotEqual(failed.returncode, 0)
                    self.assertEqual(failed.stdout, '')


if __name__ == '__main__':
    unittest.main()
