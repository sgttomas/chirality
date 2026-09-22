#!/usr/bin/env python3
"""Read-only exact-key, changed-unit, negative-probe and live-reference backcheck."""
import collections, csv, hashlib, importlib.util, json, re, subprocess
from pathlib import Path
HOME = Path(__file__).resolve().parent
ROOT = Path(subprocess.check_output(['git', '-C', str(HOME), 'rev-parse', '--show-toplevel'], text=True).strip())
RUN = HOME.parent.parent
BASIS = json.loads((HOME / "EXECUTION.json").read_text())["basis"]

def rows(path):
    with path.open() as f:
        return list(csv.DictReader(f))

def exact(expected, actual):
    if collections.Counter(expected) != collections.Counter(actual) or len(actual) != len(set(actual)):
        raise ValueError('exact-key coverage mismatch')

def sections(data):
    text = data.decode(); matches = list(re.finditer(r'^#{2,3} .+$', text, re.M))
    result = {'PREAMBLE': text[:matches[0].start()] if matches else text}
    for i, match in enumerate(matches):
        key = match[0]; occurrence = 1
        while key in result:
            occurrence += 1; key = match[0] + ' [occurrence ' + str(occurrence) + ']'
        result[key] = text[match.start():matches[i + 1].start() if i + 1 < len(matches) else len(text)]
    return result

def hashes(units):
    for row in units:
        data = (ROOT / row['SourcePath']).read_bytes()
        if row['CurrentSHA256'] == 'REMOVED':
            if row['Unit'] in sections(data):
                raise ValueError('removed unit still exists')
            continue
        if row['Unit'] != 'FILE':
            data = sections(data)[row['Unit']].encode()
        if hashlib.sha256(data).hexdigest() != row['CurrentSHA256']:
            raise ValueError('source hash mismatch: ' + row['SourcePath'])

expected = [r['ClaimKey'] for r in rows(RUN / 'R5/ROW_ACCOUNTING.csv')]
actual = [r['ClaimKey'] for r in rows(HOME / 'CURRENT_ROWS.csv')]
exact(expected, actual)
units = rows(HOME / 'CURRENT_CHANGED_UNITS.csv'); hashes(units)
# Derive the changed production/navigation population independently from Git's
# supplied immutable basis. New continuation/audit artifacts have their own
# manifests; this population covers modified files that existed at that basis.
changed_paths = subprocess.check_output(['git', '-C', str(ROOT), 'diff', '--diff-filter=M', '--name-only', BASIS, '--', 'projects/chirality-app-dev'], text=True).splitlines()
expected_units = []
for relative in changed_paths:
    path = ROOT / relative
    if '/WORK_GRAPH.json' in relative or HOME in path.parents:
        continue  # Parent-owned graph; continuation evidence is not source input.
    before = subprocess.check_output(['git', '-C', str(ROOT), 'show', BASIS + ':' + relative])
    after = path.read_bytes()
    if path.name == 'ScopeOfWork.md':
        old_sections, new_sections = sections(before), sections(after)
        for identity in set(old_sections) | set(new_sections):
            if old_sections.get(identity) != new_sections.get(identity):
                expected_units.append((relative, identity))
    elif before != after:
        expected_units.append((relative, 'FILE'))
unit_ids = [(r['SourcePath'], r['Unit']) for r in units]
exact(expected_units, unit_ids)

probes = {}
try:
    exact(expected_units, unit_ids[:-1])
except ValueError:
    probes['missing_changed_unit_against_git'] = 'REJECTED'
else:
    raise AssertionError('missing changed-unit probe accepted')
for label, candidate in [('missing', actual[:-1]), ('duplicate', actual + [actual[0]])]:
    try:
        exact(expected, candidate)
    except ValueError:
        probes[label] = 'REJECTED'
    else:
        raise AssertionError('negative key probe accepted')
bad = [dict(r) for r in units]; bad[0]['CurrentSHA256'] = '0' * 64
try:
    hashes(bad)
except ValueError:
    probes['mismatched_source_hash'] = 'REJECTED'
else:
    raise AssertionError('negative hash probe accepted')
path = ROOT / 'projects/chirality-app-dev/execution/_Reconciliation/References/reconcile_authority_corpus.py'
spec = importlib.util.spec_from_file_location('d38_readonly', path)
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
all_files = list(module._iter_reference_files())
excluded = [p for p in all_files if '/DEL-09-07_' in p]
live = [p for p in all_files if p not in excluded]
module._iter_reference_files = lambda: iter(live)
assert module.cmd_audit(None) == 0
print(json.dumps({'exact_keys': len(actual), 'changed_units': len(units), 'negative_probes': probes,
                  'live_reference_files': len(live), 'retired_reference_files_excluded': len(excluded),
                  'reference_scope': 'All applicable live references only; unfiltered canonical audit remains nonzero for immutable retired history. No waiver or full canonical PASS.'}, indent=2))

# Preserve the discovery ledger rather than silently rewriting its history.
original = {r['ClaimKey']: r for r in rows(RUN / 'R5/ROW_ACCOUNTING.csv')}
wave_keys = []
for name in ['W00_03_ROWS.csv', 'W02_03_ROWS.csv', 'W04_06_ROWS.csv', 'W07_10_ROWS.csv', 'W10_ROWS.csv', 'WEXT_ROWS.csv']:
    for row in rows(HOME / name):
        wave_keys.append(row['ClaimKey'])
        assert all(row.get(k) == v for k, v in original[row['ClaimKey']].items()), (name, row['ClaimKey'], 'altered original field')
expected_residuals = [r['ClaimKey'] for p in (RUN / 'R5/RESIDUALS').glob('*.csv') for r in rows(p)]
expected_residuals += [r['ClaimKey'] for r in rows(RUN / 'R5/EXTENSION_RESIDUALS.csv')]
exact(expected_residuals, wave_keys)

def head(path):
    return subprocess.check_output(['git', '-C', str(ROOT), 'show', BASIS + ':' + str(path.relative_to(ROOT))])

execution = ROOT / 'projects/chirality-app-dev/execution'
control_count = 0
for path in execution.glob('PKG-*/1_Working/DEL-*/_STATUS.md'):
    before = head(path).decode(); after = path.read_text()
    for field in ['Current State', 'Checking Approval SHA', 'Authorization Basis', 'Directive']:
        pattern = r'^\*\*' + field + r':?\*\*:?[^\n]*$'
        assert re.findall(pattern, before, re.M) == re.findall(pattern, after, re.M), (path, field)
    old_history = before.split('## History', 1)[-1]; new_history = after.split('## History', 1)[-1]
    cursor = 0
    for line in old_history.splitlines():
        if not line.strip():
            continue
        position = new_history.find(line, cursor)
        assert position >= 0, (path, 'historical line changed', line)
        cursor = position + len(line)
    control_count += 1
retired = next(execution.glob('PKG-09*/1_Working/DEL-09-07_*'))
tracked = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '--', str(retired.relative_to(ROOT))], text=True).splitlines()
assert len(tracked) == 25
assert all((ROOT / p).read_bytes() == head(ROOT / p) for p in tracked)
frozen_paths = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '--', str(RUN.relative_to(ROOT))], text=True).splitlines()
for relative in frozen_paths:
    path = ROOT / relative
    if path == RUN / 'HANDOFF_STATE.md' or HOME in path.parents:
        continue
    assert path.read_bytes() == head(path), (relative, 'frozen original changed')
print(json.dumps({'original_residual_keys_and_fields': len(wave_keys), 'control_and_history_deliverables': control_count,
                  'retired_files_byte_identical': len(tracked), 'original_run_frozen': True}))

# Current Remaining is the executable handoff. Derive its complete physical
# population independently so a stale census or omitted plain-text bullet fails.
remaining_actual = []
for path in sorted(execution.glob('PKG-*/1_Working/DEL-*/_STATUS.md')):
    did = path.parent.name[:9]
    section = path.read_text().split('## Remaining\n', 1)[1].split('## History', 1)[0]
    matches = list(re.finditer(r'^- ', section, re.M))
    items = []
    if matches:
        for index, match in enumerate(matches, 1):
            body = section[match.start():matches[index].start() if index < len(matches) else len(section)].strip()
            label = re.match(r'^- \*\*([^*]+)\*\*', body)
            items.append((label.group(1) if label else f'ITEM-{index:02d}', body))
    else:
        items.append(('NO_CURRENT_TASK', section.strip()))
    assert all(body for _, body in items), did
    file_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    remaining_actual.extend((did, label, body, str(path.relative_to(ROOT)), file_hash) for label, body in items)
remaining_census = rows(HOME / 'REMAINING_WORK_CENSUS.csv')
remaining_recorded = [(r['DeliverableID'], r['Item'], r['Remaining'], r['SourcePath'], r['SourceSHA256'])
                      for r in remaining_census]
exact(remaining_actual, remaining_recorded)
assert len({r[0] for r in remaining_actual}) == 54
try:
    exact(remaining_actual, remaining_recorded[:-1])
except ValueError:
    remaining_probe = 'REJECTED'
else:
    raise AssertionError('missing Remaining item probe accepted')
print(json.dumps({'remaining_items': len(remaining_actual), 'remaining_deliverables': 54,
                  'no_current_task_markers': sum(r[1] == 'NO_CURRENT_TASK' for r in remaining_actual),
                  'missing_remaining_probe': remaining_probe}))
