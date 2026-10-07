#!/usr/bin/env python3
"""Inspect registration or print an opt-in snippet; never overwrite host configuration."""
import argparse
import json
from pathlib import Path
import sys
import tomllib


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    parser.add_argument('--config', default=str(Path.home() / '.codex/config.toml'))
    parser.add_argument('--executable', default='serena')
    args = parser.parse_args()
    try:
        workspace = Path(args.workspace)
        if not workspace.is_absolute() or not workspace.is_dir():
            raise ValueError('workspace must be an existing absolute directory')
        configuration = Path(args.config)
        settings = tomllib.loads(configuration.read_text()) if configuration.exists() else {}
        registered = [name for name in settings.get('mcp_servers', {}) if 'serena' in name.lower()]
        if registered:
            print(json.dumps({'registered_names': registered, 'action': 'inspect-and-reuse',
                'live_connection_verified': False,
                'next': 'Verify exposed tools, activate the selected project, disable memory/onboarding and editing, then use read-only symbols/references. Do not add a duplicate registration.'}))
            return 0
        launcher = Path(__file__).resolve().with_name('launch.py')
        print('# Opt-in example only: review in the host, then verify actual delivery.')
        print('[mcp_servers.mentor_serena]')
        print('command = ' + json.dumps(sys.executable))
        print('args = ' + json.dumps([str(launcher), '--workspace', str(workspace.resolve()), '--executable', args.executable]))
    except (OSError, ValueError) as error:
        print(f'Serena setup failed: {error}; retain ordinary-tool fallback.', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
