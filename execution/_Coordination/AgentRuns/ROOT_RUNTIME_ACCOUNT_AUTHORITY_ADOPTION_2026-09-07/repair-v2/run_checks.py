"""Run the narrow review-v1 repair checks and retain outputs."""
from pathlib import Path
import json
import os
import subprocess

root = Path(__file__).resolve().parents[5]
out = Path(__file__).resolve().parent
python = '/Users/ryan/.local/share/mise/installs/python/3.13/bin/python'
commands = [
    [python, '-m', 'unittest', 'tools.validation.test_root_runtime_successors', '-v'],
    [python, 'execution/_Coordination/AgentRuns/ROOT_RUNTIME_ACCOUNT_AUTHORITY_ADOPTION_2026-09-07/verify_composition.py'],
    [python, 'execution/_Coordination/AgentRuns/ROOT_RUNTIME_ACCOUNT_AUTHORITY_ADOPTION_2026-09-07/repair-v2/verify_injected_account.py'],
    [python, 'tools/validation/validate_root_materialization_fence.py'],
    [python, 'tools/validation/validate_root_harness_adapter.py'],
    [python, 'tools/validation/validate_root_surface_ownership.py'],
    [python, 'tools/validation/validate_root_work_graph_dispatch.py'],
    [python, 'tools/run_affected_tests.py', '--base', 'c3e9ab0f8e49314befc1fc81a9e01346641a7344'],
    [python, 'tools/validation/validate_candidate_whitespace.py', '--base-ref', 'origin/main'],
    ['git', 'diff', '--check'],
]
environment = dict(os.environ)
environment['PYTHONPATH'] = str(root / 'tools/validation')
records = []
for number, command in enumerate(commands):
    result = subprocess.run(command, cwd=root, capture_output=True, text=True,
                            env=environment)
    log = f'check-{number:02}.log'
    (out / log).write_text(result.stdout + result.stderr)
    records.append({'command': command, 'exit': result.returncode, 'log': log})
    if result.returncode:
        (out / 'CHECKS.json').write_text(json.dumps(records, indent=2) + '\n')
        raise SystemExit(result.returncode)
(out / 'CHECKS.json').write_text(json.dumps(records, indent=2) + '\n')
print('PASS:', len(records), 'narrow repair checks')
