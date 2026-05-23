# Procedure: DEL-08-04 Type 2 Subagent Governance Bridge

## Purpose

Define the operational steps to produce and verify the Type 2 subagent governance bridge for SDK-backed subagent execution.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted source corpus for DEL-08-04 | Available; REF-006 has hash mismatch warning per dispatch. |
| Current deliverable status permits authoring | OPEN at P1/P2 run start. |
| Existing `evaluateSubagentGovernance` behavior or target contract | TBD at implementation time; source docs identify it as authoritative but do not provide the code shape. |
| Permission overlay and hook infrastructure | Required by source sequencing; implementation readiness TBD. |
| SDK `agents` capability verified by R0/R1 probes | Required by PLAN/PRD sequencing; current probe status TBD. |
| Declared upstream dependencies | TBD; dependency extraction deferred by dispatch. |

## Steps

1. Locate the existing `evaluateSubagentGovernance` implementation or define the narrow adapter contract that will call it.
2. Define the governance input required by the bridge: parent session identity, requested candidate agent, requested task scope, context-sealed indicator, pipeline approval indicator, approval reference, persona allowlist result, environment enablement, and requested child tool/cwd constraints.
3. Ensure every required input has a fail-closed default. Missing, malformed, or unknown values must deny or require human ruling.
4. Build or configure SDK `agents` definitions only from allowed Type 2 task-agent instructions.
5. Apply explicit child restrictions to each SDK agent definition, including restricted tools and working directory.
6. Add the SDK `Agent` tool hook or equivalent pre-execution guard.
7. In the hook, call the bridge before SDK subagent execution.
8. Deny execution when the bridge returns denial, when hook execution fails, or when the candidate/tool/cwd configuration cannot be verified.
9. Return structured denial reasons suitable for tests and audit records.
10. Provide handoff fields or callback points for DEL-08-05 to persist parent-child lifecycle records and output artifact paths when execution is enabled.
11. Add table-driven tests for all denial paths and for the allowed path with restricted child tools/cwd.
12. Add regression tests proving SDK defaults, inherited permissions, and `allowedTools` alone cannot authorize delegation.

## Verification

| Check | Expected result |
|---|---|
| Missing governance metadata | Denied; no SDK subagent execution. |
| Missing approval reference | Denied; no SDK subagent execution. |
| Unsealed context | Denied or human-ruling-needed; no ghost-input execution. |
| Non-allowlisted candidate | Denied. |
| Non-Type-2 candidate | Denied. |
| Hook error | Denied fail-closed. |
| Child requests broad tools/cwd | Denied or narrowed to explicit approved restrictions before execution. |
| Allowed governed request | SDK `Agent` execution may proceed only with restricted child tools/cwd and handoff data for child record persistence. |
| Event/persistence handoff | DEL-08-05 can consume bridge/hook result metadata without DEL-08-04 owning full persistence. |

## Records

The implementation should produce or update these records/artifacts:

- bridge module or adapter for `evaluateSubagentGovernance`;
- SDK agent-definition builder or definitions;
- `Agent` hook tests;
- denial fixtures for missing metadata, non-allowlisted candidate, non-Type-2 candidate, unsealed context, missing approval reference, hook error, and broad child capability request;
- allowed-path fixture showing restricted tools/cwd;
- handoff/interface note for DEL-08-05 child run record persistence.

Dependency extraction remains deferred. Do not create `Dependencies.csv` during this procedure.
