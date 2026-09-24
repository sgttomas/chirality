from pathlib import Path
import subprocess,json,hashlib,os,sys
r=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
raw=Path(__file__).resolve().parent
out=raw/"FINAL_CHECKS_R4"
case=sys.argv[1] if len(sys.argv)>1 else "browser"
if case not in {"browser","browser-retry"}:raise SystemExit("Unknown retained run name")
f=json.loads((raw/"COMBINED_FREEZE_R4.json").read_text())
for x in f["files"]:
 if hashlib.sha256((r/x["path"]).read_bytes()).hexdigest()!=x["sha256"]:raise SystemExit("Frozen source changed: "+x["path"])
port=subprocess.run(["lsof","-nP","-iTCP:5174","-iTCP:5175","-sTCP:LISTEN"],capture_output=True,text=True)
(out/(case+"-ports-before.txt")).write_text(port.stdout+port.stderr)
if port.stdout.strip():raise SystemExit("Existing port owner; not starting")
cmd=["npx","playwright","test","e2e/b4-pipes.spec.ts","e2e/b4-table-editing.spec.ts","e2e/b4-sections.spec.ts","--grep","B4 Pipes|B4 node coordinates apply|B4 Materials preserve mixed-unit|B4 Sections mixed-unit|B4 Sections enum explicit|B4 Sections moved review row","--workers=2","--max-failures=1","--output="+str(out/(case+"-artifacts"))]
env=os.environ.copy();env["CI"]="1";env["PLAYWRIGHT_WORKERS"]="2";env["PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH"]="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
desktop=r/"projects/chirality-piping/apps/desktop"
(out/(case+"-command.json")).write_text(json.dumps({"cwd":str(desktop),"argv":cmd,"env":{k:env[k] for k in ["CI","PLAYWRIGHT_WORKERS","PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH"]},"frozen_sources":f["files"],"expected_scenarios":12,"expected_project_executions":24},indent=2)+"\n")
with (out/(case+".log")).open("w") as log:res=subprocess.run(cmd,cwd=desktop,env=env,stdout=log,stderr=subprocess.STDOUT)
(out/(case+"-result.json")).write_text(json.dumps({"exit_code":res.returncode})+"\n")
port=subprocess.run(["lsof","-nP","-iTCP:5174","-iTCP:5175","-sTCP:LISTEN"],capture_output=True,text=True)
(out/(case+"-ports-after.txt")).write_text(port.stdout+port.stderr)
print(case,"exit",res.returncode,"ports_empty",not bool(port.stdout.strip()),flush=True)
raise SystemExit(res.returncode)
