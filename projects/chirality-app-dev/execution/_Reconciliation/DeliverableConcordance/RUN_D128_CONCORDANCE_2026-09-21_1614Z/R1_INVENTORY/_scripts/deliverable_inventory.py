#!/usr/bin/env python3
"""DELIVERABLE_INVENTORY.csv: one row per deliverable folder in the frozen checkout.

Rules: LifecycleState/LastUpdated from `**Current State:**`/`**Last Updated:**` in _STATUS.md;
SoWLines = line count of ScopeOfWork.md; ClaimUnits = CLAIM_INDEX rows for the deliverable;
RemainingItems = CLAIM_INDEX REM+REMTXT rows; GatedRemainingItems = those with >=1 parsed gate
fragment (same parser as REMAINING_INVENTORY); AssessmentFile = Assessment_*.md (sorted, `;`-joined);
AssessmentDate = the `| Date | ... |` header cell of each; DecompositionBasis = SoW front-matter
`decomposition_basis:`; HasDependenciesCsv = Y/N for Dependencies.csv.
"""
import argparse, glob, os, re
import r1_common as C


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--claim-index", default=None)
    a = ap.parse_args()
    root = a.frozen_root
    claims = C.load_claim_index(a.claim_index)
    rem = C.remaining_units(root, claims)
    rows = []
    for del_id, d in sorted(C.deliverable_dirs(root).items()):
        pkg = os.path.basename(os.path.dirname(os.path.dirname(d)))[:6]
        st = C.read_text(os.path.join(d, "_STATUS.md"))
        sow_path = os.path.join(d, "ScopeOfWork.md")
        sow = C.read_text(sow_path)
        m = re.search(r"^decomposition_basis:\s*(.*)$", sow, re.M)
        assess = sorted(glob.glob(os.path.join(d, "Assessment_*.md")))
        dates = []
        for p in assess:
            mm = re.search(r"^\|\s*Date\s*\|\s*([^|]*?)\s*\|", C.read_text(p), re.M)
            dates.append(mm.group(1) if mm else "")
        units = [r for r in claims if r["DeliverableID"] == del_id]
        drem = [u for u in rem if u["DeliverableID"] == del_id]
        rows.append([
            pkg, del_id, C.rel(root, d),
            C.status_field(st, "Current State"), C.status_field(st, "Last Updated"),
            len(sow.splitlines()), len(units), len(drem), sum(1 for u in drem if u["Gates"]),
            ";".join(C.rel(root, p) for p in assess), ";".join(dates),
            m.group(1).strip() if m else "",
            "Y" if os.path.isfile(os.path.join(d, "Dependencies.csv")) else "N",
        ])
    C.write_csv(a.out, ["PackageID", "DeliverableID", "Path", "LifecycleState", "LastUpdated", "SoWLines",
                        "ClaimUnits", "RemainingItems", "GatedRemainingItems", "AssessmentFile",
                        "AssessmentDate", "DecompositionBasis", "HasDependenciesCsv"], rows)
    print(len(rows), "deliverables")


if __name__ == "__main__":
    main()
