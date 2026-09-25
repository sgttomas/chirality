"""Independent bounded backcheck: files, unified patch, Fraction algebra; no product execution."""
from pathlib import Path
from fractions import Fraction as Q
import datetime, difflib, hashlib, json, math, re, struct

OUT = Path(__file__).resolve().parent
PM = OUT.parent
ROOT = next(p for p in OUT.parents if (p / 'projects/chirality-piping').is_dir())
PUB = PM / 'MEMBRANE_PUBLICATION'
FREEZE = PM / 'FREEZE_03'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
digest = lambda b: hashlib.sha256(b).hexdigest()
rel = lambda p: str(p.relative_to(ROOT))
binding = json.loads((PUB / 'REPAIR_BINDING.json').read_text())
manifest = json.loads((FREEZE / 'SOURCE_MANIFEST.json').read_text())
patch = PUB / 'PHYS_R4.delta.patch'
assert sha(patch) == binding['patch_sha256']
assert manifest['candidate_content_sha256'] in binding['basis']

# Apply every unified hunk in memory to the F03 snapshots. No Git or filesystem mutation.
lines = patch.read_text().splitlines(keepends=True)
sections = []
i = 0
while i < len(lines):
    assert lines[i].startswith('--- '), lines[i]
    old = lines[i][4:].strip()
    new = lines[i + 1][4:].strip()
    assert new.startswith('b/')
    path = new[2:]
    assert path in binding['files']
    data = [] if old == '/dev/null' else (FREEZE / 'source' / path).read_text().splitlines(keepends=True)
    before = None if old == '/dev/null' else digest(''.join(data).encode())
    assert before == binding['files'][path]['before_sha256']
    i += 2
    result, cursor, hunks = [], 0, 0
    while i < len(lines) and not lines[i].startswith('--- '):
        m = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', lines[i])
        assert m, lines[i]
        oldstart, oldcount = int(m[1]), int(m[2] or 1)
        newstart, newcount = int(m[3]), int(m[4] or 1)
        start = oldstart - 1 if oldcount else oldstart
        assert start >= cursor
        result.extend(data[cursor:start])
        assert len(result) == (newstart - 1 if newcount else newstart)
        left, right = [], []
        i += 1
        while i < len(lines) and not lines[i].startswith(('@@ ', '--- ')):
            marker, content = lines[i][0], lines[i][1:]
            assert marker in ' +-'
            if marker in ' -': left.append(content)
            if marker in ' +': right.append(content)
            i += 1
        assert len(left) == oldcount and len(right) == newcount
        assert data[start:start + oldcount] == left
        result.extend(right)
        cursor = start + oldcount
        hunks += 1
    result.extend(data[cursor:])
    after = ''.join(result).encode()
    assert after == (ROOT / path).read_bytes()
    assert digest(after) == binding['files'][path]['after_sha256']
    sections.append({'path': path, 'before_sha256': before, 'after_sha256': digest(after), 'hunks': hunks})
assert {x['path'] for x in sections} == set(binding['files'])

f03_checks = []
for item in manifest['paths']:
    p = item['path']
    assert sha(FREEZE / 'source' / p) == item['sha256']
    expected = binding['files'][p]['after_sha256'] if p in binding['files'] else item['sha256']
    assert sha(ROOT / p) == expected, p
    f03_checks.append({'path': p, 'current_sha256': expected, 'unchanged_from_F03': p not in binding['files']})

reference_binding_path = PUB / binding['reference']
reference_binding = json.loads(reference_binding_path.read_text())
reference_path = ROOT / reference_binding['reference_path']
assert sha(reference_path) == reference_binding['reference_sha256']
test_path = ROOT / reference_binding['test_path']
assert sha(test_path) == reference_binding['test_sha256']
test = test_path.read_text()
assert 'let tolerance = 1e-9' in test
assert '"L_m":1.0' in test and '"L_m":1e-77' not in test
assert 'let expected_membrane = 3.1333333333333337e-171;' in test
assert 'wall.to_bits(),\n        1,' in test

execution_records = []
for label, expected_exit, source_sha in [
    ('red-02', 101, binding['files'][sections[0]['path']]['before_sha256']),
    ('green-01', 0, binding['files'][sections[0]['path']]['after_sha256']),
]:
    p = PUB / (label + '-execution.json')
    record = json.loads(p.read_text())
    log = PUB / (label + '.log')
    assert sha(log) == record['log_sha256']
    assert record['exit_code'] == expected_exit and record['all_inputs_unchanged'] is True
    assert record['inputs'][sections[0]['path']] == source_sha
    assert record['inputs'][rel(test_path)] == sha(test_path)
    assert record['inputs'][rel(FREEZE / 'SOURCE_MANIFEST.json')] == sha(FREEZE / 'SOURCE_MANIFEST.json')
    assert record['actor'] == '/root/physics_resume'
    assert 'pressure_membrane_range' in record['command']
    text = log.read_text()
    for mode in ['SparseInteractive', 'DenseScrutiny']:
        assert f'mode={mode} wall=4.94065645841246544e-324' in text
    assert 'PIPE_ELEMENT_INPUT_INVALID' not in text
    execution_records.append({'path': rel(p), 'sha256': sha(p), 'log_sha256': sha(log),
                              'exit_code': record['exit_code'], 'attribution': record['actor']})
assert 'PIPE_ELEMENT_INPUT_INVALID' in (PUB / 'red-01.log').read_text()
assert '"L_m":1e-77' in (PUB / 'red-01-test.rs').read_text()

# Exact represented input rationals. For fully restrained axial displacement and no
# thermal/primitive load, Nm=0, Nw=2nu*p*Ai. Pi cancels from the membrane quotient.
q = Q.from_float
od, wall, p, nu = map(q, [4e-77, 1e-77, 4.7e-170, .1])
ri = od / 2 - wall
area_without_pi = wall * (od - wall)
membrane_exact = 2 * nu * p * ri**2 / area_without_pi
membrane = float(membrane_exact)
pi64 = q(math.pi)
wall_exact = 2 * nu * p * pi64 * ri**2
published_wall = float(wall_exact)
published_area = float(pi64 * area_without_pi)
redivided = published_wall / published_area
prior = json.loads(reference_path.read_text())['membrane_publication_arithmetic']
assert membrane == prior['stable_membrane_Pa']
assert published_wall == prior['wall_published_N']
assert redivided == prior['redivided_membrane_Pa']
assert struct.pack('>d', published_wall).hex() == '0000000000000001'
assert abs(redivided / membrane - 1) > .67
green = float('3.13333333333333325e-171')
assert abs(green - membrane) <= 1e-9 * abs(membrane)

# Independent exact polynomial consequence check. Constant pressure adds c to N;
# force/moment equilibrium leaves N'=-wx and all nonaxial statics unchanged.
# Cover tensile/compressive/zero mechanical forces and axial load slopes.
cases = 0
for n0 in [Q(-7), Q(0), Q(11)]:
    for w in [Q(-5, 3), Q(0), Q(9, 4)]:
        for x in [Q(0), Q(1, 4), Q(1, 2), Q(1)]:
            a, h, c = Q(7, 5), Q(3, 2), Q(19, 13)
            row = (n0 - w * h * x + c) / a
            q0, q1, q2 = (n0 + c) / a, (n0 + c) / a - w * h / (2 * a), (n0 + c) / a - w * h / a
            control = q0 * (1-x)**2 + 2*q1*x*(1-x) + q2*x*x
            assert row == control
            assert (n0-w*h*x)/a == (n0/a)*(1-x)**2 + 2*(n0/a-w*h/(2*a))*x*(1-x) + (n0/a-w*h/a)*x*x
            cases += 1

inputs = [ROOT / 'AGENTS.md', ROOT / 'projects/chirality-piping/AGENTS.md',
          ROOT / 'projects/chirality-piping/loop/LOOP_INIT.md', ROOT / '.agents/skills/software-code-review/SKILL.md',
          OUT / 'BRIEF.md', FREEZE / 'SOURCE_MANIFEST.json',
          PM / 'INDEPENDENT_REVIEW/FREEZE_03_BACKCHECK/RETURN.md',
          PM / 'INDEPENDENT_REVIEW/FREEZE_03_BACKCHECK/independent_arithmetic_probe.py',
          reference_path, PUB / 'REPAIR_BINDING.json', PUB / 'REFERENCE_BINDING.json',
          reference_binding_path, patch, test_path, PUB / 'red-01-test.rs', PUB / 'red-01.log',
          PUB / 'RED_01_EXECUTION.json', PUB / 'run_check.py', PUB / 'RETURN.md',
          PUB / 'red-02-execution.json', PUB / 'green-01-execution.json',
          PUB / 'red-02.log', PUB / 'green-01.log']
record = {
    'actor': '/root/physics_resume/membrane_backcheck', 'actual_parent': '/root/physics_resume',
    'method': 'Independent Python hashes, in-memory unified-patch reconstruction and exact Fraction algebra. No Git, Cargo, Rust/public product execution, native/browser or delegation.',
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'basis': manifest['candidate_content_sha256'], 'patch_sha256': sha(patch),
    'changed_paths': sections, 'F03_snapshot_and_current_checks': f03_checks,
    'manager_execution_records_verified': execution_records,
    'reference_binding': {'path': rel(reference_binding_path), 'sha256': sha(reference_binding_path),
                          'stale_predecessor_preserved': True, 'successor_matches_executed_test': True},
    'independent_arithmetic': {'OD_m': float(od), 'wall_m': float(wall), 'p_Pa': float(p), 'nu': float(nu),
                             'stable_membrane_Pa': membrane, 'wall_published_N': published_wall,
                             'redivided_membrane_Pa': redivided, 'old_relative_error': redivided / membrane - 1,
                             'green_relative_error': (green - membrane) / membrane,
                             'constant_pressure_polynomial_identities': cases,
                             'length_independence': 'Fully fixed Nm=0; membrane ratio has no length term.',
                             'scope': 'Reference arithmetic and source consequence only; manager logs establish observed public reachability.'},
    'inspected_input_hashes': {rel(p): sha(p) for p in inputs},
    'limits': ['No independent runtime run.', 'No general solver or subnormal force forward-error qualification.',
               'Affected public regression reruns, full suite, consumer/native joins and merge gates remain manager/ROOT obligations.'],
}
(OUT / 'verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'all_checks_pass': True, 'patch_sections': len(sections), 'F03_paths_verified': len(f03_checks),
                  'reference': membrane, 'old_relative_error': redivided / membrane - 1,
                  'green_relative_error': (green - membrane) / membrane, 'polynomial_cases': cases}, indent=2))
