#!/usr/bin/env python3
"""Response-local macOS launcher. INACTIVE / NOT LIVE-QUALIFIED at authorship.

ROOT invocation with an explicit job JSON is the run grant; no approval token.
Only direct commands with inherited process-group descendants are in scope.
No daemon, automatic retry, detached-runner support, or remote control endpoint.
See instances/GUARD-IMPLEMENTATION for provider derivation and qualification.
Importing this module performs no process, provider, filesystem or signal action.
"""
from __future__ import annotations

import argparse
import ctypes as C
from dataclasses import asdict, dataclass
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import secrets
import select
import signal
import socket
import stat
import subprocess
import sys
import time

MIB = 1024 ** 2
GIB = 1024 ** 3
MAX_AGE = 2.0
INTERVAL = 1.0
HEARTBEAT = 3.0
TERM_GRACE = 2.0
MAX_MEMBERS = 512
MAX_OUTPUT = 8 * MIB
MAX_EVENTS = 8 * MIB
MAX_PACKET = 4096
RUN_ID = 'HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE'


class Refusal(Exception):
    """Untrusted/absent observation, violated limit, or unsupported invocation."""


def finite(value, name, minimum=0):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise Refusal('malformed:' + name)
    if not math.isfinite(value) or value < minimum:
        raise Refusal('invalid:' + name)
    return value


def integer(value, name, minimum=0):
    finite(value, name, minimum)
    if not isinstance(value, int):
        raise Refusal('noninteger:' + name)
    return value


@dataclass(frozen=True)
class Identity:
    pid: int
    start_sec: int
    start_usec: int
    uid: int
    ruid: int
    pgid: int
    sid: int

    def validate(self):
        for k, v in asdict(self).items():
            integer(v, k, 1 if k in ('pid', 'start_sec', 'pgid', 'sid') else 0)
        if self.start_usec >= 1000000:
            raise Refusal('invalid:start_usec')


@dataclass(frozen=True)
class Row:
    pid: int
    ppid: int
    pgid: int
    uid: int
    zombie: bool


@dataclass(frozen=True)
class Sample:
    at: float                    # earliest acquisition time, monotonic
    total_bytes: int
    available_pct: float         # memory_pressure -Q estimate, NOT exact free bytes
    pressure: int                # accepted normal value 1; everything else stops
    swap_used_bytes: int
    swapouts: int                # vm_stat cumulative pages, independent of swap used
    disk_free_bytes: int
    rss_bytes: int               # sum of live registered-group RSS (incl supervisor)
    footprint_bytes: int         # sum of ri_phys_footprint (incl supervisor)

    def validate(self, now):
        finite(now, 'clock')
        finite(self.at, 'sample-time')
        if self.at > now or now - self.at > MAX_AGE:
            raise Refusal('stale-or-future-sample')
        for k in ('total_bytes', 'pressure', 'swap_used_bytes', 'swapouts',
                  'disk_free_bytes', 'rss_bytes', 'footprint_bytes'):
            integer(getattr(self, k), k, 1 if k == 'total_bytes' else 0)
        finite(self.available_pct, 'available_pct')
        if self.available_pct > 100:
            raise Refusal('invalid:available_pct')


@dataclass(frozen=True)
class Limits:
    cap_bytes: int
    allowance_bytes: int
    disk_write_budget_bytes: int
    disk_reserve_bytes: int
    max_seconds: int

    def validate(self):
        for k, v in asdict(self).items():
            integer(v, k, 1)
        if self.cap_bytes > 2 * GIB or self.max_seconds > 3600:
            raise Refusal('unsupported-cap-or-duration')
        if self.disk_write_budget_bytes < 3 * MAX_EVENTS + MAX_OUTPUT:
            raise Refusal('disk-budget-must-cover-guard-evidence')


def assess(sample, baseline, limits, now, admission=False):
    """Pure decision: stable high swap is allowed; growth is not attributed."""
    limits.validate()
    sample.validate(now)
    # Baseline was validated at acquisition; its age is deliberately historical.
    baseline.validate(baseline.at)
    if sample.total_bytes != baseline.total_bytes:
        return 'memory-total-changed'
    if sample.pressure != 1:
        return 'pressure-not-normal'
    if sample.available_pct <= 40:
        return 'available-at-or-below-40pct'
    if sample.swapouts < baseline.swapouts:
        return 'swap-counter-reset'
    if sample.swapouts > baseline.swapouts:
        return 'new-swapouts'
    if sample.swap_used_bytes - baseline.swap_used_bytes >= 64 * MIB:
        return 'swap-growth-at-least-64MiB'
    if sample.disk_free_bytes <= limits.disk_write_budget_bytes + limits.disk_reserve_bytes:
        return 'insufficient-disk-headroom'
    if sample.rss_bytes >= limits.cap_bytes:
        return 'rss-cap'
    if sample.footprint_bytes >= limits.cap_bytes:
        return 'footprint-cap'
    if admission and sample.swap_used_bytes != baseline.swap_used_bytes:
        return 'quiet-swap-baseline-unstable'
    if admission:
        # Conservative projection consumes the FULL group cap plus allowance.
        # The percentage is an OS estimate, not a byte-exact RAM reservation.
        projected = sample.available_pct - 100 * (limits.cap_bytes + limits.allowance_bytes) / sample.total_bytes
        if projected <= 40:
            return 'projected-available-at-or-below-40pct'
    return None


def parse_percentage(text):
    matches = re.findall(r'^System-wide memory free percentage: ([0-9]+)%\s*$', text, re.M)
    if len(matches) != 1 or not 0 <= int(matches[0]) <= 100:
        raise Refusal('malformed-memory-pressure')
    return float(matches[0])


def parse_swap(text):
    match = re.fullmatch(r'\s*total = ([0-9]+(?:\.[0-9]+)?)M\s+used = ([0-9]+(?:\.[0-9]+)?)M\s+free = ([0-9]+(?:\.[0-9]+)?)M(?:\s+\(encrypted\))?\s*', text)
    if not match:
        raise Refusal('malformed-swap')
    total, used, free = [float(x) for x in match.groups()]
    if used > total or free > total or abs(total - used - free) > .05:
        raise Refusal('inconsistent-swap')
    return int(used * MIB)


def parse_swapouts(text):
    matches = re.findall(r'^Swapouts:\s+([0-9]+)\.\s*$', text, re.M)
    if len(matches) != 1:
        raise Refusal('malformed-vm-stat')
    return int(matches[0])


def parse_rows(text):
    rows = {}
    for line in text.splitlines():
        fields = line.split()
        if len(fields) != 5 or not all(x.isdecimal() for x in fields[:4]):
            raise Refusal('malformed-process-table')
        pid, ppid, pgid, uid = map(int, fields[:4])
        if pid < 0 or pid in rows or not re.fullmatch(r'[A-Za-z+<>NsEX]+', fields[4]):
            raise Refusal('malformed-process-row')
        rows[pid] = Row(pid, ppid, pgid, uid, fields[4].startswith('Z'))
    if not rows:
        raise Refusal('empty-process-table')
    return rows


def select_members(rows, leader, known):
    """Pure containment check. A poll cannot detect an unobserved double fork."""
    leader.validate()
    if leader.pid not in rows:
        raise Refusal('leader-loss')
    selected = {leader.pid}
    # Remember prior live identities to detect reparented, escaped descendants.
    selected.update(pid for pid in known if pid in rows)
    selected.update(pid for pid, row in rows.items() if row.pgid == leader.pgid)
    while True:
        expanded = selected | {pid for pid, row in rows.items() if row.ppid in selected}
        if expanded == selected:
            break
        selected = expanded
        if len(selected) > MAX_MEMBERS:
            raise Refusal('too-many-members')
    if len(selected) > MAX_MEMBERS:
        raise Refusal('too-many-members')
    for pid in selected:
        row = rows[pid]
        if row.uid != leader.uid or row.pgid != leader.pgid:
            raise Refusal('escaped-group-or-changed-uid')
    return selected


def validate_member(expected, actual, leader):
    actual.validate()
    if expected is not None and actual != expected:
        raise Refusal('identity-changed-or-pid-reused')
    if (actual.uid, actual.ruid, actual.pgid, actual.sid) != (leader.uid, leader.ruid, leader.pgid, leader.sid):
        raise Refusal('member-identity-or-session-mismatch')


class MonitorState:
    """Pure control state: never signals a number, even on ownership failure."""
    def __init__(self):
        self.stopped = None

    def step(self, provider, control, baseline, limits, now):
        if self.stopped:
            return self.stopped
        try:
            sample = provider()
            reason = assess(sample, baseline, limits, now() if callable(now) else now)
        except Exception as exc:
            sample, reason = None, 'monitoring-failure:' + type(exc).__name__ + ':' + str(exc)[:256]
        if reason:
            self.stopped = reason
            control('STOP', reason)   # caller's private channel, no PID/PGID target
        else:
            control('HEARTBEAT', '')
        return reason


class StopState:
    """Pure supervisor watchdog. Sink is injected; tests use a list, not OS."""
    def __init__(self, now):
        finite(now, 'watchdog-clock')
        self.last_heartbeat = now
        self.stop_at = None
        self.reason = None
        self.term_sent = False
        self.kill_sent = False

    def request(self, now, reason):
        finite(now, 'stop-clock')
        if self.stop_at is None:
            self.stop_at, self.reason = now, reason

    def heartbeat(self, now):
        finite(now, 'heartbeat')
        if now < self.last_heartbeat:
            raise Refusal('nonmonotonic-heartbeat')
        self.last_heartbeat = now

    def tick(self, now, self_valid, sink):
        finite(now, 'watchdog-clock')
        if now < self.last_heartbeat:
            raise Refusal('nonmonotonic-watchdog-clock')
        if now - self.last_heartbeat >= HEARTBEAT:
            self.request(now, 'heartbeat-loss')
        if self.stop_at is None:
            return
        # Never signal if current self identity/session is no longer the owner.
        if not self_valid:
            raise Refusal('supervisor-self-identity-mismatch')
        if not self.term_sent:
            sink('TERM', self.reason)
            self.term_sent = True
        if now - self.stop_at >= TERM_GRACE and not self.kill_sent:
            sink('KILL', self.reason)
            self.kill_sent = True


# macOS SDK 26.5 declarations, not inferred from output. See PROVIDERS.md.
class BSDInfo(C.Structure):
    _fields_ = [(n, C.c_uint32) for n in (
        'flags', 'status', 'xstatus', 'pid', 'ppid', 'uid', 'gid', 'ruid',
        'rgid', 'svuid', 'svgid', 'reserved')] + [
        ('comm', C.c_char * 16), ('name', C.c_char * 32)] + [
        (n, C.c_uint32) for n in ('nfiles', 'pgid', 'pjobc', 'tdev', 'tpgid')] + [
        ('nice', C.c_int32), ('start_sec', C.c_uint64), ('start_usec', C.c_uint64)]


class RUsageV0(C.Structure):
    _fields_ = [('uuid', C.c_uint8 * 16)] + [(n, C.c_uint64) for n in (
        'user_time', 'system_time', 'pkg_idle_wkups', 'interrupt_wkups',
        'pageins', 'wired_size', 'resident_size', 'phys_footprint',
        'proc_start_abstime', 'proc_exit_abstime')]


def bounded_command(argv, deadline, trace=None):
    """Fixed read-only providers, bounded output/deadline; no shell."""
    process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               close_fds=True, env={'PATH': '/usr/bin:/bin:/usr/sbin:/sbin', 'LC_ALL': 'C'})
    output = bytearray()
    try:
        os.set_blocking(process.stdout.fileno(), False)
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise Refusal('provider-timeout')
            ready, _, _ = select.select([process.stdout], [], [], min(.05, remaining))
            if ready:
                chunk = os.read(process.stdout.fileno(), 65536)
                if not chunk:
                    break
                output.extend(chunk)
                if len(output) > MIB:
                    raise Refusal('provider-output-limit')
        code = process.wait(timeout=max(.001, deadline - time.monotonic()))
        decoded = output.decode('ascii', 'strict')
        if trace:
            trace('provider-command', argv=argv, returncode=code, raw=decoded)
        if code:
            raise Refusal('provider-denied-or-failed:' + Path(argv[0]).name)
        return decoded
    finally:
        # This is our unreaped direct provider child, never a discovered PID.
        if process.poll() is None:
            process.kill()
        process.wait()
        process.stdout.close()


class MacProvider:
    """Construct only at explicit run time. Native provider errors are fatal."""
    def __init__(self, log_dir, trace=None):
        self.trace = trace
        if sys.platform != 'darwin' or C.sizeof(C.c_void_p) != 8:
            raise Refusal('provider-requires-64-bit-macOS')
        if (C.sizeof(BSDInfo), BSDInfo.start_sec.offset, C.sizeof(RUsageV0),
                RUsageV0.resident_size.offset, RUsageV0.phys_footprint.offset) != (136, 120, 96, 64, 72):
            raise Refusal('ctypes-layout-mismatch')
        self.lib = C.CDLL('/usr/lib/libproc.dylib', use_errno=True)
        self.lib.proc_pidinfo.argtypes = [C.c_int, C.c_int, C.c_uint64, C.c_void_p, C.c_int]
        self.lib.proc_pidinfo.restype = C.c_int
        self.lib.proc_listpids.argtypes = [C.c_uint32, C.c_uint32, C.c_void_p, C.c_int]
        self.lib.proc_listpids.restype = C.c_int
        # Header: rusage_info_t is void*; API accepts rusage_info_t*.
        self.lib.proc_pid_rusage.argtypes = [C.c_int, C.c_int, C.POINTER(C.c_void_p)]
        self.lib.proc_pid_rusage.restype = C.c_int
        self.log_dir = log_dir
        self.known = {}

    def identity(self, pid):
        first, second = BSDInfo(), BSDInfo()
        for obj in (first, second):
            C.set_errno(0)
            if self.lib.proc_pidinfo(pid, 3, 0, C.byref(obj), C.sizeof(obj)) != C.sizeof(obj):
                raise Refusal('proc-pidinfo-denied-missing-short:' + str(C.get_errno()))
            if obj is first:
                sid = os.getsid(pid)
        if bytes(first) != bytes(second):
            # Compare stable identity fields below; counters/names can change.
            a = (first.pid, first.start_sec, first.start_usec, first.uid, first.ruid, first.pgid)
            b = (second.pid, second.start_sec, second.start_usec, second.uid, second.ruid, second.pgid)
            if a != b:
                raise Refusal('identity-raced')
        if second.pid != pid or os.getsid(pid) != sid:
            raise Refusal('session-raced')
        ident = Identity(pid, second.start_sec, second.start_usec, second.uid, second.ruid, second.pgid, sid)
        ident.validate()
        return ident, second.status == 5

    def table(self, deadline):
        return parse_rows(bounded_command(['/bin/ps', '-axo', 'pid=,ppid=,pgid=,uid=,stat='], deadline, self.trace))

    def live_group(self, leader):
        # Supervisor cleanup must not spawn ps inside the owned group. Read the
        # native group directly; proc_listpids returns BYTES, not PID count.
        buffer = (C.c_int * (MAX_MEMBERS + 1))()
        count = self.lib.proc_listpids(2, leader.pgid, buffer, C.sizeof(buffer))
        if count <= 0 or count >= C.sizeof(buffer) or count % C.sizeof(C.c_int):
            raise Refusal('group-enumeration-denied-empty-or-truncated')
        pids = list(buffer[:count // C.sizeof(C.c_int)])
        if leader.pid not in pids or len(set(pids)) != len(pids) or any(pid <= 0 for pid in pids):
            raise Refusal('group-enumeration-invalid')
        live = []
        for pid in pids:
            ident, zombie = self.identity(pid)
            validate_member(leader if pid == leader.pid else self.known.get(pid), ident, leader)
            if not zombie and pid != leader.pid:
                live.append(pid)
        return live

    def group(self, leader, deadline):
        rows = self.table(deadline)
        selected = select_members(rows, leader, self.known)
        rss = footprint = 0
        identities = {}
        live_children = []
        for pid in sorted(selected):
            ident, zombie = self.identity(pid)
            validate_member(leader if pid == leader.pid else self.known.get(pid), ident, leader)
            if rows[pid].uid != ident.uid or rows[pid].pgid != ident.pgid:
                raise Refusal('process-table-raced')
            identities[pid] = ident
            if not zombie:
                usage = RUsageV0()
                if self.lib.proc_pid_rusage(pid, 0, C.cast(C.byref(usage), C.POINTER(C.c_void_p))) != 0:
                    raise Refusal('rusage-denied-or-missing:' + str(C.get_errno()))
                after, after_zombie = self.identity(pid)
                if after != ident or after_zombie or usage.proc_start_abstime == 0 or usage.proc_exit_abstime != 0:
                    raise Refusal('rusage-identity-raced')
                rss += usage.resident_size
                footprint += usage.phys_footprint
                if pid != leader.pid:
                    live_children.append(pid)
            if time.monotonic() > deadline:
                raise Refusal('group-sample-timeout')
        self.known = identities
        return rss, footprint, live_children, identities

    def sample(self, leader=None):
        started = time.monotonic()
        deadline = started + 1.5
        def command(*args):
            return bounded_command(list(args), deadline, self.trace)
        total = command('/usr/sbin/sysctl', '-n', 'hw.memsize').strip()
        pressure = command('/usr/sbin/sysctl', '-n', 'kern.memorystatus_vm_pressure_level').strip()
        if not total.isdecimal() or not pressure.isdecimal():
            raise Refusal('malformed-sysctl')
        available = parse_percentage(command('/usr/bin/memory_pressure', '-Q'))
        swap = parse_swap(command('/usr/sbin/sysctl', '-n', 'vm.swapusage'))
        swapouts = parse_swapouts(command('/usr/bin/vm_stat'))
        disk = os.statvfs(self.log_dir)
        rss, footprint = 0, 0
        if leader:
            rss, footprint, _, _ = self.group(leader, deadline)
        result = Sample(started, int(total), available, int(pressure), swap, swapouts,
                        disk.f_bavail * disk.f_frsize, rss, footprint)
        result.validate(time.monotonic())
        return result


class Channel:
    """Private inherited socket pair plus per-job nonce and monotonic sequence.

    No pathname, listener, PID-based lookup, environment or on-disk secret.
    FD is closed before exec. Not a boundary against a hostile same-UID debugger.
    """
    def __init__(self, sock, nonce):
        self.sock, self.nonce = sock, nonce
        self.sent = self.received = 0
        sock.setblocking(False)

    def send(self, kind, **data):
        self.sent += 1
        raw = json.dumps({'nonce': self.nonce, 'seq': self.sent, 'kind': kind, 'data': data},
                         separators=(',', ':'), allow_nan=False).encode()
        if len(raw) > MAX_PACKET:
            raise Refusal('control-packet-limit')
        if self.sock.send(raw) != len(raw):
            raise Refusal('short-control-write')

    def receive(self):
        try:
            raw = self.sock.recv(MAX_PACKET + 1)
        except BlockingIOError:
            return None
        if not raw or len(raw) > MAX_PACKET:
            raise Refusal('bad-control-size')
        value = json.loads(raw)
        if (value.get('nonce') != self.nonce or type(value.get('seq')) is not int
                or value['seq'] != self.received + 1 or not isinstance(value.get('data'), dict)):
            raise Refusal('unauthenticated-or-replayed-control')
        self.received = value['seq']
        return value['kind'], value['data']


class Events:
    def __init__(self, path):
        self.file = open(path, 'xb', buffering=0)
        self.count = 0

    def emit(self, kind, **data):
        raw = (json.dumps({'at': time.monotonic(), 'wall_ns': time.time_ns(), 'kind': kind,
                           'data': data}, sort_keys=True, allow_nan=False) + '\n').encode()
        if len(raw) > 256 * 1024 or self.count + len(raw) > MAX_EVENTS:
            raise Refusal('event-log-limit')
        if self.file.write(raw) != len(raw):
            raise Refusal('short-event-log-write')
        self.count += len(raw)

    def close(self):
        self.file.close()


def self_is_owner(leader):
    # The currently executing supervisor cannot have reused its own PID/start.
    # Its start was captured before worker fork; no external PID is signalled.
    return (os.getpid(), os.getuid(), os.geteuid(), os.getpgrp(), os.getsid(0)) == (
        leader.pid, leader.ruid, leader.uid, leader.pgid, leader.sid)


def reset_worker_signals():
    # Explicit DFL, never inherited SIG_IGN; exec also resets caught handlers.
    for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGPIPE):
        signal.signal(sig, signal.SIG_DFL)


def supervisor(channel, slot_fd, job, log_dir):
    """Only this process signals, and only its own continuously live group."""
    os.setsid()
    events = Events(log_dir / 'supervisor.jsonl')
    provider = MacProvider(log_dir)
    leader, zombie = provider.identity(os.getpid())
    if zombie or leader.pid != leader.pgid or leader.pid != leader.sid or not self_is_owner(leader):
        raise Refusal('not-independent-supervisor-session')
    state = StopState(time.monotonic())
    signal.signal(signal.SIGTERM, lambda *_: state.request(time.monotonic(), 'supervisor-TERM'))
    signal.signal(signal.SIGINT, lambda *_: state.request(time.monotonic(), 'supervisor-INT'))
    signal.signal(signal.SIGHUP, lambda *_: state.request(time.monotonic(), 'supervisor-HUP'))
    events.emit('identity', identity=asdict(leader))
    channel.send('READY', identity=asdict(leader))
    child = None
    child_status = None
    pipe = None
    output = None
    output_bytes = 0
    started = time.monotonic()
    last_group_check = started
    stop_reason = None

    def record(kind, **data):
        try:
            events.emit(kind, **data)
        except Exception:
            state.request(time.monotonic(), 'supervisor-evidence-failure')

    def signal_own_group(kind, reason):
        record('signal-intent', signal=kind, reason=reason, identity=asdict(leader))
        try:
            os.fsync(events.file.fileno())
        except OSError:
            pass  # failed evidence must never disable the independent stop
        if not self_is_owner(leader):
            raise Refusal('self-identity-lost-before-signal')
        os.killpg(os.getpgrp(), signal.SIGTERM if kind == 'TERM' else signal.SIGKILL)

    try:
        while True:
            now = time.monotonic()
            try:
                packet = channel.receive()
                if packet:
                    kind, data = packet
                    if kind == 'START' and child is None and state.stop_at is None:
                        state.heartbeat(now)
                        read_fd, write_fd = os.pipe()
                        output = open(log_dir / 'workload.log', 'xb', buffering=0)
                        child = os.fork()
                        if child == 0:
                            try:
                                reset_worker_signals()
                                channel.sock.close()
                                os.close(slot_fd)
                                events.close()
                                output.close()
                                os.close(read_fd)
                                os.dup2(write_fd, 1)
                                os.dup2(write_fd, 2)
                                os.close(write_fd)
                                null_fd = os.open('/dev/null', os.O_RDONLY)
                                os.dup2(null_fd, 0)
                                os.close(null_fd)
                                os.chdir(job['cwd'])
                                env = os.environ.copy()
                                env.update(job['env'])
                                os.execvpe(job['command'][0], job['command'], env)
                            except BaseException:
                                os._exit(127)
                        os.close(write_fd)
                        pipe = read_fd
                        os.set_blocking(pipe, False)
                        record('worker-launched', pid=child)
                        channel.send('STARTED', pid=child)
                    elif kind == 'HEARTBEAT' and child is not None:
                        state.heartbeat(now)
                    elif kind == 'STOP':
                        state.request(now, str(data.get('reason', 'requested'))[:256])
                    else:
                        raise Refusal('invalid-control-transition')
            except Exception as exc:
                state.request(now, 'control-failure:' + type(exc).__name__)
            if now - started >= job['limits']['max_seconds']:
                state.request(now, 'supervisor-runtime-limit')
            # Drain at most 64 KiB per turn so a noisy child cannot starve heartbeat.
            if pipe is not None:
                try:
                    chunk = os.read(pipe, 65536)
                    if chunk:
                        remaining = MAX_OUTPUT - output_bytes
                        if output.write(chunk[:remaining]) != min(len(chunk), remaining):
                            raise Refusal('short-workload-log-write')
                        output_bytes += min(len(chunk), remaining)
                        if len(chunk) > remaining:
                            state.request(now, 'workload-output-limit')
                    else:
                        os.close(pipe)
                        pipe = None
                except BlockingIOError:
                    pass
                except Exception:
                    state.request(now, 'workload-log-failure')
            if child is not None and child_status is None:
                reaped, status = os.waitpid(child, os.WNOHANG)
                if reaped:
                    child_status = os.waitstatus_to_exitcode(status)
                    record('worker-exit', returncode=child_status)
            state.tick(time.monotonic(), self_is_owner(leader), signal_own_group)
            # Keep supervisor pinned until no non-zombie children remain.
            if child_status is not None and time.monotonic() - last_group_check >= .2:
                last_group_check = time.monotonic()
                try:
                    live = provider.live_group(leader)
                    if not live and pipe is None:
                        stop_reason = state.reason
                        record('group-drained', returncode=child_status, reason=stop_reason)
                        channel.send('DONE', returncode=child_status, reason=stop_reason)
                        # Stay alive until monitor records/verifies the completion.
                        deadline = time.monotonic() + HEARTBEAT
                        while time.monotonic() < deadline:
                            packet = channel.receive()
                            if packet and packet[0] == 'ACK':
                                return 0 if stop_reason is None else 2
                            time.sleep(.02)
                        return 2
                except Exception as exc:
                    state.request(time.monotonic(), 'containment-monitor-failure:' + type(exc).__name__)
            if child is None and state.stop_at is not None:
                return 2     # no worker ever launched; no need to hold session
            time.sleep(.02)
    finally:
        if pipe is not None:
            os.close(pipe)
        if output:
            output.close()
        events.close()
        channel.sock.close()
        # Do not unlock the shared flock explicitly. Last close releases it.
        os.close(slot_fd)


def private_dir(path):
    path.mkdir(mode=0o700, parents=False, exist_ok=True)
    info = path.lstat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
        raise Refusal('directory-not-private-owned')


def validate_compile_argv(command):
    """GR-01/02: narrow argv grammar, not proof of executable/toolchain identity.

    The exact executable hash and pinned environment are checked by read_job.
    A leading +1.97.1 is the only supported explicit rustup proxy selector.
    Actual direct binaries may reject it; argv never establishes their version.
    """
    tool = Path(command[0]).name
    args = command[1:]
    if args and args[0].startswith('+'):
        if args[0] != '+1.97.1':
            raise Refusal('compile-incompatible-explicit-toolchain')
        args = args[1:]
    if not args:
        raise Refusal('compile-missing-arguments')
    if tool == 'rustc':
        # Reject additional/misplaced selector-like tokens conservatively.
        # A filename beginning '+' can instead be spelled './+filename.rs'.
        if any(arg.startswith('+') for arg in args):
            raise Refusal('rustc-ambiguous-explicit-toolchain')
        return

    subcommand, *controls = args
    if subcommand not in ('build', 'check', 'test', 'run', 'rustc'):
        raise Refusal('cargo-unsupported-subcommand')
    if '--' in controls:
        if subcommand not in ('test', 'run', 'rustc'):
            raise Refusal('cargo-unsupported-forwarding')
        # These trailing tokens belong to the program/test/compiler, not Cargo.
        controls = controls[:controls.index('--')]
    flags = {'--offline', '--locked', '--frozen', '--release', '--lib', '--bins',
             '--tests', '--all-targets', '--workspace', '--all-features',
             '--no-default-features', '--no-run', '--no-fail-fast', '--quiet',
             '--verbose'}
    values = {'--manifest-path', '--target-dir', '--target', '--package', '--bin',
              '--example', '--test', '--features', '--profile', '--message-format',
              '--color', '--exclude', '--jobs'}
    aliases = {'-p': '--package', '-F': '--features', '-q': '--quiet',
               '-v': '--verbose', '-j': '--jobs'}
    seen = set()
    index = 0
    while index < len(controls):
        token = controls[index]
        option, separator, value = token.partition('=')
        option = aliases.get(option, option)
        if token.startswith('-j') and token != '-j':
            option, separator, value = '--jobs', '=', token[2:]
        if option not in flags | values:
            raise Refusal('cargo-unsupported-or-ambiguous-option')
        if option in seen:
            raise Refusal('cargo-duplicate-option:' + option)
        seen.add(option)
        if option in flags:
            if separator:
                raise Refusal('cargo-flag-does-not-take-value')
        else:
            if not separator:
                index += 1
                if index >= len(controls):
                    raise Refusal('cargo-missing-option-value')
                value = controls[index]
            # Do not count an operand resembling another option as a control.
            if not value or value.startswith(('-', '+')):
                raise Refusal('cargo-ambiguous-option-value')
            if option == '--jobs' and value != '1':
                raise Refusal('cargo-jobs-must-be-one')
        index += 1
    if not {'--offline', '--locked', '--jobs'} <= seen:
        raise Refusal('cargo-missing-own-offline-locked-jobs1')
    if {'--quiet', '--verbose'} <= seen or {'--release', '--profile'} <= seen:
        raise Refusal('cargo-conflicting-options')


def read_job(path):
    with open(path, 'rb') as source:
        raw = source.read(65537)
    if len(raw) > 65536:
        raise Refusal('job-spec-too-large')
    job = json.loads(raw)
    required = {'job_id', 'run_id', 'candidate_sha', 'input_hashes', 'kind', 'containment', 'cwd', 'command', 'env', 'limits'}
    if set(job) != required:
        raise Refusal('job-schema')
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', job['job_id']) or job['run_id'] != RUN_ID:
        raise Refusal('job-identity')
    if not re.fullmatch(r'[a-f0-9]{40}', job['candidate_sha']):
        raise Refusal('candidate-sha')
    if job['kind'] not in ('compile', 'tiny-probe', 'qualification') or job['containment'] != 'inherited-group':
        raise Refusal('unsupported-job-kind-or-containment')
    if not Path(job['cwd']).is_absolute() or not Path(job['cwd']).is_dir():
        raise Refusal('cwd')
    if (not isinstance(job['command'], list) or not job['command'] or len(job['command']) > 128
            or not all(isinstance(x, str) and '\0' not in x for x in job['command'])
            or not Path(job['command'][0]).is_absolute()):
        raise Refusal('command')
    if not isinstance(job['env'], dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in job['env'].items()):
        raise Refusal('environment')
    if not isinstance(job['input_hashes'], dict) or not job['input_hashes']:
        raise Refusal('input-hashes-required')
    for filename, expected in job['input_hashes'].items():
        if not Path(filename).is_absolute() or not re.fullmatch(r'[a-f0-9]{64}', expected):
            raise Refusal('input-hash-schema')
        digest = hashlib.sha256()
        with open(filename, 'rb') as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b''):
                digest.update(chunk)
        if digest.hexdigest() != expected:
            raise Refusal('input-hash-mismatch')
    if job['command'][0] not in job['input_hashes']:
        raise Refusal('executable-hash-required')
    limits = Limits(**job['limits'])
    limits.validate()
    if job['kind'] == 'compile':
        if Path(job['command'][0]).name not in ('cargo', 'rustc'):
            raise Refusal('compile-must-be-direct-cargo-or-rustc')
        expected = {'RUSTUP_TOOLCHAIN': '1.97.1', 'RUSTUP_AUTO_INSTALL': '0',
                    'CARGO_INCREMENTAL': '0', 'CARGO_BUILD_JOBS': '1', 'RUST_TEST_THREADS': '1'}
        if any(job['env'].get(k) != v for k, v in expected.items()):
            raise Refusal('compile-environment-not-pinned-and-serial')
        validate_compile_argv(job['command'])
    return job, hashlib.sha256(raw).hexdigest()


def run(runtime, job_path):
    job, spec_hash = read_job(job_path)
    runtime = runtime.absolute()
    if runtime.resolve() != runtime:
        raise Refusal('runtime-path-must-be-canonical-without-symlinks')
    private_dir(runtime)
    guard_dir, logs_dir = runtime / 'guard', runtime / 'logs'
    private_dir(guard_dir)
    private_dir(logs_dir)
    slot = os.open(guard_dir / 'slot.lock', os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
    info = os.fstat(slot)
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
        os.close(slot)
        raise Refusal('unsafe-slot-lock')
    try:
        fcntl.flock(slot, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(slot)
        raise Refusal('heavy-slot-busy')
    active = guard_dir / 'ACTIVE.json'
    if active.exists():
        os.close(slot)
        raise Refusal('previous-job-not-cleared-by-root')
    log_dir = logs_dir / job['job_id']
    log_dir.mkdir(mode=0o700)       # never reuse or overwrite job evidence
    events = Events(log_dir / 'monitor.jsonl')
    events.emit('job', job=job, spec_sha256=spec_hash, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    limits = Limits(**job['limits'])
    supervisor_pid = None
    channel = None
    result = 2
    try:
        provider = MacProvider(log_dir, trace=events.emit)
        monitor_identity, _ = provider.identity(os.getpid())
        events.emit('monitor-identity', identity=asdict(monitor_identity))
        baseline = None
        for index in range(3):
            sample = provider.sample()
            if baseline is None:
                baseline = sample
            reason = assess(sample, baseline, limits, time.monotonic(), admission=True)
            events.emit('preflight', sample=asdict(sample), reason=reason)
            if reason:
                raise Refusal(reason)
            if index < 2:
                time.sleep(INTERVAL)
        # Revalidate freshness after final quiet-sample spacing, before launch.
        sample.validate(time.monotonic())
        with open(active, 'x') as handle:
            json.dump({'job_id': job['job_id'], 'spec_sha256': spec_hash, 'status': 'active-or-unresolved'}, handle)
        left, right = socket.socketpair(socket.AF_UNIX, socket.SOCK_DGRAM)
        nonce = secrets.token_hex(32)
        supervisor_pid = os.fork()
        if supervisor_pid == 0:
            left.close()
            events.close()
            fresh_pid, fresh_uid, fresh_euid = os.getpid(), os.getuid(), os.geteuid()
            try:
                code = supervisor(Channel(right, nonce), slot, job, log_dir)
            except BaseException:
                # If failure occurs before/after workload launch, supervisor's
                # outer safety fallback owns its current session only. This
                # branch cannot guess a historical PGID. The ACTIVE latch stays.
                if (os.getpid() == fresh_pid == os.getpgrp() == os.getsid(0)
                        and os.getuid() == fresh_uid and os.geteuid() == fresh_euid):
                    os.killpg(os.getpgrp(), signal.SIGKILL)
                code = 2
            os._exit(code)
        right.close()
        channel = Channel(left, nonce)
        leader = None
        launched = False
        finished = False
        healthy_completion = False
        stop = None
        monitor_state = MonitorState()
        launch_at = time.monotonic()
        next_sample = launch_at
        stop_deadline = None
        while True:
            now = time.monotonic()
            packet = channel.receive()
            if packet:
                kind, data = packet
                events.emit('control-received', control_kind=kind, data=data)
                if kind == 'READY' and leader is None and not launched:
                    leader = Identity(**data['identity'])
                    actual, zombie = provider.identity(supervisor_pid)
                    if (actual != leader or zombie or leader.pid != supervisor_pid or leader.sid != supervisor_pid
                            or leader.pgid != supervisor_pid or leader.uid != os.geteuid() or leader.ruid != os.getuid()
                            or os.getpgrp() == leader.pgid):
                        raise Refusal('supervisor-authentication-failed')
                    with open(log_dir / 'registry.json', 'x') as registry:
                        json.dump({'run_id': RUN_ID, 'job_id': job['job_id'], 'spec_sha256': spec_hash,
                                   'monitor': asdict(monitor_identity), 'supervisor': asdict(leader),
                                   'channel_binding_sha256': hashlib.sha256(nonce.encode()).hexdigest(),
                                   'limits': job['limits'], 'candidate_sha': job['candidate_sha'],
                                   'input_hashes': job['input_hashes']}, registry, indent=2)
                    sample = provider.sample(leader)
                    reason = assess(sample, baseline, limits, time.monotonic(), admission=True)
                    events.emit('prelaunch', sample=asdict(sample), identity=asdict(leader), reason=reason)
                    if reason:
                        raise Refusal(reason)
                    channel.send('START')
                    launched = True
                    next_sample = time.monotonic()
                elif kind == 'STARTED' and launched:
                    pass
                elif kind == 'DONE' and launched and leader is not None:
                    actual, zombie = provider.identity(supervisor_pid)
                    validate_member(leader, actual, leader)
                    _, _, live, _ = provider.group(leader, time.monotonic() + 1)
                    if zombie or live:
                        raise Refusal('completion-not-drained')
                    healthy_completion = data['reason'] is None and stop is None
                    # A contained, normally completed failing test releases the
                    # slot too. Guard refusal remains distinct in the record.
                    result = 0 if healthy_completion and data['returncode'] == 0 else 2
                    events.emit('result', result=result, guard_healthy=healthy_completion, workload_returncode=data['returncode'], stop_reason=data['reason'])
                    channel.send('ACK')
                    finished = True
                    break
                else:
                    raise Refusal('unexpected-supervisor-control')
            if leader is None and now - launch_at >= HEARTBEAT:
                raise Refusal('supervisor-startup-timeout')
            if launched and now >= next_sample and stop is None:
                def observe():
                    sample = provider.sample(leader)
                    events.emit('sample', sample=asdict(sample), members=[asdict(x) for x in provider.known.values()])
                    if time.monotonic() - launch_at >= limits.max_seconds:
                        raise Refusal('runtime-limit')
                    return sample
                reason = monitor_state.step(observe, lambda kind, why: channel.send(kind, reason=why),
                                            baseline, limits, time.monotonic)
                if reason:
                    stop = reason
                    events.emit('stop-request', reason=reason)
                    stop_deadline = time.monotonic() + HEARTBEAT + TERM_GRACE + 2
                next_sample = time.monotonic() + INTERVAL
            reaped, status = os.waitpid(supervisor_pid, os.WNOHANG)
            if reaped:
                supervisor_pid = None
                events.emit('supervisor-exit-before-ack', returncode=os.waitstatus_to_exitcode(status), reason=stop)
                break
            if stop_deadline is not None and now >= stop_deadline:
                raise Refusal('stop-not-confirmed-within-budget')
            time.sleep(.02)
        if finished and supervisor_pid is not None:
            deadline = time.monotonic() + 1
            while time.monotonic() < deadline:
                reaped, status = os.waitpid(supervisor_pid, os.WNOHANG)
                if reaped:
                    supervisor_pid = None
                    if os.waitstatus_to_exitcode(status) != 0:
                        result = 2
                        healthy_completion = False
                    break
                time.sleep(.02)
            if supervisor_pid is not None:
                result = 2
                healthy_completion = False
        if healthy_completion:
            active.unlink()
        return result
    except BaseException as exc:
        try:
            events.emit('refusal-or-failure', error=type(exc).__name__, detail=str(exc)[:1024])
        except Exception:
            pass
        if channel is not None:
            try:
                channel.send('STOP', reason='monitor-exception-or-interruption')
            except Exception:
                pass
        # No external kill fallback. Socket closure / heartbeat loss drives the
        # live supervisor's watchdog. ACTIVE remains latched; no automatic retry.
        return 2
    finally:
        if channel is not None:
            channel.sock.close()
        events.close()
        os.close(slot)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['run'])
    parser.add_argument('--runtime-dir', required=True, type=Path)
    parser.add_argument('--job-spec', required=True, type=Path)
    args = parser.parse_args()
    try:
        return run(args.runtime_dir, args.job_spec)
    except Exception as exc:
        print('host_guard refusal: ' + type(exc).__name__ + ': ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
