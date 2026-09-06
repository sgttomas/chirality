from pathlib import Path
import subprocess,json,hashlib,datetime,os
repo=Path(__file__).resolve().parents[7]
# Derive canonical repository at execution, never assume fixed checkout.
repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
o=Path(__file__).resolve().parent;app=repo/'projects/chirality-app-dev';front=app/'frontend'
def run(name,args,cwd):
 at=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(args,cwd=cwd,capture_output=True,text=True)
 (o/(name+'.stdout')).write_text(p.stdout);(o/(name+'.stderr')).write_text(p.stderr)
 row={'command':args,'cwd':str(cwd.relative_to(repo)),'started':at,'finished':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'environment':'inherited; no command-specific overrides','stdout':name+'.stdout','stderr':name+'.stderr'}
 (o/(name+'.json')).write_text(json.dumps(row,indent=2)+'\n');print(name,p.returncode,flush=True);return p
p=run('sync-before-checks',['git','fetch','origin','main'],repo)
assert p.returncode==0
assert subprocess.run(['git','merge-base','--is-ancestor','origin/main','HEAD'],cwd=repo).returncode==0,'origin/main advanced; stop and route parent'
run('versions',['node','--version'],front)
run('npm-version',['npm','--version'],front)
checks=['frontend-typecheck','frontend-test','frontend-build','app-hold-integrity','harness-self-check','harness-pytest']
run('registered-check-runner',['python3','tools/software_workflow/run_registered_checks.py','projects/chirality-app-dev/software-workflow.json',*[a for c in checks for a in ['--check',c]],'--output',str(o/'REGISTERED_CHECKS.json'),'--timeout-seconds','600'],repo)
run('compiler-resolution',['node','node_modules/typescript/bin/tsc','-p','tsconfig.electron.json','--noEmit','--incremental','false','--traceResolution'],front)
assets={str(x.relative_to(repo)):hashlib.sha256(x.read_bytes()).hexdigest() for d in ['dist-electron','.next/static'] for x in (front/d).rglob('*') if x.is_file()}
(o/'BUILD_ASSETS_AFTER.json').write_text(json.dumps(assets,indent=2)+'\n')
before=json.loads((o/'BUILD_ASSETS_BEFORE.json').read_text());common=set(before)&set(assets)
(o/'BUILD_ASSET_COMPARISON.json').write_text(json.dumps({'before_count':len(before),'after_count':len(assets),'unchanged':[x for x in sorted(common) if before[x]==assets[x]],'changed':[x for x in sorted(common) if before[x]!=assets[x]],'added':sorted(set(assets)-set(before)),'removed':sorted(set(before)-set(assets))},indent=2)+'\n')
run('scoped-diff-check',['git','diff','--check','--','projects/chirality-app-dev/frontend/tsconfig.electron.json'],repo)

run('premerge-check-runner',['python3','tools/software_workflow/run_registered_checks.py','projects/chirality-app-dev/software-workflow.json','--check','frontend-premerge','--output',str(o/'PREMERGE_CHECK.json'),'--timeout-seconds','600'],repo)
