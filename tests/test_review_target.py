"""Real Git scope contracts; PR fixtures exercise transport failures, not live GitHub."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ENTRY = Path(__file__).resolve().parents[1] / 'adapters/codex/review_target.py'
spec = importlib.util.spec_from_file_location('review_target', ENTRY)
targets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(targets)


class LocalSnapshotTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='mentor-target-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.git('init')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        (self.root / 'rule.txt').write_text('original\n')
        (self.root / '[draft].txt').write_text('selected\n')
        (self.root / 'd.txt').write_text('not selected\n')
        self.git('add', '.')
        self.git('commit', '-m', 'baseline')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.root), *args], capture_output=True, check=True).stdout

    def capture(self, scope='uncommitted', *extra):
        result = subprocess.run([sys.executable, str(ENTRY), 'local', '--workspace', str(self.root),
            '--scope', scope, *extra], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_staged_and_worktree_snapshots_distinguish_same_head_and_keep_source(self):
        (self.root / 'rule.txt').write_text('staged\n')
        self.git('add', 'rule.txt')
        (self.root / 'rule.txt').write_text('working\n')
        (self.root / 'new.txt').write_text('untracked\n')
        index = (self.root / '.git/index').read_bytes()
        staged = self.capture('staged')
        working = self.capture('unstaged')
        both = self.capture()
        self.assertEqual(staged['layers'][0]['entries'][0]['after']['text'], 'staged\n')
        self.assertEqual(working['layers'][0]['entries'][0]['before']['text'], 'staged\n')
        self.assertEqual(working['layers'][0]['entries'][0]['after']['text'], 'working\n')
        self.assertIn('new.txt', both['included_paths'])
        self.assertNotEqual(staged['snapshot_id'], working['snapshot_id'])
        (self.root / 'rule.txt').write_text('new working\n')
        changed = self.capture()
        self.assertEqual(changed['head'], both['head'])
        self.assertNotEqual(changed['snapshot_id'], both['snapshot_id'])
        self.assertEqual(staged['snapshot_id'], self.capture('staged')['snapshot_id'])
        self.assertEqual((self.root / '.git/index').read_bytes(), index)
        self.assertEqual((self.root / 'new.txt').read_text(), 'untracked\n')

    def test_literal_selection_modes_renames_deletions_and_untracked_content(self):
        self.git('mv', 'rule.txt', 'renamed.txt')
        (self.root / '[draft].txt').write_text('changed selected\n')
        (self.root / 'd.txt').write_text('changed excluded\n')
        chosen = self.capture('uncommitted', '--path', '[draft].txt')
        self.assertEqual(chosen['included_paths'], ['[draft].txt'])
        rename = self.capture('staged')['layers'][0]['entries'][0]
        self.assertEqual((rename['old_path'], rename['path']), ('rule.txt', 'renamed.txt'))
        self.assertTrue(rename['status'].startswith('R'))
        (self.root / 'renamed.txt').unlink()
        deleted = self.capture('unstaged')['layers'][0]['entries']
        self.assertIsNone(next(item for item in deleted if item['path'] == 'renamed.txt')['after'])
        executable = self.root / 'run.sh'
        executable.write_text('#!/bin/sh\n')
        first = self.capture()
        executable.chmod(0o755)
        self.assertNotEqual(first['snapshot_id'], self.capture()['snapshot_id'])
        (self.root / 'binary').write_bytes(b'\xff\x00')
        (self.root / 'link').symlink_to('not-present')
        entries = self.capture()['layers'][-1]['entries']
        self.assertEqual(next(item for item in entries if item['path'] == 'link')['after']['text'], 'not-present')
        self.assertIn('base64', next(item for item in entries if item['path'] == 'binary')['after'])

    def test_submodule_commit_is_captured_but_dirty_contents_require_separate_target(self):
        module = self.root / 'module'
        module.mkdir()

        def module_git(*args):
            return subprocess.run(['git', '-C', str(module), *args],
                                  capture_output=True, check=True).stdout

        module_git('init')
        module_git('config', 'user.name', 'Test')
        module_git('config', 'user.email', 'test@example.invalid')
        rule = module / 'rule.txt'
        rule.write_text('initial\n')
        module_git('add', '.')
        module_git('commit', '-m', 'initial')
        self.git('add', 'module')
        self.git('commit', '-m', 'track module')
        rule.write_text('committed change\n')
        module_git('commit', '-am', 'module change')
        entry = self.capture('unstaged')['layers'][0]['entries'][0]
        self.assertEqual(entry['after']['submodule_commit'],
                         module_git('rev-parse', 'HEAD').decode().strip())
        index = (self.root / '.git/index').read_bytes()
        rule.write_text('uncommitted change\n')
        failed = subprocess.run([sys.executable, str(ENTRY), 'local', '--workspace',
                                 str(self.root), '--scope', 'unstaged'],
                                capture_output=True, text=True)
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn('dirty submodule requires a separate local target', failed.stderr)
        self.assertEqual(failed.stdout, '')
        self.assertEqual((self.root / '.git/index').read_bytes(), index)
        self.assertEqual(rule.read_text(), 'uncommitted change\n')

    def test_range_and_invalid_targets_do_not_silently_select_working_changes(self):
        base = self.git('rev-parse', 'HEAD').decode().strip()
        (self.root / 'rule.txt').write_text('committed\n')
        self.git('commit', '-am', 'change')
        (self.root / 'rule.txt').write_text('not in range\n')
        result = self.capture('range', '--base', base)
        self.assertEqual(result['layers'][0]['entries'][0]['after']['text'], 'committed\n')
        for extra in ([], ['--base', 'missing'], ['--base', base, '--path', '../outside']):
            failed = subprocess.run([sys.executable, str(ENTRY), 'local', '--workspace', str(self.root),
                '--scope', 'range', *extra], capture_output=True, text=True)
            self.assertNotEqual(failed.returncode, 0)
            self.assertEqual(failed.stdout, '')


class RecordedTransport:
    """Recorded API shapes; no software or live-delivery assertion uses these as receipts."""
    def __init__(self, changed=False, unavailable=False):
        self.calls = 0
        self.changed, self.unavailable = changed, unavailable

    def metadata(self, repository, number):
        self.calls += 1
        if self.unavailable:
            raise OSError('GitHub unavailable')
        return {'number': number, 'changed_files': 1, 'title': 'Boundary fix', 'body': 'Exclusive end',
                'base': {'sha': 'a' * 40, 'repo': {'full_name': repository}},
                'head': {'sha': ('c' if self.changed and self.calls > 1 else 'b') * 40,
                         'repo': {'full_name': 'fork/example'}}}

    def diff(self, repository, number):
        return 'diff --git a/rule.py b/rule.py\n'

    def merge_base(self, repository, base, head, head_repository):
        return 'd' * 40

    def files(self, repository, number):
        return [{'filename': 'rule.py', 'status': 'modified'}]

    def file(self, repository, revision, path):
        return {'text': 'before' if revision == 'd' * 40 else 'after', 'mode': 'remote'}


class PullRequestBoundaryTests(unittest.TestCase):
    def test_pinned_revisions_context_and_fork_identity(self):
        result = targets.capture_pr('https://github.com/owner/example/pull/7', RecordedTransport())
        self.assertEqual(result['base'], 'a' * 40)
        self.assertEqual(result['head'], 'b' * 40)
        self.assertEqual(result['merge_base'], 'd' * 40)
        self.assertEqual(result['head_repository'], 'fork/example')
        self.assertEqual(result['entries'][0]['before']['text'], 'before')
        self.assertEqual(result['entries'][0]['after']['text'], 'after')

    def test_revision_access_and_incomplete_context_errors_are_visible(self):
        for transport in (RecordedTransport(changed=True), RecordedTransport(unavailable=True)):
            with self.assertRaises((ValueError, OSError)):
                targets.capture_pr('https://github.com/owner/example/pull/7', transport)
        for url in ('', 'https://example.com/owner/example/pull/7', 'https://github.com/owner/example/pull/0'):
            with self.assertRaises(ValueError):
                targets.capture_pr(url, RecordedTransport())
        transport = RecordedTransport()
        transport.files = lambda repository, number: []
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            targets.capture_pr('https://github.com/owner/example/pull/7', transport)


if __name__ == '__main__':
    unittest.main()
