import datetime,hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[10]
# Locate this checkout independent of nesting depth.
root=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
base=Path(__file__).resolve().parent
label=sys.argv[1]
args=sys.argv[2:]
cmd=["cargo","test","--manifest-path",str(root/"projects/chirality-piping/core/product_physics/Cargo.toml"),"--offline","--locked","-j","2","--target-dir",str(base/"target_product")]+args+["--","--test-threads=2","--nocapture"]
manifest=base.parent/"FREEZE_03/SOURCE_MANIFEST.json"
inputs=[root/item["path"] for item in json.loads(manifest.read_text())["paths"]]+[root/"projects/chirality-piping/core/product_physics/tests/pressure_membrane_range.rs",manifest,Path(__file__).resolve()]
for extra in [root/"projects/chirality-piping/core/product_physics/src/historical_pressure_reference.rs", base.parent/"TEST_DISPOSITION_REPAIR/SUCCESSOR_BINDING.json"]:
 if extra.exists(): inputs.append(extra)
def hashes(): return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
r={"actor":"/root/physics_resume","actual_harness_parent":"/root","command":cmd,"cwd":str(root),"started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"versions":{x:subprocess.check_output([x,"--version"],text=True).strip() for x in ["cargo","rustc"]},"inputs":hashes()}
with (base/(label+".log")).open("w") as f: result=subprocess.run(cmd,cwd=root,stdout=f,stderr=subprocess.STDOUT)
r.update(exit_code=result.returncode,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_inputs_unchanged=r["inputs"]==hashes(),log_sha256=hashlib.sha256((base/(label+".log")).read_bytes()).hexdigest())
(base/(label+"-execution.json")).write_text(json.dumps(r,indent=2)+"\n")
print(json.dumps({"label":label,"exit_code":result.returncode,"log":str(base/(label+".log"))}))
print("\n".join((base/(label+".log")).read_text().splitlines()[-32:]))
