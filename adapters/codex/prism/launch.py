#!/usr/bin/env python3
"""Launch Mentor's dedicated Prism storage over stdio with no host port or credentials."""

import argparse
import os
import re
import shutil
import sys

IMAGE = 'mentor-prism:20.21.17'
VOLUME = 'mentor-prism-data'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--volume', default=VOLUME)
    parser.add_argument('--image', default=IMAGE)
    args = parser.parse_args()
    try:
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', args.volume):
            raise ValueError('volume must be a Docker volume name, not a filesystem path')
        docker = shutil.which('docker')
        if not docker:
            raise ValueError('Docker is unavailable; start Docker to use isolated Mentor memory')
        # Do not inherit cloud credentials or mount the host's Prism directory.
        # The isolated network also prevents backend reconciliation with Workflow.
        command = [docker, 'run', '--rm', '-i', '--network', 'none',
                   '--mount', f'type=volume,source={args.volume},target=/root/.prism-mcp',
                   '--env', 'PRISM_STORAGE=local', args.image]
        os.execv(docker, command)
    except (OSError, ValueError) as error:
        print(f'Mentor Prism unavailable: {error}. Use local docs; do not fall back to shared memory.', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
