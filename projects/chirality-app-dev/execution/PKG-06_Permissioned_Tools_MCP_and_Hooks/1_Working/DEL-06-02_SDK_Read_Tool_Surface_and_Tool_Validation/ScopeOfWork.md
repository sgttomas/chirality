---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-02
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-047, SOW-049, SOW-050]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-02` in service of project scope [SOW-047, SOW-049, SOW-050] and package objectives [OBJ-005].

- **OUT-001** — A deterministic SDK read-tool surface resolver and validation contract that maps registered SDK and Chirality MCP names, rejects unknown names, orders exposure stably, and exposes read tools before write, edit, or bash capability.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-02 SDK Read Tool Surface and Tool Validation

> #### Datasheet: DEL-06-02 SDK Read Tool Surface and Tool Validation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-06-02 |
> | Deliverable name | SDK Read Tool Surface and Tool Validation |
> | Package | PKG-06 Permissioned Tools, MCP, and Hooks |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible party | TBD |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Context envelope | M |
> | Scope items | SOW-047, SOW-049, SOW-050 |
> | Objective context | OBJ-005 |
> | Anticipated artifacts | Tool resolver; unknown-tool tests; deterministic ordering fixtures |
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-047 through SOW-050.
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary feature | Resolve `opts.tools` to registered SDK built-ins or Chirality MCP names. | `_CONTEXT.md`; decomposition DEL-06-02 |
> | Unknown-tool behavior | Unknown tool names produce structured validation errors and are not silently passed through. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, MATCH status — reconciled under D-APP-38 |
> | SDK built-in candidates | `Read`, `LS`, `Glob`, `Grep`, `Write`, `Edit`, `Bash` where available. | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.3 |
> | Initial read surface | SDK read tools plus Chirality read MCP tools are enabled before write/edit/bash capability. | `docs/PRD.md` Section 8.13, MATCH status; `docs/PLAN.md` R2 — reconciled under D-APP-38 |
> | Chirality MCP namespace | Chirality-specific deterministic tools use `mcp__chirality__*` names. | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.4 |
> | Initial Chirality MCP read candidates | `mcp__chirality__status_read`, `mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, and scaffold preview/dry-run where appropriate. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
> | Determinism condition | Tool-surface ordering, naming, MCP server IDs, and allow/deny lists are stable for a given session, persona, mode, and option set. | `docs/PRD.md` Section 8.13, MATCH status; decomposition SOW-049 — reconciled under D-APP-38 |
> | Exposure boundary | Tool implementation availability does not imply model exposure. | decomposition SOW-049; `docs/CONTRACT.md` Section 1.6 K-TOOL-2 |
> | Restriction boundary | `allowedTools` alone is not a restriction boundary. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Constraint | Source |
> |---|---|---|
> | PRD source state | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
> | Package boundary | DEL-06-02 is bounded to tool exposure and validation; domain-engine operation semantics are excluded except protected-path hooks in adjacent scopes. | `_CONTEXT.md`; decomposition PKG-06 |
> | Permission overlay dependency | Capability-forward policy with explicit hard-deny precedence mode semantics and `canUseTool` mediation are adjacent policy inputs, primarily owned by DEL-06-01. | decomposition DEL-06-01 and DEL-06-02 |
> | MCP implementation boundary | Chirality MCP tool definitions are adjacent to this resolver, primarily owned by DEL-06-03. | decomposition DEL-06-03 |
> | Write/bash sequencing | Write/edit and bash capability remain later-phase surfaces and must not be exposed by the read-first resolver until the required hooks and governance land. | `docs/PRD.md` Section 8.13, MATCH status; `docs/PLAN.md` R2/R3 — reconciled under D-APP-38 |
> | Shipped runtime posture | `readOnly` mode exposes or allows read-only tools only; write/edit/bash/network-capable tools are unavailable or hard-denied. | `docs/PRD.md` Section 8.14, MATCH status; `docs/TYPES.md` Section 8.1 — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Construction note | Source |
> |---|---|---|
> | Tool registry | Maintain an explicit registry of SDK built-ins and Chirality MCP tool names eligible for resolution. Exact registry file path: TBD. | `docs/SPEC.md` Sections 14.1 and 14.2 |
> | Resolver input | Consume resolved runtime options, including `opts.tools`, plus session/persona/mode/policy context needed for deterministic exposure. Exact interface shape: TBD. | `docs/PRD.md` FR-023 and Section 8.13, MATCH status — reconciled under D-APP-38 |
> | Name validation | Reject unknown `opts.tools` entries with structured validation errors before SDK request construction. | `docs/SPEC.md` Section 14.3; decomposition SOW-047 |
> | Deterministic ordering | Normalize the visible tool list into stable order for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | `docs/CONTRACT.md` Section 1.6 K-TOOL-1; `docs/PRD.md` FR-080, MATCH status — reconciled under D-APP-38 |
> | Read-first filtering | Build the initial exposed surface from SDK read tools and Chirality read MCP tools; exclude or deny write/edit/bash until later phases. | `docs/PRD.md` Section 8.13, MATCH status; `docs/PLAN.md` R2 — reconciled under D-APP-38 |
> | Permission handoff | Feed the resolved tool surface into the Chirality permission overlay; do not rely on `allowedTools` alone for restriction. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
> | Tests | Include unknown-tool tests and deterministic ordering fixtures. Exact test paths: TBD. | `_CONTEXT.md`; decomposition DEL-06-02 |
>

### CLM-006 — Pending Implementation Evidence

> ###### Pending Implementation Evidence
>
> | Evidence slot | Current disposition | Source |
> |---|---|---|
> | Implementation, registry, metadata, and fixture paths | TBD until implementation ownership assigns concrete files; do not infer paths from planned artifact names. (P3: B-001) | `_CONTEXT.md` Anticipated Artifacts; `docs/CONTRACT.md` K-INVENT-1 |
> | Terminology boundary | Use "read-first" for sequencing, "read-only" for capability class, and `readOnly` only for the runtime mode token. (P3: B-002) | `docs/TYPES.md` Section 8.1; `docs/PLAN.md` R2 |
>

### CLM-007 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` Sections 2 and 4 | Product-owned runtime governance, filesystem truth, read-before-powerful-tool posture | MATCH |
> | REF-002 | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool, and MCP invariants | MATCH |
> | REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool names, MCP tools, surface rules, mode mapping | MATCH |
> | REF-004 | `docs/TYPES.md` Section 8 | Permission modes and tool-surface vocabulary | MATCH |
> | REF-005 | `docs/PLAN.md` R2/R3 | Implementation sequencing and acceptance context | MATCH |
> | REF-006 | `docs/PRD.md` Sections 8.13, 8.14, R2, KG-005, KG-023 | Product requirements and implementation direction | MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-06-02 SDK Read Tool Surface and Tool Validation

> #### Specification: DEL-06-02 SDK Read Tool Surface and Tool Validation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> DEL-06-02 specifies the read-first SDK tool-surface resolver and validation behavior for PKG-06. It covers mapping `opts.tools` to registered SDK built-ins or Chirality MCP names, rejecting unknown names, producing deterministic tool exposure for a resolved runtime context, and enabling read tools before write/edit/bash capability.
>
> In scope:
>
> - Resolve requested tool names against explicit SDK built-in and Chirality MCP registries.
> - Reject unknown tool names with structured validation errors before SDK request construction.
> - Produce deterministic tool-surface ordering for stable session/persona/mode/policy inputs.
> - Expose SDK read tools and Chirality read MCP tools as the initial user-visible tool surface.
> - Ensure implementation availability does not itself imply model exposure.
> - Add unknown-tool tests and deterministic ordering fixtures.
>
> Out of scope:
>
> - Capability-forward policy with explicit hard-deny precedence permission decision semantics, mode mapping, and `canUseTool` approval mediation, except where this resolver consumes or forwards their policy outputs. Those are primarily DEL-06-01.
> - In-process MCP tool implementation details and wrapper metadata, which are primarily DEL-06-03.
> - Write/edit path hooks and provenance capture, which are DEL-06-04.
> - Bash enablement and timeout/capture policy, which are DEL-06-05.
> - Remote MCP, plugins, broad tool search, marketplace extension, and remote execution, which remain out of current scope without governed amendment.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/SPEC.md` Sections 14 and 15; `docs/CONTRACT.md` Section 1.6; `docs/PRD.md` Section 8.13 with MATCH status. (reconciled under D-APP-38).
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-06-02-REQ-001 | The resolver MUST map `opts.tools` entries only to registered SDK built-ins or registered Chirality MCP tool names. | decomposition SOW-047; `docs/PRD.md` FR-078, MATCH status — reconciled under D-APP-38 |
> | DEL-06-02-REQ-002 | Unknown `opts.tools` names MUST produce structured validation errors and MUST NOT be silently passed through to SDK configuration or model context. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` FR-078, MATCH status — reconciled under D-APP-38 |
> | DEL-06-02-REQ-003 | SDK built-in mappings MUST use SDK names where available, including read candidates `Read`, `LS`, `Glob`, and `Grep`, and later powerful candidates `Write`, `Edit`, and `Bash`. | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.3 |
> | DEL-06-02-REQ-004 | Chirality-specific deterministic tools MUST use the `mcp__chirality__*` naming convention and resolve only from the accepted Chirality MCP registry. | `docs/SPEC.md` Sections 14.1 and 14.2; `docs/TYPES.md` Section 8.4 |
> | DEL-06-02-REQ-005 | Tool-surface construction MUST be deterministic for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | `docs/CONTRACT.md` Section 1.6 K-TOOL-1; `docs/PRD.md` FR-080, MATCH status — reconciled under D-APP-38 |
> | DEL-06-02-REQ-006 | Tool implementation availability MUST NOT imply model exposure; a tool must pass resolver and permission-surface checks before exposure. | `docs/CONTRACT.md` Section 1.6 K-TOOL-2; decomposition SOW-049 |
> | DEL-06-02-REQ-007 | Initial user-visible capability MUST expose read-only SDK tools and Chirality read MCP tools before write/edit/bash capability. | decomposition SOW-050; `docs/PRD.md` FR-082, MATCH status — reconciled under D-APP-38 |
> | DEL-06-02-REQ-008 | Write/edit and bash tools MUST remain excluded or denied by the read-first surface until the later write/bash governance phases activate them. | `docs/PRD.md` Section 8.13, MATCH status; `docs/PLAN.md` R2/R3 — reconciled under D-APP-38 |
> | DEL-06-02-REQ-009 | The resolver MUST NOT treat SDK `allowedTools` alone as a restriction boundary. Restriction requires disallowed tools, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture from the permission layer. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
> | DEL-06-02-REQ-010 | Denied tools SHOULD be omitted from model context where possible, while runtime denial remains required for safety. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` FR-081, MATCH status — reconciled under D-APP-38 |
> | DEL-06-02-REQ-011 | In `readOnly` mode, the resolved surface MUST expose or allow read-only tools only; write/edit/bash/network-capable tools are unavailable or hard-denied. | `docs/TYPES.md` Section 8.1; `docs/PRD.md` FR-091, MATCH status — reconciled under D-APP-38 |
> | DEL-06-02-REQ-012 | Resolver outputs SHOULD be represented in safe runtime metadata or boot fingerprints, including actual SDK tool names/versions and MCP server versions where available. | `docs/SPEC.md` Section 13; `docs/PRD.md` FR-029, MATCH status — reconciled under D-APP-38 |
> | DEL-06-02-REQ-013 | Tests MUST cover unknown tool names, deterministic ordering, and read-before-write/bash sequencing. | `_CONTEXT.md`; decomposition DEL-06-02; `docs/PLAN.md` R2 acceptance |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or governing source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` Section 1.6 | Binding permission/tool/MCP invariants, including deterministic exposure, implementation-vs-exposure separation, and `allowedTools` limitation. |
> | `docs/SPEC.md` Section 14 | SDK built-in names, Chirality MCP names, initial tool set, and surface rules. |
> | `docs/SPEC.md` Section 15 | Mode mapping and hook context consumed by tool-surface filtering. |
> | `docs/TYPES.md` Section 8 | Tool-surface vocabulary, permission modes, and initial MCP names. |
> | `docs/PLAN.md` R2/R3 | Sequencing: permission-gated read surface before controlled writes and bash. |
> | `docs/PRD.md` Section 8.13 | Product requirements for tool-surface behavior; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement | Verification approach |
> |---|---|
> | DEL-06-02-REQ-001, REQ-003, REQ-004 | Unit tests feed known SDK built-in and `mcp__chirality__*` names and assert canonical resolver outputs. |
> | DEL-06-02-REQ-002 | Unknown-tool tests assert structured validation error shape and assert unknown names are absent from emitted SDK options/model context. |
> | DEL-06-02-REQ-005 | Deterministic ordering fixtures vary input order and assert stable normalized output for the same session/persona/mode/policy context. |
> | DEL-06-02-REQ-006 | Tests assert registered implementation availability is insufficient unless resolver and permission-surface checks include the tool. |
> | DEL-06-02-REQ-007, REQ-008, REQ-011 | Read-first sequencing tests assert read tools can resolve in initial mode and write/edit/bash tools remain excluded or hard-denied until later policies are active. |
> | DEL-06-02-REQ-009 | Tests assert `allowedTools` is not treated as containment and cannot bypass deny inputs from the permission layer. |
> | DEL-06-02-REQ-010 | Surface-filtering tests assert denied tools are omitted where possible and still rejected if called. |
> | DEL-06-02-REQ-012 | Metadata or boot-fingerprint tests assert resolved tool names/versions and MCP server identifiers are stable and safe to record. Exact metadata path: TBD. |
> | DEL-06-02-REQ-013 | Test suite includes DEL-06-02 traceability markers or fixture names. Exact test paths: TBD. |
>

### CLM-013 — Pass 3 Verification Evidence Disposition

> ###### Pass 3 Verification Evidence Disposition
>
> | ItemID | Disposition | Source reread evidence |
> |---|---|---|
> | C-001 | Incorporated as a verification-evidence requirement while concrete implementation paths remain TBD. Resolver, registry, deterministic-ordering, and read-first evidence must be named before closure. | `docs/CONTRACT.md` K-TOOL-1/K-TOOL-2; `docs/SPEC.md` Sections 13 and 14.3 |
> | D-001 | Incorporated as explicit tests for permission-boundary bypass cases: `allowedTools` cannot override deny inputs, and implementation availability alone cannot expose a tool. | `docs/CONTRACT.md` K-PERM-3 and K-TOOL-2; `docs/SPEC.md` Section 14.3 |
> | E-001 | Converted to a metadata-path TBD. Safe metadata or boot-fingerprint evidence is required, but the exact record path is not assigned in the current sources. | `docs/SPEC.md` Section 13; `docs/PRD.md` FR-128 with MATCH status — reconciled under D-APP-38 |
>

### CLM-014 — Documentation

> ##### Documentation
>
> Required implementation evidence:
>
> - Tool resolver or equivalent deterministic tool-surface builder.
> - Registry of supported SDK built-ins and Chirality MCP names.
> - Structured validation error contract for unknown tool names.
> - Deterministic ordering fixtures.
> - Read-first sequencing tests.
> - Residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state. (reconciled under D-APP-38).
>
> Concrete evidence locations remain TBD until implementation ownership assigns files. The documentation package must not close DEL-06-02 solely on planned artifact names or decomposition prose. (P3: B-001, C-001, E-001)
>

### CLM-015 — Traceability

> ##### Traceability
>
> | Source item | Covered by |
> |---|---|
> | SOW-047 Tool option mapping | DEL-06-02-REQ-001 through REQ-004 |
> | SOW-049 Deterministic tool surface | DEL-06-02-REQ-005, REQ-006, REQ-010, REQ-012 |
> | SOW-050 Read tools before writes/bash | DEL-06-02-REQ-007, REQ-008, REQ-011, REQ-013 |
> | OBJ-005 Tool governance objective | DEL-06-02-REQ-001 through REQ-013 |

- **AC-001** — For identical resolved runtime context and requested registered tool set, the resolver produces stable ordered SDK and MCP exposure; unknown names yield structured validation errors before SDK request construction; and read-first or readOnly posture excludes or hard-denies write, edit, bash, and network-capable tools.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-06-02 SDK Read Tool Surface and Tool Validation

> #### Procedure: DEL-06-02 SDK Read Tool Surface and Tool Validation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-017 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-02 SDK read tool-surface resolver and validation evidence. It is written for the deliverable artifact, not as an end-user operation runbook.
>

### CLM-018 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Accepted DEL-06-02 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
> | Tool-surface vocabulary | Available in `docs/TYPES.md` Section 8 |
> | Binding permission/tool/MCP invariants | Available in `docs/CONTRACT.md` Section 1.6 |
> | SDK and MCP tool naming specification | Available in `docs/SPEC.md` Section 14 |
> | Mode and hook context | Available in `docs/SPEC.md` Section 15 |
> | Roadmap sequencing for R2/R3 | Available in `docs/PLAN.md`; `docs/PRD.md` is current and MATCH — reconciled under D-APP-38 |
> | Declared upstream dependencies | TBD - `_DEPENDENCIES.md` lists no accepted upstream edges yet |
> | Exact implementation file paths | TBD |
> | Exact test fixture paths | TBD |
>

### CLM-019 — Steps

> ##### Steps
>
> 1. Establish the accepted tool-name registry.
>    - Include SDK built-in candidates from `docs/SPEC.md` Section 14.1: `Read`, `LS`, `Glob`, `Grep`, `Write`, `Edit`, and `Bash` where available.
>    - Include accepted Chirality MCP names from `docs/SPEC.md` Section 14.2 and `docs/TYPES.md` Section 8.4.
>    - Do not introduce aliases or remote/plugin tool names without an accepted source update.
>
> 2. Define the resolver input and output.
>    - Input should include resolved runtime options, especially `opts.tools`, plus context needed for deterministic ordering and policy filtering.
>    - Keep the exact interface shape TBD until the runtime owner assigns the object or function boundary carrying `opts.tools`, session, persona, mode, SDK version, MCP server set, and permission policy. (P3: F-001)
>    - Output should identify SDK built-ins and Chirality MCP tools in the form required by SDK options/MCP configuration.
>    - Keep SDK-specific values as adapter metadata, not public Chirality contract terms.
>
> 3. Validate requested names.
>    - For each `opts.tools` entry, resolve against the accepted registry.
>    - If a name is unknown, produce a structured validation error and stop before SDK request construction.
>    - Keep the exact structured validation error type and fixture assertion shape TBD until the implementation contract is named. (P3: C-002)
>    - Ensure unknown names are not present in emitted SDK options or model context.
>
> 4. Apply read-first sequencing.
>    - Permit initial exposure of SDK read candidates (`Read`, `LS`, `Glob`, `Grep`) where available.
>    - Permit initial exposure of Chirality read MCP tools such as status read, dependency read, scope scan, and scaffold preview/dry-run where supported by registry policy.
>    - Exclude or deny `Write`, `Edit`, and `Bash` until later write/bash governance phases activate them.
>
> 5. Preserve permission policy boundaries.
>    - Do not treat `allowedTools` alone as restriction.
>    - Hand the resolved surface to capability policy with explicit hard-deny precedence, disallowed tools, hooks, `canUseTool`, and/or `dontAsk` posture as applicable.
>    - Ensure implementation availability does not override policy filtering.
>
> 6. Normalize deterministic ordering.
>    - Sort or otherwise canonicalize the final visible tool surface after validation and filtering.
>    - Use stable inputs: session, persona, mode, option set, SDK version, MCP server set, and permission policy.
>    - Record safe metadata or fingerprints when required by the runtime contract. Exact metadata path: TBD.
>
> 7. Add unknown-tool tests.
>    - Verify unknown names produce structured validation errors.
>    - Verify unknown names are absent from SDK options and model context.
>    - Include at least one unknown SDK-like name and one unknown `mcp__chirality__*` name.
>
> 8. Add deterministic ordering fixtures.
>    - Feed the same set of tools in varied input orders.
>    - Assert stable normalized output for identical context.
>    - Add fixture coverage for mixed SDK built-ins and Chirality MCP names.
>
> 9. Add read-first sequencing tests.
>    - Verify read candidates resolve in the initial surface.
>    - Verify write/edit/bash do not appear or are hard-denied in read-first/read-only posture.
>    - Verify `allowedTools` cannot cause a denied or unsupported tool to execute.
>
> 10. Record residual gaps.
>    - Keep exact implementation and fixture paths as `TBD` until assigned.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-020 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Registry validation | Only registered SDK built-ins and accepted `mcp__chirality__*` names resolve. |
> | Unknown-tool behavior | Unknown names produce structured validation errors and are not passed to the SDK. |
> | Determinism | Same context and tool set produce stable output ordering and identifiers. |
> | Read-first sequencing | Initial surface contains read tools only; write/edit/bash are excluded or hard-denied. |
> | Permission boundary | `allowedTools` does not restrict by itself and cannot bypass deny policy. |
> | Implementation-vs-exposure | SDK/tool implementation availability does not imply model exposure. |
> | MCP parity | Chirality MCP names pass through the same surface and permission path as SDK built-ins. |
> | PRD warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
>

### CLM-021 — Records

> ##### Records
>
> - Tool resolver implementation path: TBD.
> - SDK built-in and Chirality MCP registry path: TBD.
> - Structured validation error contract: TBD. (P3: C-002)
> - Unknown-tool test path: TBD. (P3: F-002)
> - Deterministic ordering fixture path: TBD. (P3: F-002)
> - Read-first sequencing test path: TBD. (P3: F-002)
> - Safe metadata or boot-fingerprint path for SDK names, versions, and MCP identifiers: TBD. (P3: E-001)
> - Trace package tying resolver, registry, error contract, fixtures, sequencing tests, and PRD warning note to implementation evidence: TBD. (P3: X-001)
> - Review note for PRD MATCH: required under the reconciled D-APP-38 source state. (P3: A-001, D-002, E-002) (reconciled under D-APP-38).

- **VER-001** — Run unit and fixture tests for registered and unknown names, permuted input ordering, implementation-versus-exposure separation, and read-first or readOnly deny behavior; inspect safe runtime metadata or boot fingerprints for stable tool and MCP identifiers.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-06-02 SDK Read Tool Surface and Tool Validation

> #### Guidance: DEL-06-02 SDK Read Tool Surface and Tool Validation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-023 — Purpose

> ##### Purpose
>
> DEL-06-02 exists to make `opts.tools` meaningful without letting SDK defaults or tool implementation availability define Chirality's runtime authority. It is the read-first tool-surface slice of PKG-06: it validates requested names, normalizes deterministic exposure, and hands the resulting surface to permission policy before model execution.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Section 14; `docs/PRD.md` Section 8.13 with MATCH status. (reconciled under D-APP-38).
>

### CLM-024 — Principles

> ##### Principles
>
> 1. Resolve before request construction. Tool names should be validated and normalized before SDK options or model context are built. Sources: decomposition SOW-047; `docs/PRD.md` FR-078, MATCH status. (reconciled under D-APP-38).
> 2. Unknown is an error, not a fallback. Unknown tool names should produce structured validation errors rather than being silently passed through. Source: `docs/SPEC.md` Section 14.3.
> 3. Determinism is part of the contract. Stable inputs should produce stable tool ordering, names, MCP server IDs, and allow/deny lists. Sources: decomposition SOW-049; `docs/CONTRACT.md` Section 1.6 K-TOOL-1.
> 4. Read tools come first. Initial exposure should be SDK read tools plus Chirality read MCP tools; write/edit/bash wait for later governance phases. Sources: decomposition SOW-050; `docs/PRD.md` FR-082, MATCH status. (reconciled under D-APP-38).
> 5. Exposure is separate from implementation. A tool being implemented or available in the SDK does not mean it belongs in model context. Source: `docs/CONTRACT.md` Section 1.6 K-TOOL-2.
> 6. `allowedTools` is not a safety boundary. Treat it as SDK posture/auto-approval input only; restriction still requires deny rules, mode policy, hooks, `canUseTool`, and/or `dontAsk`. Sources: `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3.
> 7. MCP is not a bypass. Chirality MCP names are transport exposure for deterministic operations, not a path around policy. Source: `docs/CONTRACT.md` Section 1.6 K-MCP-1.
>

### CLM-025 — Considerations

> ##### Considerations
>

### CLM-026 — Resolver Shape

> ###### Resolver Shape
>
> The resolver should be small and auditable:
>
> | Concern | Guidance |
> |---|---|
> | Registry ownership | Keep SDK built-in names and Chirality MCP names in an explicit registry or catalog. Exact path: TBD. |
> | Alias policy | Avoid implicit aliases unless a source file defines them. Current sources name SDK candidates and `mcp__chirality__*` names directly. |
> | Error shape | Return structured validation errors for unknown names. Exact error type: TBD. |
> | Ordering | Sort or otherwise normalize deterministically after validation and policy filtering. |
> | Output | Emit SDK-facing names and MCP server/tool identifiers as adapter metadata, not public product semantics. |
>

### CLM-027 — Read-First Surface

> ###### Read-First Surface
>
> Initial read candidates are `Read`, `LS`, `Glob`, and `Grep` where available, plus Chirality read MCP tools such as status read, dependency read, scope scan, and scaffold preview/dry-run. Do not use this deliverable to expose `Write`, `Edit`, or `Bash`; those require later hooks, path policy, output storage, and audit behavior.
>

### CLM-028 — Relationship to Adjacent Deliverables

> ###### Relationship to Adjacent Deliverables
>
> | Adjacent deliverable | Interface point |
> |---|---|
> | DEL-06-01 | Provides capability policy with explicit hard-deny precedence and mode policy that this resolver must consume or preserve. |
> | DEL-06-03 | Provides Chirality MCP read tool definitions that this resolver registers or references. |
> | DEL-06-04 | Provides write/edit hooks and path policy needed before powerful write tools can be exposed. |
> | DEL-06-05 | Provides bash governance needed before `Bash` can be exposed. |
> | DEL-05-05 | Provides tool result budget/artifact policy referenced by later tool-result handling. |
>

### CLM-029 — PRD Hash Status

> ###### PRD Hash Status
>
> `docs/PRD.md` is listed as MATCH in `_REFERENCES.md`. Its R2/Section 8.13 content aligns with matching SPEC, CONTRACT, TYPES, PLAN, and decomposition slices used here, but PRD-only implementation details should be reviewed after source-state reconciliation. (reconciled under D-APP-38).
>
> REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-030 — Terminology Normalization

> ###### Terminology Normalization
>
> Use the following terms distinctly:
>
> | Term | Use |
> |---|---|
> | read-first | Sequencing posture: read tools are enabled before write/edit/bash capability. |
> | read-only | Capability class: tools that do not write, shell out, or perform network-capable side effects. |
> | `readOnly` | Runtime mode token from the permission vocabulary. |
>
> This normalization preserves the difference between staged rollout, tool capability, and runtime mode policy. (P3: B-002)
>

### CLM-031 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Omit denied tools vs include and deny at call time | Prefer omission where possible to reduce context and accidental attempts, but never rely on omission alone; runtime denial must still hold. |
> | Strict registry vs permissive passthrough | Use strict registry behavior. Passthrough conflicts with SOW-047 and makes unknown tool names hard to audit. |
> | Resolver owns permission vs resolver consumes permission | Keep the resolver focused on validation and deterministic exposure. Capability-forward policy with explicit hard-deny precedence semantics belong to permission policy, but resolver output must not bypass it. |
> | SDK-specific names vs Chirality contracts | SDK names are adapter metadata. Public runtime contracts and event schemas should stay Chirality-owned. |
> | Read convenience vs staged governance | Exposing read tools first is useful, but it must not become a back door to write/bash or remote tool expansion. |
>

### CLM-032 — Examples

> ##### Examples
>
> | Scenario | Expected result |
> |---|---|
> | `opts.tools` contains `Read`, `Grep`, and `mcp__chirality__status_read` in read-first mode | Resolver accepts registered names and emits deterministic SDK/MCP surface order, subject to permission filtering. |
> | `opts.tools` contains `Read` and `UnknownSearch` | Resolver returns a structured validation error for `UnknownSearch`; unknown name is not sent to the SDK. |
> | SDK supports `Write`, but current mode is read-first/read-only | Resolver excludes or marks `Write` denied according to policy; implementation availability does not imply exposure. |
> | `allowedTools` includes a tool that Chirality policy denies | Final exposed/executable surface respects deny policy; `allowedTools` does not bypass restriction. |
> | A new `mcp__chirality__domain_*` name appears before governed domain amendment | Treat as unsupported/TBD unless accepted source updates authorize future domain tools. |
>

### CLM-033 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | TBD | No direct source conflict identified during P1/P2. PRD has a MATCH source state. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections used above | All PRD-cited requirements and guidance | Treat PRD as a current MATCH source under the reconciled D-APP-38 source state. | TBD — reconciled under D-APP-38 |
>

### CLM-034 — D-APP-56 roster clarification (2026-07-12)

> ##### D-APP-56 roster clarification (2026-07-12)
>
> R4-P27 reconciles the former unsupported/TBD domain-tool roster wording: PKG-10 owns the ruled domain-profile registry and proposal-tool roster. DEL-06-02 remains the SDK read-tool and validation owner and does not duplicate that ownership.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-047 SOW-049 SOW-050 OBJ-005 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
