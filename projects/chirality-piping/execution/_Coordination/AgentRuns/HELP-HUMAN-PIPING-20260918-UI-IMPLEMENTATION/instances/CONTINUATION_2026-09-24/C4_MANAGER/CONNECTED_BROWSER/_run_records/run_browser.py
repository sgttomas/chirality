#!/usr/bin/env python3
"""Run-specific wrapper around unchanged maintained Playwright configs."""
from pathlib import Path
import argparse, hashlib, json, os, re, subprocess, time
parser=argparse.ArgumentParser(); parser.add_argument("name"); parser.add_argument("lane", choices=["source","dist"]); parser.add_argument("arguments", nargs=argparse.REMAINDER); args=parser.parse_args()
assert re.fullmatch(r"[a-z0-9-]+", args.name)
root=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"], text=True).strip()); project=root/"projects/chirality-piping"; app=project/"apps/desktop"; records=Path(__file__).resolve().parent
identity=json.loads((records/"browser-environment.json").read_text()); browser=Path(identity["browser_path"])
assert hashlib.sha256(browser.read_bytes()).hexdigest()==identity["browser_sha256"]
port=5174 if args.lane=="source" else 5175
probe=subprocess.run(["lsof","-nP",f"-iTCP:{port}","-sTCP:LISTEN"],capture_output=True,text=True)
assert probe.returncode==1 and not probe.stdout, f"Port {port} occupied: {probe.stdout}"
output=records/args.name; output.mkdir(exist_ok=True)
command=[str(project/"node_modules/.bin/playwright"),"test"]
if args.lane=="dist": command += ["--config","playwright.dist.config.ts"]
command += args.arguments + ["--workers","1","--max-failures","1","--reporter=list,json","--output",str(output)]
env=dict(os.environ,CI="1",PLAYWRIGHT_WORKERS="1",PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=str(browser),PLAYWRIGHT_JSON_OUTPUT_FILE=str(records/(args.name+".json")))
inputs={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in app.glob("e2e/c4-label-policy*.ts")}
for value in args.arguments:
 p=app/value
 if p.is_file(): inputs[value]=hashlib.sha256(p.read_bytes()).hexdigest()
metadata={"head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"cwd":str(app),"port":port,"command":command,"browser":identity,"test_inputs":inputs}
start=time.time(); log=records/(args.name+".log")
with log.open("w") as stream:
 stream.write("$ "+" ".join(command)+"\n"); stream.flush()
 process=subprocess.Popen(command,cwd=app,env=env,stdout=stream,stderr=subprocess.STDOUT); metadata["pid"]=process.pid
 (records/(args.name+"-command.json")).write_text(json.dumps(metadata,indent=2)+"\n")
 code=process.wait(); stream.write(f"\nexit={code}\nelapsed_seconds={time.time()-start:.3f}\n")
post=subprocess.run(["lsof","-nP",f"-iTCP:{port}","-sTCP:LISTEN"],capture_output=True,text=True)
(records/(args.name+"-port-after.json")).write_text(json.dumps({"port":port,"exit":post.returncode,"stdout":post.stdout,"stderr":post.stderr},indent=2)+"\n")
print(log.read_text()[-20000:])
if post.returncode!=1 or post.stdout: raise SystemExit("Owned lane did not release port; inspect before any further launch.")
raise SystemExit(code)
