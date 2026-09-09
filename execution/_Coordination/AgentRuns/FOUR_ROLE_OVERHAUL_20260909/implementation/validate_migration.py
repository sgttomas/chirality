#!/usr/bin/env python3
"""Validate this migration's inventory, historical custody and concrete routing."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    plan = json.loads((HERE / 'MIGRATION_PLAN.json').read_text())
    checks = []
    def check(name, ok, detail=None):
        checks.append({'check': name, 'pass': bool(ok), 'detail': detail})
    subjects = plan['dispositions']
    check('source component coverage', len(subjects) == 79 and len({s['source'] for s in subjects}) == 79)
    check('original agent coverage', sum(s['source'].startswith('agents/') for s in subjects) == 34)
    check('original workflow coverage', sum(s['source'].startswith('skills/') for s in subjects) == 45)
    check('original package file coverage', sum(len(s.get('files', [])) for s in subjects) == 183)
    original_files = {s['source']: s['source_sha256'] for s in subjects}
    for subject in subjects:
        for item in subject.get('files', []):
            original_files[item['path']] = item['sha256']
        destination = ROOT / subject['destination']
        check('destination ' + subject['source'], destination.is_file(), subject['destination'])
        if subject['disposition'] != 'retain-role':
            check('retired source ' + subject['source'], not (ROOT / subject['source']).exists())
    for path, expected in original_files.items():
        result = subprocess.run(['git','show',f"{plan['basis']}:{path}"], cwd=ROOT, capture_output=True)
        check('original basis ' + path, result.returncode == 0 and hashlib.sha256(result.stdout).hexdigest() == expected)
    check('four role files', sorted(p.name for p in (ROOT/'agents').glob('AGENT_*.md')) ==
          sorted('AGENT_'+name+'.md' for name in ['HELP_HUMAN','HELPS_HUMANS','WORKING_ITEMS','TASK']))
    entrypoints = sorted((ROOT/'workflows').glob('*/WORKFLOW.md'))
    check('71 workflow entrypoints', len(entrypoints) == 71)
    aliases = json.loads((ROOT/'workflows/legacy-agents.json').read_text())['aliases']
    retired = {Path(s['source']).stem[6:] for s in subjects if s['source'].startswith('agents/') and s['disposition'] != 'retain-role'}
    check('all retired role aliases', set(aliases) == retired)
    for name, alias in aliases.items():
        destination = ROOT / ('workflows/'+alias['workflow']+'/WORKFLOW.md' if 'workflow' in alias else alias['tool'])
        check('alias destination '+name, destination.is_file())
    next_hits=[]
    for path in (ROOT/'workflows').rglob('*'):
        if path.is_file() and path.suffix in {'.md','.json'}:
            if re.search(r'NEXT_INSTANCE_(?:PROMPT|STATE)', path.read_text()): next_hits.append(str(path.relative_to(ROOT)))
    check('human continuation-contract exclusion', not next_hits, next_hits)
    routes=json.loads((HERE/'NOTICE_ROUTES.json').read_text())['routes']
    check('five coordination routes', len(routes)==5 and all((ROOT/p).is_file() for p in routes))
    census=json.loads((HERE/'DOWNSTREAM_REFERENCE_CENSUS.json').read_text())['records']
    changed=[record['path'] for record in census if not (ROOT/record['path']).is_file() or digest(ROOT/record['path'])!=record['sha256']]
    check('downstream referenced bytes preserved', not changed, changed)
    broken=[]
    for path in (ROOT/'workflows').rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            target=target.strip('<>').split('#')[0]
            if not target or '://' in target or target in {'path','...'} or any(c in target for c in '{<*$…') or target.startswith('/Users/'): continue
            target=re.sub(r':\d+$','',target)
            if not (path.parent/target).exists(): broken.append({'path':str(path.relative_to(ROOT)),'target':target})
    check('explicit relative workflow links', not broken, broken)
    result={'status':'PASS' if all(c['pass'] for c in checks) else 'FAIL','checks':checks,'count':len(checks),
            'limits':'Inventory/custody/link verification; semantic migration judgment and downstream adoption are separate.'}
    print(json.dumps(result,indent=2))
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__':
    sys.exit(main())
