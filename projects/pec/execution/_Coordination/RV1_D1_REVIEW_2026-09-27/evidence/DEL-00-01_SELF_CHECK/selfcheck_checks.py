"""RV1 SELF_CHECK DEL-00-01 mechanical checks (read-only on the repository)."""
import csv, re, sys, json, hashlib
R = sys.argv[1]
P = R + "/projects/pec/execution"
D = P + "/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures"
sow = open(D + "/ScopeOfWork.md", encoding="utf-8").read().splitlines()
adr = open(D + "/artifacts/v2/ADRs.md", encoding="utf-8").read().splitlines()

def show(title): print("\n## " + title)

show("C1 identity check (substitute for audit-decomp)")
ctx = open(D + "/_CONTEXT.md", encoding="utf-8").read()
fm = {l.split(":",1)[0]: l.split(":",1)[1].strip() for l in sow[1:7]}
row = next(r for r in csv.DictReader(open(P + "/_Decomposition/Deliverables.csv", encoding="utf-8")) if r["DeliverableID"] == "DEL-00-01")
led = next(r for r in csv.DictReader(open(P + "/_Decomposition/ScopeLedger.csv", encoding="utf-8")) if r["ScopeItemID"] == "SOW-088")
dec = open(P + "/_Decomposition/SOFTWARE_DECOMP.md", encoding="utf-8").read()
checks = [
 ("SOW frontmatter deliverable_id == DEL-00-01", fm.get("deliverable_id") == "DEL-00-01"),
 ("SOW frontmatter package_id == PKG-00 == Deliverables.csv PackageID", fm.get("package_id") == "PKG-00" == row["PackageID"]),
 ("SOW project_scope_refs [SOW-088] == Deliverables.csv CoversScopeItems", fm.get("project_scope_refs") == "[SOW-088]" and row["CoversScopeItems"] == "SOW-088"),
 ("SOW package_objective_refs [OBJ-005] == Deliverables.csv SupportsObjectives", fm.get("package_objective_refs") == "[OBJ-005]" and row["SupportsObjectives"] == "OBJ-005"),
 ("_CONTEXT.md DeliverableID/PackageID/CoversScopeItems/SupportsObjectives agree", all(s in ctx for s in ["| DeliverableID | DEL-00-01 |", "| PackageID | PKG-00", "| CoversScopeItems | SOW-088 |", "| SupportsObjectives | OBJ-005 |"])),
 ("_CONTEXT.md description == Deliverables.csv Description", row["Description"] in ctx),
 ("SOW CLM-002 quotes Deliverables.csv Description (minus final period)", row["Description"].rstrip(".") in "\n".join(sow)),
 ("ScopeLedger SOW-088 maps PKG-00 / DEL-00-01 / OBJ-005, OpenIssue TRUE", (led["PackageID"], led["DeliverableIDs"], led["ObjectiveIDs"], led["OpenIssue"]) == ("PKG-00", "DEL-00-01", "OBJ-005", "TRUE")),
 ("SOW quotes SOW-088 statement verbatim (whitespace-normalized)", " ".join(led["ScopeItemStatement"].split()) in " ".join(" ".join(sow).split())),
 ("SOFTWARE_DECOMP §5 row DEL-00-01 present", "| DEL-00-01 | v2 first ADRs (core isolation + carried postures) | DOC_UPDATE | S | pre-P1 | SOW-088 |" in dec),
 ("SOFTWARE_DECOMP OBJ-005 maps SOW-088 and DEL-00-01", re.search(r"\| OBJ-005 \|[^\n]*SOW-088[^\n]*DEL-00-01", dec) is not None),
 ("OI-012 disposition 'Decided in DEL-00-01's ADR; owner review at that ADR' present", "| Decided in DEL-00-01's ADR; owner review at that ADR |" in dec),
]
for name, ok in checks: print(("PASS " if ok else "FAIL ") + name)

show("C2 output/evaluation matrix closure")
rows = [l for l in sow if l.startswith("| OUT-")]
ids = lambda pfx, text: set(re.findall(pfx + r"-\d{3}", text))
defined = lambda pfx: [m for l in sow for m in re.findall(r"^- \*\*(" + pfx + r"-\d{3})\*\*", l)]
acs_in = []; vers_in = set(); reqs_in = set(); outs_in = set()
for r in rows:
    c = [x.strip() for x in r.strip("|").split("|")]
    outs_in.add(c[0]); reqs_in |= ids("REQ", c[2]); acs_in += re.findall(r"AC-\d{3}", c[3]); vers_in |= ids("VER", c[4])
print("matrix rows:", len(rows))
for pfx, used in [("OUT", outs_in), ("REQ", reqs_in), ("VER", vers_in)]:
    d = defined(pfx); print(f"{pfx} defined {len(d)} {d}; in matrix {sorted(used)}; missing {sorted(set(d)-used)}")
d = defined("AC"); print(f"AC defined {len(d)}; matrix occurrences {acs_in}; each exactly once: {sorted(acs_in)==sorted(d)}")
print("AC-007 verification cell:", [ [x.strip() for x in r.strip('|').split('|')][4] for r in rows if 'AC-007' in r][0])

show("C3 TBD inventory (ScopeOfWork.md and ADRs.md)")
print("registered TBD items:", defined("TBD"))
for name, lines in [("ScopeOfWork.md", sow), ("artifacts/v2/ADRs.md", adr)]:
    hits = [(i+1, l) for i, l in enumerate(lines) if re.search(r"\bTBD\b", l)]
    print(f"{name}: {len(hits)} line(s) containing the token TBD")
    for i, l in hits: print(f"  L{i}: {l[:150]}")

show("C4 AC-002: CLM-006 Gate 4 basis elements vs the ADR-PEC-V2-001 Context section")
start = adr.index("### Context"); end = adr.index("### Decision")
context = " ".join(adr[start:end]); whole = " ".join(adr)
elements = [
 ("E1 invariants force isolation properties either way (PEC-K-07, PEC-K-02, PEC-SVC-001)", ["two conforming isolation styles", "PEC-K-07", "PEC-K-02", "PEC-SVC-001"]),
 ("E2 package grain congruent with hexagonal (PKG-03/04/05 + PKG-01; PKG-02/06 + store; PKG-07/08/09)", ["PKG-03/04/05", "PKG-02/06", "PKG-07/08/09"]),
 ("E3 nearly all §16 open decisions are adapter-level, so core isolation keeps them open cheaply", ["adapter-level"]),
 ("E4 lighter functional-core/imperative-shell variant fits a deterministic-derivation service", ["lighter"]),
 ("E5 seam: entity schema (core) vs store persistence (adapter) inside PKG-01", ["entity-schema/core versus", "store-persistence/adapter seam inside PKG-01"]),
]
for name, toks in elements:
    inctx = all(t in context for t in toks); inadr = all(t in whole for t in toks)
    print(f"{name}: tokens {toks} -> in Context section: {inctx}; anywhere in ADR: {inadr}")
for pat in ["§16", "adapter-level", "open cheaply", "OI-001", "lighter", "ceremony"]:
    print(f"  grep '{pat}' in ADRs.md:", [i+1 for i, l in enumerate(adr) if pat in l])

show("C5 REQ-005 literal archive path in ADRs.md")
print("grep 'docs/.archive' :", [i+1 for i, l in enumerate(adr) if "docs/.archive" in l])
print("grep 'ADR.md' :", [i+1 for i, l in enumerate(adr) if "ADR.md" in l])
print("grep 'archived ADR' :", [i+1 for i, l in enumerate(adr) if "archived ADR" in l])

show("C6 SOW state and currency wording (proposal Other findings 1, 7, 8)")
pats = ["No ADR exists for this deliverable", "`INITIALIZED`", "is **undecided** at the time of this contract", "the deliverable is at `INITIALIZED` and no ADR has been authored",
        "revision 1.3, the current successor basis", "now names `SOFTWARE_DECOMP.md`", "SCA-003 establishes revision 1.3 as the", "The accepted basis is `SOFTWARE_DECOMP.md` revision 1.3", "future authoring run"]
def locate(pat):
    """Return the 1-based start lines of whitespace-normalized matches of pat."""
    norm = " ".join(pat.split()); out = []
    for i in range(len(sow)):
        window = " ".join(" ".join(sow[i:i+3]).split())
        if window.startswith(norm) or (norm in window and norm not in " ".join(" ".join(sow[i+1:i+3]).split())):
            out.append(i+1)
    return out
for pat in pats:
    print(f"  '{' '.join(pat.split())}': start lines", locate(pat))
refs = open(D + "/_REFERENCES.md", encoding="utf-8").read()
print("  _REFERENCES.md names revision 1.6 current_basis:", "revision 1.6, accepted `current_basis`" in refs)
print("  _STATUS.md current state:", [l for l in open(D + "/_STATUS.md", encoding="utf-8").read().splitlines() if l.startswith("**Current State:**")])
print("  ADR file exists, ADR-PEC-V2-001 Status line:", [l for l in adr if l.startswith("- Status:")])

show("C7 REQ-004 / CLM-005 vs ADR carried posture 3 (runtime boundary elements)")
elems = ["application-owned Runtime service", "sessions, delegation", "tools, turn locks", "interruption", "custodied by Codex", "local-model residency", "optional client", "no second execution loop", "human-only", "D-GOV-43", "K-RUNTIME-1"]
req4 = next(l for l in sow if l.startswith("- **REQ-004**")); clm5 = next(l for l in sow if l.startswith("- **CLM-005**"))
p3s = next(i for i, l in enumerate(adr) if l.startswith("3. **The surviving live boundary")); p3 = " ".join(adr[p3s:p3s+9])
p3n = re.sub(r"\s+", " ", p3)
for e in elems: print(f"  {e!r}: CLM-005 {e in clm5}; REQ-004 {e in req4}; ADR posture 3 {e in p3n}")
print("  'Root owns' anywhere in SOW:", [i+1 for i, l in enumerate(sow) if "Root owns" in l], "; in ADR:", [i+1 for i, l in enumerate(adr) if "Root owns" in l])
print("  ADR 'Root-owned' lines:", [(i+1, l.strip()) for i, l in enumerate(adr) if "Root-owned" in l])
print("  retired-allocation list in REQ-004:", "deterministic acts, RBAC, reporting, visibility, and data boundaries" in req4,
      "; in ADR posture 2:", "deterministic acts, RBAC, reporting, visibility, and data" in " ".join(adr))

show("C8 whitespace of bytes under review")
for name, lines in [("ScopeOfWork.md", sow), ("artifacts/v2/ADRs.md", adr)]:
    print(f"  {name}: trailing-whitespace lines {[i+1 for i,l in enumerate(lines) if l != l.rstrip()]}")
