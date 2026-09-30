#!/usr/bin/env python3
"""Read-only comparison of the four response deliverable registers to DAG-011."""
import csv, hashlib, json, re, subprocess
from collections import Counter
from pathlib import Path
ROOT=Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
P=ROOT/"projects/chirality-piping"
E=P/"execution"
IDS=["DEL-04-01", "DEL-04-05", "DEL-04-07", "DEL-09-01"]
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p: list(csv.DictReader(p.open()))
dp=E/"_DAG/DAG-011/DependencyEdges.csv"
drows=read(dp)
result={"kind":"focused_B0_comparison", "head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(), "graph":"DAG-011", "dag_sha256":sha(dp), "expected_currency_directory_exists":(E/"_Evaluation/DAGCurrency").exists(), "deliverables":[], "limits":"Structural register agreement and exact preserved binding checks only. No dependency satisfaction, deliverable readiness or fresh source-owner/consumer acceptance is established."}
for ident in IDS:
    d=next(E.glob("PKG-*/1_Working/"+ident+"_*"))
    lp=d/"Dependencies.csv"; rows=read(lp)
    a={r["DependencyID"]:r for r in rows}
    b={r["DependencyID"]:r for r in drows if r["FromDeliverableID"]==ident}
    common=set(a)&set(b); diffs=[]; notes=[]; extensions=[]
    for key in sorted(common):
        for field in sorted(set(a[key])|set(b[key])):
            av=a[key].get(field,"");bv=b[key].get(field,"")
            if av==bv: continue
            change={"id":key,"field":field,"local":av,"dag":bv}
            if field=="Notes" and bv.startswith(av): notes.append(change)
            elif field in {"EstimateImpactClass","ConsumerHint"} and field not in a[key]: extensions.append(change)
            else: diffs.append(change)
    active=[r for r in rows if r["DependencyClass"]=="EXECUTION" and r["Status"]=="ACTIVE"]
    result["deliverables"].append({"id":ident,"path":str(d.relative_to(ROOT)),"rows":len(rows),"dag_rows":len(b),"duplicate_local_ids":len(rows)-len(a),"duplicate_dag_ids":sum(r["FromDeliverableID"]==ident for r in drows)-len(b),"only_local":sorted(set(a)-set(b)),"only_dag":sorted(set(b)-set(a)),"core_differences":diffs,"dag_notes_extend_local_notes":notes,"nonempty_extension_fields_absent_locally":extensions,"active_execution_satisfaction":dict(Counter(r["SatisfactionStatus"] for r in active)),"unresolved_execution":[{k:r[k] for k in ["DependencyID","TargetDeliverableID","RequiredMaturity","ProposedMaturity","SatisfactionStatus"]} for r in active if r["SatisfactionStatus"]!="SATISFIED"],"input_hashes":[{"path":str((d/n).relative_to(ROOT)),"sha256":sha(d/n)} for n in ["Dependencies.csv","_DEPENDENCIES.md","ScopeOfWork.md","_CONTEXT.md"]]})
bp=E/"_ScopeChange/_PostAcceptanceValidation/SCA-011_20260922T173404Z/dependencies/CURRENT_SOURCE_BINDINGS.json"
bind=json.loads(bp.read_text())
result["accepted_binding_source"]={"path":str(bp.relative_to(ROOT)),"sha256":sha(bp)}
result["accepted_file_bindings_checked"]=[]
for entry in bind["source_files"]:
    if any(ident in entry["path"] for ident in IDS) or entry["path"].endswith("_Decomposition/SOFTWARE_DECOMP.md"):
        path=ROOT/entry["path"]
        got=sha(path) if path.exists() else None
        result["accepted_file_bindings_checked"].append({"path":entry["path"],"expected":entry["accepted_sha256"],"actual":got,"matches":got==entry["accepted_sha256"]})
result["accepted_DEL0407_quotes_checked"]=[]
for entry in bind["row_bindings"]:
    if entry["DependencyID"].startswith("DEP-04-07-"):
        path=P/entry["EvidenceFile"]
        body=path.read_text()
        locus=entry["SourceRef"].split(" # ",1)[1]
        if locus.startswith("frontmatter/"):
            section=body.split("---",2)[1]
        else:
            match=re.search(r"^### "+re.escape(locus)+r"[^\n]*\n(.*?)(?=^### |^## |\Z)",body,re.M|re.S)
            section=match.group(1) if match else ""
        result["accepted_DEL0407_quotes_checked"].append({"id":entry["DependencyID"],"path":str(path.relative_to(ROOT)),"hash_matches":sha(path)==entry["accepted_source_sha256"],"verbatim_quote_present":entry["EvidenceQuote"] in body,"named_locus":locus,"quote_in_named_locus":entry["EvidenceQuote"] in section,"scope":"fresh current-byte literal quote and named-locus check; historical whole-source hash drift remains disclosed"})
result["focused_register_comparison"]="NO_STRUCTURAL_DEPARTURE_FOUND" if all(not d[k] for d in result["deliverables"] for k in ["duplicate_local_ids","duplicate_dag_ids","only_local","only_dag","core_differences","nonempty_extension_fields_absent_locally"]) else "REVIEW_DEPARTURE"
print(json.dumps(result,indent=2))
