from pathlib import Path
import subprocess,json,hashlib,os,sys
r=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip());raw=Path(__file__).resolve().parent
project=sys.argv[1]
if project not in {"chromium-desktop","chromium-compact"}:raise SystemExit("Unknown project")
out=raw/"FINAL_CHECKS_R4_SERIAL"/project;out.mkdir(parents=True,exist_ok=False)
f=json.loads((raw/"COMBINED_FREEZE_R4.json").read_text());assets=json.loads((raw/"FINAL_CHECKS_R3/wasm-build-result.json").read_text())["after_assets"]
for x in f["files"]:
 if hashlib.sha256((r/x["path"]).read_bytes()).hexdigest()!=x["sha256"]:raise SystemExit("Frozen source changed: "+x["path"])
for x in assets:
 if hashlib.sha256(Path(x["path"]).read_bytes()).hexdigest()!=x["sha256"]:raise SystemExit("Built asset changed: "+x["path"])
port=subprocess.run(["lsof","-nP","-iTCP:5174","-iTCP:5175","-sTCP:LISTEN"],capture_output=True,text=True);(out/"ports-before.txt").write_text(port.stdout+port.stderr)
if port.stdout.strip():raise SystemExit("Existing port owner")
cmd=["npx","playwright","test","e2e/b4-pipes.spec.ts","e2e/b4-table-editing.spec.ts","e2e/b4-sections.spec.ts","--project="+project,"--grep","B4 Pipes|B4 node coordinates apply|B4 Materials preserve mixed-unit|B4 Sections mixed-unit|B4 Sections enum explicit|B4 Sections moved review row","--workers=1","--max-failures=1","--reporter=list,json","--output="+str(out/"artifacts")]
env=os.environ.copy();env["CI"]="1";env["PLAYWRIGHT_WORKERS"]="1";env["PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH"]="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";env["PLAYWRIGHT_JSON_OUTPUT_FILE"]=str(out/"report.json")
desktop=r/"projects/chirality-piping/apps/desktop"
(out/"command.json").write_text(json.dumps({"cwd":str(desktop),"argv":cmd,"env":{k:env[k] for k in ["CI","PLAYWRIGHT_WORKERS","PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH","PLAYWRIGHT_JSON_OUTPUT_FILE"]},"actual_head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"frozen_sources":f["files"],"built_assets":assets,"expected_cases":12,"reason":"ROOT-authorized per-project one-worker recovery after project-transition teardown stall; assertions and timeouts unchanged"},indent=2)+"\n")
with (out/"run.log").open("w") as log:res=subprocess.run(cmd,cwd=desktop,env=env,stdout=log,stderr=subprocess.STDOUT)
(out/"result.json").write_text(json.dumps({"exit_code":res.returncode})+"\n")
port=subprocess.run(["lsof","-nP","-iTCP:5174","-iTCP:5175","-sTCP:LISTEN"],capture_output=True,text=True);(out/"ports-after.txt").write_text(port.stdout+port.stderr)
print(project,"exit",res.returncode,"ports_empty",not bool(port.stdout.strip()),flush=True);raise SystemExit(res.returncode)
