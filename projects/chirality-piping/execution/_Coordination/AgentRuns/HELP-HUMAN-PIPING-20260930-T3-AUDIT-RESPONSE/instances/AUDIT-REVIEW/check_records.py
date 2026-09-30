#!/usr/bin/env python3
"""Independent read-only packet checks; no audit or solver imports.

Run from repo root with python3 -B; prints compact JSON. Working inputs are
checked against the sealed snapshots before reliance. Hashing is streamed.
"""
import hashlib
import json
import pathlib
import re
import subprocess
from datetime import datetime

ROOT = pathlib.Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
T3 = pathlib.Path('projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3')
A = T3 / 'AUDIT'
BASE = '74b3c7313491f27f71c4361d5e1657ee4a39e2f1'
HEAD = '7fd632f60ee0d4eeb0429ff4dbd2193eaeeb5d6d'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def load(path):
    return json.loads((ROOT / path).read_text())


def digest(path):
    h = hashlib.sha256()
    with (ROOT / path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def manifest_entries(path):
    result = []
    for line in (ROOT / path).read_text().splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r'([a-f0-9]{64}) [ *](.+)', line)
        assert match, (str(path), line[:80])
        result.append(match.groups())
    return result


def main():
    changes = git('diff', '--name-status', BASE, HEAD).decode().splitlines()
    assert len(changes) == 15
    for change in changes:
        status, path = change.split('\t')
        assert status == 'A' and path.startswith(str(A) + '/')
        assert git('show', f'{HEAD}:{path}') == (ROOT/path).read_bytes(), path
    basis = load(A/'_run_records/basis.json')
    for inp in basis['inputs']:
        assert digest(inp['path']) == inp['sha256'], inp['path']
        assert hashlib.sha256(git('show', BASE+':'+inp['path'])).hexdigest() == inp['sha256']
    for sha, name in manifest_entries(A/'SHA256SUMS'):
        assert digest(A/name) == sha, name
    # Independently resolve each manifest from two documented candidate bases.
    manifests = sorted(p.relative_to(ROOT) for p in (ROOT/T3).rglob('SHA256SUMS')
                       if not p.is_relative_to(ROOT/A))
    entries, exceptions = 0, []
    for path in manifests:
        refs = manifest_entries(path)
        bases = [path.parent, path.parent.parent]
        valid = [base for base in bases if all((ROOT/base/name).is_file() for _, name in refs)]
        assert valid, str(path)
        base = valid[0]
        if base != path.parent:
            exceptions.append(str(path.relative_to(T3)))
        for sha, name in refs:
            assert digest(base/name) == sha, str(base/name)
        entries += len(refs)
    merges = load(A/'_run_records/merges.json')['results']
    merge_results = []
    for row in merges:
        parents = git('show', '-s', '--format=%P', row['recorded_merge']).decode().split()
        assert parents == row['parents'] and parents[1] == row['recorded_head']
        subprocess.run(['git','merge-base','--is-ancestor',row['recorded_target_base'],row['recorded_head']], cwd=ROOT, check=True)
        assert not git('diff','--name-only',row['recorded_head'],row['recorded_merge'],'--','projects/chirality-piping','tools','.github')
        merge_results.append({'slice':row['slice'], 'second_parent_matches':True,
                              'first_parent_equals_target':parents[0] == row['recorded_target_base']})
    by_slice = {r['slice']: r for r in merges}
    ci = load(A/'_run_records/ci.json')['results']
    numerical = []
    for row in ci:
        meta = row['metadata']
        assert meta['conclusion'] == 'success' and meta['status'] == 'completed'
        assert meta['headSha'] == by_slice[row['slice']]['recorded_head']
        for job in row['jobs']:
            if job['name'] == 'Numerical cargo suite':
                duration = (datetime.fromisoformat(job['completedAt'])-datetime.fromisoformat(job['startedAt'])).total_seconds()
                assert duration == job['duration_seconds'] and job['conclusion'] == 'success'
                numerical.append(duration)
    plans = load(A/'_run_records/dispatches.json')['results']
    for row in plans:
        p, m = row['plan'], by_slice[row['slice']]
        assert p['head'] == m['recorded_head']
        assert p['base'] == p['target_base'] == m['recorded_target_base']
        assert p['mode'] == 'full' and p['coverage_full'] and p['numerical_required']
        assert p['selected_specs'] == p['inventory']
    # Hash summaries preserve reviewable counts, not raw test-name evidence.
    missing_raw = []
    for row in load(A/'_run_records/dec025.json')['results']:
        for sweep in row['sweeps']:
            assert sweep['git']['commit_hash'] == by_slice[row['slice']]['recorded_head']
            assert load(sweep['file'])['git'] == sweep['git']
        folder = ROOT/T3/'IMPLEMENTATION'/(row['slice']+'_MERGE')/'dec025'
        assert not list((folder/'suites').glob('*.log'))
        missing_raw.append(row['slice'])
    print(json.dumps({'frozen_added_files':len(changes),'basis_inputs_verified':len(basis['inputs']),
                      'audit_manifest_entries':len(manifest_entries(A/'SHA256SUMS')),
                      'historical_manifests':len(manifests),'historical_entries':entries,
                      'parent_base_exceptions':exceptions,'merges':merge_results,
                      'stored_ci_runs_crosschecked':len(ci),'numerical_durations_seconds':numerical,
                      'stored_full_dispatch_plans':len(plans),'merge_folders_without_suite_logs':missing_raw,
                      'limits':['Stored GitHub metadata checked internally; live sampling recorded separately.',
                                'Hashes establish byte identity, not correctness or completeness of the original experiments.']},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
