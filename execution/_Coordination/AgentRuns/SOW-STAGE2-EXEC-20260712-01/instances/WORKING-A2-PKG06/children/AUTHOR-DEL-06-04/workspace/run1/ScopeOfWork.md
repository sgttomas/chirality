---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-04
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-027, SOW-057, SOW-060]
package_objective_refs: [OBJ-005, OBJ-006]
---

# Scope of Work — DEL-06-04

## Purpose and Objective Traceability

This migration candidate defines `DEL-06-04` in service of project scope [SOW-027, SOW-057, SOW-060] and package objectives [OBJ-005, OBJ-006].

- **OUT-001** — Write/edit execution gate, PreToolUse hooks, write/edit tests, provenance metadata, and path policy fixtures.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-04 Write/Edit Surface and Path Hooks

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"0ddde6412e5cca890175cfeffb666ed276f16e53ef590af6a438103e0521c344","target_id":"CLM-001"} -->
#### Datasheet: DEL-06-04 Write/Edit Surface and Path Hooks

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":21,"line_start":5,"source_sha256":"0ddde6412e5cca890175cfeffb666ed276f16e53ef590af6a438103e0521c344","target_id":"CLM-002"} -->
##### Identification

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

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":34,"line_start":22,"source_sha256":"0ddde6412e5cca890175cfeffb666ed276f16e53ef590af6a438103e0521c344","target_id":"CLM-003"} -->
##### Attributes

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

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":46,"line_start":35,"source_sha256":"0ddde6412e5cca890175cfeffb666ed276f16e53ef590af6a438103e0521c344","target_id":"CLM-004"} -->
##### Conditions

| Condition | Constraint | Source |
|---|---|---|
| PRD source state | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
| Mode dependency | `workspaceWrite` can use SDK edit acceptance only after write hooks pass; `readOnly` cannot write. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Hook failure policy | Hook failures fail closed for write, shell, domain, and subagent actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| MCP parity | Chirality MCP write tools must pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1 |
| Current MCP write surface | The current source inventory identifies `mcp__chirality__status_transition` and `mcp__chirality__deps_write` as write/gated tools; `mcp__chirality__scaffold` is gated and must be classified before any mutation behavior is enabled. | `docs/SPEC.md` Section 14.2 |
| Adjacent deliverables | Permission mode mapping is owned by DEL-06-01; tool resolver/read MCP surfaces are owned by DEL-06-02 and DEL-06-03; compaction/terminal hook mirroring is owned by DEL-06-06. | decomposition PKG-06 rows |
| Dependency state | `_DEPENDENCIES.md` lists no accepted upstream or downstream edges yet. | `_DEPENDENCIES.md` |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":58,"line_start":47,"source_sha256":"0ddde6412e5cca890175cfeffb666ed276f16e53ef590af6a438103e0521c344","target_id":"CLM-005"} -->
##### Construction

| Component | Construction note | Source |
|---|---|---|
| Path policy helper | Resolve and validate candidate write/edit targets against the active project or working root and instruction root. Exact implementation path: TBD. | `docs/CONTRACT.md` Section 1.6 K-PATH-2; `docs/PRD.md` Section 7.9 |
| PreToolUse gate | Deny write/edit attempts before execution when containment, instruction-root, symlink, mode, or permission policy fails. | `docs/SPEC.md` Section 15.2; `docs/TYPES.md` Section 8.5 |
| Exact edit validator | Require exact edit preconditions for edit-style operations before mutation. Exact diff/match algorithm: TBD. | `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Safe write/edit execution | Perform atomic write/edit where practical only after permission and hook gates pass. Atomicity details: TBD. | `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| Provenance recorder | Capture safe provenance, diff/summary, permission/runtime events, and source metadata for each write attempt. Exact event fields beyond source docs: TBD. | `docs/PLAN.md` R3; `docs/SPEC.md` Section 15.2 |
| Path policy fixtures | Include fixtures for outside-root targets, instruction-root targets, symlink targets, missing files, stale edit preconditions, allowed in-root writes, and the current MCP write/gated surface. | `_CONTEXT.md`; `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R3 acceptance |
| Tests | Include write/edit tests for denied outside-root writes, denied instruction-root writes, denied symlink writes, exact edit preconditions, provenance evidence, MCP parity, and PRD warning carry-forward. Exact test paths: TBD. | `_CONTEXT.md`; `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R3 acceptance; `_REFERENCES.md` REF-006 |

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":69,"line_start":59,"source_sha256":"0ddde6412e5cca890175cfeffb666ed276f16e53ef590af6a438103e0521c344","target_id":"CLM-006"} -->
##### References

| RefID | Source | Use | Source state |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` Sections 2, 4, 7 | Reliance boundary and provenance principles | MATCH |
| REF-002 | `docs/CONTRACT.md` Sections 1.3, 1.6, 1.7 | Binding root, permission, hook, path, MCP, and write-scope invariants | MATCH |
| REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool surface rules, mode mapping, required hooks, validation IDs | MATCH |
| REF-004 | `docs/TYPES.md` Section 8 | Permission modes, tool terms, hook terms, event names | MATCH |
| REF-005 | `docs/PLAN.md` R2/R3 and risk table | Sequencing and acceptance context | MATCH |
| REF-006 | `docs/PRD.md` Sections 7.9, 9.4, R2/R3, NFRs | Product requirements and implementation direction | MATCH status — reconciled under D-APP-38 |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-06-04 Write/Edit Surface and Path Hooks

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"678ebd69cec8cf7bee7b162769ce0be9bcc2d463f473a136300e34d45699d9e2","target_id":"CLM-007"} -->
#### Specification: DEL-06-04 Write/Edit Surface and Path Hooks

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-008 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":28,"line_start":5,"source_sha256":"678ebd69cec8cf7bee7b162769ce0be9bcc2d463f473a136300e34d45699d9e2","target_id":"CLM-008"} -->
##### Scope

DEL-06-04 specifies the write/edit execution surface and path hooks needed to permit controlled workspace writes without relying on prompt text, SDK defaults, or `allowedTools` alone. It covers project-root or working-root containment, instruction-root write blocking, symlink write rejection, exact edit preconditions, and provenance hooks for write/edit attempts.

In scope:

- Gate SDK `Write`/`Edit` and Chirality MCP write tools before mutation.
- Enforce active project or working-root containment.
- Block instruction-root writes during ordinary project execution.
- Reject symlink writes in the initial policy.
- Require exact edit preconditions before edit-style mutation.
- Record safe provenance, diff/summary, permission/runtime event evidence, and hook outcomes.
- Provide path policy fixtures and write/edit tests for allowed and denied cases.

Out of scope:

- Permission overlay mode semantics and `canUseTool` approval mediation owned by DEL-06-01, except where their decisions feed this hook.
- Read tool exposure, read MCP wrappers, unknown-tool validation, and deterministic tool ordering owned by DEL-06-02 and DEL-06-03.
- Bash governance owned by DEL-06-05.
- Hook lifecycle and compaction mirror details owned by DEL-06-06, except for write/edit hook evidence needed by this deliverable.
- Domain-engine protected-path operation semantics, except where a protected path hook implication is shared with future path policy.

Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/CONTRACT.md` Sections 1.3 and 1.6; `docs/SPEC.md` Sections 14 and 15; `docs/PRD.md` Section 7.9 with MATCH status. (reconciled under D-APP-38).

<!-- sow-source-end -->

### CLM-009 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":49,"line_start":29,"source_sha256":"678ebd69cec8cf7bee7b162769ce0be9bcc2d463f473a136300e34d45699d9e2","target_id":"CLM-009"} -->
##### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-06-04-REQ-001 | The runtime MUST run a pre-execution hook or equivalent gate before any write/edit mutation is performed. | decomposition SOW-057; `docs/SPEC.md` Section 15.2 |
| DEL-06-04-REQ-002 | The write/edit gate MUST deny filesystem operations outside the active project or working root. | decomposition SOW-027; `docs/CONTRACT.md` Section 1.6 K-PATH-2 |
| DEL-06-04-REQ-003 | The write/edit gate MUST deny ordinary project writes under the instruction root. | decomposition SOW-027; `docs/CONTRACT.md` Section 1.3 K-ROOT-2 |
| DEL-06-04-REQ-004 | The write/edit gate MUST reject symlink writes in the initial policy. | decomposition SOW-060; `docs/CONTRACT.md` Section 1.6 K-PATH-3 |
| DEL-06-04-REQ-005 | Edit-style operations MUST require exact edit preconditions before mutation. | decomposition SOW-060; `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| DEL-06-04-REQ-006 | Hook failures MUST fail closed for write/edit actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| DEL-06-04-REQ-007 | Explicit denies from policy, path containment, hook, governance, SDK deny rule, or human gate MUST override any allow. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
| DEL-06-04-REQ-008 | `allowedTools` MUST NOT be treated as sufficient restriction or safety boundary for write/edit capability. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| DEL-06-04-REQ-009 | `readOnly` mode MUST deny write/edit capability, and `workspaceWrite` MUST allow governed writes only after hooks and policy pass. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| DEL-06-04-REQ-010 | In-process Chirality MCP write/gated tools MUST pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins before mutation behavior is enabled. Current source inventory includes `mcp__chirality__status_transition`, `mcp__chirality__deps_write`, and gated `mcp__chirality__scaffold` classification. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2 |
| DEL-06-04-REQ-011 | Successful controlled writes/edits SHOULD be atomic where practical and MUST emit a diff or summary suitable for audit. | `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| DEL-06-04-REQ-012 | Every write attempt MUST produce permission/runtime event evidence or equivalent audit records, including denials. | `docs/PLAN.md` R3 acceptance; `docs/PRD.md` Section 7.9, MATCH status — reconciled under D-APP-38 |
| DEL-06-04-REQ-013 | Provenance append hooks MUST record safe provenance/run evidence where policy requires it. | `docs/SPEC.md` Section 15.2 |
| DEL-06-04-REQ-014 | Path validation SHOULD include regular-file and symlink checks for attachment/write-relevant paths where applicable. | `docs/SPEC.md` attachment/path validation bullets; decomposition SOW-060 |
| DEL-06-04-REQ-015 | Tests MUST cover outside-root denial, instruction-root denial, symlink denial, stale or missing exact edit preconditions, allowed in-root write/edit behavior, and provenance/event evidence. | `_CONTEXT.md`; `docs/PLAN.md` R3 acceptance |
| DEL-06-04-REQ-016 | Acceptance evidence MUST keep PRD-derived controlled-write behavior warning-qualified under the reconciled D-APP-38 source state or a governed hash-bypass record is accepted. | `_REFERENCES.md` REF-006; `docs/CONTRACT.md` Section 1.7 K-REF-1 |

<!-- sow-source-end -->

### CLM-010 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":59,"line_start":50,"source_sha256":"678ebd69cec8cf7bee7b162769ce0be9bcc2d463f473a136300e34d45699d9e2","target_id":"CLM-010"} -->
##### Standards

| Standard or governing source | Applicability |
|---|---|
| `docs/CONTRACT.md` Sections 1.3 and 1.6 | Binding root, permission, hook, MCP, and path invariants. |
| `docs/SPEC.md` Sections 14 and 15 | Tool surface rules, mode mapping, and required hook behavior. |
| `docs/TYPES.md` Section 8 | Permission mode vocabulary, tool surface terms, and hook terms. |
| `docs/PLAN.md` R3 | Controlled write/edit sequencing and acceptance criteria. |
| `docs/PRD.md` Section 7.9 | Controlled write/edit product flow; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-011 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":77,"line_start":60,"source_sha256":"678ebd69cec8cf7bee7b162769ce0be9bcc2d463f473a136300e34d45699d9e2","target_id":"CLM-011"} -->
##### Verification

| Requirement | Verification approach |
|---|---|
| DEL-06-04-REQ-001, REQ-006 | Unit or integration tests inject hook pass/fail outcomes and assert no mutation occurs when the hook fails or is unavailable. |
| DEL-06-04-REQ-002 | Path containment tests attempt outside-root absolute and traversal-equivalent targets and assert denial before mutation. |
| DEL-06-04-REQ-003 | Instruction-root fixtures assert writes under the instruction root are denied during ordinary project execution. |
| DEL-06-04-REQ-004 | Symlink fixtures assert symlink targets and symlink path segments are rejected in the initial policy. |
| DEL-06-04-REQ-005 | Edit tests assert stale, missing, or non-exact preconditions do not mutate files. |
| DEL-06-04-REQ-007, REQ-008 | Precedence tests assert SDK allows, `allowedTools`, or session allows cannot override Chirality deny policy. |
| DEL-06-04-REQ-009 | Mode tests assert `readOnly` cannot write and `workspaceWrite` writes only after permission and hook gates pass. |
| DEL-06-04-REQ-010 | MCP parity tests assert `mcp__chirality__status_transition`, `mcp__chirality__deps_write`, gated `mcp__chirality__scaffold` if mutation-capable, and future write MCP tools pass through equivalent gates. |
| DEL-06-04-REQ-011, REQ-013 | Successful-write tests assert diff/summary and provenance metadata are produced without leaking unsafe data. |
| DEL-06-04-REQ-012 | Runtime event tests assert allowed and denied write attempts produce permission/runtime evidence. |
| DEL-06-04-REQ-014 | Path fixture tests cover regular-file, symlink, extension, and validation failure cases where those checks apply. |
| DEL-06-04-REQ-015 | Test index or validation marker references this deliverable and includes the required negative and positive fixtures. |
| DEL-06-04-REQ-016 | Source-state verifier asserts PRD-derived requirements remain annotated with REF-006 MATCH until the reference hash is reconciled or an accepted bypass record exists. — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-012 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":90,"line_start":78,"source_sha256":"678ebd69cec8cf7bee7b162769ce0be9bcc2d463f473a136300e34d45699d9e2","target_id":"CLM-012"} -->
##### Documentation

Required implementation evidence:

- Write/edit hook module or equivalent gate: TBD path to module that registers the pre-execution write/edit decision point and fail-closed behavior.
- Path policy helper or fixture set: TBD path to helper and fixtures covering outside-root, instruction-root, symlink, malformed target, and allowed in-root cases.
- Instruction-root and working-root resolver integration: TBD path to resolver integration proving a single active containment root is used for this deliverable.
- Exact edit precondition validator: TBD path to validator plus selected stale-content behavior, matcher, and diff strategy.
- MCP write/gated surface coverage: TBD test evidence for `mcp__chirality__status_transition`, `mcp__chirality__deps_write`, gated `mcp__chirality__scaffold` classification, and any later write-capable MCP tools.
- Provenance/diff/summary recorder: TBD path to event or artifact writer that records allowed and denied write attempts.
- Write/edit negative and positive tests: TBD paths for denial and allowed-mutation fixtures.
- Source-state verifier and residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state or a governed hash-bypass record is accepted. (reconciled under D-APP-38).

<!-- sow-source-end -->

### CLM-013 — Traceability

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":99,"line_start":91,"source_sha256":"678ebd69cec8cf7bee7b162769ce0be9bcc2d463f473a136300e34d45699d9e2","target_id":"CLM-013"} -->
##### Traceability

| Source item | Covered by |
|---|---|
| SOW-027 Project-root containment and instruction-root protection | DEL-06-04-REQ-002, REQ-003, REQ-007, REQ-015 |
| SOW-057 Hooks and fail-closed behavior | DEL-06-04-REQ-001, REQ-006, REQ-012, REQ-013 |
| SOW-060 Safe write/edit behavior | DEL-06-04-REQ-004, REQ-005, REQ-011, REQ-014, REQ-015 |
| OBJ-005 Capability-forward policy with explicit hard-deny precedence permission policy, hooks, result budgets, and approvals | DEL-06-04-REQ-001, REQ-006 through REQ-013 |
| OBJ-006 Filesystem project truth through containment and change discipline | DEL-06-04-REQ-002 through REQ-005, REQ-011 through REQ-016 |
<!-- sow-source-end -->

- **AC-001** — The write/edit surface denies unauthorized or unsafe mutation before execution, preserves prior content on failed gates, and emits the required verification and provenance evidence.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-06-04 Write/Edit Surface and Path Hooks

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"ac85da4b46b2f71d90929834d4384fd5a24a36d89dc74cc0e679072732ce900e","target_id":"CLM-014"} -->
#### Procedure: DEL-06-04 Write/Edit Surface and Path Hooks

<!-- sow-source-end -->

### CLM-015 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"ac85da4b46b2f71d90929834d4384fd5a24a36d89dc74cc0e679072732ce900e","target_id":"CLM-015"} -->
##### Purpose

This procedure describes how to produce and verify the DEL-06-04 write/edit surface and path hook implementation evidence. It is written for the deliverable artifact, not as an end-user operation runbook.

<!-- sow-source-end -->

### CLM-016 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":19,"line_start":7,"source_sha256":"ac85da4b46b2f71d90929834d4384fd5a24a36d89dc74cc0e679072732ce900e","target_id":"CLM-016"} -->
##### Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted DEL-06-04 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
| Binding root, permission, hook, path, and MCP invariants | Available in `docs/CONTRACT.md` Sections 1.3 and 1.6 |
| Tool surface and hook specification | Available in `docs/SPEC.md` Sections 14 and 15 |
| Hook and tool vocabulary | Available in `docs/TYPES.md` Section 8 |
| Roadmap sequencing for controlled writes | Available in `docs/PLAN.md` R3; `docs/PRD.md` is warning-qualified due to HASH_MISMATCH |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` lists no accepted upstream edges yet |
| Exact implementation file paths | TBD |
| Exact test fixture paths | TBD |

<!-- sow-source-end -->

### CLM-017 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":73,"line_start":20,"source_sha256":"ac85da4b46b2f71d90929834d4384fd5a24a36d89dc74cc0e679072732ce900e","target_id":"CLM-017"} -->
##### Steps

1. Establish the mutation surfaces.
   - Identify SDK built-in `Write` and `Edit` surfaces, plus any Chirality MCP write tools currently exposed.
   - Treat `mcp__chirality__status_transition` and `mcp__chirality__deps_write` as current write/gated MCP surfaces from the SPEC inventory.
   - Classify gated `mcp__chirality__scaffold` before enabling any mutation behavior, and record whether it remains preview-only, scaffold-write capable, or out of this deliverable's active write surface.
   - Confirm write/edit surfaces are not exposed in `readOnly` and are only available in governed write modes.
   - Keep unknown or future write-capable tools out of scope until registered and governed.

2. Define or locate the active root resolver.
   - Resolve the active project or working root and the instruction root from product-owned runtime state.
   - Treat the decomposition phrase "project root" and the governance phrase "working root" as the same containment boundary until implementation chooses canonical naming.
   - Record any naming or resolver ambiguity as `TBD` or a review item.

3. Implement the pre-execution path gate.
   - Reject missing, malformed, or unresolvable target paths where the write/edit operation requires a target.
   - Deny targets outside the active project or working root.
   - Deny ordinary project writes under the instruction root.
   - Reject symlink targets and symlink path segments under the initial policy.
   - Fail closed if path classification cannot be completed.

4. Implement exact edit precondition checks.
   - Require edit-style operations to specify the exact content or equivalent exact precondition needed for safe replacement.
   - Deny or fail without mutation when the current file content does not match the precondition.
   - Select and document the exact matching algorithm, stale-content behavior, and diff strategy; keep them as `TBD` until implementation design selects them.
   - Record whether stale content is surfaced as permission denial, tool validation failure, or another terminal outcome so runtime event evidence can be tested.

5. Connect permission and hook decisions.
   - Feed DEL-06-01 permission overlay results into the write/edit gate.
   - Apply explicit hard-deny precedence when SDK options, mode, operator intent, or `allowedTools` conflict with Chirality policy or hook denial.
   - Do not rely on `allowedTools` alone as a restriction boundary.

6. Execute controlled mutation only after gates pass.
   - Perform the write/edit atomically where practical.
   - Preserve existing file content when any pre-execution gate fails.
   - Ensure Chirality MCP write tools and SDK built-ins follow equivalent policy.

7. Record provenance and runtime evidence.
   - Record permission/runtime evidence for allowed and denied attempts.
   - For successful writes/edits, capture safe provenance, diff or summary, and hook outcome metadata.
   - For failed or denied write/edit attempts, capture the deliverable-local evidence needed to prove no mutation occurred; leave lifecycle-wide hook failure mirroring to DEL-06-06.
   - Apply redaction and result-budget policy where outputs could be large or sensitive.

8. Add tests and fixtures.
   - Add fixtures for allowed in-root regular-file writes and edits.
   - Add denial fixtures for outside-root targets, instruction-root targets, symlink targets, hook failure, mode denial, and stale edit preconditions.
   - Add parity coverage for SDK built-ins and Chirality MCP write tools where both are in scope.
   - Record exact test paths as `TBD` until assigned.

9. Record residual gaps.
   - Track unresolved root naming, exact edit algorithm, implementation file paths, fixture paths, and PRD HASH_MISMATCH state.
   - Add or reference a source-state verifier that keeps PRD-derived behavior warning-qualified until REF-006 is reconciled or a governed bypass record is accepted.
   - Surface any remaining source conflicts in the deliverable review notes.

<!-- sow-source-end -->

### CLM-018 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":89,"line_start":74,"source_sha256":"ac85da4b46b2f71d90929834d4384fd5a24a36d89dc74cc0e679072732ce900e","target_id":"CLM-018"} -->
##### Verification

| Check | Expected result |
|---|---|
| Pre-execution hook | Write/edit mutation does not occur until the hook or equivalent gate passes. |
| Path containment | Outside-root targets are denied without mutation. |
| Instruction-root protection | Instruction-root targets are denied during ordinary project execution. |
| Symlink rejection | Symlink target or path-segment attempts are denied in the initial policy. |
| Exact edit precondition | Stale, missing, or ambiguous edit preconditions fail without mutation. |
| Deny precedence | Hook, path, policy, SDK deny, governance, or human-gate denial overrides any allow. |
| Mode behavior | `readOnly` cannot write; `workspaceWrite` writes only after permission and hooks pass. |
| MCP parity | Chirality MCP write tools pass through equivalent gates as SDK built-ins. |
| Provenance | Successful writes produce safe diff/summary/provenance evidence; denied attempts produce audit evidence. |
| PRD warning | PRD-derived controlled-write details remain traceable to `_REFERENCES.md` HASH_MISMATCH until reconciled. |
| Hook-lifecycle boundary | Write/edit denial or failure evidence is captured here, while broader hook lifecycle and compaction/terminal mirroring remain assigned to DEL-06-06. |

<!-- sow-source-end -->

### CLM-019 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":100,"line_start":90,"source_sha256":"ac85da4b46b2f71d90929834d4384fd5a24a36d89dc74cc0e679072732ce900e","target_id":"CLM-019"} -->
##### Records

- Write/edit hook implementation path: TBD.
- Root resolver and instruction-root resolver integration: TBD.
- Path policy fixtures: TBD.
- Exact edit validator and matcher tests: TBD.
- Stale-content terminal outcome classification: TBD.
- MCP write/gated surface inventory and parity tests: TBD.
- Provenance/diff/summary evidence format: TBD.
- Runtime event evidence for allowed and denied write attempts: TBD.
- Review note for PRD HASH_MISMATCH: required under the reconciled D-APP-38 source state.
<!-- sow-source-end -->

- **VER-001** — Validate path containment, instruction-root protection, symlink rejection, exact edit preconditions, deny precedence, mode behavior, MCP parity, and provenance using the source-defined checks and fixtures.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-06-04 Write/Edit Surface and Path Hooks

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-020"} -->
#### Guidance: DEL-06-04 Write/Edit Surface and Path Hooks

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-021 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":10,"line_start":5,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-021"} -->
##### Purpose

DEL-06-04 exists to make controlled workspace writes possible without weakening Chirality's filesystem, permission, and provenance boundaries. It is the write/edit security-control slice for PKG-06: permission overlay decisions, read tool exposure, MCP wrapper shape, bash governance, and hook lifecycle mirroring are adjacent deliverables, but this deliverable defines the path and mutation gates that must pass before files change.

Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/CONTRACT.md` Sections 1.3 and 1.6; `docs/SPEC.md` Section 15; `docs/PLAN.md` R3.

<!-- sow-source-end -->

### CLM-022 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":19,"line_start":11,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-022"} -->
##### Principles

1. Runtime code is the boundary. Prompt text, persona wording, or tool descriptions must not be relied on to protect filesystem writes. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-2.
2. Capability-forward policy with explicit hard-deny precedence remains controlling. A denial from policy, path containment, hook, governance, SDK deny rule, or human gate overrides any allow. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-1.
3. The active project or working root bounds ordinary writes. Target paths outside that root are denied before mutation. Source: `docs/CONTRACT.md` Section 1.6 K-PATH-2.
4. Instruction-root writes are release/change operations, not ordinary project execution. Ordinary project runs must not mutate the instruction root. Source: `docs/CONTRACT.md` Section 1.3 K-ROOT-2.
5. Symlink write rejection is the initial policy. Any relaxation would need a governed amendment and tests. Source: `docs/CONTRACT.md` Section 1.6 K-PATH-3.
6. Provenance is part of the write, not an afterthought. Allowed and denied attempts need enough event, diff, summary, and provenance evidence for audit. Sources: `docs/PLAN.md` R3; `docs/SPEC.md` Section 15.2.

<!-- sow-source-end -->

### CLM-023 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":21,"line_start":20,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-023"} -->
##### Considerations

<!-- sow-source-end -->

### CLM-024 — Root Terminology

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":25,"line_start":22,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-024"} -->
###### Root Terminology

The decomposition uses "project-root containment"; `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/PRD.md` primarily use "working root." Treat these as the active runtime containment root for this deliverable until implementation selects the exact public name. Do not create two independent roots without a source update.

<!-- sow-source-end -->

### CLM-025 — Hook Placement

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":29,"line_start":26,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-025"} -->
###### Hook Placement

`PreToolUse` should be the normal enforcement point for path containment, instruction-root protection, symlink rejection, exact edit preconditions, and mode/policy denial before mutation. `PostToolUse` should record successful write provenance, diff/summary, and safe metadata. This deliverable owns the evidence that a write/edit attempt was allowed, denied, or failed without mutation; DEL-06-06 owns broader hook lifecycle, compaction, stop/finalization, and terminal mirror semantics. Post-failure records should therefore capture the minimum write/edit denial or failure evidence here and hand lifecycle-wide failure mirroring to DEL-06-06. Sources: `docs/SPEC.md` Section 15.2; decomposition rows DEL-06-04 and DEL-06-06.

<!-- sow-source-end -->

### CLM-026 — Exact Edit Preconditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":33,"line_start":30,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-026"} -->
###### Exact Edit Preconditions

Exact edit preconditions should prevent stale or ambiguous edits from mutating files. The source corpus requires exact preconditions but does not specify the matching algorithm. Keep algorithmic details as `TBD` until implementation design chooses the file matcher, diff strategy, and stale-content behavior. The design record should state whether stale content is a denied permission decision, a tool validation failure, or another terminal outcome, because that choice determines the event evidence and user-facing feedback.

<!-- sow-source-end -->

### CLM-027 — MCP Write/Gated Surface

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":37,"line_start":34,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-027"} -->
###### MCP Write/Gated Surface

The current SPEC inventory names `mcp__chirality__status_transition` and `mcp__chirality__deps_write` as write/gated Chirality MCP tools, and `mcp__chirality__scaffold` as gated. Treat `scaffold` as requiring explicit mutation classification before exposure, and require any future write-capable MCP tool to opt into the same gate sequence as SDK `Write`/`Edit`. Source: `docs/SPEC.md` Section 14.2.

<!-- sow-source-end -->

### CLM-028 — PRD Hash Status

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":41,"line_start":38,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-028"} -->
###### PRD Hash Status

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-029 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":51,"line_start":42,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-029"} -->
##### Trade-offs

| Trade-off | Guidance |
|---|---|
| Omit write tools vs expose and deny | Prefer not exposing write/edit tools until mode and permission policy allow them, but still enforce hook denial because exposure control alone is not a safety boundary. Sources: `docs/SPEC.md` Section 14.3; `docs/CONTRACT.md` K-PERM-3. |
| SDK built-ins vs Chirality MCP write tools | Treat both as mutation surfaces requiring equivalent permission, hook, path, redaction, and event logging policy. Source: `docs/CONTRACT.md` K-MCP-1. |
| Atomic write/edit vs implementation simplicity | Perform atomic mutation where practical, but do not use atomicity as a substitute for pre-execution path and precondition checks. The implementation rationale should identify when atomic behavior is practical, when it is not, and what evidence proves failed gates preserved prior content. Source: `docs/PRD.md` Section 7.9, MATCH status. — reconciled under D-APP-38 |
| Symlink denial vs advanced workspace layouts | Reject symlink writes initially. If future workspace needs require symlink support, add a governed policy amendment and targeted tests first. Source: `docs/CONTRACT.md` K-PATH-3. |
| Provenance detail vs data exposure | Record enough diff/summary/provenance to audit the write while applying the same redaction and result-budget posture as other tools. Source: `docs/SPEC.md` Section 15.2. |

<!-- sow-source-end -->

### CLM-030 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":64,"line_start":52,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-030"} -->
##### Examples

| Scenario | Expected behavior |
|---|---|
| `readOnly` session attempts `Write` or `Edit` | Deny before mutation; record permission/runtime evidence where governed. |
| `workspaceWrite` session edits an in-root regular file with exact precondition match and passing hooks | Allow mutation, preferably atomic where practical; record diff/summary and provenance. |
| Write target resolves outside the active project or working root | Deny in `PreToolUse` or equivalent gate; no mutation occurs. |
| Write target is under the instruction root | Deny as ordinary project execution; instruction-root mutation requires governed release/change operation. |
| Write target or path segment is a symlink | Deny under initial policy; no mutation occurs. |
| Edit precondition does not match current file content | Deny or fail the edit without mutation; record failure evidence. |
| SDK `allowedTools` includes `Edit` but Chirality hook denies path containment | Final result is deny; `allowedTools` does not bypass hooks. |
| Chirality MCP dependency writer is used | It must pass through equivalent permission, hook, path, redaction, and event logging policy as SDK built-ins. |

<!-- sow-source-end -->

### CLM-031 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":70,"line_start":65,"source_sha256":"4db238d675f3f7c7b024132158ad034a3eb460cae999cdf18649ee88af3b932d","target_id":"CLM-031"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| DEL-06-04-CONFLICT-001 | Root terminology differs between "project root" in decomposition wording and "working root" in governance docs. | `_CONTEXT.md` and decomposition row DEL-06-04 | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` Section 7.9 | Datasheet Conditions; Specification Scope and REQ-002; Procedure Steps | Treat both as the active runtime containment root and settle canonical naming during implementation. | TBD |
| DEL-06-04-CONFLICT-002 | PRD is content-accessible but current and MATCH. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Sections 7.9 and R3 | PRD-cited requirements and guidance | Use PRD as warning-qualified source until reference hash state is reconciled. | TBD — reconciled under D-APP-38 |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-027 SOW-057 SOW-060 OBJ-005 OBJ-006 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
