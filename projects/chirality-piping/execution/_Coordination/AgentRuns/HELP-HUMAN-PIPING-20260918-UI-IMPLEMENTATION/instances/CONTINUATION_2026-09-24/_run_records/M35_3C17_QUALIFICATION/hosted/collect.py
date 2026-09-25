"""Acquire exact-head existing CI evidence; never rerun or mutate GitHub."""
from pathlib import Path
import argparse, concurrent.futures, datetime, hashlib, json, subprocess, zipfile

ap=argparse.ArgumentParser()
ap.add_argument('--run-id', required=True, type=int)
ap.add_argument('--head', required=True)
ap.add_argument('--pr', required=True, type=int)
args=ap.parse_args()
p=Path(__file__).resolve().parent
prefix='repos/sgttomas/chirality/'
def acquire(endpoint,path):
    with path.open('wb') as out:
        subprocess.run(['gh','api',prefix+endpoint],stdout=out,check=True)
    return {'endpoint':prefix+endpoint,'path':str(path.relative_to(p)),
            'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
requests=[(f'actions/runs/{args.run_id}',p/'run.json'),
          (f'actions/runs/{args.run_id}/jobs?per_page=100',p/'jobs.json'),
          (f'actions/runs/{args.run_id}/artifacts?per_page=100',p/'artifacts.json'),
          (f'pulls/{args.pr}',p/'pr.json')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(lambda x:acquire(*x),requests))
run=json.loads((p/'run.json').read_text())
assert run['head_sha']==args.head
assert run['path']=='.github/workflows/piping-desktop-e2e.yml'
assert run['event']=='pull_request'
assert any(x['number']==args.pr for x in run['pull_requests'])
aj=json.loads((p/'artifacts.json').read_text());jj=json.loads((p/'jobs.json').read_text())
arts=aj['artifacts'];jobs=jj['jobs']
assert len(arts)==aj['total_count'] and len(jobs)==jj['total_count'], 'Pagination required'
for a in arts:
    assert not a['expired'] and Path(a['name']).name==a['name']
    assert a['workflow_run']['id']==args.run_id and a['workflow_run']['head_sha']==args.head
requests=[(f"actions/artifacts/{a['id']}/zip",p/(a['name']+'.zip')) for a in arts]
requests += [(f"actions/jobs/{j['id']}/logs",p/f"job-{j['id']}.log") for j in jobs
             if j['status']=='completed' and j['conclusion']!='skipped']
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records.extend(pool.map(lambda x:acquire(*x),requests))
for a in arts:
    target=p/'extracted'/a['name'];target.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(p/(a['name']+'.zip')) as z:
        assert all((target/name).resolve().is_relative_to(target.resolve()) for name in z.namelist())
        z.extractall(target)
(p/'ACQUISITION.json').write_text(json.dumps({'actor':'/root/m35_integration_review','parent':'/root',
    'role':'TASK','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'run_id':args.run_id,'expected_head':args.head,'pr':args.pr,'status':run['status'],
    'conclusion':run['conclusion'],'requests':records,
    'limits':'Acquisition only; incomplete, cancelled, failed, or skipped execution is never promoted to PASS.'},indent=2)+'\n')
print(json.dumps({'artifacts':len(arts),'jobs':len(jobs),'run':args.run_id,'head':run['head_sha'],
                 'status':run['status'],'conclusion':run['conclusion']}))
