#!/usr/bin/env python3
"""Infrastructure management scripts."""

import subprocess
import sys


def docker_up():
    """Start Docker infrastructure."""
    try:
        subprocess.run(["docker", "compose", "up", "-d"], check=True)
        print("✅ Docker infrastructure started")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start infrastructure: {e}")
        sys.exit(1)


def docker_down():
    """Stop Docker infrastructure."""
    try:
        subprocess.run(["docker", "compose", "stop"], check=True)
        print("✅ Docker infrastructure stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to stop infrastructure: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "down":
        docker_down()
    else:
        docker_up()
