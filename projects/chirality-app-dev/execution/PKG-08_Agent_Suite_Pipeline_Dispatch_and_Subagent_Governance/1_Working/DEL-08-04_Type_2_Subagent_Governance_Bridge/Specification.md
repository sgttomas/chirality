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

## Documentation

Required artifacts for this deliverable:

- `evaluateSubagentGovernance` bridge;
- SDK agent definitions or deterministic definition builder;
- `Agent` hook tests;
- denial/restriction fixtures;
- handoff notes or typed interface for DEL-08-05 child-run persistence.

## Conflict Table (for human ruling)

| Conflict ID | Source A | Source B | Issue | Proposed handling |
|---|---|---|---|---|
| C-001 | `_REFERENCES.md` expected PRD SHA | `_REFERENCES.md` actual PRD SHA | PRD hash mismatch exists. Dispatch explicitly says to treat it as a source warning, not a blocker. | Proceeded with REF-006 as warning; human may later decide whether to refresh the accepted snapshot/hash. |
