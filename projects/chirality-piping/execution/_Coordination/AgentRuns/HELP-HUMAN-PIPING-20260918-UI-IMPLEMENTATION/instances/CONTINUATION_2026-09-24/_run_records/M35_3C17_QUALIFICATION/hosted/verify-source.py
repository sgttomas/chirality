"""Verify complete hosted source identity/execution; export binding only on success."""
import argparse, ast, collections, hashlib, json, pathlib, re, subprocess
ap=argparse.ArgumentParser();ap.add_argument('--head',required=True);ap.add_argument('--repo',required=True);ap.add_argument('--pr',required=True,type=int)
a=ap.parse_args();p=pathlib.Path(__file__).resolve().parent;repo=pathlib.Path(a.repo);head=a.head
project='projects/chirality-piping/';desktop=project+'apps/desktop/'
load=lambda f:json.loads(f.read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *v:subprocess.check_output(['git','-C',str(repo),*v])
r=load(p/'run.json');jobs=load(p/'jobs.json')['jobs'];request=load(p/'pr.json')
assert r['head_sha']==head and r['status']=='completed' and r['conclusion']=='success', 'Complete successful exact-head workflow required'
assert request['number']==a.pr and request['head']['sha']==head, 'Superseded run cannot qualify current PR head'
plan=load(p/'extracted/piping-e2e-selection/piping-e2e-plan.json')
assert plan['mode']=='full' and plan['coverage_full'] and plan['head']==head and plan['pr']==str(a.pr)
specs=sorted(x[len(desktop):] for x in git('ls-tree','-r','--name-only',head,desktop+'e2e').decode().splitlines()
    if re.search(r'\.(spec|test)\.[cm]?[jt]sx?$',pathlib.PurePosixPath(x).name) and not x.endswith('-dist.spec.ts'))
assert plan['inventory']==specs and plan['selected_specs']==specs
selector=git('show',head+':'+project+'tools/ci/e2e_plan.py');profiles=None
for node in ast.parse(selector).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PROJECTS' for t in node.targets):profiles=ast.literal_eval(node.value)
assert profiles and plan['projects']==profiles
key=lambda row:(row['id'],row['project'],row['file'],tuple(row['title_path']))
def collected(report):
    out=[]
    def visit(s,titles):
        for spec in s.get('specs',[]):
            for t in spec['tests']:
                out.append({'id':spec['id'],'project':t['projectName'],'file':'e2e/'+spec['file'],'title_path':titles+[spec['title']]})
        for child in s.get('suites',[]):visit(child,titles+[child['title']] if child.get('line',0) else titles)
    assert not report.get('errors');visit(report,[]);return out
union=[];base=None;stages=set();summaries=[];configured_partitions=None
for file in sorted((p/'extracted').glob('*/collection.json')):
    c=load(file)
    assert c['head']==head and c['status']=='validated' and c['mode']=='full' and not c['omitted']
    assert c['plan_sha256']==sha(json.dumps(plan,sort_keys=True).encode())
    identity=c['identity']
    for field,name in [('config_sha256',desktop+'playwright.config.ts'),('selector_sha256',project+'tools/ci/e2e_plan.py'),('duration_hints_sha256',project+'tools/ci/e2e_duration_hints.json')]:
        assert identity[field]==sha(git('show',head+':'+name))
    assert sorted(identity['source_file_sha256'])==specs
    for name,expected in identity['source_file_sha256'].items():assert expected==sha(git('show',head+':'+desktop+name))
    source=collections.Counter(map(key,collected(load(file.parent/'source.stdout.json'))))
    assert source and all(v==1 for v in source.values())
    assert collections.Counter(map(key,c['selected']))==source
    if base is None:base=source
    assert source==base and {x[1] for x in source}==set(profiles)
    partition=collections.Counter(key(t) for part in c['partition'].values() for t in part);assert partition==base
    if configured_partitions is None:configured_partitions=set(c['partition'])
    assert set(c['partition'])==configured_partitions
    stage='barrier' if c['stage']=='barrier' else f"shard-{c['shard']}"
    assert stage not in stages;stages.add(stage)
    assert collections.Counter(map(key,c['execution_tests']))==collections.Counter(map(key,c['partition'][stage]))
    jobname='Accessibility barrier and selected coverage' if stage=='barrier' else f"Source remainder ({c['shard']}/{len(configured_partitions)-1})"
    job=next(j for j in jobs if j['name']==jobname)
    stepname='Run accessibility first, then any reduced selection' if stage=='barrier' else 'Run isolated source remainder shard'
    step=next(s for s in job['steps'] if s['name']==stepname)
    assert job['head_sha']==head and job['conclusion']=='success' and step['conclusion']=='success'
    log=(p/f"job-{job['id']}.log").read_text()
    running=[int(x) for x in re.findall(r'Running (\d+) tests? using',log)]
    passed=[int(x) for x in re.findall(r'Z\s+(\d+) passed \(',log)]
    skipped=[int(x) for x in re.findall(r'Z\s+(\d+) skipped\s*$',log,re.M)]
    assert sum(running)==len(c['execution_tests']) and sum(passed)+sum(skipped)==sum(running)
    union+=c['execution_tests']
    summaries.append({'stage':stage,'job_id':job['id'],'job_url':job['html_url'],'step':step,'identities':len(c['execution_tests']),
        'passed':sum(passed),'skipped':sum(skipped),'collection':str(file.relative_to(p)),'collection_sha256':sha(file.read_bytes())})
assert configured_partitions and stages==configured_partitions and collections.Counter(map(key,union))==base
aggregate=next(j for j in jobs if j['name']=='Desktop E2E (source mode)')
assert aggregate['head_sha']==head and aggregate['conclusion']=='success'
assert next(s for s in aggregate['steps'] if s['name']=='Require all planned coverage')['conclusion']=='success'
report={'reviewer':'/root/m35_integration_review','head':head,'pr':a.pr,'run_id':r['id'],'run_url':r['html_url'],'run_attempt':r['run_attempt'],
    'canonical_identity':['id','project','file','title_path'],'candidate_inventory_files':len(specs),'candidate_inventory':specs,
    'source_hashes_against_exact_git_verified':True,'discovered':len(base),'union':len(union),'missing':0,'duplicates':0,'unexpected':0,
    'profiles':profiles,'passed':sum(x['passed'] for x in summaries),'skipped':sum(x['skipped'] for x in summaries),'jobs':summaries,
    'limitations':'Collection artifacts establish identities; successful hosted execution steps/raw logs establish execution. Skips are not passes. Separate governance/native/DEC025/acceptance gates are not cleared.'}
(p/'IDENTITY_EXECUTION_CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
binding={'workflow_path':'.github/workflows/piping-desktop-e2e.yml','run_id':r['id'],'run_attempt':r['run_attempt'],'head_sha':head,
    'conclusion':'success','registered_e2e_specs_executed':True,'viewport_projects':profiles}
(p/'surface4-ci-binding.json').write_text(json.dumps(binding,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['head','run_id','candidate_inventory_files','discovered','passed','skipped','missing','duplicates','unexpected']}))
