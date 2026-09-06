from pathlib import Path
import json,os,shutil,subprocess
root=Path(__file__).resolve().parents[5]
frontend=root/'frontend'
out=Path(__file__).resolve().parent/'release-quality-v5-host'
out.mkdir()
argv=['npm','run','validate:release-quality','--','--skip-premerge','Registered local premerge failed with session/list/create/boot HTTP503 and no configured runtime daemon binding; App AGENTS permits configured PR CI deferral. This is not a premerge PASS.']
assert (frontend/'package.json').exists(), frontend
result=subprocess.run(argv,cwd=frontend,text=True,capture_output=True)
(out/'stdout.log').write_text(result.stdout);(out/'stderr.log').write_text(result.stderr)
(out/'COMMAND.json').write_text(json.dumps({'argv':argv,'cwd':str(frontend),'exit_code':result.returncode,'host_escalation':'Registered fixture checks require loopback sockets','binding_environment_present':{k:bool(os.environ.get(k)) for k in ['CHIRALITY_RUNTIME_SOCKET_PATH','CHIRALITY_RUNTIME_TOKEN_FILE','CHIRALITY_RUNTIME_PROJECT_ID','CHIRALITY_RUNTIME_PROJECT_ROOT']}},indent=2)+'\n')
art=frontend/'artifacts/harness/release-quality/latest'
if art.exists():shutil.copytree(art,out/'artifacts')
print(json.dumps({'exit_code':result.returncode,'output':str(out)}))
raise SystemExit(result.returncode)
