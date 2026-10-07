"""Shared context boundary for explicit review, feedback and PR-check wrappers."""

import argparse
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))
from runtime.preferences import PreferenceStore, control, resolve_data_root, resolve_project
from adapters.codex.prism.context import guidance_paths

WORKFLOWS = {
    'review': 'review.md',
    'feedback': 'feedback.md',
    'pr-check': 'pr-understanding.md',
}


def main(kind: str) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    parser.add_argument('--data-root')
    parser.add_argument('--session', default='{}')
    args = parser.parse_args()
    try:
        if not Path(args.workspace).is_absolute():
            raise ValueError('workspace must be absolute')
        project_id = resolve_project(args.workspace)
        # Prefer the hook-pinned root so host and explicit skill share storage.
        configured = args.data_root
        if configured is None:
            configured = os.environ.get('MENTOR_DATA_DIR', str(Path.home() / '.mentor'))
        data_root = str(resolve_data_root(configured))
        adapter = REPOSITORY / 'adapters/codex'
        resources = {
            'policy_path': REPOSITORY / 'core/policy.md',
            'workflow_path': REPOSITORY / 'core/workflows' / WORKFLOWS[kind],
        }
        for path in resources.values():
            if not path.read_text(encoding='utf-8').strip():
                raise ValueError(f'Mentor resource is empty: {path}')
        for entry in ('control.py', 'reports.py', 'review_target.py'):
            if not (adapter / entry).is_file():
                raise ValueError(f'Mentor adapter resource is missing: {entry}')
        status = control(PreferenceStore(data_root, project_id), session=json.loads(args.session))
        locations = ['--project-id', project_id, '--data-root', data_root]
        result = {
            **{name: str(path) for name, path in resources.items()},
            'workspace': str(Path(args.workspace).resolve()),
            'project_id': project_id,
            'data_root': data_root,
            'status': status,
            'control_command': shlex.join([sys.executable, str(adapter / 'control.py'), *locations]),
            'report_command': shlex.join([sys.executable, str(adapter / 'reports.py'), *locations, '--kind', kind]),
            'target_command': shlex.join([sys.executable, str(adapter / 'review_target.py')]),
            **guidance_paths(args.workspace),
        }
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, RuntimeError,
            subprocess.SubprocessError) as error:
        print(f'Mentor {kind} context failed: {error}', file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write('\n')
    return 0
