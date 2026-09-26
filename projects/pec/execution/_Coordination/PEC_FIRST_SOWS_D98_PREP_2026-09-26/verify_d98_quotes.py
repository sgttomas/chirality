#!/usr/bin/env python3
"""Check that every verbatim source quotation in the two D-PEC-98 candidate
ScopeOfWork.md files is a substring of its cited source, in a repository tree.

Usage: verify_d98_quotes.py <repo_root> <candidate_dir_08> <candidate_dir_09>
Exit 0 when every check passes; 1 otherwise. Stdlib only; read-only.
"""
import csv, re, sys, unicodedata
from pathlib import Path

root = Path(sys.argv[1]); c08 = Path(sys.argv[2]) / "ScopeOfWork.md"; c09 = Path(sys.argv[3]) / "ScopeOfWork.md"
pec = root / "projects/pec"
dec = pec / "execution/_Decomposition"

def norm(s):
    s = re.sub(r"\s+", " ", s.replace("> ", " ").replace("\n>", " ")).strip()
    return s

def src(rel): return norm((root / rel).read_text(encoding="utf-8"))

def blockquote_after(text, marker):
    i = text.index(marker)
    lines = text[i:].splitlines()[1:]
    out = []
    started = False
    for l in lines:
        if l.startswith(">"):
            started = True; out.append(l[1:].strip())
        elif started:
            break
        elif l.strip() == "":
            continue
        else:
            break
    return " ".join(x for x in out if x)

checks = []
def check(name, needle, hay):
    n = norm(needle)
    ok = len(n) >= 12 and n in hay
    checks.append((ok, f"{name} [{len(n)} chars]"))

ledger_raw = (dec / "ScopeLedger.csv").read_text(encoding="utf-8")
deliv = {r["DeliverableID"]: r for r in csv.DictReader(open(dec / "Deliverables.csv", encoding="utf-8"))}
cbqa = {r["DeliverableID"]: r for r in csv.DictReader(open(dec / "ContextBudgetQA.csv", encoding="utf-8"))}
prd = src("projects/pec/docs/PRD.md")
decomp = src("projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md")
plan = src("projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md")
ia = src("projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Impact_Assessment.md")
tmpl = src("workflows/construct-local-work-graph/resources/work-graph-template.md")
wf = src("workflows/construct-local-work-graph/WORKFLOW.md")
memt = src("docs/templates/MEMORY_TEMPLATE.md")
agents = src("projects/pec/AGENTS.md")
dn = src("projects/pec/execution/_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md")
sow0101 = src("projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md")

for cand, sid, did in ((c08, "SOW-095", "DEL-02-08"), (c09, "SOW-096", "DEL-02-09")):
    t = cand.read_text(encoding="utf-8")
    tag = did
    # CLM-001 ledger row
    row = re.search(r"``(%s,IN,.*?)``" % sid, t).group(1)
    checks.append((row + "\n" in ledger_raw or row in ledger_raw.splitlines(), f"{tag} CLM-001 ledger row verbatim"))
    # description verbatim
    d = deliv[did]["Description"]
    checks.append((('"' + d + '"') in t.replace("\n", " ") or d in norm(t), f"{tag} CLM-005 register Description verbatim"))
    # objective statements
    check(f"{tag} OBJ-001 statement", "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation", decomp)
    check(f"{tag} OBJ-002 statement", "Staleness is detected structurally by SHA comparison, never by judgment", decomp)
    check(f"{tag} §3 mapping note", "Parser items (SOW-011..017, SOW-095, SOW-096) underlie OBJ-001/OBJ-002 through the record tier (SOW-001)", decomp)
    check(f"{tag} DL-20 entry quote", "SOW-095 and SOW-096 enter mapped to OBJ-001/OBJ-002", decomp)
    check(f"{tag} PEC-RCN-002 lead", "The reconciler shall ingest, per the closed, PEC-versioned feed profile declared on each loop-registry row (§16.3; PEC's reading hypothesis, never the loop's truth), at minimum:", prd)
    check(f"{tag} PKG-02 charter head", "Read-side grammars over governed files:", decomp)
    check(f"{tag} PKG-02 charter feeds", "Markdown work graphs, the MEMORY run index and `LOOP_INIT.md` identity as first-class feeds;", decomp)
    check(f"{tag} PKG-02 out of scope", "Writing anything; interpretation beyond declared grammars", decomp)
    check(f"{tag} §B4 carry-forward", blockquote_after(t, "records a carry-forward for the parser contracts:"), plan)
    check(f"{tag} §B7 fixture strategy", blockquote_after(t, "In their words:" if did == "DEL-02-08" else "In its words:").replace("(SCA-005 `Propagation_Plan.md` §B7.)", ""), plan)
    check(f"{tag} §B7 placement", "inside the DEL-02-08/09 and DEL-02-03 SOWs", plan)
    check(f"{tag} K-10 quote", "Paths, counts, SHAs, states, hashes — never file or diff content", prd)
    check(f"{tag} fourteen/RunRecord upstream", "exactly the fourteen record-tier entity types", sow0101)

t8 = c08.read_text(encoding="utf-8"); t9 = c09.read_text(encoding="utf-8")
check("08 RCN-002 work-graph clause", blockquote_after(t8, "its work-graph clause reads:"), prd)
check("08 §7.1 WorkGraph row", blockquote_after(t8, 'The §7.1 record-tier row "WorkGraph / WorkNode" states the entity\'s purpose:'), prd)
check("08 envelope notes", deliv["DEL-02-08"]["ContextEnvelopeNotes"], norm(t8))
check("08 CBQA action", cbqa["DEL-02-08"]["RecommendedAction"], norm(t8))
check("08 DEL-01-01 register 16 types", "16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows)", norm(deliv["DEL-01-01"]["Description"]))
check("08 DEL-02-05 description tail", "Markdown `WORK_GRAPH.md` belongs to DEL-02-08", norm(deliv["DEL-02-05"]["Description"]))
check("08 §8 envelope", "is M with MEDIUM risk", decomp)
check("08 §8 slice", "held as one parser slice", decomp)
check("08 template identity bullet", "Stable run identity: <ID used by the graph, deliverable MEMORY rows and PR>", tmpl)
check("08 template columns", "| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |", tmpl)
check("08 template states", "Use PLANNED, READY, ACTIVE, BLOCKED, UNCERTAIN and COMPLETE consistently. A node awaiting a human decision is BLOCKED and names that decision.", tmpl)
check("08 template current graph ref", "Current graph ref:", tmpl)
check("08 method authority clause", "changes no scope, hold, lifecycle or release authority by itself", wf)
check("08 design note authority class", "for undertaking execution state only", dn.replace("**", ""))
check("08 design note threshold", "a small length threshold", dn)
for q in ("receipt fields, Examined-Through ancestry, run ID = folder", "run ID ≠ folder; dated-heading MEMORY; partial coverage", "run ID ≠ folder; bullet `## Runs`; em-dash node suffixes", "missing run identity, unknown state token, unresolved PR, seeded two-graph overlap (SOW-061)"):
    check("08 IA §9.3 " + q[:30], q, ia)
check("08 PRD DependencyEdge", "From `Dependencies.csv` registers and work-graph dependencies (WorkGraph)", prd)
check("08 SOW-015 notes", "Markdown work-graph dependencies arrive through SOW-095", norm(ledger_raw))
check("08 §5 row", "| DEL-02-08 | Work-graph parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-095 |", decomp)

check("09 RCN-002 run evidence", "run evidence — deliverable `MEMORY.md` run-index entries as RunRecord join evidence, with `STATUS.json` / `RUNTIME_SUMMARY.json` as declared historical grammar or current evidence per profile", prd)
check("09 §7.1 RunRecord row", blockquote_after(t9, 'The §7.1 record-tier row "RunRecord" states the entity\'s purpose:'), prd)
check("09 DEL-01-01 REQ-006 quote", "only summaries of checkout-contained AgentRun evidence (`STATUS.json`, `RUNTIME_SUMMARY.json` under `execution/**`)", sow0101)
check("09 DEL-01-01 register RunRecord", "RunRecord is sourced from central receipts, work graphs and the MEMORY run index, with JSON run evidence historical", norm(deliv["DEL-01-01"]["Description"]))
checks.append((cbqa["DEL-02-09"]["RecommendedAction"] == "None" and cbqa["DEL-02-09"]["Risk"] == "LOW", "09 CBQA LOW / None (equality)"))
check("09 §8", "DEL-02-09 (MEMORY run-index parser) is S, LOW", decomp)
check("09 §5 row", "| DEL-02-09 | MEMORY run-index parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-096 |", decomp)
check("09 template intro", "Terse deliverable-local index of runs", memt)
check("09 template not a list", "This is not a future-work list or another decision register. Preserve existing historical entries.", memt)
check("09 template columns", "| Run ID / date | Work in this deliverable | Result and source links |", memt)
check("09 AGENTS indexes", "indexes what each run did in this deliverable", agents)
check("09 AGENTS no future", "memory carries no future assignments", agents)
check("09 design note class", "Derivative index", dn.replace("**", ""))
check("09 IA R-08", "0 template tables; bullet and dated-heading forms observed", ia)
check("09 IA FC-3 bullet", "bullet `## Runs`", ia)
for tag in ("08", "09"):
    check(tag + " PRD §7.1 remaining items field", "remaining items is a per-loop optional field, read only where the loop's feed profile declares it", prd)
    check(tag + " PRD §7.1 census source", "Lifecycle census from `_STATUS.md` (OPEN→ISSUED), stuck-age; remaining items is a per-loop optional field", prd)

bad = [n for ok, n in checks if not ok]
for ok, n in checks:
    print(("PASS " if ok else "FAIL ") + n)
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(checks)-len(bad)}/{len(checks)}")
sys.exit(1 if bad else 0)
