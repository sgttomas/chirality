#!/usr/bin/env python3
"""Build R3/R3_SPOT_CHECK.md from T8A/T8B/T8C verdicts. A REFUTED item whose checked value came from an
R3 re-mapping (R3_RULE/R3_RUNWIDE on that field) is written to _work/T8_REVERTS.csv for the second
REMAP_LOG pass; refutations of sealed/errata/corrected values are carried to R4 as contested items."""
import os, collections
from r3lib import *
log = read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1]
items = []
for t in ("T8A", "T8B", "T8C"):
    for x in read_csv(os.path.join(WORK, f"{t}_VERDICTS.csv"))[1]:
        items.append(dict(x, Task=t))
def cls(s): return s["SampleID"][:2]
reverts, contested = [], []
for x in items:
    f = x["CheckField"].split("+")[0]
    r3 = [l for l in log if l["ClaimKey"] == x["ClaimKey"] and l["Field"] == f and l["Source"].startswith("R3")]
    x["R3Origin"] = "YES" if r3 else "NO"
    if x["Verdict"] == "REFUTED":
        if r3:
            reverts.append({"ClaimKey": x["ClaimKey"], "Field": f, "RevertTo": r3[0]["SealedValue"],
                            "OriginalSource": r3[-1]["Source"], "Evidence": x["Evidence"]})
        else:
            contested.append(x)
write_csv(os.path.join(WORK, "T8_REVERTS.csv"), ["ClaimKey", "Field", "RevertTo", "OriginalSource", "Evidence"], reverts)
c = collections.Counter((cls(x), x["Verdict"]) for x in items)
tot = collections.Counter(x["Verdict"] for x in items)
S = {"S1": "S1 stratified ~5% sample (Disposition)", "S2": "S2 AUTHORITY_CONFLICT + UNKNOWN rows (Disposition and HDN)", "S3": "S3 R3 re-mappings"}
nrows = {k: len({x["ClaimKey"] for x in items if cls(x) == k}) for k in S}
out = ["# R3 independent spot check — RUN_D128_CONCORDANCE_2026-09-21_1614Z", "",
       "Three fresh TASK workers (T8A, T8B, T8C; Opus), blind to REMAP_LOG, the run-wide write-ups, the R3 task files and the "
       "Notes column, rechecked a deterministic stratified sample of the final concordance against the frozen tree "
       "(`_scripts/r3_spot_sample.py`; verdicts in `_work/T8A_VERDICTS.csv`, `T8B_VERDICTS.csv`, `T8C_VERDICTS.csv`; notes in "
       "`_work/T8*_NOTES.md`). Verdicts: CONFIRMED, REFUTED, UNVERIFIABLE; the workers also used UNDECIDED where both readings stay "
       "defensible (recorded as such, not forced).", "", "<!-- SUMMARY -->",
       f"- Items checked: {len(items)} over {sum(nrows.values())} row-samples — S1 {nrows['S1']} rows (5.0% of 3,568, stratified by package × Disposition); "
       f"S2 {nrows['S2']} of 194 AUTHORITY_CONFLICT/UNKNOWN rows (all 40 mandatory + 25 in order; at least 20 required); S3 {nrows['S3']} REMAP_LOG entries.",
       f"- Totals: CONFIRMED {tot['CONFIRMED']}, REFUTED {tot['REFUTED']}, UNDECIDED {tot['UNDECIDED']}, UNVERIFIABLE {tot['UNVERIFIABLE']}.",
       f"- S3 re-mappings: CONFIRMED {c[('S3','CONFIRMED')]}, REFUTED {c[('S3','REFUTED')]}, UNDECIDED {c[('S3','UNDECIDED')]}. "
       f"Refuted items whose checked value came from an R3 re-mapping: {len(reverts)} → second REMAP_LOG pass reverts {len(reverts)}.",
       f"- {len(contested)} refutations hit sealed (or errata/corrected) values that R3 did not re-map; they are not changed by R3 and are carried to R4 as contested items (table below).",
       "<!-- /SUMMARY -->", "", "## Counts by sample class", "", "| Class | Rows | CONFIRMED | REFUTED | UNDECIDED | UNVERIFIABLE |", "|---|---:|---:|---:|---:|---:|"]
for k, v in S.items():
    out.append(f"| {v} | {nrows[k]} | {c[(k,'CONFIRMED')]} | {c[(k,'REFUTED')]} | {c[(k,'UNDECIDED')]} | {c[(k,'UNVERIFIABLE')]} |")
out += ["", "S1 Disposition refutation rate: " + f"{c[('S1','REFUTED')]}/{nrows['S1']} ({100*c[('S1','REFUTED')]/nrows['S1']:.1f}%).", "",
        "## REFUTED items", "", "| Sample | ClaimKey | Field | Checked | Proposed | R3 re-mapped this field? | Handling | Evidence |", "|---|---|---|---|---|---|---|---|"]
for x in items:
    if x["Verdict"] == "REFUTED":
        h = "REVERTED (second pass)" if x["R3Origin"] == "YES" else "CONTESTED → R4 (sealed value kept)"
        out.append(f"| {x['SampleID']} | `{x['ClaimKey']}` | {x['CheckField']} | {x['CheckedValue']} | {x['ProposedValue']} | {x['R3Origin']} | {h} | {x['Evidence'][:260].replace('|','/')} |")
out += ["", "## UNDECIDED items (both readings kept; carried to R4)", "", "| Sample | ClaimKey | Field | Checked | Readings / note |", "|---|---|---|---|---|"]
for x in items:
    if x["Verdict"] == "UNDECIDED":
        out.append(f"| {x['SampleID']} | `{x['ClaimKey']}` | {x['CheckField']} | {x['CheckedValue']} | {(x['ProposedValue'] + ' — ' + x['Evidence'])[:260].replace('|','/')} |")
out += ["", "## Systematic observations from the checkers", "",
        "- K-ENGINE-4 restatements that diverge only through D-GOV-43 upstream-event pass-through are dispositioned IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED with R4-Q5 on some rows and AUTHORITY_CONFLICT on others (T8A; bears on CL-05).",
        "- R4-Q6 is applied unevenly to \"Full access\" and DIRECTIVE §2.8 rows that also cite R4-Q1 (T8C: 4 rows lack R4-Q6; bears on CL-04; T4B listed ~70 adjacent K-ROOT/K-PATH rows it did not move).",
        "- Rule 3 (R4-Q1) is read part-by-part on rows with both LIVE and LEGACY_ONLY evidence; the rulebook does not say whether a claim is judged whole or by part (T8B; 12 sample rows; bears on CL-09).",
        "- The R3 reach re-tags follow the capability files' symbol-level reading and now differ from the evidence pack's module-level REACHABILITY.csv (T8C; recorded in RUNWIDE_CALLS (a)).",
        "- Event-name rows citing only revised SPEC §11 / TYPES §7.4 (DEL-02-05#CLM-011.3, #CLM-003.2) read as ALIGNED to the checker, against sealed AUTHORITY_CONFLICT + R4-Q5.", ""]
open(os.path.join(R3, "R3_SPOT_CHECK.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(tot, "reverts", len(reverts), "contested", len(contested))
