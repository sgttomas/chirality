#!/usr/bin/env python3
"""T1 (R4 step 1): write R3/OWNER_CHECK_APPLIED.md from DEC_OWNERCHECK.csv, the appended REMAP_LOG
lines and the check results. Reasoning text for R4-attention rows is kept here."""
import os, sys, subprocess, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "_scripts"))
from r3lib import *
from dump_rows import oc_rows
from make_dec_ownercheck import ANSWER, DECIDED, FIXES

ATTENTION = [
    ("DEL-09-05#CLM-010.8", "OC-05 yes", "PARTIALLY_IMPLEMENTED rests partly on 'no recorded gate' for the full K-VALIDATE-1 set before release; the owner confirms it passed for v3.0.0 and v3.0.1. The code part (desktop:dist in no PR gate) stands. R3 had this row UNDECIDED."),
    ("DEL-09-01#CLM-009.8", "OC-06 yes", "PARTIALLY_IMPLEMENTED and RemainingWork ('then rerun') rest partly on no post-A2 Section 8 run; the owner confirms one. The LEGACY_ONLY marker finding (R4-Q1) stands."),
    ("DEL-09-01#CLM-023", "OC-06 yes", "STALE_SPECIFICATION rests partly on 'current stable summary ... unsupported' (no summary; last recorded run 2026-09-04); a later run is confirmed, the summary is still not in the tree. The CI-chain part stands."),
    ("DEL-09-01#REM-1", "OC-06 yes", "RemainingWork asks to 'rerun Section 8 at a post-A2 basis'; the owner confirms a post-re-platform run. REMAINING_STATE_MISMATCH (gate condition 1 met) stands on code."),
    ("DEL-09-02#CLM-020.2", "OC-07 yes", "PARTIALLY_IMPLEMENTED rests partly on no recorded 16-ID Section 9 run; the owner confirms one with its summary kept (location not stated). The CI-retention finding stands."),
    ("DEL-09-04#CLM-009.8", "OC-12 yes", "PARTIALLY_IMPLEMENTED rests partly on no packaged app-server run with secret and network checks; the owner confirms one. The code finding (verify-codex-pin proves only --version; no secret/network assertion in the chain) stands. CLM-011.8 follows by SEE."),
    ("DEL-09-05#CLM-016.3", "OC-01 yes", "AUTHORITY_CONFLICT stands on the texts; the owner's testimony that the 3.0.0 and 3.0.1 candidates were named and authorized bears on the G6a exact-candidate clause and on RemainingWork's 'release act for the published build'."),
]


def main():
    dec = read_csv(os.path.join(WORK, "DEC_OWNERCHECK.csv"))[1]
    log = [l for l in read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1] if l["Source"] == "OWNER_CHECK"]
    final = {r["ClaimKey"]: r for r in read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1] + read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]}
    by_oc = collections.OrderedDict()
    for oc, kind, k in oc_rows():
        by_oc.setdefault(oc, []).append((kind, k))
    fix_by = collections.defaultdict(list)
    for oc, k, f, find, rep in FIXES:
        fix_by[(oc, k)].append((f, find, rep))
    dec_by = {(k, f): (v, why) for k, f, v, why in DECIDED}
    notes = collections.defaultdict(list)
    for d in dec:
        if d["Field"] == "Notes+":
            notes[d["ClaimKey"]].append(d["NewValue"])
    w = []
    w.append("# Owner check applied — RUN_D128 (R4 step 1)\n")
    w.append("The owner's answers to `OWNER_CHECK.md` (owner direction `r3_owner_check_answers`, read in RUN_BASIS Addendum 13) "
             "applied to `CLAIM_CONCORDANCE.csv` and `EXTENSION_CONCORDANCE.csv` through `_work/DEC_OWNERCHECK.csv` "
             "(Source `OWNER_CHECK`, last in `r3_build.py` DECISION_ORDER). Answers are owner testimony about events, not rulings on "
             "direction of change. A yes confirms an event; whether the deliverable text is accurate is judged against the claim. "
             "Helper scripts: `_work/T1R4_scripts/`.\n")
    w.append(f"Totals: {len(dec)} decision lines; {len(log)} REMAP_LOG lines appended; {len(final and {k for _, k in sum(by_oc.values(), [])})} listed rows, all changed "
             "(every listed row takes at least one note). Disposition moves: 2 (both `UNKNOWN` → `PARTIALLY_IMPLEMENTED`). "
             "HumanDecisionNeeded: unchanged on every row.\n")
    w.append("## Per question\n")
    for oc, lst in by_oc.items():
        w.append(f"### {oc} — answer: {ANSWER[oc]}\n")
        for kind, k in lst:
            ch = []
            for (dk, f), (v, why) in dec_by.items():
                if dk == k and ((oc == "OC-10" and k.endswith("011.5")) or (oc == "OC-11" and k.endswith("011.4"))):
                    old = next(l["SealedValue"] for l in log if l["ClaimKey"] == k and l["Field"] == f)
                    ch.append(f"`{f}`: `{old}` → `{v}` ({why})")
            for f, find, rep in fix_by.get((oc, k), []):
                ch.append(f"`{f}` correction: \"{find}\" → \"{rep}\" (text asserted the event did not happen)")
            ns = [n for n in notes[k] if f"{oc} " in n or f"{oc}," in n or n.startswith(f"OWNER_CHECK {oc}")]
            for n in ns:
                ch.append(f"`Notes+`: \"{n}\"")
            r = final[k]
            w.append(f"- `{k}` (rows {kind}; final {r['Disposition']}, HDN {r['HumanDecisionNeeded']})")
            for c in ch:
                w.append(f"  - {c}")
        w.append("")
    w.append("## Decided rows left `UNKNOWN`\n")
    und = [k for oc, lst in by_oc.items() for kind, k in lst if kind == "decided" and final[k]["Disposition"] == "UNKNOWN"]
    w.append(f"{len(und)} rows (OC-14, OC-18, OC-19, OC-20; answer don't know): " + ", ".join(f"`{k}`" for k in und) +
             ". Each carries the `OWNER_BELIEF` note only; Disposition, Confidence, RemainingWork, CauseTag and DirectionEvidence unchanged.\n")
    w.append("## Noted rows for R4 attention\n")
    w.append("Dispositions not changed (step 3). Each rested partly on absence of an event the owner now confirms:\n")
    for k, a, why in ATTENTION:
        w.append(f"- `{k}` ({a}): {why}")
    w.append("\nOther noted rows under yes/no answers: the Disposition rests on code or on records missing from the deliverable, which the "
             "answer does not change (OC-02 rows: the build record's location stays open; OC-04 `DEL-09-05#CLM-016.6`: the WP-11 record; "
             "OC-09 rows: the owner's 'no' agrees with the notes that a wider matrix is still open). Notes that still read "
             "`RELEASE_PROCESS_NOT_RUN:` under OC-08 and OC-14 (don't know) were left as written, per the brief.\n")
    w.append("## Checks\n")
    res = subprocess.run([sys.executable, os.path.join(HERE, "check_apply.py")], capture_output=True, text=True).stdout.strip().splitlines()
    for l in res:
        w.append(f"- {l}")
    for l in open(os.path.join(R3, "COVERAGE_AND_QA.md"), encoding="utf-8"):
        if l.startswith("| Q"):
            parts = [p.strip() for p in l.strip().strip("|").split("|")]
            w.append(f"- r3_qa {parts[0]}: {parts[1]}")
    w.append("\nNot rerun: `r3_owner_check.py`, `r3_clusters.py`, spot-check scripts.\n")
    w.append("## SHA-256 of rebuilt files\n")
    for f in ("CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv", "REVERSE_CONCORDANCE.csv", "REMAP_LOG.csv",
              "INPUT_MANIFEST.md", "COVERAGE_AND_QA.md", "R3_SUMMARY.md", "_work/SEALED_ROWS.csv", "_work/DEC_OWNERCHECK.csv"):
        w.append(f"- `{f}` `{sha256(os.path.join(R3, f))}`")
    with open(os.path.join(R3, "OWNER_CHECK_APPLIED.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(w) + "\n")


if __name__ == "__main__":
    main()
