import importlib.util
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('controller_v3', Path(__file__).with_name('qualify_case_v3.py'))
controller = importlib.util.module_from_spec(spec)
spec.loader.exec_module(controller)


class FakeChild:
    def __init__(self, stopped=False, wait_error=False):
        self.stopped, self.wait_error, self.alive = stopped, wait_error, True
        self.calls = []

    def poll(self):
        return None if self.alive else -9

    def kill(self):
        self.calls.append('kill'); self.alive = False

    def terminate(self):
        self.calls.append('terminate')
        if not self.stopped:
            self.alive = False

    def wait(self, timeout):
        self.calls.append('wait')
        if self.wait_error:
            raise OSError('injected wait failure')
        if self.alive:
            raise subprocess.TimeoutExpired('fake-child', timeout)
        return -9


class CleanupTests(unittest.TestCase):
    def setUp(self):
        self.fence = patch.object(subprocess, 'Popen', side_effect=AssertionError('no live process allowed'))
        self.fence.start(); self.addCleanup(self.fence.stop)

    def test_stopped_monitor_is_killed_and_sentinel_cleaned(self):
        monitor, sentinel, result = FakeChild(stopped=True), FakeChild(), {'errors': []}
        controller.cleanup_owned_children(monitor, sentinel, result)
        self.assertEqual(monitor.calls, ['kill', 'wait'])
        self.assertFalse(sentinel.alive)
        self.assertEqual(result['errors'], [])

    def test_monitor_wait_failure_still_cleans_sentinel_and_returns(self):
        monitor, sentinel, result = FakeChild(wait_error=True), FakeChild(), {'errors': []}
        controller.cleanup_owned_children(monitor, sentinel, result)
        self.assertFalse(sentinel.alive)
        self.assertEqual(len(result['errors']), 2)
        self.assertTrue(any('cleanup-monitor-unconfirmed' in error for error in result['errors']))

    def test_stopped_sentinel_gets_owned_handle_fallback_and_failure_record(self):
        sentinel, result = FakeChild(stopped=True), {'errors': []}
        controller.cleanup_owned_children(None, sentinel, result)
        self.assertEqual(sentinel.calls, ['terminate', 'wait', 'kill', 'wait'])
        self.assertFalse(sentinel.alive)
        self.assertEqual(len(result['errors']), 1)

    def test_reaped_children_are_not_signalled(self):
        monitor, sentinel, result = FakeChild(), FakeChild(), {'errors': []}
        monitor.alive = sentinel.alive = False
        controller.cleanup_owned_children(monitor, sentinel, result)
        self.assertEqual(monitor.calls, ['wait'])
        self.assertEqual(sentinel.calls, ['wait'])

    def test_absent_handles_return_for_result_persistence(self):
        result = {'errors': []}
        controller.cleanup_owned_children(None, None, result)
        self.assertEqual(result, {'errors': []})


if __name__ == '__main__':
    unittest.main(verbosity=2)
