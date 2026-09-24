#!/usr/bin/env python3
from pathlib import Path
import subprocess,hashlib,json
root=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip());app=root/"projects/chirality-piping/apps/desktop"; records=Path(__file__).resolve().parent
source=app/"src/features/viewport/labelProjection.ts";test=source.with_name("labelProjection.test.ts");new=source.read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest();old=subprocess.check_output(["git","show","383c941e902bac866bd8e09f468c258894e4dabe:projects/chirality-piping/apps/desktop/src/features/viewport/labelProjection.ts"])
meta={"head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"old_source_sha256":sha(old),"repaired_source_sha256":sha(new),"test_sha256":sha(test.read_bytes()),"commands":[]}
def run(name,command):
 p=records/(name+".log");assert not p.exists(),"Preserve earlier attempt, choose a new name"
 with p.open("w") as log:
  log.write("$ "+" ".join(command)+"\n");log.flush();r=subprocess.run(command,cwd=app,stdout=log,stderr=subprocess.STDOUT);log.write("\nexit="+str(r.returncode)+"\n")
 meta["commands"].append({"name":name,"command":command,"exit":r.returncode});return r.returncode
try:
 source.write_bytes(old)
 red=run("projection-causal-red-02",["../../node_modules/.bin/vitest","run","src/features/viewport/labelProjection.test.ts","-t","P-100","--maxWorkers=1"])
finally:source.write_bytes(new)
assert source.read_bytes()==new
meta["exact_repaired_source_restored"]=True
code=run("projection-tsc-02",["../../node_modules/.bin/tsc","--noEmit"])
if code==0:
 code=run("projection-focused-02",["../../node_modules/.bin/vitest","run",*["src/features/viewport/"+x for x in ["labelProjection.test.ts","labelPlacement.test.ts","labelCollisionIndex.test.ts","labelPolicy.test.ts","PipeViewport.contextLabels.test.tsx","PipeViewport.labels.test.tsx","viewportResource.test.ts"]],"--maxWorkers=1"])
meta["source_unchanged_during_repaired_checks"]=source.read_bytes()==new and sha(test.read_bytes())==meta["test_sha256"]
(records/"projection-validation-02.json").write_text(json.dumps(meta,indent=2)+"\n");print(json.dumps(meta,indent=2));raise SystemExit(code)
