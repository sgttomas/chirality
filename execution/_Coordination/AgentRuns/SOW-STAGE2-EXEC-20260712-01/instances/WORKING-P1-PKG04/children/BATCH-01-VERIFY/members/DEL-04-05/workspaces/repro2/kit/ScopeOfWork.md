---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-05
package_id: PKG-04
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713
project_scope_refs: [SOW-035]
package_objective_refs: [OBJ-003, OBJ-008]
---

# Scope of Work — DEL-04-05

## Purpose and Objective Traceability

This migration candidate defines `DEL-04-05` in service of project scope [SOW-035] and package objectives [OBJ-003, OBJ-008].

- **OUT-001** — A sparse-solver performance and regression harness contract covering deterministic practical-model runs, reproducibility, performance and conditioning observations, lawful fixture provenance, solver/version/hash settings, diagnostics, limitations, and reviewable records is produced for the declared scope and objectives.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-05 Sparse solver performance harness

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-001"} -->
#### Datasheet: DEL-04-05 Sparse solver performance harness

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-04-05-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":25,"line_start":12,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-003"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-04-05 |
| Package ID | PKG-04 |
| Package | Solver Core and Numerical Methods |
| Deliverable type | TEST_SUITE |
| Decomposition basis | `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7 |
| Scope items | SOW-035 |
| Objectives | OBJ-003, OBJ-008 |
| Context envelope | M |
| Lifecycle state during setup | Draft setup evidence only; not implementation and not ISSUED |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":36,"line_start":26,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Setup value |
|---|---|
| Harness purpose | Define a deterministic performance/regression harness for sparse solver behavior on practical piping-model sizes and numerical-conditioning cases. |
| Solver boundary | The harness observes solver behavior; it does not implement solver logic, select a numerical library, or change sparse solve algorithms. |
| Determinism posture | Repeated runs for the same model, units, solver version, and settings must be reproducible enough for regression comparison; exact tolerances remain `TBD`. |
| Performance target posture | Specific runtime, memory, scale, and conditioning thresholds are `TBD` pending solver prototype and human approval. |
| Data posture | Fixtures must use original, invented, public-permissive, or otherwise lawful inputs; no proprietary benchmark data or protected standards examples are introduced. |
| Reporting posture | Results and diagnostics must preserve warnings, assumptions, provenance, solver version, and limitations without claiming certification or code compliance. |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":42,"line_start":37,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-005"} -->
##### Conditions

The setup context authorizes only documentation of the future harness shape. It does not authorize benchmark implementation, threshold selection, dependency-version selection, or use of proprietary model data.

The harness must remain compatible with the architecture-basis constraints for module boundaries, result/diagnostic envelopes, layered tests, and protected-content review. Numerical library choice, sparse-solver settings, conditioning metrics, practical model-size bands, timing methodology, hardware normalization, and CI gating thresholds remain `TBD`.

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":52,"line_start":43,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-006"} -->
##### Construction

| Construction item | Status |
|---|---|
| Performance tests | Anticipated; no tests are implemented in this setup pass. |
| Benchmark harness | Anticipated; module path, command shape, fixture format, and runner integration are `TBD`. |
| Conditioning cases | Required conceptually by SOW-035; concrete matrices/models and acceptable ranges are `TBD`. |
| Regression records | Required conceptually for OBJ-008; retention format and comparison policy are `TBD`. |
| Diagnostics/result-envelope hooks | Required by AB-00-06; exact codes/classes for harness failures are `TBD`. |

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":62,"line_start":53,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-007"} -->
##### References

- `_CONTEXT.md` for deliverable identity, scope, objectives, anticipated artifacts, and architecture-basis injection.
- `_REFERENCES.md` for governing local references.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7, rows for PKG-04, DEL-04-05, SOW-035, OBJ-003, OBJ-008, AB-00-01, AB-00-02, AB-00-06, and AB-00-08.
- `docs/_Registers/Deliverables.csv` row DEL-04-05.
- `docs/_Registers/ScopeLedger.csv` row SOW-035.
- `docs/_Registers/ContextBudgetQA.csv` row DEL-04-05.
- `docs/CONTRACT.md` invariants OPS-K-SOLVER-1, OPS-K-UNIT-1, OPS-K-MECH-1, OPS-K-REPORT-1, OPS-K-AGENT-1..4, and OPS-K-IP-1.

<!-- sow-source-end -->

### CLM-008 — Open Setup Questions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":70,"line_start":63,"source_sha256":"95d1bd9b00ea5dbacb3d2e8e6d79c90edd679866718603550b6073d815305c5a","target_id":"CLM-008"} -->
##### Open Setup Questions

| Question | Needed from |
|---|---|
| Which sparse numerical library and solver settings are approved for implementation? | Solver lead / architecture decision |
| What practical model-size bands and conditioning metrics are meaningful for release gates? | Solver lead / validation owner |
| What deterministic timing methodology is acceptable across local and CI environments? | QA/release owner |
| Which invented or public-permissive fixtures may represent practical piping models without protected data? | Validation/IP review owner |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-009 — Specification: DEL-04-05 Sparse solver performance harness

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":3,"line_start":1,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-009"} -->
#### Specification: DEL-04-05 Sparse solver performance harness

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-010 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":11,"line_start":4,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-010"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-04-05-DECL-001`.

<!-- sow-source-end -->

### CLM-011 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":17,"line_start":12,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-011"} -->
##### Scope

This deliverable specifies setup evidence for a future test-suite harness that will exercise sparse solver performance, reproducibility, and numerical-conditioning behavior for practical piping-model sizes.

This setup pass does not implement a benchmark runner, add tests, choose thresholds, edit solver code, select a numerical library, or introduce proprietary/protected benchmark data.

<!-- sow-source-end -->

### CLM-012 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":29,"line_start":18,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-012"} -->
##### Requirements

| Req ID | Requirement | Source basis | Verification hook |
|---|---|---|---|
| DEL-04-05-RQ-001 | The harness shall be separate from solver logic and shall not modify production solver behavior. | DEL-04-05 context; PKG-04 note; AB-00-02 | Module boundary review once implementation exists. |
| DEL-04-05-RQ-002 | Harness cases shall support deterministic regression comparison for the same model, unit system, solver version, and settings. | SOW-035; docs/SPEC.md section 4.5; OPS-K-SOLVER-1 | Repeat-run tests with accepted tolerance policy; exact tolerances `TBD`. |
| DEL-04-05-RQ-003 | Performance and conditioning metrics shall be recorded without inventing release thresholds. | SOW-035; OI-005 | Review that thresholds remain `TBD` until approved. |
| DEL-04-05-RQ-004 | Fixture data shall be invented, public-permissive, or otherwise lawful and shall not contain protected standards examples, protected tables, vendor data, or proprietary commercial benchmark data. | OPS-K-IP-1; docs/DIRECTIVE.md data-boundary rules | Protected-content and provenance review. |
| DEL-04-05-RQ-005 | Harness outputs shall preserve solver version, model/hash basis where available, warning/diagnostic classes, assumptions, provenance notes, and limitations. | AB-00-06; OPS-K-REPORT-1 | Result-envelope/report-facing tests once result schema exists. |
| DEL-04-05-RQ-006 | Unit-sensitive fixture inputs and outputs shall pass the accepted unit-system/dimensional checks. | OPS-K-UNIT-1 | Unit validation tests once fixture schema exists. |
| DEL-04-05-RQ-007 | The harness shall remain mechanics-only and shall not claim professional approval, certification, or code compliance. | OPS-K-MECH-1; OPS-K-AGENT-4; OPS-K-REPORT-1 | Review of result labels, generated reports, and release notes. |

<!-- sow-source-end -->

### CLM-013 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":33,"line_start":30,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-013"} -->
##### Standards

No protected standard text, proprietary benchmark suite, or vendor dataset is available in this deliverable-local setup context. Any future benchmark basis must be recorded with provenance, redistribution status, and human/IP review disposition. Clause-level or vendor-specific requirements are `TBD`.

<!-- sow-source-end -->

### CLM-014 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":43,"line_start":34,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-014"} -->
##### Verification

| Verification area | Minimum setup expectation |
|---|---|
| Determinism | Define repeat-run evidence without setting unsupported numeric thresholds. |
| Sparse performance | Capture timing/memory/scale observations once solver implementation exists; target values remain `TBD`. |
| Conditioning | Record conditioning-related diagnostics or solver-status observations when supported by the solver/result envelope. |
| Data boundary | Confirm all fixtures are invented, public-permissive, or otherwise lawful. |
| Reporting | Confirm harness output does not imply certification, code compliance, or professional acceptance. |

<!-- sow-source-end -->

### CLM-015 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":54,"line_start":44,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-015"} -->
##### Documentation

Expected future artifacts, when implementation is authorized, are:

- performance tests;
- benchmark harness;
- benchmark fixture provenance notes;
- deterministic run records or comparable result snapshots.

The exact module paths, runner command, fixture schema, metrics, and CI gates are `TBD` and must not be resolved by this setup pass.

<!-- sow-source-end -->

### CLM-016 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":59,"line_start":55,"source_sha256":"55d845545a28d4ccb6e51a1c1996053d09ecd673d386e3f05defa6909bb1e7fb","target_id":"CLM-016"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Issue | Contenders | Human ruling |
|---|---|---|---|
| None | No source conflict identified in setup evidence. | N/A | N/A |
<!-- sow-source-end -->

- **AC-001** — The contract preserves the accepted observer-only harness boundary, deterministic regression intent, explicit units and provenance, no invented timing, memory, conditioning, model-size, or release thresholds, mechanics-only reporting, and formal-review, dimensional-validation, hosted-CI, and cross-machine policy residuals.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-04-05 Sparse solver performance harness

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"4226b3f8743f1903ca7aceb453ee6d10aba674d2d04bf9d8577f847b12f58593","target_id":"CLM-017"} -->
#### Procedure: DEL-04-05 Sparse solver performance harness

<!-- sow-source-end -->

### CLM-018 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"4226b3f8743f1903ca7aceb453ee6d10aba674d2d04bf9d8577f847b12f58593","target_id":"CLM-018"} -->
##### Purpose

Describe how a future TASK worker should produce or use the sparse-solver performance harness once implementation is authorized, while preserving the current setup-only boundary.

<!-- sow-source-end -->

### CLM-019 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":14,"line_start":7,"source_sha256":"4226b3f8743f1903ca7aceb453ee6d10aba674d2d04bf9d8577f847b12f58593","target_id":"CLM-019"} -->
##### Prerequisites

- Accepted solver/kernel interfaces from PKG-04 implementation deliverables.
- Accepted unit-system and schema contracts for model fixtures and result envelopes.
- Human-approved sparse solver/library and diagnostic policy, if implementation requires one.
- Invented, public-permissive, or otherwise lawful benchmark fixtures with provenance.
- Human-approved performance/conditioning threshold policy; current value is `TBD`.

<!-- sow-source-end -->

### CLM-020 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":26,"line_start":15,"source_sha256":"4226b3f8743f1903ca7aceb453ee6d10aba674d2d04bf9d8577f847b12f58593","target_id":"CLM-020"} -->
##### Steps

1. Confirm the sealed brief authorizes implementation and lists exact write targets.
2. Read the accepted solver interface, result-envelope schema, diagnostics contract, and unit-system contract.
3. Select or create benchmark fixtures only from invented, public-permissive, or otherwise lawful data.
4. Record fixture provenance, model/hash basis where available, unit basis, solver version, and harness settings.
5. Run repeated deterministic cases through the solver interface without changing solver logic.
6. Capture performance observations, conditioning diagnostics, warnings, assumptions, and limitations.
7. Compare repeated outputs using the approved tolerance/threshold policy; if no policy exists, record `TBD` rather than failing or passing on invented criteria.
8. Emit run records suitable for regression review and release-gate evidence.
9. Stop and escalate if protected data, proprietary benchmark content, missing engineering values, or compliance/certification wording appears.

<!-- sow-source-end -->

### CLM-021 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":36,"line_start":27,"source_sha256":"4226b3f8743f1903ca7aceb453ee6d10aba674d2d04bf9d8577f847b12f58593","target_id":"CLM-021"} -->
##### Verification

| Check | Expected evidence |
|---|---|
| Scope boundary | Harness code/tests do not modify solver logic or repo-level artifacts unless explicitly authorized. |
| Determinism | Repeat-run comparison evidence is present; tolerance policy is cited or marked `TBD`. |
| Fixture provenance | Each fixture records source/provenance and redistribution status. |
| Unit safety | Fixture inputs and outputs pass accepted dimensional checks. |
| Diagnostic/reporting boundary | Results include warnings/assumptions/limitations and avoid certification or compliance claims. |

<!-- sow-source-end -->

### CLM-022 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":44,"line_start":37,"source_sha256":"4226b3f8743f1903ca7aceb453ee6d10aba674d2d04bf9d8577f847b12f58593","target_id":"CLM-022"} -->
##### Records

- Performance/regression run records.
- Fixture provenance index.
- Solver version and settings record.
- Conditioning diagnostic summary.
- Review notes for threshold changes and human rulings.

<!-- sow-source-end -->

### CLM-023 — D-41 R5 T7 PDU-054 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":47,"line_start":45,"source_sha256":"4226b3f8743f1903ca7aceb453ee6d10aba674d2d04bf9d8577f847b12f58593","target_id":"CLM-023"} -->
##### D-41 R5 T7 PDU-054 current declaration

Earlier setup-era statements on this surface are retained as historical setup context where applicable; this section is the active current-state declaration. The sparse-solver performance harness now exists. Threshold selection, CI/release gating, platform policy, and validation remain held where recorded; existence of the harness does not establish a production-performance ruling.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, harness/solver separation, repeated-run determinism, performance and conditioning records, unit and fixture provenance, protected-content controls, diagnostics and limitations, no compliance claims, and all unresolved governed threshold and release items.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-04-05 Sparse solver performance harness

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":3,"line_start":1,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-024"} -->
#### Guidance: DEL-04-05 Sparse solver performance harness

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-025 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":11,"line_start":4,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-025"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-04-05-DECL-003`.

<!-- sow-source-end -->

### CLM-026 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":15,"line_start":12,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-026"} -->
##### Purpose

This deliverable prepares the evidence boundary for a future deterministic sparse-solver performance/regression harness. It exists to keep performance and conditioning checks observable, repeatable, and reviewable without coupling benchmark code to solver implementation choices.

<!-- sow-source-end -->

### CLM-027 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":23,"line_start":16,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-027"} -->
##### Principles

- Treat the harness as an observer and regression surface, not as solver logic.
- Prefer deterministic, schema-backed inputs and outputs so repeated runs can be compared.
- Preserve unknowns as `TBD`; do not invent runtime, memory, model-size, or conditioning thresholds.
- Use only invented, public-permissive, or otherwise lawful benchmark fixtures.
- Keep result wording mechanics-focused and avoid certification, compliance, approval, or professional-reliance claims.

<!-- sow-source-end -->

### CLM-028 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":29,"line_start":24,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-028"} -->
##### Considerations

Sparse performance measurements are sensitive to solver library, hardware, compiler settings, platform, matrix ordering, and fixture structure. Those implementation variables are not resolved here. The setup kit should therefore describe evidence expected from a future harness while leaving thresholds and tool choices open.

Conditioning cases should exercise solver diagnostic behavior without embedding protected standards examples or proprietary commercial models. If a fixture source cannot be proven redistributable, it should not enter the public harness.

<!-- sow-source-end -->

### CLM-029 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":38,"line_start":30,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-029"} -->
##### Trade-offs

| Trade-off | Guidance |
|---|---|
| Deterministic regression vs benchmark realism | Prefer reproducible invented/public fixtures first; practical realism improves only when provenance and redistribution rights are clear. |
| CI stability vs timing sensitivity | Timing gates are `TBD`; early harnesses may record metrics without failing builds on unsupported thresholds. |
| Solver abstraction vs library-specific diagnostics | Keep common harness records stable; library-specific fields should be explicit and reviewable if introduced. |
| Performance visibility vs professional claims | Publish observations and warnings, not certification, compliance, or engineering acceptance. |

<!-- sow-source-end -->

### CLM-030 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":42,"line_start":39,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-030"} -->
##### Examples

Concrete benchmark models, numerical thresholds, matrix sizes, timing budgets, and conditioning acceptance values are `TBD`. Future examples must use invented or public-permissive data with provenance.

<!-- sow-source-end -->

### CLM-031 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":48,"line_start":43,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-031"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified in setup evidence. | N/A | N/A | N/A | N/A | N/A |

<!-- sow-source-end -->

### CLM-032 — Open Enrichment Items

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":56,"line_start":49,"source_sha256":"d25bf3f65cd74987bbc8dcf68b3f7e1d7bbf06b3b0fd62e1a575ac677c16002c","target_id":"CLM-032"} -->
##### Open Enrichment Items

| Item | Status |
|---|---|
| Approved performance metrics and threshold policy | TBD |
| Approved practical model-size taxonomy | TBD |
| Approved sparse solver/library choice | TBD |
| Public/permissive fixture source list | TBD |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-035 OBJ-003 OBJ-008 | CLM-009 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
