"""Verify retained hosted numerical evidence against exact candidate Git objects."""
import argparse, ast, hashlib, json, pathlib, re, subprocess
ap=argparse.ArgumentParser();ap.add_argument('--head',required=True);ap.add_argument('--repo',required=True)
a=ap.parse_args();p=pathlib.Path(__file__).resolve().parent;repo=pathlib.Path(a.repo);head=a.head
project='projects/chirality-piping/'
load=lambda f:json.loads(f.read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *v:subprocess.check_output(['git','-C',str(repo),*v])
r=load(p/'run.json');job=next(j for j in load(p/'jobs.json')['jobs'] if j['name']=='Numerical cargo suite')
nroot=p/'extracted'/f"piping-numerical-{r['id']}-{r['run_attempt']}";n=load(nroot/'numerical.json')
assert r['head_sha']==job['head_sha']==n['head']==head
assert job['conclusion']=='success' and n['status']=='success' and n['exit_code']==0 and n['plan_validated'] is True
assert next(s for s in job['steps'] if s['name']=='Fetch locked dependencies and run offline numerical tests')['conclusion']=='success'
readiness=git('show',head+':'+project+'tools/release/check_release_readiness.py')
tree=ast.parse(readiness);roots=None
for node in tree.body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CARGO_SEARCH_ROOTS' for t in node.targets):
        roots=ast.literal_eval(node.value)
assert roots
tracked=git('ls-tree','-r','--name-only',head,*[project+x for x in roots]).decode().splitlines()
manifests=[]
for root in roots:
    manifests.extend(sorted(x[len(project):] for x in tracked if x.startswith(project+root+'/')
        and x.endswith('/Cargo.toml') and 'target' not in pathlib.PurePosixPath(x).parts))
assert manifests and len(manifests)==len(set(manifests)) and manifests==n['manifests']
inputs=set(manifests)|{str(pathlib.PurePosixPath(x).with_name('Cargo.lock')) for x in manifests}
assert set(n['input_sha256'])==inputs
for name in sorted(inputs):
    b=git('show',head+':'+project+name);assert sha(b)==n['input_sha256'][name]
    f=p/'candidate-inputs'/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b)
method_hashes={}
for name in ['tools/ci/numerical_ci.py','tools/release/check_release_readiness.py']:
    b=git('show',head+':'+project+name);(p/pathlib.Path(name).name).write_bytes(b);method_hashes[name]=sha(b)
fetches=[['cargo','fetch','--locked','--manifest-path',m] for m in manifests]
tests=[['cargo','test','--offline','--manifest-path',m,'--locked'] for m in manifests]
expected=[['rustc','--version'],['cargo','--version']]+fetches+tests
assert [x['argv'] for x in n['commands']]==expected and n['planned_commands']==fetches+tests
assert len(n['commands'])==2+2*len(manifests) and all(x['exit_code']==0 for x in n['commands'])
for command in n['commands']:
    assert sha((nroot/command['output']).read_bytes())==command['output_sha256']
results=[]
for command in n['commands'][2+len(manifests):]:
    text=(nroot/command['output']).read_text()
    summaries=re.findall(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out',text)
    assert summaries and all(int(x[1])==0 for x in summaries)
    results.append({'manifest':command['argv'][command['argv'].index('--manifest-path')+1],
        'exit_code':command['exit_code'],'summary_groups':len(summaries),'passed':sum(int(x[0]) for x in summaries),
        'ignored':sum(int(x[2]) for x in summaries),'filtered_out':sum(int(x[4]) for x in summaries)})
log=(p/f"job-{job['id']}.log").read_text();assert all('Running: '+' '.join(argv) in log for argv in expected)
report={'reviewer':'/root/m35_integration_review','candidate':head,'run_id':r['id'],'run_url':r['html_url'],
    'run_conclusion_at_acquisition':r['conclusion'],'job_id':job['id'],'job_url':job['html_url'],'job_conclusion':'success',
    'discovered_manifests':len(manifests),'locked_fetches':len(fetches),'locked_offline_tests':len(tests),
    'commands_total':len(expected),'all_command_exit_codes_zero':True,'tool_version_commands':2,
    'input_hashes_verified_against_exact_git_objects':len(inputs),'output_hashes_verified':len(n['commands']),
    'missing_manifests':0,'duplicate_manifests':0,'unexpected_manifests':0,'method_hashes':method_hashes,
    'tool_versions':{x['argv'][0]:(nroot/x['output']).read_text().strip() for x in n['commands'][:2]},
    'environment':n['environment'],'crate_results':results,'test_summary_passed':sum(x['passed'] for x in results),
    'test_summary_ignored':sum(x['ignored'] for x in results),
    'boundary':'Exact-head hosted numerical job verification, not local execution, native behavior, full workflow success, engineering acceptance or release.'}
(p/'NUMERICAL_EXECUTION_CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['candidate','discovered_manifests','commands_total','test_summary_passed','test_summary_ignored']}))
