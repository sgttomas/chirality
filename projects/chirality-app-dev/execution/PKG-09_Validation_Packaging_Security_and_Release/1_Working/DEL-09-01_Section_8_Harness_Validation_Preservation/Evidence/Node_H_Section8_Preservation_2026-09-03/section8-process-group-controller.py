#!/usr/bin/env python3
"""Anchor and continuously audit one proof process tree on macOS.

The controller becomes a session/process-group leader and launches the proof
command into that group. It retains the group identity until teardown, while
an independent libproc inventory continuously follows descendants by stable
PID/start-time identity. Any descendant that leaves the anchored group makes
the no-detach contract permanently fail closed. The controller never signals
an individual PID; the shell may only signal the kernel-owned anchored group.

macOS has no unprivileged cgroup/pidfd equivalent that can forcibly contain a
descendant after setsid(2). This helper therefore does not claim to contain an
escapee. It makes escape an observed, durable cleanup failure. The recorded
proof is accepted only when the application disables its known detach route
and this audit remains ``ok`` for the complete controlled lifetime.
"""

from __future__ import annotations

import argparse
import ctypes
from dataclasses import dataclass
import json
import os
from pathlib import Path
import signal
import subprocess
import time
from typing import Any


PROC_ALL_PIDS = 1
PROC_PIDTBSDINFO = 3


class ProcBSDInfo(ctypes.Structure):
    _fields_ = [
        ("pbi_flags", ctypes.c_uint32),
        ("pbi_status", ctypes.c_uint32),
        ("pbi_xstatus", ctypes.c_uint32),
        ("pbi_pid", ctypes.c_uint32),
        ("pbi_ppid", ctypes.c_uint32),
        ("pbi_uid", ctypes.c_uint32),
        ("pbi_gid", ctypes.c_uint32),
        ("pbi_ruid", ctypes.c_uint32),
        ("pbi_rgid", ctypes.c_uint32),
        ("pbi_svuid", ctypes.c_uint32),
        ("pbi_svgid", ctypes.c_uint32),
        ("rfu_1", ctypes.c_uint32),
        ("pbi_comm", ctypes.c_char * 16),
        ("pbi_name", ctypes.c_char * 32),
        ("pbi_nfiles", ctypes.c_uint32),
        ("pbi_pgid", ctypes.c_uint32),
        ("pbi_pjobc", ctypes.c_uint32),
        ("e_tdev", ctypes.c_uint32),
        ("e_tpgid", ctypes.c_uint32),
        ("pbi_nice", ctypes.c_int32),
        ("pbi_start_tvsec", ctypes.c_uint64),
        ("pbi_start_tvusec", ctypes.c_uint64),
    ]


@dataclass(frozen=True)
class ProcessIdentity:
    pid: int
    ppid: int
    pgid: int
    start_sec: int
    start_usec: int
    command: str

    @property
    def stable_key(self) -> tuple[int, int, int]:
        return (self.pid, self.start_sec, self.start_usec)

    def as_json(self) -> dict[str, Any]:
        return {
            "pid": self.pid,
            "ppid": self.ppid,
            "pgid": self.pgid,
            "startSec": self.start_sec,
            "startUsec": self.start_usec,
            "command": self.command,
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ready-file", required=True)
    parser.add_argument("--audit-file", required=True)
    parser.add_argument("--sample-interval", type=float, default=0.02)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command[:1] == ["--"]:
        args.command = args.command[1:]
    if not args.command:
        parser.error("a command is required after --")
    if args.sample_interval <= 0:
        parser.error("--sample-interval must be positive")
    return args


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    temporary_path.write_text(
        json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(temporary_path, path)


def decode_command(raw: bytes) -> str:
    return raw.split(b"\0", 1)[0].decode("utf-8", errors="replace")


class DarwinProcessInventory:
    def __init__(self) -> None:
        self.libproc = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
        self.libproc.proc_listpids.argtypes = [
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_void_p,
            ctypes.c_int,
        ]
        self.libproc.proc_listpids.restype = ctypes.c_int
        self.libproc.proc_pidinfo.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_uint64,
            ctypes.c_void_p,
            ctypes.c_int,
        ]
        self.libproc.proc_pidinfo.restype = ctypes.c_int

    def snapshot(self) -> dict[int, ProcessIdentity]:
        required = self.libproc.proc_listpids(PROC_ALL_PIDS, 0, None, 0)
        if required <= 0:
            error = ctypes.get_errno()
            raise OSError(error, "proc_listpids size query failed")
        # Leave headroom for forks between the size query and population call.
        capacity = max(required // ctypes.sizeof(ctypes.c_int) + 256, 1024)
        buffer = (ctypes.c_int * capacity)()
        used = self.libproc.proc_listpids(
            PROC_ALL_PIDS, 0, buffer, ctypes.sizeof(buffer)
        )
        if used <= 0:
            error = ctypes.get_errno()
            raise OSError(error, "proc_listpids inventory failed")

        result: dict[int, ProcessIdentity] = {}
        for pid in buffer[: used // ctypes.sizeof(ctypes.c_int)]:
            if pid <= 0:
                continue
            info = ProcBSDInfo()
            read = self.libproc.proc_pidinfo(
                pid,
                PROC_PIDTBSDINFO,
                0,
                ctypes.byref(info),
                ctypes.sizeof(info),
            )
            # A process may exit between the list and detail calls. A live
            # controlled process is checked explicitly below; unrelated churn
            # is not an inspection failure.
            if read != ctypes.sizeof(info):
                continue
            result[pid] = ProcessIdentity(
                pid=int(info.pbi_pid),
                ppid=int(info.pbi_ppid),
                pgid=int(info.pbi_pgid),
                start_sec=int(info.pbi_start_tvsec),
                start_usec=int(info.pbi_start_tvusec),
                command=decode_command(bytes(info.pbi_comm)),
            )
        return result


def descendant_closure(
    processes: dict[int, ProcessIdentity], roots: set[int]
) -> set[int]:
    controlled = set(roots)
    changed = True
    while changed:
        changed = False
        for process in processes.values():
            if process.pid not in controlled and process.ppid in controlled:
                controlled.add(process.pid)
                changed = True
    return controlled


def main() -> int:
    args = parse_args()
    ready_path = Path(args.ready_file)
    audit_path = Path(args.audit_file)
    ready_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.parent.mkdir(parents=True, exist_ok=True)

    os.setsid()
    controller_pid = os.getpid()
    process_group_id = os.getpgrp()

    # A caught handler is reset across exec, so the launched command receives
    # TERM normally while this anchor remains available for the final KILL.
    signal.signal(signal.SIGTERM, lambda _signum, _frame: None)
    child = subprocess.Popen(args.command)
    inventory = DarwinProcessInventory()
    tracked: dict[tuple[int, int, int], ProcessIdentity] = {}
    violations: list[dict[str, Any]] = []
    samples = 0
    max_descendants = 0

    ready_payload = {
        "schema": "chirality-section8-process-group/v2",
        "controllerPid": controller_pid,
        "processGroupId": process_group_id,
        "childPid": child.pid,
        "auditFile": str(audit_path),
        "contract": "all-controlled-descendants-remain-in-anchored-process-group",
    }
    atomic_write_json(ready_path, ready_payload)

    while True:
        try:
            processes = inventory.snapshot()
            controller = processes.get(controller_pid)
            if controller is None or controller.pgid != process_group_id:
                raise RuntimeError("controller identity/process-group inspection failed")

            # Stable tracked identities remain controlled even if a process has
            # been reparented. This preserves an observed escape in the ledger
            # without ever making its bare PID a signal target.
            live_tracked_roots = {
                identity.pid
                for key, identity in tracked.items()
                if (current := processes.get(identity.pid)) is not None
                and current.stable_key == key
            }
            controlled_pids = descendant_closure(
                processes, {controller_pid, *live_tracked_roots}
            )
            controlled_pids.discard(controller_pid)

            for pid in sorted(controlled_pids):
                identity = processes[pid]
                tracked.setdefault(identity.stable_key, identity)
                if identity.pgid != process_group_id:
                    violation = identity.as_json()
                    if violation not in violations:
                        violations.append(violation)

            child_process = processes.get(child.pid)
            if child.poll() is None and child_process is None:
                raise RuntimeError("live direct child could not be inspected")

            samples += 1
            max_descendants = max(max_descendants, len(controlled_pids))
            live_controlled = [processes[pid] for pid in sorted(controlled_pids)]
            state = "violation" if violations else "ok"
            audit_payload: dict[str, Any] = {
                "schema": "chirality-section8-descendant-audit/v1",
                "state": state,
                "controllerPid": controller_pid,
                "processGroupId": process_group_id,
                "directChildPid": child.pid,
                "samples": samples,
                "sampleIntervalSeconds": args.sample_interval,
                "maxDescendantsObserved": max_descendants,
                "liveControlled": [item.as_json() for item in live_controlled],
                "violations": violations,
            }
        except Exception as error:  # fail closed and keep the anchor alive
            samples += 1
            audit_payload = {
                "schema": "chirality-section8-descendant-audit/v1",
                "state": "inspection-error",
                "controllerPid": controller_pid,
                "processGroupId": process_group_id,
                "directChildPid": child.pid,
                "samples": samples,
                "sampleIntervalSeconds": args.sample_interval,
                "maxDescendantsObserved": max_descendants,
                "liveControlled": [],
                "violations": violations,
                "error": f"{type(error).__name__}: {error}",
            }
        atomic_write_json(audit_path, audit_payload)
        child.poll()
        time.sleep(args.sample_interval)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
