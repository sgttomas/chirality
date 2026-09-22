#!/usr/bin/env python3
"""T1 (R4 step 1): write R3/_work/DEC_OWNERCHECK.csv from the owner-check answers (RUN_BASIS
Addendum 13). Row judgements are listed explicitly below; the per-OC note appends are generated
for every row OWNER_CHECK.md lists. Deterministic."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
from r3lib import *
from dump_rows import oc_rows

SRC = "OWNER_CHECK"
A13 = "RUN_BASIS Addendum 13"
ANSWER = {**{f"OC-{i:02d}": "yes" for i in list(range(1, 8)) + [10, 11, 12]},
          "OC-08": "don't know", "OC-09": "no",
          **{f"OC-{i:02d}": "don't know" for i in range(13, 21)}}

# Field decisions on decided rows with a yes/no answer (judged against the frozen claim text,
# DEL-09-04 ScopeOfWork.md CLM-011 verification table: "The verification package should include ...").
DECIDED = [
    ("DEL-09-04#CLM-011.5", "Disposition", "PARTIALLY_IMPLEMENTED",
     "OC-10 yes: the arm64 inspection happened (owner testimony). The claim requires the verification package to "
     "include the inspected architecture; the build record states arm64 identity (BUILD_EVIDENCE_RELEASE_20260913.md:12) "
     "but no inspection output is kept in the deliverable evidence or the AgentRuns records at the frozen basis."),
    ("DEL-09-04#CLM-011.4", "Disposition", "PARTIALLY_IMPLEMENTED",
     "OC-11 yes: the LSMinimumSystemVersion inspection happened (owner testimony). The claim requires the verification "
     "package to include the inspected value; configuration pins 15.0.0 (frontend/package.json:158) but no inspected "
     "value is kept in the deliverable evidence or the AgentRuns records at the frozen basis."),
    ("DEL-09-04#CLM-011.4", "RemainingWork",
     "Record the LSMinimumSystemVersion inspection (owner testimony OC-11) in the verification package for the candidate bundle",
     "OC-11 yes: the inspection happened; the residual is the kept record, not the inspection."),
]
DECIDED_NOTE = {
    "DEL-09-04#CLM-011.5": "Disposition set from the answer and the claim: event confirmed, inspected record not kept in the "
                           "verification package; ALSO:UNKNOWN on the record part if a record is kept outside the evidence roots.",
    "DEL-09-04#CLM-011.4": "Disposition set from the answer and the claim: event confirmed, inspected value not kept in the "
                           "verification package; ALSO:UNKNOWN on the record part if a record is kept outside the evidence roots.",
}

# Corrections of text that asserted the event did not happen, in light of a yes/no answer.
FIXES = [
    ("OC-03", "DOC:BUILDREL#9.3", "Notes",
     "RELEASE_PROCESS_NOT_RUN:notarization of v3.0.1 - package.json",
     "v3.0.1 notarization: owner testimony that it was notarized and stapled (OC-03); no record in the evidence roots - package.json"),
    ("OC-05", "DEL-09-05#CLM-010.8", "Notes",
     "desktop:dist ran only in the recorded 2026-09-12 build (agent record)",
     "desktop:dist runs are recorded for the 3.0.0-rc.1 and 3.0.0 builds (agent records, 2026-09-12 and 2026-09-13), none for 3.0.1; "
     "owner testimony (OC-05) that the full set incl. desktop:dist passed before v3.0.0 and v3.0.1 were accepted"),
    ("OC-06", "DEL-09-01#CLM-009.8", "Notes",
     "the last passing run (revision 3, stub adapter, daemon) predates the A2 re-platform",
     "the last recorded passing run (revision 3, stub adapter, daemon) predates the A2 re-platform; owner testimony (OC-06) that a Section 8 pass against the Codex-hosted Runtime was run since"),
    ("OC-06", "DEL-09-01#CLM-009.8", "VerificationEvidence",
     "NONE_FOUND (no Section 8 run at or after 39c0bb6ab)",
     "NONE_FOUND (no Section 8 run recorded at or after 39c0bb6ab)"),
    ("OC-06", "DEL-09-01#CLM-023", "Notes",
     "(no summary; last run 2026-09-04)",
     "(no summary; last recorded run 2026-09-04; owner testimony OC-06 of a later run)"),
]


def main():
    out = []
    for k, f, v, why in DECIDED:
        out.append({"ClaimKey": k, "Field": f, "NewValue": v, "Source": SRC, "RuleOrEvidence": f"{A13}; {why}"})
    for oc, k, f, find, rep in FIXES:
        out.append({"ClaimKey": k, "Field": f, "NewValue": "", "Source": SRC,
                    "RuleOrEvidence": f"{A13}; {oc} {ANSWER[oc]}: text asserted the event did not happen; corrected to a record statement",
                    "Find": find, "Replace": rep})
    seen = set()
    for oc, kind, k in oc_rows():
        n = int(oc[3:])
        a = ANSWER[oc]
        if oc == "OC-08":
            note = f"OWNER_CHECK OC-08: don't know (owner does not recognise the terms; {A13})"
        elif n >= 13:
            note = f"OWNER_BELIEF: likely performed if the instructions called for it ({oc}, {A13})"
        else:
            note = f"OWNER_TESTIMONY: {oc} {a} ({A13})"
        if k in DECIDED_NOTE and n in (10, 11):
            note += ". " + DECIDED_NOTE[k]
        if (k, note) in seen:
            continue
        seen.add((k, note))
        out.append({"ClaimKey": k, "Field": "Notes+", "NewValue": note, "Source": SRC,
                    "RuleOrEvidence": f"{A13}; {oc} ({'rows decided' if kind == 'decided' else 'rows noted'}) answer: {a}"})
    write_csv(os.path.join(WORK, "DEC_OWNERCHECK.csv"),
              ["ClaimKey", "Field", "NewValue", "Source", "RuleOrEvidence", "Find", "Replace"], out)
    print(len(out), "decision lines")


if __name__ == "__main__":
    main()
