## 8. Manager's notes (hand-written)

**How the final values were built.** Precedence is applied by script (`_scripts/r3_build.py`) in this order:
1. the sealed ledger of record;
2. errata. Two DEL-09-03 errata were rejected by CORRECTIONS, so their sealed values stand;
3. CORRECTIONS;
4. R3 re-mappings, in order:
   - run-wide reach calls (a) and (b);
   - R4-Q1 re-derivation under Addendum 6 rule 3 and Addendum 8 (91 rows by script, the rest by T2);
   - plain R4 mapped to R4-Q4, R4-Q5 or R4-Q6 (T1);
   - the Addendum 5 tie-break (T5);
   - Addendum 10 owner checks (T3);
   - run-wide disposition calls (c) to (f) (T4B, T6, T2B, and three manager consistency fixes).

Every step is a REMAP_LOG line. The QA replay rebuilds the final census from the sealed census.

Some CORRECTIONS values are prose rather than a field value. For evidence cells, that prose is appended to the sealed cell instead of replacing it, so no sealed citation is lost. T2 flagged three cells where an earlier build had lost citations. The rule was fixed before the final build.

**Open contested items (carried to R4; R3 did not resolve them).**
- **Owner-deferred:** DEL-06-02#CLM-005 and #CLM-032. Both workers' verdicts are in `AltReading` (CL-01).
- **Sealed AUTHORITY_CONFLICT rows the verifiers read as needing no owner decision:** DEL-09-04#CLM-022, #CLM-023.3 and DEL-06-04#STATE-2. R3 kept the Disposition and restored `R4` for MR-11 consistency (CL-03 and CL-04 notes).
- **"Claude/Anthropic default" statement:** AUTHORITY_CONFLICT on 11 rows and STALE_SPECIFICATION on 23. Both readings are in Notes (call d, ED).
- **R4-Q6 scope, narrow or broad:**
  - Narrow means the listed clauses. Broad means DIRECTIVE versus D-GOV-43 generally, including K-PERM-3/4/5, K-NET-1 and DIRECTIVE §8.
  - About 13 T1 rows and about 70 T4B "adjacent" rows depend on which reading applies.
  - The spot check found 4 Full-access rows that lack R4-Q6.
- **Spot check:** 12 sealed values were refuted and 11 items were left UNDECIDED (`R3_SPOT_CHECK.md`). None of those values came from an R3 re-mapping, so R3 reverted nothing.
- **Items the R3 tasks left undecided:**
  - DEL-09-05#CLM-010.8: Addendum 10 (OC-05);
  - DEL-04-01#CLM-004.2 and DEL-06-06#STATE-2: tie-break;
  - DEL-06-03#CLM-010.4: subject test;
  - DEL-04-04#CLM-024 and DEL-04-05#CLM-024: R4-Q1.
  - Current values stand, and both readings are in the task files.
- **Rule 2b reading behind 9 tie-break moves:** T5 read rule 2b as covering text that is false only about the register itself. Nine moves to REMAINING_STATE_MISMATCH rest on that reading. The manager accepted it; the owner may reverse it.

**What R3 could not resolve.**
- **Rule 3 on mixed evidence:** a claim can be judged whole or part by part when live code meets part of it. 428 rows carry both LIVE and LEGACY_ONLY tags and keep their sealed R4-Q1.
- **Reach, two readings:** the evidence pack reads module-level; R3 call (a) reads symbol-level. R3 applied symbol-level. REACHABILITY.csv is unchanged.
- **Call (c):** the D-GOV-16 conversion records sit in Root `execution/`, outside the evidence roots. So 16 VER-001 rows stay UNKNOWN pending the owner (OC-20). Nine AC-001 ALIGNED rows had no parity recompute.
- **Call (g):** the RUN_BASIS §5 flags for D-APP-104, 107, 122 and 123 are stale, because their effects landed. This is recorded as a finding; RUN_BASIS belongs to HELP_HUMAN. D-APP-125 item 3 and D-APP-126 are retired by D-APP-127, not pending.
- **Regex-built key lists:** XPF-020, -022, -048 and -050 list keys found by regex. They are candidates, not reviewed row by row.
- **Validator scope:** `_scripts/validate_ledger.py` validates per-deliverable ledger files. It does not apply to the merged concordance, which has 5 extra columns. Its checks are covered in `COVERAGE_AND_QA.md`.

**Owner check applied (R4 step 1).** The owner's answers (RUN_BASIS Addendum 13) were applied through `_work/DEC_OWNERCHECK.csv` (Source `OWNER_CHECK`, appended after all R3 lines in `REMAP_LOG.csv`). Two decided rows moved from `UNKNOWN`; every listed row carries an `OWNER_TESTIMONY`, `OWNER_BELIEF` or OC-08 note; `don't know` rows stay `UNKNOWN`. Row-by-row changes, noted rows for R4 attention and checks: `OWNER_CHECK_APPLIED.md`.
