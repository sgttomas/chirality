from pathlib import Path
import os, subprocess,json,datetime
root=Path('/private/tmp/piping-generated-loads-20260924');out=Path(__file__).parent
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
assert head=='3c17e267dd06ee561e8dc9984f6623126095eec1'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True)
py='/private/tmp/chirality-piping-dec025-venv/bin/python'
commands=[[py,'tools/practitioner_harness/harness.py','self-check'],[py,'-m','pytest','-q','tools/practitioner_harness'],[py,'tools/validation/validate_instruction_tranche_manifest.py','--base','origin/main','--head','HEAD','--added-manifests-only']]
records=[]
for n,cmd in enumerate(commands):
 r={'candidate':head,'argv':cmd,'cwd':str(root),'started':datetime.datetime.now(datetime.timezone.utc).isoformat(),'log':f'profile-{n}.log'}
 with (out/r['log']).open('w') as log: p=subprocess.run(cmd,cwd=root,stdout=log,stderr=subprocess.STDOUT)
 r.update(exit_code=p.returncode,finished=datetime.datetime.now(datetime.timezone.utc).isoformat());records.append(r)
 (out/'profile-results.json').write_text(json.dumps(records,indent=2)+'\n')
 print(json.dumps(r),flush=True)
 if p.returncode: raise SystemExit(p.returncode)
