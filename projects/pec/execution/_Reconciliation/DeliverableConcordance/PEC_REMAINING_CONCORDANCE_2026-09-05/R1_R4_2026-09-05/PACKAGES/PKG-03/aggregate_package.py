from pathlib import Path
import csv,json,hashlib,collections,importlib.util
P=Path(__file__).parent
spec=importlib.util.spec_from_file_location("v",P/"validate_worker.py");v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
selected=json.loads((P/"SELECTED_WORKERS.json").read_text())["selected"]
claims=[];residuals=[];summaries=[];checks=[]
for did,wstr in selected.items():
 w=Path(wstr);check=v.validate(w);checks.append(check);assert check["pass"],check
 cs=list(csv.DictReader((w/"CLAIMS.csv").open()));rs=list(csv.DictReader((w/"RESIDUALS.csv").open()));claims+=cs;residuals+=rs
 counts=collections.Counter(c["Disposition"] for c in cs)
 summaries.append({"DeliverableID":did,"ClaimCount":len(cs),"ResidualCount":len(rs),"AlignedCount":counts["ALIGNED"],"UnknownCount":counts["UNKNOWN"],"StaleInputCount":counts["STALE_INPUT"],"Assessment":"ASSESSED_UNKNOWN" if counts["UNKNOWN"] else "ASSESSED_RESIDUALS" if rs else "ASSESSED_ALIGNED","WarrantedNONE":"NO" if counts["UNKNOWN"] or rs else "REQUIRES_VERIFIER","SelectedWorker":wstr,"ClaimsSHA256":hashlib.sha256((w/"CLAIMS.csv").read_bytes()).hexdigest(),"ResidualsSHA256":hashlib.sha256((w/"RESIDUALS.csv").read_bytes()).hexdigest()})
def write(name,rows,header):
 with (P/name).open("w",newline="") as f:
  wr=csv.DictWriter(f,fieldnames=header,lineterminator="\n");wr.writeheader();wr.writerows(rows)
write("PACKAGE_CLAIMS.csv",claims,v.CLAIM);write("PACKAGE_RESIDUALS.csv",residuals,v.RES);write("PACKAGE_SUMMARY.csv",summaries,list(summaries[0]))
source_census=json.loads((P/"SOURCE_CLAIM_CENSUS.json").read_text());coverage=[]
for entry in source_census:
 did=entry["deliverable_id"];actual={c["ClaimID"] for c in claims if c["DeliverableID"]==did};missing=[x for x in entry["bullet_definition_ids"] if did+"::"+x not in actual];coverage.append({"deliverable":did,"defined_local_ids":len(entry["bullet_definition_ids"]),"missing":missing});assert not missing,coverage[-1]
assert len(set(c["ClaimID"] for c in claims))==len(claims)
assert len(set(r["ResidualID"] for r in residuals))==len(residuals)
(P/"AGGREGATE_VALIDATION.json").write_text(json.dumps({"pass":True,"claim_count":len(claims),"residual_count":len(residuals),"deliverable_count":len(summaries),"dispositions":dict(collections.Counter(c["Disposition"] for c in claims)),"worker_checks":checks,"source_definition_coverage":coverage,"summaries_reproduced":True},indent=2)+"\n")
print((P/"AGGREGATE_VALIDATION.json").read_text())
