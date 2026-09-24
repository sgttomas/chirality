from pathlib import Path
import subprocess,hashlib,json,sys
root=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip()); records=Path(__file__).resolve().parent;app=root/"projects/chirality-piping/apps/desktop";source=app/"src/features/viewport/labelProjection.ts";temporary=app/"e2e/c4-startup-observation.spec.ts";old=source.read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest();proposal=json.loads((records/"startup-observation-proposal.json").read_text());assert sha(old)==proposal["base_product_sha256"];assert not temporary.exists();instrumented=(records/"startup-observation-proposed-projector.ts").read_bytes();assert sha(instrumented)==proposal["proposed_product_sha256"];spec=(records/"startup-observation-proposed-spec.ts").read_bytes();assert spec.startswith((app/"e2e/ui-foundation.spec.ts").read_bytes());meta={"head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"original_source_sha256":sha(old),"instrumented_source_sha256":sha(instrumented),"test_sha256":sha(spec),"purpose":"Uncalibrated defect attribution only; unchanged maintained test bodies/assertions/deadlines"};code=None
try:
 source.write_bytes(instrumented);temporary.write_bytes(spec)
 (records/"startup-observation-19-bindings.json").write_text(json.dumps(meta,indent=2)+"\n")
 code=subprocess.run([sys.executable,str(records/"run_browser.py"),"source-startup-observation-19","source","e2e/c4-startup-observation.spec.ts","--project","chromium-desktop","--grep","Project pointer click followed by Shift-node"],cwd=root).returncode
finally:
 source.write_bytes(old);temporary.unlink(missing_ok=True);meta.update({"exit":code,"source_restored":source.read_bytes()==old,"temporary_spec_removed":not temporary.exists()});(records/"startup-observation-19-restoration.json").write_text(json.dumps(meta,indent=2)+"\n")
raise SystemExit(code)
