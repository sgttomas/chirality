from pathlib import Path
import subprocess,os,json,datetime,hashlib
root=Path('/private/tmp/piping-first-correctness-20260924');p=root/'projects/chirality-piping'
out=Path(__file__).parent
manifest='validation/benchmarks/physics_audit_regression/Cargo.toml'
env=os.environ.copy();env.update(CARGO_BUILD_JOBS='2',CARGO_NET_OFFLINE='true',CARGO_TARGET_DIR='/private/tmp/piping-solver-correctness-target')
cmd=['cargo','test','--offline','--locked','--manifest-path',manifest,'--test','authored_units_product','--no-run','-vv']
record={'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'command':cmd,'cwd':str(p),'environment':{k:env[k] for k in ['CARGO_BUILD_JOBS','CARGO_NET_OFFLINE','CARGO_TARGET_DIR']},'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
with (out/'shared-reproduction.log').open('w') as f:r=subprocess.run(cmd,cwd=p,env=env,stdout=f,stderr=subprocess.STDOUT)
record.update(exit_code=r.returncode,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),log_sha256=hashlib.sha256((out/'shared-reproduction.log').read_bytes()).hexdigest())
(out/'shared-reproduction.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
