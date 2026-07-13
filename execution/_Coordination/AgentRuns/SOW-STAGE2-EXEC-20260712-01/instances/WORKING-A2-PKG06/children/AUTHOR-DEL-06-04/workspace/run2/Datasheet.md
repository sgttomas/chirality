# Datasheet: DEL-06-04 Write/Edit Surface and Path Hooks

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-06-04 |
| Deliverable name | Write/Edit Surface and Path Hooks |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Type | SECURITY_CONTROL |
| Responsible party | TBD |
| Decomposition variant | SOFTWARE_DECOMP v3.2 |
| Context envelope | L |
| Scope items | SOW-027, SOW-057, SOW-060 |
| Objective context | OBJ-005, OBJ-006 |
| Anticipated artifacts | PreToolUse hooks; write/edit tests; provenance metadata; path policy fixtures |

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks", scope ledger rows SOW-027, SOW-057, SOW-060, and objective rows OBJ-005 and OBJ-006.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary control surface | Write/edit execution gate using hooks and runtime path policy | `_CONTEXT.md`; decomposition row DEL-06-04 |
| Hook phase in scope | `PreToolUse` for pre-execution denial and `PostToolUse`/post-failure evidence where applicable | `docs/TYPES.md` Section 8.5; `docs/SPEC.md` Section 15.2 |
| Path containment rule | Filesystem operations outside the active project or working root are denied | `docs/CONTRACT.md` Section 1.6 K-PATH-2; `docs/SPEC.md` Section 15.2 |
| Instruction-root rule | Ordinary project execution must not mutate the instruction root | `docs/CONTRACT.md` Section 1.3 K-ROOT-2; `docs/SPEC.md` Section 1 |
| Symlink rule | Symlink writes are rejected in the initial policy | `docs/CONTRACT.md` Section 1.6 K-PATH-3; `docs/SPEC.md` Section 15.2 |
| Exact edit precondition | Controlled edits require exact edit preconditions before execution | `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Provenance obligation | Successful writes/edits emit diff, summary, provenance, or runtime event evidence | `docs/PLAN.md` R3; `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Deny precedence | Hook, path, policy, SDK deny, governance, and human-gate denials override allows | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |

## Conditions

| Condition | Constraint | Source |
|---|---|---|
| PRD source state | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
| Mode dependency | `workspaceWrite` can use SDK edit acceptance only after write hooks pass; `readOnly` cannot write. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Hook failure policy | Hook failures fail closed for write, shell, domain, and subagent actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| MCP parity | Chirality MCP write tools must pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1 |
| Current MCP write surface | The current source inventory identifies `mcp__chirality__status_transition` and `mcp__chirality__deps_write` as write/gated tools; `mcp__chirality__scaffold` is gated and must be classified before any mutation behavior is enabled. | `docs/SPEC.md` Section 14.2 |
| Adjacent deliverables | Permission mode mapping is owned by DEL-06-01; tool resolver/read MCP surfaces are owned by DEL-06-02 and DEL-06-03; compaction/terminal hook mirroring is owned by DEL-06-06. | decomposition PKG-06 rows |
| Dependency state | `_DEPENDENCIES.md` lists no accepted upstream or downstream edges yet. | `_DEPENDENCIES.md` |

## Construction

| Component | Construction note | Source |
|---|---|---|
| Path policy helper | Resolve and validate candidate write/edit targets against the active project or working root and instruction root. Exact implementation path: TBD. | `docs/CONTRACT.md` Section 1.6 K-PATH-2; `docs/PRD.md` Section 7.9 |
| PreToolUse gate | Deny write/edit attempts before execution when containment, instruction-root, symlink, mode, or permission policy fails. | `docs/SPEC.md` Section 15.2; `docs/TYPES.md` Section 8.5 |
| Exact edit validator | Require exact edit preconditions for edit-style operations before mutation. Exact diff/match algorithm: TBD. | `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Safe write/edit execution | Perform atomic write/edit where practical only after permission and hook gates pass. Atomicity details: TBD. | `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Provenance recorder | Capture safe provenance, diff/summary, permission/runtime events, and source metadata for each write attempt. Exact event fields beyond source docs: TBD. | `docs/PLAN.md` R3; `docs/SPEC.md` Section 15.2 |
| Path policy fixtures | Include fixtures for outside-root targets, instruction-root targets, symlink targets, missing files, stale edit preconditions, allowed in-root writes, and the current MCP write/gated surface. | `_CONTEXT.md`; `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R3 acceptance |
| Tests | Include write/edit tests for denied outside-root writes, denied instruction-root writes, denied symlink writes, exact edit preconditions, provenance evidence, MCP parity, and PRD warning carry-forward. Exact test paths: TBD. | `_CONTEXT.md`; `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R3 acceptance; `_REFERENCES.md` REF-006 |

## References

| RefID | Source | Use | Source state |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` Sections 2, 4, 7 | Reliance boundary and provenance principles | MATCH |
| REF-002 | `docs/CONTRACT.md` Sections 1.3, 1.6, 1.7 | Binding root, permission, hook, path, MCP, and write-scope invariants | MATCH |
| REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool surface rules, mode mapping, required hooks, validation IDs | MATCH |
| REF-004 | `docs/TYPES.md` Section 8 | Permission modes, tool terms, hook terms, event names | MATCH |
| REF-005 | `docs/PLAN.md` R2/R3 and risk table | Sequencing and acceptance context | MATCH |
| REF-006 | `docs/PRD.md` Sections 7.9, 9.4, R2/R3, NFRs | Product requirements and implementation direction | MATCH status — reconciled under D-APP-38 |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |
