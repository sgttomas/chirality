---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-01
package_id: PKG-08
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@eaad463c0d481f6f1654e6adb5ee718f566176e9
project_scope_refs: [SOW-024]
package_objective_refs: [OBJ-007]
---

# Scope of Work — DEL-08-01

## Purpose and Objective Traceability

This migration candidate defines `DEL-08-01` in service of project scope [SOW-024] and package objectives [OBJ-007].

- **OUT-001** — A calculation-report generation contract covering auditable input, source, result, warning, assumption, limitation, unit, provenance, rule-pack, and reproducibility content is produced without claiming certification or professional approval.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-08-01 Calculation report generator

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"aa27b3cb459cdb88897402662c522030f979df8c263aca090869e0ff2433804a","target_id":"CLM-001"} -->
#### Datasheet: DEL-08-01 Calculation report generator

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"aa27b3cb459cdb88897402662c522030f979df8c263aca090869e0ff2433804a","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-08-01-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":25,"line_start":12,"source_sha256":"aa27b3cb459cdb88897402662c522030f979df8c263aca090869e0ff2433804a","target_id":"CLM-003"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-08-01 |
| Deliverable name | Calculation report generator |
| Package ID | PKG-08 |
| Package name | Reporting, Audit, and Reproducibility |
| Deliverable type | BACKEND_FEATURE_SLICE |
| Scope item | SOW-024 |
| Objective | OBJ-007 |
| Context envelope | L |
| Current setup status | SEMANTIC_READY setup artifacts prepared |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":37,"line_start":26,"source_sha256":"aa27b3cb459cdb88897402662c522030f979df8c263aca090869e0ff2433804a","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Source-grounded value |
|---|---|
| Production family | Calculation reports for OpenPipeStress analysis outputs. |
| Required report content | Inputs, sources, warnings, assumptions, results, rule-pack checksums, and limitations. |
| Anticipated downstream artifacts | Report renderer, report template, tests. |
| Setup-session implementation boundary | Renderer source, templates outside this deliverable, tests, schemas, and repo-level artifacts are out of write scope. |
| Architecture baseline | Rust core/application services, schema-first command/query/job/result envelopes, JSON Schema 2020-12 contracts, canonical JSON/JCS-compatible hash basis where JSON payload hashes are used. |
| Report authority boundary | Reports are decision-support artifacts and must not claim certification, sealing, approval, authentication, or automatic code compliance. |
| Protected-content boundary | Public templates/examples must not reproduce protected standards text, protected standards tables, protected figures, proprietary formulas, or protected code-derived content. |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":49,"line_start":38,"source_sha256":"aa27b3cb459cdb88897402662c522030f979df8c263aca090869e0ff2433804a","target_id":"CLM-005"} -->
##### Conditions

| Condition | Handling requirement |
|---|---|
| Missing solve-required data | Preserve as explicit diagnostics or report findings; do not hide with silent defaults. |
| Missing rule-check-required data | Preserve as explicit rule-check-blocking diagnostics or findings; do not imply a completed check. |
| User-supplied code data | Record as user-supplied or private/provenance-tagged data; do not convert it into public defaults. |
| Rule-pack references | Report only identity, version, checksum, source/provenance notices, redistribution status, and user-provided report notices; do not reproduce protected rule text. |
| Professional reliance | Include a notice that competent human review is required before project reliance. |
| Unit-bearing values | Preserve units and dimensional context in generated report sections. |
| Private project data | Keep redaction/export handling visible as a requirement and defer detailed controls to PKG-12 where needed. |

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":66,"line_start":50,"source_sha256":"aa27b3cb459cdb88897402662c522030f979df8c263aca090869e0ff2433804a","target_id":"CLM-006"} -->
##### Construction

The calculation report generator deliverable is specified here as a bounded backend feature slice, not implemented in this setup session. Its future implementation should assemble report content from schema-first project/model/result envelopes, diagnostics, provenance metadata, and rule-pack references. The report generator must preserve the diagnostic/result-envelope boundary injected by AB-00-03 and AB-00-06: report content reflects mechanics outputs, user-rule-check outputs, warnings, assumptions, and limitations without promoting software output into professional approval.

The setup artifact family prepared for this session is:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_run_records/*`
- `_STATUS.md`

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":77,"line_start":67,"source_sha256":"aa27b3cb459cdb88897402662c522030f979df8c263aca090869e0ff2433804a","target_id":"CLM-007"} -->
##### References

| Source | SourceRef | Use |
|---|---|---|
| `_CONTEXT.md` | Scope Coverage; Architecture Basis Injection | Deliverable identity, scope, objective, accepted architecture basis, and write boundary. |
| `docs/_Registers/Deliverables.csv` | Row DEL-08-01 | Registered description, anticipated artifacts, scope, objective, context envelope, and risk note. |
| `docs/_Registers/ScopeLedger.csv` | Row SOW-024 | Report content scope and protected-content warning. |
| `docs/CONTRACT.md` | OPS-K-IP-1..3, OPS-K-DATA-1..3, OPS-K-RULE-1..3, OPS-K-AUTH-1, OPS-K-REPORT-1..2, OPS-K-PRIV-1..2, OPS-K-UNIT-1, OPS-K-AGENT-1..4 | Invariant constraints for report generation. |
| `docs/SPEC.md` | Sections 1, 3, 6, 7, 8, 9, 11 | Architecture, report domain object, rule-pack metadata, warning classes, reporting/audit content, report tests, and acceptance semantics. |
| `docs/TYPES.md` | Sections 4, 6, 8, 9 | Analysis-status vocabulary, professional boundary terms, report settings/report object definitions, and lifecycle meaning. |
| `docs/DIRECTIVE.md` | Sections 2, 3, 4, 5, 6 | Founding data/professional boundaries, stop rules, and auditability principles. |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-08-01 Calculation report generator

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":3,"line_start":1,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-008"} -->
#### Specification: DEL-08-01 Calculation report generator

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-009 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":11,"line_start":4,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-009"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-08-01-DECL-001`.

<!-- sow-source-end -->

### CLM-010 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":17,"line_start":12,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-010"} -->
##### Scope

This deliverable defines the calculation report generator behavior for OpenPipeStress reporting. It covers report assembly requirements for model input summaries, load cases, results, warnings, assumptions, source/provenance notes, rule-pack references, checksums, and limitations.

This setup session does not implement renderer source, report templates outside this deliverable, tests, schemas, or repo-level artifacts. Those remain future implementation work under sealed deliverable scope and review.

<!-- sow-source-end -->

### CLM-011 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":32,"line_start":18,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-011"} -->
##### Requirements

| ID | Requirement | SourceRef | Verification |
|---|---|---|---|
| R-08-01-001 | The report generator shall assemble auditable reports that include inputs, sources, warnings, assumptions, results, rule-pack checksums, and limitations. | ScopeLedger.csv row SOW-024; CONTRACT.md OPS-K-REPORT-1; SPEC.md section 8 | Inspect generated report contract/template behavior in future implementation tests. |
| R-08-01-002 | Reports shall include software version, solver version, model hash, input manifest, unit system, provenance summary, load cases/combinations, mechanical results, warnings, assumptions, missing data, rule-pack name/version/checksum, user-supplied data notice, and professional-review notice where those inputs exist. | SPEC.md section 8 | Report fixture/golden-output tests verify presence and omission rules. |
| R-08-01-003 | Public report templates and examples shall not reproduce protected code text, protected standards tables, protected figures, proprietary formulas, protected examples, protected dimensional tables, or proprietary commercial data. | CONTRACT.md OPS-K-IP-1, OPS-K-REPORT-2; SPEC.md section 8 | Protected-content report gate and human review before public release. |
| R-08-01-004 | Reports shall not claim to certify, seal, approve, authenticate, or declare engineering code compliance for reliance. | CONTRACT.md OPS-K-AUTH-1; TYPES.md sections 4 and 8; DIRECTIVE.md sections 2 and 6 | Text review/lint gate checks prohibited claim language. |
| R-08-01-005 | Reports shall distinguish mechanics solved, user-rule checked, rule inputs incomplete, and human review required states. | TYPES.md section 4; SOFTWARE_DECOMP.md AB-00-03 and AB-00-06 | Status fields in report fixtures are checked against analysis-status vocabulary. |
| R-08-01-006 | Reports shall preserve unit context for unit-bearing inputs and results. | CONTRACT.md OPS-K-UNIT-1; SPEC.md sections 3 and 8 | Unit-aware fixture tests verify displayed and structured units. |
| R-08-01-007 | Reports shall disclose diagnostics using result-envelope-compatible warning classes including solve-blocking, rule-check-blocking, provenance, assumption, nonlinear, and IP-boundary warnings when present. | SPEC.md section 7; SOFTWARE_DECOMP.md AB-00-06 | Diagnostic fixture tests verify warning class pass-through and report rendering. |
| R-08-01-008 | Reports shall treat rule packs as user/private design-basis artifacts and expose only safe metadata such as identity, version, checksum, source notice, redistribution status, required-input status, and user-provided report notices. | SPEC.md section 6; CONTRACT.md OPS-K-DATA-1, OPS-K-RULE-3 | Rule-pack report fixtures verify metadata display and protected-content exclusion. |
| R-08-01-009 | The report generator shall use schema-first command/query/job result envelopes and application-service boundaries; adapters/plugins must not bypass units, provenance, diagnostics, sandboxing, or report controls. | SOFTWARE_DECOMP.md AB-00-02, AB-00-03, AB-00-07 | Architecture review verifies service boundary conformance before implementation acceptance. |
| R-08-01-010 | Report reproducibility tests shall verify deterministic output for the same model/result/rule-pack inputs, versions, and report settings, subject to explicitly documented volatile fields. | SPEC.md section 9; CONTRACT.md OPS-K-REPORT-1 | Future tests compare normalized report outputs and audit manifests. |

<!-- sow-source-end -->

### CLM-012 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":36,"line_start":33,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-012"} -->
##### Standards

No protected standards text, protected tables, protected formulas, or proprietary code examples are used as source content for this deliverable. Any future user-private report template or rule-pack notice remains user responsibility and must be handled outside public-template distribution unless redistribution rights are documented.

<!-- sow-source-end -->

### CLM-013 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":47,"line_start":37,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-013"} -->
##### Verification

The future implementation should be accepted only after these checks exist and pass:

- Four-document setup artifacts exist for this deliverable.
- `Dependencies.csv` is valid v3.1 and every ACTIVE row has evidence.
- Report fixtures cover mechanics-only, rule-inputs-incomplete, user-rule-checked, warnings-present, and protected-content-risk cases.
- Report reproducibility tests normalize volatile metadata and verify stable report payloads.
- Protected-content and prohibited-claim gates scan public report templates/examples.
- Human review confirms that the report generator does not assert compliance, certification, sealing, or project acceptance.

<!-- sow-source-end -->

### CLM-014 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":59,"line_start":48,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-014"} -->
##### Documentation

Required setup documentation for this deliverable:

- `Datasheet.md` records identity, boundaries, conditions, and reference basis.
- `Specification.md` records requirements and verification targets.
- `Guidance.md` records rationale, principles, trade-offs, and open questions.
- `Procedure.md` records execution and future implementation workflow.
- `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` record semantic setup evidence only.
- `Dependencies.csv` and `_DEPENDENCIES.md` record information-flow dependencies.
- `_run_records/*` record setup sequence evidence.

<!-- sow-source-end -->

### CLM-015 — Acceptance Criteria For This Setup Session

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":66,"line_start":60,"source_sha256":"31dede492911fcb730a06e7f83cd75a03a7aac61c2478d2cd77299b1774ae58e","target_id":"CLM-015"} -->
##### Acceptance Criteria For This Setup Session

- No file outside `execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-01_Calculation report generator/` is edited.
- No renderer source, external report template, test, schema, or repo-level artifact is modified.
- Setup artifacts are source-grounded to local governance, decomposition, register, and context files.
- No protected standards content or certification/compliance claim is introduced.
- `_STATUS.md` reports `SEMANTIC_READY` only after the four-document kit, semantic artifacts, dependency register, and validation checks are complete.
<!-- sow-source-end -->

- **AC-001** — The contract preserves report content and status boundaries, explicit missing-data and diagnostic findings, units and provenance, safe rule-pack metadata, protected-content limits, reproducibility requirements, and competent-human-review notices without inventing unresolved renderer or schema choices.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-08-01 Calculation report generator

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":3,"line_start":1,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-016"} -->
#### Procedure: DEL-08-01 Calculation report generator

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-017 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":11,"line_start":4,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-017"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-08-01-DECL-004`.

<!-- sow-source-end -->

### CLM-018 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":15,"line_start":12,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-018"} -->
##### Purpose

This procedure records the setup and future implementation workflow for the calculation report generator deliverable. It does not implement renderer code.

<!-- sow-source-end -->

### CLM-019 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":25,"line_start":16,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-019"} -->
##### Prerequisites

| Prerequisite | Status |
|---|---|
| Sealed deliverable scope for DEL-08-01 | Present in `_CONTEXT.md` and user brief. |
| Scope item and objective mapping | Present: SOW-024 and OBJ-007. |
| Applicable invariants | Present in `docs/CONTRACT.md` and user brief. |
| Architecture basis injection | Present in `_CONTEXT.md` with AB-00-01, AB-00-02, AB-00-03, AB-00-04, AB-00-06, AB-00-07, AB-00-08. |
| Renderer/template/test/schema implementation authority | Not present in this setup session; future sealed brief required. |

<!-- sow-source-end -->

### CLM-020 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":27,"line_start":26,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-020"} -->
##### Steps

<!-- sow-source-end -->

### CLM-021 — Setup sequence completed in this session

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":37,"line_start":28,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-021"} -->
###### Setup sequence completed in this session

1. Run `four-documents` with `RUN_PASSES=P1_P2`.
2. Run `semantic-matrix-build`.
3. Run `lens-register`.
4. Run `four-documents` with `RUN_PASSES=P3_ONLY`.
5. Run `dependency-extract`.
6. Validate the resulting setup files and dependency schema.
7. Set `_STATUS.md` to `SEMANTIC_READY` only after the setup gates pass.

<!-- sow-source-end -->

### CLM-022 — Future implementation sequence

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":48,"line_start":38,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-022"} -->
###### Future implementation sequence

1. Confirm a sealed implementation brief for DEL-08-01 or a split deliverable if scope expands.
2. Read the current report/result/rule-pack schemas and application-service result envelopes.
3. Define report input contract without bypassing units, provenance, diagnostics, or private-data controls.
4. Implement report assembly with safe placeholders and metadata-only rule-pack references.
5. Add report fixtures for mechanics-only, user-rule-check, incomplete-rule-input, warning-heavy, and protected-content-risk cases.
6. Add reproducibility tests for deterministic report output and manifest/hash binding.
7. Add protected-content and prohibited-claim gates for public templates/examples.
8. Route to REVIEW with explicit evidence: fixtures, tests, lint output, dependency register, and limitations.

<!-- sow-source-end -->

### CLM-023 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":60,"line_start":49,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-023"} -->
##### Verification

Setup verification for this session:

- `tools/validation/check_four_documents.sh <deliverable>` passes.
- `tools/validation/check_min_viable_fileset.sh <deliverable>` passes.
- `python3 tools/validation/validate_dependencies_schema.py <deliverable>/Dependencies.csv` passes.
- Dependency enum validation passes for all enum fields in ACTIVE rows.
- `_SEMANTIC.md` final result tables contain no algebra/operator leaks and no final cell over 80 characters.
- `_SEMANTIC_LENSING.md` includes complete lens coverage for matrices A, B, C, F, D, X, and E.
- `rg` checks do not identify prohibited certification or protected-standards claims in DEL-08-01 artifacts.

<!-- sow-source-end -->

### CLM-024 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":71,"line_start":61,"source_sha256":"3bdd745621607c1bc81252cc403add123737d3372d0fbd407d7fa1d7a226ac28","target_id":"CLM-024"} -->
##### Records

Required records for this setup session:

- `_run_records/TASK_RUN_2026-04-30_1200_four-documents-p1-p2.md`
- `_run_records/TASK_RUN_2026-04-30_1205_semantic-matrix-build.md`
- `_run_records/TASK_RUN_2026-04-30_1210_lens-register.md`
- `_run_records/TASK_RUN_2026-04-30_1215_four-documents-p3.md`
- `_run_records/TASK_RUN_2026-04-30_1220_dependency-extract.md`

Future implementation records should include source slices used, tests run, report fixture outputs, protected-content scans, reproducibility checks, and open issues.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, report-content completeness, mechanics and rule-check state separation, unit/provenance visibility, protected-content and professional-authority boundaries, deterministic-output requirements, and every retained TBD or governed residual.

## Governing Values and Decisions — Axiology

### CLM-025 — Guidance: DEL-08-01 Calculation report generator

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":3,"line_start":1,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-025"} -->
#### Guidance: DEL-08-01 Calculation report generator

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-026 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":11,"line_start":4,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-026"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-08-01-DECL-003`.

<!-- sow-source-end -->

### CLM-027 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":15,"line_start":12,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-027"} -->
##### Purpose

The calculation report generator exists to make analysis outputs reviewable and reproducible without converting software output into professional approval. It should help a competent reviewer see what was analyzed, what data was supplied, what assumptions or gaps remain, what warnings were raised, what rule-pack metadata was used, and what limitations apply.

<!-- sow-source-end -->

### CLM-028 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":27,"line_start":16,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-028"} -->
##### Principles

| Principle | Guidance |
|---|---|
| Auditability first | Report content should be traceable to model inputs, result envelopes, diagnostics, provenance records, report settings, and rule-pack references. |
| Boundary clarity | The report should separate mechanics solve output, user-rule-check output, incomplete inputs, and human review. |
| No protected content | Public report templates and examples should contain placeholders, invented values, or safe metadata, not protected code text/tables/formulas. |
| No professional overclaim | Report language should say what the software computed and what data was supplied, not that the work is certified, sealed, approved, or code-compliant for reliance. |
| Unit visibility | Unit-bearing values should display units and keep dimensional context visible. |
| Reproducibility | Reports should bind to versions, hashes, manifests, warnings, and rule-pack checksums so reviewers can reproduce or compare results. |
| Local-first privacy | Private project/rule/material/component data should remain user-controlled unless intentionally exported with documented rights. |

<!-- sow-source-end -->

### CLM-029 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":35,"line_start":28,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-029"} -->
##### Considerations

The report generator will depend on upstream model/result/rule-pack envelopes that are not implemented in this setup session. Where the current source set does not provide exact field names, template structure, renderer API, or output format, those details remain `TBD` for future sealed implementation briefs.

The report generator should be conservative about rule-pack content. A report can identify a rule pack, version, checksum, required-input state, source notice, redistribution status, and user-provided notice. It should not copy protected rule text or proprietary formulas into public templates/examples.

The report generator should expose warnings as findings, not as decoration. Missing solve-required values, rule-check-required values, weak provenance, assumptions, nonlinear uncertainty, and IP-boundary concerns should be report-visible when present in the input envelopes.

<!-- sow-source-end -->

### CLM-030 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":44,"line_start":36,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-030"} -->
##### Trade-offs

| Topic | Conservative direction |
|---|---|
| Human-readable PDF/HTML vs structured output | This deliverable can define report assembly behavior, but result export format is a separate DEL-08-04 concern. Avoid binding a public transport/output format here beyond setup requirements. |
| Rich template language vs protected-content control | Prefer constrained placeholders and safe metadata over a template model that encourages copying protected code text into public examples. |
| User-private templates vs public templates | User-private templates may contain user-owned content under user responsibility; public templates must stay protected-content-free. |
| Completion language vs professional boundary | Use "generated", "computed", "reported", "checked by user rule pack" and "human review required"; avoid compliance/certification language. |

<!-- sow-source-end -->

### CLM-031 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":60,"line_start":45,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-031"} -->
##### Examples

Safe report section labels may include:

- Model input summary
- Source and provenance summary
- Load case and combination summary
- Result summary
- Warnings and missing data
- Assumptions and limitations
- Rule-pack references and checksums
- Reproducibility manifest
- Professional review notice

These labels are illustrative only and do not define a renderer template in this setup session.

<!-- sow-source-end -->

### CLM-032 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":68,"line_start":61,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-032"} -->
##### Conflict Table (for human ruling)

No source conflicts were identified in the local reference set for this setup run.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | None identified | N/A | N/A | N/A | N/A | N/A |

<!-- sow-source-end -->

### CLM-033 — Open Questions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":76,"line_start":69,"source_sha256":"99da03c474cf2784c37b810ca4c84f6ce2e9c6b9f83e9a1a3674993b67b6fc80","target_id":"CLM-033"} -->
##### Open Questions

| ID | Question | Current disposition |
|---|---|---|
| OQ-08-01-001 | Exact renderer library, file format, and report template language. | TBD; outside setup-session write scope. |
| OQ-08-01-002 | Exact report schema fields and result-envelope field names. | TBD; downstream schema/service deliverables must define before implementation. |
| OQ-08-01-003 | Redaction/export configuration for private project data in shared reports. | TBD; coordinate with PKG-12 in future sealed work. |
| OQ-08-01-004 | Human approval workflow and acceptance-record binding to report hashes. | TBD; outside software authority unless human governance defines a record process. |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-024 OBJ-007 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
