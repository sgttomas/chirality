# Procedure: DEL-01-02 Reliance Boundary Register

## Purpose

This procedure describes how to produce, review, and maintain the Reliance Boundary Register for DEL-01-02. It is a production workflow for the register artifact, enforcement matrix, and test index, not a runtime implementation procedure.

## Prerequisites

| Prerequisite | Status / source |
|---|---|
| Deliverable-local context | `_CONTEXT.md` read for identity, scope, anticipated artifacts, and traceability. |
| Lifecycle state | `_STATUS.md` read; current P1/P2 drafting state was `OPEN`. |
| References | `_REFERENCES.md` read; REF-001 through REF-007 available. |
| Dependency declarations | `_DEPENDENCIES.md` read; upstream/downstream dependencies are TBD pending extraction. |
| Decomposition entry | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-01-02 row read. |
| Source-state warning | `docs/PRD.md` hash mismatch preserved as a warning. |
| Required source review | Directive, Contract, Spec, Types, Plan, PRD, and Software Decomp source slices reviewed. |

## Steps

### 1. Confirm Scope and Status

1. Read `_CONTEXT.md` and confirm:
   - `DeliverableID = DEL-01-02`
   - `DeliverableName = Reliance Boundary Register`
   - `Type = REQ_SLICE`
   - anticipated artifact includes `docs/harness/reliance_boundary_register.md`
2. Read `_STATUS.md`.
3. Proceed only if the current state permits drafting under the authorized overwrite set.
4. If current state is beyond the authorized set, stop and surface `SKIPPED_PROTECT_HUMAN_WORK`.

### 2. Load Authoritative Source Slices

1. Read `_REFERENCES.md`.
2. Verify each listed source path is locally accessible.
3. Record hash status for every reference.
4. Treat REF-006 `docs/PRD.md` `HASH_MISMATCH` as a source-state warning.
5. Read source slices for:
   - reliance-boundary definition and provider-neutral runtime ownership;
   - invariant catalog entries for engine, audit, permission, settings, hooks, lifecycle, filesystem, subagent, human gates, redaction, fallback;
   - runtime event, SDK option, hook, MCP, and validation requirements;
   - decomposition SOW/OBJ/DEL traceability.

### 3. Build Boundary Inventory

1. Create candidate rows for at least:
   - runtime engine contract;
   - runtime audit mirror;
   - structured permission decisions;
   - filesystem containment and instruction-root protection;
   - lifecycle status and human gates;
   - SDK transcript separation;
   - SDK settings isolation;
   - subagent governance;
   - deterministic tool surface and MCP wrappers;
   - hook lifecycle and fail-closed behavior;
   - secret redaction and key handling;
   - SDK fallback criteria.
2. Assign stable `BoundaryID` values.
3. For each row, define the protected Chirality product semantic in Chirality terms.
4. Cite source references.
5. Mark exact implementation file paths as `TBD` where downstream deliverables have not produced them yet.

### 4. Assign Enforcement Surfaces

For each boundary row:

1. Identify the enforcement owner:
   - Chirality code;
   - SDK option;
   - SDK hook/callback;
   - MCP wrapper;
   - human gate;
   - release check;
   - prompt support;
   - mixed.
2. Identify the concrete enforcement surface.
3. If the only surface is prompt support, mark the row incomplete for P0.
4. If the only surface is opaque SDK default behavior, mark the row incomplete for P0.
5. Add residual-risk notes where SDK behavior is not yet empirically verified.

### 5. Attach Validation Evidence

1. Map rows to existing Section 9 validation IDs where available:
   - `section9.runtime_engine_contract`
   - `section9.sdk_turn_engine_event_log`
   - `section9.sdk_message_mapper`
   - `section9.session_event_replay`
   - `section9.reliance_boundary_register`
   - `section9.settingsources_isolation`
   - `section9.sdk_session_link_resume`
   - `section9.permission_overlay_deny_first`
   - `section9.tool_runtime_read_file`
   - `section9.chirality_mcp_status_dependencies`
   - `section9.path_containment_hook`
   - `section9.instruction_root_protection_hook`
   - `section9.tool_result_budget`
   - `section9.context_compaction_boundary`
   - `section9.subagent_governance_hook`
2. Use `TBD` for validation IDs not yet implemented or not yet named.
3. Add test index rows that connect each validation ID to one or more boundary IDs.

### 6. Cross-Check Against Specification

1. Verify every Datasheet boundary ID has a corresponding Specification requirement or verification entry.
2. Verify every Specification requirement is reflected in either the boundary matrix, test index, residual-risk notes, or open items.
3. Verify Guidance principles do not overstate accepted implementation state.
4. Verify no source-warning item has been silently converted into accepted truth.
5. Verify all unsupported details remain `TBD`, `ASSUMPTION`, `PROPOSAL`, or conflict entries.
6. Verify PRD-cited rows distinguish hash-verified evidence from REF-006 warning-limited evidence.
7. Verify no candidate Section 9 validation label is represented as an implemented test until the downstream validation deliverable supplies the file or test name.

### 7. Produce Artifacts

1. Draft or update `docs/harness/reliance_boundary_register.md` from the schema and requirements in the four-document kit.
2. Create an enforcement matrix view suitable for implementation review.
3. Create a test index keyed by validation ID and boundary ID.
4. Carry forward:
   - `docs/PRD.md` hash mismatch warning;
   - SDK transcript placement residual risk;
   - SDK API drift residual risk;
   - subagent inherited-permission residual risk;
   - implementation-surface `TBD`s.
5. Record row-level completion criteria for any downstream `TBD`, including the expected source of closure evidence.

### 8. Review and Close

1. Run a consistency review across register rows, enforcement matrix, and test index.
2. Confirm there are no P0 rows with prompt-only or SDK-default-only enforcement.
3. Confirm human-gate and professional-boundary rows do not imply automated approval.
4. Confirm PRD hash mismatch is still visible until human/source reconciliation occurs.
5. Confirm the generated register, enforcement matrix, and test index can be traced back to the datasheet fields and specification requirements.
6. Move the deliverable to the next lifecycle state only through the authorized status workflow.

## Verification

| Verification item | Pass condition |
|---|---|
| Scope confirmation | DEL-01-02 identity and scope match `_CONTEXT.md` and decomposition row. |
| Source access | All listed sources are accessible, with REF-006 warning recorded. |
| Boundary coverage | All required boundary categories have rows. |
| Enforcement mapping | Each P0 row names a non-prompt-only and non-opaque-SDK-default enforcement surface. |
| Validation mapping | Each row has a validation ID or `TBD` with residual-risk explanation. |
| Human authority | No row states or implies automated professional approval, certification, issuance, or external validation. |
| Cross-document consistency | Datasheet, Specification, Guidance, and Procedure use the same boundary IDs and terms. |
| Source-state handling | REF-006 PRD usage is marked warning-limited until hash reconciliation or human/source-owner acceptance. |
| Generated-register closure | Downstream register rows are cross-checked against requirements, field schema, and test index before final acceptance. |

## Records

| Record | Purpose |
|---|---|
| `Datasheet.md` | Boundary taxonomy, source state, minimum fields, candidate validation index. |
| `Specification.md` | Normative requirements and verification expectations. |
| `Guidance.md` | Drafting principles, trade-offs, examples, conflict/source-warning table. |
| `Procedure.md` | Workflow for producing and maintaining the register. |
| `docs/harness/reliance_boundary_register.md` | Final register artifact once produced by downstream work. |
| Enforcement matrix | Reviewable mapping of boundaries to owners/surfaces. |
| Test index | Validation ID to boundary coverage map. |
| TASK run records | Evidence of bounded drafting and source-state warnings. |

## Remaining Blockers

| ID | Blocker | Required action |
|---|---|---|
| BLK-RBR-001 | `docs/PRD.md` hash mismatch | Human/source owner must reconcile expected hash or approve the current PRD as accepted source. |
| BLK-RBR-002 | Exact implementation surfaces not yet complete | Downstream runtime implementation deliverables must fill file paths and tests. |
| BLK-RBR-003 | SDK transcript and settings behavior require empirical probe | R0/R1 SDK probe and validation must confirm behavior before final acceptance. |
