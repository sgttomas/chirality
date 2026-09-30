"""Load preserved behavioral/argv suites and bind their guard reference to v3."""
from pathlib import Path
from reproduce_v2 import load

CURRENT_DIR = Path(__file__).resolve().parent
HERE = CURRENT_DIR.parent / 'continuation_01'  # legacy regression fixture origin
previous = load('guard_v2_test_harness_preserved', HERE/'harness.py')
FORBIDDEN, blocked = previous.FORBIDDEN, previous.blocked
original, original_guard = previous.original, previous.original_guard
v3 = load('host_guard_v3', CURRENT_DIR.parents[2]/'tools/host_guard_v3.py')
original.guard = v3
v2 = v3  # preserved v2 admission suite imports this name from harness
legacy_admission = load('preserved_v2_admission_tests_against_v3', HERE/'test_compile_admission.py')
assert legacy_admission.guard is v3 and original.guard is v3
