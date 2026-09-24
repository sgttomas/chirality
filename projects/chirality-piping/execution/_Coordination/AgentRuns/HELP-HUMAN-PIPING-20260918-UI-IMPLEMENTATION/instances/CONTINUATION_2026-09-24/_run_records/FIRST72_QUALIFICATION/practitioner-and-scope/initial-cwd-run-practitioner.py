from pathlib import Path
import subprocess,json,datetime,os
out=Path(__file__).parent
root=Path('/private/tmp/piping-first-correctness-20260924')
p=root/'projects/chirality-piping'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()=='72f09c4b195b1cb9e6576eafa963997a1b289a01'
commands=[['/private/tmp/chirality-piping-dec025-venv/bin/python', 'tools/practitioner_harness/harness.py', 'self-check'], ['/private/tmp/chirality-piping-dec025-venv/bin/python', '-m', 'pytest', '-q', 'tools/practitioner_harness']]
records=[]
env=os.environ.copy();env['PATH']='/private/tmp/chirality-piping-dec025-venv/bin:'+env['PATH'];env.pop('CARGO_TARGET_DIR',None)
for i,cmd in enumerate(commands):
 rec={'candidate':'72f09c4b195b1cb9e6576eafa963997a1b289a01','argv':cmd,'cwd':str(p),'started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 with (out/f'profile-harness-{i}.log').open('w') as f:r=subprocess.run(cmd,cwd=p,env=env,stdout=f,stderr=subprocess.STDOUT)
 rec.update(finished=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=r.returncode,log=f'profile-harness-{i}.log');records.append(rec);(out/'profile-harness-results.json').write_text(json.dumps(records,indent=2)+'\n');print(i,r.returncode,flush=True)
 if r.returncode:raise SystemExit(r.returncode)
