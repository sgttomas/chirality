from pathlib import Path
import subprocess,os,json,datetime,hashlib,tempfile
root=Path('/private/tmp/piping-first-correctness-20260924');p=root/'projects/chirality-piping';out=Path(__file__).parent
fresh=Path(tempfile.mkdtemp(prefix='piping-serde-isolation-20260924-',dir='/private/tmp'))
env=os.environ.copy();env.update(CARGO_BUILD_JOBS='2',CARGO_NET_OFFLINE='true',CARGO_TARGET_DIR=str(fresh))
records=[]
commands=[('audit-fresh',['cargo','test','--offline','--locked','--manifest-path','validation/benchmarks/physics_audit_regression/Cargo.toml','--test','authored_units_product','-vv']),('applier-overwrite',['cargo','build','--offline','--locked','--manifest-path','core/model_operations/operation_applier/Cargo.toml','-vv']),('audit-after-overwrite',['cargo','test','--offline','--locked','--manifest-path','validation/benchmarks/physics_audit_regression/Cargo.toml','--test','authored_units_product','--no-run','-vv'])]
for label,cmd in commands:
 rec={'label':label,'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'cwd':str(p),'command':cmd,'target':str(fresh),'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 with (out/(label+'.log')).open('w') as f:r=subprocess.run(cmd,cwd=p,env=env,stdout=f,stderr=subprocess.STDOUT)
 rec.update(exit_code=r.returncode,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),log_sha256=hashlib.sha256((out/(label+'.log')).read_bytes()).hexdigest())
 for name in ['libopen_pipe_stress_operation_applier.rlib','libopen_pipe_stress_operation_applier.dylib']:
  f=fresh/'debug/deps'/name
  if f.exists():rec[name]={'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'mtime_ns':f.stat().st_mtime_ns}
 records.append(rec);(out/'isolation-control.json').write_text(json.dumps(records,indent=2)+'\n');print(label,r.returncode,flush=True)
 if label!='audit-after-overwrite' and r.returncode!=0:break
print('Target',fresh,flush=True)
