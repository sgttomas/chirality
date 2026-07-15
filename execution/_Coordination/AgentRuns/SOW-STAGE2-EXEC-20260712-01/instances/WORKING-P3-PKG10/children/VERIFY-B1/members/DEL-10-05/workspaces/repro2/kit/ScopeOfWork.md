---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-05
package_id: PKG-10
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@4d153302c3c4cd42578936db160c2bac1270225a
project_scope_refs: [SOW-054, SOW-032]
package_objective_refs: [OBJ-008, OBJ-009, OBJ-012]
---

# Scope of Work — DEL-10-05

## Purpose and Objective Traceability

This migration candidate defines `DEL-10-05` in service of project scope [SOW-054, SOW-032] and package objectives [OBJ-008, OBJ-009, OBJ-012].

- **OUT-001** — A headless CLI and structured-I/O analysis-runner contract for governed solve, input validation, result export, benchmark, and regression workflows is produced.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"08c6f372eb2af28bad26b6a8225c71680de281e1d53b7ccb412aaf4312c4495e","target_id":"CLM-001"} -->
#### Datasheet: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":13,"line_start":3,"source_sha256":"08c6f372eb2af28bad26b6a8225c71680de281e1d53b7ccb412aaf4312c4495e","target_id":"CLM-002"} -->
##### Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-10-05 | `_CONTEXT.md` |
| Package ID | PKG-10 | `_CONTEXT.md` |
| Package | Build, Packaging, API, and Interoperability | `_CONTEXT.md` |
| Type | BACKEND_FEATURE_SLICE | `_CONTEXT.md`; `docs/TYPES.md` section 3 |
| Lifecycle target for setup | SEMANTIC_READY | `skills/semantic-matrix-build/SKILL.md` |
| Current production posture | Stable local `openpipestress-runner` CLI policy implemented for the bounded DEC-065 solve/validate/stub surface; release packaging and public transport remain outside this deliverable record | `DEC-065`; TP-RUNNER-015 |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":24,"line_start":14,"source_sha256":"08c6f372eb2af28bad26b6a8225c71680de281e1d53b7ccb412aaf4312c4495e","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary purpose | Headless or structured I/O solve execution for early solver verification, regression, and automation before full GUI maturity | `docs/_Registers/ScopeLedger.csv` row SOW-054; `docs/_Registers/Deliverables.csv` row DEL-10-05 |
| Required alignment | Schema-first command/query/job envelopes and result exports | `docs/_Registers/Deliverables.csv` row DEL-10-05; `execution/_Decomposition/SOFTWARE_DECOMP.md` section 8.1 AB-00-03 |
| Reproducibility basis | Deterministic, unit-safe model data flow; canonical JSON and JCS-compatible hashing where JSON payload hashes are used | `_CONTEXT.md` Architecture Basis Injection; `execution/_Decomposition/SOFTWARE_DECOMP.md` section 8.2 |
| Diagnostics basis | Result envelopes and diagnostics carry machine-readable warning/error information and must not claim certification or code compliance | `execution/_Decomposition/SOFTWARE_DECOMP.md` section 8.1 AB-00-06; `docs/CONTRACT.md` invariant OPS-K-AUTH-1 |
| Build/automation relationship | Must remain compatible with reproducible build, packaging, and CI/CD workflows; exact CI provider and release matrix are TBD | `docs/_Registers/ScopeLedger.csv` row SOW-032; `execution/_Decomposition/SOFTWARE_DECOMP.md` section 8.2 |
| Public/private boundary | No protected standards data, proprietary catalog values, private rule packs, or private project data are public defaults | `INIT.md`; `docs/DIRECTIVE.md` sections 3-4; `docs/CONTRACT.md` OPS-K-IP-1 and OPS-K-PRIV-1 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":36,"line_start":25,"source_sha256":"08c6f372eb2af28bad26b6a8225c71680de281e1d53b7ccb412aaf4312c4495e","target_id":"CLM-004"} -->
##### Conditions

| Condition | Status |
|---|---|
| Exact CLI command names | Settled for the local runner surface: `openpipestress-runner` with verbs `solve`, `validate-input`, `export-results`, `run-benchmark`, and `run-regression` |
| Exact structured input schema fields | Settled for the TP-RUNNER-015 local CLI input wrapper: `request`, optional `solve.preview_model`, and optional `rule_check_aggregate`; future persisted-project input remains separate |
| Public API transport | TBD per SCA-001 remaining-TBD boundary |
| External import/export format list | TBD; schema-first JSON envelopes are the baseline |
| CI provider and coverage thresholds | TBD; release gates remain future implementation detail |
| Process/network/filesystem policy | Settled by `DEC-065`: single foreground local process; no network, daemon, telemetry, hidden filesystem mutation, repository-default private-data write, user-home scanning, or direct SQL/SQLite bypass; stdout JSON default with explicit `--output` path allowed |
| Protected-data status | No protected standards text, tables, examples, material allowables, SIF/flexibility tables, proprietary values, or certification claims introduced here |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":54,"line_start":37,"source_sha256":"08c6f372eb2af28bad26b6a8225c71680de281e1d53b7ccb412aaf4312c4495e","target_id":"CLM-005"} -->
##### Construction

The current bounded implementation defines the stable local CLI runner surface,
not a release package or public transport. The implemented `solve` path accepts
schema-first JSON input, runs the invented preview-model payload through the
validated in-memory kernel bridge, and emits structured JSON on stdout. The
`validate-input` path validates runner metadata. The `export-results`,
`run-benchmark`, and `run-regression` verbs are stable command vocabulary and
currently return structured blocking diagnostics until downstream payload
bindings are supplied by later bounded tranches.

The runner must not bypass unit validation, provenance validation,
result-envelope diagnostics, rule-pack sandbox boundaries, private-data
controls, report controls, or human professional review boundaries. CI
workflow files, release packaging/signing/publication, public API transport,
external adapter formats, and lifecycle issuance remain outside this
implementation.

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":63,"line_start":55,"source_sha256":"08c6f372eb2af28bad26b6a8225c71680de281e1d53b7ccb412aaf4312c4495e","target_id":"CLM-006"} -->
##### References

- `_CONTEXT.md` for sealed deliverable identity, SOW/OBJ coverage, acceptance/risk notes, and architecture-basis injection.
- `docs/CONTRACT.md` for invariants OPS-K-IP-1/2/3, OPS-K-DATA-1/2/3, OPS-K-UNIT-1, OPS-K-RULE-1/2/3, OPS-K-PRIV-1/2, OPS-K-AUTH-1, and OPS-K-AGENT-1..4.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` sections 8, 9, 11, and 12 for architecture basis, scope ledger, open issues, and accepted decisions.
- `docs/_Registers/Deliverables.csv` row DEL-10-05.
- `docs/_Registers/ScopeLedger.csv` rows SOW-054 and SOW-032.
- `docs/SPEC.md` sections 1, 7, 8, 9, and 10 for layer boundaries, diagnostics/reporting, V&V, and deliverable mechanics.
- `docs/TYPES.md` sections 3, 4, 6, 8, and 9 for deliverable type, analysis-status vocabulary, data boundaries, object registry, and lifecycle semantics.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":3,"line_start":1,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-007"} -->
#### Specification: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-008 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":11,"line_start":4,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-008"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-10-05-DECL-001`.

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":22,"line_start":12,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-009"} -->
##### Scope

This deliverable defines setup-stage requirements and evidence for a future headless CLI or equivalent structured I/O analysis runner. The future runner exists to support early solver verification, regression automation, and non-GUI execution paths while the full GUI matures.

`DEC-065` settles the local CLI/process policy for this deliverable. The
current bounded implementation provides the stable `openpipestress-runner`
binary with `solve`, `validate-input`, `export-results`, `run-benchmark`, and
`run-regression` verbs. It does not implement release packaging/signing,
hosted/public transport, external adapters, CI workflows, public publication,
or lifecycle issuance.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":36,"line_start":23,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-010"} -->
##### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| R-01 | The future runner must execute through schema-first command/query/job/result-envelope boundaries rather than direct solver bypasses. | `_CONTEXT.md` Architecture Basis Injection; `execution/_Decomposition/SOFTWARE_DECOMP.md` AB-00-03 | Confirm future implementation calls application-service contracts and preserves command/job separation. |
| R-02 | Structured input and output must remain unit-aware, deterministic, and reproducible. | `docs/CONTRACT.md` OPS-K-UNIT-1; `docs/_Registers/ScopeLedger.csv` SOW-054 and OBJ-012 | Confirm future fixtures include unit-bearing values and deterministic rerun expectations. |
| R-03 | Missing solve-required or rule-check-required data must surface as diagnostics, not silent defaults. | `docs/CONTRACT.md` OPS-K-DATA-2; `docs/DIRECTIVE.md` section 3 | Confirm future runner exits/results include blocking diagnostics for missing required inputs. |
| R-04 | Result output must align with schema-first result exports and diagnostic/result-envelope contracts. | `docs/_Registers/ScopeLedger.csv` SOW-046 and SOW-061; `docs/_Registers/Deliverables.csv` DEL-10-05 notes | Confirm future outputs can be consumed by regression comparison and report/result export workflows without private-data leakage. |
| R-05 | Diagnostics must preserve code/class/severity/source/object/remediation/provenance semantics and no compliance/certification claim. | `execution/_Decomposition/SOFTWARE_DECOMP.md` AB-00-06; `docs/CONTRACT.md` OPS-K-AUTH-1 | Confirm future error/warning examples include professional-boundary notices where relevant. |
| R-06 | The local runner must expose stable development/test CLI verbs while keeping CI provider, release matrix, signing/publication, and hosted/public transport outside this implementation. | `docs/_Registers/ScopeLedger.csv` SOW-032; `DEC-065`; `DEC-025`; `DEC-057`; `DEC-059` | Confirm `openpipestress-runner` verbs are stable, package scripts are not release claims, and repo-level CI/release workflow files are not introduced by this tranche. |
| R-07 | Public examples and fixtures must use original/invented or otherwise permitted data and must not embed protected standards content. | `docs/CONTRACT.md` OPS-K-IP-1 and OPS-K-RULE-1; `docs/DIRECTIVE.md` sections 3-5 | Future fixture review must check protected-content risk and provenance. |
| R-08 | The runner must not transmit private project, material, component, or rule-pack data by default. | `docs/CONTRACT.md` OPS-K-PRIV-1/2; `docs/DIRECTIVE.md` section 6 | Future runner configuration review must confirm local-first/private-data defaults. |
| R-09 | Runner results may indicate mechanics solve and user-rule-check statuses but must not use automatic code-compliance status. | `docs/TYPES.md` section 4; `docs/CONTRACT.md` OPS-K-MECH-2 and OPS-K-AUTH-1 | Future status tests must reject misleading compliance/certification wording. |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":45,"line_start":37,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-011"} -->
##### Standards

| Standard or basis | Applicability | Status |
|---|---|---|
| JSON Schema 2020-12 baseline | Governs public schema/interchange posture for future structured I/O | Accepted by SCA-001; exact schema files TBD |
| Canonical JSON/JCS-compatible hashing | Applies where JSON payload hashes are used for reproducibility | Accepted by SCA-001; physical package/container TBD |
| Command/query/job/result-envelope baseline | Governs application-service separation for GUI/headless execution | Accepted by SCA-001; concrete interface language TBD |
| Professional responsibility boundary | Prohibits software or agent claims of certification, sealing, approval, or automatic code compliance | Binding invariant |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":66,"line_start":46,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-012"} -->
##### Verification

TP-RUNNER-015 verification covers the bounded final local CLI surface:

- `openpipestress-runner solve` runs an invented preview-model payload and
  emits structured JSON with a completed runner result and deterministic result
  references.
- `openpipestress-runner validate-input` emits structured blocking diagnostics
  for invalid request metadata.
- `openpipestress-runner run-benchmark` proves the stable verb mapping while
  returning a structured blocking diagnostic until a downstream benchmark
  payload binding exists.
- Rust crate tests cover the library, compatibility preview binary, and final
  CLI binary.
- The schema contract test confirms the `DEC-065` settled/deferred decision
  vocabulary.

Future implementation verification remains for persisted-project input,
full result-export payload binding, benchmark/regression payload execution,
CI/public transport/release packaging, and external adapter integrations.

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":81,"line_start":67,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-013"} -->
##### Documentation

Required setup artifacts for this run:

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

### CLM-014 — Pass 3 Lensing Addendum

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":89,"line_start":82,"source_sha256":"d1c2a4b72abef49110fb5a9388563189029e0494ede93d81bc07b4a0a62d926e","target_id":"CLM-014"} -->
##### Pass 3 Lensing Addendum

Semantic lensing identified implementation-sensitive TBDs. `DEC-065` resolves
the local CLI command names, local process policy, network prohibition,
filesystem posture, and package-script posture for TP-RUNNER-015. Public API
transport, CI provider, release matrix, external adapter formats,
persisted-project storage roots, and release automation remain visible TBDs
that must be handled by their owning decisions or later bounded tranches.
<!-- sow-source-end -->

- **AC-001** — The contract preserves the DEC-065 local command surface, schema-first application-service routing, unit-aware deterministic I/O, blocking diagnostics, result-envelope and reproducibility evidence, invented/permitted fixtures, local-first private-data behavior, current bounded implementation evidence, and deferred persisted-project, external-adapter, CI, public-transport, and release concerns without compliance claims.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":3,"line_start":1,"source_sha256":"4550819f0b06fb6d6d8afc6d322108276e50b8775ec7e3270ec19244ffe58371","target_id":"CLM-015"} -->
#### Procedure: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-016 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":11,"line_start":4,"source_sha256":"4550819f0b06fb6d6d8afc6d322108276e50b8775ec7e3270ec19244ffe58371","target_id":"CLM-016"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-10-05-DECL-004`.

<!-- sow-source-end -->

### CLM-017 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":15,"line_start":12,"source_sha256":"4550819f0b06fb6d6d8afc6d322108276e50b8775ec7e3270ec19244ffe58371","target_id":"CLM-017"} -->
##### Purpose

Define the setup and future execution procedure for a governed headless runner deliverable without implementing the runner in this session.

<!-- sow-source-end -->

### CLM-018 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":23,"line_start":16,"source_sha256":"4550819f0b06fb6d6d8afc6d322108276e50b8775ec7e3270ec19244ffe58371","target_id":"CLM-018"} -->
##### Prerequisites

- Sealed context for DEL-10-05 with write scope limited to this deliverable folder.
- Governing references listed in `_REFERENCES.md`.
- Architecture-basis constraints injected in `_CONTEXT.md`.
- No protected standards data, proprietary values, private project data, or certification/compliance claims in the artifacts.
- Future implementation must receive a separate sealed brief before changing CLI/source files, fixtures, package manifests, CI files, or repo-level automation.

<!-- sow-source-end -->

### CLM-019 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":35,"line_start":24,"source_sha256":"4550819f0b06fb6d6d8afc6d322108276e50b8775ec7e3270ec19244ffe58371","target_id":"CLM-019"} -->
##### Steps

1. Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, decomposition and register rows for DEL-10-05, SOW-054, and SOW-032.
2. Draft the four-document kit from accessible governance, decomposition, and register sources.
3. Keep exact CLI commands, schema fields, public API transport, CI provider, release matrix, and package/container details as `TBD` unless a cited source or human ruling resolves them.
4. Generate `_SEMANTIC.md` from the deliverable-local perspective and production documents.
5. Generate `_SEMANTIC_LENSING.md` from `_SEMANTIC.md` and the four production documents.
6. Apply warranted semantic-lensing items conservatively, with source reread evidence and no new implementation particulars.
7. Generate `Dependencies.csv` and `_DEPENDENCIES.md` from local source documents and the decomposition basis.
8. Validate the four-document kit, dependency schema, semantic coverage, lens coverage, and status state.
9. Record run evidence under `_run_records/`.

<!-- sow-source-end -->

### CLM-020 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":47,"line_start":36,"source_sha256":"4550819f0b06fb6d6d8afc6d322108276e50b8775ec7e3270ec19244ffe58371","target_id":"CLM-020"} -->
##### Verification

Setup is acceptable for `SEMANTIC_READY` only when:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist.
- `_SEMANTIC.md` is populated and has no failed final-cell semantic gate.
- `_SEMANTIC_LENSING.md` includes all required lens coverage rows.
- `Dependencies.csv` validates against v3.1 schema.
- `_DEPENDENCIES.md` counts align with `Dependencies.csv`.
- `_STATUS.md` records `SEMANTIC_READY` only, not `ISSUED`.
- `git status` shows changes only inside this deliverable folder for this run.

<!-- sow-source-end -->

### CLM-021 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":62,"line_start":48,"source_sha256":"4550819f0b06fb6d6d8afc6d322108276e50b8775ec7e3270ec19244ffe58371","target_id":"CLM-021"} -->
##### Records

Required records:

- Four production documents.
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-04-30_1105_four-documents-p1-p2.md`
- `_run_records/TASK_RUN_2026-04-30_1105_semantic-matrix-build.md`
- `_run_records/TASK_RUN_2026-04-30_1105_lens-register.md`
- `_run_records/TASK_RUN_2026-04-30_1105_four-documents-p3.md`
- `_run_records/TASK_RUN_2026-04-30_1105_dependency-extract.md`
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, five stable verb families, service-boundary and unit-aware I/O behavior, blocking diagnostics and result envelopes, deterministic fixture evidence, retained downstream/deferred integrations, privacy/protected-content controls, and professional-authority limits.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":3,"line_start":1,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-022"} -->
#### Guidance: DEL-10-05 Headless CLI and structured I/O analysis runner

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-023 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":11,"line_start":4,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-023"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-10-05-DECL-003`.

<!-- sow-source-end -->

### CLM-024 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":15,"line_start":12,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-024"} -->
##### Purpose

This deliverable keeps the early automation path coherent while GUI maturity, packaging details, and result export schemas are still evolving. The headless runner is useful only if it exercises the same governed service boundaries that GUI and downstream automation will rely on.

<!-- sow-source-end -->

### CLM-025 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":24,"line_start":16,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-025"} -->
##### Principles

- Treat the runner as an application-service client, not a solver shortcut.
- Keep command/query/job separation visible so progress, cancellation, diagnostics, and result envelopes stay testable.
- Preserve unit safety and deterministic serialization across input, solve, and output.
- Prefer explicit `TBD` over invented command names, schema fields, CI provider decisions, or platform matrices.
- Keep protected standards data, private project data, private rule packs, and proprietary component/material values out of public fixtures.
- Use result statuses as software findings only; professional reliance still requires competent human review.

<!-- sow-source-end -->

### CLM-026 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":30,"line_start":25,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-026"} -->
##### Considerations

The future runner should be useful for R0/R1 verification and regression work before a complete GUI exists. That usefulness depends on stable structured I/O, reproducible runs, and machine-readable diagnostics. It does not require this setup pass to pick final commands, package scripts, or file formats.

The runner is also adjacent to several other deliverables. It must align with the command/query/job model, diagnostics/result envelopes, result export format, build/CI pipeline, unit system, persistence/hash strategy, and solver diagnostics. Those relationships are dependencies and constraints, not permission to edit those deliverables here.

<!-- sow-source-end -->

### CLM-027 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":39,"line_start":31,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-027"} -->
##### Trade-offs

| Choice | Benefit | Risk | Setup posture |
|---|---|---|---|
| Early headless path before full GUI | Enables solver verification and automation earlier | Can bypass GUI warnings if service boundaries are ignored | Require command/job/result-envelope alignment |
| Schema-first I/O | Supports tests, regression comparison, and downstream tooling | Final fields can be over-specified too early | Keep exact schema fields TBD |
| JSON/JCS-compatible reproducibility | Supports stable hashes and audit trails | Physical package/container remains unresolved | Record accepted basis and defer container details |
| CLI command surface | Familiar for CI and developer workflows | Command names may ossify before architecture is ready | Do not define final command syntax in setup |

<!-- sow-source-end -->

### CLM-028 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":43,"line_start":40,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-028"} -->
##### Examples

No executable CLI examples are provided in this setup run. Future examples must use invented/public-permissive data only and include visible diagnostics for missing data, provenance warnings, and professional-boundary notices where applicable.

<!-- sow-source-end -->

### CLM-029 — Pass 3 Semantic Lensing Notes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":51,"line_start":44,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-029"} -->
##### Pass 3 Semantic Lensing Notes

The semantic lensing register reinforced three points for downstream work:

- Exact command names and schema fields remain TBD until implementation scope or human approval resolves them.
- Future implementation must include a verification hook showing that no CLI/source, fixture, manifest, or repo-level automation file is modified outside its sealed write scope.
- Result export compatibility must be tested against the schema-first result-envelope baseline instead of an ad hoc output shape.

<!-- sow-source-end -->

### CLM-030 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":56,"line_start":52,"source_sha256":"20cfabd5772e0a874b9ff3074b1eddb400bfd404eead29b80c0e645e2f531fd5","target_id":"CLM-030"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No conflicting source statements identified during setup. | N/A | N/A | N/A | N/A | N/A |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-054 SOW-032 OBJ-008 OBJ-009 OBJ-012 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
