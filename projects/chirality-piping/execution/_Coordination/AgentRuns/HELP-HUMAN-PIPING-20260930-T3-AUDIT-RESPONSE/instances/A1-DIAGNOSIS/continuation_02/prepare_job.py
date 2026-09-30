"""Prepare one authorized job; read/hash files, never invoke a provider/compiler."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile

root=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip()).resolve()
run=root/'projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE'
a1=run/'instances/A1-DIAGNOSIS'; out=a1/'continuation_02'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate='888e388812f65dffce4428c96c18d2ddc8d2ae61'
grant=run/'decisions/05_A0_COMPILE_TRIAL_GRANT.md'
prompt=run/'instances/DESIGN/continuation_03/RESUME_PROMPT.md'
guard=run/'tools/host_guard_v2.py'
assert sha(grant)=='ddd05d9cd09cd7f55e8515ce3ce48a9c6a1787e94e7d451f17c45ece89a770e5'
assert sha(prompt)=='a71a4718b456743a377c12470352eb449c93a3cfe3e6393b971aed111ce852cb'
assert sha(guard)=='533a6f7506da4e031d8a824a27b4e9c496f374a3af8b7e98c72da55e8bbc26b5'
old=json.loads((a1/'CONTEXT.json').read_text())
instructions=['AGENTS.md','projects/chirality-piping/AGENTS.md','agents/AGENT_TASK.md','.agents/skills/software-defect-diagnosis/SKILL.md']
instruction_hashes={p:sha(root/p) for p in instructions}
for p,h in instruction_hashes.items(): assert h==next(s['sha256'] for s in old['sources'] if s['path']==p)
preserved=[]
for base in [a1,a1/'continuation_01']:
    for line in (base/'SHA256SUMS').read_text().splitlines():
        h,p=line.split('  ',1); assert sha(base/p)==h
        preserved.append(dict(path=str((base/p).relative_to(root)),sha256=h))
binding=json.loads((run/'RUNTIME_BINDING.json').read_text())
runtime=(Path(tempfile.gettempdir())/binding['runtime_directory_name']).resolve()
scratch=runtime/'scratch/a1-diagnosis'; target=runtime/'targets/a1/3bddc2b05f6106e969c7cf43373b230845c7cc66'
snap=json.loads((run/'runtime_setup/01_native_rust/A1_SOURCE_SNAPSHOT.json').read_text())
source=runtime/snap['runtime_relative_path']
assert {str(p.relative_to(source)) for p in source.rglob('*') if p.is_file()}=={f['path'] for f in snap['files']}
hashes={str(guard):sha(guard),str(grant):sha(grant),str(prompt):sha(prompt)}
for f in snap['files']:
    p=source/f['path']; assert sha(p)==f['sha256']; hashes[str(p)]=f['sha256']
for rel in ['Cargo.toml','oracle.py','matrix.json','src/main.rs','src/cases.rs']:
    p=scratch/rel; assert sha(p)==sha(a1/rel); hashes[str(p)]=sha(p)
assert sha(scratch/'Cargo.lock')==sha(a1/'continuation_01/Cargo.lock')
hashes[str(scratch/'Cargo.lock')]=sha(scratch/'Cargo.lock')
lock_context=json.loads((a1/'continuation_01/CONTEXT.json').read_text())
for tool in lock_context['native_toolchain_file_hashes']:
    p=runtime/tool['runtime_relative_path']; assert sha(p)==tool['sha256']; hashes[str(p)]=sha(p)
toolchain=runtime/'rustup/toolchains/1.97.1-aarch64-apple-darwin'
cargo=toolchain/'bin/cargo'; rustc=toolchain/'bin/rustc'
# Cargo walks from the invocation cwd to its ancestors, plus isolated CARGO_HOME.
configs=[]
for directory in [scratch,*scratch.parents]:
    for name in ['config','config.toml']:
        p=directory/'.cargo'/name
        item=dict(path=str(p),exists=p.exists())
        if p.exists():
            item.update(sha256=sha(p),text=p.read_text()); hashes[str(p)]=sha(p)
        configs.append(item)
for name in ['config','config.toml']:
    p=runtime/'cargo'/name
    item=dict(path=str(p),exists=p.exists())
    if p.exists(): item.update(sha256=sha(p),text=p.read_text()); hashes[str(p)]=sha(p)
    configs.append(item)
assert not any(c['exists'] for c in configs), 'Configuration exists: return for bounded review before invocation'
job_id='a1-compile-888e3888-20260930-01'
raw=scratch/job_id; assert not raw.exists(); assert not (runtime/'logs'/job_id).exists()
assert not (runtime/'guard/ACTIVE.json').exists(), 'Existing ACTIVE latch; ROOT resolution required'
raw.mkdir(mode=0o700); (scratch/'tmp').mkdir(mode=0o700,exist_ok=True)
env={'PATH':str(toolchain/'bin')+':/usr/bin:/bin:/usr/sbin:/sbin','LC_ALL':'C',
     'RUSTUP_HOME':str(runtime/'rustup'),'CARGO_HOME':str(runtime/'cargo'),
     'RUSTUP_TOOLCHAIN':'1.97.1','RUSTUP_AUTO_INSTALL':'0','CARGO_BUILD_JOBS':'1',
     'RUST_TEST_THREADS':'1','CARGO_INCREMENTAL':'0','CARGO_NET_OFFLINE':'true',
     'RUSTC':str(rustc),'CARGO_TARGET_DIR':str(target),'TMPDIR':str(scratch/'tmp'),
     'PYTHONDONTWRITEBYTECODE':'1'}
for key in ['HOME','CODEX_HOME']:
    if key in os.environ: env[key]=os.environ[key]
job=dict(job_id=job_id,run_id='HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE',candidate_sha=candidate,
         input_hashes=hashes,kind='compile',containment='inherited-group',cwd=str(scratch),
         command=[str(cargo),'build','--offline','--locked','--manifest-path',str(scratch/'Cargo.toml'),
                  '--bin','a1_public_probe','--no-default-features','-j','1'],env=env,
         limits=dict(cap_bytes=2147483648,allowance_bytes=134217728,disk_write_budget_bytes=1073741824,
                     disk_reserve_bytes=4294967296,max_seconds=300))
(raw/'job.json').write_text(json.dumps(job,indent=2)+'\n')
actual_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
record=dict(status='PREPARED_NOT_INVOKED',actual_head=actual_head,candidate=candidate,
            numerical_source=snap['source_commit'],instruction_hashes=instruction_hashes,
            old_seals_verified=preserved,input_hashes=hashes,configs=configs,
            target_existed_before=target.exists(),active_latch_before=False,job_spec_sha256=sha(raw/'job.json'),
            runtime=str(runtime),raw_directory=str(raw),guard=str(guard),python_executable=sys.executable,
            env_keys=list(env),live_preflight='Mandatory in guard invocation; not yet sampled')
(raw/'PRECHECK.raw.json').write_text(json.dumps(record,indent=2)+'\n')
def sanitize(text):
    for old,new in [(str(runtime),'<RESPONSE_RUNTIME>'),(str(root),'<REPO_ROOT>')]: text=text.replace(old,new)
    if 'HOME' in os.environ: text=text.replace(os.environ['HOME'],'<OWNER_HOME>')
    return text
(out/'JOB_SPEC.sanitized.json').write_text(sanitize((raw/'job.json').read_text()))
(out/'PRECHECK.sanitized.json').write_text(sanitize((raw/'PRECHECK.raw.json').read_text()))
(out/'RAW_BINDING.json').write_text(json.dumps(dict(runtime_directory_name=binding['runtime_directory_name'],
    scratch_relative_path='scratch/a1-diagnosis/'+job_id,guard_log_relative_path='logs/'+job_id,
    job_id=job_id,raw_spec_sha256=sha(raw/'job.json'),raw_precheck_sha256=sha(raw/'PRECHECK.raw.json')),indent=2)+'\n')
print(json.dumps(dict(status='PREPARED_NOT_INVOKED',job_id=job_id,verified_input_hashes=len(hashes),
    old_seal_entries_verified=len(preserved),cargo_configs_present=0,actual_head=actual_head)))
