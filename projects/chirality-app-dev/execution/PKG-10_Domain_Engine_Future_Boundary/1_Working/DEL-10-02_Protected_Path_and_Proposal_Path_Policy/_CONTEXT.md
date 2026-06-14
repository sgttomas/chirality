# Context: DEL-10-02 Protected Path and Proposal Path Policy

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-10 |
| PackageName | Domain Engine Future Boundary |
| DeliverableID | DEL-10-02 |
| DeliverableName | Protected Path and Proposal Path Policy |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Generic domain profiles, protected paths, operation proposals, OpenPipeStress fixture posture.

**InclusionCriteria:** Future platform compatibility.

**Exclusions:** Current-release domain operation execution.

## Deliverable Scope

Define future path policy so agents write proposals/summaries but not protected domain-engine model truth.

## Anticipated Artifacts

Protected/proposal path policy; hook implications; examples

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-068 |
| SupportsObjectives | OBJ-010 |
| ContextEnvelopeNotes | Security boundary slice. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Protected/proposal path policy must preserve explicit hard-deny precedence for domain truth and protected paths.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
