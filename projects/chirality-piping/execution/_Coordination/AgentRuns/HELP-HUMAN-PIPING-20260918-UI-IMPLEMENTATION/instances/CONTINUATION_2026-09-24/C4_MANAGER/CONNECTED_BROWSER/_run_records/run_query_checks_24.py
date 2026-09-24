from pathlib import Path
import subprocess,hashlib,json,datetime
root=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip());app=root/"projects/chirality-piping/apps/desktop";records=Path(__file__).resolve().parent;source=app/"src/features/viewport/labelCollisionIndex.ts";test=source.with_name("labelCollisionIndex.test.ts");new=source.read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest();assert sha(new)=="b6d4eb2ff2de41e6d458f58db5a943b91532c6682ce05f15d77542002d0cad73";assert sha(test.read_bytes())=="af378ece75cac36b5535da5bb327b87e25b93a0301e67e7aa2b10e0ee14f4fa8";old=subprocess.check_output(["git","show","ab2561246c9f2983914402f413f0add97eb54bab:projects/chirality-piping/apps/desktop/src/features/viewport/labelCollisionIndex.ts"]);meta={"started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"old_source_sha256":sha(old),"candidate_source_sha256":sha(new),"test_sha256":sha(test.read_bytes()),"claim":"Shared semantic tests should pass old/new; this is not a timing/performance or old-red test","commands":[]}
def run(name,command):
 p=records/(name+".log");assert not p.exists()
 with p.open("w") as log:
  log.write("$ "+" ".join(command)+"\n");log.flush();r=subprocess.run(command,cwd=app,stdout=log,stderr=subprocess.STDOUT);log.write("\nexit="+str(r.returncode)+"\n")
 meta["commands"].append({"name":name,"command":command,"exit":r.returncode});return r.returncode
try:
 source.write_bytes(old);old_code=run("query-old-semantic-24",["../../node_modules/.bin/vitest","run","src/features/viewport/labelCollisionIndex.test.ts","--maxWorkers=1"])
finally:source.write_bytes(new)
code=run("query-tsc-24",["../../node_modules/.bin/tsc","--noEmit"])
if code==0:code=run("query-focused-24",["../../node_modules/.bin/vitest","run",*["src/features/viewport/"+x for x in ["labelCollisionIndex.test.ts","labelPlacement.test.ts","labelPolicy.test.ts","labelProjection.test.ts","PipeViewport.contextLabels.test.tsx","PipeViewport.labels.test.tsx","viewportResource.test.ts"]],"--maxWorkers=1"])
meta.update({"old_semantic_exit":old_code,"ended_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"candidate_restored_and_unchanged":source.read_bytes()==new and sha(test.read_bytes())==meta["test_sha256"]});(records/"query-validation-24.json").write_text(json.dumps(meta,indent=2)+"\n");print(json.dumps(meta,indent=2));raise SystemExit(code or old_code)
