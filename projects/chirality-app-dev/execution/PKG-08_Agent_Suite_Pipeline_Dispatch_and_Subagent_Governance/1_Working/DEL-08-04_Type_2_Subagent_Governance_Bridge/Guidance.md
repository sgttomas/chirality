# Guidance: DEL-08-04 Type 2 Subagent Governance Bridge

## Purpose

This deliverable exists to let Chirality use SDK subagent mechanics while keeping Type 2 delegation under Chirality governance. The bridge should make delegation possible only when the product-owned gate says the request is allowed, the child context is sealed, the candidate is eligible, approvals are traceable, and child capabilities are narrower than or equal to the permitted boundary.

## Principles

| Principle | Guidance |
|---|---|
| Deny first | Treat any missing governance metadata, unknown candidate status, hook error, unsealed context, missing approval reference, or unsupported state as denial or human-ruling-needed. Do not infer permission from SDK defaults. |
| Chirality owns semantics | SDK `agents`, `Agent` tool behavior, permission modes, and transcripts are implementation details. Public runtime contracts, audit events, and governance decisions remain Chirality-owned. |
| No capability inheritance by accident | A child subagent should receive an explicit restricted tool list and cwd. It should not inherit parent capabilities implicitly, and it should not broaden parent authority. |
| Sealed context only | Type 2 task-agent context is limited to folder contents and declared references. Avoid "ghost inputs" that are not in the sealed brief or declared sources. |
| Approval is evidence, not vibes | The approval reference must be non-empty and traceable. If the approval reference is absent or ambiguous, the bridge should deny. |
| Separate gate from record persistence | This slice owns bridge and hook behavior. Full parent-child record persistence and output artifact-path storage should be handed to DEL-08-05 through a clear interface. |

## Considerations

- The PLAN places governed subagent runtime after earlier engine, permission, tool, hook, and result-storage work. If those prerequisites are absent or unstable, the bridge should remain disabled or deny execution.
- `allowedTools` alone is not a restriction boundary. Restrictions require disallowed tools, permission mode, hooks, and overlay policy.
- Hook failures fail closed for subagent actions. This should include bridge exceptions, missing policy inputs, malformed approval references, and failed candidate resolution.
- The candidate resolver should prefer explicit `AGENT_TYPE: 2` and task-agent metadata. If an instruction file is ambiguous, classify it as ineligible until a human or conformance validator resolves it.
- Child cwd should be the approved bounded working root for the task, not the instruction root and not a broad ambient workspace.
- The bridge should produce denial reasons suitable for audit and tests without leaking sensitive prompt or environment data.

## Trade-offs

| Trade-off | Preferred direction |
|---|---|
| Convenience vs. safety | Prefer denial over opportunistic delegation when governance metadata is incomplete. |
| SDK-native shape vs. product contract | Wrap SDK-native fields behind Chirality types so later SDK changes do not redefine product behavior. |
| Broad child capability vs. bounded execution | Prefer narrow child tool/cwd definitions generated from the approved Type 2 task scope. |
| Bridge-only scope vs. record persistence | Keep this deliverable focused on gate/hook/definition behavior and expose a minimal handoff to DEL-08-05 for lifecycle records. |

## Examples

| Scenario | Expected outcome |
|---|---|
| Delegation request lacks approval reference | Denied before SDK `Agent` execution. |
| Candidate agent is not on the persona allowlist | Denied before SDK `Agent` execution. |
| Candidate instruction is Type 1 or lacks `AGENT_TYPE: 2` | Denied as non-Type-2 candidate. |
| Context is not sealed or includes undeclared references | Denied or human-ruling-needed; do not execute with ghost inputs. |
| Child tool list requests write/bash beyond approved scope | Denied or reduced to explicit approved tools; do not inherit parent capability. |
| Hook throws during governance evaluation | Denied with fail-closed hook outcome. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Impact | Human ruling needed |
|---|---|---|---|
| C-001 | REF-006 PRD hash mismatch is present but dispatch says it is a warning, not a blocker. | Source acceptance state should be refreshed or waived in a later governance pass. | Confirm whether to update the expected PRD hash or preserve the warning for downstream review. |

## Open Items

| Item | Status |
|---|---|
| Exact TypeScript module/file names for the bridge and SDK agent-definition builder | TBD |
| Exact serialized shape of the governance decision object | TBD; should align with existing `evaluateSubagentGovernance` implementation and Chirality runtime event schema. |
| Exact approval reference format | TBD; must be non-empty and traceable to human/gate evidence. |
| Exact interface boundary with DEL-08-05 | TBD; should carry child lifecycle metadata and output artifact-path hooks without duplicating persistence ownership. |
