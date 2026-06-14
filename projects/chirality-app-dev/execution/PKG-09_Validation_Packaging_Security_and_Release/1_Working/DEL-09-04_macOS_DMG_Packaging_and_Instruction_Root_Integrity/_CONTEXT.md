# Context: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DeliverableID | DEL-09-04 |
| DeliverableName | macOS DMG Packaging and Instruction Root Integrity |
| ResponsibleParty | TBD |
| Type | CI_CD_CHANGE |
| ContextEnvelope | L |

## Package Scope

**ScopeDescription:** Required checks, CI, Section 8/9 validation, network/key security, macOS DMG packaging.

**InclusionCriteria:** Release readiness and test infrastructure.

**Exclusions:** Feature implementation except test fixtures and packaging glue.

## Deliverable Scope

Produce the macOS arm64 unsigned DMG and prove required instruction-root assets plus SDK packaging posture are valid.

## Anticipated Artifacts

`desktop:dist`; integrity summary; SDK subprocess packaging probe

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-030, SOW-072, SOW-073 |
| SupportsObjectives | OBJ-008 |
| ContextEnvelopeNotes | Broad packaging slice but bounded to one release target. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Packaging validation remains first-adapter-aware and must not imply Pi or other provider runtime migrations.

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
