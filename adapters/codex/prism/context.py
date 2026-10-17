#!/usr/bin/env python3
"""Prepare project-scoped calls for an existing Prism MCP connection; never launch it."""

import argparse
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tomllib

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from runtime.preferences import resolve_project


def guidance_paths(workspace):
    """Expose optional resources without loading memory or requiring a server."""
    handler = Path(__file__).resolve()
    guide = handler.with_name('README.md')
    if not guide.is_file():
        return {'prism_warning': 'Optional Prism guide unavailable; use local docs and ordinary tools.'}
    return {'prism_command': shlex.join([sys.executable, str(handler), '--workspace', str(workspace)]),
            'prism_guidance_path': str(guide),
            'mcp_setup_command': shlex.join([sys.executable, str(handler.parent.parent / 'setup_mcp.py'),
                '--workspace', str(workspace), '--codex-home',
                str(Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')))])}


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a nonempty string')
    return value


def strings(value, label):
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError(f'{label} must be an array of strings')
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    actions = parser.add_subparsers(dest='action', required=True)
    inspect = actions.add_parser('inspect')
    inspect.add_argument('--config', default=str(Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'config.toml'))
    inspect.add_argument('--connected-server', action='append', default=[])
    setup = actions.add_parser('setup')
    setup.add_argument('--codex-home', default=os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    setup.add_argument('--connected-server', action='append', default=[])
    setup.add_argument('--apply', action='store_true')
    setup.add_argument('--prism-memory', choices=('separate', 'shared'), default='separate')
    load = actions.add_parser('load')
    load.add_argument('--project', required=True)
    load.add_argument('--conversation-id', required=True)
    load.add_argument('--server-name', required=True, help='Actual dedicated Mentor connection name')
    save = actions.add_parser('save')
    save.add_argument('--session', required=True, help='Binding from load, with the observed expected_version added')
    args = parser.parse_args()
    try:
        workspace = Path(args.workspace)
        if not workspace.is_absolute() or not workspace.is_dir():
            raise ValueError('workspace must be an existing absolute directory')
        if args.action == 'setup':
            command = [sys.executable, str(Path(__file__).resolve().parent.parent / 'setup_mcp.py'),
                       '--workspace', str(workspace), '--codex-home', args.codex_home, '--server', 'prism',
                       '--prism-memory', args.prism_memory]
            for name in args.connected_server:
                command += ['--connected-prism', name]
            if args.apply:
                command.append('--apply')
            return subprocess.call(command)
        workspace_id = resolve_project(args.workspace)
        if args.action == 'inspect':
            path = Path(args.config)
            settings = tomllib.loads(path.read_text()) if path.exists() else {}
            servers = settings.get('mcp_servers', {})
            if not isinstance(servers, dict):
                raise ValueError('mcp_servers must be a table')
            registrations = []
            for name, entry in servers.items():
                if not isinstance(entry, dict):
                    raise ValueError('MCP registrations must be tables')
                # Host aliases need not contain "prism". Inspect the launcher too;
                # registration evidence still cannot prove live tool delivery.
                launch = str(entry.get('command', '')) + ' ' + str(entry.get('args', []))
                if ('prism' in name.lower() or 'prism-mcp-server' in launch.lower()
                        or '/prism/launch.py' in launch):
                    package = re.search(r'prism-mcp-server(?:@[\w.\-]+)?', launch)
                    registrations.append({'name': name, 'enabled': entry.get('enabled', True),
                                          'transport': 'http' if entry.get('url') else 'stdio',
                                          'declared_package': package.group() if package else None})
            names = sorted({item['name'] for item in registrations} | set(args.connected_server))
            result = {'registered_names': names, 'registrations': registrations,
                      'action': 'inspect-and-reuse' if names else 'ordinary-tool-fallback',
                      'live_connection_verified': False, 'server_started': False}
        else:
            if args.action == 'load':
                session = {'workspace_id': workspace_id,
                           'project': nonempty(args.project, 'Prism project'),
                           'conversation_id': nonempty(args.conversation_id, 'conversation_id'),
                           'server_name': nonempty(args.server_name, 'server_name')}
                requests = [{'server': session['server_name'], 'tool': 'session_load_context', 'arguments': {
                    'project': session['project'], 'conversation_id': session['conversation_id'],
                    'max_tokens': 2000, 'toolAction': 'Loading project context',
                    'toolSummary': 'Mentor project handoff'}}]
            else:
                session = json.loads(args.session)
                if not isinstance(session, dict) or session.get('workspace_id') != workspace_id:
                    raise ValueError('Prism binding belongs to another project/workspace')
                project = nonempty(session.get('project'), 'Prism project')
                conversation = nonempty(session.get('conversation_id'), 'conversation_id')
                server_name = nonempty(session.get('server_name'), 'server_name')
                # Null is allowed only when the actual fresh load supplied no
                # version. Missing metadata must never become an invented zero.
                if 'expected_version' not in session:
                    raise ValueError('record the loaded expected_version (null only if none was returned)')
                version = session['expected_version']
                if version is not None and (type(version) is not int or version < 0):
                    raise ValueError('expected_version must be null or a nonnegative integer')
                record = json.load(sys.stdin)
                allowed = {'summary', 'todos', 'decisions', 'files_changed', 'active_branch', 'key_context'}
                if not isinstance(record, dict) or set(record) - allowed:
                    raise ValueError('record accepts project summary, todos, decisions, files_changed, active_branch and key_context only')
                summary = nonempty(record.get('summary'), 'summary')
                arrays = {key: strings(record.get(key, []), key) for key in ('todos', 'decisions', 'files_changed')}
                handoff = {'project': project, 'conversation_id': conversation,
                           'last_summary': summary, 'open_todos': arrays['todos'], 'disable_merge': True}
                for field in ('active_branch', 'key_context'):
                    if field in record:
                        handoff[field] = nonempty(record[field], field)
                if version is not None:
                    handoff['expected_version'] = version
                requests = [
                    {'server': server_name, 'tool': 'session_save_ledger', 'arguments': {
                        'project': project, 'conversation_id': conversation, 'summary': summary, **arrays}},
                    {'server': server_name, 'tool': 'session_save_handoff', 'arguments': handoff},
                ]
            result = {'session': session, 'requests': requests, 'executed': False,
                      'guidance_path': str(Path(__file__).with_name('README.md'))}
    except (OSError, UnicodeError, ValueError, TypeError, RuntimeError, subprocess.SubprocessError) as error:
        print(f'Prism context unavailable: {error}; continue Mentor with local docs and ordinary tools.', file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write('\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
