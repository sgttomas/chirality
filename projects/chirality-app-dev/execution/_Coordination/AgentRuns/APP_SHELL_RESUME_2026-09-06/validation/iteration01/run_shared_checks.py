"""Run parent-released shared checks only; no frontend build or browser work."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import subprocess

repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
work = repo / 'projects/chirality-app-dev'
out = Path(__file__).resolve().parent
environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
checks = [
    ('receipt-pre-append', repo, ['python3', 'tools/validation/validate_app_dev_loop_receipts.py', '--repo-root', '.']),
    ('corpus-status', work, ['python3', 'execution/_Reconciliation/References/reconcile_authority_corpus.py', 'status']),
    ('self-check', repo, ['python3', 'tools/practitioner_harness/harness.py', 'self-check']),
    ('harness-pytest', repo, ['python3', '-m', 'pytest', 'tools/practitioner_harness', '-q', '-p', 'no:cacheprovider']),
    ('app-hold-reliance', work, ['python3', 'execution/_Scripts/app_hold.py', 'check', '--operation', 'reliance', '--entry-path', 'HELP_HUMAN:APP_SHELL_RESUME_2026-09-06:RECORDS:PROGRESS', '--target', 'DEL-02-01', '--target', 'DEL-02-02', '--target', 'DEL-02-03', '--target', 'DEL-02-04', '--target', 'DEL-02-05', '--target', 'DEL-07-03']),
]

def run(item):
    name, cwd, argv = item
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(argv, cwd=cwd, env=environment, capture_output=True)
    identities = []
    for suffix, data in [('stdout.txt', result.stdout), ('stderr.txt', result.stderr)]:
        p = out / f'{name}.{suffix}'
        with p.open('xb') as f:
            f.write(data)
        identities.append({'path': p.name, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)})
    return {'name': name, 'argv': argv, 'cwd': cwd.relative_to(repo).as_posix(), 'explicit_environment': {'PYTHONDONTWRITEBYTECODE': '1'}, 'started_at': started, 'finished_at': datetime.now(timezone.utc).isoformat(), 'exit_code': result.returncode, 'outputs': identities}

with ThreadPoolExecutor(max_workers=len(checks)) as pool:
    results = list(pool.map(run, checks))
record = {'phase': 'iteration01-progress, before source-manager fan-in and before receipt append', 'repo_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(), 'branch': subprocess.check_output(['git', 'branch', '--show-current'], text=True).strip(), 'checks': results, 'limitations': 'No frontend typecheck/test/build, browser, runtime dependency install or sibling build performed. No final receipt/completion update or final union review claimed. Inherited environment values/secrets not captured. Worktree may contain concurrent package-owned edits; these are progress-time results.'}
with (out / 'CHECKS_v1.json').open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
print(json.dumps([{'name': r['name'], 'exit_code': r['exit_code']} for r in results], indent=2))
