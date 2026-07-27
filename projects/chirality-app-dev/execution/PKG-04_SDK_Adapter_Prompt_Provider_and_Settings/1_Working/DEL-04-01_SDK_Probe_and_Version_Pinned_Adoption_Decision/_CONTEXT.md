# Context: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-01 |
| DeliverableName | First-Adapter Probe and Version-Pinned Adoption Decision |
| ResponsibleParty | TBD |
| Type | REQ_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App integration, project-input composition, packaged-daemon credential-boundary participation, provider-adapter compatibility, settings isolation, and conformance evidence.

**InclusionCriteria:** First-adapter probe; App client/packaging integration; prompt/project inputs; provider and settings conformance.

**Exclusions:** Generic adapters, engines, credentials, residency, and unresolved generic-versus-private component classification.

## Deliverable Scope

Confirm App packaged-daemon/client compatibility with the first Root-runtime adapter, including version, messages, policy inputs, hooks, project MCP acts, session linkage, interruption, packaging, conformance, and unresolved component-classification risks.

## Anticipated Artifacts

App first-adapter client probe; version decision; conformance criteria; component-classification open items; residual-risk notes

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-018, SOW-044, SOW-046 |
| SupportsObjectives | OBJ-004 |
| ContextEnvelopeNotes | App client/probe slice; no generic adapter ownership or new tool exposure. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: First-adapter probe must be framed as Claude Agent SDK / Anthropic within provider-adapter architecture, not permanent provider scope.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## D-APP-56 approving-role deferral (2026-07-12)

R4-P47 explicitly defers assignment of the adoption-verdict approving role. The field remains `TBD` until an accountable human assigns it; no agent role is inferred.

## D-APP-65 approving-role assignment (2026-07-18)

D-APP-65 assigned the adoption-verdict approving role (`ADOPT`, `ADOPT_WITH_RESIDUAL_RISK`, or `FALLBACK`) to Ryan Tufts (K-AUTH-1), scoped to the demonstrator context of this repository. This supersedes the D-APP-56 R4-P47 deferral above prospectively; the deferral remains preserved as dated history. The assignment names the accountable human only — no adoption verdict, acceptance, or issuance is rendered by it; the verdict itself remains a separate future owner act.

## D-APP-68 adoption verdict (2026-07-19)

Ryan Tufts (K-AUTH-1) rendered `ADOPT_WITH_RESIDUAL_RISK` for the repository
demonstrator, pinned to `@anthropic-ai/claude-agent-sdk@0.3.150` and observed
Claude Code `2.1.150`. The D-APP-65 paragraph above remains dated pre-ruling
history; its “future owner act” condition is discharged by D-APP-68
recommendation 8. See
`Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` for the twelve residual
assessments and fallback triggers. The verdict is not release approval,
issuance, certification, professional acceptance, signing, notarization,
publication, or external distribution, and it does not alter
`ResponsibleParty: TBD` or the deliverable lifecycle.
