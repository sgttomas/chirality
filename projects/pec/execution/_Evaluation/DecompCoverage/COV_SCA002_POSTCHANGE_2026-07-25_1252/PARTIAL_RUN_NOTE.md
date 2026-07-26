# PARTIAL RUN — contract-incomplete by construction

**This snapshot is NOT a conformant `AUDIT_DECOMP` run.** It carries 3 of the
8 artifacts the `AGENT_AUDIT_DECOMP.md` STRUCTURE contract requires
(`coverage_summary.json`, `Decomp_Coverage_IssueLog.csv`,
`Decomp_Coverage_Matrix.csv`). `Brief.md`, `RUN_SUMMARY.md`, `QA_Report.md`,
`Decision_Log.md` and `Decomp_Coverage_Report.md` are absent and are
**deliberately not backfilled** — writing them after the fact would fabricate
narrative for a run that was halted.

## What this is

The **aborted first-pass** post-change audit from SCA-002 Gate 5, step 12. It
returned `RUN_STATUS = BLOCKERS` with a single blocker:

```
COV-074, Check 10, BLOCKER: Active snapshot contract failed —
missing ['Post_Change_Coverage.json', 'Handoff_State.md', 'RUN_SUMMARY.md']
```

## Why it is retained

It is evidence of a real defect, not of a problem with the amendment. The
SCA-002 propagation plan (v2) ordered the audit *after* the
`_ScopeChange/_LATEST.md` repoint so Check 10 would validate SCA-002's
snapshot — but Check 10 requires the complete artifact set, and
`Post_Change_Coverage.json` / `Handoff_State.md` / `RUN_SUMMARY.md` are written
*after* the audit (`Post_Change_Coverage.json` cannot precede it, because it
cites the audit's output). The first pass could therefore never pass Check 10.

Gate 5 aborted here rather than improvising. Agent 0 dispositioned
propagation-plan amendment **v2.1: two-pass audit**. Deleting this snapshot to
tidy the record would erase the trace of the ordering defect that produced the
amendment.

## Status

**SUPERSEDED** for all closure purposes by
`COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257` (`RUN_STATUS = OK`, 0 blockers,
0 warnings, Check 10 `PASS`), which is contract-complete.

This snapshot is cited in `Post_Change_Coverage.json.audit_decomp` as
first-pass register/coverage evidence; the final run is cited in
`audit_decomp_final`. Its register and coverage numbers are valid — only the
Check 10 verdict is an artifact of the ordering.
