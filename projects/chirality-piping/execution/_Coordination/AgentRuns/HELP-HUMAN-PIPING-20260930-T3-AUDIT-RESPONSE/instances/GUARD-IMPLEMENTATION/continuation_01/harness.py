"""Additive capability-fenced loader; the sealed 41 tests are never rewritten."""
from contextlib import ExitStack
import importlib.util
from pathlib import Path
import sys
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ORIGINAL_TESTS = HERE.parent / 'test_host_guard.py'
V2 = HERE.parents[2] / 'tools' / 'host_guard_v2.py'
# Keep import fenced before importing even the original harness itself.
FORBIDDEN = ('os.kill', 'os.killpg', 'os.fork', 'os.execvpe', 'os.execve',
             'os.setsid', 'os.setpgid', 'os._exit', 'fcntl.flock',
             'subprocess.Popen', 'ctypes.CDLL', 'socket.socketpair',
             'signal.signal', 'time.sleep', 'os.getsid', 'os.getpgid',
             'os.getpgrp', 'os.getpid', 'os.getuid', 'os.geteuid')


def blocked(*args, **kwargs):
    raise AssertionError('LIVE CAPABILITY FORBIDDEN IN PURE TESTS')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    with ExitStack() as fence:
        for target in FORBIDDEN:
            fence.enter_context(patch(target, side_effect=blocked))
        spec.loader.exec_module(module)
    return module


original = load('sealed_guard_tests_against_v2', ORIGINAL_TESTS)
assert original.FORBIDDEN == FORBIDDEN
original_guard = original.guard
v2 = load('host_guard_v2', V2)
# Every original test refers to its module's guard global. Rebinding that
# reference runs the unchanged behavioral assertions against v2's objects.
original.guard = v2
assert original.guard is v2
