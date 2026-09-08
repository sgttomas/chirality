"""Verify exact current composition and fail-closed cases in a disposable copy."""
from pathlib import Path
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[4]
out = Path(__file__).resolve().parent
fixture = Path(tempfile.mkdtemp(prefix='root-runtime-account-adoption-')).resolve()
tracked = subprocess.check_output(
    ['git', '-C', str(root), 'ls-files', 'execution', 'docs', 'tools', 'plans/steers',
     'projects/chirality-runtime', 'AGENTS.md', 'CLAUDE.md'], text=True).splitlines()
for name in tracked:
    source = root / name
    if source.is_file():
        target = fixture / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
for source in [
    root / 'docs/governance_harness/_DECISIONS/D-GOV-39_runtime_account_authority_successor_adoption.md',
    out / 'SUCCESSOR_ADOPTIONS.json',
]:
    target = fixture / source.relative_to(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
(fixture / '.git').write_text(
    'gitdir: ' + subprocess.check_output(
        ['git', '-C', str(root), 'rev-parse', '--absolute-git-dir'], text=True).strip() + '\n')

sys.path.insert(0, str(fixture / 'tools/validation'))
import yaml
import root_governance_state as governance
import root_runtime_successors as successors

config = yaml.safe_load((fixture / 'execution/_harness/root_guards.yaml').read_text())
state = governance.load_governance_state(fixture, config, require_effective=True)
recognition = state['runtime_successor_recognition']
assert recognition['adoptions'] == ['D36_STAGE1', 'D36_STAGE2', 'D36_ACCOUNT_AUTHORITY']
assert recognition['state'] == 'accepted-pending-publication'
assert recognition['published'] is False and recognition['execution_authority'] is False
assert [len(state[key]) for key in
        ['source_ids', 'governance_ids', 'runtime_ids', 'held_capabilities']] == [53, 46, 7, 9]

policy = json.loads((out / 'SUCCESSOR_ADOPTIONS.json').read_text())
prior = json.loads((root / ('execution/_Coordination/AgentRuns/'
                            'ROOT_RUNTIME_STAGE2_ADOPTION_2026-09-07/'
                            'SUCCESSOR_ADOPTIONS.json')).read_text())
assert policy['adoptions'][:2] == prior['adoptions']
entry = policy['adoptions'][2]
negative = []
cases = [
    ('missing acceptance', entry['acceptance']['path'], None),
    ('tampered acceptance', entry['acceptance']['path'], b'not accepted'),
    ('missing subject', entry['subject']['path'], None),
    ('tampered subject', entry['subject']['path'], b'{}'),
    ('missing acceptance manifest', entry['acceptance_manifest']['path'], None),
    ('tampered acceptance manifest', entry['acceptance_manifest']['path'], b'{}'),
    ('missing SCA-002 snapshot', entry['snapshot_manifests'][0]['path'], None),
    ('tampered SCA-003 snapshot', entry['snapshot_manifests'][1]['path'], b'{}'),
    ('mixed canonical ledger', entry['changes'][2]['path'],
     subprocess.check_output(['git', '-C', str(root), 'show',
                              'c3e9ab0f8e49314befc1fc81a9e01346641a7344^:' +
                              entry['changes'][2]['path']])),
]
subject = json.loads((fixture / entry['subject']['path']).read_text())
subject_base = Path(entry['subject']['path']).parent.parent
subject_member = subject['members'][0]['path']
subject_member_path = (Path(subject_member) if subject_member.startswith('projects/')
                       else subject_base / subject_member)
cases.append(('tampered subject member', str(subject_member_path), b'tampered'))
snapshot = json.loads((fixture / entry['snapshot_manifests'][0]['path']).read_text())
snapshot_member = Path(entry['snapshot_manifests'][0]['path']).parent / snapshot['members'][0]['path']
cases.append(('missing snapshot member', str(snapshot_member), None))

for label, name, replacement in cases:
    path = fixture / name
    before = path.read_bytes()
    try:
        path.unlink() if replacement is None else path.write_bytes(replacement)
        try:
            governance.load_governance_state(fixture, config)
        except governance.GovernanceError as exc:
            negative.append({'case': label, 'result': 'REJECTED', 'error': str(exc)})
        else:
            raise AssertionError('invalid composition passed: ' + label)
    finally:
        path.write_bytes(before)

unknown = copy.deepcopy(policy)
unknown['adoptions'][2]['changes'].append({
    'path': 'projects/chirality-runtime/execution/_Decomposition/UNKNOWN.md',
    'before': None,
    'after': 'a' * 64,
})
policy_path = fixture / successors.POLICY
before_policy = policy_path.read_bytes()
policy_path.write_text(json.dumps(unknown))
old_sha = successors.POLICY_SHA
successors.POLICY_SHA = hashlib.sha256(policy_path.read_bytes()).hexdigest()
try:
    try:
        governance.load_governance_state(fixture, config)
    except governance.GovernanceError as exc:
        negative.append({'case': 'unknown path', 'result': 'REJECTED', 'error': str(exc)})
    else:
        raise AssertionError('unknown path passed')
finally:
    policy_path.write_bytes(before_policy)
    successors.POLICY_SHA = old_sha

guards = []
for name in ['root_materialization_fence', 'root_harness_adapter',
             'root_surface_ownership', 'root_work_graph_dispatch']:
    result = subprocess.run(
        [sys.executable, str(fixture / 'tools/validation' / ('validate_' + name + '.py'))],
        cwd=fixture, capture_output=True, text=True)
    guards.append({'check': name, 'exit': result.returncode,
                   'stdout': result.stdout, 'stderr': result.stderr})
    assert result.returncode == 0

result = {
    'status': 'PASS',
    'initial_head': 'c3e9ab0f8e49314befc1fc81a9e01346641a7344',
    'pr_base': 'd4b8a8cec2e4d3c636740cb97a27fe3b1a3ef327',
    'preserved_prior_adoptions': True,
    'recognition': recognition,
    'counts': [53, 46, 7, 9],
    'guards': guards,
    'negative': negative,
    'scope': 'disposable fixture; no Runtime live bytes written',
}
(out / 'COMPOSITION_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print('PASS: exact three-adoption composition; four guards; 12 fail-closed cases; 53/46/7/9')
