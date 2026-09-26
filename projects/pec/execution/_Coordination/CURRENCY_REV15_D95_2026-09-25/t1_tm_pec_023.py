#!/usr/bin/env python3
"""D-PEC-95 T1 draft: close TM-PEC-023 RESOLVED_BY_DECISION in the PEC Task Management register.

For WORKING_ITEMS under task-management (a TASK never writes register rows). Deterministic,
stdlib only; fails closed (exit 1, nothing written) unless REGISTER.csv hashes to its pinned
preimage at 13df8b795, every row round-trips byte-exactly (QUOTE_ALL, LF), TM-PEC-023 is OPEN
with the pinned Concern, and the EvidenceQuote is verbatim in the first EvidenceRef file with
every EvidenceSha matching. Only Status, Disposition, EvidenceRef, EvidenceSha, EvidenceQuote,
LastReviewed, Closed and Notes of that one row change. Archiving the closed row is a separate,
mechanical `tools/taskmgmt/taskmgmt.py archive` step.

Usage: python3 t1_tm_pec_023.py --repo <REPO_ROOT> --act-date YYYY-MM-DD [--check-only]
"""
import argparse
import csv
import hashlib
import io
import sys
from pathlib import Path

REG = "projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv"
REG_PRE = "d350d007362641323dba7dac44309b27b3f8a091432abdf9bed825c4b5d5799d"
EVIDENCE = [
    ("projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md",
     "50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350"),
    ("projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/DECISION.md",
     "ca88f6a8f9bca197f64a56f07c73364cd8f7533acb7bf64206a34e0e1fba3d66"),
    ("projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-3_2026-09-25/DECISION.md",
     "35c211a604cb7a05d3fca5cec86fe6bb297a095ad6aa7c5efa72b2cd1599f673"),
    ("projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/DECISION.md",
     "4328633cf0d134b86b01ad8981a2fcb259acac828785d211bdee5f8aea8f3013"),
]
QUOTE = "TM-PEC-023 closure `RESOLVED_BY_DECISION` citing SCA-005"
CONCERN_START = "Accepted revision-1.4 residue: nine deliverables (DEL-00-02, DEL-03-05, DEL-05-01, DEL-07-02,"
NOTE = ("; Closed {D} as RESOLVED_BY_DECISION by WORKING_ITEMS under task-management, applying recorded owner "
        "decisions, confirmed in the D-PEC-95 ruling (question 2): SCA-005 group-1 amendment 1 (2026-09-24) selected "
        "objectives for rows 1, 2, 3, "
        "5, 8 and 9 and made rows 4, 6 and 7 moot by retirement; checkpoint 2 (D-PEC-92, 2026-09-25) accepted "
        "Propagation_Plan.md §B8, which names this closure after checkpoint 3; checkpoint 3 (2026-09-25) accepted "
        "revision 1.5, where the nine deliverables carry the selected SupportsObjectives or are RETIRED, and the "
        "post-setup audit COV_SCA005_POSTSETUP_2026-09-25_1606 reports no IN scope item and no active deliverable "
        "without an objective. Recorded under D-PEC-95 T1. No product, lifecycle, source, release or reliance "
        "state changes.")


def line(values):
    out = io.StringIO()
    csv.writer(out, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow(values)
    return out.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--act-date", required=True)
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    repo, act = a.repo.resolve(), a.act_date
    try:
        raw = (repo / REG).read_bytes()
        if hashlib.sha256(raw).hexdigest() != REG_PRE:
            raise ValueError("REGISTER.csv preimage mismatch")
        for rel, want in EVIDENCE:
            if hashlib.sha256((repo / rel).read_bytes()).hexdigest() != want:
                raise ValueError(f"evidence hash mismatch {rel}")
        if QUOTE not in (repo / EVIDENCE[0][0]).read_text(encoding="utf-8"):
            raise ValueError("EvidenceQuote not verbatim in the first EvidenceRef")
        text = raw.decode("utf-8")
        lines = text.split("\n")
        if lines[-1] != "":
            raise ValueError("no trailing newline")
        lines = lines[:-1]
        header = next(csv.reader([lines[0]]))
        out, hit = [lines[0] + "\n"], 0
        for ln in lines[1:]:
            values = next(csv.reader([ln]))
            if line(values) != ln + "\n":
                raise ValueError(f"row does not round-trip: {values[1]}")
            row = dict(zip(header, values))
            if row["ActionItemID"] != "TM-PEC-023":
                out.append(ln + "\n")
                continue
            hit += 1
            if row["Status"] != "OPEN" or row["Disposition"] or not row["Concern"].startswith(CONCERN_START):
                raise ValueError("TM-PEC-023 is not the pinned OPEN row")
            row.update({
                "Status": "CLOSED", "Disposition": "RESOLVED_BY_DECISION",
                "EvidenceRef": "; ".join(p for p, _ in EVIDENCE),
                "EvidenceSha": "; ".join(s for _, s in EVIDENCE),
                "EvidenceQuote": QUOTE, "LastReviewed": act, "Closed": act,
                "Notes": row["Notes"] + NOTE.replace("{D}", act),
            })
            out.append(line([row[k] for k in header]))
        if hit != 1:
            raise ValueError(f"TM-PEC-023 found {hit} times")
        data = "".join(out).encode("utf-8")
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    if not a.check_only:
        (repo / REG).write_bytes(data)
    print(f"{'RENDER' if a.check_only else 'WRITE'}\t{REG}\t{REG_PRE}\t{hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
