import csv,json,hashlib,re,sys
from pathlib import Path
CLAIM="ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes".split(",")
RES="ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes".split(",")
def validate(w):
 errors=[];cs=[];rs=[]
 for name,header in [("CLAIMS.csv",CLAIM),("RESIDUALS.csv",RES)]:
  p=w/name
  if not p.exists():errors.append(name+" missing");continue
  if b"\r" in p.read_bytes():errors.append(name+" non-LF")
  with p.open() as f:
   reader=csv.DictReader(f);rows=list(reader)
   if reader.fieldnames!=header:errors.append(name+" schema")
  if name=="CLAIMS.csv":cs=rows
  else:rs=rows
 cids=[c["ClaimID"] for c in cs];rids=[r["ResidualID"] for r in rs]
 if len(set(cids))!=len(cids):errors.append("duplicate claims")
 if len(set(rids))!=len(rids):errors.append("duplicate residuals")
 did=cs[0]["DeliverableID"] if cs else w.name
 expected=[f"{did}-REM-{i:03}" for i in range(1,len(rs)+1)]
 if sorted(rids)!=expected:errors.append("residual sequence")
 def ids(v,kind):return set(re.findall(r"DEL-\d{2}-\d{2}::[A-Za-z0-9_-]+" if kind=="claim" else r"DEL-\d{2}-\d{2}-REM-\d{3}",v))
 for c in cs:
  if not c["ClaimID"].startswith(did+"::"):errors.append("claim owner "+c["ClaimID"])
  if c["SourceCommit"]!="2be412ccea62bdc4bd96deb082c46d7a792076ea":errors.append("claim base "+c["ClaimID"])
  if not c["SourceHashes"]:errors.append("missing source hashes "+c["ClaimID"])
  for rid in ids(c["ProposedResidualID"],"residual"):
   match=[r for r in rs if r["ResidualID"]==rid]
   if not match or c["ClaimID"] not in ids(match[0]["ClaimIDs"],"claim"):errors.append("claim reciprocity "+c["ClaimID"])
 for r in rs:
  for cid in ids(r["ClaimIDs"],"claim"):
   match=[c for c in cs if c["ClaimID"]==cid]
   if not match or r["ResidualID"] not in ids(match[0]["ProposedResidualID"],"residual"):errors.append("residual reciprocity "+r["ResidualID"])
 for row in cs+rs:
  if not row["Depends"].strip():errors.append("blank Depends")
  if not any(x in row["ExactGate"] for x in ["(gated:","(stage-gated:","NOT_SELECTABLE_UNTIL:"]):errors.append("gate marker "+row.get("ClaimID",row.get("ResidualID","")))
  if row["Selectability"]!="NON_SELECTABLE_PENDING_OWNER_APPLICATION":errors.append("selectability")
 m=json.loads((w/"READ_MANIFEST.json").read_text())
 for p,h in m["hashes"].items():
  if Path(p).is_absolute() or not Path(p).is_file() or hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h:errors.append("hash/path "+p)
 if m["source_commit"]!="2be412ccea62bdc4bd96deb082c46d7a792076ea" or not m["source_unchanged"]:errors.append("manifest source")
 return {"worker":str(w),"claims":len(cs),"residuals":len(rs),"read_hashes":len(m["hashes"]),"errors":errors,"pass":not errors}
if __name__=="__main__":
 result=validate(Path(sys.argv[1]));print(json.dumps(result,indent=2));sys.exit(0 if result["pass"] else 1)
