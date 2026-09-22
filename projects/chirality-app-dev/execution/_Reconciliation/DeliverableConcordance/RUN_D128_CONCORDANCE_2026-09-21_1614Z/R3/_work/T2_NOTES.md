# T2 notes: R4-Q1 on rows the REACH-tag script cannot decide

Input: `R3/_work/CAND_R4Q1_TASK.csv`, 105 rows (46 `ADD?`, 59 `KEEP?`). Output: `R3/_work/T2_R4Q1_VERDICTS.csv`.
Script: `R3/_work/T2_scripts/t2_verdicts.py`. It records the verdicts and checks three things: each TagFix Find occurs exactly once in the current cell, each added module is LEGACY_ONLY in `REACHABILITY.csv` (or symbol-level, as noted below), and no ALSO_MODULE is added where Notes already have one.

## Counts
- ADD? (46): ADD 14, NO_ADD 32.
- KEEP? (59): KEEP_RULE3 42 (each with a TagFix), KEEP_OTHER 10, DROP 5, UNDECIDED 2.
- ALSO_MODULE notes proposed: 6 (5 on ADD rows, 1 on KEEP_RULE3 DEL-04-05#CLM-004).

## Patterns
- **ADD? on STALE_SPECIFICATION TBD/status rows → NO_ADD.** Most ADD? rows are STATE_ASSERTION or CONTEXT_CLAIM rows that say "path/record TBD". There the legacy code shows the TBD is false. It does not meet the claim.
  - The same applies where legacy code contradicts the claim: the Pi adapter against the Pi exclusion, the numeric contractVersion, and the OpenPipeStress registration.
  - It also applies to exclusions that hold by absence on the live path as well (no `/api/domain` routes).
- **ADD** where legacy code is the only non-test code for a substantive part of the claim. Examples: resolver construction and shape (DEL-06-02 CLM-005, 014, 026), the v7 coordination policy, the seven-name UIEvent output, adapter-metadata failure details, `turn.cancelled` on disconnect, the shell timeout line, the PEC registry entry and the ADDING_A_TOOL primary sources.
  - A stated part that is true only of legacy code also counts (DEL-06-05#CLM-019.1, DEL-06-06#CLM-018).
- **KEEP? verification rows → KEEP_RULE3.** Most KEEP? rows are test or verification rows. The row text says the tests exercise legacy code ("over LEGACY_ONLY modules", "legacy overlay tests", "exercise LEGACY_ONLY modules") but gives the module no REACH tag, so the script sees only TEST_ONLY.
  - Each TagFix adds the modules the cited tests import, checked in the frozen tree, as `REACH=LEGACY_ONLY`. This follows the existing DEL-05-05#CLM-010.10 form ("… REACH=TEST_ONLY exercising X REACH=LEGACY_ONLY").
- **KEEP_OTHER** where the row gives its own R4-Q1 reason: history or obligation of the retained credential store, register rows citing legacy surfaces, the settingSources condition, K-HOOK/K-PERM/SPEC §15.2 conflicts unamended for D-GOV-43, and "whether those requirements are history or obligation".
- **DROP** (5): no legacy code and no stated R4-Q1 reason.
  - DEL-01-02#CLM-016, DEL-04-02#STATE-1, DEL-06-05#CLM-009.11, DEL-06-05#CLM-019.2 → `NO`.
  - DEL-06-06#STATE-1 → `R4; R4-Q6`.
## R3 build finding (lost tags)
Three KEEP? rows appear only because a verifier CORRECTION replaced a whole ImplementationEvidence cell with prose. The CorrectedValue dropped the sealed LEGACY_ONLY citations, although its text said "R4-Q1 … hold".
- DEL-04-05#CLM-004: `sdk-options-builder.ts:30-33,248`.
- DEL-04-05#CLM-012: `anthropic-agent-sdk-manager.ts`.
- DEL-05-05#CLM-003: `tool-result-artifacts.ts:58-139`. Here every path is lost; the cell is now verifier prose only (`R2/PKG-05/CORRECTIONS.csv`, `R3/REMAP_LOG.csv`).
The TagFixes restore the legacy citation only. The manager may want to check the other CORRECTION remaps for the same whole-cell loss.
## Symbol-level tags and references
- DEL-05-01#CLM-016 and #CLM-024 add `session-manager.ts` (module LIVE in `REACHABILITY.csv`) as `REACH=LEGACY_ONLY`. This is symbol-level: FileSessionManager is constructed only by LEGACY_ONLY `runtime.ts:158`, as DEL-05-01#CLM-010.4 already tags it.
- DEL-08-03#CLM-015 and #CLM-019.1, and DEL-06-06#CLM-020, add legacy paths by reference to their sibling rows (CLM-013.11 and CLM-015.1).
## UNDECIDED (HDN left unchanged)
- DEL-04-04#CLM-024. The principles name SDK mechanisms that only legacy code provides (KEEP), but LIVE `runtime-method-service.ts` meets them in substance (DROP).
- DEL-04-05#CLM-024 (AUTHORITY_CONFLICT). There are two readings:
  - KEEP: the Claude substrate as retained-harness obligation.
  - DROP: the row turns on the unamended DIRECTIVE §2.8, which is R4-Q6 scope. But DROP would leave AUTHORITY_CONFLICT with `NO`.
## Not decided here
- DEL-06-02#CLM-005 is owner-deferred (Addendum 5). ADD adds only the R4-Q1 token, which worker B already cites; the Disposition is untouched.
- Disposition changes on rows that lost LIVE tags are left to the other task.
