"""Pure tests: real process, signal, native-provider and socket creation blocked."""
import ctypes
from contextlib import ExitStack
from types import SimpleNamespace
from dataclasses import replace
import importlib.util
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

def blocked(*args, **kwargs):
    raise AssertionError('LIVE CAPABILITY FORBIDDEN IN PURE TESTS')


FORBIDDEN = ('os.kill', 'os.killpg', 'os.fork', 'os.execvpe', 'os.execve',
             'os.setsid', 'os.setpgid', 'os._exit', 'fcntl.flock',
             'subprocess.Popen', 'ctypes.CDLL', 'socket.socketpair',
             'signal.signal', 'time.sleep', 'os.getsid', 'os.getpgid',
             'os.getpgrp', 'os.getpid', 'os.getuid', 'os.geteuid')
SOURCE = Path(__file__).resolve().parents[2] / 'tools' / 'host_guard.py'
spec = importlib.util.spec_from_file_location('host_guard', SOURCE)
guard = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = guard
with ExitStack() as import_fence:
    for target in FORBIDDEN:
        import_fence.enter_context(patch(target, side_effect=blocked))
    spec.loader.exec_module(guard)  # a future import-time effect fails here


class PureCase(unittest.TestCase):
    def setUp(self):
        # Every test blocks live side effects, even if an assertion accidentally
        # reaches adapter code. No signals, socket creation, fork or commands.
        for target in FORBIDDEN:
            self.enterContext(patch(target, side_effect=blocked))
        self.base = guard.Sample(100, 16 * guard.GIB, 68, 1, 3 * guard.GIB, 700,
                                 100 * guard.GIB, 12 * guard.MIB, 10 * guard.MIB)
        self.limits = guard.Limits(128 * guard.MIB, 64 * guard.MIB,
                                  64 * guard.MIB, guard.GIB, 30)
        self.leader = guard.Identity(100, 12000, 50, 501, 501, 100, 100)
        self.worker = guard.Identity(101, 12000, 60, 501, 501, 100, 100)
        self.sentinel = guard.Identity(900, 11000, 1, 501, 501, 900, 900)

    def decision(self, **delta):
        return guard.assess(replace(self.base, **delta), self.base, self.limits, 100)


class Metrics(PureCase):
    def test_high_baseline_swap_stable_is_not_pressure(self):
        self.assertIsNone(self.decision())
        self.assertIsNone(guard.assess(self.base, self.base, self.limits, 100, admission=True))

    def test_new_swap_growth_and_swapouts(self):
        self.assertIsNone(self.decision(swap_used_bytes=self.base.swap_used_bytes + 64 * guard.MIB - 1))
        self.assertEqual(self.decision(swap_used_bytes=self.base.swap_used_bytes + 64 * guard.MIB), 'swap-growth-at-least-64MiB')
        self.assertEqual(self.decision(swapouts=701), 'new-swapouts')
        self.assertEqual(self.decision(swapouts=699), 'swap-counter-reset')

    def test_quiet_admission_requires_unchanged_swap(self):
        changed = replace(self.base, swap_used_bytes=self.base.swap_used_bytes + 1)
        self.assertEqual(guard.assess(changed, self.base, self.limits, 100, True), 'quiet-swap-baseline-unstable')

    def test_stop_before_35_percent_policy_floor(self):
        self.assertIsNone(self.decision(available_pct=40.01))
        for pct in (40, 35, 0):
            self.assertEqual(self.decision(available_pct=pct), 'available-at-or-below-40pct')

    def test_projection_consumes_full_cap_and_allowance(self):
        limits = replace(self.limits, cap_bytes=2 * guard.GIB, allowance_bytes=guard.GIB)
        # 58.75 - 18.75 = 40; equality refuses.
        self.assertEqual(guard.assess(replace(self.base, available_pct=58.75), self.base, limits, 100, True),
                         'projected-available-at-or-below-40pct')
        self.assertIsNone(guard.assess(replace(self.base, available_pct=58.76), self.base, limits, 100, True))

    def test_rss_and_footprint_are_independent_caps(self):
        self.assertEqual(self.decision(rss_bytes=self.limits.cap_bytes), 'rss-cap')
        self.assertEqual(self.decision(footprint_bytes=self.limits.cap_bytes), 'footprint-cap')
        self.assertIsNone(self.decision(rss_bytes=self.limits.cap_bytes-1, footprint_bytes=self.limits.cap_bytes-1))

    def test_pressure_unknown_values_stop(self):
        for value in (0, 2, 4, 999):
            self.assertEqual(self.decision(pressure=value), 'pressure-not-normal')

    def test_disk_and_total_changes_stop(self):
        self.assertEqual(self.decision(disk_free_bytes=self.limits.disk_write_budget_bytes + self.limits.disk_reserve_bytes),
                         'insufficient-disk-headroom')
        self.assertEqual(self.decision(total_bytes=8 * guard.GIB), 'memory-total-changed')

    def test_invalid_nan_negative_types(self):
        for field in self.base.__dataclass_fields__:
            for value in (-1, float('nan'), float('inf'), None, True, '12'):
                with self.subTest(field=field, value=repr(value)), self.assertRaises(guard.Refusal):
                    replace(self.base, **{field: value}).validate(100)
        with self.assertRaises(guard.Refusal):
            replace(self.base, available_pct=101).validate(100)
        with self.assertRaises(guard.Refusal):
            replace(self.base, total_bytes=0).validate(100)

    def test_stale_future_and_exact_age(self):
        self.base.validate(102)
        for now in (102.001, 99):
            with self.assertRaises(guard.Refusal):
                self.base.validate(now)

    def test_limits_enforce_ceiling_and_evidence_budget(self):
        for limits in (replace(self.limits, cap_bytes=2 * guard.GIB+1),
                       replace(self.limits, max_seconds=3601),
                       replace(self.limits, allowance_bytes=0),
                       replace(self.limits, disk_write_budget_bytes=1)):
            with self.assertRaises(guard.Refusal):
                limits.validate()


class Parsers(PureCase):
    def test_percentage(self):
        self.assertEqual(guard.parse_percentage('System-wide memory free percentage: 68%\n'), 68)
        for raw in ('', 'System-wide memory free percentage: NaN%',
                    'System-wide memory free percentage: -1%',
                    'System-wide memory free percentage: 101%',
                    'System-wide memory free percentage: 1%\nSystem-wide memory free percentage: 2%'):
            with self.assertRaises(guard.Refusal):
                guard.parse_percentage(raw)

    def test_swap_and_vm_stat(self):
        raw = 'total = 4096.00M  used = 3118.19M  free = 977.81M  (encrypted)\n'
        self.assertEqual(guard.parse_swap(raw), int(3118.19 * guard.MIB))
        for raw in ('', 'denied', 'total = 1M used = 2M free = 0M',
                    'total = 4M used = NaNM free = 0M', 'total = 4M used = -1M free = 5M'):
            with self.assertRaises(guard.Refusal):
                guard.parse_swap(raw)
        self.assertEqual(guard.parse_swapouts('Swapouts: 123.\n'), 123)
        for raw in ('Swapouts: -1.', 'Swapouts: 1.5.', '', 'Swapouts: 1.\nSwapouts: 2.'):
            with self.assertRaises(guard.Refusal):
                guard.parse_swapouts(raw)

    def test_process_table(self):
        result = guard.parse_rows('100 1 100 501 S\n101 100 100 501 Z+\n900 1 900 501 Ss\n')
        self.assertEqual(set(result), {100, 101, 900})
        self.assertTrue(result[101].zombie)
        for raw in ('', '100 bad 100 501 S', '100 1 100 501 S\n100 1 100 501 S', 'pid ppid uid pgid'):
            with self.assertRaises(guard.Refusal):
                guard.parse_rows(raw)


class Ownership(PureCase):
    def rows(self):
        return {100: guard.Row(100, 2, 100, 501, False),
                101: guard.Row(101, 100, 100, 501, False),
                900: guard.Row(900, 2, 900, 501, False)}

    def test_unrelated_sentinel_never_selected(self):
        selected = guard.select_members(self.rows(), self.leader, {})
        self.assertEqual(selected, {100, 101})
        self.assertNotIn(self.sentinel.pid, selected)

    def test_leader_loss_and_escaped_groups(self):
        rows = self.rows()
        del rows[100]
        with self.assertRaisesRegex(guard.Refusal, 'leader-loss'):
            guard.select_members(rows, self.leader, {})
        rows = self.rows()
        rows[101] = replace(rows[101], pgid=101)
        with self.assertRaisesRegex(guard.Refusal, 'escaped'):
            guard.select_members(rows, self.leader, {})
        rows[101] = replace(rows[101], ppid=1)
        with self.assertRaisesRegex(guard.Refusal, 'escaped'):
            guard.select_members(rows, self.leader, {101: self.worker})

    def test_changed_uid_and_session(self):
        rows = self.rows()
        rows[101] = replace(rows[101], uid=502)
        with self.assertRaises(guard.Refusal):
            guard.select_members(rows, self.leader, {})
        for delta in ({'uid': 502}, {'ruid': 502}, {'sid': 99}, {'pgid': 101}):
            with self.assertRaises(guard.Refusal):
                guard.validate_member(None, replace(self.worker, **delta), self.leader)

    def test_reused_pid_start_mismatch_refuses(self):
        for delta in ({'start_sec': 12001}, {'start_usec': 51}, {'pid': 900}):
            with self.assertRaisesRegex(guard.Refusal, 'pid-reused'):
                guard.validate_member(self.worker, replace(self.worker, **delta), self.leader)

    def test_descendants_and_members_are_bounded(self):
        rows = self.rows()
        rows[102] = guard.Row(102, 101, 100, 501, False)
        self.assertEqual(guard.select_members(rows, self.leader, {}), {100, 101, 102})
        for pid in range(1000, 1000 + guard.MAX_MEMBERS):
            rows[pid] = guard.Row(pid, 100, 100, 501, False)
        with self.assertRaisesRegex(guard.Refusal, 'too-many'):
            guard.select_members(rows, self.leader, {})

    def test_invalid_identity(self):
        for delta in ({'start_usec': 1000000}, {'uid': -1}, {'pid': True}, {'sid': 0}):
            with self.assertRaises(guard.Refusal):
                replace(self.leader, **delta).validate()


class StateMachines(PureCase):
    def test_monitor_success_only_sends_heartbeat(self):
        calls = []
        state = guard.MonitorState()
        self.assertIsNone(state.step(lambda: self.base, lambda *v: calls.append(v), self.base, self.limits, lambda: 100))
        self.assertEqual(calls, [('HEARTBEAT', '')])

    def test_monitor_failure_requests_stop_once_through_fake_control(self):
        for exception in (PermissionError('denied'), guard.Refusal('leader-loss'),
                          guard.Refusal('pid-reused'), ValueError('malformed'), RuntimeError('lost')):
            calls = []
            state = guard.MonitorState()
            def provider():
                raise exception
            state.step(provider, lambda *v: calls.append(v), self.base, self.limits, 100)
            state.step(provider, lambda *v: calls.append(v), self.base, self.limits, 101)
            self.assertEqual(len(calls), 1)
            self.assertEqual(calls[0][0], 'STOP')
            # No identity or PGID is ever handed to the control sink.
            self.assertEqual(len(calls[0]), 2)

    def test_stale_monitoring_stops(self):
        calls = []
        state = guard.MonitorState()
        state.step(lambda: self.base, lambda *v: calls.append(v), self.base, self.limits, 103)
        self.assertEqual(calls[0][0], 'STOP')

    def test_monitor_cap_crossing_stops(self):
        calls = []
        state = guard.MonitorState()
        state.step(lambda: replace(self.base, footprint_bytes=self.limits.cap_bytes),
                   lambda *v: calls.append(v), self.base, self.limits, 100)
        self.assertEqual(calls, [('STOP', 'footprint-cap')])

    def test_heartbeat_loss_terms_then_kills_with_grace(self):
        calls = []
        state = guard.StopState(10)
        state.tick(12.999, True, lambda *v: calls.append(v))
        self.assertEqual(calls, [])
        state.tick(13, True, lambda *v: calls.append(v))
        state.tick(14.999, True, lambda *v: calls.append(v))
        self.assertEqual(calls, [('TERM', 'heartbeat-loss')])
        state.tick(15, True, lambda *v: calls.append(v))
        state.tick(20, True, lambda *v: calls.append(v))
        self.assertEqual(calls, [('TERM', 'heartbeat-loss'), ('KILL', 'heartbeat-loss')])

    def test_authentication_loss_never_signals(self):
        calls = []
        state = guard.StopState(10)
        state.request(10, 'requested')
        with self.assertRaises(guard.Refusal):
            state.tick(10, False, lambda *v: calls.append(v))
        self.assertEqual(calls, [])
        state.tick(10, True, lambda *v: calls.append(v))
        with self.assertRaises(guard.Refusal):
            state.tick(12, False, lambda *v: calls.append(v))
        self.assertEqual(calls, [('TERM', 'requested')])

    def test_late_heartbeat_does_not_cancel_stop(self):
        calls = []
        state = guard.StopState(10)
        state.request(11, 'memory-cap')
        state.heartbeat(12)
        state.tick(13, True, lambda *v: calls.append(v))
        self.assertEqual(calls, [('TERM', 'memory-cap'), ('KILL', 'memory-cap')])

    def test_worker_resets_handlers_to_default(self):
        # Fake handler sink overrides global safety patch only for this call.
        calls = []
        with patch('signal.signal', side_effect=lambda *v: calls.append(v)):
            guard.reset_worker_signals()
        self.assertIn((guard.signal.SIGTERM, guard.signal.SIG_DFL), calls)
        self.assertTrue(all(handler == guard.signal.SIG_DFL for _, handler in calls))

    def test_live_capabilities_are_blocked(self):
        for fn in (guard.os.killpg, guard.os.fork, guard.C.CDLL, guard.socket.socketpair, guard.subprocess.Popen):
            with self.assertRaisesRegex(AssertionError, 'FORBIDDEN'):
                fn()


class JobSchema(PureCase):
    def test_executable_exact_path_hash_is_required_and_checked(self):
        executable = b'fake executable bytes'
        unrelated = b'an unrelated input is not an executable pin'
        job = {
            'job_id': 'pure-schema', 'run_id': guard.RUN_ID,
            'candidate_sha': 'a' * 40, 'kind': 'qualification',
            'containment': 'inherited-group', 'cwd': '/fake/workspace',
            'command': ['/fake/program'], 'env': {},
            'input_hashes': {'/fake/input': guard.hashlib.sha256(unrelated).hexdigest()},
            'limits': guard.asdict(self.limits),
        }
        def fake_open(path, mode):
            self.assertEqual(mode, 'rb')
            values = {'/fake/job.json': json.dumps(job).encode(),
                      '/fake/program': executable, '/fake/input': unrelated}
            return io.BytesIO(values[str(path)])
        with patch('builtins.open', side_effect=fake_open), patch.object(Path, 'is_dir', return_value=True):
            with self.assertRaisesRegex(guard.Refusal, 'executable-hash-required'):
                guard.read_job(Path('/fake/job.json'))
            job['input_hashes']['/fake/program'] = '0' * 64
            with self.assertRaisesRegex(guard.Refusal, 'input-hash-mismatch'):
                guard.read_job(Path('/fake/job.json'))
            job['input_hashes']['/fake/program'] = guard.hashlib.sha256(executable).hexdigest()
            observed, digest = guard.read_job(Path('/fake/job.json'))
            self.assertEqual(observed, job)
            self.assertEqual(digest, guard.hashlib.sha256(json.dumps(job).encode()).hexdigest())


class NativeAdapterFakes(PureCase):
    def fake_provider(self):
        provider = object.__new__(guard.MacProvider)
        provider.known = {}
        provider.trace = None
        return provider

    def test_live_group_enumeration_uses_bytes_and_preserves_sentinel(self):
        provider = self.fake_provider()
        def listing(kind, pgid, buffer, size):
            self.assertEqual((kind, pgid), (2, 100))
            buffer[0], buffer[1] = 100, 101
            return 2 * ctypes.sizeof(ctypes.c_int)
        provider.lib = SimpleNamespace(proc_listpids=listing)
        provider.identity = lambda pid: ({100: self.leader, 101: self.worker}[pid], False)
        self.assertEqual(provider.live_group(self.leader), [101])
        self.assertNotIn(self.sentinel.pid, provider.live_group(self.leader))

    def test_group_empty_of_workers_requires_live_leader(self):
        provider = self.fake_provider()
        def listing(kind, pgid, buffer, size):
            buffer[0] = 100
            return 4
        provider.lib = SimpleNamespace(proc_listpids=listing)
        provider.identity = lambda pid: (self.leader, False)
        self.assertEqual(provider.live_group(self.leader), [])

    def test_group_denied_short_truncated_missing_leader(self):
        provider = self.fake_provider()
        provider.identity = blocked
        for value in (0, -1, 1, (guard.MAX_MEMBERS + 1) * 4):
            provider.lib = SimpleNamespace(proc_listpids=lambda *args: value)
            with self.assertRaises(guard.Refusal):
                provider.live_group(self.leader)
        def listing(kind, pgid, buffer, size):
            buffer[0] = 101
            return 4
        provider.lib = SimpleNamespace(proc_listpids=listing)
        with self.assertRaises(guard.Refusal):
            provider.live_group(self.leader)

    def test_identity_provider_denied_or_short_fails_closed(self):
        provider = self.fake_provider()
        for returned in (0, -1, ctypes.sizeof(guard.BSDInfo)-1):
            provider.lib = SimpleNamespace(proc_pidinfo=lambda *args: returned)
            with self.assertRaisesRegex(guard.Refusal, 'denied-missing-short'):
                provider.identity(100)

    def test_identity_uses_pid_start_uid_and_session(self):
        provider = self.fake_provider()
        def info(pid, flavor, arg, raw, size):
            self.assertEqual((pid, flavor, arg, size), (100, 3, 0, 136))
            value = ctypes.cast(raw, ctypes.POINTER(guard.BSDInfo)).contents
            value.pid, value.uid, value.ruid, value.pgid = 100, 501, 501, 100
            value.start_sec, value.start_usec = 12000, 50
            value.status = 2
            return size
        provider.lib = SimpleNamespace(proc_pidinfo=info)
        with patch('os.getsid', return_value=100):
            self.assertEqual(provider.identity(100), (self.leader, False))

    def test_identity_race_or_session_change_refuses(self):
        provider = self.fake_provider()
        count = [0]
        def info(pid, flavor, arg, raw, size):
            count[0] += 1
            value = ctypes.cast(raw, ctypes.POINTER(guard.BSDInfo)).contents
            value.pid, value.uid, value.ruid, value.pgid = 100, 501, 501, 100
            value.start_sec, value.start_usec = 12000, count[0]
            return size
        provider.lib = SimpleNamespace(proc_pidinfo=info)
        with patch('os.getsid', return_value=100), self.assertRaisesRegex(guard.Refusal, 'identity-raced'):
            provider.identity(100)

    def test_self_owner_uses_current_identity_only(self):
        with ExitStack() as fake:
            for function, value in (('getpid', 100), ('getuid', 501), ('geteuid', 501),
                                    ('getpgrp', 100), ('getsid', 100)):
                fake.enter_context(patch('os.' + function, return_value=value))
            self.assertTrue(guard.self_is_owner(self.leader))
            self.assertFalse(guard.self_is_owner(replace(self.leader, pid=900)))
            self.assertFalse(guard.self_is_owner(replace(self.leader, uid=502)))
            self.assertFalse(guard.self_is_owner(replace(self.leader, sid=900)))


class FakeSocket:
    def __init__(self):
        self.raw = None
    def setblocking(self, value):
        pass
    def send(self, raw):
        self.raw = raw
        return len(raw)
    def recv(self, size):
        if self.raw is None:
            raise BlockingIOError()
        raw, self.raw = self.raw, None
        return raw


class AuthenticationAndBounds(PureCase):
    def test_authenticated_sequence_and_no_nonce_log(self):
        sock = FakeSocket()
        sender, receiver = guard.Channel(sock, 'secret'), guard.Channel(sock, 'secret')
        sender.send('STOP', reason='memory')
        self.assertEqual(receiver.receive(), ('STOP', {'reason': 'memory'}))
        sender.send('HEARTBEAT')
        saved = sock.raw
        self.assertEqual(receiver.receive(), ('HEARTBEAT', {}))
        sock.raw = saved
        with self.assertRaisesRegex(guard.Refusal, 'replayed'):
            receiver.receive()

    def test_wrong_nonce_and_oversize_rejected(self):
        sock = FakeSocket()
        sender, receiver = guard.Channel(sock, 'wrong'), guard.Channel(sock, 'right')
        sender.send('STOP')
        with self.assertRaises(guard.Refusal):
            receiver.receive()
        with self.assertRaisesRegex(guard.Refusal, 'limit'):
            sender.send('STOP', reason='x' * guard.MAX_PACKET)
        sock.raw = b'x' * (guard.MAX_PACKET+1)
        with self.assertRaises(guard.Refusal):
            receiver.receive()

    def test_event_log_limit_without_filesystem(self):
        events = object.__new__(guard.Events)
        events.file = io.BytesIO()
        events.count = 0
        events.emit('test', value=1)
        self.assertIn(b'"kind": "test"', events.file.getvalue())
        events.count = guard.MAX_EVENTS
        with self.assertRaisesRegex(guard.Refusal, 'event-log-limit'):
            events.emit('test')

    def test_sdk_declared_layout_pure_ctypes_only(self):
        # Layout calculation only: never loads libproc or executes ABI calls.
        self.assertEqual(ctypes.sizeof(guard.BSDInfo), 136)
        self.assertEqual(guard.BSDInfo.start_sec.offset, 120)
        self.assertEqual(ctypes.sizeof(guard.RUsageV0), 96)
        self.assertEqual(guard.RUsageV0.resident_size.offset, 64)
        self.assertEqual(guard.RUsageV0.phys_footprint.offset, 72)


if __name__ == '__main__':
    unittest.main(verbosity=2)
