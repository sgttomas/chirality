# Context: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-01 |
| DeliverableName | ChiralityPermissionOverlay and Mode Mapping |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App/project permission policy, explicit hard-deny inputs, human approvals, project-specific deterministic tools/hooks, client presentation, and daemon conformance.

**InclusionCriteria:** Project authority and policy inputs; App approval UI; project-specific tool acts; affected-client evidence.

**Exclusions:** Generic runtime tool mediation/execution, interruption, operational event persistence, and domain-engine operation semantics.

## Deliverable Scope

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-054, SOW-055, SOW-056, SOW-058 |
| SupportsObjectives | OBJ-005 |
| ContextEnvelopeNotes | App/project authority and conformance slice; generic tool execution remains daemon-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Permission overlay must become capability-forward with explicit hard-deny precedence, not blanket denial.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
