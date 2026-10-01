"""One decision07 B case per invocation under guard v3, guarded and compared. No loop/retry/repair."""
from pathlib import Path
import hashlib,json,os,re,subprocess,sys,tempfile,time

here=Path(__file__).resolve().parent
a1=here.parent; run=here.parents[2]
root=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip()).resolve()
assert len(sys.argv)==2 and re.fullmatch(r'B(?:0[2-9]|1[0-6])',sys.argv[1])
cid=sys.argv[1]; number=int(cid[1:])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
grant=run/'decisions/07_A0_B_RESUME_AFTER_GUARD_V3.md'; prompt=run/'instances/DESIGN/continuation_06/RESUME_PROMPT.md'
guard=run/'tools/host_guard_v3.py'; oracle=a1/'oracle.py'
assert sha(grant)=='421d4005a4558041d28e9b92fda259da2944f625eb0e29a55834d46ae4084db3'
assert sha(prompt)=='4328889932f19278f2ca1a712d3952d89ee3070c5a00f1f3b85aeba21681a767'
assert sha(guard)=='b32050c72d0bbad0f69526fc98d1f28dcb1fa131115227a2169db8100d66848b'
assert sha(oracle)=='35cf4b9321ebe126693e52ad96ea010bed9f280c3058d02fbae98c17275627be'
if number>2:
    prior=json.loads((here/'cases'/f'B{number-1:02}'/'CASE_RESULT.json').read_text())
    assert prior['may_consider_next_B'], 'Prior case stopped tranche'
    review=json.loads((here/'cases'/f'B{number-1:02}'/'TASK_REVIEW.json').read_text())
    assert review['advance_allowed'], 'No explicit TASK inspection of prior case'
assert json.loads((a1/'continuation_03/cases/B01/CASE_RESULT.json').read_text())['guard_healthy']
assert not json.loads((a1/'continuation_03/cases/B02/CASE_RESULT.json').read_text())['guard_healthy']
binding=json.loads((run/'RUNTIME_BINDING.json').read_text())
runtime=(Path(tempfile.gettempdir())/binding['runtime_directory_name']).resolve()
scratch=runtime/'scratch/a1-diagnosis'; target=runtime/'targets/a1/3bddc2b05f6106e969c7cf43373b230845c7cc66'
binary=target/'debug/a1_public_probe'
assert sha(binary)=='426fb26fb52e8f7781ebef8d0876ba74ba6c025ada4a66b5532423b462a9b386'
hashes={str(p):sha(p) for p in [grant,prompt,guard,oracle,a1/'matrix.json',binary]}
snapshot=json.loads((run/'runtime_setup/01_native_rust/A1_SOURCE_SNAPSHOT.json').read_text())
source=runtime/snapshot['runtime_relative_path']
assert len(snapshot['files'])==36
assert {str(p.relative_to(source)) for p in source.rglob('*') if p.is_file()}=={f['path'] for f in snapshot['files']}
for item in snapshot['files']:
    p=source/item['path']; assert sha(p)==item['sha256']; hashes[str(p)]=sha(p)
for rel in ['Cargo.toml','src/main.rs','src/cases.rs','matrix.json','oracle.py']:
    p=scratch/rel; assert sha(p)==sha(a1/rel); hashes[str(p)]=sha(p)
assert sha(scratch/'Cargo.lock')==sha(a1/'continuation_01/Cargo.lock'); hashes[str(scratch/'Cargo.lock')]=sha(scratch/'Cargo.lock')
old=json.loads((a1/'CONTEXT.json').read_text())
for rel in ['AGENTS.md','projects/chirality-piping/AGENTS.md','agents/AGENT_TASK.md','.agents/skills/software-defect-diagnosis/SKILL.md']:
    assert sha(root/rel)==next(x['sha256'] for x in old['sources'] if x['path']==rel)
    hashes[str(root/rel)]=sha(root/rel)
preserved=[]
for base in [a1,a1/'continuation_01',a1/'continuation_02',a1/'continuation_03',run/'instances/ROOT-A0-BUILD']:
    for line in (base/'SHA256SUMS').read_text().splitlines():
        h,rel=line.split('  ',1); assert sha(base/rel)==h
        preserved.append(dict(path=str((base/rel).relative_to(root)),sha256=h))
job_id='a1-b-v3-'+cid.lower()+'-325516a7-20260930-01'
raw=scratch/'b-tranche-v3-20260930'/cid
raw.mkdir(mode=0o700,parents=True,exist_ok=False)
out=here/'cases'/cid; out.mkdir(parents=True,exist_ok=False)
env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','LC_ALL':'C','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(scratch/'tmp')}
for key in ['HOME','CODEX_HOME']:
    if key in os.environ: env[key]=os.environ[key]
job=dict(job_id=job_id,run_id='HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE',
    candidate_sha='325516a7bb21492458d2c84026db709de8b1b4d9',input_hashes=hashes,
    kind='tiny-probe',containment='inherited-group',cwd=str(scratch),
    command=[str(binary),cid,'100000000','100000000','B'],env=env,
    limits=dict(cap_bytes=536870912,allowance_bytes=134217728,disk_write_budget_bytes=134217728,
                disk_reserve_bytes=4294967296,max_seconds=60))
spec=raw/'job.json'; spec.write_text(json.dumps(job,indent=2)+'\n')
def sanitize(text):
    text=text.replace(str(runtime),'<RESPONSE_RUNTIME>').replace(str(root),'<REPO_ROOT>')
    if 'HOME' in os.environ: text=text.replace(os.environ['HOME'],'<OWNER_HOME>')
    return text
pre=dict(actual_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),input_hashes=hashes,
         preserved_manifest_entries=preserved,active_latch_before=(runtime/'guard/ACTIVE.json').exists(),
         job_spec_sha256=sha(spec),candidate=job['candidate_sha'])
(raw/'PRECHECK.json').write_text(json.dumps(pre,indent=2)+'\n')
(out/'PRECHECK.sanitized.json').write_text(sanitize((raw/'PRECHECK.json').read_text()))
(out/'JOB_SPEC.sanitized.json').write_text(sanitize(spec.read_text()))
command=[sys.executable,str(guard),'run','--runtime-dir',str(runtime),'--job-spec',str(spec)]
started=time.monotonic(); wall=time.time_ns()
with open(raw/'INVOCATION_STARTED.json','x') as f: json.dump(dict(wall_ns=wall,pid=os.getpid()),f)
with open(raw/'guard.stdout','xb') as stdout,open(raw/'guard.stderr','xb') as stderr:
    process=subprocess.Popen(command,env=env,cwd=root,stdout=stdout,stderr=stderr)
    guard_code=process.wait()
elapsed=time.monotonic()-started
logdir=runtime/'logs'/job_id
events=[json.loads(line) for line in (logdir/'monitor.jsonl').read_text().splitlines()] if (logdir/'monitor.jsonl').exists() else []
guard_results=[e['data'] for e in events if e['kind']=='result']
samples=[e['data']['sample'] for e in events if e['kind'] in ('preflight','prelaunch','sample')]
work_samples=[e['data']['sample'] for e in events if e['kind']=='sample']
post=[dict(path=p,before=h,after=sha(Path(p)),match=sha(Path(p))==h) for p,h in hashes.items()]
post_ok=all(x['match'] for x in post)
(raw/'POSTCHECK.json').write_text(json.dumps(dict(input_hashes=post,actual_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()),indent=2)+'\n')
(out/'POSTCHECK.sanitized.json').write_text(sanitize((raw/'POSTCHECK.json').read_text()))
healthy=guard_code==0 and len(guard_results)==1 and guard_results[0]['guard_healthy'] and guard_results[0]['workload_returncode']==0 and not (runtime/'guard/ACTIVE.json').exists()
supervisor_events=[json.loads(line) for line in (logdir/'supervisor.jsonl').read_text().splitlines()] if (logdir/'supervisor.jsonl').exists() else []
exited_unmeasured=sorted({e['data']['pid'] for e in events+supervisor_events if e['kind']=='member-exit-confirmed' and e['data']['measurement_state']=='exited-unmeasured'})
zombie_unmeasured=sorted({pid for e in events+supervisor_events if e['kind']=='group-collection' for pid in e['data']['zombie_present_unmeasured']})
comparison=None; comparator_code=None; status=None; selected=None; meter=None
workload=logdir/'workload.log'
if healthy and workload.exists():
    for line in workload.read_text().splitlines():
        v=line.split('\t')
        if v[0]=='STATUS': status=v[1]
        elif v[0]=='SELECTED': selected=[int(v[1]),int(v[2])]
        elif v[0]=='METER': meter=[int(v[1]),int(v[2]),v[3]]
    with open(raw/'comparison.stdout.json','xb') as stdout,open(raw/'comparison.stderr','xb') as stderr:
        comparator_code=subprocess.run([sys.executable,str(oracle),'compare',str(workload)],env=env,cwd=root,stdout=stdout,stderr=stderr).returncode
    if comparator_code==0:
        try: comparison=json.loads((raw/'comparison.stdout.json').read_text())
        except Exception: comparison=None
    (out/'COMPARISON.json').write_bytes((raw/'comparison.stdout.json').read_bytes())
    (out/'comparison.stderr').write_text(sanitize((raw/'comparison.stderr').read_text()))
inventory=[]
for source_dir,prefix in [(raw,'controller'),(logdir,'guard')]:
    if not source_dir.exists(): continue
    for p in sorted(source_dir.iterdir()):
        if p.is_file():
            dest=out/(prefix+'-'+p.name)
            dest.write_text(sanitize(p.read_text()))
            inventory.append(dict(runtime_relative_path=str(p.relative_to(runtime)),raw_sha256=sha(p),raw_size_bytes=p.stat().st_size,
                                  sanitized_file=dest.name,sanitized_sha256=sha(dest)))
(out/'RAW_INVENTORY.json').write_text(json.dumps(inventory,indent=2)+'\n')
may_next=bool(healthy and post_ok and comparator_code==0 and comparison is not None and not comparison.get('violations')
              and status in ['Selected','SourceRefused','Refused','Unresolved'])
result=dict(case=cid,job_id=job_id,guard_returncode=guard_code,guard_result=guard_results,guard_healthy=healthy,
    elapsed_seconds=elapsed,preflight_sample_count=sum(e['kind']=='preflight' for e in events),
    work_sample_count=len(work_samples),sampled_rss_peak_bytes=max((s['rss_bytes'] for s in samples),default=None),
    sampled_footprint_peak_bytes=max((s['footprint_bytes'] for s in samples),default=None),
    minimum_observed_available_pct=min((s['available_pct'] for s in samples),default=None),
    active_latch_after=(runtime/'guard/ACTIVE.json').exists(),post_hashes_match=post_ok,case_status=status,
    exited_unmeasured_pids=exited_unmeasured,zombie_present_unmeasured_pids=zombie_unmeasured,
    memory_limit='Sampled validated group values only; exited-unmeasured members have no measured lifetime peaks, never zero memory.',
    selected_precisions=selected,meter=meter,comparator_returncode=comparator_code,
    comparison_disposition=comparison.get('disposition') if comparison else None,
    comparison_rows=len(comparison.get('comparisons',[])) if comparison else None,
    comparison_violations=comparison.get('violations') if comparison else None,
    comparison_limits=comparison.get('limits') if comparison else None,may_consider_next_B=may_next,
    stop_reason=None if may_next else 'host_guard_or_comparator_or_input_integrity_stop',
    false_claims=[x for x in comparison.get('violations',[]) if x.startswith('claim:')] if comparison else [],
    binary_sha256=sha(binary),oracle_sha256=sha(oracle),job_spec_sha256=sha(spec),numerical_source=snapshot['source_commit'],
    source_json_sha256=next(c['input_json_sha256'] for c in json.loads((a1/'matrix.json').read_text())['cases'] if c['id']==cid))
(out/'CASE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(0 if may_next else 2)
