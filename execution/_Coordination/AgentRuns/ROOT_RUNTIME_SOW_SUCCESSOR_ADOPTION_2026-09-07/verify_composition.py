"""Exact SOW successor composition and fail-closed checks in a disposable copy."""
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
fixture = Path(tempfile.mkdtemp(prefix='root-runtime-sow-adoption-')).resolve()
paths = set(subprocess.check_output(
    ['git', '-C', str(root), 'ls-files', 'execution', 'docs', 'tools', 'plans/steers',
     'projects/chirality-runtime', 'AGENTS.md', 'CLAUDE.md'], text=True).splitlines())
paths.update(subprocess.check_output(
    ['git', '-C', str(root), 'diff', '--cached', '--name-only'], text=True).splitlines())
for name in paths:
    source = root / name
    if source.is_file():
        target = fixture / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
for source in [
    root / 'docs/governance_harness/_DECISIONS/D-GOV-40_runtime_sow_successor_adoption.md',
    out / 'SUCCESSOR_ADOPTIONS.json',
]:
    target = fixture / source.relative_to(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
(fixture / '.git').write_text('gitdir: ' + subprocess.check_output(
    ['git', '-C', str(root), 'rev-parse', '--absolute-git-dir'], text=True).strip() + '\n')

sys.path.insert(0, str(fixture / 'tools/validation'))
import yaml
import root_governance_state as governance
import root_runtime_successors as successors

config = yaml.safe_load((fixture / 'execution/_harness/root_guards.yaml').read_text())
state = governance.load_governance_state(fixture, config, require_effective=True)
observed = state['runtime_successor_recognition']
assert observed['adoptions'] == [
    'D36_STAGE1', 'D36_STAGE2', 'D36_ACCOUNT_AUTHORITY',
    'D36_RUNTIME_SOW_PROPAGATION']
assert observed['state'] == 'accepted-pending-publication'
assert observed['published'] is False and observed['execution_authority'] is False
assert [len(state[key]) for key in
        ['source_ids', 'governance_ids', 'runtime_ids', 'held_capabilities']] == [53, 46, 7, 9]

policy_path = fixture / successors.POLICY
policy_bytes = policy_path.read_bytes()
policy = json.loads(policy_bytes)
prior = json.loads((root / ('execution/_Coordination/AgentRuns/'
                            'ROOT_RUNTIME_ACCOUNT_AUTHORITY_ADOPTION_2026-09-07/'
                            'SUCCESSOR_ADOPTIONS.json')).read_text())
assert policy['adoptions'][:3] == prior['adoptions']
entry = policy['adoptions'][3]
negative = []

def rejected(label, path, replacement):
    target = fixture / path
    before = target.read_bytes() if target.is_file() else None
    try:
        if replacement is None:
            target.unlink()
        elif replacement == b'__directory__':
            target.unlink()
            target.mkdir()
        elif replacement == b'__symlink__':
            target.unlink()
            target.symlink_to(target.parent / 'missing-target')
        else:
            target.write_bytes(replacement)
        try:
            governance.load_governance_state(fixture, config)
        except governance.GovernanceError as exc:
            negative.append({'case': label, 'result': 'REJECTED', 'error': str(exc)})
        else:
            raise AssertionError(label + ' passed')
    finally:
        if target.is_symlink():
            target.unlink()
        elif target.is_dir():
            target.rmdir()
        if before is not None:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(before)

for label, ref in [
    ('acceptance', entry['acceptance']), ('subject', entry['subject']),
    ('acceptance manifest', entry['sow_acceptance_manifest']),
    ('postimage index', entry['postimage_index']), ('bindings', entry['bindings']),
    ('manager manifest', entry['manager_manifest']), ('audit manifest', entry['audit_manifest']),
    ('application manifest', entry['application_manifest']), ('pointer', entry['pointer']),
    ('handoff manifest', entry['handoff_manifest']), ('Root input', entry['root_input']),
]:
    rejected('missing ' + label, ref['path'], None)
    rejected('altered ' + label, ref['path'], b'altered')

package = json.loads((fixture / entry['sow_acceptance_manifest']['path']).read_text())
member = Path(entry['sow_acceptance_manifest']['path']).parent / package['members'][1]['path']
rejected('altered acceptance member', str(member), b'altered member')
rejected('subject wrong type', entry['subject']['path'], b'__directory__')
rejected('subject symlink', entry['subject']['path'], b'__symlink__')
rejected('mixed Runtime SOW', entry['changes'][0]['path'], subprocess.check_output(
    ['git', '-C', str(root), 'show', 'HEAD:' + entry['changes'][0]['path']]))

for label, mutate in [
    ('wrong predecessor', lambda p: p['adoptions'][3]['changes'][0].update(before='a' * 64)),
    ('wrong postimage', lambda p: p['adoptions'][3]['changes'][0].update(after='a' * 64)),
    ('App path injection', lambda p: p['adoptions'][3]['changes'].append({
        'path': 'projects/chirality-app-dev/execution/PKG-02/ScopeOfWork.md',
        'before': None, 'after': 'a' * 64})),
    ('unknown path injection', lambda p: p['adoptions'][3]['changes'].append({
        'path': 'projects/chirality-runtime/execution/unknown.md',
        'before': None, 'after': 'a' * 64})),
    ('escaping path injection', lambda p: p['adoptions'][3]['changes'].append({
        'path': '../outside.md', 'before': None, 'after': 'a' * 64})),
    ('duplicate change', lambda p: p['adoptions'][3]['changes'].append(
        copy.deepcopy(p['adoptions'][3]['changes'][0]))),
]:
    altered = copy.deepcopy(policy)
    mutate(altered)
    policy_path.write_text(json.dumps(altered))
    old_sha = successors.POLICY_SHA
    successors.POLICY_SHA = hashlib.sha256(policy_path.read_bytes()).hexdigest()
    try:
        try:
            governance.load_governance_state(fixture, config)
        except governance.GovernanceError as exc:
            negative.append({'case': label, 'result': 'REJECTED', 'error': str(exc)})
        else:
            raise AssertionError(label + ' passed')
    finally:
        policy_path.write_bytes(policy_bytes)
        successors.POLICY_SHA = old_sha

guards = []
for name in ['root_materialization_fence', 'root_harness_adapter',
             'root_surface_ownership', 'root_work_graph_dispatch']:
    result = subprocess.run([sys.executable, str(fixture / 'tools/validation' /
                            ('validate_' + name + '.py'))], cwd=fixture,
                            capture_output=True, text=True)
    guards.append({'check': name, 'exit': result.returncode,
                   'stdout': result.stdout, 'stderr': result.stderr})
    assert result.returncode == 0

result = {'status': 'PASS', 'recognition': observed, 'priorObjectsPreserved': True,
          'counts': [53, 46, 7, 9], 'negative': negative, 'guards': guards,
          'stagedBasis': {'paths': 83,
                          'tree': '64f944b55cc69b34ecccaca585f4ca399354d8c5',
                          'binaryDiffSha256': '4e00e0147eb66b779ce6a7aecc079c61ad87e2afc854110e12685df2b7f61577'},
          'scope': 'disposable copy; no staged or Runtime/App bytes written'}
(out / 'COMPOSITION_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print('PASS: four adoptions,', len(negative), 'rejections, four guards, 53/46/7/9')
