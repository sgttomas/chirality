# Source Pack: SRC-DEL-DEL-03-05-RIGID-COMPONENT-MODELS-FOR-VALVES-FLANGES-REDUCERS-AND-SPECIALTY-ITEMS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-05_Rigid component models for valves, flanges, reducers, and specialty items/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-05_Rigid component models for valves, flanges, reducers, and specialty items/Datasheet.md

### Datasheet: DEL-03-05 Rigid component models for valves, flanges, reducers, and specialty items

#### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-03-05 |
| Package ID | PKG-03 |
| Package | Piping Components, Materials, and Library Data Model |
| Type | BACKEND_FEATURE_SLICE |
| Scope item | SOW-009 |
| Objective | OBJ-004 |
| Lifecycle state read for reconciliation | IN_PROGRESS (`_STATUS.md` read only; no lifecycle edit) |

#### Attributes

This deliverable describes implemented evidence for rigid and semi-rigid component library schema slots, fixture shape, and validation coverage for valves, flanges, reducers, rigid placeholders, and specialty items. The implementation evidence is `schemas/component.schema.yaml`, `fixtures/component/invented_component_library_valid.json`, `tests/test_component_section_schema.py`, and the deliverable-local memory/review records.

Implemented descriptive slots and retained gaps are:

| Slot | Source / basis | Reconciled value |
|---|---|---|
| Component families | SOW-009; `ComponentType`; fixture `contract.component.rigid-semirigid`; test enum checks | `valve`, `flange`, `reducer`, `rigid`, and `specialty` are accepted component types and are covered by the rigid/semi-rigid family contract. |
| Geometry slots | `ComponentFieldKind`; fixture field definitions; strict fixture tests | `rigid_body_length`, `end_a_size`, `end_b_size`, `connection_end_a_reference`, and `connection_end_b_reference` are schema/fixture-recognized slots. Public fixture values remain schema-shape-only. |
| Weight input | SOW-009; fixture rigid record; protected-value policy | `weight` is implemented as a required mechanics-solve field kind. Public catalog/vendor weights remain omitted; value policy remains private or public-permissive only after review. |
| Center of gravity input | SOW-009; fixture rigid record; protected-value policy | `center_of_gravity` is implemented as a required mechanics-solve field kind. Coordinate convention/reference-frame policy remains `TBD`. |
| Semi-rigid behavior | `ComponentQuantityDimension`; fixture field definitions; review finding resolution evidence | Stiffness is split into `linear_stiffness` and `rotational_stiffness`; generic `stiffness` is not used as a component quantity dimension. Exact solver treatment remains `TBD`. |
| Provenance and review metadata | OPS-K-DATA-3; OPS-K-IP-2; schema required fields | Component library metadata, records, fields, diagnostics, and fixture slots carry provenance/review status requirements. Human review disposition remains `TBD` where recorded in `Review_Findings.csv`. |
| Unit handling | OPS-K-UNIT-1; AB-00-04; schema/test evidence | Unit-bearing dimensions include length, force, linear stiffness, and rotational stiffness. Connection/reference slots keep `dimension_id: TBD` where no unit-bearing value is defined. |
| Public-data boundary | OPS-K-IP-1..3; OPS-K-DATA-1; fixture policies | Public artifacts carry schema shape and invented diagnostics only. Protected tables, vendor data, catalog dimensions, actual weights, COGs, and stiffness values remain excluded. |

The base rigid/semi-rigid field taxonomy is implemented for schema validation and strict fixture coverage. Policy-level source catalogs, public fixture-value acceptance, concrete import formats, exact solver consumption, per-family engineering profiles, dependency satisfaction, human disposition, and lifecycle closure remain `TBD`.

#### Conditions

- Public artifacts must not include proprietary component/vendor data, protected dimensional tables, copied standards content, or invented weights/COGs.
- User-entered or lawfully imported private data must carry provenance and redistribution status where it can enter a library or reusable fixture.
- Missing solve-required or model-required values must remain explicit findings or validation diagnostics, never silent defaults.
- Outputs are documentation reconciliation evidence and do not claim certification, compliance, or fitness for professional reliance.

#### Construction

Repository-level implementation evidence already exists in the component schema, invented component fixture, and component schema tests. This reconciliation run does not edit those repository-level schema, fixture, source, test, DAG, dependency, status, review CSV, or coordination files.

The implemented model evidence preserves the architecture basis stated in the sealed brief: inward dependency direction toward domain contracts, deterministic unit-aware persistence, schema-governed data, diagnostics/result envelopes where validation fails, internal/public API boundary preservation, and layered tests.

#### References

- `_CONTEXT.md` for deliverable identity, architecture-basis injection, and scope envelope.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7 rows for PKG-03, DEL-03-05, SOW-009, OBJ-004, and AB-00-01/02/04/06/07/08.
- `docs/_Registers/Deliverables.csv` row DEL-03-05.
- `docs/_Registers/ScopeLedger.csv` row SOW-009.
- `docs/_Registers/ContextBudgetQA.csv` row DEL-03-05.
- `docs/CONTRACT.md` invariants OPS-K-IP-1..3, OPS-K-DATA-1..3, OPS-K-UNIT-1, OPS-K-MECH-1, OPS-K-AGENT-1..4.

## Component: execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-05_Rigid component models for valves, flanges, reducers, and specialty items/Guidance.md

### Guidance: DEL-03-05 Rigid component models for valves, flanges, reducers, and specialty items

#### Purpose

This deliverable reconciles the implemented rigid and semi-rigid component schema evidence without importing protected component data. Its value is to keep the implementation boundary explicit: the software may structure and validate user-supplied component information, but it must not ship hidden catalog knowledge as defaults.

#### Principles

- Use schema and validation to separate implemented component shape from protected component data.
- Treat dimensions, weights, COGs, and stiffness behavior as project/library inputs with provenance.
- Prefer explicit `TBD` or diagnostics over plausible defaults.
- Keep public examples synthetic, minimal, and labeled as examples rather than engineering recommendations.
- Keep mechanics-facing data compatible with a 3D centerline/frame model while preserving local-analysis handoff options.

#### Considerations

The current component schema and strict fixture implement a base rigid/semi-rigid family contract for `valve`, `flange`, `reducer`, `rigid`, and `specialty`. The implemented base contract includes rigid body length, end-size/reference slots, weight, center of gravity, `linear_stiffness`, `rotational_stiffness`, stiffness behavior reference, and source/manufacturer reference slots. Human/project authority must still decide coordinate conventions, exact solver treatment of stiffness inputs, accepted source catalogs, public fixture-value policy, import formats, review disposition, dependency satisfaction, lifecycle closure, and any stricter per-family profiles.

Public fixture data is especially sensitive. Even common-looking valve, flange, reducer, rigid, or specialty dimensions, weights, COGs, and stiffness values may originate from protected standards, catalogs, or vendor sources. The current invented fixture keeps actual values missing and uses schema-shape-only/private-value policies; any public value example still needs accepted source and redistribution policy.

Preferred vocabulary for downstream work:

- `user-supplied data`: project data entered by a user or imported into a private project/library with provenance.
- `rights-cleared library data`: reusable data with documented source, redistribution status, contributor certification, and review disposition.
- `synthetic fixture`: public test/example data created only to exercise validation paths and labeled non-authoritative.
- `rigid component`: a component represented for global analysis without flexible element behavior except explicitly modeled mass/geometry effects.
- `semi-rigid component`: a component with user/manufacturer-supplied stiffness behavior; no default stiffness may be inferred.

#### Trade-offs

| Choice | Benefit | Risk / mitigation |
|---|---|---|
| Implemented shared rigid/semi-rigid family contract | Reduces duplication across valves, flanges, reducers, rigid placeholders, and specialty items | May hide family-specific validation; stricter per-family profiles remain `TBD` |
| Family-specific records | Clearer validation per family | More schema surface; keep common provenance/unit fields consistent |
| Split stiffness into `linear_stiffness` and `rotational_stiffness` | Aligns with accepted unit dimensions and addresses the generic-stiffness audit concern technically | Exact solver consumption remains `TBD`; require user/manufacturer provenance |
| Schema-shape public fixtures | Enables tests without protected data | Must remain non-authoritative and blocked from mechanics use until reviewed values and source policy exist |

#### Examples

- Current strict fixture example: `comp.invented.rigid.alpha` contains schema slots for rigid body length, connection reference, weight, COG, `linear_stiffness`, and `rotational_stiffness`, but each actual value remains missing.
- `TBD`: Public fixture value examples must be synthetic or user-supplied with documented rights and accepted redistribution policy before they can be added.
- Synthetic public fixtures are acceptable only as validation examples. They must be labeled non-authoritative and must not be used to imply engineering recommendations, code compliance, catalog equivalence, or vendor performance.
- `ASSUMPTION`: The implemented common component identity/provenance envelope remains appropriate across component families because AB-00-04 and OPS-K-DATA-3 require deterministic, provenance-preserving records.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| PKG03-DEL-03-05-PKG02-001 | Earlier audit found `specialty` in PKG-03 but not in the PKG-02 canonical component enum. | `Review_Findings.csv` row PKG03-DEL-03-05-PKG02-001 | `tests/test_component_section_schema.py` verifies `ComponentType` equals the PKG-02 canonical enum. | `Specification.md`; schema evidence interpretation | Treat as technically addressed pending human disposition. | TBD |
| PKG03-DEL-03-05-PKG02-002 | Earlier audit found generic `stiffness` dimension ambiguous against PKG-02 units. | `Review_Findings.csv` row PKG03-DEL-03-05-PKG02-002 | `ComponentQuantityDimension` uses `linear_stiffness` and `rotational_stiffness`; tests verify accepted dimensions and retired dimensions are absent. | `Specification.md`; schema evidence interpretation | Treat as technically addressed pending human disposition. | TBD |

## Component: execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-05_Rigid component models for valves, flanges, reducers, and specialty items/Procedure.md

### Procedure: DEL-03-05 Rigid component models for valves, flanges, reducers, and specialty items

#### Purpose

Define the reconciliation procedure for keeping DEL-03-05 documentation aligned with implemented component schema evidence while preserving the data boundary, unit discipline, and architecture-basis constraints.

#### Prerequisites

- Sealed brief for DEL-03-05 and write scope limited to this deliverable folder.
- `_CONTEXT.md`, `_REFERENCES.md`, and decomposition/register rows for DEL-03-05, SOW-009, OBJ-004.
- `docs/CONTRACT.md` invariants listed in the sealed brief.
- No proprietary, protected, or vendor component data in the working inputs.
- Read-only evidence: `schemas/component.schema.yaml`, `fixtures/component/invented_component_library_valid.json`, `tests/test_component_section_schema.py`, `MEMORY.md`, `_REVIEW.md`, and `Review_Findings.csv`.

#### Steps

1. Confirm the component families in scope from implementation evidence: `valve`, `flange`, `reducer`, `rigid`, and `specialty`.
2. Confirm implemented model slots from schema/fixture/test evidence: rigid body length, end-size/reference slots, weight, COG, `linear_stiffness`, `rotational_stiffness`, stiffness behavior reference, and source/manufacturer reference slots.
3. Confirm strict fixture behavior: public component values remain omitted, missing values are explicit, provenance/review metadata is present, and blocking diagnostics represent incomplete mechanics inputs.
4. Preserve unresolved choices as `TBD`: accepted source catalogs, public fixture-value policy, coordinate convention, exact stiffness solver treatment, concrete import formats, per-family engineering profiles, dependency satisfaction, human disposition, and lifecycle closure.
5. Apply public/private data controls: every reusable component datum needs provenance, license/redistribution status where applicable, and contributor/review disposition before public acceptance.
6. Preserve review finding semantics: PKG03-DEL-03-05-PKG02-001 and PKG03-DEL-03-05-PKG02-002 remain conceptually `TECHNICALLY_ADDRESSED_PENDING_HUMAN` with `HumanDisposition=TBD`; do not edit `Review_Findings.csv`.
7. Preserve architecture constraints from AB-00-01, AB-00-02, AB-00-04, AB-00-06, AB-00-07, and AB-00-08 for any downstream implementation handoff.
8. Surface gaps as diagnostics, `TBD` markers, or human-ruling items rather than resolving them silently.
9. Run targeted validation when feasible: `python3 -m pytest tests/test_component_section_schema.py` and a stale-language `rg` scoped to `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.

#### Verification

- Four local reconciliation documents exist and retain the default sections.
- No numeric component defaults, vendor data, protected tables, or standards text are introduced.
- Implemented schema/fixture/test evidence is distinguished from unresolved policy, dependency, human-disposition, and lifecycle gaps.
- All unknown implementation specifics are marked `TBD` or as assumptions/proposals.
- Dependency register validates against v3.1 schema.
- `_STATUS.md` is not set to `ISSUED`.

#### Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_run_records/TASK_RUN_*.md`

## Component: execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-05_Rigid component models for valves, flanges, reducers, and specialty items/Specification.md

### Specification: DEL-03-05 Rigid component models for valves, flanges, reducers, and specialty items

#### Scope

This deliverable covers the reconciled evidence specification for the implemented rigid and semi-rigid component schema contract for valves, flanges, reducers, rigid placeholders, and specialty items. It is limited to behavior grounded in the sealed brief, decomposition/register rows, contract invariants, `schemas/component.schema.yaml`, `fixtures/component/invented_component_library_valid.json`, `tests/test_component_section_schema.py`, and deliverable-local memory/review evidence.

Out of scope for this reconciliation:

- Editing repository-level schemas, code, fixtures, tests, package metadata, lifecycle/status files, dependency registers, review CSVs, DAG files, coordination files, or DEL-03-01.
- Introducing protected dimensional tables, manufacturer data, catalog weights, COGs, stiffness values, or default component properties.
- Claiming compliance, certification, or professional acceptance.

#### Requirements

| ID | Requirement | Source / basis | Verification hook |
|---|---|---|---|
| R01 | Support rigid and semi-rigid component data structures for valves, flanges, reducers, rigid placeholders, and specialty items. | SOW-009; Deliverables.csv row DEL-03-05; `ComponentType`; fixture rigid/semi-rigid contract | Tests verify the component enum against the PKG-02 canonical model enum and verify fixture contract coverage for `valve`, `flange`, `reducer`, `rigid`, and `specialty`. |
| R02 | Treat dimensions, weights, and centers of gravity as user-supplied or lawfully imported private/library data. | SOW-009; OPS-K-DATA-1; fixture public-value policies | Strict fixture records omit actual public component values and mark required values as missing with schema-shape or private/public-permissive policy gates. |
| R03 | Preserve unit awareness and dimensional checking for dimensional, weight, COG, and split stiffness fields. | OPS-K-UNIT-1; AB-00-04; `ComponentQuantityDimension` | Tests verify `linear_stiffness` and `rotational_stiffness` are accepted component dimensions and that retired/generic stiffness dimensions are not present. |
| R04 | Carry provenance fields for reusable component data, including source and redistribution status where public contribution or import is possible. | OPS-K-IP-2; OPS-K-DATA-3; AB-00-07; schema required fields | Schema validation requires provenance/review metadata on library, record, field, and diagnostic surfaces. |
| R05 | Represent unknown required values explicitly as `TBD`, validation findings, or diagnostics, not silent defaults. | OPS-K-DATA-2; OPS-K-AGENT-1; AB-00-06; fixture completeness rules | Strict fixture records carry missing value states, incomplete completeness findings, and blocking diagnostics such as `RIGID_COMPONENT_GEOMETRY_INCOMPLETE`. |
| R06 | Preserve the 3D centerline/frame model boundary; shell/solid FEA remains a local-analysis handoff path. | OPS-K-MECH-1 | Model interfaces do not require shell/solid elements for global analysis. |
| R07 | Keep dependencies inward toward domain contracts and through validation/diagnostics boundaries. | AB-00-02; AB-00-07 | Architecture review confirms adapters/plugins cannot bypass validation or public/private data boundaries. |
| R08 | Use deterministic, versioned, schema-governed persistence for component records. | AB-00-04 | Round-trip and canonical JSON/hash checks where JSON payloads are hashed. |
| R09 | Include strict fixture evidence for the rigid/semi-rigid contract using synthetic schema-shape records only. | Deliverables.csv artifact expectation; OPS-K-IP-1; invented component fixture | Fixture tests confirm the family contract and rigid record slots without proprietary/vendor/protected values. Concrete public fixture values for reducer, flange, valve, and specialty items remain `TBD`. |
| R10 | Define COG coordinate convention and reference frame before project or library COG values are accepted for mechanics use. | SOW-009; OPS-K-UNIT-1 | Human ruling remains `TBD`; implemented schema slots do not settle the convention. |
| R11 | Preserve minimum provenance fields for user-supplied and library-imported component data before reusable public fixtures are accepted. | OPS-K-IP-2; OPS-K-DATA-3; AB-00-07 | Provenance validator checks source, rights/redistribution status where applicable, and review disposition. Source catalog and public fixture-value policy remain `TBD`. |

#### Review Finding Reconciliation

| FindingID | Existing local CSV state | Reconciled technical evidence | Human disposition |
|---|---|---|---|
| PKG03-DEL-03-05-PKG02-001 | `TECHNICALLY_ADDRESSED_PENDING_HUMAN` | `ComponentType` includes `specialty`, and `tests/test_component_section_schema.py` verifies the PKG-03 component enum equals the PKG-02 canonical model enum. | `TBD`; CSV not edited. |
| PKG03-DEL-03-05-PKG02-002 | `TECHNICALLY_ADDRESSED_PENDING_HUMAN` | Generic `stiffness` is absent from `ComponentQuantityDimension`; implemented stiffness slots use `linear_stiffness` and `rotational_stiffness` with schema and strict fixture coverage. | `TBD`; CSV not edited. |

#### Standards

No standards text, protected tables, or code-specific component defaults are locally available or authorized for this reconciliation. References to PRD sections in the registers identify scope provenance only; they do not authorize copying standard, vendor, or catalog data.

#### Verification

Current verification signals:

- Schema validation for required component-family tags, unit dimensions, provenance fields, and explicit missing-value states.
- Protected-content review for fixtures and public examples.
- Unit tests for field validation, component enum alignment, split stiffness dimensions, strict fixture shape, and protected-content guardrails.
- Architecture tests or reviews for no-bypass validation, diagnostics, and public/private data boundaries.
- Fixture tests for the rigid/semi-rigid family contract and a rigid schema-shape record with missing required values.
- Protected-content fixture review for every public reducer, flange, valve, rigid, and specialty-item value example before any such value is accepted.
- Acceptance checks that required dimensions, weights, COGs, split stiffness entries, units, provenance, and missing-value diagnostics cannot be bypassed by adapters or public APIs.

#### Documentation

Expected documentation artifacts retained for implementation handoff include:

- Rigid/semi-rigid component model notes.
- Reducer/flange/valve fixture provenance notes.
- Explicit `TBD` list for coordinate conventions, exact stiffness solver treatment, fixture values, source catalogs, import formats, review disposition, dependency satisfaction, lifecycle closure, and reusable public-data acceptance criteria.
