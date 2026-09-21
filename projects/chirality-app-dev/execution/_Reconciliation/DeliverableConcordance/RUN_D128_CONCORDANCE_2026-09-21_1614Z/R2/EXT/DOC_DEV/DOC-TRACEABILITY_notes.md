# DOC-TRACEABILITY notes (RUN_D128 R2 EXT, item 7, audit-only)

Ledger: `DOC-TRACEABILITY_claims.csv`, 2 rows, validator `RESULT PASS errors=0 warnings=0`. This ledger is audit-only (CONVENTIONS §8): nothing is repaired by this run.

## 1. Census

STATE_ASSERTION 2: STALE_SPECIFICATION 1 (#1), PARTIALLY_IMPLEMENTED 1 (#2). Split rate 0/2: the 19-row table in #1 was not split, because 17 rows verify as stated and the two defects are the heading owner and REQ-17. SEE rows 0. No errata.

## 2. Least-confident rows

- `DOC:TRACEABILITY#1` (MEDIUM). Alternative: split into 19 REQ rows (17 ALIGNED, REQ-17 STALE_SPECIFICATION, plus the heading label). Not split: the per-row verdicts do not differ enough to justify splitting.
- `DOC:TRACEABILITY#2` (MEDIUM, PARTIALLY_IMPLEMENTED, R4-Q5). Alternative: STALE_SPECIFICATION for the sentence calling `section8.sdk_native_stream` Claude-path history. It is a REQUIRED premerge ID that runs against the live route.

## 3. Register-defect summary

None.

## 4. Direction and cause

PRE_V3_DRIFT (#1): the heading dates from 2026-05-18; the three missing Section 9 IDs were added on 2026-07-10 and the doc was never updated. DeliverableID is DEL-09-01 by content (Section 8 Harness Validation Preservation); the doc's own label DEL-07-01 now names Working Root Validation. CODEX_SOLE_ENGINE (#2), direction NONE_FOUND. Register/CONTEXT search behind every NONE_FOUND: grep of projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md (frozen tree) for docs/harness, tool_catalog, adding_a_tool, runtime_engine_contract, TRACEABILITY, instructions/AGENTS, UIEvent, example-project, network-policy, harness-contract, D-GOV-43, Pi; hits: D-APP-47, D-APP-72, D-APP-89, D-APP-127 (none addresses the point). grep of projects/chirality-app-dev/plans/** and execution/_Coordination/AgentRuns/APPDEV_V3_NODE_* for UIEvent|eight-name: pre-v3 plans only; no plans/steers/chirality_app_v3_* exist under the App tree at the frozen basis.

## 5. Method friction

- Scripts under `frontend/scripts/**` and `frontend/package.json` sit outside the static reach map but match the validator's code-path pattern, so they must carry a REACH tag. I tagged them `REACH=TEST_ONLY` as verification tooling. Proposal: add `REACH=TOOLING` (or seed the pack from package.json scripts) so tooling is not conflated with test-only product code.
- The runtime-contracts descriptor registry is tagged LIVE by the pack only through the contracts barrel; its sole importers are legacy `lib/harness` modules. Under a literal rule 3 that LIVE tag would suppress R4-Q1 on exposure claims. I cited R4-Q1 where the exposure/enforcement part of the claim is met only by LEGACY_ONLY code and the LIVE module supplies metadata only (ADDING_A_TOOL#1, RUNTIME_ENGINE_CONTRACT#6, TOOL_CATALOG#3). Proposal: the pack could mark barrel-only reach as `LIVE(barrel)` so R3 can re-derive consistently.

## 6. Effort

About 6 files (doc, section8/section9/premerge scripts, DELIVERABLE_INVENTORY, test-file existence). Context comfortable.
