---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-15-04
package_id: PKG-15
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@e8f59a63372f38d9e788ac39b39995558f5aba73
project_scope_refs: [SOW-075]
package_objective_refs: [OBJ-017, OBJ-018]
---

# Scope of Work — DEL-15-04

## Purpose and Objective Traceability

This migration candidate defines `DEL-15-04` in service of project scope [SOW-075] and package objectives [OBJ-017, OBJ-018].

- **OUT-001** — A schema-first flexible external-prover boundary metadata contract for descriptive references, attachments, and handoff or comparison links is produced.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-15-04 External prover boundary metadata

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"6045fdbd759adf77dfec02ee2f7b35f8f51c6e4b6d3a4ffc063e92a4cf451de7","target_id":"CLM-001"} -->
#### Datasheet: DEL-15-04 External prover boundary metadata

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"6045fdbd759adf77dfec02ee2f7b35f8f51c6e4b6d3a4ffc063e92a4cf451de7","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-15-04-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":25,"line_start":12,"source_sha256":"6045fdbd759adf77dfec02ee2f7b35f8f51c6e4b6d3a4ffc063e92a4cf451de7","target_id":"CLM-003"} -->
##### Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-15-04 | `_CONTEXT.md` |
| Name | External prover boundary metadata | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` row DEL-15-04 |
| Package ID | PKG-15 | `_CONTEXT.md` |
| Package Name | Handoff and External Prover Workflow | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` `PKG-15` |
| Type | DATA_MODEL_CHANGE | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` row DEL-15-04 |
| Scope Coverage | SOW-075 | `_CONTEXT.md`; `docs/_Registers/ScopeLedger.csv` row SOW-075 |
| Objective Support | OBJ-017; OBJ-018 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` objective mapping |
| Context Envelope | M | `_CONTEXT.md`; `docs/_Registers/ContextBudgetQA.csv` row DEL-15-04 |
| Accepted Decomposition Basis | revision 0.7 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":39,"line_start":26,"source_sha256":"6045fdbd759adf77dfec02ee2f7b35f8f51c6e4b6d3a4ffc063e92a4cf451de7","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Value | Evidence / Status |
|---|---|---|
| Metadata purpose | Support external-prover workflow metadata | `docs/_Registers/ScopeLedger.csv` row SOW-075 |
| Required metadata posture | Flexible names, tags, notes, external references, attachments, and comparison-report linkage | `execution/_Decomposition/SOFTWARE_DECOMP.md` DEL-15-04 row and SOW-075 note |
| Prohibited automatic statuses | No hard-coded approval, certification, code-compliance, formal prover lifecycle, or automatic professional acceptance status | `docs/_Registers/Deliverables.csv` row DEL-15-04; `docs/_Registers/ScopeLedger.csv` row SOW-075; `docs/TYPES.md` section 4 |
| Commercial tool result ingestion | Comprehensive commercial-tool result ingestion is out of MVP scope | `docs/_Registers/ScopeLedger.csv` row SOW-075; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-016 |
| Professional reliance boundary | Non-authoritative; software output remains decision support until competent human review | `INIT.md` Agent rule; `docs/DIRECTIVE.md` sections 1-3; `docs/CONTRACT.md` OPS-K-AUTH-1 |
| Public/private data boundary | External artifacts and examples must not introduce protected standards text, proprietary values, private project data, or commercial software examples without permission | `docs/IP_AND_DATA_BOUNDARY.md` sections 2-6; `docs/SPEC.md` report/result export boundary sections |
| Schema basis | JSON Schema 2020-12 contracts and schema-first envelopes are the accepted architecture basis | `_CONTEXT.md` Architecture Basis Injection; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-010 |
| Concrete schema file path | `schemas/external_prover_metadata.schema.json` | Materialized JSON Schema 2020-12 metadata contract matching the current builder output |
| Field names and cardinality | Materialized provider-neutral record groups: names, tags, notes, external references, attachments, handoff/package/export links, assumptions, warnings, unsupported target flags, rejected authority claims, diagnostics, provenance, and professional boundary | `schemas/external_prover_metadata.schema.json`; `core/handoff/external_prover/metadata.py` |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":49,"line_start":40,"source_sha256":"6045fdbd759adf77dfec02ee2f7b35f8f51c6e4b6d3a4ffc063e92a4cf451de7","target_id":"CLM-005"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Upstream architecture basis | AB-00-01, AB-00-02, AB-00-03, AB-00-04, AB-00-06, AB-00-07, AB-00-08 | `_CONTEXT.md` Architecture Basis Injection; `Dependencies.csv` rows DAG-002-E0723 through DAG-002-E0729 |
| Upstream professional-boundary dependency | DEL-01-04 | `Dependencies.csv` row DAG-002-E0818 |
| Upstream handoff/state dependencies | DEL-15-01, DEL-15-02, DEL-15-03, DEL-14-01 | `Dependencies.csv` rows DAG-002-E0819 through DAG-002-E0822 |
| Approved DAG mirror status | 12 ACTIVE rows, synchronized from approved DAG-006 | `_DEPENDENCIES.md`; `Dependencies.csv` |
| Boundary validation tests | `tests/test_external_prover_boundary_metadata.py` validates generated records against schema and boundary behavior | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` row DEL-15-04 |

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":59,"line_start":50,"source_sha256":"6045fdbd759adf77dfec02ee2f7b35f8f51c6e4b6d3a4ffc063e92a4cf451de7","target_id":"CLM-006"} -->
##### Construction

| Construct | Required Shape | Source / Status |
|---|---|---|
| External reference record | Must allow flexible external references and related descriptive metadata without implying approval | `execution/_Decomposition/SOFTWARE_DECOMP.md` DEL-15-04 row; SOW-075 |
| Descriptive fields | Names, tags, notes, references, and attachments are in scope as metadata categories | `execution/_Decomposition/SOFTWARE_DECOMP.md` DEL-15-04 row |
| Comparison linkage | Comparison reports may support external-prover workflows but are diagnostic/handoff support only | `docs/_Registers/ScopeLedger.csv` rows SOW-073 and SOW-075; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-015 |
| Status fields | Must not encode automatic professional/code-compliance authority; any human acceptance reference, if present, is external and hash-bound | `docs/TYPES.md` section 4; `docs/SPEC.md` sections 4.4 and analysis-status boundary |
| Protected/private data handling | Source/provenance and redistribution status are required for public data records; protected or uncertain content is quarantined/escalated | `docs/IP_AND_DATA_BOUNDARY.md` sections 4-6 |

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":69,"line_start":60,"source_sha256":"6045fdbd759adf77dfec02ee2f7b35f8f51c6e4b6d3a4ffc063e92a4cf451de7","target_id":"CLM-007"} -->
##### References

- `_CONTEXT.md` - deliverable identity, scope, objectives, architecture basis, and anticipated artifacts.
- `_REFERENCES.md` - governing source list for this folder.
- `_DEPENDENCIES.md` and `Dependencies.csv` - approved DAG-006 local mirror/evidence surface.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` - revision 0.7 package, scope, objective, decision, and issue context.
- `docs/_Registers/Deliverables.csv` - row DEL-15-04.
- `docs/_Registers/ScopeLedger.csv` - row SOW-075.
- `docs/_Registers/ContextBudgetQA.csv` - row DEL-15-04.
- `INIT.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/TYPES.md`, `docs/SPEC.md`, and `docs/IP_AND_DATA_BOUNDARY.md` - governance, authority, status, schema, and data-boundary constraints.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-15-04 External prover boundary metadata

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"50bd7cd4835c118ac6354c58413b627fc0467f3fffb51581d89852d16d71c28f","target_id":"CLM-008"} -->
#### Specification: DEL-15-04 External prover boundary metadata

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":8,"line_start":3,"source_sha256":"50bd7cd4835c118ac6354c58413b627fc0467f3fffb51581d89852d16d71c28f","target_id":"CLM-009"} -->
##### Scope

This deliverable covers the data-model boundary for external-prover workflow metadata in PKG-15. It is limited to flexible metadata and validation expectations for names, tags, notes, external references, attachments, and related handoff/comparison context.

This deliverable excludes hard-coded professional approval, certification, code-compliance, sealing, authentication, formal prover-status lifecycle, automatic professional acceptance records, and comprehensive commercial stress-software result ingestion for the MVP. Source: `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` row DEL-15-04; `docs/_Registers/ScopeLedger.csv` row SOW-075; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-015 and DEC-016.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":23,"line_start":9,"source_sha256":"50bd7cd4835c118ac6354c58413b627fc0467f3fffb51581d89852d16d71c28f","target_id":"CLM-010"} -->
##### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-15-04-R1 | The data model shall support external-prover workflow metadata. | SOW-075 in `docs/_Registers/ScopeLedger.csv`; `_CONTEXT.md` | `tests/test_external_prover_boundary_metadata.py` confirms the metadata surface exists and validates records against `schemas/external_prover_metadata.schema.json`. |
| DEL-15-04-R2 | The metadata surface shall support flexible names, tags, notes, external references, and attachments. | `execution/_Decomposition/SOFTWARE_DECOMP.md` DEL-15-04 row; SOW-075 note | Schema/review tests check that these categories are representable without requiring a fixed prover lifecycle. |
| DEL-15-04-R3 | The metadata model shall not force a formal prover-status lifecycle. | SOW-075 in `docs/_Registers/ScopeLedger.csv`; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-016 | Negative tests reject or flag hard-coded lifecycle authority when represented as automatic software status. |
| DEL-15-04-R4 | The metadata model shall not create automatic professional acceptance records. | SOW-075; `docs/TYPES.md` section 4; `docs/SPEC.md` section 4.4 | Tests verify software-generated metadata cannot assert human acceptance. |
| DEL-15-04-R5 | The metadata model shall not emit approval, certification, code-compliance, sealing, authentication, endorsement, or professional-reliance equivalents as automatic statuses. | `INIT.md` Agent rule; `docs/CONTRACT.md` OPS-K-AUTH-1; `docs/TYPES.md` section 4; `docs/SPEC.md` analysis-status boundary | Boundary validation tests cover prohibited status labels and equivalents. |
| DEL-15-04-R6 | External prover metadata shall remain diagnostic/handoff support rather than proof of external verification sufficiency. | `execution/_DAG/DAG-006/DAG-002_EdgeDispositionReview.md` DAG2-RD-010; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-015 | Review/test evidence checks wording and status semantics. |
| DEL-15-04-R7 | Any external human acceptance reference, if later represented, shall be external, human-actor-owned, and bound to reviewed payload hashes. | `docs/TYPES.md` section 4; `docs/SPEC.md` section 4.4 and analysis-status boundary | Tests require external/hash-bound representation and prevent content-change survival without re-review. |
| DEL-15-04-R8 | Public fixtures, examples, report snippets, and metadata examples shall not copy protected standards text, protected tables, proprietary formulas, proprietary engineering values, private project data, private rule-pack payloads, private library content, real secrets, or unauthorized commercial software examples. | `docs/IP_AND_DATA_BOUNDARY.md` sections 2-6; `docs/SPEC.md` report/result export boundary sections | Protected-content/private-data review or lint evidence is required for public examples. |
| DEL-15-04-R9 | Metadata records that become public data contributions shall carry source, provenance, license/redistribution status, contributor certification, and review disposition where applicable. | `docs/IP_AND_DATA_BOUNDARY.md` section 4; `docs/CONTRACT.md` OPS-K-IP-2 | Schema/review checks confirm required provenance slots or explicit `TBD`. |
| DEL-15-04-R10 | The deliverable shall align with the accepted architecture basis: schema-first contracts, JSON Schema 2020-12 where applicable, canonical hash basis where JSON payloads are hashed, and result/diagnostic envelope boundaries where relevant. | `_CONTEXT.md` Architecture Basis Injection; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-010 | Draft 2020-12 schema validation and focused tests confirm no incompatible schema/API/hash assumptions are introduced. |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":33,"line_start":24,"source_sha256":"50bd7cd4835c118ac6354c58413b627fc0467f3fffb51581d89852d16d71c28f","target_id":"CLM-011"} -->
##### Standards

| Standard / Policy | Applicability | Status |
|---|---|---|
| OpenPipeStress governance invariants | Binding project constraints for authority, data boundary, provenance, and agent behavior | Available in `docs/CONTRACT.md` |
| OpenPipeStress vocabulary/status model | Defines automatic status limitations and epistemic labels | Available in `docs/TYPES.md` |
| OpenPipeStress technical specification | Defines schema-first domain surfaces, persistence, adapter, report, result, and authority-boundary behavior | Available in `docs/SPEC.md` |
| OpenPipeStress IP/data boundary policy | Governs protected/private data and public contribution provenance | Available in `docs/IP_AND_DATA_BOUNDARY.md` |
| External engineering codes/standards | No clause-level content is available or required for this setup deliverable | `TBD`; do not quote or encode protected standards content |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":43,"line_start":34,"source_sha256":"50bd7cd4835c118ac6354c58413b627fc0467f3fffb51581d89852d16d71c28f","target_id":"CLM-012"} -->
##### Verification

| Verification Target | Required Evidence |
|---|---|
| Required metadata categories are representable | `python3 tests/test_external_prover_boundary_metadata.py` plus schema review evidence for names, tags, notes, external references, attachments, and relevant handoff/comparison links |
| Prohibited automatic statuses are blocked | Negative tests for approval, certification, code-compliance, sealing, authentication, professional approval, and formal prover lifecycle labels |
| Human acceptance remains external and hash-bound | Tests or review evidence showing software metadata cannot create professional acceptance and cannot preserve acceptance across bound-hash changes |
| Protected/private data is not introduced | Protected-content/private-data review evidence for any fixtures, examples, or sample external references |
| Dependency boundary remains aligned | Review against local `Dependencies.csv` mirror, especially DEL-01-04, DEL-15-01, DEL-15-02, DEL-15-03, and DEL-14-01 upstream context |

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":53,"line_start":44,"source_sha256":"50bd7cd4835c118ac6354c58413b627fc0467f3fffb51581d89852d16d71c28f","target_id":"CLM-013"} -->
##### Documentation

Implemented artifacts from `_CONTEXT.md` and `docs/_Registers/Deliverables.csv`:

- `schemas/external_prover_metadata.schema.json`;
- `core/handoff/external_prover/metadata.py`;
- `core/handoff/external_prover/authority_boundary.py`;
- `tests/test_external_prover_boundary_metadata.py`.

Concrete external prover tools, target-specific parsers, lifecycle promotion, human acceptance records, certification/compliance decisions, and commercial result ingestion remain out of scope.
<!-- sow-source-end -->

- **AC-001** — The contract preserves provider-neutral names, tags, notes, external references, reference-only attachments, handoff, mapping, export and immutable-state links, assumptions, warnings, unsupported-target flags, rejected authority claims, diagnostics, provenance, privacy and protected-content boundaries, external human-owned hash-bound acceptance only, and explicit exclusion of formal prover lifecycle, commercial ingestion, and automatic professional authority.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-15-04 External prover boundary metadata

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"4f39919dd5e2f44049df434476f64a3adde69a7d35f581f7ab5e3d568910e960","target_id":"CLM-014"} -->
#### Procedure: DEL-15-04 External prover boundary metadata

<!-- sow-source-end -->

### CLM-015 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"4f39919dd5e2f44049df434476f64a3adde69a7d35f581f7ab5e3d568910e960","target_id":"CLM-015"} -->
##### Purpose

Define and check the external-prover boundary metadata deliverable. The current review-readiness tranche materializes the external reference schema and boundary validation tests while preserving the professional reliance and data-boundary constraints already present in the sources.

<!-- sow-source-end -->

### CLM-016 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":18,"line_start":7,"source_sha256":"4f39919dd5e2f44049df434476f64a3adde69a7d35f581f7ab5e3d568910e960","target_id":"CLM-016"} -->
##### Prerequisites

| Prerequisite | Source / Status |
|---|---|
| Deliverable context for DEL-15-04 | `_CONTEXT.md` |
| Scope item SOW-075 and objectives OBJ-017/OBJ-018 | `docs/_Registers/ScopeLedger.csv`; `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| Applicable invariants | `docs/CONTRACT.md`, especially OPS-K-IP-1 through OPS-K-IP-3, OPS-K-DATA-1 through OPS-K-DATA-3, OPS-K-AUTH-1 through OPS-K-AUTH-2, OPS-K-UNIT-1, OPS-K-GOV-3, and OPS-K-AGENT-1 through OPS-K-AGENT-4 |
| Status vocabulary and prohibited automatic statuses | `docs/TYPES.md` section 4 |
| Data and protected-content policy | `docs/IP_AND_DATA_BOUNDARY.md` |
| Approved local dependency mirror | `_DEPENDENCIES.md`; `Dependencies.csv` |
| Implementation write scope | `schemas/external_prover_metadata.schema.json`; `core/handoff/external_prover/*.py`; `tests/test_external_prover_boundary_metadata.py`; deliverable-local docs and run records |

<!-- sow-source-end -->

### CLM-017 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":31,"line_start":19,"source_sha256":"4f39919dd5e2f44049df434476f64a3adde69a7d35f581f7ab5e3d568910e960","target_id":"CLM-017"} -->
##### Steps

1. Confirm the implementation task is explicitly scoped to DEL-15-04 and has write authority for the intended schema/tests.
2. Read `_CONTEXT.md`, `_REFERENCES.md`, `Specification.md`, and the approved local dependency mirror before drafting any schema or tests.
3. Define only descriptive external-prover metadata categories supported by the sources: names, tags, notes, external references, attachments, and diagnostic comparison/handoff links.
4. Use `schemas/external_prover_metadata.schema.json` for schema path, field names, required/optional cardinality, attachment-as-reference behavior, and external artifact checksum references; concrete commercial-tool parser behavior remains out of scope.
5. Add or update schema fields so that they cannot be interpreted as automatic professional approval, certification, sealing, authentication, code compliance, or formal prover lifecycle state.
6. If a human acceptance reference is in scope, represent it only as an external, human-owned, reviewed-payload hash-bound record. Do not create it automatically.
7. Add boundary validation tests for allowed flexible metadata.
8. Add negative boundary validation tests for prohibited authority/status terms and formal prover lifecycle behavior.
9. Add protected-content/private-data review checks for any fixtures or example metadata.
10. Record unresolved design choices as `TBD`, `ASSUMPTION`, or `PROPOSAL`; do not turn them into requirements without source support.

<!-- sow-source-end -->

### CLM-018 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":42,"line_start":32,"source_sha256":"4f39919dd5e2f44049df434476f64a3adde69a7d35f581f7ab5e3d568910e960","target_id":"CLM-018"} -->
##### Verification

| Check | Expected Result |
|---|---|
| Deliverable identity check | Files and tests reference DEL-15-04 / PKG-15 consistently. |
| Flexible metadata check | Names, tags, notes, external references, attachments, and comparison/handoff links can be represented. |
| Status-boundary check | Automatic approval, certification, code-compliance, sealing, authentication, professional reliance, and formal prover lifecycle states are absent or rejected. |
| Human acceptance check | Any human acceptance reference is external, human-owned, and hash-bound; otherwise it is `TBD` or absent. |
| Data-boundary check | Fixtures/examples contain no protected standards text, proprietary values, private project data, unauthorized commercial examples, real secrets, or private rule-pack payloads. |
| Dependency check | Upstream dependency context from `Dependencies.csv` is preserved; approved DAG-006 mirror rows are not deleted, retired, or reclassified by this setup pass. |

<!-- sow-source-end -->

### CLM-019 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":55,"line_start":43,"source_sha256":"4f39919dd5e2f44049df434476f64a3adde69a7d35f581f7ab5e3d568910e960","target_id":"CLM-019"} -->
##### Records

The following records are materialized evidence for the current implementation task:

- `schemas/external_prover_metadata.schema.json`;
- `core/handoff/external_prover/metadata.py`;
- `core/handoff/external_prover/authority_boundary.py`;
- `tests/test_external_prover_boundary_metadata.py`;
- evidence that prohibited status/authority terms are blocked;
- evidence that public fixtures/examples passed protected-content/private-data review;
- explicit `TBD` list for unresolved concrete external prover tools, target-specific parsers, lifecycle promotion, human acceptance records, certification/compliance decisions, and commercial-tool parser behavior.

This tranche does not edit lifecycle `_STATUS.md`, dependency mirrors, or human review dispositions.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, every flexible metadata category, schema and attachment-as-reference behavior, prohibited-status rejection, external human-owned hash-bound acceptance boundaries, provenance and public/private controls, comprehensive commercial-ingestion exclusion, retained TBDs, and no approval, certification, compliance, sealing, or professional-reliance claims.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-15-04 External prover boundary metadata

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"e51399507f4c48ccfddd3f3a9eff47acac577093f381a5ecb8336b33b779bd01","target_id":"CLM-020"} -->
#### Guidance: DEL-15-04 External prover boundary metadata

<!-- sow-source-end -->

### CLM-021 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":6,"line_start":3,"source_sha256":"e51399507f4c48ccfddd3f3a9eff47acac577093f381a5ecb8336b33b779bd01","target_id":"CLM-021"} -->
##### Purpose

DEL-15-04 exists to let OpenPipeStress record external-prover workflow context without converting that context into automatic professional approval. The useful metadata is descriptive and traceable: names, tags, notes, external references, attachments, and links to handoff/comparison evidence. Source: `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` row DEL-15-04; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEL-15-04 row.

<!-- sow-source-end -->

### CLM-022 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":7,"source_sha256":"e51399507f4c48ccfddd3f3a9eff47acac577093f381a5ecb8336b33b779bd01","target_id":"CLM-022"} -->
##### Principles

| Principle | Guidance | Source |
|---|---|---|
| Descriptive, not authoritative | Treat external-prover metadata as context for review and handoff, not as proof that a model is code-compliant or professionally accepted. | `docs/DIRECTIVE.md` sections 2.2 and 3; `docs/CONTRACT.md` OPS-K-AUTH-1; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-015 |
| Flexible metadata | Use the schema-backed descriptive fields for names, tags, notes, references, attachments, assumptions, warnings, unsupported target flags, and handoff/export links over fixed prover-status stages. | SOW-075; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEL-15-04 row; `schemas/external_prover_metadata.schema.json` |
| No lifecycle overclaim | Do not encode a formal prover lifecycle unless later authorized by explicit scope change. | `execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-016 |
| Human authority remains external | Human acceptance, when it exists, is outside solver authority and must be a human-owned, hash-bound project record. | `docs/TYPES.md` section 4; `docs/SPEC.md` section 4.4 |
| Preserve data boundaries | Do not embed protected standards content, commercial software examples, private project data, or proprietary values in public examples or fixtures. | `docs/IP_AND_DATA_BOUNDARY.md` sections 2-6; `docs/SPEC.md` report/result export boundary sections |
| Expose unknowns | Missing or unsupported metadata should be recorded as `TBD` or a diagnostic rather than silently defaulted. | `INIT.md` Agent rule; `docs/DIRECTIVE.md` section 2.2; `docs/CONTRACT.md` OPS-K-DATA-2 |

<!-- sow-source-end -->

### CLM-023 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":24,"line_start":18,"source_sha256":"e51399507f4c48ccfddd3f3a9eff47acac577093f381a5ecb8336b33b779bd01","target_id":"CLM-023"} -->
##### Considerations

- The current schema-backed metadata contract is `schemas/external_prover_metadata.schema.json`, with generated-output behavior in `core/handoff/external_prover/metadata.py`.
- Boundary validation tests are implemented in `tests/test_external_prover_boundary_metadata.py`, including positive flexible-metadata cases and negative prohibited-status/attachment cases.
- The approved local dependency mirror says this deliverable binds to handoff package, target mapping, export workflow, immutable state, and professional-boundary context. Those rows are evidence of dependency direction only; they do not provide the content of those predecessor deliverables.
- Comprehensive commercial-tool result ingestion is explicitly deferred for MVP; a metadata link to an external artifact is not the same as parsing, validating, or accepting that artifact.

<!-- sow-source-end -->

### CLM-024 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":33,"line_start":25,"source_sha256":"e51399507f4c48ccfddd3f3a9eff47acac577093f381a5ecb8336b33b779bd01","target_id":"CLM-024"} -->
##### Trade-offs

| Trade-off | Direction |
|---|---|
| Flexible metadata vs. standardized lifecycle | Use flexible metadata now. A standardized lifecycle would conflict with SOW-075 and DEC-016 unless later approved. |
| External references vs. external result ingestion | Store references and descriptive context; do not ingest comprehensive commercial-tool results in this MVP deliverable. |
| Review usefulness vs. authority overclaim | Include enough provenance and hash/reference context for a reviewer, but avoid language that implies software certification or code compliance. |
| Public examples vs. realistic external artifacts | Use invented or cleared examples only. Real commercial files, protected standards material, and private owner data require permission and review. |

<!-- sow-source-end -->

### CLM-025 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":47,"line_start":34,"source_sha256":"e51399507f4c48ccfddd3f3a9eff47acac577093f381a5ecb8336b33b779bd01","target_id":"CLM-025"} -->
##### Examples

The current schema supports the following provider-neutral metadata field groups. Concrete external-tool-specific payload interpretation remains out of scope.

| Supported Metadata Category | Schema-backed Shape |
|---|---|
| Name | `names` records for human-readable external workflow labels. |
| Tag | `tags` values screened for prohibited authority/status wording. |
| Note | `notes` records subject to privacy/protected-content and authority-boundary diagnostics. |
| External reference | `external_references` records with reference type, URI/path, checksum, and provenance metadata. |
| Attachment | `attachments` records that reference artifacts; embedded attachment payloads are rejected. |
| Handoff/export links | `handoff_package_refs`, `target_mapping_refs`, `export_workflow_refs`, and `immutable_model_state_refs` as non-authoritative links. |
| Review evidence | `assumptions`, `warnings`, `unsupported_target_flags`, `diagnostics`, `provenance`, and `professional_boundary` records. |

<!-- sow-source-end -->

### CLM-026 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":52,"line_start":48,"source_sha256":"e51399507f4c48ccfddd3f3a9eff47acac577093f381a5ecb8336b33b779bd01","target_id":"CLM-026"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No direct source conflict identified in accessible sources. | N/A | N/A | N/A | N/A | N/A |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-075 OBJ-017 OBJ-018 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
