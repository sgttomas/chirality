# DOC-RUNTIME_ENGINE_CONTRACT notes (RUN_D128 R2 EXT, item 7, audit-only)

Ledger: `DOC-RUNTIME_ENGINE_CONTRACT_claims.csv`, 11 rows, validator `RESULT PASS errors=0 warnings=0`. This ledger is audit-only (CONVENTIONS §8): nothing is repaired by this run.

## 1. Census

STATE_ASSERTION 11: ALIGNED 2 (#7, #10); PARTIALLY_IMPLEMENTED 3 (#0, #2, #9); ACCEPTED_DIVERGENCE 3 (#1, #3, #8); IMPLEMENTED_DIFFERENTLY 2 (#4, #5); STALE_SPECIFICATION 1 (#6). Split rate 0/11. SEE rows 0. No errata. HumanDecisionNeeded: R4-Q1 on 6 rows (#1, #3, #4, #5, #6, #8), R4-Q5 on 4 rows (#0, #2, #4, #9), R4-Q2 on 1 row (#9).

## 2. Least-confident rows

- `DOC:RUNTIME_ENGINE_CONTRACT#4` (LOW, IMPLEMENTED_DIFFERENTLY, R4-Q1; R4-Q5). Alternative: ACCEPTED_DIVERGENCE, since the banner's 'first-adapter' clause arguably covers SDK tool evidence. Kept as IMPLEMENTED_DIFFERENTLY because the section also makes provider-neutral guarantees in the present tense: no raw output is stored, and a list of 'current persisted event categories'. On the live path the adapter carries Codex output deltas (up to 65,536 characters) in tool.progress and upstream params in codex.notification.
- `DOC:RUNTIME_ENGINE_CONTRACT#5` (MEDIUM). Alternative: STALE_SPECIFICATION as primary. The Pi sentence is flatly false: pi-agent-engine-adapter.ts and @earendil-works/pi-* 0.82.0 are present, and D-APP-72 ruled a bounded Pi engine. It is recorded as ALSO.
- `DOC:RUNTIME_ENGINE_CONTRACT#2` (MEDIUM, PARTIALLY_IMPLEMENTED). Alternative: STALE_SPECIFICATION ('UIEvent names are compatibility history'; 'App's thread index' does not exist).

## 3. Register-defect summary

None.

## 4. Direction and cause

CODEX_SOLE_ENGINE is primary on 8 rows. NATIVE_DELEGATION on #5 (CAUSE2:CODEX_SOLE_ENGINE). PRE_V3_DRIFT on #6 (CAUSE2:CODEX_SOLE_ENGINE). #9 carries CAUSE2:PRE_V3_DRIFT. Direction is GOV:D-GOV-43; GOV:D-APP-127 on the banner-covered and live-path rows, GOV:D-APP-47 on the path move, and NONE_FOUND on #0, #2 and #9. No record directs keeping the UIEvent envelope or exempting the Codex adapter from K-ENGINE-2 conformance; these are R4-Q5 and R4-Q2. No OTHER tokens. Register/CONTEXT search behind every NONE_FOUND: grep of projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md (frozen tree) for docs/harness, tool_catalog, adding_a_tool, runtime_engine_contract, TRACEABILITY, instructions/AGENTS, UIEvent, example-project, network-policy, harness-contract, D-GOV-43, Pi; hits: D-APP-47, D-APP-72, D-APP-89, D-APP-127 (none addresses the point). grep of projects/chirality-app-dev/plans/** and execution/_Coordination/AgentRuns/APPDEV_V3_NODE_* for UIEvent|eight-name: pre-v3 plans only; no plans/steers/chirality_app_v3_* exist under the App tree at the frozen basis.

## 5. Method friction

- Scripts under `frontend/scripts/**` and `frontend/package.json` sit outside the static reach map but match the validator's code-path pattern, so they must carry a REACH tag. I tagged them `REACH=TEST_ONLY` as verification tooling. Proposal: add `REACH=TOOLING` (or seed the pack from package.json scripts) so tooling is not conflated with test-only product code.
- The runtime-contracts descriptor registry is tagged LIVE by the pack only through the contracts barrel; its sole importers are legacy `lib/harness` modules. Under a literal rule 3 that LIVE tag would suppress R4-Q1 on exposure claims. I cited R4-Q1 where the exposure/enforcement part of the claim is met only by LEGACY_ONLY code and the LIVE module supplies metadata only (ADDING_A_TOOL#1, RUNTIME_ENGINE_CONTRACT#6, TOOL_CATALOG#3). Proposal: the pack could mark barrel-only reach as `LIVE(barrel)` so R3 can re-derive consistently.
- Several sections mix module-level contract text with product-behaviour guarantees. Addendum 6 rule 2 sends them to the live path. The ALSO_MODULE token keeps the module reading; a per-sentence split would add rows without changing R3 clustering.

## 6. Effort

About 15 files (doc, runtime-contracts agent-engine-port, event-schema, engine-conformance, delegated-engine-adapter, codex-supervisor blame, http.ts, daemon-harness-port, package.json, register rows D-APP-01/72, RTCORE/RTCONTRACT/HARNESS capabilities). Context moderate.
