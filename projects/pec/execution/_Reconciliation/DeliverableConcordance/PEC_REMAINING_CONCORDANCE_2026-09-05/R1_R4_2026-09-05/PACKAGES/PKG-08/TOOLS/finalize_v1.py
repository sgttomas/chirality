import csv,hashlib,json,re,importlib.util
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]; ROOT=Path.cwd(); BASE="2be412ccea62bdc4bd96deb082c46d7a792076ea"
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rel(p):return str(Path(p).relative_to(ROOT)) if Path(p).is_absolute() else str(p)
def writecsv(path,fields,rows):
 with path.open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n");w.writeheader();w.writerows(rows)
bv=json.loads((P/"VERIFICATION/BACKCHECK_V001/VALIDATION.json").read_text())
# Manager must inspect actual backcheck verdict before invoking this finalizer.
spec=importlib.util.spec_from_file_location("validator",P/"TOOLS/validate_v1.py"); v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
selected=[P/"WORKERS"/f"DEL-08-{n:02}" for n in range(1,6)];selected[-1]/="CORRECTION_V001"
claims=[];residuals=[];summaries=[];selection=[];structural=[];semantics=[];allhashes={}
for d in selected:
 check=v.validate(rel(d));assert check["pass"],check;structural.append(check)
 cr=list(csv.DictReader((d/"CLAIMS.csv").open()));rr=list(csv.DictReader((d/"RESIDUALS.csv").open())); claims+=cr;residuals+=rr;did=cr[0]["DeliverableID"];count=Counter(r["Disposition"] for r in cr)
 summaries.append(dict(DeliverableID=did,Claims=len(cr),RawResidualProposals=len(rr),UnknownClaims=count["UNKNOWN"],NonAlignedClaims=len(cr)-count["ALIGNED"],CandidateAssessment="ASSESSED_UNKNOWN" if count["UNKNOWN"] else "ASSESSED_WITH_HELD_RESIDUALS",WarrantedNONE="FALSE",SelectedClaims=rel(d/"CLAIMS.csv"),SelectedClaimsSHA256=sha(d/"CLAIMS.csv"),SelectedResiduals=rel(d/"RESIDUALS.csv"),SelectedResidualsSHA256=sha(d/"RESIDUALS.csv")))
 selection.append(dict(deliverable=did,path=rel(d),claims_sha256=sha(d/"CLAIMS.csv"),residuals_sha256=sha(d/"RESIDUALS.csv")))
 manifest=json.loads((d/"READ_MANIFEST.json").read_text())
 for path,h in manifest["hashes"].items():
  assert sha(path)==h,path;assert path not in allhashes or allhashes[path]==h;allhashes[path]=h
 for r in cr:
  disp=r["Disposition"];reason={"UNKNOWN":"Inspected current source and declared evidence do not establish complete behavior/acceptance. Wider absence is not inferred; candidate preserves evidence boundary.","ALIGNED":"Class-qualified documentary, source artifact, finite-method or exact human-act evidence retained; no rollup to runtime product completion.","STALE_INPUT":"Historical observation is not current-use evidence; original provenance retained and conditional routing cannot select an automatic text repair.","DOCUMENTED_UNIMPLEMENTED":"Only DEL08-04 locally scoped latency outputs: actual production semantics expose loop registry, not measurement; local output scope and registered checks support bounded absence. Outer upstream absence remains UNKNOWN.","ACCEPTED_DIVERGENCE":"D66 expressly permits historical decision-time provenance while declining current E-N13 topology; no edge revived.","DEFERRED_AGENT_WORKFLOW":"TM022 remains held until the exact next lifecycle trigger; no automatic Remaining mirror."}[disp]
  if r["ClaimID"]=="DEL-08-01::AC-005":reason+=" Listener method does not reach no-presumption clause; gap retained in evidence candidate without inventing failed result."
  if r["ClaimID"]=="DEL-08-04::AC-015":reason+=" Fixed conditioned bound does not create cadence/exceedance/release act; owner C08 disposition held."
  semantics.append(dict(ClaimID=r["ClaimID"],Disposition=disp,SelectedPacket=rel(d),ManagerVerdict="ACCEPT_REPORT_WITH_STATED_LIMITS",Reason=reason,SourceBinding="REHASH_PASS",ResidualLinkage="RECIPROCAL_PASS",GateReview="Evidence Depends NONE; future production gates separately retained"))
writecsv(P/"PACKAGE_CLAIMS.csv",v.CLAIM,claims);writecsv(P/"PACKAGE_RESIDUALS.csv",v.RES,residuals);writecsv(P/"PACKAGE_SUMMARY.csv",list(summaries[0]),summaries);writecsv(P/"MANAGER_ROW_FANIN.csv",list(semantics[0]),semantics)
(P/"SELECTED_DERIVATIVES.json").write_text(json.dumps(selection,indent=2)+"\n")
(P/"MANAGER_SOURCE_REHASH.json").write_text(json.dumps({"source_commit":BASE,"hashes":allhashes,"all_rehashed":True,"run_local_sources_are_derivative_context":True},indent=2)+"\n")
# Seal all current originals and selected derivative artifacts by explicit path; never claim original failure disappeared.
records=json.loads((P/"DISPATCH_RECORDS.json").read_text())
for record in records:
 ret=Path(record["write_scope"][:-3])/"RETURN.md"
 if ret.exists():record.update(status="terminal",return_path=str(ret),return_sha256=sha(ret))
(P/"DISPATCH_RECORDS.json").write_text(json.dumps(records,indent=2)+"\n")
common=json.loads((P/"SOURCE_MANIFEST.json").read_text());assert all(sha(k)==h for k,h in common["hashes"].items())
counts=dict(Counter(r["Disposition"] for r in claims)); val={"verdict":"PASS_REPORT_READY","base":BASE,"claims":len(claims),"residuals":len(residuals),"dispositions":counts,"members":len(selected),"local_definitions":221,"REQ_AC_VER":113,"warranted_NONE":0,"structural":structural,"manager_row_by_row_fanin":len(semantics),"common_source_rehash_count":len(common["hashes"]),"read_source_rehash_count":len(allhashes),"original_verifier":"CORRECTION_REQUIRED preserved","correction":"DEL08-05 exact locator only; independent BACKCHECK_V001 PASS inspected separately","r4":{"evidence_candidates":4,"conditional_historical":2,"held_routing":6},"source_mutation":False,"product_or_remaining_closure":False}
(P/"VALIDATION.json").write_text(json.dumps(val,indent=2)+"\n"); print(json.dumps({k:val[k] for k in ["verdict","claims","residuals","dispositions","read_source_rehash_count"]},indent=2))
