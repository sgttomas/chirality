#!/usr/bin/env python3
"""Independent postimage checks for D-PEC-101 part K1 (preparation aid; not bound).

Usage: python3 verify_d101_k1.py <pre_root> <post_root> [--allow-k4]

Compares two repository trees (pre = export of the preimage commit, post = after
the K1 act). Checks, without reusing the generator's code:
  1. containment: under projects/, the changed or added files are exactly the
     K1 grant (12 created in two new folders, 4 registers, 16 mirrors); with
     --allow-k4 the K4 re-pin targets (_CONTEXT.md / _REFERENCES.md of existing
     folders) may also differ; nothing is deleted;
  2. registers: every pre row survives; in DEP-09-06-003 / DEP-10-03-003 only
     EvidenceQuote, LastSeen and Notes change; DEL-04-03 / DEL-08-03 gain only
     one appended ANCHOR row each; new registers hold 2 ANCHOR + N EXECUTION;
  3. mirrors: each modified _DEPENDENCIES.md only gains lines; every ACTIVE
     EXECUTION edge in the corpus has one table row `| E |` in its source file
     and one `[E]` bullet in its target file;
  4. new files: _CONTEXT.md fields equal the Deliverables.csv row; _STATUS.md is
     the OPEN form; _SEMANTIC.md empty; _DEPENDENCIES.md carries the SPEC §5.2
     headings in order;
  5. quote currency: every ACTIVE EXECUTION EvidenceQuote is verbatim in its
     EvidenceFile;
  6. anchor coverage (COV-080): every IN ScopeLedger item has an ACTIVE
     TRACES_TO_REQUIREMENT row in the register of each deliverable it names;
  7. counts: registers, rows, ANCHOR/EXECUTION, ACTIVE EXECUTION edges.
Exit 0 when all pass; 1 otherwise.
"""
import csv, glob, io, os, re, sys
from pathlib import Path

pre, post = Path(sys.argv[1]), Path(sys.argv[2])
allow_k4 = "--allow-k4" in sys.argv
EX = "projects/pec/execution"
fails = []
def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)

def files(root):
    out = {}
    for dp, _, fs in os.walk(root / "projects"):
        for f in fs:
            p = Path(dp) / f
            out[str(p.relative_to(root))] = p.read_bytes()
    return out

A, B = files(pre), files(post)
changed = sorted(k for k in B if A.get(k) != B[k])
deleted = sorted(k for k in A if k not in B)
check(not deleted, f"no file deleted ({len(deleted)})")
new_dirs = {"DEL-08-06": f"{EX}/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface",
            "DEL-10-13": f"{EX}/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate"}
created = {f"{d}/{n}" for d in new_dirs.values() for n in
           ("_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "_SEMANTIC.md", "Dependencies.csv")}
def folder(did):
    return [p for p in glob.glob(str(pre / EX / f"PKG-*/1_Working/{did}_*"))][0]
mirrors = ["DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-02-04", "DEL-02-05", "DEL-02-06", "DEL-02-08", "DEL-02-09",
           "DEL-03-04", "DEL-04-01", "DEL-04-03", "DEL-04-05", "DEL-08-01", "DEL-08-02", "DEL-08-03", "DEL-10-02"]
regs = ["DEL-04-03", "DEL-08-03", "DEL-09-06", "DEL-10-03"]
grant_mod = {str(Path(folder(d)).relative_to(pre)) + "/_DEPENDENCIES.md" for d in mirrors} | \
            {str(Path(folder(d)).relative_to(pre)) + "/Dependencies.csv" for d in regs}
extra = [k for k in changed if k not in created | grant_mod]
if allow_k4:
    extra = [k for k in extra if not (k in A and re.search(r"/DEL-\d\d-\d\d_[^/]+/_(CONTEXT|REFERENCES)\.md$", k))]
check(set(changed) >= created | grant_mod and not extra,
      f"containment: {len(changed)} changed/added; grant {len(created)} created + {len(grant_mod)} modified; outside grant {extra}")

def rows(data):
    return list(csv.DictReader(io.StringIO(data.decode("utf-8"), newline="")))

# 2. registers
for d in regs:
    rel = str(Path(folder(d)).relative_to(pre)) + "/Dependencies.csv"
    ra, rb = rows(A[rel]), rows(B[rel])
    ia = {r["DependencyID"]: r for r in ra}
    ib = {r["DependencyID"]: r for r in rb}
    check(set(ia) <= set(ib), f"{d}: every pre row survives")
    for k, r in ia.items():
        diff = sorted(c for c in r if r[c] != ib[k][c])
        allowed = {"DEP-09-06-003": ["EvidenceQuote", "LastSeen", "Notes"],
                   "DEP-10-03-003": ["EvidenceQuote", "LastSeen", "Notes"]}.get(k, [])
        check(diff == allowed, f"{d} {k}: changed cells {diff}")
    added = [ib[k] for k in ib if k not in ia]
    want = 1 if d in ("DEL-04-03", "DEL-08-03") else 0
    check(len(added) == want and all(r["DependencyClass"] == "ANCHOR" and r["AnchorType"] == "TRACES_TO_REQUIREMENT"
                                     for r in added), f"{d}: {len(added)} appended ANCHOR row(s)")
    check(A[rel].decode().splitlines()[: len(ra) + 1] == B[rel].decode().splitlines()[: len(ra) + 1] or d in ("DEL-09-06", "DEL-10-03"),
          f"{d}: pre rows keep their order and bytes (append-only)")

# 3. mirrors only gain lines
for d in mirrors:
    rel = str(Path(folder(d)).relative_to(pre)) + "/_DEPENDENCIES.md"
    la, lb = A[rel].decode().split("\n"), B[rel].decode().split("\n")
    it = iter(lb)
    check(all(any(x == y for y in it) for x in la), f"{d} mirror: pre lines preserved in order (insertion only)")

# corpus mirror invariant, quote currency, counts, anchor coverage
dirs = {}
for p in glob.glob(str(post / EX / "PKG-*/1_Working/DEL-*")):
    dirs[os.path.basename(p)[:9]] = p
n_reg = n_rows = n_anchor = n_exec = n_active_exec = n_ok = 0
anchors = set()
missing = []
for did, p in sorted(dirs.items()):
    f = Path(p) / "Dependencies.csv"
    if not f.is_file():
        continue
    n_reg += 1
    for r in rows(f.read_bytes()):
        n_rows += 1
        if r["DependencyClass"] == "ANCHOR":
            n_anchor += 1
            if r["Status"] == "ACTIVE" and r["AnchorType"] == "TRACES_TO_REQUIREMENT":
                anchors.add((did, r["TargetRefID"]))
            continue
        n_exec += 1
        if r["Status"] != "ACTIVE":
            continue
        n_active_exec += 1
        ev = post / "projects/pec" / r["EvidenceFile"]
        if ev.is_file() and r["EvidenceQuote"] in ev.read_text(encoding="utf-8"):
            n_ok += 1
        e = re.search(r"EdgeID=(E-[A-Z0-9]+)", r["Notes"]).group(1)
        src = (Path(p) / "_DEPENDENCIES.md").read_text(encoding="utf-8")
        tgt = (Path(dirs[r["TargetDeliverableID"]]) / "_DEPENDENCIES.md").read_text(encoding="utf-8")
        if src.count(f"| {e} |") != 1 or tgt.count(f"[{e}]") != 1:
            missing.append(e)
check(not missing, f"mirror invariant: every ACTIVE EXECUTION edge has one source-table row and one target bullet (missing {missing})")
check(n_ok == n_active_exec, f"quote currency: {n_ok}/{n_active_exec} ACTIVE EXECUTION quotes verbatim")
print(f"INFO counts: registers {n_reg}; rows {n_rows}; ANCHOR {n_anchor}; EXECUTION {n_exec}; ACTIVE EXECUTION {n_active_exec}")
with open(post / EX / "_Decomposition/ScopeLedger.csv", newline="", encoding="utf-8") as fh:
    ledger = list(csv.DictReader(fh))
gaps = [(s["ScopeItemID"], d) for s in ledger if s["InOutStatus"] == "IN"
        for d in s["DeliverableIDs"].split(";") if d and (d, s["ScopeItemID"]) not in anchors]
check(not gaps, f"anchor coverage: every IN scope item traced by each deliverable it names (gaps {gaps})")
check(all((d, s) in anchors for d, s in [("DEL-04-03", "SOW-097"), ("DEL-08-03", "SOW-098"),
                                         ("DEL-08-06", "SOW-099"), ("DEL-10-13", "SOW-100")]), "COV-080: SOW-097..100 traced")

# 4. new files
with open(post / EX / "_Decomposition/Deliverables.csv", newline="", encoding="utf-8") as fh:
    dels = {r["DeliverableID"]: r for r in csv.DictReader(fh)}
heads = ["## Dependency Tracking Mode", "## Declared Upstream (I need these before I can proceed)",
         "## Declared Downstream (These need me)", "## Extracted Dependency Register", "## Lifecycle Summary",
         "## Run Notes", "## Run History"]
for did, d in new_dirs.items():
    if not all(k in B for k in (f"{d}/{n}" for n in ("_CONTEXT.md", "_STATUS.md", "_SEMANTIC.md",
                                                       "_DEPENDENCIES.md", "_REFERENCES.md"))):
        check(False, f"{did}: new folder files present")
        continue
    ctx = B[f"{d}/_CONTEXT.md"].decode()
    r = dels[did]
    for label, col in (("DeliverableID", "DeliverableID"), ("Canonical name", "Name"), ("Type", "Type"),
                       ("ContextEnvelope", "ContextEnvelope"), ("PhaseHint", "PhaseHint"),
                       ("CoversScopeItems", "CoversScopeItems"), ("SupportsObjectives", "SupportsObjectives")):
        check(f"| {label} | {r[col]} |" in ctx, f"{did} _CONTEXT {label} = register")
    check(f"\n{r['Description']}\n" in ctx and f"\n{r['AnticipatedArtifacts']}\n" in ctx
          and f"\n{r['ContextEnvelopeNotes'] or '(none)'}\n" in ctx, f"{did} _CONTEXT description/artifacts/notes = register")
    st = B[f"{d}/_STATUS.md"].decode()
    check(re.fullmatch(rf"# Status: {did}\n\n\*\*Current State:\*\* OPEN\n\*\*Last Updated:\*\* \d{{4}}-\d\d-\d\d\n\n## History\n- \d{{4}}-\d\d-\d\d — State set to OPEN \(TASK\+preparation\)\n", st) is not None,
          f"{did} _STATUS.md is the OPEN form")
    check(B[f"{d}/_SEMANTIC.md"] == b"", f"{did} _SEMANTIC.md empty")
    dep = B[f"{d}/_DEPENDENCIES.md"].decode()
    pos = [dep.find("\n" + h + "\n") for h in heads]
    check(all(x >= 0 for x in pos) and pos == sorted(pos), f"{did} _DEPENDENCIES.md has the SPEC §5.2 headings in order")
    ref = B[f"{d}/_REFERENCES.md"].decode()
    check("(revision 1.6, accepted `current_basis`; SCA-006 successor)" in ref and "`docs/PRD.md` v2.4" in ref
          and f"covers {r['CoversScopeItems']})" in ref, f"{did} _REFERENCES names revision 1.6, PRD v2.4 and its coverage")
print("RESULT", "PASS" if not fails else f"FAIL ({len(fails)})")
sys.exit(1 if fails else 0)
