from pathlib import Path
import csv,json,hashlib,re
P=Path(__file__).parent
C="ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes".split(",")
R="ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes".split(",")
def read(p,s):
 assert b"\r" not in p.read_bytes(),p
 with p.open() as f:
  d=csv.DictReader(f); assert d.fieldnames==s,(p,d.fieldnames); return list(d)
def write(p,s,rows):
 with p.open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=s,lineterminator="\n");w.writeheader();w.writerows(rows)
claims=[];residuals=[];summary=[];manifest={};seen=set();checks=[]
for n in range(1,8):
 d=f"DEL-09-{n:02d}";w=P/"WORKERS"/d;c=read(w/"CLAIMS.csv",C);r=read(w/"RESIDUALS.csv",R)
 assert c and all(x["DeliverableID"]==d for x in c+r)
 ci={x["ClaimID"]:x for x in c};ri={x["ResidualID"]:x for x in r};assert len(ci)==len(c) and len(ri)==len(r)
 for x in c:
  assert x["ClaimID"].startswith(d+"::") and x["ClaimID"] not in seen;seen.add(x["ClaimID"])
  assert x["SourceCommit"]=="2be412ccea62bdc4bd96deb082c46d7a792076ea"
  assert x["Depends"] and any(t in x["ExactGate"] for t in ["NOT_SELECTABLE_UNTIL:","(gated:","(stage-gated:"])
  for rid in [v for v in x["ProposedResidualID"].split(";") if v and v!="NONE"]:
   assert rid in ri and x["ClaimID"] in ri[rid]["ClaimIDs"].split(";")
 for i,x in enumerate(r,1):
  assert x["ResidualID"]==f"{d}-REM-{i:03d}"
  assert x["Depends"]=="NONE" and x["Selectability"]=="NON_SELECTABLE_PENDING_OWNER_APPLICATION"
  assert any(t in x["ExactGate"] for t in ["NOT_SELECTABLE_UNTIL:","(gated:","(stage-gated:"])
  for cid in x["ClaimIDs"].split(";"):assert cid in ci and x["ResidualID"] in ci[cid]["ProposedResidualID"].split(";")
 m=json.loads((w/"READ_MANIFEST.json").read_text());assert m["source_unchanged"]
 for src,h in m["hashes"].items():
  assert hashlib.sha256(Path(src).read_bytes()).hexdigest()==h,src
  if src in manifest:assert manifest[src]==h
  manifest[src]=h
 unknown=sum(x["Disposition"]=="UNKNOWN" for x in c)
 summary.append(dict(DeliverableID=d,ClaimCount=len(c),AlignedCount=sum(x["Disposition"]=="ALIGNED" for x in c),UnknownCount=unknown,ResidualCount=len(r),Assessment="ASSESSED_UNKNOWN" if unknown else "ASSESSED",WarrantedNONE="NO",SelectedWorker=str(w)))
 claims+=c;residuals+=r;checks.append({"deliverable":d,"schema_ids_reciprocity_hashes_lf":"PASS","read_hashes":len(m["hashes"])})
write(P/"PACKAGE_CLAIMS.csv",C,claims);write(P/"PACKAGE_RESIDUALS.csv",R,residuals);write(P/"PACKAGE_SUMMARY.csv",list(summary[0]),summary)
(P/"AGGREGATE_VALIDATION.json").write_text(json.dumps({"status":"PASS","claims":len(claims),"residuals":len(residuals),"members":7,"read_hashes":len(manifest),"checks":checks,"semantic_verification":"Separate fresh verifier and manager row-by-row fan-in required"},indent=2)+"\n")
print(json.dumps({"claims":len(claims),"residuals":len(residuals),"summary":summary},indent=2))
