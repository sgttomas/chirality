import sys
import unittest
from unittest.mock import patch
from harness import original, legacy_admission

suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromModule(original),
                           unittest.defaultTestLoader.loadTestsFromModule(legacy_admission)])
assert suite.countTestCases() == 111
with patch('time.monotonic', return_value=100.0), patch('time.time_ns', return_value=100000000000):
    result = unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
