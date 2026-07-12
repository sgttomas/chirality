# Datasheet: DEL-09-05 CI Artifact and Release Verification Workflow

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-09-05 |
| DeliverableName | CI Artifact and Release Verification Workflow |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | CI_CD_CHANGE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| Current Scope | Maintain CI premerge workflow, stable artifact upload, local command sequence, and manual release verification checklist. |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Covered scope items | SOW-035 Required local checks; SOW-036 Section 8/9 validation; SOW-072 macOS arm64 unsigned DMG release target | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 8/9, `DEL-09-05` and scope ledger rows |
| Supported objective | OBJ-008 | `_CONTEXT.md` Traceability; decomposition `DEL-09-05` row |
| Anticipated artifacts | CI workflow; stable artifact upload; release verification runbook | `_CONTEXT.md` Anticipated Artifacts; decomposition `DEL-09-05` row |
| Local check command sequence | `npm run test`; `npm run typecheck`; `npm run harness:validate:premerge`; `npm run instruction-root:integrity`; `npm run desktop:dist` | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
| Stable summary artifact | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
| Expected packaging outputs | `frontend/dist/Chirality-0.1.0-arm64.dmg`; `frontend/dist/mac-arm64/Chirality.app`; instruction-root integrity summary JSON | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
| CI workflow baseline | Checkout repository; setup Node.js 20; run `npm ci`; verify instruction-root assets; preflight validation script presence; start Next server; poll readiness; run premerge validation; verify stable summary artifact; upload summary artifact | `docs/PRD.md` Section 12.7 |
| Release target | macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |
| Ownership disposition | `ResponsibleParty` remains `TBD` until a human assigns ownership; CI/release execution must not be delegated on an inferred owner. | `_CONTEXT.md` Identity and Source Authority; `Procedure.md` Prerequisites |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source fidelity warning | `docs/PRD.md` has expected SHA `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` and observed SHA `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`; per dispatch brief, this is a source status. | `_REFERENCES.md`; dispatch brief |
| CI provider implementation | ASSUMPTION: GitHub Actions is the intended CI surface because `docs/PRD.md` Section 12.7 names "The GitHub workflow"; exact workflow file path is TBD. | `docs/PRD.md` Section 12.7 |
| Stable summary artifact path | The review target is `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | `docs/PRD.md` Sections 12.2 and 12.7; `docs/SPEC.md` Section 19.1 |
| CI upload artifact identity | The CI workflow must upload the stable summary artifact, but the CI upload artifact name, retention period, and workflow file path are `TBD` until source-defined or human-approved. | `docs/PRD.md` Section 12.7; `_SEMANTIC_LENSING.md` D-001 |
| Security posture during verification | API keys must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts; outbound network access remains loopback plus Anthropic API path unless amended. | `docs/CONTRACT.md` K-NET-1 and K-KEY-1 |
| Dependency state | Declared upstream and downstream dependencies remain `TBD`; extracted `Dependencies.csv` v3.1 rows exist but readiness remains blocked until accepted dependency-edge or blocker disposition is recorded. | `_DEPENDENCIES.md` Extracted Dependency Register; `_SEMANTIC_LENSING.md` X-002 |

## Construction

| Construct | Required Content |
|---|---|
| CI workflow | Implement or maintain a premerge workflow that executes the PRD Section 12.7 sequence and uploads the stable validation summary artifact. |
| Local command sequence | Document a reproducible local sequence from `frontend/` that runs test, typecheck, premerge validation, instruction-root integrity, and desktop distribution checks. |
| Stable artifact verification | Verify that `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` exists after relevant checks and is uploaded by CI. |
| Manual release checklist | Verify macOS DMG architecture, minimum system version, signing posture, instruction-root assets, working-root selector availability, current shipped Anthropic network guardrails, SDK-backed packaged turn startup after R1, SDK subprocess execution access, and SDK transcript storage/mirroring decision conformance. |
| Evidence capture | Record command outcomes, artifact paths, and release-check findings in a release verification runbook or equivalent reviewable artifact. |

## References

| RefID | Source | Used For | Status |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Governance and professional-boundary context | MATCH |
| REF-002 | `docs/CONTRACT.md` | Release, validation, network, key, packaging invariants | MATCH |
| REF-003 | `docs/SPEC.md` | Required checks, Section 8/9 validation, manual release verification | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary for artifacts, validation, `desktop:dist`, and lifecycle terms | MATCH |
| REF-005 | `docs/PLAN.md` | Local check command sequence and expected package artifacts | MATCH |
| REF-006 | `docs/PRD.md` | CI acceptance, validation plan, manual release verification | MATCH source status only — reconciled under D-APP-38 |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context | MATCH |
