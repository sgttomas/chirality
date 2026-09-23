---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-03
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-048, SOW-050, SOW-064, SOW-082]
package_objective_refs: [OBJ-005, OBJ-006]
---

# Scope of Work — DEL-06-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-03` in service of project scope [SOW-048, SOW-050, SOW-064, SOW-082] and package objectives [OBJ-005, OBJ-006].

- **OUT-001** — Accepted deterministic Chirality read-operation descriptors/composition and live application-tool conformance for status, dependencies, bounded scope scan and scaffold preview; the gated SOW-082 propose operation retains tuple/plan/once-per-chat validation and proposal.offered semantics.

**D-APP-80 concordance note (2026-07-28):** SOW-064 is supported here
through in-process deterministic MCP wrappers and the App extension
boundary. Remote MCP, plugin, and marketplace scope remain excluded.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

### Current acceptance obligations

Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### Seating and rulings

The D-APP-109 extraction and D-APP-110 retargeting are recorded in the existing dependency register; the former pending-extraction note is historical. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction. For propose: DEL-02-02-V3-04 selected, applicable DEL-08-01 trigger contract and DEL-06-02 catalog validation; ordinary current implementation/evidence gates for read tools; no new remote MCP/provider permission.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-03 Initial Chirality MCP Read Tools

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-06-03 |
> | DeliverableName | Initial Chirality MCP Read Tools |
> | PackageID | PKG-06 |
> | PackageName | Permissioned Tools, MCP, and Hooks |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | Scope | Expose in-process deterministic MCP tools for status read, dependency read, scope scan, and scaffold preview/dry-run. |
>

### CLM-003 — Attributes

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

Named verification: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

### CLM-004 — Conditions

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

Named verification: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

### CLM-005 — Construction

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

Unfinished delivery: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-006 — Pass 3 Notes

> ##### Pass 3 Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | C-001 | Incorporated with TBD boundary | Dependency read fallback now states the safe executable behavior for `_DEPENDENCIES.md`-only state and keeps final API shape `TBD` pending DEL-07-05. Source reread: `docs/SPEC.md` Sections 14.2 and 17.2; `docs/CONTRACT.md` Section 1.7 K-DEP-1; `_DEPENDENCIES.md` Extracted Dependency Register. |
>

### CLM-007 — References

> ##### References
>
> - `_CONTEXT.md` for deliverable identity, package scope, and anticipated artifacts.
> - `_REFERENCES.md` for source corpus and source-state warning.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 6, 7, 9, and 10A for objective, deliverable, SOW, and invariant-family mapping.
> - `docs/DIRECTIVE.md` Sections 13-14 for runtime integration boundaries and capability-forward MCP posture with explicit hard-deny precedence.
> - `docs/CONTRACT.md` Sections 1.6-1.7 for binding tool, MCP, permission, status, dependency, and invention invariants.
> - `docs/SPEC.md` Sections 14, 15, 17.2, and 19.3 for tool names, modes, API surfaces, and validation IDs.
> - `docs/TYPES.md` Sections 8.1-8.4 for permission and MCP vocabulary.
> - `docs/PLAN.md` R2 and R6 for sequencing and MCP extension boundaries.
> - `docs/PRD.md` Sections 8.13-8.14 and R2 traceability; MATCH status recorded in `_REFERENCES.md`. (reconciled under D-APP-38).

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-06-03 Initial Chirality MCP Read Tools

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-009 — Scope

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

Verification: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

### CLM-010 — Requirements

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| REQ-06-03-001 | Retain canonical identities for Chirality deterministic operations and prevent alias/catalog collisions at the current application-tool boundary. |
| REQ-06-03-002 | Provide the accepted status_read, deps_read and scope_scan operations through the live application-tool interface; compatibility-only descriptors do not satisfy exposure. |
| REQ-06-03-003 | Scaffold in this slice is preview/dry-run only and must not open uncontrolled writes. |
| REQ-06-03-004 | Application-tool descriptors declare schema, permissions, read-only/concurrency/interruption/execution/summarization behavior. |
| REQ-06-03-005 | Construct deterministic application-tool exposure from its effective catalog/policy basis; verify ordering rather than infer it from deduplication. |
| REQ-06-03-006 | Application tools retain their permission, path, redaction, event and applicable hook/validation controls. Native Codex tools independently follow selected Codex policy. |
| REQ-06-03-007 | Denied application calls must not execute and should be omitted from model context when supported. |
| REQ-06-03-008 | An allowed-name list is not an authorization boundary; application handler validation and actual Codex policy enforcement must each be evidenced. |
| REQ-06-03-009 | Read tools must remain nonmutating and must not smuggle shell, network or write actions into the read surface. |
| REQ-06-03-010 | Preserve actual application-tool permission/start/completion/failure evidence through Runtime events, without fabricating absent calls. |
| REQ-06-03-011 | _STATUS.md remains the canonical deliverable lifecycle source. |
| REQ-06-03-012 | Dependencies.csv supplies structured dependency truth; _DEPENDENCIES.md is the local explanatory index. Do not infer structured rows from prose. |
| REQ-06-03-013 | Scope scanning stays within the declared workspace/project root and does not read arbitrary external locations. |
| REQ-06-03-014 | Unknown or unsupported application-tool calls return structured validation errors rather than silent pass-through. |
| REQ-06-03-015 | When Dependencies.csv is absent, report explicit structured absence or secondary-summary status for _DEPENDENCIES.md; use the D-APP-43 resolved reader behavior and never invent rows. |

Verification: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

Evidence locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | SDK tool surface and Chirality MCP contract | Governs tool naming, initial tool set, deterministic ordering, and tool-surface rules. | `docs/SPEC.md` Section 14 |
> | Permission modes and hooks | Governs readOnly, workspaceWrite, dontAsk, ask, and bypass mapping to overlay policy. | `docs/SPEC.md` Section 15 |
> | Permission/tool/MCP invariants | Binding constraints for explicit hard-deny precedence, tool exposure, and MCP wrapper enforcement. | `docs/CONTRACT.md` Section 1.6 |
> | Lifecycle/dependency invariants | Binding constraints for `_STATUS.md`, dependency truth, provenance, and no-invention posture. | `docs/CONTRACT.md` Section 1.7 |
> | Permission and tool vocabulary | Defines permission modes, decision records, tool-surface terms, and MCP names. | `docs/TYPES.md` Section 8 |
> | R2 roadmap sequence | Requires permission-gated read surface and first MCP tools before write/bash expansion. | `docs/PLAN.md` R2; `docs/PRD.md` roadmap row R2 |
>

### CLM-012 — Verification

Required current checks: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

Named evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-013 — Acceptance Evidence Register

Required current checks: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

Named evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-014 — Documentation

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

Unfinished delivery: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-015 — Conflict Table

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-016 — Pass 3 Notes

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | F-001 | Converted to named TBD evidence | Concrete descriptor/wrapper metadata test names were added, while final implementation paths remain `TBD`. Source reread: `docs/PRD.md` Section 8.13 FR-079; `docs/SPEC.md` Section 14. |
> | F-002 | Incorporated with TBD artifact paths | Acceptance evidence for permission, hook, path, redaction, and event-policy traversal is now explicit. Source reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.3. |
> | X-002 | Incorporated with TBD closure paths | Verification now names concrete evidence categories and Section 9 mapping while preserving implementation paths as `TBD`. Source reread: `docs/SPEC.md` Section 19.3; `docs/PRD.md` Section 8.13 FR-079 and FR-083. |

- **AC-001** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-06-03 Initial Chirality MCP Read Tools

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-018 — Purpose

> ##### Purpose
>
> Define the working procedure for producing and verifying the DEL-06-03 MCP read-tool implementation artifacts. The procedure is constrained to the read-tool slice: status read, dependency read, bounded scope scan, and scaffold preview/dry-run.
>

### CLM-019 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Current implementation/adoption evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: For propose: DEL-02-02-V3-04 selected, applicable DEL-08-01 trigger contract and DEL-06-02 catalog validation; ordinary current implementation/evidence gates for read tools; no new remote MCP/provider permission.

### CLM-020 — Implementation Location Worklist

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.
4. Verify verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.
5. Retain inputs, source/candidate identity, commands, output and limitations; update governing scope and any selected work graph only for backchecked outcomes.

Locus and checks: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

Gate: For propose: DEL-02-02-V3-04 selected, applicable DEL-08-01 trigger contract and DEL-06-02 catalog validation; ordinary current implementation/evidence gates for read tools; no new remote MCP/provider permission.

### CLM-021 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.
4. Verify verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.
5. Retain inputs, source/candidate identity, commands, output and limitations; update governing scope and any selected work graph only for backchecked outcomes.

Locus and checks: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

Gate: For propose: DEL-02-02-V3-04 selected, applicable DEL-08-01 trigger contract and DEL-06-02 catalog validation; ordinary current implementation/evidence gates for read tools; no new remote MCP/provider permission.

### CLM-022 — Verification

Required current checks: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

Named evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-023 — Records

> ##### Records
>
> - MCP tool definitions.
> - Wrapper metadata.
> - Unit/API/integration test fixtures.
> - Validation output for deterministic ordering and denial behavior.
> - Status/dependency/scope/scaffold preview test results.
> - Section 9 validation mapping, including `section9.chirality_mcp_status_dependencies` where applicable.
> - Source-state note: `docs/PRD.md` REF-006 is `MATCH` under D-APP-38; dated mismatch history remains in prior run records.
> - Implementation location map for MCP definitions, wrapper metadata, status reader, dependency reader, scope scan, and scaffold preview.
> - Upstream closure record for DEL-06-01, DEL-07-05, status lifecycle API ownership, and runtime event path ownership.
> - Runtime event contract blocker record if the Chirality runtime event path remains unavailable.
>

### CLM-024 — Pass 3 Notes

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | D-001 | Converted to TBD worklist | Implementation module locations are named as required closure evidence, with all paths kept `TBD` because accessible sources do not assign ownership. Source reread: `_CONTEXT.md` Anticipated Artifacts; decomposition row `DEL-06-03`; `Procedure.md` Prerequisites and Records. |
> | D-002 | Incorporated as closure blocker | Upstream dependency state now names DEL-06-01, DEL-07-05, status lifecycle API ownership, and runtime event path ownership as closure blockers or acceptance requirements. Source reread: `_DEPENDENCIES.md` Extracted Dependency Register and Open dependency closure items. |
> | E-001 | Converted to tracked blocker | Runtime-event wording now requires a cited event path or explicit blocker/test contract rather than treating availability as optional. Source reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/PRD.md` Section 8.13 FR-083; `_DEPENDENCIES.md` open runtime event path item. |

- **VER-001** — Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

## Governing Values and Decisions — Axiology

### CLM-025 — Guidance: DEL-06-03 Initial Chirality MCP Read Tools

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-026 — Purpose

> ##### Purpose
>
> DEL-06-03 provides the first Chirality-owned in-process MCP read tools so the runtime can expose deterministic project-state operations without opening write, edit, shell, remote MCP, plugin, or domain-operation capability. The deliverable supports OBJ-005 by keeping tool exposure behind capability policy with explicit hard-deny precedence and MCP wrappers, and OBJ-006 by reading filesystem-native project truth.
>
> Source basis: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 6-7 and 9; `docs/PLAN.md` R2; `docs/PRD.md` Sections 8.13-8.14.
>

### CLM-027 — Principles

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

Named verification: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

### CLM-028 — Considerations

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

Named verification: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

### CLM-029 — Source-State Posture

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-030 — Trade-offs

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

Named verification: Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

### CLM-031 — Scaffold Boundary Rationale

> ###### Scaffold Boundary Rationale
>
> Scaffold preview belongs in this read-tool slice only as a non-mutating planning surface. `docs/SPEC.md` Section 14.2 classifies `mcp__chirality__scaffold` as gated, while `docs/PLAN.md` R2 sequences read and preview capability before write/edit/bash expansion. The practical boundary is therefore: allow a deterministic preview of intended scaffold effects, deny or defer filesystem mutation, and move any write-capable scaffold execution to the later governed write/path-hook surface.
>

### CLM-032 — Examples

> ##### Examples
>
> Example read-tool inventory:
>
> | Tool | Expected Result Shape |
> |---|---|
> | `mcp__chirality__status_read` | Parsed `_STATUS.md` snapshot plus source path, parse warnings, and raw/normalized state fields. |
> | `mcp__chirality__deps_read` | `Dependencies.csv` validation summary when present; explicit missing/not-tracked status when absent; warnings sourced to files. |
> | `mcp__chirality__scope_scan` | Bounded package/deliverable scan summary with stable IDs and rejected out-of-root requests. |
> | `mcp__chirality__scaffold` | Preview/dry-run plan showing intended scaffold effects without applying filesystem writes. |
>
> Example wrapper metadata fields:
>
> - Tool name.
> - MCP server ID.
> - Input schema.
> - Permission class.
> - Read/write classification.
> - Concurrency policy.
> - Interruption policy.
> - Execution handler reference.
> - Result summarization behavior.
> - Redaction/event metadata.
> - Denial behavior.
>

### CLM-033 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Connect and verify accepted read operations on the live application-tool path; retain missing/malformed status and dependency fixtures. Deliver propose schema/tuple/roster/policy/plan validation, once-per-chat behavior and proposal.offered after the named UI trigger prerequisite.

### CLM-034 — Pass 3 Notes

> ##### Pass 3 Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | X-001 | Incorporated as source-state posture | PRD MATCH handling is now explicit before PRD-only policy detail can be used for closure. Source reread: `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.13; `docs/CONTRACT.md` Section 1.6. — reconciled under D-APP-38 |
> | E-002 | Incorporated | Scaffold preview rationale now explains why preview/dry-run is in scope while write-capable scaffold execution remains gated. Source reread: `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2. |

### CLM-035 — D-APP-68 In-Process Coordination Composition (2026-07-19)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-68 In-Process Coordination Composition (2026-07-19)
>
> DEL-06-03 owns co-location and composition of `delegate_agent`,
> `report_coordination_notice`, `send_agent_update`, and `ack_agent_update` on
> the in-process Chirality MCP server. The four tools share the existing
> product-owned MCP transport and permission/evidence wrapper; this
> composition duty does not make them part of the legacy read-tool slice and
> does not duplicate DEL-06-02 ownership of their descriptors, canonical
> names, catalog entries, schemas, aliases, or registry validation. Handler
> semantics and managed-child lifecycle remain with their mapped owners.
>
> Evidence: D-APP-68 chronology item 3;
> `frontend/src/lib/harness/sdk-options-builder.ts`;
> `frontend/src/lib/harness/mcp/coordination-tools.ts`.

- **AC-002** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

- **VER-002** — Verify actual registration/call reach, read-only/path constraints, malformed/missing status, absent CSV/prose-only dependency outcomes, unknown names, descriptor metadata and proposal validation/replay. Existing legacy reader tests do not prove live application-tool exposure.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-048 SOW-050 SOW-064 SOW-082 OBJ-005 OBJ-006 | CLM-010 CLM-035 | AC-001 AC-002 | VER-001 VER-002 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
