"""Execute all sealed behavioral tests against the additive v2 source only."""
import hashlib
import sys
import unittest
from harness import ORIGINAL_TESTS, V2, original

print('Original test SHA256:', hashlib.sha256(ORIGINAL_TESTS.read_bytes()).hexdigest(), flush=True)
print('Bound v2 source SHA256:', hashlib.sha256(V2.read_bytes()).hexdigest(), flush=True)
suite = unittest.defaultTestLoader.loadTestsFromModule(original)
assert suite.countTestCases() == 41
result = unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
