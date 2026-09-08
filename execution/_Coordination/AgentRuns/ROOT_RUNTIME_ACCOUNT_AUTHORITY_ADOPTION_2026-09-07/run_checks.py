"""Run and retain the bounded Root adoption validation set."""
from pathlib import Path
import json
import os
import subprocess

root = Path(__file__).resolve().parents[4]
out = Path(__file__).resolve().parent
python = '/Users/ryan/.local/share/mise/installs/python/3.13.14/bin/python3'
commands = [
    [python, 'execution/_Coordination/AgentRuns/ROOT_RUNTIME_ACCOUNT_AUTHORITY_ADOPTION_2026-09-07/verify_composition.py'],
    [python, '-m', 'unittest', 'tools.validation.test_root_runtime_successors', '-v'],
    [python, 'tools/validation/validate_root_materialization_fence.py'],
    [python, 'tools/validation/validate_root_harness_adapter.py'],
    [python, 'tools/validation/validate_root_surface_ownership.py'],
    [python, 'tools/validation/validate_root_work_graph_dispatch.py'],
    [python, 'tools/validation/validate_instruction_tranche_manifest.py'],
    [python, 'tools/validation/validate_instruction_entrypoints.py'],
    [python, 'tools/practitioner_harness/harness.py', 'self-check'],
    [python, 'tools/run_affected_tests.py', '--base', 'd4b8a8cec2e4d3c636740cb97a27fe3b1a3ef327'],
    [python, 'tools/validation/validate_candidate_whitespace.py', '--base-ref', 'origin/main'],
    ['git', 'diff', '--check'],
]
records = []
for number, command in enumerate(commands):
    environment = dict(os.environ)
    environment['PYTHONPATH'] = str(root / 'tools/validation')
    result = subprocess.run(command, cwd=root, capture_output=True, text=True,
                            env=environment)
    log = f'check-{number:02}.log'
    (out / log).write_text(result.stdout + result.stderr)
    records.append({'command': command, 'exit': result.returncode, 'log': log})
    if result.returncode:
        (out / 'CHECKS.json').write_text(json.dumps(records, indent=2) + '\n')
        raise SystemExit(result.returncode)
(out / 'CHECKS.json').write_text(json.dumps(records, indent=2) + '\n')
print('PASS:', len(records), 'checks')
