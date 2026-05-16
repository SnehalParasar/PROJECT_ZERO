"""
# AUTO-GENERATED PATCH by Project Zero-Day
# Run ID: 4fdf76b0-8b4d-496e-967d-6808d77b6b9d
# Vulnerability: Command Injection
# Original vulnerable code used shell=True with unsanitized input

import subprocess
import shlex

def safe_run_command(user_input: str) -> str:
    # PATCH: Use shlex.split and shell=False to prevent injection
    allowed_commands = ["ls", "whoami", "date"]
    cmd = user_input.strip().split()[0]
    if cmd not in allowed_commands:
        return "Command not permitted"
    args = shlex.split(user_input)
    result = subprocess.check_output(args, shell=False, timeout=5)
    return result.decode()
