---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-05
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-062]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-05

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-05` in service of project scope [SOW-062] and package objectives [OBJ-005].

- **OUT-001** — Bash governance policy evidence covering default denial, governed enablement, timeout and capture policy, output metadata tests, interruption behavior, and audit behavior.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-05 Bash Governance and Timeout Policy

> #### Datasheet: DEL-06-05 Bash Governance and Timeout Policy
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-06-05 |
> | Deliverable name | Bash Governance and Timeout Policy |
> | Package | PKG-06 Permissioned Tools, MCP, and Hooks |
> | Type | SECURITY_CONTROL |
> | Responsible party | TBD |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Context envelope | M |
> | Scope items | SOW-062 |
> | Objective context | OBJ-005 |
> | Anticipated artifacts | Bash deny/default tests; timeout/capture policy; output metadata tests |
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger row SOW-062.
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Governed tool | SDK built-in `Bash` where available | `docs/SPEC.md` Section 14.1 |
> | Default posture | Bash denied by default even though the SDK ships the tool | `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
> | Enablement prerequisites | Timeout, output capture, result storage, interrupt behavior, and audit events | `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4 |
> | Denied modes | `readOnly` and `dontAsk` deny Bash/shell unless a future governed rule says otherwise | `docs/CONTRACT.md` Section 1.6 K-PERM-4 and K-PERM-5; `docs/PLAN.md` R4 acceptance |
> | Restriction mechanism | `allowedTools` is not sufficient; restriction requires disallowed tools, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
> | Permission decision record | `HarnessPermissionDecision` with decision, reason, source, timestamp, and optional safe metadata | `docs/TYPES.md` Section 8.2 |
> | Tool result policy | Small outputs inline; medium/large outputs previewed or stored as session artifacts with metadata | `docs/PRD.md` FR-096, MATCH status; `docs/PLAN.md` R4 — reconciled under D-APP-38 |
> | Audit mirror | `.chirality/sessions/<sessionId>/events.jsonl` remains the product-owned audit record | `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/PRD.md` FR-121, MATCH status — reconciled under D-APP-38 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Constraint | Source |
> |---|---|---|
> | PRD source state | `docs/PRD.md` is accessible but has MATCH in `_REFERENCES.md`; PRD-derived details are treated as source-state evidence, not as unqualified accepted truth. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
> | Bash before R4 readiness | Bash must not be exposed before governance, hooks, event logging, result storage, timeout, audit logging, and packaging checks are reliable. | `docs/DIRECTIVE.md` Section 4.2; `docs/PLAN.md` R4 |
> | Denied execution | Denied Bash must not spawn. | `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
> | Timeout value | Exact default timeout and override semantics are TBD; source material requires a timeout but does not provide a Bash-specific value. | `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4 |
> | Output channels | Allowed Bash captures stdout and stderr separately. | `docs/PLAN.md` R4 implementation targets; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
> | Interrupt behavior | Allowed Bash can be interrupted when possible; exact SDK/process mechanics are TBD. | `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Construction note | Source |
> |---|---|---|
> | Tool-surface resolver | Expose `Bash` only when session/persona/mode/options/policy permit it; otherwise omit or hard-deny. | `docs/SPEC.md` Sections 13.2, 14.3, and 15.1 |
> | Deny policy | Explicit denies from policy, path containment, hooks, governance, SDK deny rules, or human gates block Bash execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
> | Bash preflight | Enforce mode, command name/length, timeout, redirection/path-token counts, output capture, network-command and URL-scheme posture, and audit metadata before spawning. | `frontend/src/lib/harness/tool-shell-policy.ts`; `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
> | Execution capture | Capture stdout and stderr separately and classify terminal outcome as success, failure, timeout, interruption, or cancellation where available. | `docs/PLAN.md` R4; `docs/SPEC.md` Section 10.1 |
> | Result storage | Apply `ToolResultStore` policy so large output is stored under session artifacts and represented by preview plus schema-versioned metadata: tool/use/turn IDs, byte lengths, truncation, SHA-256, relative path, and stdout/stderr stream labels. | D-APP-42; `frontend/src/lib/harness/tool-result-artifacts.ts`; `frontend/src/lib/harness/tool-evidence.ts` |
> | Audit events | Persist permission, started, completed/failed, interruption/timeout, and artifact metadata in Chirality-owned events; an SDK Bash result with `interrupted: true` maps to `tool.failed` with safe stream/artifact evidence. | ADQ-11; D-APP-43; `frontend/src/lib/harness/sdk-message-mapper.ts` |
> | Tests | Include deny/default tests, timeout/capture tests, output metadata tests, and denied-never-spawns tests. Exact test paths: TBD. | `_CONTEXT.md`; `docs/PLAN.md` R4 acceptance |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` Sections 2.8, 2.9, 4.1, 4.2, and 5 | Product-owned runtime governance, reliance boundaries, bash exposure sequencing | MATCH |
> | REF-002 | `docs/CONTRACT.md` Sections 1.5 and 1.6 | Binding event, permission, hook, path, and Bash invariants | MATCH |
> | REF-003 | `docs/SPEC.md` Sections 10, 13, 14, and 15 | Engine responsibilities, option/tool resolution, tool names, mode mapping, hooks | MATCH |
> | REF-004 | `docs/TYPES.md` Sections 7 and 8 | Event vocabulary, permission modes, decision records, tool terms, artifact path fields | MATCH |
> | REF-005 | `docs/PLAN.md` R4 | Sequencing, implementation targets, and Bash acceptance criteria | MATCH |
> | REF-006 | `docs/PRD.md` Sections 8.15 and R4 | Product requirements for Bash, result storage, context mirror, and audit behavior | MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-06-05 Bash Governance and Timeout Policy

> #### Specification: DEL-06-05 Bash Governance and Timeout Policy
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-008 — Scope

> ##### Scope
>
> DEL-06-05 specifies the security-control policy for enabling SDK `Bash` in Chirality. It covers default denial, mode-based exposure, pre-execution governance, timeout requirement, stdout/stderr capture, output storage, interruption behavior, terminal outcome persistence, and audit evidence.
>
> In scope:
>
> - Keep Bash denied by default and denied in `readOnly` / `dontAsk`.
> - Permit Bash only in explicitly governed modes after permission, hook, timeout, result-storage, interrupt, and audit checks pass.
> - Ensure denied Bash never spawns.
> - Define timeout/capture/output metadata expectations for allowed Bash.
> - Provide tests for default denial, timeout/capture behavior, result artifact metadata, and denied non-execution.
>
> Out of scope:
>
> - General permission overlay semantics and mode mapping owned by DEL-06-01, except where they are applied to Bash.
> - Read tool resolver and MCP read tools owned by DEL-06-02 and DEL-06-03.
> - Write/edit path policy owned by DEL-06-04, except Bash must still obey path/hook denies when command execution could mutate the filesystem.
> - Hook lifecycle and compaction mirror implementation owned by DEL-06-06, except this deliverable must emit or require Bash-relevant events.
> - Remote MCP, plugin marketplace, and broad remote execution, which remain out of current scope without governed amendment.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06 row DEL-06-05 and SOW-062; `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14 and 15; `docs/PLAN.md` R4; `docs/PRD.md` Section 8.15 with MATCH status. (reconciled under D-APP-38).
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-06-05-REQ-001 | Bash MUST be denied by default even when the SDK ships or supports a `Bash` tool. | `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
> | DEL-06-05-REQ-002 | Bash MUST be denied or omitted from tool exposure in `readOnly` mode. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/SPEC.md` Section 15.1 |
> | DEL-06-05-REQ-003 | Bash MUST be denied without prompting in `dontAsk` unless an accepted future policy explicitly defines a safe shell subset. Current source material defines no such subset. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/PLAN.md` R4 acceptance |
> | DEL-06-05-REQ-004 | Bash MUST NOT be enabled by `allowedTools` alone; restriction and enablement MUST be mediated by disallowed tools, permission mode, Chirality policy, hooks, `canUseTool`, and/or human gate as applicable. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
> | DEL-06-05-REQ-005 | A denied Bash request MUST NOT spawn a process. | `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
> | DEL-06-05-REQ-006 | Enabling Bash MUST require a timeout before execution. The accepted default is `120000` ms and the maximum override is `600000` ms. | `docs/CONTRACT.md` Section 1.6 K-BASH-1; D-APP-56 R4-P09; `frontend/src/lib/harness/tool-shell-policy.ts` |
> | DEL-06-05-REQ-007 | Allowed Bash execution MUST capture stdout and stderr separately. | `docs/PLAN.md` R4 implementation targets; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
> | DEL-06-05-REQ-008 | Medium or large Bash output MUST be previewed or stored under session artifacts rather than streamed unbounded into chat/model context. | `docs/PRD.md` FR-096, MATCH status; `docs/PLAN.md` R4 — reconciled under D-APP-38 |
> | DEL-06-05-REQ-009 | Bash output metadata MUST include safe artifact lookup and terminal-outcome data. D-APP-42 assigns the artifact schema (`toolName`, `toolUseId`, `turnId`, byte lengths, truncation flag, SHA-256, relative artifact path, and stdout/stderr stream labels); ADQ-11/D-APP-43 establishes `interrupted` Bash results as `tool.failed` terminal evidence. | `docs/TYPES.md` `outputArtifactPath`; D-APP-42; `Evidence_ADQ-11_Permission_Tool_Residuals.md`; D-APP-43 |
> | DEL-06-05-REQ-010 | Allowed Bash execution MUST support interrupt/cancel where the SDK or process runner exposes that capability; where interruption cannot be performed, Chirality MUST persist the terminal failure, cancellation, or residual-risk outcome that actually occurred rather than claiming successful interruption. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` Section 1.5 K-EVENT-3; `docs/PLAN.md` R4 acceptance |
> | DEL-06-05-REQ-011 | Bash permission, start, completion, failure, timeout, and interruption behavior MUST be auditable in product-owned Chirality event records. | `docs/CONTRACT.md` Section 1.5 K-EVENT-2 through K-EVENT-4; `docs/TYPES.md` event vocabulary |
> | DEL-06-05-REQ-012 | Hook failures MUST fail closed for shell actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
> | DEL-06-05-REQ-013 | Bash commands that can affect filesystem state MUST remain subject to working-root containment, instruction-root protection, symlink write rejection, redaction, provenance, and hook policy where applicable. | `docs/CONTRACT.md` Section 1.6 K-PERM-1, K-PATH-2, K-PATH-3; `docs/SPEC.md` Section 15.2 |
> | DEL-06-05-REQ-014 | Public Chirality APIs, permission records, and audit events MUST remain product-owned; SDK Bash names and transcript fields are adapter metadata. | `docs/DIRECTIVE.md` Sections 2.8 and 2.10; `docs/SPEC.md` Sections 10.1 and 10.2 |
> | DEL-06-05-REQ-015 | Tests MUST cover default deny, `readOnly` deny, `dontAsk` deny, denied-never-spawns, timeout, stdout/stderr separation, output artifact metadata, and interruption behavior where technically available. | `_CONTEXT.md`; `docs/PLAN.md` R4 acceptance |
> | DEL-06-05-REQ-016 | Bash preflight MUST enforce the implemented command metadata and network posture checks: command name/length, timeout, redirection/path-token counts, network-command denial, and URL-scheme denial. | `frontend/src/lib/harness/tool-shell-policy.ts`; `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard or governing source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool exposure, hook, path, and Bash invariants. |
> | `docs/CONTRACT.md` Section 1.5 | Runtime event and audit mirror invariants. |
> | `docs/SPEC.md` Sections 14 and 15 | SDK tool naming, tool surface rules, permission mode mapping, required hooks, and fail-closed hook behavior. |
> | `docs/TYPES.md` Section 8 | Permission mode vocabulary, permission decision shape, tool-surface terms, and `ToolResultStore`. |
> | `docs/PLAN.md` R4 | Roadmap sequencing and acceptance criteria for Bash, result budgeting, and context mirror behavior. |
> | `docs/PRD.md` Section 8.15 | Product requirements for tool output storage, Bash, context management, and audit mirror; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |
>

### CLM-011 — Verification

> ##### Verification
>
> | Requirement | Verification approach |
> |---|---|
> | DEL-06-05-REQ-001 through REQ-004 | Unit or integration tests assert `Bash` is absent or denied by default, in `readOnly`, and in `dontAsk`; tests prove `allowedTools` cannot bypass denial. |
> | DEL-06-05-REQ-005 | Spawn-suppression test instruments the command runner and asserts denied Bash requests never create a process. |
> | DEL-06-05-REQ-006 | Timeout preflight tests assert no allowed Bash request can execute without the accepted `120000` ms default / `600000` ms maximum policy. |
> | DEL-06-05-REQ-007 | Capture tests run a controlled command that writes separately to stdout and stderr and assert separate capture channels. |
> | DEL-06-05-REQ-008, REQ-009 | Tool-result budget tests assert large output is stored as an artifact and chat/event payloads contain preview plus safe artifact metadata. |
> | DEL-06-05-REQ-010 | Interrupt tests assert active Bash can be cancelled or interrupted when supported; fallback tests assert unsupported interruption persists the actual terminal failure, cancellation, or residual-risk outcome. |
> | DEL-06-05-REQ-011 | Runtime event tests assert permission/start/completed/failed or interrupted evidence is written to Chirality-owned event records. |
> | DEL-06-05-REQ-012, REQ-013 | Hook/path tests assert hook failure and path-policy denial block Bash execution or filesystem mutation. |
> | DEL-06-05-REQ-014 | Contract tests assert public event/permission schemas do not become SDK-shaped except for safe adapter metadata. |
> | DEL-06-05-REQ-015 | Traceability check verifies test names or metadata cite DEL-06-05 and SOW-062; concrete test names, fixtures, and harness paths remain TBD until implementation planning assigns them. |
> | DEL-06-05-REQ-016 | Preflight-contract review verifies command metadata fields and network posture checks are either implemented from an accepted contract or explicitly deferred with cited ownership. |
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required implementation evidence:
>
> - Bash governance policy or options-builder slice showing default denial and explicit enablement rules.
> - Timeout/capture policy with explicit default and override constraints once human-approved or source-defined.
> - Output metadata schema or fixture for stdout/stderr preview and artifact storage, including PRD-derived artifact metadata fields only while the REF-006 MATCH status remains visible. (reconciled under D-APP-38).
> - Denied-never-spawns test evidence.
> - Timeout/capture and interruption test evidence.
> - Hook/path interface evidence showing composition with DEL-06-04 and DEL-06-06 once those interfaces are accepted.
> - Residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state. (reconciled under D-APP-38).
>

### CLM-013 — Traceability

> ##### Traceability
>
> | Source item | Covered by |
> |---|---|
> | SOW-062 Bash denied by default and governed when enabled | DEL-06-05-REQ-001 through REQ-015 |
> | OBJ-005 Runtime tool execution governance | DEL-06-05-REQ-001 through REQ-014 |
> | K-BASH-1 Bash default denial and enablement prerequisites | DEL-06-05-REQ-001, REQ-006 through REQ-011, REQ-015 |
> | FR-100 Bash denied by default, capture, timeout, storage, interrupt | DEL-06-05-REQ-001, REQ-005 through REQ-010 |

- **AC-001** — The output demonstrates that Bash is denied by default and, when enabled, is governed by explicit mode, timeout, separate output capture, result storage, interruption handling, and audit behavior.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-06-05 Bash Governance and Timeout Policy

> #### Procedure: DEL-06-05 Bash Governance and Timeout Policy
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-015 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-05 Bash governance implementation and timeout/capture policy evidence. It is written for the deliverable artifact, not as an end-user shell runbook.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Accepted DEL-06-05 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
> | Binding Bash invariant | Available in `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
> | Permission/mode vocabulary | Available in `docs/TYPES.md` Section 8 and `docs/SPEC.md` Section 15.1 |
> | Tool-surface rules | Available in `docs/SPEC.md` Section 14.3 |
> | R4 sequencing and acceptance criteria | Available in `docs/PLAN.md`; `docs/PRD.md` is current and MATCH — reconciled under D-APP-38 |
> | Declared upstream dependencies | Extracted ACTIVE upstream rows exist in `_DEPENDENCIES.md`; declared upstream remains TBD until dependency satisfaction is accepted. |
> | Exact implementation file paths | TBD |
> | Exact test fixture paths | TBD |
> | Bash-specific numeric timeout default and maximum | TBD - required by policy but not specified in accessible sources |
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Establish the default-deny posture.
>    - Ensure SDK `Bash` is not exposed by default.
>    - Add explicit denial for Bash in `readOnly` and `dontAsk`.
>    - Verify denial is enforced by runtime policy, not prompt text.
>
> 2. Resolve Bash tool exposure through the permission overlay.
>    - Treat SDK `Bash` as a governed tool candidate, not as automatically available.
>    - Apply `disallowedTools`, permission mode, Chirality policy, hooks, and `canUseTool` mediation as applicable.
>    - Do not rely on `allowedTools` as a restriction mechanism.
>
> 3. Implement Bash preflight.
>    - Require explicit mode or session capability that permits Bash.
>    - Require a timeout policy before execution.
>    - Require stdout/stderr capture plan.
>    - Require result storage or preview policy for medium/large outputs.
>    - Require audit metadata sufficient to record permission, start, terminal outcome, and artifact references.
>    - Treat command metadata fields and network posture checks as unresolved preflight slots until an accepted contract defines them or assigns them outside DEL-06-05. PRD R4 mentions both, but REF-006 remains MATCH-confirmed. (reconciled under D-APP-38).
>
> 4. Enforce denied-never-spawns.
>    - Place denial checks before process creation.
>    - Instrument tests or runner seams so a denied Bash request proves no child process was started.
>
> 5. Execute governed Bash only after preflight passes.
>    - Start the process with the resolved timeout.
>    - Capture stdout and stderr separately.
>    - Track exit code, timeout, interruption, cancellation, and failure classifications where available.
>    - If the SDK or process runner cannot interrupt an active Bash process, persist the actual terminal failure, cancellation, or residual-risk outcome instead of reporting successful interruption.
>    - Redact secrets from logs, tool outputs, and event records where policy requires.
>
> 6. Store and summarize output.
>    - Inline only small safe outputs.
>    - Preview medium/large outputs.
>    - Store raw large outputs under session artifacts and persist safe metadata such as artifact path, byte counts, truncation status, and channel labels where the accepted schema permits.
>    - Apply the D-APP-42 artifact schema (`toolName`, `toolUseId`, `turnId`, byte lengths, truncation, SHA-256, relative path, stdout/stderr labels) and the ADQ-11/D-APP-43 mapping of `interrupted: true` to `tool.failed` terminal evidence.
>
> 7. Persist audit evidence.
>    - Persist permission evidence before allowing execution.
>    - Persist tool started/completed/failed events and terminal success/failure/interruption/cancellation outcomes.
>    - Keep SDK transcript linkage secondary to Chirality-owned event records.
>
> 8. Add tests and traceability.
>    - Add default deny, `readOnly` deny, `dontAsk` deny, denied-never-spawns, timeout-required, stdout/stderr separation, output artifact metadata, and interruption tests.
>    - Tag or name tests with DEL-06-05 or SOW-062 where local test conventions allow.
>    - Record the PRD MATCH status in implementation or review notes. (reconciled under D-APP-38).
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Default posture | Bash is denied or omitted with no explicit enablement. |
> | `readOnly` behavior | Bash cannot execute. |
> | `dontAsk` behavior | Bash denies without prompting. |
> | `allowedTools` misconception | Tests show `allowedTools` cannot enable or restrict Bash by itself and cannot bypass deny policy. |
> | Denied-never-spawns | Denied Bash request creates no child process. |
> | Timeout preflight | Allowed Bash cannot start without a resolved timeout policy. |
> | Capture channels | stdout and stderr are captured separately. |
> | Output budget | Large output is stored as an artifact and represented by preview/metadata. |
> | Interrupt behavior | Active Bash can be interrupted when supported, and terminal outcome is persisted. |
> | Audit records | Permission, start, completion/failure/interruption, and artifact metadata are persisted in Chirality-owned event shape. |
> | Hook fail-closed | Hook failure blocks shell execution. |
> | PRD warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
>

### CLM-019 — Records

> ##### Records
>
> - Bash governance policy or options-builder slice: TBD.
> - Bash preflight hook or equivalent enforcement point: TBD.
> - Timeout default and override policy: TBD.
> - stdout/stderr capture evidence: TBD.
> - Tool output artifact metadata fixture: TBD.
> - Denied-never-spawns test evidence: TBD.
> - Interruption/timeout terminal outcome test evidence: TBD.
> - Hook/path composition evidence with DEL-06-04 and DEL-06-06: TBD.
> - Concrete test names, fixtures, and harness paths for DEL-06-05 / SOW-062 traceability: TBD.
> - Review note for PRD MATCH: required under the reconciled D-APP-38 source state. (reconciled under D-APP-38).

- **VER-001** — Review the Bash deny/default, timeout/capture, output metadata, interruption, and audit evidence against the accepted SOW-062 and OBJ-005 basis.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-06-05 Bash Governance and Timeout Policy

> #### Guidance: DEL-06-05 Bash Governance and Timeout Policy
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-021 — Purpose

> ##### Purpose
>
> DEL-06-05 exists to prevent the SDK `Bash` surface from becoming an accidental escape hatch. Bash is powerful enough to read, write, delete, invoke networks, spawn long-running work, and produce unbounded output, so Chirality treats it as denied by default and enables it only after product-owned governance, timeout, result storage, interruption, and audit behavior are ready.
>
> Sources: `_CONTEXT.md`; decomposition row SOW-062; `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4.
>

### CLM-022 — Principles

> ##### Principles
>
> 1. Denied Bash must be a non-event at the process layer. A policy denial is only effective if no shell process starts. Sources: `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, MATCH status. (reconciled under D-APP-38).
> 2. Bash exposure follows capability-forward permission semantics with explicit hard-deny precedence. Any explicit deny from policy, hook, path check, governance, SDK deny rule, or human gate blocks execution. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-1.
> 3. `allowedTools` is not a security boundary. Bash must not become available merely because it appears in a tool list; the overlay, disallowed tools, mode policy, hooks, and approval mediation remain controlling. Sources: `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3.
> 4. Timeout and result storage are part of authorization, not post-processing. A Bash request without a timeout/capture/storage plan is not ready to execute. Source: `docs/CONTRACT.md` Section 1.6 K-BASH-1.
> 5. Auditability is product-owned. SDK transcripts may help debugging and resume, but Chirality event records remain canonical for runtime governance. Sources: `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/PRD.md` FR-121, MATCH status. (reconciled under D-APP-38).
>

### CLM-023 — Considerations

> ##### Considerations
>

### CLM-024 — Mode Behavior

> ###### Mode Behavior
>
> | Mode | Guidance | Source |
> |---|---|---|
> | `readOnly` | Bash should be unavailable or hard-denied. Treat shell as write/network-capable even when a proposed command appears read-like. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/TYPES.md` Section 8.1 |
> | `dontAsk` | Bash should deny without prompting. The accessible sources do not define an approved safe-shell subset. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/PLAN.md` R4 |
> | `ask` | Bash may request approval only after the command has passed policy preflight and the approval decision can be persisted before SDK allow/deny return. | `docs/SPEC.md` Section 15.1 |
> | `workspaceWrite` | Bash still needs explicit Bash governance; write permission does not imply shell permission. | `docs/SPEC.md` Section 15.1; `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
> | `bypass` | Developer-local only, never ordinary shipped behavior, and still subject to Chirality deny hooks and disallowed tools. | `docs/CONTRACT.md` Section 1.6 K-PERM-6 |
>

### CLM-025 — Timeout And Capture Policy

> ###### Timeout And Capture Policy
>
> The accessible sources require a timeout but do not provide a Bash-specific numeric default or maximum. Keep numeric values as `TBD` until accepted source or human ruling supplies them. The implementation should nevertheless require a timeout field or resolved timeout policy before a command can start.
>
> Stdout and stderr should be captured separately so users and replay tooling can distinguish normal command output from warnings/errors. Large output should be stored under session artifacts and represented by safe metadata, not streamed unbounded into chat or model context.
>

### CLM-026 — Hooks And Path Policy

> ###### Hooks And Path Policy
>
> Bash-specific governance should compose with the broader hook model. If a command can write, delete, traverse outside the project, touch the instruction root, follow symlink writes, or invoke prohibited network behavior, the same capability-forward posture with explicit hard-deny precedence applies. Hook failures fail closed for shell actions.
>

### CLM-027 — PRD Hash Status

> ###### PRD Hash Status
>
> `docs/PRD.md` is listed as MATCH in `_REFERENCES.md`. FR-096, FR-100, FR-121, and R4 implementation targets are useful product direction for this draft, but any implementation detail that depends only on PRD wording should be rechecked after source-state reconciliation. (reconciled under D-APP-38).
>

### CLM-028 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Omit Bash vs expose and deny | Prefer omission where possible to reduce accidental model attempts, but still enforce runtime denial because tool visibility is not enough. |
> | Single global timeout vs command-class timeout | A single default is simpler, but command-class overrides may be needed. Source material does not decide this; mark numeric policy as TBD. |
> | Inline output vs artifact storage | Inline small output for usability; preview/store medium or large output so chat and model context remain bounded. |
> | User approval vs policy denial | Do not ask the user to approve a command that fails policy preflight. Approval should only mediate commands that are otherwise governable. |
> | SDK transcript vs Chirality events | Use SDK transcript linkage for resume/debugging, but rely on Chirality events for accepted-turn, permission, tool, artifact, and terminal outcome audit. |
>

### CLM-029 — Examples

> ##### Examples
>
> | Scenario | Expected result |
> |---|---|
> | A new session starts with no explicit Bash enablement | `Bash` is omitted or denied. |
> | `readOnly` session requests `Bash` for `ls` | Deny or omit; use read tools such as `LS`, `Glob`, or `Grep` where available instead. |
> | `dontAsk` session requests `Bash` for any command | Deny without prompting under current source policy. |
> | `ask` session requests a command without timeout metadata | Deny before approval because timeout is a prerequisite. |
> | Governed mode requests Bash with timeout, capture, and result-storage policy | Run only if policy, hooks, path checks, and approval mediation pass; capture stdout/stderr separately and persist audit events. |
> | Command output exceeds inline budget | Store raw output under session artifacts and surface preview plus safe artifact metadata. |
> | Active Bash is interrupted | Persist interrupted/cancelled terminal outcome and retain available output metadata according to result policy. |
>

### CLM-030 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | TBD | No direct source conflict identified during P1/P2. PRD has a MATCH source state. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections used above | All PRD-cited requirements and guidance | Treat PRD as a current MATCH source under the reconciled D-APP-38 source state. | TBD — reconciled under D-APP-38 |
> | DEL-06-05-TIMEOUT-001 | Bash timeout values were formerly TBD. | `docs/CONTRACT.md` Section 1.6 K-BASH-1; D-APP-56 R4-P09 | Live policy enforces default `120000` ms and maximum `600000` ms. | `Specification.md` REQ-006; `frontend/src/lib/harness/tool-shell-policy.ts` | Ratified by D-APP-56; preserve this row as resolved history. | RESOLVED 2026-07-12 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-062 OBJ-005 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
