---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-01
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-054, SOW-055, SOW-056, SOW-058]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-01` in service of project scope [SOW-054, SOW-055, SOW-056, SOW-058] and package objectives [OBJ-005].

- **OUT-001** — Permission overlay module; decision records; readOnly/dontAsk/ask tests; hard-deny precedence tests.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

> #### Datasheet: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-06-01 |
> | Deliverable name | ChiralityPermissionOverlay and Mode Mapping |
> | Package | PKG-06 Permissioned Tools, MCP, and Hooks |
> | Type | SECURITY_CONTROL |
> | Responsible party | TBD |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Context envelope | M |
> | Scope items | SOW-054, SOW-055, SOW-056, SOW-058 |
> | Objective context | OBJ-005 |
> | Anticipated artifacts | Permission overlay module; decision records; readOnly/dontAsk/ask tests |
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-054 through SOW-058.
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary control | `ChiralityPermissionOverlay` | `docs/PRD.md` Section 9.4, MATCH status; decomposition glossary — reconciled under D-APP-38 |
> | Decision record | `HarnessPermissionDecision` with `allow`, `deny`, or application-level `ask` | `docs/TYPES.md` Section 8.2 |
> | Decision sources | `sdk-option`, `sdk-callback`, `chirality-policy`, `hook`, `human`, `prompt-support` | `docs/TYPES.md` Section 8.2 |
> | Permission modes in scope | `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, `bypass` | `docs/TYPES.md` Section 8.1; `docs/SPEC.md` Section 15.1 |
> | Core precedence rule | Deny overrides allow | `docs/CONTRACT.md` Section 1.6 K-PERM-1; `docs/PRD.md` NFR-007, MATCH status — reconciled under D-APP-38 |
> | Restriction boundary | `allowedTools` alone is not a restriction boundary | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3; `docs/PRD.md` KG-023, MATCH status — reconciled under D-APP-38 |
> | Interactive approval path | `canUseTool` mediates application approval; decision must be persisted before returning SDK allow/deny | `docs/SPEC.md` Section 15.1; decomposition row SOW-058 |
> | Event obligation | Persist `tool.permission` events for governed tool attempts | `docs/PRD.md` R2 acceptance, MATCH status; decomposition row SOW-056 — reconciled under D-APP-38 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Constraint | Source |
> |---|---|---|
> | PRD source state | `docs/PRD.md` is accessible but has MATCH in `_REFERENCES.md`; PRD-derived details are treated as source-state evidence, not as unqualified accepted truth. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
> | Read-only mode | Must not expose or allow write/edit/bash/network-capable actions. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/TYPES.md` Section 8.1 |
> | `dontAsk` mode | Denies unapproved actions without prompting; unapproved writes, shell, network, and unknown tools deny. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/TYPES.md` Section 8.1 |
> | `ask` mode | Application may request interactive approval for governed actions; SDK callback ultimately returns allow or deny. | `docs/TYPES.md` Sections 8.1 and 8.2 |
> | `bypass` mode | Developer-local only, never shipped ordinary mode, and still subject to Chirality denies. | `docs/TYPES.md` Section 8.1; `docs/SPEC.md` Section 15.1 |
> | Hook separation | DEL-06-01 covers permission policy and approval mediation; detailed hook implementation is assigned to DEL-06-04 and DEL-06-06. | `_CONTEXT.md`; decomposition PKG-06 rows |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Construction note | Source |
> |---|---|---|
> | Overlay input | Session, optional turn, selected Chirality mode, requested tool name, resolved tool-surface posture, and explicit policy/hook/human-gate signals needed to decide tool permission. Exact TypeScript interface shape remains TBD until implementation ownership is assigned. | `docs/TYPES.md` Section 8.2; `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
> | Mode mapper | Maps Chirality modes to SDK posture plus overlay behavior. | `docs/SPEC.md` Section 15.1 |
> | Deny evaluation | Any explicit deny from policy, path containment, hook, governance, SDK deny rule, or human gate blocks execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
> | Decision persistence | A structured permission decision is recorded before downstream execution or before returning an SDK approval result. | `docs/TYPES.md` Section 8.2; decomposition rows SOW-054 and SOW-058 |
> | Event integration | Tool attempts emit permission/start/completion/failure events in the R2 scope. | `docs/PRD.md` R2 implementation targets, MATCH status; `docs/TYPES.md` Section 7.3 later event categories — reconciled under D-APP-38 |
> | Tests | Include readOnly, dontAsk, and ask behavior tests. Exact test paths and fixtures: TBD. | `_CONTEXT.md`; decomposition DEL-06-01 anticipated artifacts |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-002 | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool, MCP, hook, path, and bash invariants | MATCH |
> | REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool names, MCP tools, tool surface rules, mode mapping, hook requirements | MATCH |
> | REF-004 | `docs/TYPES.md` Section 8 | Permission modes, decision record, tool-surface terms | MATCH |
> | REF-005 | `docs/PLAN.md` R2 and R3 | Sequencing and acceptance context | MATCH |
> | REF-006 | `docs/PRD.md` Sections 9.4, R2, R3, NFR-007, KG-023 | Product requirements and implementation direction | MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

> #### Specification: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-008 — Scope

> ##### Scope
>
> DEL-06-01 specifies the Chirality permission overlay and mode mapping needed to mediate governed tool use in PKG-06. It covers structured permission decisions, explicit hard-deny precedence, Chirality-to-SDK mode posture, `canUseTool` approval mediation, and permission-event persistence for governed tool attempts.
>
> In scope:
>
> - Produce a permission overlay module that can return structured allow, deny, or application-level ask decisions.
> - Map `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and developer-local `bypass` to SDK posture plus Chirality overlay behavior.
> - Ensure explicit denies override SDK or policy allows.
> - Persist permission decisions and `tool.permission` event evidence before execution continues.
> - Provide tests for `readOnly`, `dontAsk`, and `ask` behavior.
>
> Out of scope:
>
> - Detailed path containment, instruction-root protection, symlink rejection, write provenance, and hook lifecycle implementation, which belong to DEL-06-04 and DEL-06-06.
> - Tool resolver, deterministic tool ordering, read MCP implementations, and unknown-tool validation, except where their outputs feed this overlay. Those belong primarily to DEL-06-02 and DEL-06-03.
> - Remote MCP, plugin marketplace, and broad tool search, which are out of current scope without governed amendment.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/SPEC.md` Sections 14 and 15; `docs/PRD.md` R2/R3 with MATCH status. (reconciled under D-APP-38).
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-06-01-REQ-001 | The permission overlay MUST produce or persist a structured `HarnessPermissionDecision` with `decisionId`, `sessionId`, `toolName`, `decision`, `reason`, `source`, `decidedAt`, and optional safe metadata. | `docs/TYPES.md` Section 8.2; decomposition SOW-054 |
> | DEL-06-01-REQ-002 | The decision value MUST be one of `allow`, `deny`, or application-level `ask`; `ask` MUST resolve to an SDK allow or deny before SDK callback return. | `docs/TYPES.md` Section 8.2; decomposition SOW-058 |
> | DEL-06-01-REQ-003 | Deny MUST override allow when any explicit deny is produced by policy, path containment, hook, governance, SDK deny rule, or human gate. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
> | DEL-06-01-REQ-004 | The overlay MUST NOT treat `allowedTools` alone as a restriction boundary. Restriction MUST use disallowed tools, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
> | DEL-06-01-REQ-005 | In `readOnly`, write/edit/bash/network-capable tools and unexpected tools MUST be denied or not exposed. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/SPEC.md` Section 15.1 |
> | DEL-06-01-REQ-006 | In `dontAsk`, exact safe tools may be pre-approved, and everything else MUST deny without prompting. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/SPEC.md` Section 15.1 |
> | DEL-06-01-REQ-007 | In `ask`, governed writes or shell requests MUST be mediated through `canUseTool` and UI approval, and the decision MUST be persisted before returning allow or deny. | `docs/SPEC.md` Section 15.1; decomposition SOW-058 |
> | DEL-06-01-REQ-008 | In `workspaceWrite`, SDK edit acceptance MUST be allowed only after write hooks pass; otherwise explicit approval posture is required. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` R3, MATCH status — reconciled under D-APP-38 |
> | DEL-06-01-REQ-009 | `bypass` MUST be developer-local only, never shipped as ordinary operator behavior, and still subject to Chirality denies. | `docs/CONTRACT.md` Section 1.6 K-PERM-6; `docs/SPEC.md` Section 15.1 |
> | DEL-06-01-REQ-010 | Governed tool attempts MUST produce `tool.permission` evidence including source, reason, and safe SDK metadata when available. | decomposition SOW-056; `docs/PRD.md` R2 implementation targets, MATCH status — reconciled under D-APP-38 |
> | DEL-06-01-REQ-011 | Prompt text MUST NOT be treated as a safety boundary for filesystem writes, tool exposure, bash, subagents, or domain operations. | `docs/CONTRACT.md` Section 1.6 K-PERM-2 |
> | DEL-06-01-REQ-012 | In-process Chirality MCP tools MUST pass through the same permission policy as SDK built-ins when the overlay evaluates them. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2 |
> | DEL-06-01-REQ-013 | The permission overlay MUST keep public Chirality contracts product-owned rather than SDK-shaped, with SDK-specific values translated as adapter metadata where needed. | `docs/CONTRACT.md` Section 1.5 K-ENGINE-4; `docs/PRD.md` Section 9.4, MATCH status — reconciled under D-APP-38 |
> | DEL-06-01-REQ-014 | Tests MUST cover `readOnly`, `dontAsk`, and `ask` mode behavior, including denied tool non-execution and permission-event persistence. | `_CONTEXT.md`; `docs/PRD.md` R2 acceptance, MATCH status — reconciled under D-APP-38 |
> | DEL-06-01-REQ-015 | The overlay input contract MUST include enough product-owned context to evaluate session identity, optional turn identity, requested tool name, Chirality mode, resolved tool-surface posture, and explicit deny/approval signals without making SDK request objects the public contract. | `docs/TYPES.md` Section 8.2; `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` Section 1.5 K-ENGINE-4 |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard or governing source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` Section 1.6 | Binding invariants for permission, tool exposure, hooks, MCP, path, and bash behavior. |
> | `docs/TYPES.md` Section 8 | Vocabulary and target shape for permission modes, permission decisions, tool terms, and `canUseTool`. |
> | `docs/SPEC.md` Sections 14 and 15 | Runtime tool surface, MCP tool names, tool surface rules, and Chirality-to-SDK mode mapping. |
> | `docs/PLAN.md` R2/R3 | Roadmap sequencing: permission-gated read surface before controlled writes and hooks. |
> | `docs/PRD.md` R2/R3 | Product implementation direction; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |
>

### CLM-011 — Verification

> ##### Verification
>
> | Requirement | Verification approach |
> |---|---|
> | DEL-06-01-REQ-001, REQ-002 | Unit tests assert decision record shape, allowed enum values, `ask` resolution, and safe metadata handling. |
> | DEL-06-01-REQ-003 | Precedence tests inject simultaneous allow and deny sources and assert final deny. |
> | DEL-06-01-REQ-004 | Tests prove `allowedTools` does not restrict by itself and that `disallowedTools`, mode policy, hooks, `canUseTool`, or `dontAsk` enforce restriction. |
> | DEL-06-01-REQ-005 | `readOnly` tests assert write/edit/bash/network-capable and unexpected tools deny or remain unexposed. |
> | DEL-06-01-REQ-006 | `dontAsk` tests assert only exact safe tools are allowed and unknown/unapproved actions deny without UI approval. |
> | DEL-06-01-REQ-007 | `ask` tests assert UI-mediated approval path persists the decision before SDK callback return. |
> | DEL-06-01-REQ-008 | Integration or contract tests assert `workspaceWrite` cannot allow edits unless hooks report pass. Hook internals remain owned by DEL-06-04. |
> | DEL-06-01-REQ-009 | Release/configuration tests assert ordinary shipped modes cannot select SDK `bypassPermissions`; developer-local use still applies Chirality denies. |
> | DEL-06-01-REQ-010 | Runtime event tests assert `tool.permission` records source, reason, and safe SDK metadata for governed attempts. |
> | DEL-06-01-REQ-011 | Negative tests assert prompt-only permission claims cannot authorize tool exposure or execution. |
> | DEL-06-01-REQ-012 | MCP wrapper tests assert Chirality MCP tool attempts pass through overlay evaluation. |
> | DEL-06-01-REQ-013 | Type or conformance tests assert public `HarnessEvent`, permission decision, and API contracts do not leak SDK-shaped names except adapter metadata. |
> | DEL-06-01-REQ-014 | Test suite includes readOnly/dontAsk/ask fixtures named or tagged for DEL-06-01 traceability. Exact paths: TBD. |
> | DEL-06-01-REQ-015 | Type or unit tests assert the overlay accepts a product-owned input shape and translates SDK-specific values only at the adapter boundary. Exact implementation path remains TBD. |
>
> REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required implementation evidence:
>
> - Permission overlay module or equivalent product-owned runtime component.
> - Mode mapping table or tested mapping fixture for `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and developer-local `bypass`.
> - Permission decision record type or schema.
> - `tool.permission` event schema/mapping evidence.
> - `canUseTool` approval mediation tests.
> - ReadOnly/dontAsk/ask behavioral tests.
> - Residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state. (reconciled under D-APP-38).
>

### CLM-013 — Pass 3 Semantic Lensing Disposition

> ##### Pass 3 Semantic Lensing Disposition
>
> | ItemID | Disposition | Evidence and source reread |
> |---|---|---|
> | C-001 | Incorporated as bounded interface requirements while preserving exact implementation shape as TBD. | Datasheet Construction and DEL-06-01-REQ-015 now identify the minimum product-owned context. Reread: `docs/TYPES.md` Section 8.2; `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` Section 1.5. |
> | F-001 | Incorporated as verification evidence for workspaceWrite hook-pass gating, with hook internals deferred to DEL-06-04. | Verification keeps hook implementation out of this deliverable but requires contract/integration proof before edits can allow. Reread: `docs/SPEC.md` Section 15.1; decomposition PKG-06 rows for DEL-06-04. |
> | X-002 | Converted to explicit path-TBD verification evidence requirements rather than invented test names. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | E-002 | Incorporated as MCP parity verification with concrete source obligation and adjacent wrapper ownership. | DEL-06-01-REQ-012 and verification require parity; wrapper detail remains with DEL-06-03. Reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2; decomposition PKG-06 rows for DEL-06-03. |
>

### CLM-014 — Traceability

> ##### Traceability
>
> | Source item | Covered by |
> |---|---|
> | SOW-054 Structured permission decisions | DEL-06-01-REQ-001, REQ-002, REQ-013, REQ-015 |
> | SOW-055 Permission modes and capability policy with explicit hard-deny precedence | DEL-06-01-REQ-003 through REQ-009, REQ-011, REQ-015 |
> | SOW-056 Tool permission events | DEL-06-01-REQ-010 |
> | SOW-058 Interactive approval through `canUseTool` | DEL-06-01-REQ-002, REQ-007 |
>

### CLM-015 — D-APP-56 permission-class amendment (2026-07-12)

> ##### D-APP-56 permission-class amendment (2026-07-12)
>
> R4-P33 adds the D-APP-10-governed subagent/Agent class to REQ-005: delegated children are allowed only under `workspaceWrite`; other modes hard-deny through `evaluateSubagentPreflight`. DEL-06-01 owns the declaration and DEL-08-04 consumes it.

- **AC-001** — Verification evidence demonstrates structured permission decisions, explicit deny precedence, capability-policy mode mapping, canUseTool approval mediation, and the prescribed readOnly/dontAsk/ask behavior.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

> #### Procedure: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-017 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-01 permission overlay implementation and mode mapping evidence. It is written for the deliverable artifact, not as an end-user operation runbook.
>

### CLM-018 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Accepted DEL-06-01 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
> | Authoritative permission vocabulary | Available in `docs/TYPES.md` Section 8 |
> | Binding permission invariants | Available in `docs/CONTRACT.md` Section 1.6 |
> | Tool surface and mode mapping specification | Available in `docs/SPEC.md` Sections 14 and 15 |
> | Roadmap sequencing for R2/R3 | Available in `docs/PLAN.md`; `docs/PRD.md` is current and MATCH — reconciled under D-APP-38 |
> | Declared upstream dependencies | Available as extracted dependency records in `_DEPENDENCIES.md` and `Dependencies.csv`; human-declared upstream lists remain TBD pending closure ruling |
> | Exact implementation file paths | TBD |
> | Exact test fixture paths | TBD |
>

### CLM-019 — Steps

> ##### Steps
>
> 1. Establish the source-controlled mode vocabulary.
>    - Use `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and developer-local `bypass` from `docs/TYPES.md` Section 8.1.
>    - Do not introduce new modes without a governed source update.
>
> 2. Define or locate the structured permission decision record.
>    - Align with `HarnessPermissionDecision` from `docs/TYPES.md` Section 8.2.
>    - Include safe SDK metadata only when it does not leak secrets or SDK-shaped public contract fields.
>
> 3. Implement the capability policy with explicit hard-deny precedence.
>    - Evaluate explicit denies from Chirality policy, path containment, hooks, governance, SDK deny rules, and human gates.
>    - If any explicit deny is present, return or persist `deny` even when an SDK or tool option would otherwise allow.
>
> 4. Implement the mode mapping.
>    - Map `readOnly` to read-tool posture with write/edit/bash/network-capable and unexpected tools denied.
>    - Map `dontAsk` to exact safe-tool pre-approval with all other actions denied without prompting.
>    - Map `ask` to `canUseTool` or equivalent application mediation, with decision persistence before SDK callback return.
>    - Map `workspaceWrite` only after write hooks can prove project-root containment, instruction-root protection, symlink policy, and provenance behavior.
>    - Keep `bypass` developer-local and still subject to Chirality deny rules.
>
> 5. Integrate permission-event persistence.
>    - Persist `tool.permission` evidence for governed attempts with source, reason, and safe SDK metadata when available.
>    - Use the product-owned `HarnessEvent` JSONL surface for persisted permission evidence when the owning PKG-05/PKG-03 writer contract is available; exact call path remains TBD and is a tracked blocker rather than an accepted implementation fact.
>
> 6. Integrate MCP and SDK tool evaluation points.
>    - Ensure SDK built-ins and in-process `mcp__chirality__*` tools are evaluated by equivalent overlay policy.
>    - Keep detailed MCP wrapper implementation in DEL-06-03 unless this deliverable owns a shared permission hook point.
>
> 7. Add tests.
>    - Verify `readOnly` denies write/edit/bash/network-capable and unexpected tools.
>    - Verify `dontAsk` denies unknown or unapproved tools without prompting.
>    - Verify `ask` persists the UI/human decision before returning SDK allow or deny.
>    - Verify explicit hard-deny precedence when `allowedTools` or SDK posture conflicts with Chirality deny policy.
>    - Verify `tool.permission` event records include decision source and reason.
>    - Verify in-process Chirality MCP tool attempts pass through the same overlay decision path as SDK built-ins, with detailed wrapper fixtures owned by DEL-06-03 unless this deliverable defines a shared hook point.
>
> 8. Record residual gaps.
>    - Keep exact file paths, fixture names, and implementation ownership as `TBD` until assigned.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-020 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Decision schema | Permission decisions conform to `docs/TYPES.md` Section 8.2. |
> | Deny precedence | Any explicit deny produces final `deny`. |
> | `allowedTools` misconception | Tests show `allowedTools` does not restrict by itself and cannot bypass deny policy. |
> | `readOnly` behavior | Write/edit/bash/network-capable and unexpected tools do not execute. |
> | `dontAsk` behavior | Unapproved and unknown tools deny without prompting. |
> | `ask` behavior | Approval mediation persists the decision before SDK callback return. |
> | Event persistence | Governed attempts produce `tool.permission` evidence. |
> | MCP parity | Chirality MCP tool attempts pass through the same permission overlay as SDK built-ins. |
> | PRD warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
>

### CLM-021 — Records

> ##### Records
>
> - Permission overlay module or equivalent implementation path: TBD.
> - Mode mapping fixture or table: TBD.
> - `HarnessPermissionDecision` schema/type evidence: TBD.
> - Permission event tests: TBD.
> - readOnly/dontAsk/ask behavior tests: TBD.
> - WorkspaceWrite hook-pass gating evidence: TBD, dependent on DEL-06-04 hook result interface.
> - MCP parity evidence: TBD, dependent on DEL-06-03 wrapper points or a shared overlay hook point.
> - Dependency closure ruling: TBD for human-declared upstream status; extracted rows are present in `_DEPENDENCIES.md` and `Dependencies.csv`.
> - Review note for PRD MATCH: required under the reconciled D-APP-38 source state. (reconciled under D-APP-38).
>

### CLM-022 — Pass 3 Semantic Lensing Disposition

> ##### Pass 3 Semantic Lensing Disposition
>
> | ItemID | Disposition | Evidence and source reread |
> |---|---|---|
> | D-001 | Converted to explicit Records blockers rather than invented paths. | Records now name required implementation, fixture, hook-gating, MCP parity, and decision-schema evidence as TBD. Reread: `_CONTEXT.md` anticipated artifacts; `docs/SPEC.md` Sections 14 and 15; decomposition PKG-06 rows. |
> | D-002 | Incorporated as a dependency closure distinction. | Prerequisites now distinguish extracted dependency records from still-TBD human-declared upstream closure. Reread: `_DEPENDENCIES.md` Dependency Tracking and Extracted Dependency Register; `Dependencies.csv` v3.1. |
> | E-001 | Converted from ASSUMPTION to tracked blocker. | Step 5 no longer states the event writer/session JSONL API as accepted fact; it depends on the owning writer contract and keeps exact call path TBD. Reread: `docs/SPEC.md` Section 9.2 and Section 9.4; `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `_DEPENDENCIES.md` DEP-06-01-014 warning. |
> | E-002 | Incorporated as explicit MCP parity procedure and record evidence. | Step 7 and Records require MCP parity evidence while leaving wrapper points to DEL-06-03 or a shared overlay hook point. Reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2; decomposition PKG-06 rows for DEL-06-03. |

- **VER-001** — Inspect the permission overlay module and decision records, then run readOnly/dontAsk/ask and hard-deny precedence tests.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

> #### Guidance: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-024 — Purpose

> ##### Purpose
>
> DEL-06-01 exists to make runtime tool permission decisions explicit, persisted, and governed by Chirality-owned policy rather than SDK defaults or prompt text. It is the permission-policy slice of PKG-06: hooks, write path policy, bash governance, and MCP implementation details are adjacent deliverables, but this deliverable defines the overlay semantics they must feed.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14 and 15.
>

### CLM-025 — Principles

> ##### Principles
>
> 1. Capability-forward policy with explicit hard-deny precedence is the controlling rule. If any authoritative policy, hook, governance, SDK deny rule, path boundary, or human gate says deny, the final decision is deny. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-1.
> 2. Prompt text is never enough. Permission-sensitive behavior must be enforced by runtime code, policy, hooks, callback mediation, or human gates. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-2.
> 3. `allowedTools` is convenience, not containment. Treat it as possible auto-approval only; use disallowed tools, mode posture, hooks, `canUseTool`, and `dontAsk` to restrict execution. Sources: `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3.
> 4. Product-owned records are the durable truth. `HarnessPermissionDecision` and `tool.permission` events should remain Chirality-shaped even when SDK metadata is attached. Sources: `docs/TYPES.md` Section 8.2; `docs/PRD.md` Section 9.4, MATCH status. (reconciled under D-APP-38).
> 5. MCP is not a bypass. Chirality MCP tools and SDK built-ins must pass through equivalent permission and hook policy. Source: `docs/CONTRACT.md` Section 1.6 K-MCP-1.
>

### CLM-026 — Considerations

> ##### Considerations
>

### CLM-027 — Mode Mapping

> ###### Mode Mapping
>
> | Mode | Practical guidance | Source |
> |---|---|---|
> | `readOnly` | Prefer pre-approved read tools only; deny write/edit/bash/network-capable and unexpected tools. | `docs/SPEC.md` Section 15.1; `docs/TYPES.md` Section 8.1 |
> | `workspaceWrite` | Allow governed writes only after write hooks pass and project-root/instruction-root/symlink policy is satisfied. Hook internals are not owned by this deliverable. | `docs/SPEC.md` Section 15.1 |
> | `dontAsk` | Use for non-interactive denial posture. Unknown and unapproved actions should deny without prompting. | `docs/CONTRACT.md` Section 1.6 K-PERM-5 |
> | `ask` | Use when the application can present an approval request and persist the answer before the SDK callback returns allow or deny. | `docs/SPEC.md` Section 15.1 |
> | `bypass` | Keep developer-local only; never treat it as shipped operator behavior; Chirality denies still apply. | `docs/CONTRACT.md` Section 1.6 K-PERM-6 |
>

### CLM-028 — Decision Provenance

> ###### Decision Provenance
>
> Use the `source` field deliberately. A decision from `chirality-policy` should not be mislabeled as `human`, and SDK callback mediation should be captured distinctly from hook denials. Human approvals remain non-delegable in the broader governance model; automated permission decisions should not be described as approvals for reliance.
>

### CLM-029 — PRD Hash Status

> ###### PRD Hash Status
>
> REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>
> Current disposition: keep PRD-derived implementation direction warning-qualified and require review evidence before using PRD-only details as closure proof. CONTRACT, TYPES, SPEC, PLAN, and the accepted decomposition remain the unqualified sources for binding permission vocabulary, invariants, mode mapping, sequencing, and deliverable scope.
>

### CLM-030 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Omit denied tools vs expose and deny at call time | Prefer omission where possible to reduce model context and accidental attempts, but still enforce denial at runtime because exposure control alone is not a safety boundary. Source: `docs/SPEC.md` Section 14.3. |
> | SDK mode vs Chirality overlay | Use SDK posture where it helps, but preserve Chirality-owned capability policy with explicit hard-deny precedence, decision records, event logs, path containment, and human-gate semantics. Sources: `docs/PLAN.md` risk table; `docs/PRD.md` KG-026, MATCH status. — reconciled under D-APP-38 |
> | `ask` UX vs deterministic execution | Interactive approval can be appropriate for governed actions, but only if the persisted decision precedes SDK allow/deny return. Non-interactive contexts should use `dontAsk` denial rather than inventing approval. |
> | Mode mapping now vs future SDK drift | Keep mapping centralized and tested because SDK permission behavior may change. Source: `docs/PRD.md` KG-021, MATCH status. — reconciled under D-APP-38 |
>

### CLM-031 — Examples

> ##### Examples
>
> | Scenario | Expected overlay result |
> |---|---|
> | `readOnly` session attempts `Read` on an allowed project file | `allow` if the tool surface and path policy permit it; persist permission evidence if governed. Exact path-policy integration: TBD. |
> | `readOnly` session attempts `Write`, `Edit`, `Bash`, or a network-capable tool | `deny`; do not execute. |
> | `dontAsk` session attempts an unknown tool | `deny` without prompting; unknown-tool structured validation may be owned by DEL-06-02. |
> | `ask` session attempts a governed write | `ask` at application level, persist the human/UI decision, then return SDK allow or deny. |
> | SDK `allowedTools` includes a tool that Chirality policy denies | Final decision is `deny`; `allowedTools` does not bypass deny policy. |
> | Developer-local `bypass` is enabled | SDK bypass may be used only in developer-local mode; Chirality deny hooks and disallowed tools still apply. |
>

### CLM-032 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | TBD | No direct source conflict identified during P1/P2. PRD has a MATCH source state. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections used above | All PRD-cited requirements and guidance | Treat PRD as a current MATCH source under the reconciled D-APP-38 source state. | TBD — reconciled under D-APP-38 |
>

### CLM-033 — Pass 3 Semantic Lensing Disposition

> ##### Pass 3 Semantic Lensing Disposition
>
> | ItemID | Disposition | Evidence and source reread |
> |---|---|---|
> | X-001 | Incorporated as an explicit PRD MATCH disposition. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |

### CLM-034 — D-APP-68 Managed-Orchestration Ownership Mapping (2026-07-19)

> ##### D-APP-68 Managed-Orchestration Ownership Mapping (2026-07-19)
>
> DEL-06-01 owns the `coordination` descriptor permission class and the
> `harness-permission.v7.coordination-mode` mode-policy behavior. Coordination
> tools mutate the orchestration control plane and therefore hard-deny in every
> mode except `workspaceWrite`; in `workspaceWrite` they are admitted only to
> their handler-level hierarchy, seal, parentage, capability, and project-path
> validation. This permission-class mapping does not transfer descriptor,
> in-process MCP composition, child path-policy, Bash-policy, or child-record
> ownership from DEL-06-02, DEL-06-03, DEL-06-04, DEL-06-05, or DEL-08-05.
>
> Evidence: D-APP-68 chronology item 3;
> `frontend/src/lib/harness/permission-overlay.ts`;
> `frontend/packages/harness-contract/src/tool-descriptor.ts`.

- **AC-002** — Documentary and runtime evidence agree that the coordination
  class is hard-denied outside `workspaceWrite` and remains subject to
  handler-level managed-delegation validation when admitted.
- **VER-002** — Inspect the permission overlay's v7 policy constant and
  coordination branch, then verify the ownership boundary against D-APP-68.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-054 SOW-055 SOW-056 SOW-058 OBJ-005 | CLM-007 CLM-034 | AC-001 AC-002 | VER-001 VER-002 | Claim map, parity report, and applicable verification evidence |
