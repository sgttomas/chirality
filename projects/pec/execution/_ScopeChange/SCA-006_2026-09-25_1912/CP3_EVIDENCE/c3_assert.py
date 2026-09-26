#!/usr/bin/env python3
"""B6 Lane C3: exact successor assertions (Propagation_Plan.md §C3), read-only.

Live files are read from the worktree; revision-1.5 / PRD v2.3 preimages are
read from files saved by `git show origin/main:<path>` (origin/main 94e9255b6).
Usage: c3_assert.py <preimage_dir>
"""
import csv, io, re, sys, pathlib, json
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
P = R / "projects/pec"
D = P / "execution/_Decomposition"
PRE = pathlib.Path(sys.argv[1])
res, fails = [], 0
def check(name, got, exp):
    global fails
    ok = got == exp
    fails += (not ok)
    res.append({"check": name, "expected": exp, "observed": got, "result": "PASS" if ok else "FAIL"})

sl = list(csv.DictReader((D / "ScopeLedger.csv").open(encoding="utf-8")))
dl = list(csv.DictReader((D / "Deliverables.csv").open(encoding="utf-8")))
cb = list(csv.DictReader((D / "ContextBudgetQA.csv").open(encoding="utf-8")))
st = {k: sum(1 for r in sl if r["InOutStatus"] == k) for k in ("IN", "OUT", "TBD")}
check("scope items total", len(sl), 100)
check("scope items IN/OUT/TBD", [st["IN"], st["OUT"], st["TBD"]], [74, 18, 8])
check("packages (distinct PackageID in Deliverables.csv)", len({r["PackageID"] for r in dl}), 11)
retired = [r for r in dl if r["Description"].startswith("[RETIRED")]
active = [r for r in dl if not r["Description"].startswith("[RETIRED")]
check("deliverable rows", len(dl), 68)
check("deliverables active/RETIRED", [len(active), len(retired)], [64, 4])
check("ContextBudgetQA rows", len(cb), 68)
env = {k: sum(1 for r in active if r["ContextEnvelope"] == k) for k in ("S", "M", "L", "XL")}
check("active envelopes S/M/L/XL", [env["S"], env["M"], env["L"], env["XL"]], [28, 34, 2, 0])
# unmapped
IN = [r for r in sl if r["InOutStatus"] == "IN"]
check("IN items without package", sum(1 for r in IN if not r["PackageID"].strip()), 0)
check("IN items without deliverable", sum(1 for r in IN if not r["DeliverableIDs"].strip()), 0)
check("IN items without objective", sum(1 for r in IN if not r["ObjectiveIDs"].strip()), 0)
check("active deliverables without SupportsObjectives", sum(1 for r in active if not r["SupportsObjectives"].strip()), 0)
# union rule
objs = {r["ScopeItemID"]: set(x for x in r["ObjectiveIDs"].split(";") if x) for r in sl}
bad = []
for r in active:
    covers = [x for x in r["CoversScopeItems"].split(";") if x]
    u = set().union(*[objs.get(c, set()) for c in covers]) if covers else set()
    if u != set(x for x in r["SupportsObjectives"].split(";") if x):
        bad.append(r["DeliverableID"])
check("union rule holds on active rows", f"{len(active) - len(bad)}/{len(active)}", "64/64")
# per-package assigned IN scope
for pkg, n in (("PKG-04", 7), ("PKG-08", 8), ("PKG-10", 13)):
    check(f"{pkg} assigned IN scope", sum(1 for r in IN if r["PackageID"] == pkg), n)
# decomposition document
doc = (D / "SOFTWARE_DECOMP.md").read_text(encoding="utf-8")
pre_doc = (PRE / "DECOMP_rev1_5.md").read_text(encoding="utf-8")
def section(t, head):
    m = re.search(rf"^## {re.escape(head)}.*?$(.*?)(?=^## )", t, flags=re.S | re.M)
    return m.group(1) if m else ""
oi = section(doc, "10. Open Issues")
oi_rows = [l for l in oi.split("\n") if re.match(r"^\| OI-\d{3} \|", l)]
resolved = [l for l in oi_rows if "**RESOLVED" in l]
check("open / resolved issues", [len(oi_rows) - len(resolved), len(resolved)], [10, 3])
voc = section(doc, "9. Vocabulary Map")
voc_rows = [l for l in voc.split("\n") if l.startswith("| ") and not l.startswith("| CanonicalTerm") and not l.startswith("|---")]
check("vocabulary terms", len(voc_rows), 29)
def obj_statements(t):
    s = section(t, "3. Objectives")
    return {m.group(1): m.group(2) for m in re.finditer(r"^\| (OBJ-\d{3}) \| (.*?) \|", s, flags=re.M)}
o_new, o_old = obj_statements(doc), obj_statements(pre_doc)
check("objectives count", len(o_new), 6)
check("objective statements byte-identical to revision 1.5", o_new == o_old, True)
# stable identity: every rev-1.5 ID, name, package retained
pre_dl = {r["DeliverableID"]: r for r in csv.DictReader((PRE / "Deliverables_rev1_5.csv").open(encoding="utf-8"))}
pre_sl = {r["ScopeItemID"] for r in csv.DictReader((PRE / "ScopeLedger_rev1_5.csv").open(encoding="utf-8"))}
cur_dl = {r["DeliverableID"]: r for r in dl}
lost = [k for k in pre_dl if k not in cur_dl or cur_dl[k]["Name"] != pre_dl[k]["Name"] or cur_dl[k]["PackageID"] != pre_dl[k]["PackageID"]]
check("rev-1.5 deliverable IDs/names/packages retained", lost, [])
check("rev-1.5 scope IDs retained", sorted(pre_sl - {r["ScopeItemID"] for r in sl}), [])
check("new deliverable IDs (append-only)", sorted(set(cur_dl) - set(pre_dl)), ["DEL-08-06", "DEL-10-13"])
check("new scope IDs (append-only)", sorted({r["ScopeItemID"] for r in sl} - pre_sl), ["SOW-097", "SOW-098", "SOW-099", "SOW-100"])
# folder paths of existing deliverables unchanged (no folder added/removed by Lane A)
folders = sorted(p.name.split("_")[0] for p in (P / "execution").glob("PKG-*/*/DEL-*") if p.is_dir())
check("deliverable folders on disk (66; none added or removed)", len(folders), 66)
check("no folder for DEL-08-06 / DEL-10-13 (B1 deferred)", [x for x in folders if x in ("DEL-08-06", "DEL-10-13")], [])
# PRD
prd = (P / "docs/PRD.md").read_text(encoding="utf-8")
prd_old = (PRE / "PRD_v2_3.md").read_text(encoding="utf-8")
reqs = re.findall(r"^\| (PEC-(?:ORI|RCN|GAT|PRS|STR|API|DSH|SVC)-\d{3}) \|", prd, flags=re.M)
check("PRD requirement rows", len(reqs), 49)
check("PRD unique requirement IDs", len(set(reqs)), 49)
def row(t, key):
    rows = [l for l in t.split("\n") if l.startswith(f"| {key} |") or l.startswith(f"| **{key}** |") or l.startswith(f"| **{key} — ")]
    return rows
for key in ("PEC-K-01", "PEC-K-02", "PEC-K-11", "P1"):
    a, b = row(prd, key), row(prd_old, key)
    check(f"PRD {key} row byte-identical to v2.3 (rows found {len(a)})", a == b and len(a) >= 1, True)
out = {"fails": fails, "results": res}
print(json.dumps(out, indent=1))
sys.exit(1 if fails else 0)
