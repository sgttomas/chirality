# DOC-README notes (RUN_D128 R2 EXT, item 7, audit-only)

Ledger: `DOC-README_claims.csv`, 7 rows, validator `RESULT PASS errors=0 warnings=0`. This ledger is audit-only (CONVENTIONS §8): nothing is repaired by this run.

## 1. Census

STATE_ASSERTION 7: ALIGNED 3 (#1, #3, #6); STALE_SPECIFICATION 3 (#2, #4, #5); PARTIALLY_IMPLEMENTED 1 (#0). Split rate 0/7. SEE rows 0. No errata.

## 2. Least-confident rows

- `DOC:README#0` (LOW, PARTIALLY_IMPLEMENTED, R4-Q5). Alternative: STALE_SPECIFICATION, reading 'the former eight-name UIEvent set is compatibility history' as a now-false present fact. The live browser stream is UIEvent-typed (daemon-harness-port DaemonTurnFrame = UIEvent; the section8 sdk_native_stream check asserts chat:complete and process:exit on the live route), with upstream method and params nested in harness:event codex.notification. The coverage sentence (options fallback, subagent governance, attachments) is also only partly met.
- `DOC:README#4` (MEDIUM, STALE_SPECIFICATION). Alternative: ALIGNED as a generic recipe; the named example root no longer exists, so it cannot run as written.

## 3. Register-defect summary

None.

## 4. Direction and cause

CODEX_SOLE_ENGINE (#0), with direction NONE_FOUND: no record directs keeping the UIEvent envelope. PRE_V3_DRIFT (#2, #4, #5): examples/example-project last touched in ae3abde37 (2026-05-19); the network-policy default output folder dates from 2026-08-01, the README line from 2026-06-21. No CAUSE2. No OTHER tokens. Register/CONTEXT search behind every NONE_FOUND: grep of projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md (frozen tree) for docs/harness, tool_catalog, adding_a_tool, runtime_engine_contract, TRACEABILITY, instructions/AGENTS, UIEvent, example-project, network-policy, harness-contract, D-GOV-43, Pi; hits: D-APP-47, D-APP-72, D-APP-89, D-APP-127 (none addresses the point). grep of projects/chirality-app-dev/plans/** and execution/_Coordination/AgentRuns/APPDEV_V3_NODE_* for UIEvent|eight-name: pre-v3 plans only; no plans/steers/chirality_app_v3_* exist under the App tree at the frozen basis.

## 5. Method friction

- Scripts under `frontend/scripts/**` and `frontend/package.json` sit outside the static reach map but match the validator's code-path pattern, so they must carry a REACH tag. I tagged them `REACH=TEST_ONLY` as verification tooling. Proposal: add `REACH=TOOLING` (or seed the pack from package.json scripts) so tooling is not conflated with test-only product code.
- The runtime-contracts descriptor registry is tagged LIVE by the pack only through the contracts barrel; its sole importers are legacy `lib/harness` modules. Under a literal rule 3 that LIVE tag would suppress R4-Q1 on exposure claims. I cited R4-Q1 where the exposure/enforcement part of the claim is met only by LEGACY_ONLY code and the LIVE module supplies metadata only (ADDING_A_TOOL#1, RUNTIME_ENGINE_CONTRACT#6, TOOL_CATALOG#3). Proposal: the pack could mark barrel-only reach as `LIVE(barrel)` so R3 can re-derive consistently.
- `.github/workflows/harness-premerge.yml` is cited as evidence only, following the item-4 convention for workflow files.

## 6. Effort

About 12 files (README, section8/section9/premerge/release-quality/network/secret/packaged-proof scripts by grep and line range, the CI workflow, http.ts, delegated-engine-adapter.ts). Context comfortable.
