from pathlib import Path
import subprocess,hashlib,json,sys,difflib
root=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip());records=Path(__file__).resolve().parent;app=root/"projects/chirality-piping/apps/desktop";temporary=app/"e2e/c4-startup-observation.spec.ts";sha=lambda b:hashlib.sha256(b).hexdigest();pairs={app/"src/features/viewport/labelProjection.ts":records/"startup-observation-proposed-projector.ts",app/"src/features/viewport/labelPolicy.ts":records/"startup-policy-observation-20-tested-policy.ts"};originals={p:p.read_bytes() for p in pairs};assert not temporary.exists()
for p,data in originals.items():assert data==subprocess.check_output(["git","show","158bd7f971744a91cb70563335518353a505debd:"+str(p.relative_to(root))])
spec=(records/"startup-policy-observation-20-tested-spec.ts").read_bytes();assert spec.startswith((app/"e2e/ui-foundation.spec.ts").read_bytes());meta={"head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"scope":"Temporary aggregate policy-stage and projector observation; uncalibrated diagnosis only","source":{str(p.relative_to(root)):{"original_sha256":sha(originals[p]),"tested_sha256":sha(instrument.read_bytes())} for p,instrument in pairs.items()},"test_sha256":sha(spec)};code=None
try:
 for p,instrument in pairs.items():p.write_bytes(instrument.read_bytes())
 temporary.write_bytes(spec);(records/"startup-policy-observation-20-bindings.json").write_text(json.dumps(meta,indent=2)+"\n")
 code=subprocess.run([sys.executable,str(records/"run_browser.py"),"source-startup-policy-observation-20","source","e2e/c4-startup-observation.spec.ts","--project","chromium-desktop","--grep","Project pointer click followed by Shift-node"],cwd=root).returncode
finally:
 for p,data in originals.items():p.write_bytes(data)
 temporary.unlink(missing_ok=True);meta.update({"exit":code,"restored":{str(p.relative_to(root)):sha(p.read_bytes())==sha(data) for p,data in originals.items()},"temporary_spec_removed":not temporary.exists()});(records/"startup-policy-observation-20-restoration.json").write_text(json.dumps(meta,indent=2)+"\n")
raise SystemExit(code)
