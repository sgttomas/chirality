"""Run and retain the exact Root SOW-adoption validation set."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

root = Path(__file__).resolve().parents[4]
out = Path(__file__).resolve().parent
python = '/Users/ryan/.local/share/mise/installs/python/3.13/bin/python'
expected_tree = '64f944b55cc69b34ecccaca585f4ca399354d8c5'
expected_diff = '4e00e0147eb66b779ce6a7aecc079c61ad87e2afc854110e12685df2b7f61577'

def staged_identity():
    names = subprocess.check_output(['git', '-C', str(root), 'diff', '--cached',
                                     '--name-only']).splitlines()
    tree = subprocess.check_output(['git', '-C', str(root), 'write-tree'], text=True).strip()
    diff = subprocess.check_output(['git', '-C', str(root), 'diff', '--cached', '--binary'])
    return len(names), tree, hashlib.sha256(diff).hexdigest()

assert staged_identity() == (83, expected_tree, expected_diff)
commands = [
    [python, '-m', 'unittest', 'tools.validation.test_root_runtime_successors', '-v'],
    [python, 'execution/_Coordination/AgentRuns/ROOT_RUNTIME_SOW_SUCCESSOR_ADOPTION_2026-09-07/verify_composition.py'],
    [python, 'tools/validation/validate_root_materialization_fence.py'],
    [python, 'tools/validation/validate_root_harness_adapter.py'],
    [python, 'tools/validation/validate_root_surface_ownership.py'],
    [python, 'tools/validation/validate_root_work_graph_dispatch.py'],
    [python, 'tools/validation/validate_instruction_tranche_manifest.py'],
    [python, 'tools/practitioner_harness/harness.py', 'self-check'],
    [python, 'tools/run_affected_tests.py', '--base', 'c5192790f98ec024e7c2728cb1d4df3ae2b2a2dd'],
    [python, 'tools/validation/validate_candidate_whitespace.py', '--base-ref', 'HEAD'],
    ['git', 'diff', '--check', 'HEAD'],
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
assert staged_identity() == (83, expected_tree, expected_diff)
(out / 'CHECKS.json').write_text(json.dumps(records, indent=2) + '\n')
(out / 'STAGED_PRESERVATION.json').write_text(json.dumps({
    'status': 'PASS', 'paths': 83, 'indexTree': expected_tree,
    'stagedBinaryDiffSha256': expected_diff,
    'rootOutputsStaged': False,
}, indent=2) + '\n')
print('PASS:', len(records), 'checks; staged 83 preserved')
