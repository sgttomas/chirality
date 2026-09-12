# Runtime loop return: D-GOV-43 application tranche (2026-09-12)

Bounded TASK executor; worktree branch `claude/chirality-codex-replatform-3999f1`; no git write operations performed. All work under `projects/chirality-runtime/`, excluding `packages/`, `tests/`, `package*.json`, `tsconfig*`, `vitest*`, `loop/`, `_harness/`.

## Files changed

- `README.md`: rewritten to the App-owned service architecture (one-process composition, `chirality-runtime-service` entry, socket API, lockfile-pinned stock Codex, effective home, how the App owns the child, interruption versus retirement), retirement note naming the deleted tools and last commit `e83cb1f47`, short Pi/oMLX "Reference" section.
- `docs/CODEX_MVP_INTEGRATION.md`: body replaced with a supersession header (D-GOV-43 A2; Root `docs/SPEC.md` section 14; App `docs/SPEC.md`; original at `e83cb1f47`).
- `docs/PRD.md`: "D-GOV-43 revision (2026-09-12)" section inserted after the status paragraph; original body preserved.
- `docs/PRD_AUTHORITY.md`: appended revision section re-issuing hashes once for `docs/PRD.md`, `HOLD_SUCCESSOR_MAP.csv`, `GATE_READINESS.md`; Gate3 table kept as the historical identity record.
- `execution/PKG-02_Runtime_Product/1_Working/DEL-02-07` to `DEL-02-12` `_STATUS.md`: `Current State: RETIRED`, dated history line with family rationale; no other deliverable content touched.
- `DEL-02-06/ScopeOfWork.md`: D-GOV-43 revision notes appended beside the fan-in paragraph, REQ-010 (lease, supplier snapshot, version mismatch) and REQ-041 (D-GOV-36 custody exception); original clauses preserved. `DEL-02-06/_STATUS.md`: history entry; state unchanged.
- `execution/_Decomposition/HOLD_SUCCESSOR_MAP.csv`: nine `HELD_UNAVAILABLE` rows set to `CurrentDisposition=CLOSED_D-GOV-43_SCA-004`, `State=CLOSED_RETIRED_FAMILY_1`, rationale in `ReleasingEvidence`; historical columns and the Tier-0 row unchanged.
- `execution/_Decomposition/GATE_READINESS.md`: supersession note appended.
- `execution/_Coordination/AgentRuns/RUNTIME_DGOV43_HOLD_CLOSURE_20260912/` (new): `Brief.md`, `Impact_Assessment.md`, `Amendment_Actions.csv`, `Decision_Log.md`, `RUN_SUMMARY.md` (pre/post hashes), `LATEST_PREIMAGE.md`, `LATEST_POSTIMAGE.md`. `_LATEST.md` now points to SCA-004.
- `execution/_Coordination/HANDOFF_STATE.md`, `MIGRATION_APPLICATION.md` (with the revised DEL-02-06 SOW hash, once), `MIGRATION_ACCEPTANCE_2026-09-06.md`: supersession entries appended.
- `execution/_Coordination/NOTICE_2026-09-12_ROOT_D-GOV-43_CODEX_HOST_REPLATFORM.md` (new, 41 lines).
- `execution/_Coordination/AgentRuns/RUNTIME_*`: unchanged.

## Files deleted (git history at `e83cb1f47`)

`tools/codex-supplier/` (12 files plus `history/build03`, `history/build04`), `tools/native-admission/` (9 files incl. `p2-host-xpc-probe/`), `tools/provision-hosted-release-anchor-v2.mjs`. `tools/` is now empty.

## Out-of-scope references to the deleted paths (not edited)

- `projects/chirality-runtime/tests/p2-host-xpc-probe.test.ts:8` requires `../tools/native-admission/p2-host-xpc-probe/p2-host-xpc-probe.cjs`.
- `projects/chirality-runtime/tests/hosted-release-provisioner.test.ts:193,221` import `../tools/provision-hosted-release-anchor-v2.mjs`.
These two tests will fail until the implementing session retires them (both belong to family 1). No `vitest*`, `tsconfig*` or `package.json` references the deleted paths.

Related live references to the `@chirality/native-admission` package (not the deleted tools directory; retired by the implementing session): `packages/daemon/src/{codex-authenticated-transport,account-free-login-observation,host-account-release,codex-login,hosted-private-composition,codex-worker}.ts`, `packages/daemon/package.json`, `packages/daemon/tsconfig.json`, `tsconfig.json`, `package-lock.json`, `packages/core/src/runtime-conformance-v2.ts`, `tests/{runtime-admission-native,hosted-packaged-release,runtime-conformance-v2,runtime-conformance-v2-admission,d36-v2-connected,account-free-login-observation}.test.ts`; App loop: `frontend/package.json:49,130`, `frontend/package-lock.json`, `frontend/scripts/{build-electron,verify-packaged-dependency-boundary,build-controlled-ci-runtime}.mjs`, `frontend/src/__tests__/scripts/{verify-packaged-dependency-boundary,dmg-packaging-policy,build-electron,sign-electron-runtime-v2,finalize-electron-resources}.test.ts`, `frontend/src/__tests__/integration/controlled-ci-runtime.integration.test.ts`. Historical mentions in `AgentRuns/**`, `_PROPOSALS/**` and `TOPOLOGY_COMPARISON.md` are history.

## Validators

- `validate_decomposition_registers.py projects/chirality-runtime/execution`: 204 ERROR findings, identical before and after (DRB-001/006, EVQ-003/006); the tool targets the generic `Deliverables.csv`/`Dependencies.csv` shape and this loop's frozen `Dependencies.csv` registers, none of which this tranche touched. Pre-existing, not introduced.
- `validate_path_anchors.py --text .`: PASS (4331 surfaces).
- `validate_scope_change_packet.py` on SCA-004: FAIL for missing `Packet_*.md`, `SCOPE_CHANGE_INIT.md`, `Proposed_SCA_Actions.csv`, `Affected_Surfaces.csv`, `Evidence_Index.csv`; it validates the PKG-00 consumable-packet shape, which SCA-001 to SCA-003 also do not use (SCA-003 fails identically). The packet follows the loop's own SCA-003 convention.

## Judgment calls

1. Accepted texts (`docs/PRD.md`, `DEL-02-06/ScopeOfWork.md`, `GATE_READINESS.md`, migration records) were revised by inserting dated D-GOV-43 revision sections beside the original clauses rather than rewriting them, so executed and accepted bytes remain readable in place.
2. `PRD_AUTHORITY.md` hashes were re-issued once for the three amended payload files; the Gate3 table is kept as the historical identity record. No other consumer of those hashes exists (`root_governance_state.py` reads a Root copy under `SCA-005_2026-09-06_GATE4_PLAN`).
3. Registers (`RUNTIME_DELIVERABLE_REGISTER.csv`, `RUNTIME_SCOPE_LEDGER.csv`, objective register, `SOURCE_SCOPE_REQUIREMENTS/`, DECOMP) were left unchanged as the frozen Gate3 basis; retirement is carried by `_STATUS.md`, the hold map and the packet, per item 11 (no new register).
4. `_STATUS.md` retirement was written by hand: `tools/scaffolding/write_status.sh` does not accept `RETIRED`. History lines keep the file's existing `date — text` separator for consistency with the appender; all new prose elsewhere avoids em-dashes.
5. `execution/_Coordination/_COORDINATION.md` (human-owned notes, "nine holds remain") was left unchanged and is flagged for the owner.
6. The README describes the A2 composition as the design in force; source under `packages/` still contains the retired modules until the implementing session lands its changes.
