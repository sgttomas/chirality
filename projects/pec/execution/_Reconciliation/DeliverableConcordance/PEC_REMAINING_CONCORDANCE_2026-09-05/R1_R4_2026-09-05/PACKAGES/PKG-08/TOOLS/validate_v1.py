"""Frozen manager aggregate structural checker v1; no worker authoring support."""
import csv, hashlib, json, re, sys
from pathlib import Path
BASE="2be412ccea62bdc4bd96deb082c46d7a792076ea"
CLAIM="ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes".split(",")
RES="ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes".split(",")
def validate(d):
    d=Path(d); errors=[]; tables=[]
    for name,fields in [("CLAIMS.csv",CLAIM),("RESIDUALS.csv",RES)]:
        p=d/name; b=p.read_bytes(); reader=csv.DictReader(b.decode().splitlines()); rows=list(reader); tables.append(rows)
        if reader.fieldnames!=fields: errors.append(name+" schema")
        if b"\r" in b: errors.append(name+" CR bytes")
        for i,row in enumerate(rows):
            if not row.get("Depends"): errors.append(name+f" row {i} empty Depends")
            if not re.search(r"\(gated:|\(stage-gated:|NOT_SELECTABLE_UNTIL:",row.get("ExactGate", "")): errors.append(name+f" row {i} gate")
    claims,res=tables; ci={r["ClaimID"]:r for r in claims}; ri={r["ResidualID"]:r for r in res}
    if len(ci)!=len(claims) or len(ri)!=len(res): errors.append("duplicate IDs")
    for r in claims:
        if r["SourceCommit"]!=BASE or not r["SourceHashes"]: errors.append(r["ClaimID"]+" source binding")
        for rid in filter(None,re.split(r"[;|]",r["ProposedResidualID"])):
            if rid in ("NONE","N/A"): continue
            if rid not in ri or r["ClaimID"] not in ri[rid]["ClaimIDs"]: errors.append(r["ClaimID"]+" backlink "+rid)
    for i,r in enumerate(res,1):
        if r["ResidualID"]!=r["DeliverableID"]+f"-REM-{i:03}": errors.append(r["ResidualID"]+" sequence")
        if r["Selectability"]!="NON_SELECTABLE_PENDING_OWNER_APPLICATION": errors.append(r["ResidualID"]+" selectability")
        for cid in re.split(r"[;|]",r["ClaimIDs"]):
            if cid not in ci or r["ResidualID"] not in ci[cid]["ProposedResidualID"]: errors.append(r["ResidualID"]+" reciprocity "+cid)
    m=json.loads((d/"READ_MANIFEST.json").read_text())
    if m.get("source_commit")!=BASE or m.get("source_unchanged") is not True: errors.append("manifest source")
    for p,h in m["hashes"].items():
        if not Path(p).is_file() or hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h: errors.append("hash "+p)
    return {"directory":str(d),"claims":len(claims),"residuals":len(res),"errors":errors,"pass":not errors}
if __name__=="__main__":
    results=[validate(p) for p in sys.argv[1:]]; print(json.dumps(results,indent=2)); sys.exit(any(not r["pass"] for r in results))
