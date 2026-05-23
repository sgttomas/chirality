# Specification: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

## Scope

This deliverable covers the macOS arm64 unsigned DMG packaging path and the release-readiness evidence needed to prove instruction-root asset integrity and SDK subprocess package executability for Chirality App vNext.

In scope:

- `frontend/` local packaging command `npm run desktop:dist`.
- DMG output verification for macOS 15+ Apple Silicon.
- App bundle instruction-root asset inclusion and integrity verification.
- SDK subprocess/binary package-layout probe.
- Integrity summary evidence.

Out of scope:

- Windows/Linux packaging, unless a governed amendment reopens it.
- Feature implementation unrelated to packaging glue, integrity checks, or package-readiness probes.
- Signing/notarization beyond the current unsigned/adhoc local-builder posture.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-09-04-REQ-001 | The release target must remain macOS 15+ Apple Silicon (`arm64`) unsigned/unnotarized local-builder DMG unless amended. | `docs/PRD.md` Section 6.2; `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 | Inspect app bundle architecture, `LSMinimumSystemVersion`, and signing posture. |
| DEL-09-04-REQ-002 | The desktop distribution build must be produced through `npm run desktop:dist` from `frontend/`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` FR-067 | Run or review build evidence for `npm run desktop:dist`. |
| DEL-09-04-REQ-003 | The expected DMG output must include `frontend/dist/Chirality-0.1.0-arm64.dmg`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 7.12 | Confirm file exists after packaging. |
| DEL-09-04-REQ-004 | The expected app bundle output must include `frontend/dist/mac-arm64/Chirality.app`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 | Confirm app bundle exists after packaging. |
| DEL-09-04-REQ-005 | The build/integrity flow must produce or preserve `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 | Confirm summary JSON exists and records a passing integrity result, or record blocker. |
| DEL-09-04-REQ-006 | Packaged builds must contain required instruction-root resources and verify integrity before distribution. | `docs/CONTRACT.md` K-PACKAGE-1; `docs/SPEC.md` Section 1.1 | Run/review `npm run instruction-root:integrity` and bundle resource inspection. |
| DEL-09-04-REQ-007 | Missing required instruction-root assets are a P0 packaging and runtime-readiness blocker. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1; decomposition OI-004 | Fail packaging readiness if required assets are absent, or document accepted amendment. |
| DEL-09-04-REQ-008 | The package-readiness evidence must verify that the SDK subprocess/binary can be found and executed from the app bundle/package layout. | `docs/PRD.md` NFR-030; `docs/PRD.md` KG-025; `docs/SPEC.md` Section 19.4 | Execute SDK subprocess packaging probe in packaged layout; record result. |
| DEL-09-04-REQ-009 | The packaged validation must preserve Anthropic-only network guardrails. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 | Run/review network guardrail checks or document blocker. |
| DEL-09-04-REQ-010 | Windows/Linux packaging must not be introduced by this deliverable without explicit scope amendment. | Decomposition SOW-078; `docs/PRD.md` KG-014 | Review package scripts/config changes for target creep. |

## Standards

- `docs/CONTRACT.md` K-ROOT-1, K-ROOT-2, K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1.
- `docs/SPEC.md` Section 1.1 instruction-root requirements and Sections 19.1/19.4 release validation requirements.
- `docs/PRD.md` FR-067, NFR-030, KG-014, KG-025.
- `docs/TYPES.md` release and validation vocabulary for `instruction-root:integrity` and `desktop:dist`.

## Verification

The verification package should include:

| Verification Item | Expected Evidence | Requirement Coverage |
|---|---|---|
| Local build command evidence | command transcript or CI/local run record for `npm run desktop:dist` | DEL-09-04-REQ-002 |
| DMG artifact check | file listing or checksum for `frontend/dist/Chirality-0.1.0-arm64.dmg` | DEL-09-04-REQ-001, DEL-09-04-REQ-003 |
| App bundle check | file listing for `frontend/dist/mac-arm64/Chirality.app` | DEL-09-04-REQ-004 |
| Minimum macOS version check | inspected `LSMinimumSystemVersion` value `15.0.0` or later | DEL-09-04-REQ-001 |
| Architecture check | inspected arm64 binary architecture | DEL-09-04-REQ-001 |
| Signing posture check | evidence that signing is unsigned/adhoc as scoped | DEL-09-04-REQ-001 |
| Instruction-root integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | DEL-09-04-REQ-005, DEL-09-04-REQ-006, DEL-09-04-REQ-007 |
| SDK subprocess packaging probe | package-layout execution result for SDK subprocess/binary | DEL-09-04-REQ-008 |
| Network guardrail check | evidence Anthropic-only network policy remains active | DEL-09-04-REQ-009 |

## Documentation

Required deliverable artifacts:

- `desktop:dist` evidence.
- Instruction-root integrity summary.
- SDK subprocess packaging probe result.
- `TBD` residual-blocker list for incomplete instruction-root assets or SDK package-layout failures.
- `ASSUMPTION` or `PROPOSAL` entries for any packaging config interpretation not directly supported by source evidence.
