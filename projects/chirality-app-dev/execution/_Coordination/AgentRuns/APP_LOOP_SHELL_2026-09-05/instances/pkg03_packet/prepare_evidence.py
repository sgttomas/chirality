#!/usr/bin/env python3
"""Recompute bounded retirement candidate evidence; never edit source tree."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import difflib

parser = argparse.ArgumentParser()
parser.add_argument('--repo-root', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
repo, out = args.repo_root.resolve(), args.output.resolve()
out.mkdir(parents=True, exist_ok=False)
commands = []

def run(argv, cwd=repo):
    r = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    n = len(commands)
    (out / f'command-{n:02d}.stdout').write_text(r.stdout)
    (out / f'command-{n:02d}.stderr').write_text(r.stderr)
    commands.append({'argv': argv, 'cwd': str(cwd), 'exit_status': r.returncode,
                     'stdout': f'command-{n:02d}.stdout', 'stderr': f'command-{n:02d}.stderr'})
    return r

def sha(data):
    return hashlib.sha256(data).hexdigest()

head = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
tracked = run(['git', 'ls-files', '-z']).stdout.split('\0')
tracked = sorted(p for p in tracked if p)
matches = run(['git', 'grep', '-l', '-E', '@chirality/harness-contract|packages/harness-contract']).stdout.splitlines()
inventory = []
for p in sorted(matches):
    b = (repo / p).read_bytes()
    if '/frontend/' in p:
        category = ('facade-definition' if '/packages/harness-contract/' in p else
                    'rollback-test-consumer' if '/src/__tests__/' in p else
                    'workspace-registration' if p.endswith('package-lock.json') else
                    'validator-policy' if p.endswith('assert-harness-contract-deps.mjs') else
                    'documentary-source-comment')
    elif p.startswith('runtime/'):
        category = 'documentary-generated-catalog-label'
    else:
        category = 'governance-history-evidence-or-metadata'
    inventory.append({'path': p, 'sha256': sha(b), 'bytes': len(b), 'category': category})
(out / 'consumer-inventory.json').write_text(json.dumps(inventory, indent=2) + '\n')

front = 'projects/chirality-app-dev/frontend/'
source_candidates = [p for p in tracked if (p.startswith(('runtime/', 'tools/')) or
                    ('/frontend/' in p) or ('/src/' in p and p.startswith('projects/')))
                    and '/execution/' not in p and '/plans/' not in p
                    and Path(p).suffix in {'.ts', '.tsx', '.js', '.mjs', '.cjs', '.py', '.json'}]
source_hits = []
for p in source_candidates:
    s = (repo / p).read_text(errors='replace')
    for i, line in enumerate(s.splitlines(), 1):
        if '@chirality/harness-contract' in line or 'packages/harness-contract' in line:
            source_hits.append({'path': p, 'line': i, 'text': line})
(out / 'active-source-hits.json').write_text(json.dumps(source_hits, indent=2) + '\n')
(out / 'source-search-scope.json').write_text(json.dumps(source_candidates, indent=2) + '\n')

deletions = [p for p in tracked if p.startswith(front + 'packages/harness-contract/')]
edits = [front + 'package.json', front + 'package-lock.json']
images = {}
for p in deletions + edits:
    before = (repo / p).read_bytes()
    if p in deletions:
        after = None
    else:
        data = json.loads(before)
        if p.endswith('/package.json'):
            assert data['workspaces'] == ['packages/*']
            del data['workspaces']
        else:
            assert data['packages']['']['workspaces'] == ['packages/*']
            del data['packages']['']['workspaces']
            del data['packages']['node_modules/@chirality/harness-contract']
            del data['packages']['packages/harness-contract']
        after = (json.dumps(data, indent=2, ensure_ascii=False) + '\n').encode()
    images[p] = (before, after)
    pre = out / 'preimage' / p
    pre.parent.mkdir(parents=True, exist_ok=True)
    pre.write_bytes(before)
    if after is not None:
        post = out / 'postimage' / p
        post.parent.mkdir(parents=True, exist_ok=True)
        post.write_bytes(after)

def patch(reverse=False):
    result = []
    for p, (before, after) in sorted(images.items()):
        if reverse:
            before, after = after, before
        result.extend(difflib.unified_diff(
            before.decode().splitlines(keepends=True) if before is not None else [],
            after.decode().splitlines(keepends=True) if after is not None else [],
            fromfile='a/' + p if before is not None else '/dev/null',
            tofile='b/' + p if after is not None else '/dev/null'))
    return ''.join(result)
(out / 'candidate.patch').write_text(patch())
(out / 'rollback.patch').write_text(patch(True))
(out / 'change-manifest.json').write_text(json.dumps([
    {'path': p, 'operation': 'delete' if a is None else 'edit',
     'before_sha256': sha(b), 'after_sha256': None if a is None else sha(a)}
    for p, (b, a) in sorted(images.items())], indent=2) + '\n')

run(['node', '--version'])
run(['npm', '--version'])
scratch = Path(tempfile.mkdtemp(prefix='app-facade-packet-'))
try:
    for p in tracked:
        if p.startswith((front + 'src/', front + 'scripts/', front + 'packages/')) or p in edits + [front + 'tsconfig.json', front + 'next.config.mjs']:
            dest = scratch / p
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(repo / p, dest)
    baseline = run(['node', './scripts/assert-harness-contract-deps.mjs'], scratch / front)
    apply = run(['git', 'apply', '--check', str(out / 'candidate.patch')], scratch)
    assert apply.returncode == 0
    assert run(['git', 'apply', str(out / 'candidate.patch')], scratch).returncode == 0
    postimage_exact = all((not (scratch / p).exists()) if a is None else (scratch / p).read_bytes() == a for p, (_, a) in images.items())
    candidate = run(['node', './scripts/assert-harness-contract-deps.mjs'], scratch / front)
    assert run(['git', 'apply', '--check', str(out / 'rollback.patch')], scratch).returncode == 0
    assert run(['git', 'apply', str(out / 'rollback.patch')], scratch).returncode == 0
    rollback_exact = all((scratch / p).read_bytes() == b for p, (b, _) in images.items())
    restored = run(['node', './scripts/assert-harness-contract-deps.mjs'], scratch / front)
finally:
    shutil.rmtree(scratch)

result = {'basis_commit': head, 'tracked_matching_files': len(inventory),
          'scope': 'Tracked live checkout; named source roots separately inspected; external installations not observable',
          'candidate_deleted_files': len(deletions), 'candidate_edited_files': len(edits),
          'baseline_contract_deps_exit': baseline.returncode,
          'candidate_contract_deps_exit': candidate.returncode,
          'restored_contract_deps_exit': restored.returncode,
          'candidate_postimage_exact': postimage_exact, 'rollback_preimage_exact': rollback_exact,
          'scratch_removed': not scratch.exists(),
          'source_tree_changed_by_evaluator': False,
          'release_disposition': 'none', 'retirement_verdict': 'HOLD'}
(out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
(out / 'commands.json').write_text(json.dumps({'commands': commands, 'environment': {
    'inheritance': 'host environment, no credential variables recorded; no overrides',
    'PATH': os.environ.get('PATH'), 'platform': os.uname().sysname,
    'machine': os.uname().machine}}, indent=2) + '\n')
(out / 'MANIFEST.sha256').write_text(''.join(f'{sha(p.read_bytes())}  {p.relative_to(out)}\n' for p in sorted(out.rglob('*')) if p.is_file()))
print(json.dumps(result, indent=2))
