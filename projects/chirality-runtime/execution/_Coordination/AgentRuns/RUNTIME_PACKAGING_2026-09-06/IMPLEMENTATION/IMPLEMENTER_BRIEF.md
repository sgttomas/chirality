# Sealed Agent 2 implementation brief
RequestedBy: /root/packaging_manager (WORKING_ITEMS Agent 1)
RunID: RUNTIME_PACKAGING_2026-09-06
ParentInstanceID: /root/packaging_manager
ChildInstanceID: /root/packaging_manager/implement (actual native identity recorded after dispatch)
PackageID: PKG-02_Runtime_Product
DeliverableID: DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
Form: ephemeral generalist Agent 2 for the novel ESM/CommonJS consumer integration boundary. No delegation.
Model: inherited OpenAI GPT-6; exact serving ID unavailable. Role/non-delegation instruction-asserted, not mechanically enforced.

Objective: Repair Runtime's eager Pi SDK import boundary so the App's existing esbuild node24/CommonJS bundle starts, while preserving actual Pi operation and current public synchronous createPiTurnRuntime API and v1/v2 semantics. Consumer root barrel reexports pi-turn-runtime; its top-level value SDK imports become invalid require() against import-only coding-agent exports. Pi-ai is also import-only; observed frontend external list names coding-agent, not pi-ai. Diagnose coherent lazy native import shape; do not merely suppress error or remove public exports.

AcceptedBasis: PLAN_V1.json and CONTEXT_SHA256.json; accepted migration/current owner direction, prior spec fan-in and amendment11. These authorize bounded implementation, no contract/hold acceptance.
DeclaredReads: root AGENTS.md; project AGENTS/loop/PRD/authority; accepted DEL-02-06 SOW and prior plan, owner direction/spec fan-in/amendment11; Runtime packages/tests/manifests/node_modules; read-only frontend scripts/build-electron.mjs, electron/runtime-host.ts and related import files; CI log/PR737. Read applicable nested AGENTS if present.
AllowedTools: read, write, bash/exec tests and deterministic evidence tools; no delegation or external messaging; no credential/server/supplier operational access. Current owner authorization supersedes historical Piping-specific child tool restrictions.
AllowedWriteTargets (exclusive): projects/chirality-runtime/packages/engine-pi-omlx/src/pi-turn-runtime.ts; projects/chirality-runtime/tests/pi-packaging.test.ts; projects/chirality-runtime/package.json; projects/chirality-runtime/package-lock.json; IMPLEMENTATION/IMPLEMENTER/** in this run; /private/tmp/runtime-packaging-20260906/manager/implement/**. Registered typecheck may regenerate Runtime ignored dist/tsbuildinfo only. Any new exact production path requires manager recorded amendment first.
Dependencies: frozen manager diagnosis/plan. No other production writer.
EXCLUSIONS: frontend/shared/Root/sibling writes; accepted SOW/status/hold/ruling edits; public factory/API changes or weakening security/timeout/cancellation; supplier scratch/builds, oMLX/provider calls, credentials, user operational state, release, commit/push/merge.
Checks: authorized npm run typecheck and focused Vitest Pi suite; build consumer-shaped esbuild node24/CJS Pi-externals integration under Runtime test/owned scratch. Use installed esbuild; add explicit pinned dev dependency/lock only if durable regression needs it. Do not run frontend build itself. Parent owns whole registered suite after freeze.
AcceptanceCriteria: preserve reproducible pre-fix ERR_PACKAGE_PATH_NOT_EXPORTED evidence; post-fix consumer CJS startup plus actual real SDK Pi turn with offline fake fetch; ESM operation retained; cover loading/cancellation/deadline interactions introduced by asynchronous import, root/account/binding concurrency checks unchanged; no provider network/account access. Avoid mocked-SDK-only passing evidence. Source/dep hashes, command logs, diff and scope proof in return. No unsupported universal App/CI adoption claim.
ExpectedOutputs: IMPLEMENTER/RETURN.md and checks/logs/pre-fix fixture evidence, exact changed paths and SHA256, diagnosis, limitations, reruns. Preserve originals or equivalent pre-fix bundle/log before editing.
Escalation: exact additional paths via manager; semantic/cross-scope needs return concrete evidence. Cancellation deadline must bound SDK loading; no mutable state gap causing turn races.
