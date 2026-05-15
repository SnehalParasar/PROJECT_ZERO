"""Remediation stub for command injection in POST /run."""

import shlex
import subprocess


def run_safe_command(command: str) -> str:
    """Run command without shell=True; reject metacharacters."""
    if any(c in command for c in ';|&$`<>\n'):
        raise ValueError("Unsafe characters in command")
    args = shlex.split(command)
    return subprocess.check_output(args, text=True)
