# DOC-ADDING_A_TOOL notes (RUN_D128 R2 EXT, item 7, audit-only)

Ledger: `DOC-ADDING_A_TOOL_claims.csv`, 8 rows, validator `RESULT PASS errors=0 warnings=0`. This ledger is audit-only (CONVENTIONS §8): nothing is repaired by this run.

## 1. Census

STATE_ASSERTION 8: ALIGNED 2 (#2, #7); STALE_SPECIFICATION 2 (#0, #1); ACCEPTED_DIVERGENCE 4 (#3-#6). Split rate 0/8. SEE rows 0. No errata. R4-Q1 on 5 rows (#1, #3-#6).

## 2. Least-confident rows

- `DOC:ADDING_A_TOOL#3` (LOW, ACCEPTED_DIVERGENCE). Alternative: IMPLEMENTED_DIFFERENTLY. The body states the SDK enforcement path in the present tense, and only the line-10 D-GOV-43 amendment acknowledges it as history. I applied one rule across items: where the file's own D-GOV-43 note names the section's subject as compatibility history, use ACCEPTED_DIVERGENCE (D-GOV-43 is GOVERNING and permits the difference); otherwise IMPLEMENTED_DIFFERENTLY. #4-#6 follow the same reading (MEDIUM).
- `DOC:ADDING_A_TOOL#1` (MEDIUM, STALE_SPECIFICATION, R4-Q1). Alternative: ACCEPTED_DIVERGENCE under the banner. The removed paths in steps 1-2 are an uncovered, repair-shaped defect, so STALE_SPECIFICATION is primary.

## 3. Register-defect summary

None.

## 4. Direction and cause

PRE_V3_DRIFT with CAUSE2:FACADE_DEPRECATION (#0) and CAUSE2:CODEX_SOLE_ENGINE (#1): the paths moved in ee290e22a (2026-07-04) under D-APP-47 (GOV:D-APP-47; facade retained by D-APP-89). CODEX_SOLE_ENGINE (#3-#5) and NATIVE_DELEGATION with CAUSE2:CODEX_SOLE_ENGINE (#6), direction GOV:D-GOV-43; GOV:D-APP-127. No NONE_FOUND direction rows. No OTHER tokens.

## 5. Method friction

- Scripts under `frontend/scripts/**` and `frontend/package.json` sit outside the static reach map but match the validator's code-path pattern, so they must carry a REACH tag. I tagged them `REACH=TEST_ONLY` as verification tooling. Proposal: add `REACH=TOOLING` (or seed the pack from package.json scripts) so tooling is not conflated with test-only product code.
- The runtime-contracts descriptor registry is tagged LIVE by the pack only through the contracts barrel; its sole importers are legacy `lib/harness` modules. Under a literal rule 3 that LIVE tag would suppress R4-Q1 on exposure claims. I cited R4-Q1 where the exposure/enforcement part of the claim is met only by LEGACY_ONLY code and the LIVE module supplies metadata only (ADDING_A_TOOL#1, RUNTIME_ENGINE_CONTRACT#6, TOOL_CATALOG#3). Proposal: the pack could mark barrel-only reach as `LIVE(barrel)` so R3 can re-derive consistently.

## 6. Effort

About 12 files (doc, runtime-contracts tool-descriptor and tool-names, harness-contract facade, legacy mcp and options modules by grep, tests, HARNESS capabilities). Context comfortable.
