#!/usr/bin/env python3
"""Read-only D-PEC-95 postimage checks: compare a pre-state tree with a post-state tree.

Usage: python3 verify_d95.py <pre_root> <post_root> [--option A|P]
Exit 0 when every check holds; 1 otherwise. Prints one line per check.
"""
import argparse
import csv
import difflib
import io
import re
import sys
from pathlib import Path

EX = "projects/pec/execution"
QUOTE_ROWS = {"DEP-03-01-005", "DEP-03-01-008", "DEP-03-01-009", "DEP-03-01-010", "DEP-03-01-011",
              "DEP-03-01-012", "DEP-03-01-013", "DEP-05-01-004", "DEP-05-02-003", "DEP-06-03-003",
              "DEP-08-04-005", "DEP-08-05-004", "DEP-09-05-006", "DEP-09-05-007", "DEP-09-05-008",
              "DEP-10-05-004", "DEP-10-05-005", "DEP-10-10-003", "DEP-10-12-003"}
RETIRED = {"DEL-06-04", "DEL-07-02", "DEL-07-04", "DEL-07-05"}
REV15 = re.compile(r"revision 1\.5 \(`current_basis`,\s+SCA-005 successor")


def rows(path: Path):
    return list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"), newline="")))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pre", type=Path)
    ap.add_argument("post", type=Path)
    ap.add_argument("--option", choices=["A", "P"], default="A")
    ap.add_argument("--retired-covers", action="store_true")
    a = ap.parse_args()
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print(f"{'PASS' if cond else 'FAIL'}\t{name}\t{detail}")

    pre, post = a.pre, a.post
    ctx = sorted(p.relative_to(post) for p in (post / EX).glob("PKG-*/1_Working/DEL-*/_CONTEXT.md"))
    ref = sorted(p.relative_to(post) for p in (post / EX).glob("PKG-*/1_Working/DEL-*/_REFERENCES.md"))
    check("population", (len(ctx), len(ref)) == (66, 66), f"{len(ctx)} contexts / {len(ref)} references")
    c15 = [p for p in ctx if REV15.search((post / p).read_text(encoding="utf-8"))]
    c14 = [p for p in ctx if "SCA-004 successor)." in (post / p).read_text(encoding="utf-8")]
    check("contexts name revision 1.5", len(c15) == 66 and not c14, f"{len(c15)}/66; ending at 1.4: {len(c14)}")
    r15 = [p for p in ref if "(revision 1.5, accepted `current_basis`; SCA-005 successor)" in (post / p).read_text(encoding="utf-8")
           and "`docs/PRD.md` v2.3 (accepted source corpus" in (post / p).read_text(encoding="utf-8")]
    r14 = [p for p in ref if re.search(r"revision 1\.4, accepted|`docs/PRD.md` v2\.2", (post / p).read_text(encoding="utf-8"))]
    check("references name revision 1.5 and PRD v2.3", len(r15) == 66 and not r14, f"{len(r15)}/66; at 1.4/v2.2: {len(r14)}")

    # N2 semantic preservation: every changed metadata file differs only on the pinned anchor lines
    n_ctx = n_ref = 0
    bad = []
    for p in ctx + ref:
        a_t = (pre / p).read_text(encoding="utf-8").splitlines(keepends=True)
        b_t = (post / p).read_text(encoding="utf-8").splitlines(keepends=True)
        if a_t == b_t:
            continue
        d = [ln for ln in difflib.unified_diff(a_t, b_t, n=0) if ln[:1] in "+-" and ln[:3] not in ("+++", "---")]
        minus = [ln[1:] for ln in d if ln[0] == "-"]
        plus = [ln[1:] for ln in d if ln[0] == "+"]
        if p.name == "_CONTEXT.md":
            n_ctx += 1
            good = (len(minus) == 1 and minus[0].endswith("then by revision 1.4 (`current_basis`, SCA-004 successor).\n")
                    and plus == [minus[0][:-2] + ",\n", "then by revision 1.5 (`current_basis`, SCA-005 successor).\n"])
        else:
            n_ref += 1
            exp = [m.replace("revision 1.4", "revision 1.5").replace("SCA-004", "SCA-005").replace("v2.2", "v2.3")
                   if ("revision 1.4" in m or "v2.2" in m) else
                   re.sub(r"covers (SOW-\d{3})\)", r"covers none — retired under SCA-005, formerly \1)", m)
                   for m in minus]
            n_exp = 3 if (a.retired_covers and p.parent.name.split("_")[0] in RETIRED) else 2
            good = len(minus) == n_exp and exp == plus
        if not good:
            bad.append(str(p))
    check("metadata edits confined to anchors", not bad and (n_ctx, n_ref) == (42, 64),
          f"changed {n_ctx} contexts / {n_ref} references; off-anchor {bad[:3]}")
    tails = {(post / p).read_text(encoding="utf-8").split("## Provenance", 1)[1] for p in ctx
             if not p.parent.name.startswith(("DEL-02-08_", "DEL-02-09_"))}
    check("64 pre-existing contexts share one provenance block", len(tails) == 1, f"{len(tails)} distinct")

    # N3: row identity and cell conservation; quote currency
    changed_cells = {}
    n_active = n_verb = 0
    for p in sorted((post / EX).glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
        rel = p.relative_to(post)
        before, after = rows(pre / rel), rows(post / rel)
        if [r["DependencyID"] for r in before] != [r["DependencyID"] for r in after]:
            check(f"row identity {rel}", False)
        for rb, ra in zip(before, after):
            diff = sorted(k for k in rb if rb[k] != ra[k])
            if diff:
                changed_cells[rb["DependencyID"]] = diff
        for r in after:
            if (r["DependencyClass"], r["Status"]) == ("EXECUTION", "ACTIVE"):
                n_active += 1
                ev = post / "projects/pec" / r["EvidenceFile"]
                n_verb += ev.is_file() and r["EvidenceQuote"] in ev.read_text(encoding="utf-8")
    check("only the 19 rows changed", set(changed_cells) == QUOTE_ROWS, f"{len(changed_cells)} rows")
    check("only EvidenceQuote, LastSeen, Notes changed",
          all(v == ["EvidenceQuote", "LastSeen", "Notes"] for v in changed_cells.values()),
          str(sorted({tuple(v) for v in changed_cells.values()})))
    check("ACTIVE EXECUTION quotes verbatim", n_active == n_verb == 111, f"{n_verb}/{n_active}")

    # ACTIVE ANCHOR rows: field-summary quotes agree with the registers (design form, not verbatim)
    dels = {r["DeliverableID"]: r for r in rows(post / EX / "_Decomposition/Deliverables.csv")}
    ledger = {r["ScopeItemID"]: r for r in rows(post / EX / "_Decomposition/ScopeLedger.csv")}
    anchors = bad_anchor = 0
    for p in sorted((post / EX).glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
        for r in rows(p):
            if (r["DependencyClass"], r["Status"]) != ("ANCHOR", "ACTIVE"):
                continue
            anchors += 1
            if r["AnchorType"] == "IMPLEMENTS_NODE":
                good = dels[r["FromDeliverableID"]]["PackageID"] == r["TargetRefID"]
            else:
                good = r["FromDeliverableID"] in ledger[r["TargetRefID"]]["DeliverableIDs"].split(";")
            bad_anchor += not good
    check("ACTIVE ANCHOR rows agree with the registers", bad_anchor == 0, f"{anchors - bad_anchor}/{anchors}")

    # N1 files: append-only for the SCA-005 snapshot files under option A; unchanged under P
    sca = f"{EX}/_ScopeChange/SCA-005_2026-09-23_2139"
    for name in ("Handoff_State.md", "RUN_SUMMARY.md"):
        a_b, p_b = (pre / sca / name).read_bytes(), (post / sca / name).read_bytes()
        if a.option == "A":
            check(f"{name} append-only", p_b.startswith(a_b) and len(p_b) > len(a_b), f"+{len(p_b) - len(a_b)} bytes")
        else:
            check(f"{name} unchanged", a_b == p_b)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
