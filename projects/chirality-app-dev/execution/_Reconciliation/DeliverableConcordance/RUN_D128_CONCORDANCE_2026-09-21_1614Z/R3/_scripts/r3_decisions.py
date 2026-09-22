#!/usr/bin/env python3
"""Convert TASK verdict files in R3/_work/ into the DEC_*.csv decision files that r3_build.py
applies. Deterministic; every decision cites its TASK file and rule. Re-runnable; a DEC file is
written only when its inputs exist.

DEC schema: ClaimKey,Field,NewValue,Source,RuleOrEvidence,Find,Replace
  Field = a ledger column (NewValue is the full new cell), `Notes+` (NewValue appended to Notes),
  `HDN_TOKENS` (NewValue = space-separated +TOKEN / -TOKEN operations on HumanDecisionNeeded), or a
  ledger column with Find/Replace (literal substring replacement, must occur exactly once).
"""
import os, sys
from r3lib import *

COLS = ["ClaimKey", "Field", "NewValue", "Source", "RuleOrEvidence", "Find", "Replace"]


def w(name, rows):
    write_csv(os.path.join(WORK, name), COLS, rows)
    print(name, len(rows))


def have(name):
    return os.path.exists(os.path.join(WORK, name))


def rd(name):
    return read_csv(os.path.join(WORK, name))[1]


def main():
    # --- run-wide reach calls (a), (b): T4A
    if have("T4A_REMAPS.csv"):
        out = []
        for r in rd("T4A_REMAPS.csv"):
            out.append({"ClaimKey": r["ClaimKey"], "Field": r["Field"], "Source": "R3_RUNWIDE",
                        "Find": r["Find"], "Replace": r["Replace"],
                        "RuleOrEvidence": f"RUNWIDE_CALLS.md ({r['Call']}) reach call; {r['Evidence'][:240]}"})
        w("DEC_RUNWIDE_REACH.csv", out)

    # --- R4-Q1 (Addendum 6 rule 3 + Addendum 8): script adds + T2 verdicts
    if have("DEC_R4Q1_SCRIPT.csv"):
        out = []
        for r in rd("DEC_R4Q1_SCRIPT.csv"):
            out.append(dict(r, Find="", Replace=""))
        if have("T2_R4Q1_VERDICTS.csv"):
            for r in rd("T2_R4Q1_VERDICTS.csv"):
                k, v = r["ClaimKey"], r["Verdict"]
                why = f"T2 {v}: {r['Basis'][:240]}"
                if v == "ADD":
                    out.append({"ClaimKey": k, "Field": "HDN_TOKENS", "NewValue": "+R4-Q1", "Source": "R3_RULE",
                                "RuleOrEvidence": "Addendum 6 rule 3 + Addendum 8; " + why})
                elif v == "DROP":
                    out.append({"ClaimKey": k, "Field": "HDN_TOKENS", "NewValue": "-R4-Q1", "Source": "R3_RULE",
                                "RuleOrEvidence": "Addendum 6 rule 3 (no LEGACY_ONLY code meets the claim; no other R4-Q1 reason); " + why})
                if r.get("TagFix") and "=>" in r["TagFix"]:
                    f_, rp = r["TagFix"].split("=>", 1)
                    out.append({"ClaimKey": k, "Field": "ImplementationEvidence", "Source": "R3_RULE",
                                "Find": f_, "Replace": rp, "RuleOrEvidence": "REACH tag fix found under rule 3; " + why})
                if r.get("AlsoModule"):
                    out.append({"ClaimKey": k, "Field": "Notes+", "NewValue": r["AlsoModule"], "Source": "R3_RULE",
                                "RuleOrEvidence": "Addendum 6 rule 4; " + why})
        w("DEC_R4Q1.csv", out)

    # --- Addenda 4, 7, 9: T1 plain R4 -> named questions
    if have("T1_R4QN_VERDICTS.csv"):
        out = []
        for r in rd("T1_R4QN_VERDICTS.csv"):
            old, new = hdn_tokens(r["OldHumanDecisionNeeded"]), hdn_tokens(r["NewHumanDecisionNeeded"])
            if old == new:
                continue
            ops = [f"-{t}" for t in old if t not in new] + [f"+{t}" for t in new if t not in old]
            add = {"R4-Q4": "Addendum 4", "R4-Q5": "Addendum 7", "R4-Q6": "Addendum 9"}
            cite = ", ".join(sorted({add[t[1:]] for t in ops if t[1:] in add})) or "Addenda 4/7/9"
            out.append({"ClaimKey": r["ClaimKey"], "Field": "HDN_TOKENS", "NewValue": " ".join(ops), "Source": "R3_RULE",
                        "RuleOrEvidence": f"{cite}: plain R4 mapped to the named question the row turns on (T1 {r['Question']}); {r['Basis'][:240]}"})
        w("DEC_R4QN.csv", out)

    # --- Addendum 5 tie-break: T5
    if have("T5_TIEBREAK_VERDICTS.csv"):
        out = []
        for r in rd("T5_TIEBREAK_VERDICTS.csv"):
            if r["Verdict"] != "MOVE":
                continue
            out.append({"ClaimKey": r["ClaimKey"], "Field": "Disposition", "NewValue": r["NewDisposition"],
                        "Source": "R3_RULE", "RuleOrEvidence": f"Addendum 5 tie-break (T5); {r['Basis'][:240]}"})
            note = f"R3_TIEBREAK(Addendum 5): sealed {r['CurrentDisposition']}"
            if r.get("AlsoNote"):
                note += f"; {r['AlsoNote']}"
            out.append({"ClaimKey": r["ClaimKey"], "Field": "Notes+", "NewValue": note, "Source": "R3_RULE",
                        "RuleOrEvidence": "Addendum 5 tie-break (T5)"})
        w("DEC_TIEBREAK.csv", out)

    # --- Addendum 10: T3
    if have("T3_ADD10_VERDICTS.csv"):
        out = []
        for r in rd("T3_ADD10_VERDICTS.csv"):
            v = r["Verdict"]
            if v not in ("REMAP_UNKNOWN", "NOTE_ONLY", "UNDECIDED"):
                continue
            why = f"Addendum 10 (T3 {v}, {r['EventGroup']}); {r['Evidence'][:200]}"
            if v == "REMAP_UNKNOWN":
                out.append({"ClaimKey": r["ClaimKey"], "Field": "Disposition", "NewValue": "UNKNOWN",
                            "Source": "R3_RULE", "RuleOrEvidence": why})
            tag = "OWNER_CHECK" if v != "UNDECIDED" else "OWNER_CHECK(R3 UNDECIDED: Disposition kept; two readings in T3_NOTES)"
            out.append({"ClaimKey": r["ClaimKey"], "Field": "Notes+", "NewValue": f"{tag}: {r['OwnerCheck']}",
                        "Source": "R3_RULE", "RuleOrEvidence": why})
        w("DEC_ADD10.csv", out)

    # --- run-wide disposition calls: T4B (c, d, f), T6 (e), T2B (subject test after reach calls)
    out = []
    base_hdn = {}
    if have("BASELINE_HDN.csv"):
        base_hdn = {r["ClaimKey"]: r["HumanDecisionNeeded"] for r in rd("BASELINE_HDN.csv")}
    for fname in ("T4B_REMAPS.csv", "T6_REMAPS.csv", "T2B_REMAPS.csv", "MGR_REMAPS.csv"):
        if not have(fname):
            continue
        for r in rd(fname):
            f = r["Field"]
            why = f"RUNWIDE_CALLS.md ({r['Call']}) via {fname}; {r['Evidence'][:240]}"
            if f == "HumanDecisionNeeded":
                # full-cell values were computed against the post-CORRECTIONS baseline: apply as token ops
                old, new = hdn_tokens(base_hdn[r["ClaimKey"]]), hdn_tokens(r["NewValue"])
                ops = [f"-{t}" for t in old if t not in new] + [f"+{t}" for t in new if t not in old]
                if ops:
                    out.append({"ClaimKey": r["ClaimKey"], "Field": "HDN_TOKENS", "NewValue": " ".join(ops),
                                "Source": "R3_RUNWIDE", "RuleOrEvidence": why})
            elif f == "HDN_TOKENS":
                out.append({"ClaimKey": r["ClaimKey"], "Field": f, "NewValue": r["NewValue"], "Source": "R3_RUNWIDE",
                            "RuleOrEvidence": why})
            else:
                out.append({"ClaimKey": r["ClaimKey"], "Field": f, "NewValue": r["NewValue"], "Source": "R3_RUNWIDE",
                            "RuleOrEvidence": why})
    if out:
        w("DEC_RUNWIDE.csv", out)

    # --- spot-check reverts: T8
    if have("T8_REVERTS.csv"):
        out = []
        for r in rd("T8_REVERTS.csv"):
            out.append({"ClaimKey": r["ClaimKey"], "Field": r["Field"], "NewValue": r["RevertTo"],
                        "Source": r["OriginalSource"],
                        "RuleOrEvidence": f"SPOT-CHECK REVERT (second REMAP_LOG pass): R3_SPOT_CHECK.md refuted the R3 re-mapping; {r['Evidence'][:240]}"})
        w("DEC_SPOTREVERT.csv", out)


if __name__ == "__main__":
    main()
