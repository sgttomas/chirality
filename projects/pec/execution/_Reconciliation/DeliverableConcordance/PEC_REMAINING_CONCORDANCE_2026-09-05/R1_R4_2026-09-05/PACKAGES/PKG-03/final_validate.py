from pathlib import Path
import json,hashlib,re,csv,subprocess
P=Path(__file__).resolve().parent.relative_to(Path.cwd());errors=[];checks=[]
def hashcheck(path,digest,kind):
 if path.is_absolute():errors.append(kind+" absolute "+str(path));return
 if ".." in path.parts:errors.append(kind+" traversal "+str(path));return
 if not path.is_file():errors.append(kind+" missing "+str(path));return
 if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:errors.append(kind+" drift "+str(path))
common=P.parent.parent/"COMMON/SOURCE_MANIFEST.json";m=json.loads(common.read_text())
for p,h in m["hashes"].items():hashcheck(Path(p),h,"common source")
checks.append({"kind":"common frozen rehash","count":len(m["hashes"])})
for f in sorted((P/"ORIGINAL_SEALS").glob("*.json")):
 m=json.loads(f.read_text())
 if "hashes" not in m:continue
 for p,h in m["hashes"].items():hashcheck(Path(p),h,"original seal")
 checks.append({"kind":"immutable seal","manifest":str(f),"count":len(m["hashes"])})
for f in sorted(P.rglob("READ_MANIFEST.json")):
 m=json.loads(f.read_text())
 for p,h in m["hashes"].items():hashcheck(Path(p),h,"read manifest")
 if not m.get("source_unchanged") or m.get("source_commit")!="2be412ccea62bdc4bd96deb082c46d7a792076ea":errors.append("source state "+str(f))
 checks.append({"kind":"read manifest","manifest":str(f),"count":len(m["hashes"])})
for f in sorted(P.rglob("OUTPUT_MANIFEST.json")):
 if f==P/"OUTPUT_MANIFEST.json":continue
 m=json.loads(f.read_text());d=m.get("hashes",m.get("files",m));count=0
 if isinstance(d,dict):
  for k,h in d.items():
   if isinstance(h,str) and re.fullmatch("[a-f0-9]{64}",h):
    pp=Path(k);pp=pp if pp.is_file() else f.parent/pp
    if pp==f:errors.append("self inclusion "+str(f))
    hashcheck(pp,h,"output manifest");count+=1
 checks.append({"kind":"output manifest","manifest":str(f),"count":count})
for f in P.rglob("*.csv"):
 if b"\r" in f.read_bytes():errors.append("non-LF "+str(f))
for f in P.rglob("*"):
 if f.is_symlink():errors.append("symlink "+str(f))
 if f.suffix==".pyc" or f.name=="__pycache__":errors.append("cache "+str(f))
selected=json.loads((P/"SELECTED_WORKERS.json").read_text())["selected"]
for did,w in selected.items():
 pp=Path(w)
 if not pp.is_relative_to(P/"WORKERS"/did):errors.append("selection containment "+w)
agg=json.loads((P/"AGGREGATE_VALIDATION.json").read_text());assert agg["pass"]
result={"pass":not errors,"errors":errors,"checks":checks,"aggregate":agg,"closure_meaning":"report readiness only; all6 ASSESSED_UNKNOWN; no production/Remaining/lifecycle closure","role_evidence":"delegated-harness-native instruction-asserted; not mechanically enforced","source_commit":"2be412ccea62bdc4bd96deb082c46d7a792076ea"}
(P/"VALIDATION.json").write_text(json.dumps(result,indent=2)+"\n");print(json.dumps({"pass":not errors,"errors":errors,"checks":len(checks)},indent=2))
raise SystemExit(0 if not errors else 1)
