# Assessment INSP-03: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

Deliverable: DEL-09-04
Package: PKG-09 Validation, Packaging, Security, and Release
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `d0766e0f24b923f7925c711fe05e0cf5d28fd1fb`
Spec source: `Specification.md`

Current calibration (2026-08-20): lifecycle is `IN_PROGRESS`. The selected
REQ-009 / R4-P49 packaged-network residual is current at the DEL-09-06 compact
evidence package; the historical inspection header remains the original
inspection basis.

## Scope

This assessment inspected the macOS arm64 unsigned DMG packaging path, instruction-root integrity resources, SDK subprocess/binary package layout checks, and release-target boundaries. It did not run `npm run desktop:dist` and found no current DMG/app bundle artifact in `frontend/dist`.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ001 - Current release target is macOS 15+ Apple Silicon arm64 unsigned/unnotarized local-builder DMG. | PASS | `frontend/package.json` build config pins mac `minimumSystemVersion` and arm64 DMG target at lines 90-99; `frontend/src/__tests__/scripts/dmg-packaging-policy.test.ts` asserts unsigned script posture and macOS arm64 DMG target at lines 38-76. | Target policy is encoded. |
| REQ002 - Produced via `npm run desktop:dist`. | PARTIAL | `frontend/package.json` exposes `desktop:dist` at line 27 with signing auto-discovery disabled; no current `desktop:dist` run was executed for this assessment. | Script exists; current artifact production is unproven. |
| REQ003 - Expected DMG path `frontend/dist/Chirality-0.1.0-arm64.dmg`. | PARTIAL | Build config implies DMG output under `frontend/dist`; direct artifact check found no DMG in `frontend/dist`. | Expected output path is not currently present. |
| REQ004 - Expected app bundle `frontend/dist/mac-arm64/Chirality.app`. | PARTIAL | Build config targets mac arm64; direct artifact check found no app bundle in `frontend/dist/mac-arm64`. | Expected output path is not currently present. |
| REQ005 - Build/integrity flow produces instruction-root integrity summary. | PARTIAL | `frontend/package.json` exposes `instruction-root:integrity` at line 24; `frontend/scripts/verify-instruction-root-integrity.mjs` writes summary status/details at lines 461-528. | No current `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` was present. |
| REQ006 - Packaged builds contain required instruction-root resources and verify before distribution. | PASS | `frontend/package.json` `extraResources` bundles agents/docs/root files at lines 71-88; `frontend/src/__tests__/scripts/dmg-packaging-policy.test.ts` asserts bundled instruction-root resources at lines 78-94. | Resource packaging is covered by config and tests. |
| REQ007 - Missing instruction-root assets are P0 blockers. | PASS | `frontend/scripts/verify-instruction-root-integrity.mjs` detects missing/mismatched files and exits fail at lines 300-344 and 530-567; tests prove missing SDK files fail at lines 203-238. | Fail-closed behavior exists. |
| REQ008 - Package readiness verifies SDK subprocess/binary from app bundle layout without secret leakage or broader network. | PARTIAL | `frontend/scripts/verify-packaged-agent-sdk-runtime.mjs` validates SDK module/package/root and app.asar-unpacked placement at lines 270-393; no current app bundle proof was run. | This is the main packaged evidence gap. |
| REQ009 - Packaged validation preserves Anthropic network guardrails. | PASS | `../DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20_Precedence_Closure/summary.json` identity-binds the fresh packaged app and records the blocked renderer diagnostic/probes plus five descendant TCP snapshots. | Zero non-allowlisted outbound TCP was observed; provider scope remained unchanged. |
| REQ010 - No Windows/Linux packaging without amendment. | PASS | Current build target is mac arm64 DMG in `frontend/package.json` lines 90-99; release docs state macOS 15+ Apple Silicon unsigned DMG as current target. | No broader packaging target is active. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| Current DMG/app artifacts absent | G6 / High | `frontend/dist` does not contain the expected DMG or app bundle during this inspection. | Packaging validation tranche |
| Packaged SDK subprocess proof not current | G6 / High | The no-live and live packaged SDK proof scripts exist, but no current proof against a built app bundle was available. | Packaging/security tranche |
| Instruction-root summary artifact absent | Medium | Integrity script exists and fails closed, but no current stable summary artifact was present. | Release validation tranche |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-09-04 has 9 active dependency rows: 3 are `NOT_APPLICABLE` and 6 remain `TBD`; closure remains open because six active rows are still unsatisfied.

## Forward Development Recommendation

1. Run `npm run desktop:dist` in a clean environment and archive the DMG/app bundle path, architecture, minimum OS, and signing state. Type: packaging validation. Size: M. Strategic fit: ON-STRATEGY.
2. Run instruction-root integrity against the packaged bundle and retain the stable summary artifact. Type: release validation. Size: S. Strategic fit: ON-STRATEGY.
3. Run the packaged SDK resolver proof against the app bundle layout and record SDK command path under `app.asar.unpacked`. Type: packaging/security validation. Size: M. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

This deliverable should not issue without real package artifacts. Source/config evidence is meaningful but insufficient for a packaging deliverable whose core acceptance requires inspecting produced app outputs.
