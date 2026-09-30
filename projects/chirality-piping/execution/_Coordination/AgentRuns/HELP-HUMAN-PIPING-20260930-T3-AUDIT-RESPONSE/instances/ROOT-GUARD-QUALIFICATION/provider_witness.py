"""Read-only live provider witness; ROOT runs only after independent review."""
import ctypes
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time


def main():
    source, runtime = (Path(x).resolve() for x in sys.argv[1:3])
    spec = importlib.util.spec_from_file_location('reviewed_host_guard', source)
    guard = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = guard
    spec.loader.exec_module(guard)
    trace = []
    provider = guard.MacProvider(runtime / 'logs', trace=lambda kind, **data: trace.append({'kind': kind, **data}))
    rows = []
    identity = None
    for index in range(3):
        started = time.monotonic()
        current, zombie = provider.identity(os.getpid())
        current_tuple = (current.pid, current.uid, current.ruid, current.pgid, current.sid)
        expected = (os.getpid(), os.geteuid(), os.getuid(), os.getpgrp(), os.getsid(0))
        assert current_tuple == expected and not zombie
        assert identity is None or current == identity
        identity = current
        usage = guard.RUsageV0()
        rc = provider.lib.proc_pid_rusage(os.getpid(), 0, ctypes.cast(ctypes.byref(usage), ctypes.POINTER(ctypes.c_void_p)))
        assert rc == 0 and usage.proc_start_abstime > 0 and usage.proc_exit_abstime == 0
        sample = provider.sample()
        rss_crosscheck = guard.bounded_command(['/bin/ps', '-p', str(os.getpid()), '-o', 'rss='], time.monotonic() + 1.5)
        assert rss_crosscheck.strip().isdigit()
        rows.append({'index': index, 'started': started, 'finished': time.monotonic(), 'identity': guard.asdict(current), 'sample': guard.asdict(sample), 'own_rss_bytes': usage.resident_size, 'own_footprint_bytes': usage.phys_footprint, 'ps_own_rss_kib': int(rss_crosscheck.strip())})
        if index < 2:
            time.sleep(1)
    print(json.dumps({'kind': 'read-only-provider-witness', 'guard_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'platform': platform.platform(), 'python': sys.version, 'samples': rows, 'provider_trace': trace}, indent=2))


if __name__ == '__main__':
    main()
