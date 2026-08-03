# Sealed Agent 2 brief — D-APP-88 standalone helper R2

## Identity and method

- ChildInstance: `A2-DAPP88-R2-IMPLEMENT-01`
- Parent: `WI-PKG09-DAPP88-B-R2`
- Role: Agent 2 `TASK`
- TaskSkill: `software-bounded-implementation`
- ScopePath: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- Profile: `projects/chirality-app-dev/software-workflow.json`

Read `AGENTS.md`, `agents/AGENT_TASK.md`, `docs/SOFTWARE_WORKFLOW_PROFILE.md`, the selected skill and companions, D-APP-88 packet/ruling, DEL-09-04 kit, R2 activation/graph, and Attempt-1 manager/handoff/evidence. Attempt 1 is immutable diagnostic input only.

## Objective

Implement the untried separately built full Electron helper target. Build a complete standalone helper `.app` from an explicit helper electron-builder target/config with:

- `appId=com.chirality.app.runtime-helper` unless a live builder constraint proves a precise alternative necessary;
- its own product and executable name;
- electron-builder-generated matching Chromium helper applications/topology;
- an explicit helper entry that may reuse the compiled main code in runtime-helper mode;
- the same Root daemon/socket/auth/session/project semantics without Root source changes.

Then embed/copy that finished helper bundle as a whole, deterministically, into the GUI package at `Chirality.app/Contents/Library/LoginItems/`. Do not construct the helper by copying or mutating the finished GUI bundle, its executable, frameworks, or child helpers. Do not fall back to a signal wrapper.

## Allowed writes

- bounded `projects/chirality-app-dev/frontend/electron/**` helper/packaging integration;
- bounded `projects/chirality-app-dev/frontend/scripts/**` build/proof support;
- bounded Electron/helper tests under `frontend/src/__tests__/**`;
- `frontend/package.json`, lockfile, and TypeScript/build metadata only where the standalone target genuinely requires them;
- DEL-09-04 `_STATUS.md`, `MEMORY.md`, and one new R2 TASK run record;
- this R2 AgentRuns root and instance evidence/return.

Do not write decisions/register/TM/receipt/completion log, Root source, PRD/corpus, decomposition/SCA, other deliverables/packages/loops, Git, release, signing, notarization, publication, or distribution surfaces. Preserve all D-APP-89/planning/ruling bytes. A reversible Root dependency projection is validation-only and must be restored exactly.

## Required implementation and proof

1. Start from the restored D-APP-89 predecessor; do not import Attempt-1 candidate source.
2. Produce separate explicit helper build configuration, entry, output, and deterministic whole-bundle embedding step.
3. Prove GUI identity `com.chirality.app`; helper identity `com.chirality.app.runtime-helper` (or exact justified alternative), distinct product/executable names, `LSUIElement`, matching builder-generated helper topology, relative/relocatable internal links, and exactly one top-level runtime helper.
4. Prove LaunchAgent `ProgramArguments` targets the standalone helper executable.
5. On exact final packaged bits, prove:
   - login/job-equivalent launch starts only helper/daemon posture without a real login event;
   - one daemon/runtime singleton and shared socket/auth/session/project stores;
   - packaged CLI binds that daemon; GUI coexistence does not replace/retire it;
   - first `SIGTERM`/ordinary stop after GUI coexistence is graceful and removes the socket;
   - SIGKILL stale-state recover-on-start is bounded;
   - safeStorage namespace continuity without prompting/touching the owner login keychain; use accepted predecessor evidence plus current isolated proof where safe;
   - helper resource, asar, instruction-root, native-module, and runtime CLI integrity;
   - no TCP listener, token disclosure, global Node dependency, or extra runtime singleton.
6. Run focused tests, typecheck, production/Electron build, clean desktop package, dependency boundary, instruction-root integrity, full frontend tests, applicable registered checks/premerge/release-quality checks, diff/containment, receipt/corpus/self-check/practitioner checks as read-only validation, and D-APP-89 zero-consumer plus rollback guards.
7. Preserve sanitized raw logs/plist extracts/hashes/manifests before removing temporary state. Never copy or print token contents.
8. Cleanup all exact test processes, launchd jobs/plists, temporary trees, credential/token files, sockets, and validation projections. Prove zero residue.

## Returns and stop conditions

Write a TASK run record with the allowed terminal enum, a complete implementation return, package/source/evidence manifests, drill report, cleanup record, rollback manifest, and exact validation outcomes. Record telemetry events through the run-local ledger.

If bounded standalone-builder variants cannot satisfy the target, return `FAILED` with the exact builder/packaging blocker after preserving sanitized evidence and rolling back any known-defective product state. Do not weaken D-APP-88, mutate Root semantics, reuse copied-main construction, or add a signal wrapper.
