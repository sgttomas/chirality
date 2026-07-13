# Datasheet: DEL-06-05 Bash Governance and Timeout Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-06-05 |
| Deliverable name | Bash Governance and Timeout Policy |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Type | SECURITY_CONTROL |
| Responsible party | TBD |
| Decomposition variant | SOFTWARE_DECOMP v3.2 |
| Context envelope | M |
| Scope items | SOW-062 |
| Objective context | OBJ-005 |
| Anticipated artifacts | Bash deny/default tests; timeout/capture policy; output metadata tests |

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger row SOW-062.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Governed tool | SDK built-in `Bash` where available | `docs/SPEC.md` Section 14.1 |
| Default posture | Bash denied by default even though the SDK ships the tool | `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
| Enablement prerequisites | Timeout, output capture, result storage, interrupt behavior, and audit events | `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4 |
| Denied modes | `readOnly` and `dontAsk` deny Bash/shell unless a future governed rule says otherwise | `docs/CONTRACT.md` Section 1.6 K-PERM-4 and K-PERM-5; `docs/PLAN.md` R4 acceptance |
| Restriction mechanism | `allowedTools` is not sufficient; restriction requires disallowed tools, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| Permission decision record | `HarnessPermissionDecision` with decision, reason, source, timestamp, and optional safe metadata | `docs/TYPES.md` Section 8.2 |
| Tool result policy | Small outputs inline; medium/large outputs previewed or stored as session artifacts with metadata | `docs/PRD.md` FR-096, MATCH status; `docs/PLAN.md` R4 — reconciled under D-APP-38 |
| Audit mirror | `.chirality/sessions/<sessionId>/events.jsonl` remains the product-owned audit record | `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/PRD.md` FR-121, MATCH status — reconciled under D-APP-38 |

## Conditions

| Condition | Constraint | Source |
|---|---|---|
| PRD source state | `docs/PRD.md` is accessible but has MATCH in `_REFERENCES.md`; PRD-derived details are treated as source-state evidence, not as unqualified accepted truth. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
| Bash before R4 readiness | Bash must not be exposed before governance, hooks, event logging, result storage, timeout, audit logging, and packaging checks are reliable. | `docs/DIRECTIVE.md` Section 4.2; `docs/PLAN.md` R4 |
| Denied execution | Denied Bash must not spawn. | `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
| Timeout value | Exact default timeout and override semantics are TBD; source material requires a timeout but does not provide a Bash-specific value. | `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4 |
| Output channels | Allowed Bash captures stdout and stderr separately. | `docs/PLAN.md` R4 implementation targets; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
| Interrupt behavior | Allowed Bash can be interrupted when possible; exact SDK/process mechanics are TBD. | `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |

## Construction

| Component | Construction note | Source |
|---|---|---|
| Tool-surface resolver | Expose `Bash` only when session/persona/mode/options/policy permit it; otherwise omit or hard-deny. | `docs/SPEC.md` Sections 13.2, 14.3, and 15.1 |
| Deny policy | Explicit denies from policy, path containment, hooks, governance, SDK deny rules, or human gates block Bash execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
| Bash preflight | Enforce mode, command name/length, timeout, redirection/path-token counts, output capture, network-command and URL-scheme posture, and audit metadata before spawning. | `frontend/src/lib/harness/tool-shell-policy.ts`; `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
| Execution capture | Capture stdout and stderr separately and classify terminal outcome as success, failure, timeout, interruption, or cancellation where available. | `docs/PLAN.md` R4; `docs/SPEC.md` Section 10.1 |
| Result storage | Apply `ToolResultStore` policy so large output is stored under session artifacts and represented by preview plus schema-versioned metadata: tool/use/turn IDs, byte lengths, truncation, SHA-256, relative path, and stdout/stderr stream labels. | D-APP-42; `frontend/src/lib/harness/tool-result-artifacts.ts`; `frontend/src/lib/harness/tool-evidence.ts` |
| Audit events | Persist permission, started, completed/failed, interruption/timeout, and artifact metadata in Chirality-owned events; an SDK Bash result with `interrupted: true` maps to `tool.failed` with safe stream/artifact evidence. | ADQ-11; D-APP-43; `frontend/src/lib/harness/sdk-message-mapper.ts` |
| Tests | Include deny/default tests, timeout/capture tests, output metadata tests, and denied-never-spawns tests. Exact test paths: TBD. | `_CONTEXT.md`; `docs/PLAN.md` R4 acceptance |

## References

| RefID | Source | Use | Source state |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` Sections 2.8, 2.9, 4.1, 4.2, and 5 | Product-owned runtime governance, reliance boundaries, bash exposure sequencing | MATCH |
| REF-002 | `docs/CONTRACT.md` Sections 1.5 and 1.6 | Binding event, permission, hook, path, and Bash invariants | MATCH |
| REF-003 | `docs/SPEC.md` Sections 10, 13, 14, and 15 | Engine responsibilities, option/tool resolution, tool names, mode mapping, hooks | MATCH |
| REF-004 | `docs/TYPES.md` Sections 7 and 8 | Event vocabulary, permission modes, decision records, tool terms, artifact path fields | MATCH |
| REF-005 | `docs/PLAN.md` R4 | Sequencing, implementation targets, and Bash acceptance criteria | MATCH |
| REF-006 | `docs/PRD.md` Sections 8.15 and R4 | Product requirements for Bash, result storage, context mirror, and audit behavior | MATCH status — reconciled under D-APP-38 |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |
