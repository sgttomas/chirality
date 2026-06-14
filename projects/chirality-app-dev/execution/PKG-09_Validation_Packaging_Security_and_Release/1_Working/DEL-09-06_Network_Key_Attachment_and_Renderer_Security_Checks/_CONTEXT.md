# Context: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DeliverableID | DEL-09-06 |
| DeliverableName | Network, Key, Attachment, and Renderer Security Checks |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Required checks, CI, Section 8/9 validation, network/key security, macOS DMG packaging.

**InclusionCriteria:** Release readiness and test infrastructure.

**Exclusions:** Feature implementation except test fixtures and packaging glue.

## Deliverable Scope

Verify renderer allowlist, API key redaction/storage, provider endpoint policy, and attachment validation/retry behavior.

## Anticipated Artifacts

Security tests; network guard tests; attachment resolver validation; key storage checks

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-019, SOW-020, SOW-022, SOW-023 |
| SupportsObjectives | OBJ-008 |
| ContextEnvelopeNotes | Security validation family. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Network/key checks must preserve current shipped provider scope and gate future provider expansion.

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
