# Specification: DEL-08-04 Type 2 Subagent Governance Bridge

## Scope

This deliverable specifies a backend feature slice that connects Chirality's fail-closed Type 2 subagent governance to SDK-backed subagent execution. It covers:

- generation or assembly of SDK `agents` definitions from allowed Type 2 task-agent instructions;
- the `evaluateSubagentGovernance` bridge used as the authoritative delegation gate;
- `Agent` tool hook behavior that fails closed before SDK subagent execution;
- restrictions on child tool lists and child working directory;
- tests proving denial and restriction behavior.

This deliverable excludes:

- general SDK adapter mechanics outside the subagent bridge;
- persistence of full parent-child runtime records and output artifact paths, except for interface handoff points to DEL-08-05;
- dependency extraction and `Dependencies.csv` creation.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-08-04-R01 | The bridge MUST call `evaluateSubagentGovernance` as the authoritative fail-closed gate before SDK `Agent` subagent execution. | `docs/TYPES.md` Section 10; `docs/SPEC.md` Section 15.2; `docs/PLAN.md` R5 |
| DEL-08-04-R02 | Delegation MUST be denied unless environment enablement, persona allowlist, context sealing, pipeline approval, approval reference, and Type 2 eligibility all pass. | `docs/CONTRACT.md` K-SUBAGENT-1; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R03 | Delegation without governance metadata MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R04 | Delegation to a non-allowlisted candidate MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R05 | Delegation to a non-Type-2 candidate MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R06 | SDK `agents` definitions MUST be generated or selected only from allowed Type 2 task-agent instructions. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R07 | Child subagents MUST use restricted tool lists and restricted cwd; they MUST NOT inherit or expand capabilities beyond parent governance. | `docs/CONTRACT.md` K-SUBAGENT-2; `docs/PLAN.md` R5 |
| DEL-08-04-R08 | Hook failures for subagent actions MUST fail closed. | `docs/CONTRACT.md` K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| DEL-08-04-R09 | The bridge MUST preserve Chirality-owned runtime semantics rather than treating SDK defaults, SDK transcript shape, SDK tool names, or SDK permission modes as product authority. | `docs/DIRECTIVE.md` Sections 7-8; `docs/PRD.md` Principles 9-10 |
| DEL-08-04-R10 | Unknown values or unsupported facts in governance metadata MUST produce `TBD`, denial, or human-ruling-needed behavior rather than guessed allow decisions. | `docs/CONTRACT.md` K-INVENT-1; `docs/CONTRACT.md` K-CONFLICT-1 |
| DEL-08-04-R11 | The bridge SHOULD expose a clear interface for DEL-08-05 to persist parent-child lifecycle records and output artifact references when execution is enabled. | `docs/CONTRACT.md` K-SUBAGENT-3; decomposition DEL-08-05 |

## Governance Decision Contract

The exact serialized decision-object type is `TBD` until implementation locates or defines the `evaluateSubagentGovernance` contract. The accepted contract must, at minimum, preserve these product-owned semantics without becoming SDK-shaped:

| Field family | Required content | Source |
|---|---|---|
| Decision behavior | `allow`, `deny`, or application-level `ask`/human-ruling-needed outcome; deny overrides allow. | `docs/PRD.md` FR-087, FR-089; `docs/CONTRACT.md` K-PERM-1 |
| Denial reason | Audit-suitable reason code and summary that are stable enough for tests and do not leak sensitive prompt or environment data. | `docs/PRD.md` FR-092; `Guidance.md` Considerations |
| Decision source | Whether the outcome came from Chirality policy, hook, governance gate, SDK callback, or human gate. | `docs/PRD.md` FR-087, FR-092; `docs/TYPES.md` Section 8.2 |
| Approval reference | Non-empty human/gate evidence string when delegation is allowed; missing or ambiguous approval references deny. | `docs/TYPES.md` Section 10; `docs/CONTRACT.md` K-AUTH-1, K-AUTH-2 |
| Candidate and scope facts | Candidate agent identity, Type 2 eligibility result, allowlist result, context-sealed result, requested tools, restricted tools, requested cwd, and approved cwd. | `docs/TYPES.md` Section 10; `docs/PLAN.md` R5 |
| DEL-08-05 handoff | Parent session/turn identifiers and child lifecycle/output-reference hooks sufficient for DEL-08-05 to persist child records without this deliverable owning persistence. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |

## Standards

| Standard or contract | Applicability |
|---|---|
| `docs/CONTRACT.md` K-SEAL-1, K-GHOST-1, K-SUBAGENT-1, K-SUBAGENT-2, K-SUBAGENT-3 | Core subagent governance invariants. |
| `docs/SPEC.md` Sections 14-15 | Tool surface, permission modes, and hook requirements. |
| `docs/TYPES.md` Section 10 | Canonical subagent vocabulary and `evaluateSubagentGovernance` meaning. |
| `docs/PLAN.md` R5 | Implementation sequencing, targets, and acceptance criteria. |
| `docs/PRD.md` Section 8.15 | User/runtime behavior for governed delegation. |
| `AGENT_SOFTWARE_DECOMP.md` deliverable sizing rules | Confirms Type 2 deliverables are bounded executable units; no sub-task level should be invented. |

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-08-04-R01 | Unit or integration test proves `Agent` hook invokes `evaluateSubagentGovernance` before execution and denies on gate failure. |
| DEL-08-04-R02 | Table-driven tests cover each missing governance condition: environment enablement, persona allowlist, context sealing, pipeline approval, approval reference, and Type 2 eligibility. |
| DEL-08-04-R03 | Test missing/empty governance metadata produces denial and no child execution. |
| DEL-08-04-R04 | Test non-allowlisted candidate produces denial. |
| DEL-08-04-R05 | Test candidate without `AGENT_TYPE: 2` or acceptable Type 2 task metadata produces denial. |
| DEL-08-04-R06 | Fixture test proves SDK `agents` definitions are limited to allowed Type 2 task-agent instructions. |
| DEL-08-04-R07 | Fixture or integration test proves child tool list and cwd are restricted and cannot broaden parent governance. |
| DEL-08-04-R08 | Hook failure test proves fail-closed denial. |
| DEL-08-04-R09 | Contract test verifies bridge inputs/outputs use Chirality-owned types and do not expose SDK-specific state as product authority. |
| DEL-08-04-R10 | Negative tests prove missing or unknown governance values deny or require human ruling. |
| DEL-08-04-R11 | Interface test or type test verifies handoff fields needed by DEL-08-05 are available without this deliverable owning persistence. |

The concrete fixture paths, passing test names, and local/CI commands are `TBD` until the implementation task selects module paths. Before implementation closure, verification evidence must name fixtures for missing metadata, missing approval reference, unsealed context, non-allowlisted candidate, non-Type-2 candidate, hook error, broad child capability request, allowed restricted execution, audit-safe denial reasons, and DEL-08-05 handoff fields.

## Documentation

Required artifacts for this deliverable:

- `evaluateSubagentGovernance` bridge;
- SDK agent definitions or deterministic definition builder;
- `Agent` hook tests;
- denial/restriction fixtures;
- handoff notes or typed interface for DEL-08-05 child-run persistence.
- implementation path record naming the bridge module, SDK agent-definition builder, `Agent` hook module, fixture directory, runnable test command, and output evidence location, or an explicit blocking `TBD` if any path is not yet selected.

## Conflict Table (for human ruling)

| Conflict ID | Source A | Source B | Issue | Proposed handling |
|---|---|---|---|---|
| C-001 | `_REFERENCES.md` REF-006 | D-APP-38 authority corpus | Former PRD source-state warning is resolved for this tranche. | Use PRD-derived subagent governance text under D-APP-38; keep implementation proof separate from source-state proof. |
