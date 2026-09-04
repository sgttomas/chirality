#!/usr/bin/env python3
"""Anchor one proof process tree in a non-reusable POSIX process group.

The controller becomes a session/process-group leader, launches the requested
command into that group, ignores SIGTERM itself, and remains alive even when
the command exits. The parent shell deliberately retains this child without
waiting until cleanup has atomically signalled the whole group. Consequently
the controller PID/PGID cannot be reallocated across the TERM/KILL boundary.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ready-file", required=True)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command[:1] == ["--"]:
        args.command = args.command[1:]
    if not args.command:
        parser.error("a command is required after --")
    return args


def main() -> int:
    args = parse_args()
    ready_path = Path(args.ready_file)
    ready_path.parent.mkdir(parents=True, exist_ok=True)

    os.setsid()

    # A caught signal handler is reset to the default disposition across exec,
    # so the launched command receives TERM normally while this anchor remains.
    signal.signal(signal.SIGTERM, lambda _signum, _frame: None)
    child = subprocess.Popen(args.command)

    payload = {
        "schema": "chirality-section8-process-group/v1",
        "controllerPid": os.getpid(),
        "processGroupId": os.getpgrp(),
        "childPid": child.pid,
    }
    temporary_path = ready_path.with_suffix(ready_path.suffix + ".tmp")
    temporary_path.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary_path, ready_path)

    # Polling reaps the direct command if it exits, but the controller remains
    # as the live PGID anchor until the parent atomically kills the whole group.
    while True:
        child.poll()
        time.sleep(1)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
