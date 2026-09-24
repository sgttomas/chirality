#!/usr/bin/env python3
"""Run-specific ordinary desktop build with unchanged existing WASM assets."""
from pathlib import Path
import hashlib,json,subprocess,time
root=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip()); project=root/"projects/chirality-piping"; app=project/"apps/desktop"; records=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
identity=json.loads((records/"browser-environment.json").read_text())
for p,h in identity["assets"].items(): assert sha(root/p)==h, p
for port in [5174,5175]:
 probe=subprocess.run(["lsof","-nP",f"-iTCP:{port}","-sTCP:LISTEN"],capture_output=True,text=True)
 assert probe.returncode==1 and not probe.stdout,probe.stdout
inputs=[p for p in (app/"src").rglob("*") if p.is_file()]+[app/p for p in ["package.json","tsconfig.json","vite.config.ts"]]+[project/"package-lock.json"]
meta={"head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"command":["npm","run","build","--workspace","apps/desktop"],"cwd":str(project),"inputs":{str(p.relative_to(root)):sha(p) for p in inputs},"existing_assets":identity["assets"]}
(records/"production-build-02-command.json").write_text(json.dumps(meta,indent=2)+"\n")
start=time.time()
with (records/"production-build-02.log").open("w") as log:
 log.write("$ npm run build --workspace apps/desktop\n");log.flush();run=subprocess.run(meta["command"],cwd=project,stdout=log,stderr=subprocess.STDOUT);log.write(f"\nexit={run.returncode}\nelapsed_seconds={time.time()-start:.3f}\n")
assert all(sha(root/p)==h for p,h in meta["inputs"].items()),"Source changed during build"
assert all(sha(root/p)==h for p,h in meta["existing_assets"].items()),"WASM assets changed"
result={"exit":run.returncode,"head":meta["head"],"dist":{str(p.relative_to(root)):sha(p) for p in (app/"dist").rglob("*") if p.is_file()}};(records/"production-build-02-result.json").write_text(json.dumps(result,indent=2)+"\n")
print((records/"production-build-02.log").read_text());raise SystemExit(run.returncode)
