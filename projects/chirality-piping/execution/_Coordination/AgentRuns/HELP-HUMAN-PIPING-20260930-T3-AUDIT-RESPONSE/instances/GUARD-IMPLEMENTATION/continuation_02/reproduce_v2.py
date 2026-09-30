"""Frozen pure zombie-snapshot -> ESRCH reproducer; native calls are Python fakes."""
from contextlib import ExitStack
import ctypes as C
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[2]
BLOCKED = ('os.kill', 'os.killpg', 'os.fork', 'os.execvpe', 'os.execve', 'os.setsid',
           'os.setpgid', 'os._exit', 'fcntl.flock', 'subprocess.Popen', 'ctypes.CDLL',
           'socket.socketpair', 'signal.signal', 'time.sleep', 'os.getsid', 'os.getpgid',
           'os.getpgrp', 'os.getpid', 'os.getuid', 'os.geteuid')

def blocked(*a, **kw):
    raise AssertionError('LIVE CAPABILITY FORBIDDEN')

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module
    with ExitStack() as fence:
        for target in BLOCKED:
            fence.enter_context(patch(target, side_effect=blocked))
        spec.loader.exec_module(module)
    return module

def reproduce():
    guard = load('v2_exit_repro', RUN/'tools/host_guard_v2.py')
    with ExitStack() as fence:
        for target in BLOCKED:
            fence.enter_context(patch(target, side_effect=blocked))
        fence.enter_context(patch('os.getsid', return_value=100))
        fence.enter_context(patch('time.monotonic', return_value=100.0))
        provider = object.__new__(guard.MacProvider)
        provider.known = {}; provider.trace = None
        leader = guard.Identity(100, 12000, 50, 501, 501, 100, 100)
        rows = {100: guard.Row(100, 2, 100, 501, False),
                101: guard.Row(101, 100, 100, 501, True)}
        calls = []
        provider.table = lambda deadline: rows
        def info(pid, flavor, arg, raw, size):
            calls.append({'operation':'proc_pidinfo','pid':pid})
            if pid == 101:
                C.set_errno(3); return 0
            obj = C.cast(raw, C.POINTER(guard.BSDInfo)).contents
            obj.pid=100;obj.uid=obj.ruid=501;obj.pgid=100
            obj.start_sec=12000;obj.start_usec=50;obj.status=2
            return size
        def usage(pid, flavor, raw):
            obj=C.cast(raw,C.POINTER(guard.RUsageV0)).contents
            obj.proc_start_abstime=1;obj.resident_size=100;obj.phys_footprint=80
            return 0
        provider.lib=SimpleNamespace(proc_pidinfo=info,proc_pid_rusage=usage)
        try:
            provider.group(leader,101.5)
            raise AssertionError('v2 unexpectedly accepted disappearing worker')
        except guard.Refusal as exc:
            assert str(exc)=='proc-pidinfo-denied-missing-short:3'
            return {'control':'frozen v2','fake_native_only':True,'snapshot_worker_state':'Z',
                    'fake_failure_pid':101,'historical_B02_failed_call_pid':'not recorded; not inferred',
                    'refusal':str(exc),'native_calls':calls,
                    'proposed_fresh_complete_next_snapshot_pids':[100],
                    'v2_queries_fresh_absence':False}

if __name__=='__main__':
    print(json.dumps(reproduce(),indent=2))
