"""Print pure regression decisions without activating providers or processes."""
import json
from test_compile_admission import CASES, attempt, make_job

results = []
for case in CASES:
    result = {**case, **attempt(make_job(case['argv']))}
    assert result['accepted'] == result['expected_accept'], result
    results.append(result)
print(json.dumps({'fake_files_only': True, 'live_capabilities': 'blocked during import and cases',
                  'cases': results}, indent=2))
