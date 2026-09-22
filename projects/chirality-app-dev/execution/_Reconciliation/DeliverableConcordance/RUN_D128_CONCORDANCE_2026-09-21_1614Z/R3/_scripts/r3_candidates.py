#!/usr/bin/env python3
"""Build R3 candidate lists from the post-errata/post-corrections concordance (run before any
_work/DEC_*.csv exists, or with --pre to ignore them). Deterministic keyword and tag screens.

Outputs in R3/_work/:
  DEC_R4Q1_SCRIPT.csv   script-decided R4-Q1 additions (Addendum 6 rule 3 + Addendum 8)
  CAND_R4Q1_TASK.csv    rows the script cannot decide (TASK)
  CAND_R4PLAIN.csv      plain R4 rows (Addenda 4, 7, 9 classification; TASK)
  CAND_TIEBREAK.csv     Addendum 5 tie-break candidates (TASK)
  CAND_ADD10.csv        Addendum 10 candidates (TASK)
"""
import os, re, sys, collections
from r3lib import *

PKG09_S8 = """DEL-09-04#CLM-005 DEL-09-04#CLM-011.1 DEL-09-04#CLM-011.2 DEL-09-04#CLM-011.3 DEL-09-04#CLM-011.7
DEL-09-04#CLM-012.1 DEL-09-04#CLM-018 DEL-09-04#CLM-011.5 DEL-09-04#CLM-009.8 DEL-09-04#CLM-011.8 DEL-09-04#CLM-017
DEL-09-04#REM-1 DEL-09-05#CLM-010.8 DEL-09-05#CLM-010.9 DEL-09-05#CLM-010.15 DEL-09-05#CLM-016.5 DEL-09-05#CLM-016.6
DEL-09-05#CLM-021 DEL-09-05#CLM-022 DEL-09-05#CLM-023.1 DEL-09-05#CLM-016.3 DEL-09-05#CLM-026 DEL-09-04#CLM-022
DEL-09-04#CLM-023.3 DEL-09-01#CLM-011 DEL-09-01#CLM-009.8 DEL-09-01#REM-1 DEL-09-02#CLM-020.2 DEL-09-06#CLM-016
DEL-09-06#CLM-021 DEL-09-06#CLM-014""".split()
EXT_RELEASE_NOT_RUN = """DOC:BUILDREL#1 DOC:BUILDREL#4.7 DOC:BUILDREL#7.4 DOC:BUILDREL#9.3 DOC:BUILDREL#9.5
DOC:BUILDREL#11 DOC:BUILDREL#12 DOC:RQGATES#12 DOC:VALSTRAT#4.7 DOC:VALSTRAT#4.11 DOC:VALSTRAT#7 DOC:VALSTRAT#8
DOC:RELIANCE#3.2 DOC:RELIANCE#8 DOC:RELIANCE#11.1""".split()
RELEASE_DOC_PREFIX = ("DOC:BUILDREL#", "DOC:RQGATES#", "DOC:RQRUN#", "DOC:VALSTRAT#", "DOC:RELIANCE#")

EVENT = re.compile(r"notari[sz]|\bsign(ed|ing|ature)?\b|unsigned|stapl|publish|release (job|run|act|execution|workflow)|"
                   r"\bCI\b|premerge run|pre-merge run|attestation|SBOM|manual(ly)? (step|check|review|test)|checklist|"
                   r"\bran\b|was run|were run|been run|executed|performed|build record|\bDMG\b|proof run|"
                   r"credential(ed)? (operation|step)|upload|tag(ged)? v?\d|owner('s)? (act|approval|sign-off)|human (step|gate|approval|review)", re.I)
ABSENT = re.compile(r"never (ran|run|executed|performed|recorded|published|signed|notarized)|not (been )?(run|ran|performed|executed|recorded|notarized|signed|published|attested)\b|"
                    r"no (record|evidence|run|transcript|log|trace)|unrecorded|without (a )?record|no .{0,40} (recorded|found|exists)|"
                    r"NONE_FOUND", re.I)
FIELDS = ["DeclaredState", "ImplementationEvidence", "VerificationEvidence", "RemainingWork", "Notes"]
DIVERGENT_Q1_SCRIPT = {"ALIGNED", "PARTIALLY_IMPLEMENTED"}
NO_MEET = {"DOCUMENTED_UNIMPLEMENTED", "NOT_AUDITABLE", "RETIRED_BY_RULING"}


def main():
    rows = read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1] + read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]
    q1s, q1t, plain, tb, a10 = [], [], [], [], []
    for r in rows:
        k = r["ClaimKey"]
        toks = hdn_tokens(r["HumanDecisionNeeded"])
        tags = set(reach_tags(r["ImplementationEvidence"]))
        legacy_only = "LEGACY_ONLY" in tags and "LIVE" not in tags
        d = r["Disposition"]
        # --- R4-Q1
        if legacy_only and "R4-Q1" not in toks and d not in NO_MEET:
            if d in DIVERGENT_Q1_SCRIPT:
                q1s.append({"ClaimKey": k, "Field": "HDN_TOKENS",
                            "NewValue": "+R4-Q1", "Source": "R3_RULE",
                            "RuleOrEvidence": f"Addendum 6 rule 3 + Addendum 8: ImplementationEvidence REACH tags {sorted(tags)} (no LIVE); Disposition {d} means the cited code meets the claim in whole or part"})
            else:
                q1t.append(dict(r, Question="ADD?", Why=f"legacy-only REACH tags {sorted(tags)}; Disposition {d}: does LEGACY_ONLY code meet (part of) the claim?"))
        if "R4-Q1" in toks and "LEGACY_ONLY" not in tags:
            q1t.append(dict(r, Question="KEEP?", Why=f"cites R4-Q1 but REACH tags {sorted(tags) or 'none'}: is the claim met only by LEGACY_ONLY (non-test) code, or does the row cite R4-Q1 for another reason?"))
        # --- plain R4
        if "R4" in toks:
            plain.append(r)
        # --- tie-break (Addendum 5)
        if k not in DB_B_KEYS:
            is_rem = r["ClaimType"] == "REMAINING_WORK" or "#REM-" in k or "#REMTXT-" in k
            if d == "STALE_SPECIFICATION" and is_rem:
                tb.append(dict(r, Why="STALE_SPECIFICATION on a Remaining item / REMAINING_WORK row (rule 2a points to REMAINING_STATE_MISMATCH when its open/done status is contradicted)"))
            elif d == "REMAINING_STATE_MISMATCH" and not is_rem and r["ClaimType"] != "REGISTER_DEFECT":
                tb.append(dict(r, Why="REMAINING_STATE_MISMATCH on a non-Remaining, non-register row (rule 1 points to STALE_SPECIFICATION for a present fact now false; rule 2b keeps RSM only for register bookkeeping)"))
            elif d == "REMAINING_STATE_MISMATCH" and r["ClaimType"] == "REGISTER_DEFECT" and re.search(r"MATCH|SATISFIED|exist|current", r["Notes"] + r["DeclaredState"]):
                tb.append(dict(r, Why="REGISTER_DEFECT with RSM whose text may assert a now-false fact (MATCH/SATISFIED/exists/current): rule 1 vs 2b"))
            elif d == "STALE_SPECIFICATION" and r["ClaimType"] == "REGISTER_DEFECT" and re.search(r"Last Updated|TBD|lagging|placeholder|date", r["Notes"] + r["DeclaredState"], re.I) and not re.search(r"MATCH", r["Notes"] + r["DeclaredState"]):
                tb.append(dict(r, Why="REGISTER_DEFECT with SS that may be bookkeeping lag only (rule 2b)"))
        # --- Addendum 10
        reasons = []
        if k in PKG09_S8:
            reasons.append("PKG-09 PACKAGE_SUMMARY §8 OWNER_CHECK candidate")
        if k in EXT_RELEASE_NOT_RUN:
            reasons.append("EXT_SUMMARY §5 RELEASE_PROCESS_NOT_RUN")
        if k.startswith(RELEASE_DOC_PREFIX) and d not in ("ALIGNED", "NOT_AUDITABLE"):
            text = " ".join(r[f] for f in FIELDS)
            if EVENT.search(text):
                reasons.append("EXT release-doc row with event wording")
        if d not in ("ALIGNED", "NOT_AUDITABLE", "UNKNOWN", "RETIRED_BY_RULING"):
            text = " ".join(r[f] for f in FIELDS)
            ev, ab = EVENT.search(text), ABSENT.search(text)
            if ev and ab and ("NONE_FOUND" not in ab.group(0) or r["ImplementationEvidence"].startswith("NONE_FOUND") or r["VerificationEvidence"].startswith("NONE_FOUND")):
                reasons.append(f"keyword screen: event '{ev.group(0)}' + absence '{ab.group(0)}'")
        if d == "UNKNOWN" and "OWNER_CHECK" in r["Notes"]:
            reasons.append("already UNKNOWN with OWNER_CHECK (sealed after Addendum 10)")
        if reasons:
            a10.append(dict(r, Why="; ".join(reasons)))

    cand_cols = ["ClaimKey", "PackageID", "DeliverableID", "ClaimType", "NormativeSource", "DeclaredState",
                 "ImplementationEvidence", "VerificationEvidence", "Disposition", "CauseTag",
                 "HumanDecisionNeeded", "RemainingWork", "Notes", "AltReading"]
    write_csv(os.path.join(WORK, "DEC_R4Q1_SCRIPT.csv"), ["ClaimKey", "Field", "NewValue", "Source", "RuleOrEvidence"], q1s)
    write_csv(os.path.join(WORK, "CAND_R4Q1_TASK.csv"), ["Question", "Why"] + cand_cols, q1t)
    if "--only-r4q1" in sys.argv:
        print("R4Q1 script adds", len(q1s), "| R4Q1 task", collections.Counter(x["Question"] for x in q1t))
        return
    write_csv(os.path.join(WORK, "CAND_R4PLAIN.csv"), cand_cols, plain)
    write_csv(os.path.join(WORK, "CAND_TIEBREAK.csv"), ["Why"] + cand_cols, tb)
    write_csv(os.path.join(WORK, "CAND_ADD10.csv"), ["Why"] + cand_cols, a10)
    print("R4Q1 script adds", len(q1s), "| R4Q1 task", collections.Counter(x["Question"] for x in q1t),
          "| plain R4", len(plain), "| tiebreak", len(tb), "| add10", len(a10))
    print("add10 by pkg", collections.Counter(x["PackageID"] for x in a10))
    print("tb by pkg", collections.Counter(x["PackageID"] for x in tb))


if __name__ == "__main__":
    main()
