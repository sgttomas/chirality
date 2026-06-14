# Context: DEL-09-03 Unit and Integration Test Expansion

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DeliverableID | DEL-09-03 |
| DeliverableName | Unit and Integration Test Expansion |
| ResponsibleParty | TBD |
| Type | TEST_SUITE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Required checks, CI, Section 8/9 validation, network/key security, macOS DMG packaging.

**InclusionCriteria:** Release readiness and test infrastructure.

**Exclusions:** Feature implementation except test fixtures and packaging glue.

## Deliverable Scope

Add focused unit/API/integration tests for TurnEngine, SSE, event replay, attachments, status, dependencies, interrupts, and denied actions.

## Anticipated Artifacts

Jest/API/integration tests; fixtures; regression cases

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029 |
| SupportsObjectives | OBJ-002, OBJ-003, OBJ-006, OBJ-008 |
| ContextEnvelopeNotes | Cross-cutting tests, but bounded to named behaviors. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Unit/integration tests must target provider-neutral contracts and explicit hard-deny precedence where applicable.

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
