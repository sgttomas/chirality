#!/usr/bin/env python3
"""Host-pinned macOS LaunchAgent coalition supervisor for Section 8.

The outer process remains outside the transient LaunchAgent job. launchd gives
that job a distinct resource coalition which ordinary fork/exec, setpgid, and
setsid descendants inherit. Cleanup enumerates the coalition and signals every
member with ``proc_signal_with_audittoken``. The audit token binds PID plus the
kernel pidversion atomically, so PID reuse cannot redirect a signal.

The libproc flavors used here are private Darwin ABI. A behavioral capability
probe is mandatory before the job is created. Any unsupported, missing,
ambiguous, or failed inspection/signal/launchctl operation fails closed.
"""

from __future__ import annotations

import argparse
import ctypes
from dataclasses import dataclass
import errno
import hashlib
import json
import os
from pathlib import Path
import plistlib
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from typing import Any
import uuid


PROC_PIDTBSDINFO = 3
PROC_PIDUNIQIDENTIFIERINFO = 17
PROC_PIDCOALITIONINFO = 20
COALITION_TYPE_RESOURCE = 0
COALITION_TYPE_JETSAM = 1
COALITION_SPAWN_ENTITLEMENT = "com.apple.private.coalition-spawn"


class SupervisorError(RuntimeError):
    pass


class ProcessVanished(SupervisorError):
    pass


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


class ProcUniqueIdentifierInfo(ctypes.Structure):
    _fields_ = [
        ("uuid", ctypes.c_uint8 * 16),
        ("unique_id", ctypes.c_uint64),
        ("parent_unique_id", ctypes.c_uint64),
        ("id_version", ctypes.c_int32),
        ("reserved2", ctypes.c_uint32),
        ("reserved3", ctypes.c_uint64),
        ("reserved4", ctypes.c_uint64),
    ]


class ProcPidCoalitionInfo(ctypes.Structure):
    _fields_ = [
        ("coalition_id", ctypes.c_uint64 * 2),
        ("reserved1", ctypes.c_uint64),
        ("reserved2", ctypes.c_uint64),
        ("reserved3", ctypes.c_uint64),
    ]


class AuditToken(ctypes.Structure):
    _fields_ = [("value", ctypes.c_uint32 * 8)]


@dataclass(frozen=True)
class ProcessIdentity:
    pid: int
    unique_id: int
    parent_unique_id: int
    id_version: int
    resource_coalition_id: int
    jetsam_coalition_id: int
    ppid: int
    pgid: int
    command: str
    start_sec: int
    start_usec: int

    def as_json(self) -> dict[str, Any]:
        return {
            "pid": self.pid,
            "uniqueId": self.unique_id,
            "parentUniqueId": self.parent_unique_id,
            "idVersion": self.id_version,
            "resourceCoalitionId": self.resource_coalition_id,
            "jetsamCoalitionId": self.jetsam_coalition_id,
            "ppid": self.ppid,
            "pgid": self.pgid,
            "command": self.command,
            "startSec": self.start_sec,
            "startUsec": self.start_usec,
        }

    def audit_token(self, *, id_version: int | None = None) -> AuditToken:
        token = AuditToken()
        # audit_token_t: pid is word 5 and pidversion is word 7. The kernel
        # lookup used by proc_signal_with_audittoken validates those fields.
        token.value[5] = self.pid & 0xFFFFFFFF
        token.value[7] = (
            self.id_version if id_version is None else id_version
        ) & 0xFFFFFFFF
        return token


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def decode_command(raw: bytes) -> str:
    return raw.split(b"\0", 1)[0].decode("utf-8", errors="replace")


class DarwinAPI:
    def __init__(self, fail_operation: str | None = None) -> None:
        if sys.platform != "darwin":
            raise SupervisorError("Darwin libproc is required")
        expected_sizes = {
            "PROC_PIDUNIQIDENTIFIERINFO": (ctypes.sizeof(ProcUniqueIdentifierInfo), 56),
            "PROC_PIDCOALITIONINFO": (ctypes.sizeof(ProcPidCoalitionInfo), 40),
            "audit_token_t": (ctypes.sizeof(AuditToken), 32),
        }
        invalid_sizes = {
            name: {"actual": actual, "expected": expected}
            for name, (actual, expected) in expected_sizes.items()
            if actual != expected
        }
        if invalid_sizes:
            raise SupervisorError(f"unsupported Darwin ABI sizes: {invalid_sizes}")
        self.fail_operation = fail_operation
        self.libproc = ctypes.CDLL("/usr/lib/libSystem.B.dylib", use_errno=True)
        self.libproc.proc_listallpids.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.libproc.proc_listallpids.restype = ctypes.c_int
        self.libproc.proc_pidinfo.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_uint64,
            ctypes.c_void_p,
            ctypes.c_int,
        ]
        self.libproc.proc_pidinfo.restype = ctypes.c_int
        try:
            signal_function = self.libproc.proc_signal_with_audittoken
        except AttributeError as error:
            raise SupervisorError("proc_signal_with_audittoken unavailable") from error
        signal_function.argtypes = [ctypes.POINTER(AuditToken), ctypes.c_int]
        signal_function.restype = ctypes.c_int
        self.signal_function = signal_function

    def maybe_fail(self, operation: str) -> None:
        if self.fail_operation == operation:
            raise SupervisorError(f"injected {operation} failure")

    def list_pids(self) -> list[int]:
        self.maybe_fail("enumeration")
        required = self.libproc.proc_listallpids(None, 0)
        if required <= 0:
            raise SupervisorError("proc_listpids size query failed")
        capacity = max(required + 64, 1024)
        while True:
            values = (ctypes.c_int * capacity)()
            ctypes.set_errno(0)
            count = self.libproc.proc_listallpids(values, ctypes.sizeof(values))
            if count <= 0:
                raise SupervisorError(
                    f"proc_listallpids inventory failed: errno={ctypes.get_errno()}"
                )
            if count < capacity:
                return [int(pid) for pid in values[:count] if pid > 0]
            capacity *= 2

    def read_struct(self, pid: int, flavor: int, structure: Any, operation: str) -> Any:
        self.maybe_fail(operation)
        value = structure()
        ctypes.set_errno(0)
        read = self.libproc.proc_pidinfo(
            pid, flavor, 0, ctypes.byref(value), ctypes.sizeof(value)
        )
        if read == ctypes.sizeof(value):
            return value
        error = ctypes.get_errno()
        if read == 0 and error == errno.ESRCH:
            raise ProcessVanished(f"pid {pid} vanished during {operation}")
        raise SupervisorError(
            f"{operation} failed for pid {pid}: read={read} errno={error}"
        )

    def stable_snapshot(
        self, pid: int
    ) -> tuple[ProcUniqueIdentifierInfo, ProcPidCoalitionInfo]:
        for _ in range(3):
            first = self.read_struct(
                pid,
                PROC_PIDUNIQIDENTIFIERINFO,
                ProcUniqueIdentifierInfo,
                "unique",
            )
            coalition = self.read_struct(
                pid, PROC_PIDCOALITIONINFO, ProcPidCoalitionInfo, "coalition"
            )
            second = self.read_struct(
                pid,
                PROC_PIDUNIQIDENTIFIERINFO,
                ProcUniqueIdentifierInfo,
                "unique",
            )
            if (
                first.unique_id == second.unique_id
                and first.id_version == second.id_version
            ):
                return second, coalition
        raise SupervisorError(f"pid {pid} identity changed during inspection")

    def identity(self, pid: int) -> ProcessIdentity:
        unique, coalition = self.stable_snapshot(pid)
        bsd = self.read_struct(pid, PROC_PIDTBSDINFO, ProcBSDInfo, "bsd")
        after, after_coalition = self.stable_snapshot(pid)
        if (
            unique.unique_id != after.unique_id
            or unique.id_version != after.id_version
            or list(coalition.coalition_id) != list(after_coalition.coalition_id)
        ):
            raise SupervisorError(f"pid {pid} changed during full identity inspection")
        return ProcessIdentity(
            pid=pid,
            unique_id=int(unique.unique_id),
            parent_unique_id=int(unique.parent_unique_id),
            id_version=int(unique.id_version),
            resource_coalition_id=int(
                coalition.coalition_id[COALITION_TYPE_RESOURCE]
            ),
            jetsam_coalition_id=int(
                coalition.coalition_id[COALITION_TYPE_JETSAM]
            ),
            ppid=int(bsd.pbi_ppid),
            pgid=int(bsd.pbi_pgid),
            command=decode_command(bytes(bsd.pbi_comm)),
            start_sec=int(bsd.pbi_start_tvsec),
            start_usec=int(bsd.pbi_start_tvusec),
        )

    def coalition_members(
        self, resource_coalition_id: int, jetsam_coalition_id: int
    ) -> list[ProcessIdentity]:
        if resource_coalition_id <= 0 or jetsam_coalition_id <= 0:
            raise SupervisorError("coalition ids must be positive")
        members: list[ProcessIdentity] = []
        for pid in self.list_pids():
            try:
                unique, coalition = self.stable_snapshot(pid)
            except ProcessVanished:
                continue
            if (
                int(coalition.coalition_id[COALITION_TYPE_RESOURCE])
                == resource_coalition_id
                and int(coalition.coalition_id[COALITION_TYPE_JETSAM])
                == jetsam_coalition_id
            ):
                try:
                    identity = self.identity(pid)
                except ProcessVanished:
                    continue
                if (
                    identity.unique_id != int(unique.unique_id)
                    or identity.id_version != int(unique.id_version)
                    or identity.resource_coalition_id != resource_coalition_id
                    or identity.jetsam_coalition_id != jetsam_coalition_id
                ):
                    raise SupervisorError(
                        f"pid {pid} changed while joining coalition snapshot"
                    )
                members.append(identity)
        members.sort(key=lambda item: (item.unique_id, item.pid))
        return members

    def signal(self, identity: ProcessIdentity, signal_number: int) -> str:
        self.maybe_fail("signal")
        token = identity.audit_token()
        result = int(self.signal_function(ctypes.byref(token), signal_number))
        if result == 0:
            return "signalled"
        if result == errno.ESRCH:
            return "vanished-or-stale"
        raise SupervisorError(
            f"audit-token signal {signal_number} failed for pid {identity.pid}: {result}"
        )

    def signal_with_version(
        self, identity: ProcessIdentity, signal_number: int, id_version: int
    ) -> int:
        token = identity.audit_token(id_version=id_version)
        return int(self.signal_function(ctypes.byref(token), signal_number))


def run_command(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(arguments, text=True, capture_output=True, check=False)


def ensure_no_coalition_spawn_entitlement(paths: list[Path]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    candidates: dict[Path, Path] = {}
    for path in paths:
        resolved = path.resolve()
        if not resolved.exists():
            raise SupervisorError(f"target binary missing: {resolved}")
        if resolved.is_dir():
            executable_members = sorted(
                item.resolve()
                for item in resolved.rglob("*")
                if item.is_file() and os.access(item, os.X_OK)
            )
            if not executable_members:
                raise SupervisorError(
                    f"target bundle contains no executable members: {resolved}"
                )
        else:
            executable_members = [resolved]
        for member in executable_members:
            candidates[member] = resolved

    for resolved, declared_target in sorted(
        candidates.items(), key=lambda item: str(item[0])
    ):
        completed = run_command(
            ["/usr/bin/codesign", "-d", "--entitlements", "-", str(resolved)]
        )
        output = completed.stdout + completed.stderr
        if COALITION_SPAWN_ENTITLEMENT in output:
            raise SupervisorError(
                f"target binary carries coalition-spawn privilege: {resolved}"
            )
        if completed.returncode != 0 and "code object is not signed at all" not in output:
            raise SupervisorError(
                f"could not inspect target entitlements: {resolved}: "
                f"exit={completed.returncode} output={output.strip()}"
            )
        results.append(
            {
                "path": str(resolved),
                "declaredTarget": str(declared_target),
                "codesignExit": completed.returncode,
                "coalitionSpawnEntitlement": False,
            }
        )
    return results


def capability_probe(
    api: DarwinAPI,
    target_binaries: list[Path],
    probe_root: Path,
    *,
    fail_operation: str | None = None,
) -> dict[str, Any]:
    supervisor = api.identity(os.getpid())
    if supervisor.resource_coalition_id <= 0 or supervisor.jetsam_coalition_id <= 0:
        raise SupervisorError("supervisor coalition pair is unavailable")
    domain = run_command(["/bin/launchctl", "print", f"gui/{os.getuid()}"])
    if domain.returncode != 0:
        raise SupervisorError(
            f"per-user launchd domain unavailable: {domain.stderr.strip()}"
        )
    entitlement_results = ensure_no_coalition_spawn_entitlement(target_binaries)

    probe_root.mkdir(parents=True, exist_ok=True)
    label = f"ai.chirality.section8.probe.{os.getpid()}.{uuid.uuid4().hex[:12]}"
    service_target = f"gui/{os.getuid()}/{label}"
    plist_path = probe_root / f"{label}.plist"
    ready_path = probe_root / "probe-ready.json"
    leader_ready_path = probe_root / "probe-leader-ready.json"
    start_path = probe_root / "probe-start"
    forker_ready_path = probe_root / "forker-ready.json"
    stdout_path = probe_root / "probe.stdout.log"
    stderr_path = probe_root / "probe.stderr.log"
    write_launch_agent(
        plist_path,
        label=label,
        program_arguments=[
            sys.executable,
            str(Path(__file__).resolve()),
            "fixture",
            "--ready-file",
            str(ready_path),
            "--leader-ready-file",
            str(leader_ready_path),
            "--start-file",
            str(start_path),
            "--children",
            "4",
            "--forker-ready-file",
            str(forker_ready_path),
        ],
        environment={"PATH": os.environ.get("PATH", "/usr/bin:/bin")},
        working_directory=Path.cwd(),
        stdout_path=stdout_path,
        stderr_path=stderr_path,
    )
    if launchctl_print_target(service_target).returncode == 0:
        raise SupervisorError(f"pre-existing capability-probe label: {label}")
    bootstrapped = False
    target_pair: tuple[int, int] | None = None
    probe_detail: dict[str, Any] = {}
    foreign_command = [
        "/usr/bin/perl",
        "-e",
        "$SIG{TERM} = 'IGNORE'; sleep 60;",
    ]
    foreign: subprocess.Popen[Any] | None = None
    foreign_identity: ProcessIdentity | None = None
    try:
        if fail_operation == "bootstrap":
            raise SupervisorError("injected bootstrap failure")
        bootstrap = run_command(
            ["/bin/launchctl", "bootstrap", f"gui/{os.getuid()}", str(plist_path)]
        )
        if bootstrap.returncode != 0:
            raise SupervisorError(
                f"capability-probe bootstrap failed: {bootstrap.stderr.strip()}"
            )
        bootstrapped = True
        leader_ready = wait_for_json(leader_ready_path, 15)
        leader = api.identity(int(leader_ready["pid"]))
        target_pair = (
            leader.resource_coalition_id,
            leader.jetsam_coalition_id,
        )
        if 0 in target_pair or target_pair == (
            supervisor.resource_coalition_id,
            supervisor.jetsam_coalition_id,
        ):
            raise SupervisorError("probe did not receive a distinct coalition pair")
        # The probe fixture waits for this trigger. Start the adversarial
        # foreign process and all controlled Python descendants inside the same
        # kernel start-second so command/start-time heuristics demonstrably
        # cannot identify the signal target.
        fraction = time.time() % 1
        if fraction > 0.10:
            time.sleep(1.01 - fraction)
        foreign = subprocess.Popen(foreign_command)
        foreign_identity = api.identity(foreign.pid)
        start_path.write_text("start\n")
        ready = wait_for_json(ready_path, 15)
        children = [api.identity(int(pid)) for pid in ready["allDescendants"]]
        for child in children:
            if (
                child.resource_coalition_id,
                child.jetsam_coalition_id,
            ) != target_pair:
                raise SupervisorError("setsid child did not inherit probe coalition pair")
        if not any(
            child.command == foreign_identity.command
            and child.start_sec == foreign_identity.start_sec
            for child in children
        ):
            raise SupervisorError(
                "capability probe did not establish same-command/same-second foreign "
                f"control: foreign={foreign_identity.as_json()} "
                f"children={[item.as_json() for item in children]}"
            )
        members = api.coalition_members(*target_pair)
        expected_unique_ids = {leader.unique_id, *(item.unique_id for item in children)}
        if {item.unique_id for item in members} != expected_unique_ids:
            raise SupervisorError("probe coalition membership was missing or ambiguous")
        identity = children[0]
        if api.signal(identity, signal.SIGCONT) != "signalled":
            raise SupervisorError("correct audit token did not signal probe child")
        stale_result = api.signal_with_version(
            identity, signal.SIGCONT, identity.id_version + 1
        )
        if stale_result != errno.ESRCH:
            raise SupervisorError(
                f"stale pidversion was not rejected with ESRCH: {stale_result}"
            )
        probe_detail = {
            "label": label,
            "leader": leader.as_json(),
            "setsidChildren": [item.as_json() for item in children],
            "members": [item.as_json() for item in members],
            "coalitionPair": list(target_pair),
            "stalePidversion": "ESRCH",
            "foreignBefore": foreign_identity.as_json(),
        }
    finally:
        bootout_error: Exception | None = None
        postcondition_error: Exception | None = None
        if bootstrapped:
            completed = run_command(["/bin/launchctl", "bootout", service_target])
            if completed.returncode != 0:
                bootout_error = SupervisorError(
                    f"capability-probe bootout failed: {completed.stderr.strip()}"
                )
            elif fail_operation == "bootout":
                bootout_error = SupervisorError("injected bootout failure")
        # If an inspection failed after bootstrap but before target_pair was
        # accepted, a clean API may still recover the fixture leader's pair.
        # This recovery is cleanup-only and never converts the failed probe to
        # success.
        if target_pair is None and (leader_ready_path.exists() or ready_path.exists()):
            try:
                recovery_path = (
                    leader_ready_path if leader_ready_path.exists() else ready_path
                )
                cleanup_ready = json.loads(recovery_path.read_text())
                cleanup_leader = DarwinAPI().identity(int(cleanup_ready["pid"]))
                target_pair = (
                    cleanup_leader.resource_coalition_id,
                    cleanup_leader.jetsam_coalition_id,
                )
            except (OSError, KeyError, TypeError, ValueError, SupervisorError):
                pass
        if target_pair is not None:
            # Fault injection must never prevent cleanup of the disposable probe.
            cleanup_api = DarwinAPI()
            survivors_after_bootout = []
            expected_after_bootout = {
                int(item["uniqueId"])
                for item in probe_detail.get("setsidChildren", [])
            }
            for pid in [
                int(item["pid"])
                for item in probe_detail.get("setsidChildren", [])
            ]:
                try:
                    survivors_after_bootout.append(cleanup_api.identity(int(pid)).as_json())
                except ProcessVanished:
                    pass
            probe_detail["setsidChildrenAfterBootout"] = survivors_after_bootout
            observed_after_bootout = {
                int(item["uniqueId"]) for item in survivors_after_bootout
            }
            if expected_after_bootout and observed_after_bootout != expected_after_bootout:
                postcondition_error = SupervisorError(
                    "TERM-resistant setsid descendants did not all survive ordinary bootout"
                )
            probe_detail["sweep"] = sweep_coalition(
                cleanup_api, *target_pair, grace_seconds=0.2
            )
            if cleanup_api.coalition_members(*target_pair):
                raise SupervisorError("capability-probe coalition remained nonempty")
        if foreign is not None and foreign_identity is not None:
            clean_api = DarwinAPI()
            try:
                current_foreign = clean_api.identity(foreign.pid)
                if (
                    current_foreign.unique_id != foreign_identity.unique_id
                    or clean_api.signal(current_foreign, signal.SIGCONT) != "signalled"
                ):
                    raise SupervisorError("foreign same-command process did not survive")
                probe_detail["foreignAfterSweep"] = current_foreign.as_json()
                clean_api.signal(current_foreign, signal.SIGKILL)
            except ProcessVanished as error:
                raise SupervisorError("foreign same-command process was removed") from error
            finally:
                try:
                    foreign.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    foreign.kill()
                    foreign.wait()
        if bootout_error is not None:
            raise bootout_error
        if postcondition_error is not None:
            raise postcondition_error

    return {
        "schema": "chirality-section8-coalition-capability/v1",
        "status": "PASS",
        "platform": sys.platform,
        "supervisor": supervisor.as_json(),
        "auditTokenSignal": "PASS",
        "launchAgentProbe": probe_detail,
        "launchdDomain": f"gui/{os.getuid()}",
        "targetBinaries": entitlement_results,
    }


def signal_members(
    api: DarwinAPI, members: list[ProcessIdentity], signal_number: int
) -> list[dict[str, Any]]:
    outcomes: list[dict[str, Any]] = []
    for member in members:
        outcome = api.signal(member, signal_number)
        outcomes.append(
            {
                "identity": member.as_json(),
                "signal": signal_number,
                "outcome": outcome,
            }
        )
    return outcomes


def sweep_coalition(
    api: DarwinAPI,
    resource_coalition_id: int,
    jetsam_coalition_id: int,
    *,
    grace_seconds: float = 1.0,
) -> dict[str, Any]:
    report: dict[str, Any] = {
        "resourceCoalitionId": resource_coalition_id,
        "jetsamCoalitionId": jetsam_coalition_id,
        "termRounds": [],
        "stopKillRounds": [],
    }
    initial = api.coalition_members(resource_coalition_id, jetsam_coalition_id)
    report["initialMembers"] = [item.as_json() for item in initial]
    term_deadline = time.monotonic() + grace_seconds
    while time.monotonic() < term_deadline:
        members = api.coalition_members(resource_coalition_id, jetsam_coalition_id)
        report["termRounds"].append(signal_members(api, members, signal.SIGTERM))
        time.sleep(min(0.1, max(0.01, grace_seconds / 5)))

    consecutive_empty = 0
    for round_number in range(1, 51):
        members = api.coalition_members(resource_coalition_id, jetsam_coalition_id)
        if not members:
            consecutive_empty += 1
            report["stopKillRounds"].append(
                {"round": round_number, "emptyScan": consecutive_empty}
            )
            if consecutive_empty >= 3:
                report["rounds"] = round_number
                report["remainingMembers"] = []
                report["consecutiveEmptyScans"] = consecutive_empty
                report["status"] = "PASS"
                return report
            time.sleep(0.05)
            continue
        consecutive_empty = 0
        stopped = signal_members(api, members, signal.SIGSTOP)
        # Enumerate again after STOP. New members inherit the coalition and are
        # included in this or the next round; already-stopped members cannot fork.
        after_stop = api.coalition_members(resource_coalition_id, jetsam_coalition_id)
        killed = signal_members(api, after_stop, signal.SIGKILL)
        report["stopKillRounds"].append(
            {
                "round": round_number,
                "beforeStop": [item.as_json() for item in members],
                "stop": stopped,
                "afterStop": [item.as_json() for item in after_stop],
                "kill": killed,
            }
        )
        time.sleep(0.05)

    remaining = api.coalition_members(resource_coalition_id, jetsam_coalition_id)
    report["remainingMembers"] = [item.as_json() for item in remaining]
    report["status"] = "FAIL"
    raise SupervisorError(
        f"coalition sweep did not converge: {len(remaining)} members remain"
    )


def launchctl_print_target(service_target: str) -> subprocess.CompletedProcess[str]:
    return run_command(["/bin/launchctl", "print", service_target])


def write_launch_agent(
    path: Path,
    *,
    label: str,
    program_arguments: list[str],
    environment: dict[str, str],
    working_directory: Path,
    stdout_path: Path,
    stderr_path: Path,
) -> None:
    payload = {
        "Label": label,
        "ProgramArguments": program_arguments,
        "EnvironmentVariables": environment,
        "WorkingDirectory": str(working_directory),
        "RunAtLoad": True,
        "AbandonProcessGroup": True,
        "ProcessType": "Background",
        "StandardOutPath": str(stdout_path),
        "StandardErrorPath": str(stderr_path),
    }
    with path.open("wb") as handle:
        plistlib.dump(payload, handle, sort_keys=True)
    path.chmod(0o600)


def wait_for_json(path: Path, timeout: float) -> dict[str, Any]:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if path.exists():
            try:
                return json.loads(path.read_text())
            except (OSError, json.JSONDecodeError):
                pass
        time.sleep(0.05)
    raise SupervisorError(f"timed out waiting for {path}")


def bootout(service_target: str, *, injected_failure: bool = False) -> dict[str, Any]:
    completed = run_command(["/bin/launchctl", "bootout", service_target])
    record = {
        "exit": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "injectedFailure": injected_failure,
    }
    if completed.returncode != 0:
        raise SupervisorError(f"launchctl bootout failed: {record}")
    if injected_failure:
        raise SupervisorError("injected bootout failure")
    return record


def manifest_run_root(run_root: Path) -> None:
    entries: list[str] = []
    for top in (run_root / "artifacts", run_root / "logs"):
        if not top.exists():
            continue
        for path in sorted(item for item in top.rglob("*") if item.is_file()):
            relative = path.relative_to(run_root).as_posix()
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            entries.append(f"{digest}  {relative}")
    if not entries:
        raise SupervisorError("run root contains no manifestable artifacts/logs")
    (run_root / "MANIFEST.sha256").write_text("\n".join(entries) + "\n")


def inspect_listener_count(port: int) -> int:
    version = run_command(["/usr/sbin/lsof", "-v"])
    if version.returncode != 0:
        raise SupervisorError("lsof capability probe failed")
    completed = run_command(
        [
            "/usr/sbin/lsof",
            "-nP",
            "-t",
            f"-iTCP:{port}",
            "-sTCP:LISTEN",
        ]
    )
    if completed.returncode == 0:
        values = [line for line in completed.stdout.splitlines() if line]
        if any(not value.isdigit() for value in values) or completed.stderr:
            raise SupervisorError("ambiguous lsof listener output")
        return len(values)
    if completed.returncode == 1 and not completed.stdout and not completed.stderr:
        return 0
    raise SupervisorError(
        f"lsof listener inspection failed: {completed.returncode} {completed.stderr}"
    )


def capability_self_test(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    temporary_root = Path(
        tempfile.mkdtemp(prefix="coalition-probe.", dir=str(root))
    )
    report_path = root / (
        "coalition-capability.json"
        if args.inject_failure is None
        else f"coalition-capability-{args.inject_failure}-failure.json"
    )
    report: dict[str, Any] = {
        "schema": "chirality-section8-coalition-self-test/v1",
        "status": "FAIL",
        "injectedFailure": args.inject_failure,
    }
    status = 74
    try:
        api = DarwinAPI(args.inject_failure)
        report["capability"] = capability_probe(
            api,
            [Path(item) for item in args.target_binary],
            temporary_root,
            fail_operation=args.inject_failure,
        )
        if args.inject_failure is not None:
            raise SupervisorError(
                f"injected failure did not fail closed: {args.inject_failure}"
            )
        report["status"] = "PASS"
        status = 0
    except BaseException as error:
        report["error"] = f"{type(error).__name__}: {error}"
    finally:
        try:
            shutil.rmtree(temporary_root)
        except Exception as error:
            report["temporaryRootRemovalError"] = f"{type(error).__name__}: {error}"
            report["status"] = "FAIL"
            status = 74
        report["temporaryRootRemoved"] = not temporary_root.exists()
        report["exitCode"] = status
        atomic_json(report_path, report)
    return status


def supervise(args: argparse.Namespace) -> int:
    run_root = Path(args.run_root).resolve()
    logs = run_root / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    (run_root / "artifacts").mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "schema": "chirality-section8-coalition-supervisor/v1",
        "status": "FAIL",
    }
    cleanup_failed = False
    incoming_status = 74
    bootstrapped = False
    coalition_pair: tuple[int, int] | None = None
    temporary_root = Path(
        tempfile.mkdtemp(prefix="chirality-section8-launchagent.", dir="/private/tmp")
    )
    label = f"ai.chirality.section8.{os.getpid()}.{uuid.uuid4().hex[:12]}"
    service_target = f"gui/{os.getuid()}/{label}"
    report["label"] = label
    report["serviceTarget"] = service_target
    plist_path = temporary_root / f"{label}.plist"
    ready_path = temporary_root / "job-ready.json"
    ack_path = temporary_root / "job-ack"
    result_path = temporary_root / "job-result.json"
    api = DarwinAPI(args.inject_failure)

    try:
        if inspect_listener_count(args.port) != 0:
            raise SupervisorError("port became occupied before job creation")
        capability = capability_probe(
            api,
            [Path(item) for item in args.target_binary],
            temporary_root / "capability-probe",
            fail_operation=args.inject_failure,
        )
        atomic_json(logs / "coalition-capability.json", capability)
        supervisor_identity = api.identity(os.getpid())

        existing = launchctl_print_target(service_target)
        if existing.returncode == 0:
            raise SupervisorError(f"pre-existing LaunchAgent label: {label}")

        environment = {
            key: value
            for key in (
                "HOME",
                "PATH",
                "TMPDIR",
                "REPO_ROOT",
                "RUN_ROOT",
                "PORT",
                "USER_DATA",
                "WITH_RELEASE_QUALITY",
                "KEEP",
                "SKIP_BUILD",
                "APPROVED_BY",
                "APPROVAL_REF",
            )
            if (value := os.environ.get(key)) is not None
        }
        environment["SECTION8_COALITION_INNER"] = "1"
        program_arguments = [
            sys.executable,
            str(Path(__file__).resolve()),
            "job",
            "--script",
            str(Path(args.script).resolve()),
            "--ready-file",
            str(ready_path),
            "--ack-file",
            str(ack_path),
            "--result-file",
            str(result_path),
        ]
        write_launch_agent(
            plist_path,
            label=label,
            program_arguments=program_arguments,
            environment=environment,
            working_directory=Path(args.repo_root).resolve(),
            stdout_path=logs / "launchagent-job.stdout.log",
            stderr_path=logs / "launchagent-job.stderr.log",
        )
        report["plistSha256"] = hashlib.sha256(plist_path.read_bytes()).hexdigest()

        bootstrap = run_command(
            ["/bin/launchctl", "bootstrap", f"gui/{os.getuid()}", str(plist_path)]
        )
        report["bootstrap"] = {
            "exit": bootstrap.returncode,
            "stdout": bootstrap.stdout,
            "stderr": bootstrap.stderr,
        }
        if bootstrap.returncode != 0:
            raise SupervisorError(f"launchctl bootstrap failed: {report['bootstrap']}")
        bootstrapped = True

        ready = wait_for_json(ready_path, 15)
        leader = api.identity(int(ready["pid"]))
        coalition_pair = (
            leader.resource_coalition_id,
            leader.jetsam_coalition_id,
        )
        supervisor_pair = (
            supervisor_identity.resource_coalition_id,
            supervisor_identity.jetsam_coalition_id,
        )
        if 0 in coalition_pair or coalition_pair == supervisor_pair:
            raise SupervisorError("LaunchAgent did not receive a distinct coalition pair")
        members = api.coalition_members(*coalition_pair)
        if not any(
            item.unique_id == leader.unique_id and item.id_version == leader.id_version
            for item in members
        ):
            raise SupervisorError("LaunchAgent leader missing from its resource coalition")
        if len(members) != 1:
            raise SupervisorError(
                "LaunchAgent coalition was not unique before inner lifecycle acknowledgement"
            )
        report["supervisor"] = supervisor_identity.as_json()
        report["leader"] = leader.as_json()
        report["membersBeforeAck"] = [item.as_json() for item in members]
        ack_path.write_text("coalition-accepted\n")

        result = wait_for_json(result_path, args.timeout)
        incoming_status = int(result["exitCode"])
        report["innerResult"] = result
    except BaseException as error:
        report["error"] = f"{type(error).__name__}: {error}"
        cleanup_failed = True
    finally:
        if bootstrapped:
            try:
                report["bootout"] = bootout(
                    service_target,
                    injected_failure=args.inject_failure == "bootout",
                )
            except Exception as error:
                report["bootoutError"] = f"{type(error).__name__}: {error}"
                cleanup_failed = True
        if coalition_pair is not None:
            try:
                report["sweep"] = sweep_coalition(api, *coalition_pair)
            except Exception as error:
                report["sweepError"] = f"{type(error).__name__}: {error}"
                cleanup_failed = True
        try:
            report["finalCoalitionMembers"] = (
                []
                if coalition_pair is None
                else [
                    item.as_json()
                    for item in api.coalition_members(*coalition_pair)
                ]
            )
            if report["finalCoalitionMembers"]:
                cleanup_failed = True
        except Exception as error:
            report["finalEnumerationError"] = f"{type(error).__name__}: {error}"
            cleanup_failed = True
        try:
            listener_count = inspect_listener_count(args.port)
            report["finalPortListenerCount"] = listener_count
            if listener_count != 0:
                cleanup_failed = True
        except Exception as error:
            report["finalPortError"] = f"{type(error).__name__}: {error}"
            cleanup_failed = True
        socket_path = Path(os.environ["USER_DATA"]) / "runtime" / "control.sock"
        report["finalSocketPresent"] = socket_path.exists()
        if report["finalSocketPresent"]:
            cleanup_failed = True
        if (
            os.environ.get("KEEP", "0") != "1"
            and os.environ.get("USER_DATA_CREATED") == "1"
            and os.environ.get("USER_DATA")
        ):
            try:
                shutil.rmtree(os.environ["USER_DATA"], ignore_errors=False)
            except FileNotFoundError:
                pass
            except Exception as error:
                report["userDataRemovalError"] = f"{type(error).__name__}: {error}"
                cleanup_failed = True
        try:
            shutil.rmtree(temporary_root)
        except Exception as error:
            report["temporaryRootRemovalError"] = f"{type(error).__name__}: {error}"
            cleanup_failed = True
        report["temporaryRootRemoved"] = not temporary_root.exists()
        report["cleanupFailed"] = cleanup_failed
        final_status = incoming_status if incoming_status != 0 else (74 if cleanup_failed else 0)
        report["exitCode"] = final_status
        report["status"] = "PASS" if final_status == 0 else "FAIL"
        atomic_json(logs / "coalition-supervisor.json", report)
        environment_path = logs / "environment.txt"
        if environment_path.exists() and coalition_pair is not None:
            with environment_path.open("a", encoding="utf-8") as handle:
                handle.write(f"launchagent_label={label}\n")
                handle.write(f"resource_coalition_id={coalition_pair[0]}\n")
                handle.write(f"jetsam_coalition_id={coalition_pair[1]}\n")
                handle.write(
                    "coalition_cleanup=audit-token TERM then STOP/KILL repeated to zero\n"
                )
        manifest_run_root(run_root)
    return int(report["exitCode"])


def job_main(args: argparse.Namespace) -> int:
    ready_path = Path(args.ready_file)
    ack_path = Path(args.ack_file)
    result_path = Path(args.result_file)
    atomic_json(ready_path, {"schema": "chirality-section8-job-ready/v1", "pid": os.getpid()})
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline and not ack_path.exists():
        time.sleep(0.05)
    if not ack_path.exists():
        atomic_json(result_path, {"exitCode": 75, "error": "supervisor ack timeout"})
        return 75
    child = subprocess.Popen(["/bin/bash", str(Path(args.script).resolve())])
    atomic_json(
        ready_path,
        {
            "schema": "chirality-section8-job-ready/v1",
            "pid": os.getpid(),
            "childPid": child.pid,
            "acknowledged": True,
        },
    )
    child_status = child.wait()
    atomic_json(
        result_path,
        {
            "schema": "chirality-section8-job-result/v1",
            "pid": os.getpid(),
            "childPid": child.pid,
            "exitCode": child_status,
        },
    )
    # Keep the launchd job leader (and therefore the coalition identity) alive
    # until the outer supervisor boots out the job and performs the sweep.
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    while True:
        time.sleep(1)


def fixture_main(args: argparse.Namespace) -> int:
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    atomic_json(
        Path(args.leader_ready_file),
        {"schema": "chirality-section8-coalition-fixture-leader/v1", "pid": os.getpid()},
    )
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline and not Path(args.start_file).exists():
        time.sleep(0.01)
    if not Path(args.start_file).exists():
        raise SupervisorError("capability fixture start trigger timed out")
    children: list[subprocess.Popen[Any]] = []
    child_command = [
        "/usr/bin/perl",
        "-e",
        "$SIG{TERM} = 'IGNORE'; sleep 60;",
    ]
    for _ in range(args.children):
        children.append(
            subprocess.Popen(child_command, start_new_session=True)
        )
    forker = subprocess.Popen(
        [
            sys.executable,
            str(Path(__file__).resolve()),
            "forker",
            "--ready-file",
            args.forker_ready_file,
        ],
        start_new_session=True,
    )
    forker_ready = wait_for_json(Path(args.forker_ready_file), 10)
    all_descendants = [child.pid for child in children]
    all_descendants.extend([forker.pid, int(forker_ready["childPid"])])
    atomic_json(
        Path(args.ready_file),
        {
            "schema": "chirality-section8-coalition-fixture/v1",
            "pid": os.getpid(),
            "children": [child.pid for child in children],
            "forkerPid": forker.pid,
            "grandchildPid": int(forker_ready["childPid"]),
            "allDescendants": all_descendants,
        },
    )
    while True:
        time.sleep(1)


def forker_main(args: argparse.Namespace) -> int:
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    child = subprocess.Popen(
        [
            sys.executable,
            "-c",
            "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
        ],
        start_new_session=True,
    )
    atomic_json(
        Path(args.ready_file),
        {"schema": "chirality-section8-coalition-forker/v1", "childPid": child.pid},
    )
    while True:
        time.sleep(1)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser()
    commands = root.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument("--run-root", required=True)
    run.add_argument("--script", required=True)
    run.add_argument("--repo-root", required=True)
    run.add_argument("--port", required=True, type=int)
    run.add_argument("--target-binary", action="append", default=[])
    run.add_argument("--timeout", type=float, default=1200)
    run.add_argument(
        "--inject-failure",
        choices=[
            "enumeration",
            "unique",
            "coalition",
            "signal",
            "bootstrap",
            "bootout",
        ],
    )
    self_test = commands.add_parser("self-test")
    self_test.add_argument("--root", required=True)
    self_test.add_argument("--target-binary", action="append", default=[])
    self_test.add_argument(
        "--inject-failure",
        choices=[
            "enumeration",
            "unique",
            "coalition",
            "signal",
            "bootstrap",
            "bootout",
        ],
    )
    job = commands.add_parser("job")
    job.add_argument("--script", required=True)
    job.add_argument("--ready-file", required=True)
    job.add_argument("--ack-file", required=True)
    job.add_argument("--result-file", required=True)
    fixture = commands.add_parser("fixture")
    fixture.add_argument("--ready-file", required=True)
    fixture.add_argument("--leader-ready-file", required=True)
    fixture.add_argument("--start-file", required=True)
    fixture.add_argument("--children", type=int, default=8)
    fixture.add_argument("--forker-ready-file", required=True)
    forker = commands.add_parser("forker")
    forker.add_argument("--ready-file", required=True)
    return root


def main() -> int:
    args = parser().parse_args()
    if args.command == "run":
        return supervise(args)
    if args.command == "self-test":
        return capability_self_test(args)
    if args.command == "job":
        return job_main(args)
    if args.command == "fixture":
        return fixture_main(args)
    if args.command == "forker":
        return forker_main(args)
    raise SupervisorError(f"unknown command: {args.command}")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SupervisorError as error:
        print(f"section8 coalition supervisor: {error}", file=sys.stderr)
        raise SystemExit(74)
