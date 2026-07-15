---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-03
package_id: PKG-06
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@eaad463c0d481f6f1654e6adb5ee718f566176e9
project_scope_refs: [SOW-004]
package_objective_refs: [OBJ-002, OBJ-005]
---

# Scope of Work — DEL-06-03

## Purpose and Objective Traceability

This migration candidate defines `DEL-06-03` in service of project scope [SOW-004] and package objectives [OBJ-002, OBJ-005].

- **OUT-001** — A required-input-completeness contract connecting declarative rule-pack requirements to project, model, and user-supplied data, with explicit missing, unit-incompatible, unprovenanced, and rule-check-blocking findings, is produced for the declared scope and objectives.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-03 Required-input completeness checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"c9eb60a8983e2b88d00bc197ac12ff86cb2a9e700e32c6213c34b7fd662c58ef","target_id":"CLM-001"} -->
#### Datasheet: DEL-06-03 Required-input completeness checker

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"c9eb60a8983e2b88d00bc197ac12ff86cb2a9e700e32c6213c34b7fd662c58ef","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-06-03-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":25,"line_start":12,"source_sha256":"c9eb60a8983e2b88d00bc197ac12ff86cb2a9e700e32c6213c34b7fd662c58ef","target_id":"CLM-003"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-06-03 |
| Deliverable name | Required-input completeness checker |
| Package ID | PKG-06 |
| Package name | Rule Packs and User-Supplied Code Check Engine |
| Deliverable type | BACKEND_FEATURE_SLICE |
| Scope item | SOW-004 |
| Supported objectives | OBJ-002, OBJ-005 |
| Context envelope | M |
| Current production mode | Setup/document production only |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":36,"line_start":26,"source_sha256":"c9eb60a8983e2b88d00bc197ac12ff86cb2a9e700e32c6213c34b7fd662c58ef","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Source-grounded value |
|---|---|
| Primary behavior | Identify missing rule-pack-required user inputs and prevent rule-check status from advancing when those inputs are absent. |
| Protected-data boundary | The checker must not bundle protected standards text, code tables, allowables, SIF/flexibility factors, proprietary formulas, or code-specific defaults. |
| User-data boundary | Code-specific and project-specific values remain user-supplied or privately imported data with provenance. |
| Status vocabulary | The relevant analysis state is `RULE_INPUTS_INCOMPLETE`; software must not emit automatic `CODE_COMPLIANT` status. |
| Warning class | Missing rule-pack input is a `RULE_CHECK_BLOCKING` condition, distinct from solve-blocking physical data. |
| Professional boundary | Checker output is a software finding; professional acceptance remains outside solver/rule code. |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":46,"line_start":37,"source_sha256":"c9eb60a8983e2b88d00bc197ac12ff86cb2a9e700e32c6213c34b7fd662c58ef","target_id":"CLM-005"} -->
##### Conditions

| Condition | Handling |
|---|---|
| Required code/project input missing | Emit an explicit missing-input finding and block user-rule-check completion. |
| Required physical input missing | Keep classified separately as solve-blocking, not rule-check-blocking. |
| Input exists but provenance is absent or weak | Surface provenance warning; do not silently accept as reliable. |
| Rule pack requests protected bundled data | Treat as data-boundary/IP issue and escalate rather than fill a default. |
| Completeness cannot be determined | Mark as `TBD` or equivalent unresolved finding; do not infer engineering values. |

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":52,"line_start":47,"source_sha256":"c9eb60a8983e2b88d00bc197ac12ff86cb2a9e700e32c6213c34b7fd662c58ef","target_id":"CLM-006"} -->
##### Construction

The setup artifact defines the future feature boundary only. It does not create executable completeness rules, code formulas, material allowables, design-code tables, or checker implementation files.

The future implementation is expected to consume a rule-pack schema contract from DEL-06-01, analysis-status semantics from DEL-05-04, and diagnostics/result-envelope constraints from the architecture basis. Those dependencies are recorded as information-flow dependencies, not as schedule decisions.

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":67,"line_start":53,"source_sha256":"c9eb60a8983e2b88d00bc197ac12ff86cb2a9e700e32c6213c34b7fd662c58ef","target_id":"CLM-007"} -->
##### References

| Source | Used for |
|---|---|
| `INIT.md` | Bootstrap boundaries for open mechanics, user rule checks, and professional responsibility. |
| `AGENTS.md` | TASK dispatch boundary and sealed deliverable discipline. |
| `docs/CONTRACT.md` | Invariants OPS-K-DATA, OPS-K-RULE, OPS-K-IP, OPS-K-AGENT, and professional authority constraints. |
| `docs/DIRECTIVE.md` | No silent defaults, private code data, and human authority principles. |
| `docs/TYPES.md` | Analysis statuses, epistemic labels, provenance labels, and rule-pack vocabulary. |
| `docs/SPEC.md` | Rule-pack object, required inputs, evaluator constraints, warning classes, report notices, and acceptance semantics. |
| `docs/IP_AND_DATA_BOUNDARY.md` | Public/private data rules, quarantine expectations, and private rule-pack handling. |
| `docs/VALIDATION_STRATEGY.md` | Rule-pack missing-input test expectation. |
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | PKG-06 and DEL-06-03 decomposition context. |
| `docs/_Registers/Deliverables.csv` | Machine-readable deliverable row. |
| `docs/_Registers/ScopeLedger.csv` | SOW-004 scope mapping. |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-06-03 Required-input completeness checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":3,"line_start":1,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-008"} -->
#### Specification: DEL-06-03 Required-input completeness checker

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-009 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":11,"line_start":4,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-009"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-06-03-DECL-001`.

<!-- sow-source-end -->

### CLM-010 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":17,"line_start":12,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-010"} -->
##### Scope

This deliverable specifies the setup boundary for a required-input completeness checker for user-defined rule packs. The future checker must connect a rule pack's declared required inputs to project/model/user-supplied data and prevent a user-rule-check status from being reported when required rule-check data is missing.

This setup run does not implement code, schemas, executable completeness rules, code-specific formulas, allowables, or standards-derived defaults.

<!-- sow-source-end -->

### CLM-011 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":29,"line_start":18,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-011"} -->
##### Requirements

| ID | Requirement | Source basis | Verification approach |
|---|---|---|---|
| R-DEL-06-03-001 | Missing rule-check-required values must be explicit findings, never silent defaults. | `docs/CONTRACT.md` OPS-K-DATA-2; `docs/DIRECTIVE.md` no silent engineering defaults | Future unit tests for missing required inputs and explicit findings. |
| R-DEL-06-03-002 | Code-specific and project-specific values must be user-supplied or privately imported, not bundled as public defaults. | `docs/CONTRACT.md` OPS-K-DATA-1; `docs/IP_AND_DATA_BOUNDARY.md` private user data | Protected-content and default-data review of checker fixtures. |
| R-DEL-06-03-003 | Rule-pack values, materials, components, SIF/flexibility factors, allowables, and related inputs must carry provenance where relied upon. | `docs/CONTRACT.md` OPS-K-DATA-3; `docs/TYPES.md` provenance labels | Schema/provenance validation in future feature tests. |
| R-DEL-06-03-004 | Completeness must be machine-checkable from declarative rule-pack input declarations, not arbitrary executable code. | SOW-004; `docs/SPEC.md` rule-pack `required_inputs`; OPS-K-RULE-2 | Future tests bind rule-pack required-input declarations to missing-input diagnostics without executing arbitrary code. |
| R-DEL-06-03-005 | Missing rule-pack input must map to a rule-check-blocking condition distinct from solve-blocking physical input. | `docs/SPEC.md` warning classes; `docs/TYPES.md` `RULE_INPUTS_INCOMPLETE` | Status/diagnostic tests verify `RULE_CHECK_BLOCKING` classification. |
| R-DEL-06-03-006 | The checker must not assert code compliance, certification, approval, sealing, or professional reliance. | OPS-K-AUTH-1; `docs/TYPES.md` analysis-status vocabulary | Report/API text review and future status tests exclude automatic `CODE_COMPLIANT`. |
| R-DEL-06-03-007 | Suspected protected or proprietary data requests must be surfaced and escalated, not translated into public data. | OPS-K-IP-1/2/3; `docs/IP_AND_DATA_BOUNDARY.md` quarantine rule | Protected-content lint and quarantine-path tests in later implementation. |

<!-- sow-source-end -->

### CLM-012 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":33,"line_start":30,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-012"} -->
##### Standards

No standards-body formulas, allowables, tables, text, examples, or code-specific interpretations are included in this setup artifact. Any future private project use of licensed standards data must remain user-controlled and provenance-marked.

<!-- sow-source-end -->

### CLM-013 — External Inputs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":42,"line_start":34,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-013"} -->
##### External Inputs

| Input | Required from | Notes |
|---|---|---|
| Rule-pack schema required-input declarations | DEL-06-01 Rule-pack schema | Needed before executable completeness checking can be implemented. |
| Analysis status semantics | DEL-05-04 Analysis status semantics | Needed to bind missing inputs to `RULE_INPUTS_INCOMPLETE` without compliance claims. |
| Diagnostics/result envelope contract | Architecture basis AB-00-06 | Needed for `RULE_CHECK_BLOCKING` findings and remediation text. |
| User/project rule data | User-controlled private rule pack/project files | Must not be bundled into the public repository by this deliverable. |

<!-- sow-source-end -->

### CLM-014 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":52,"line_start":43,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-014"} -->
##### Verification

Future implementation verification must include:

- rule-pack missing-input tests using invented/non-code data only;
- unit-aware binding checks where the rule-pack schema declares dimensions or units;
- tests that missing code/project inputs block rule-check status but do not block the mechanics solve status by default;
- tests that no protected defaults, code-specific formulas, or material allowables are shipped;
- tests that output messages preserve the professional responsibility boundary.

<!-- sow-source-end -->

### CLM-015 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":68,"line_start":53,"source_sha256":"10dcc8e71d72db9ed622ae646f72e526321fd2fdb980fca260005da520ace3eb","target_id":"CLM-015"} -->
##### Documentation

Required setup artifacts for this deliverable are:

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

Implementation artifacts listed in the register (`rule completeness checker`, `tests`) remain future work outside this setup session's write scope.
<!-- sow-source-end -->

- **AC-001** — The contract preserves the accepted separation between solve-blocking physical inputs and rule-check-required data, explicit no-default behavior, private user-data and protected-content boundaries, and professional responsibility, while retaining the expression grammar/library decision as TBD and inventing no engineering values.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-06-03 Required-input completeness checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":3,"line_start":1,"source_sha256":"d41f66de507e029cff0c3c9c6a84238181c743650e360d61515ed6b03a703cd4","target_id":"CLM-016"} -->
#### Procedure: DEL-06-03 Required-input completeness checker

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-017 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":11,"line_start":4,"source_sha256":"d41f66de507e029cff0c3c9c6a84238181c743650e360d61515ed6b03a703cd4","target_id":"CLM-017"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-06-03-DECL-004`.

<!-- sow-source-end -->

### CLM-018 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":15,"line_start":12,"source_sha256":"d41f66de507e029cff0c3c9c6a84238181c743650e360d61515ed6b03a703cd4","target_id":"CLM-018"} -->
##### Purpose

Define the setup-time procedure and future implementation checks for the required-input completeness checker without writing implementation files or executable rules in this session.

<!-- sow-source-end -->

### CLM-019 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":25,"line_start":16,"source_sha256":"d41f66de507e029cff0c3c9c6a84238181c743650e360d61515ed6b03a703cd4","target_id":"CLM-019"} -->
##### Prerequisites

| Prerequisite | Status for setup | Notes |
|---|---|---|
| Sealed DEL-06-03 context | Available | `_CONTEXT.md` identifies SOW-004, OBJ-002, and OBJ-005. |
| Governing data/IP boundary | Available | `docs/CONTRACT.md`, `docs/DIRECTIVE.md`, and `docs/IP_AND_DATA_BOUNDARY.md`. |
| Rule-pack schema contract | Future dependency | DEL-06-01 must define required-input declarations before checker implementation. |
| Analysis status semantics | Future dependency | DEL-05-04 supplies status vocabulary such as `RULE_INPUTS_INCOMPLETE`. |
| Rule expression grammar/library | TBD | Open issue OI-006; not resolved here. |

<!-- sow-source-end -->

### CLM-020 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":35,"line_start":26,"source_sha256":"d41f66de507e029cff0c3c9c6a84238181c743650e360d61515ed6b03a703cd4","target_id":"CLM-020"} -->
##### Steps

1. Confirm the deliverable identity and scope match `DEL-06-03`, `PKG-06`, and SOW-004.
2. Preserve the protected-data boundary by excluding standards text, tables, code formulas, allowables, SIF/flexibility data, vendor proprietary data, and private rule-pack content.
3. Define required checker behavior in terms of declarative required-input metadata, missing-input findings, provenance expectations, and status gating.
4. Keep solve-required missing data separate from rule-check-required missing data.
5. Require future tests to verify that missing rule-pack inputs produce `RULE_CHECK_BLOCKING` / `RULE_INPUTS_INCOMPLETE` behavior without asserting professional compliance.
6. Record dependencies on schema/status/diagnostic contracts in `Dependencies.csv`.
7. Leave implementation code, checker modules, schemas, and tests untouched for this setup-only run.

<!-- sow-source-end -->

### CLM-021 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":46,"line_start":36,"source_sha256":"d41f66de507e029cff0c3c9c6a84238181c743650e360d61515ed6b03a703cd4","target_id":"CLM-021"} -->
##### Verification

For this setup run, verify:

- the four-document kit exists;
- `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` exist and preserve lens-not-authority language;
- `Dependencies.csv` validates against the v3.1 schema;
- `_DEPENDENCIES.md` counts match the CSV;
- `_STATUS.md` remains within the allowed setup lifecycle and reaches `SEMANTIC_READY` only after semantic and dependency artifacts exist;
- no files outside the DEL-06-03 write scope were edited.

<!-- sow-source-end -->

### CLM-022 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":49,"line_start":47,"source_sha256":"d41f66de507e029cff0c3c9c6a84238181c743650e360d61515ed6b03a703cd4","target_id":"CLM-022"} -->
##### Records

The setup records are the deliverable-local documents, dependency register, semantic artifacts, status history, and run records under `_run_records/`.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, declarative input binding, completeness and provenance classes, unit compatibility, RULE_INPUTS_INCOMPLETE and RULE_CHECK_BLOCKING behavior, schema/status dependencies, protected-content escalation, and surviving governed conflicts.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-06-03 Required-input completeness checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":3,"line_start":1,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-023"} -->
#### Guidance: DEL-06-03 Required-input completeness checker

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-024 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":11,"line_start":4,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-024"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-06-03-DECL-003`.

<!-- sow-source-end -->

### CLM-025 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":15,"line_start":12,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-025"} -->
##### Purpose

The required-input completeness checker protects the boundary between an open mechanics solve and a user-defined rule-pack check. A mechanics result may exist while a rule-check result is blocked because the user has not supplied required code-specific or project-specific data.

<!-- sow-source-end -->

### CLM-026 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":23,"line_start":16,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-026"} -->
##### Principles

1. Missing rule-check data is a finding.
2. Code-specific defaults are not invented by the public project.
3. User rule packs are user-owned or private design-basis artifacts unless explicitly contributed with redistribution rights.
4. The checker gates software status only; it does not certify code compliance or professional acceptability.
5. Provenance is part of completeness whenever reliance on the supplied value may affect engineering judgment.

<!-- sow-source-end -->

### CLM-027 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":29,"line_start":24,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-027"} -->
##### Considerations

The checker should eventually be strict about required-input declarations while staying neutral about the content of private rule packs. It can say that a required value is absent, unit-incompatible, unprovenanced, or unresolved. It must not embed standards-body tables, quote protected clauses, derive protected formulas, or silently choose engineering values.

Completeness should be machine-checkable from declarative metadata. If a future rule pack needs code-specific formulas or allowables, those belong in the user's private rule pack or another lawfully redistributable source with provenance.

<!-- sow-source-end -->

### CLM-028 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":38,"line_start":30,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-028"} -->
##### Trade-offs

| Trade-off | Guidance |
|---|---|
| Strict blocking vs. user convenience | Prefer explicit blocking for missing declared required inputs. Convenience must not create hidden defaults. |
| Provenance warning vs. missing input | Distinguish "value absent" from "value present but source weak or unknown." |
| Public examples vs. realistic code data | Use invented non-code examples in public artifacts. Do not approximate protected standards data. |
| Software finding vs. professional judgment | Report a machine finding and keep professional acceptance outside the rule engine. |

<!-- sow-source-end -->

### CLM-029 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":42,"line_start":39,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-029"} -->
##### Examples

This setup artifact intentionally includes no engineering example values. Later public tests should use invented/non-code placeholder rule packs that demonstrate missing-input behavior without resembling protected standards content.

<!-- sow-source-end -->

### CLM-030 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":47,"line_start":43,"source_sha256":"39fefc2c7b8271f90d804ccb30badec4db299b902a7451923a2fb5c30492baa7","target_id":"CLM-030"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CF-DEL-06-03-001 | Exact future expression grammar/library for rule-pack declarations is not selected. | `execution/_Decomposition/SOFTWARE_DECOMP.md` OI-006 | `docs/SPEC.md` rule-pack evaluator section | Specification External Inputs; Procedure Prerequisites | Treat grammar/library as `TBD` and do not encode executable rules in setup artifacts. | TBD |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-004 OBJ-002 OBJ-005 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
