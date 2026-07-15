---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-01
package_id: PKG-09
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@eaad463c0d481f6f1654e6adb5ee718f566176e9
project_scope_refs: [SOW-026]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-01

## Purpose and Objective Traceability

This migration candidate defines `DEL-09-01` in service of project scope [SOW-026] and package objectives [OBJ-008].

- **OUT-001** — A mechanics benchmark-suite contract covering cantilevers, frames, thermal growth, imposed displacement, and stiffness transforms with original/public/permissive provenance is produced.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-01 Mechanics benchmark suite

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-001"} -->
#### Datasheet: DEL-09-01 Mechanics benchmark suite

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-09-01-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":25,"line_start":12,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-003"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-09-01 |
| Package ID | PKG-09 |
| Package | Verification, Validation, and Quality Oracles |
| Deliverable type | TEST_SUITE |
| Decomposition basis | `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7 |
| Scope items | SOW-026 |
| Objectives | OBJ-008 |
| Context envelope | M |
| Lifecycle state during setup | Draft setup evidence only; not implementation and not ISSUED |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":37,"line_start":26,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Setup value |
|---|---|
| Suite purpose | Define the evidence boundary for future mechanics benchmark cases that exercise solver and stress-recovery behavior through original/public mechanics examples. |
| Benchmark families | Cantilevers, frames, thermal growth, imposed displacement, and local-to-global stiffness transforms. |
| Solver boundary | The suite observes solver behavior; this setup pass does not implement solver logic, benchmark source files, tests, or final comparison tolerances. |
| Source posture | Benchmark sources must be original, public-domain, public-permissive, or otherwise documented for redistribution before entering public artifacts. |
| Data boundary | Protected standards examples, code text, protected tables, proprietary commercial benchmarks, and vendor/private project data are excluded. |
| Tolerance posture | Final numerical tolerances, benchmark acceptance ranges, and release thresholds remain `TBD` pending solver prototype and human authority. |
| Result posture | Benchmark outputs should preserve units, solver version, diagnostics/result-envelope fields, assumptions, provenance, and limitations once implementation is authorized. |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":43,"line_start":38,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-005"} -->
##### Conditions

This setup context authorizes only document production and local setup registers. It does not authorize edits to validation benchmark source files, implementation tests, solver modules, repo-level CI, or `ISSUED` lifecycle state.

The future mechanics benchmark suite must stay aligned with the architecture-basis constraints for module boundaries, diagnostics/result envelopes, layered validation gates, unit safety, and protected-content/provenance review. Exact fixture schema, runner command, solver numerical library, output comparison format, comparison tolerances, and CI/release thresholds remain `TBD`.

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":56,"line_start":44,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-006"} -->
##### Construction

| Construction item | Status |
|---|---|
| `validation/benchmarks/mechanics` | Anticipated future artifact; not created or edited in this setup pass. |
| Hand-calculation notes | Anticipated future artifact; formulas and numerical cases must be original/public/permissive and source-noted. |
| Cantilever cases | Required family; concrete geometry, loads, units, expected values, and tolerances are `TBD`. |
| Frame cases | Required family; concrete portal/frame cases and acceptance ranges are `TBD`. |
| Thermal growth cases | Required family; material/thermal inputs must be user/original/public-permissive and unit-aware; values are `TBD`. |
| Imposed displacement cases | Required family; boundary-condition semantics and expected reactions/displacements are `TBD`. |
| Stiffness transform cases | Required family; local/global transform cases and expected matrices/results are `TBD`. |
| Provenance index | Required before public fixture publication; exact format is `TBD`. |

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":68,"line_start":57,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-007"} -->
##### References

- `_CONTEXT.md` for deliverable identity, scope, objectives, anticipated artifacts, and architecture-basis injection.
- `_REFERENCES.md` for governing local references.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7, rows for PKG-09, DEL-09-01, SOW-026, OBJ-008, AB-00-01, AB-00-02, AB-00-06, and AB-00-08.
- `docs/_Registers/Deliverables.csv` row DEL-09-01.
- `docs/_Registers/ScopeLedger.csv` row SOW-026.
- `docs/_Registers/ContextBudgetQA.csv` row DEL-09-01.
- `docs/SPEC.md` sections 4.1, 4.2, 4.5, and 9.
- `docs/VALIDATION_STRATEGY.md` sections 1, 2, 4, and 5.
- `docs/CONTRACT.md` invariants OPS-K-IP-1, OPS-K-IP-2, OPS-K-IP-3, OPS-K-DATA-1, OPS-K-DATA-2, OPS-K-DATA-3, OPS-K-UNIT-1, OPS-K-AUTH-1, OPS-K-SOLVER-1, and OPS-K-AGENT-1..4.

<!-- sow-source-end -->

### CLM-008 — Open Setup Questions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":77,"line_start":69,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-008"} -->
##### Open Setup Questions

| Question | Needed from |
|---|---|
| Which mechanics benchmark fixtures and public/permissive sources are approved for implementation? | Validation owner / IP review owner |
| What numerical comparison tolerance policy is acceptable for each benchmark family? | Solver lead / validation owner / human project authority |
| What fixture schema, runner interface, and result-envelope fields should executable benchmarks use? | Architecture / solver / validation owners |
| Which benchmark cases gate release and which are advisory regression checks? | QA/release owner / human project authority |

<!-- sow-source-end -->

### CLM-009 — D-41 R5 T2B PDU-013 Evidence State

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":82,"line_start":78,"source_sha256":"9ce5647c01ecc4793ce21cc8491b84b37a1145bb8639e462382f07bac93de92f","target_id":"CLM-009"} -->
##### D-41 R5 T2B PDU-013 Evidence State

| Basis | Evidence | Limit |
|---|---|---|
| Fixture-local units | Explicit N-m-rad-K identifiers and dimensional checks in the mechanics benchmark crate. | Does not establish the still-TBD accepted project catalog/conversion basis. |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-010 — Specification: DEL-09-01 Mechanics benchmark suite

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":3,"line_start":1,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-010"} -->
#### Specification: DEL-09-01 Mechanics benchmark suite

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-011 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":11,"line_start":4,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-011"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-09-01-DECL-001`.

<!-- sow-source-end -->

### CLM-012 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":17,"line_start":12,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-012"} -->
##### Scope

This deliverable specifies setup evidence for a future mechanics benchmark suite covering cantilevers, frames, thermal growth, imposed displacement, and stiffness transforms.

This setup pass does not implement benchmark source files, add tests, create numerical hand-calculation cases, modify solver code, edit validation directories outside this deliverable, choose final tolerances, or introduce protected/proprietary benchmark data.

<!-- sow-source-end -->

### CLM-013 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":29,"line_start":18,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-013"} -->
##### Requirements

| Req ID | Requirement | Source basis | Verification hook |
|---|---|---|---|
| DEL-09-01-RQ-001 | The benchmark suite shall remain separate from solver implementation and shall not modify production solver behavior. | DEL-09-01 context; AB-00-02; docs/SPEC.md section 9 | Module boundary review once implementation exists. |
| DEL-09-01-RQ-002 | The suite shall cover cantilever, frame, thermal-growth, imposed-displacement, and stiffness-transform benchmark families. | DEL-09-01 context; docs/VALIDATION_STRATEGY.md section 2 | Fixture inventory review against required families. |
| DEL-09-01-RQ-003 | Benchmark sources and expected-result derivations shall be original, public-domain, public-permissive, or otherwise documented with redistribution rights. | SOW-026; docs/VALIDATION_STRATEGY.md section 5; OPS-K-IP-1..3 | Protected-content/provenance review before publication. |
| DEL-09-01-RQ-004 | Benchmark inputs and expected outputs shall be unit-aware and dimensionally checked. | OPS-K-UNIT-1; docs/SPEC.md sections 4.1 and 4.2 | Unit validation tests once fixture schema exists. |
| DEL-09-01-RQ-005 | The suite shall preserve solver diagnostics, result-envelope status, solver version, assumptions, provenance, and limitations where supported by implementation contracts. | AB-00-06; docs/SPEC.md sections 4.5 and 9 | Result-envelope comparison and diagnostic review. |
| DEL-09-01-RQ-006 | The setup artifacts shall not set final numerical tolerances, release thresholds, or benchmark pass/fail authority without human approval. | OI-005; OPS-K-AGENT-1..4 | Review confirms unresolved tolerances remain `TBD`. |
| DEL-09-01-RQ-007 | The suite shall remain mechanics verification support and shall not claim certification, code compliance, professional approval, or project-specific reliance. | OPS-K-AUTH-1; docs/VALIDATION_STRATEGY.md section 1 | Review of result labels, reports, and release notes. |

<!-- sow-source-end -->

### CLM-014 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":35,"line_start":30,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-014"} -->
##### Standards

No protected standard text, proprietary benchmark suite, commercial software example, or vendor dataset is available in this deliverable-local setup context. Any future mechanics case must record source, provenance, license/redistribution status, contributor certification, and review disposition before it is accepted as a public benchmark.

Clause-level or code-specific validation requirements are `TBD` and must not be inferred from protected standards.

<!-- sow-source-end -->

### CLM-015 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":46,"line_start":36,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-015"} -->
##### Verification

| Verification area | Minimum setup expectation |
|---|---|
| Required family coverage | The future fixture inventory explicitly maps each case to one or more required benchmark families. |
| Analytical derivation | Hand-calculation notes identify assumptions, units, equations used from public/original mechanics, and expected result fields. |
| Numerical comparison | Tolerance policy is cited when approved; until then each tolerance field remains `TBD`. |
| Unit safety | Inputs, expected values, and outputs are dimensionally checked under the accepted unit system. |
| Data boundary | Fixture provenance confirms original/public/permissive status and excludes protected standards/commercial examples. |
| Diagnostics/result envelopes | Benchmark outputs preserve warnings, diagnostics, solver version, and limitations without compliance claims. |

<!-- sow-source-end -->

### CLM-016 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":58,"line_start":47,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-016"} -->
##### Documentation

Expected future artifacts, when implementation is authorized, are:

- `validation/benchmarks/mechanics` fixture set;
- hand-calculation notes for each benchmark family;
- fixture provenance and redistribution-status index;
- benchmark runner or integration notes;
- comparison-result records suitable for regression and release-gate review.

The exact module paths, fixture schema, runner command, result export format, numerical tolerances, and CI gates are `TBD` and must not be resolved by this setup pass.

<!-- sow-source-end -->

### CLM-017 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":64,"line_start":59,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-017"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Issue | Contenders | Human ruling |
|---|---|---|---|
| None | No source conflict identified in setup evidence. | N/A | N/A |

<!-- sow-source-end -->

### CLM-018 — D-41 R5 T2B PDU-013 Evidence Disposition (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":67,"line_start":65,"source_sha256":"2174cb9e04fc690f8bd2175b9ba0b9cebb5403fae03dcc4de86c3ea93f1cc05d","target_id":"CLM-018"} -->
##### D-41 R5 T2B PDU-013 Evidence Disposition (2026-07-12)

The existing mechanics benchmarks remain explicit and dimensionally checked under `PKG09-FIXTURE-UNITS-EXPLICIT-N-M-RAD-K`. That fixture-local basis does not satisfy RQ-004 or Unit safety at the accepted-project-unit-system grain while the canonical catalog and conversion constants remain unresolved. No threshold or validation outcome is selected here.
<!-- sow-source-end -->

- **AC-001** — The contract preserves unit-aware inputs and outputs, solver diagnostics, result-envelope fields, assumptions, provenance, limitations, fixture-local unit evidence, and explicit TBD tolerances and project-unit-system decisions without claiming certification, code compliance, professional approval, or project reliance.

## Production and Verification Method — Praxeology

### CLM-019 — Procedure: DEL-09-01 Mechanics benchmark suite

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":3,"line_start":1,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-019"} -->
#### Procedure: DEL-09-01 Mechanics benchmark suite

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-020 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":11,"line_start":4,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-020"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-09-01-DECL-004`.

<!-- sow-source-end -->

### CLM-021 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":15,"line_start":12,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-021"} -->
##### Purpose

Describe how a future TASK worker should produce or use the mechanics benchmark suite once implementation is authorized, while preserving the current setup-only boundary.

<!-- sow-source-end -->

### CLM-022 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":25,"line_start":16,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-022"} -->
##### Prerequisites

- Accepted frame-stiffness and coordinate-transform interfaces from PKG-04 implementation deliverables.
- Accepted straight-element mechanics behavior for cantilever-style cases.
- Accepted support, restraint, and imposed-displacement semantics for boundary-condition cases.
- Accepted load/thermal input semantics where thermal-growth benchmarks require them.
- Accepted unit-system, diagnostics, and result-envelope contracts for benchmark inputs and outputs.
- Original, public-domain, public-permissive, or otherwise lawfully redistributable benchmark sources with provenance.
- Human-approved numerical tolerance and release-gate policy; current value is `TBD`.

<!-- sow-source-end -->

### CLM-023 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":37,"line_start":26,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-023"} -->
##### Steps

1. Confirm the sealed brief authorizes benchmark implementation and lists exact write targets.
2. Read the accepted solver interfaces, unit-system contract, diagnostics/result-envelope contract, and applicable validation strategy.
3. Select or create benchmark fixtures only from original, public-domain, public-permissive, or otherwise documented lawful sources.
4. For each fixture, record benchmark family, source/provenance, redistribution status, assumptions, units, model inputs, expected result fields, and derivation notes.
5. Keep protected standards examples, proprietary commercial benchmarks, vendor-private data, and copied code-derived formulas out of public fixtures.
6. Run benchmark cases through the authorized solver or headless runner without changing solver logic.
7. Compare outputs using the approved comparison/tolerance policy; if no approved policy exists, record `TBD` rather than inventing pass/fail criteria.
8. Capture solver version, result-envelope fields, warnings, diagnostics, assumptions, limitations, and comparison records.
9. Stop and escalate if fixture provenance is missing, protected content is suspected, numerical tolerances are unsupported, or output wording implies certification, code compliance, or professional approval.

<!-- sow-source-end -->

### CLM-024 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":48,"line_start":38,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-024"} -->
##### Verification

| Check | Expected evidence |
|---|---|
| Scope boundary | Benchmark work stays in authorized validation/test locations and does not modify solver logic unless separately authorized. |
| Family coverage | Fixture inventory covers cantilevers, frames, thermal growth, imposed displacement, and stiffness transforms or records an explicit `TBD`. |
| Fixture provenance | Every public fixture records source, license/redistribution status, and review disposition. |
| Unit safety | Inputs, expected values, and solver outputs pass accepted dimensional checks. |
| Tolerance authority | Comparison tolerances cite an approved source or remain `TBD`. |
| Diagnostics/reporting boundary | Results preserve warnings/assumptions/limitations and avoid certification or compliance claims. |

<!-- sow-source-end -->

### CLM-025 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":56,"line_start":49,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-025"} -->
##### Records

- Benchmark fixture inventory and provenance index.
- Hand-calculation or derivation notes for each case.
- Solver version and benchmark runner settings.
- Unit-check and result-envelope comparison records.
- Review notes for tolerance policy, fixture approval, and human rulings.

<!-- sow-source-end -->

### CLM-026 — D-41 R5 T2B PDU-013 Check

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":59,"line_start":57,"source_sha256":"cf08e38bf85b00d7c7ac20177e66d662e8e4940bda44efce80cca71722cf7373","target_id":"CLM-026"} -->
##### D-41 R5 T2B PDU-013 Check

Record fixture-local unit identifiers and canonical dimensions exactly. Do not describe those checks as project-unit-system acceptance until the upstream catalog and conversions are accepted and the cases are rerun through that basis. Keep comparison tolerances and pass/fail authority unchanged.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, required benchmark-family coverage, source and redistribution posture, unit and diagnostic visibility, setup versus implementation boundaries, retained tolerance and project-unit TBDs, and professional-authority limits.

## Governing Values and Decisions — Axiology

### CLM-027 — Guidance: DEL-09-01 Mechanics benchmark suite

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":3,"line_start":1,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-027"} -->
#### Guidance: DEL-09-01 Mechanics benchmark suite

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-028 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":11,"line_start":4,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-028"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-09-01-DECL-003`.

<!-- sow-source-end -->

### CLM-029 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":15,"line_start":12,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-029"} -->
##### Purpose

This deliverable prepares the evidence boundary for a future mechanics benchmark suite. It exists to make open mechanics verification repeatable and reviewable while preserving the data boundary between public mechanics cases and protected standards or proprietary examples.

<!-- sow-source-end -->

### CLM-030 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":23,"line_start":16,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-030"} -->
##### Principles

- Treat benchmarks as verification evidence, not as solver implementation.
- Use public/original mechanics cases with clear provenance and redistribution status.
- Keep final comparison tolerances and release thresholds as `TBD` until approved by the proper human authority.
- Make units, assumptions, expected result fields, diagnostics, and limitations explicit.
- Preserve the distinction between mechanics verification, user-rule checks, and professional approval.

<!-- sow-source-end -->

### CLM-031 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":31,"line_start":24,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-031"} -->
##### Considerations

Cantilever, frame, thermal-growth, imposed-displacement, and stiffness-transform cases exercise different solver interfaces. Future implementation should identify which solver/load/support contracts each case depends on before marking a benchmark executable.

Thermal-growth and imposed-displacement cases can look similar to code or owner-standard examples if copied from protected sources. Future workers should create original cases or use permissively licensed/public-domain mechanics references, then record source and license status before publishing fixtures.

Stiffness-transform cases should isolate local-to-global coordinate behavior and sign conventions. Concrete transform matrices, geometry, expected values, and numerical tolerances are not authorized by this setup pass.

<!-- sow-source-end -->

### CLM-032 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":40,"line_start":32,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-032"} -->
##### Trade-offs

| Trade-off | Guidance |
|---|---|
| Simple hand checks vs representative piping behavior | Start with analytically transparent cases; broaden only when provenance and expected-result derivations remain reviewable. |
| Strict tolerances vs solver maturity | Record exact and approximate expected values separately when authorized; final acceptance tolerances remain `TBD`. |
| Public benchmark usefulness vs IP risk | Prefer original/public mechanics cases even when protected examples are familiar. |
| Release gating vs exploratory regression | Distinguish required release benchmarks from advisory regression checks after human QA policy is approved. |

<!-- sow-source-end -->

### CLM-033 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":44,"line_start":41,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-033"} -->
##### Examples

Concrete benchmark geometries, material values, loads, boundary conditions, expected results, and comparison tolerances are `TBD`. Future examples must be original, public-domain, or permissively licensed and must include provenance.

<!-- sow-source-end -->

### CLM-034 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":50,"line_start":45,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-034"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified in setup evidence. | N/A | N/A | N/A | N/A | N/A |

<!-- sow-source-end -->

### CLM-035 — Open Enrichment Items

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":59,"line_start":51,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-035"} -->
##### Open Enrichment Items

| Item | Status |
|---|---|
| Approved benchmark fixture list and source basis | TBD |
| Approved numerical tolerance/comparison policy | TBD |
| Approved fixture schema and result-envelope comparison format | TBD |
| Release-gating vs advisory benchmark classification | TBD |

<!-- sow-source-end -->

### CLM-036 — D-41 R5 T2B PDU-013 Boundary

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":62,"line_start":60,"source_sha256":"60c4b5ae4d34733e8e244ef59432bd68539e4b571e19f50d89b21ef722860523","target_id":"CLM-036"} -->
##### D-41 R5 T2B PDU-013 Boundary

Fixture-local dimensional rigor is useful evidence, but it must not be promoted into a claim about an accepted project-wide unit catalog. The remaining catalog/conversion decision is upstream and is recorded as held rather than filled with new constants.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-026 OBJ-008 | CLM-010 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
