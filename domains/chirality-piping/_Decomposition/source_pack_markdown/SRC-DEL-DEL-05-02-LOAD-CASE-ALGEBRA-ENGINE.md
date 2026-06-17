# Source Pack: SRC-DEL-DEL-05-02-LOAD-CASE-ALGEBRA-ENGINE

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-02_Load-case algebra engine/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-02_Load-case algebra engine/Datasheet.md

### Datasheet: DEL-05-02 Load-case algebra engine

#### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-05-02 |
| Name | Load-case algebra engine |
| Package | PKG-05 Loads, Load Cases, and Stress Recovery |
| Type | BACKEND_FEATURE_SLICE |
| Scope items | SOW-014 |
| Objectives | OBJ-003, OBJ-005 |
| Context envelope | M |

#### Attributes

| Attribute | Evidence value | Source |
|---|---|---|
| Primary subject | Unit-aware algebra for user-defined load-case combinations and result-state subtraction/ranging. | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` row DEL-05-02 |
| Mechanics boundary | Combination results remain mechanics solver/result states; code acceptability is evaluated by user rule packs. | `docs/CONTRACT.md` OPS-K-MECH-2 |
| Unit discipline | Implemented algebra quantities carry `LoadDimension`; combinations, subtraction, and range envelopes block incompatible dimensions instead of converting or repairing them. | `core/loads/load_case_algebra/README.md`; `core/loads/load_case_algebra/src/lib.rs` |
| Result boundary metadata | Result-boundary export requires explicit unit metadata, provenance reference, result schema binding, payload reference, and payload-hash reference. Load-record schema bindings are rejected for result quantities. | `core/loads/load_case_algebra/README.md`; `core/loads/load_case_algebra/src/lib.rs` |
| Data boundary | Code-specific combinations, allowables, protected standards content, and project-specific rule content are not bundled defaults. | `docs/CONTRACT.md` OPS-K-DATA-1; `core/loads/load_case_algebra/README.md` |
| Rule-pack boundary | The crate does not implement the rule-pack expression evaluator or arbitrary executable rules; rule-pack integration remains outside this deliverable slice. | SOW-014; OPS-K-RULE-2; `core/loads/load_case_algebra/README.md` |
| Expression grammar/library | General expression grammar/library remains TBD. The implemented API uses explicit enum variants and terms rather than a parser or code-specific syntax. | `_CONTEXT.md` Still TBD; `core/loads/load_case_algebra/src/lib.rs` |

#### Conditions

- Missing combination inputs, missing result states, duplicate operands, non-finite factors, incompatible dimensions, empty expressions, unsupported expression shapes, and status-boundary violations are represented as deterministic findings rather than silent defaults. Source: `core/loads/load_case_algebra/README.md`; `core/loads/load_case_algebra/src/lib.rs`; OPS-K-DATA-2.
- Solver/rule changes require deterministic verification before release. Current crate evidence includes targeted unit tests for the bounded algebra surface. Source: OPS-K-SOLVER-1; AB-00-08; `core/loads/load_case_algebra/src/lib.rs`.
- Result envelopes must preserve mechanics-solved, user-rule-checked, human-review-required, and human-approved distinctions; the crate rejects automatic propagation of `HumanApprovedForProject`. Source: AB-00-03; `core/loads/load_case_algebra/src/lib.rs`.
- Diagnostics and result envelopes must carry code, class, severity, source, affected object, message, remediation, and provenance where applicable. Source: AB-00-06.

#### Construction

| Artifact | Description | Evidence status |
|---|---|---|
| Combination engine | `open_pipe_stress_load_case_algebra` exposes explicit linear combinations, result-state subtraction, and range envelopes over compatible mechanics quantities. | Implemented in `core/loads/load_case_algebra` |
| Expression tests | Unit tests cover compatible combinations, subtraction, range envelopes, dimension mismatch, missing/duplicate operands, non-finite factors, result boundary metadata, status propagation, and human-approval rejection. | Implemented in `core/loads/load_case_algebra/src/lib.rs` |
| Rule-pack handoff | Boundary allows explicit mechanics/result operands while excluding rule-pack expression evaluation, code-specific defaults, protected standard formulas, and professional reliance claims. | Implemented boundary; evaluator/interface details remain TBD |
| Diagnostics | Finding vocabulary covers missing operands, empty expressions, non-finite factors, dimension mismatches, duplicate operands, unsupported expression shapes, missing result states, and status-boundary violations. | Implemented finding vocabulary and deterministic blocking behavior |

#### References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7
- `docs/_Registers/Deliverables.csv` row DEL-05-02
- `docs/_Registers/ScopeLedger.csv` row SOW-014
- `docs/_Registers/ContextBudgetQA.csv` row DEL-05-02
- `docs/CONTRACT.md`

## Component: execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-02_Load-case algebra engine/Guidance.md

### Guidance: DEL-05-02 Load-case algebra engine

#### Purpose

This deliverable documents the bounded load-case algebra implementation that combines explicit mechanics quantities and result states in a unit-aware way while leaving code-specific combinations and acceptance decisions to user-owned rule packs and human authority.

#### Principles

- Keep algebra mechanics-focused: addition, scaling, subtraction, and ranging describe load/result relationships, not code compliance.
- Treat units and dimensions as first-class constraints; an expression that mixes incompatible dimensions is a finding, not a repair opportunity.
- Keep code-specific combinations outside the product baseline unless supplied by lawful/private user rule packs.
- Keep rule-pack evaluation declarative and sandboxed; this implementation does not include arbitrary executable rules or the rule-pack expression evaluator.
- Preserve status separation between mechanics solved, rule-pack checked, and human-approved outputs.

#### Considerations

| Topic | Guidance | Evidence |
|---|---|---|
| Expression grammar | General grammar/library remains TBD. Current implementation uses explicit `AlgebraExpression` variants and `CombinationTerm` values, not a parser or code-specific syntax. | `_CONTEXT.md` Still TBD; `core/loads/load_case_algebra/src/lib.rs`; OPS-K-RULE-2 |
| Primitive load and result dependencies | Inputs must arrive as explicit mechanics/result operands with dimensions and boundary metadata already governed upstream. DEL-05-01 and DEL-05-04 remain pending dependency maturity items in the local register. | `_DEPENDENCIES.md`; `core/loads/load_case_algebra/README.md` |
| Rule-pack combinations | User rule packs may supply code-specific combinations through a governed interface, but the crate does not provide code-specific defaults or a rule-pack evaluator. The DEL-06-02 evaluator interface remains TBD/low-confidence. | SOW-014; OBJ-005; `_DEPENDENCIES.md` |
| Diagnostics | Missing operands, empty expressions, non-finite factors, dimensional mismatch, duplicate operands, unsupported expression shapes, missing result states, and status-boundary violations are deterministic findings or boundary errors. | OPS-K-DATA-2; AB-00-06; `core/loads/load_case_algebra/src/lib.rs` |
| Result boundary metadata | Boundary export requires explicit unit metadata, result schema binding, provenance reference, payload reference, and payload-hash reference; load-record schema binding is rejected for result quantities. | `core/loads/load_case_algebra/README.md`; `core/loads/load_case_algebra/src/lib.rs` |

#### Trade-offs

- A more expressive grammar can help users define combinations, but increases validation and sandboxing risk. Grammar choice remains TBD.
- Hard-coded combinations might appear convenient, but would violate the data boundary for code-specific and project-specific rule content.
- Implemented subtraction/ranging support deliberately stays deterministic and mechanics-focused instead of broadening into expression-language flexibility.

#### Examples

Examples remain intentionally abstract. No code-specific load combination, allowable, or protected standard formula is provided in this deliverable.

#### Conflict Table (for human ruling)

| Conflict ID | Topic | Contenders | Human ruling |
|---|---|---|---|
| None | No source conflict identified during this implementation-evidence alignment. | N/A | N/A |

## Component: execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-02_Load-case algebra engine/Procedure.md

### Procedure: DEL-05-02 Load-case algebra engine

#### Purpose

Define the procedure for maintaining and verifying the bounded load-case algebra implementation evidence without introducing code-specific defaults, protected content, or professional/code-compliance claims.

#### Prerequisites

- Sealed deliverable context in `_CONTEXT.md`.
- Governing invariants in `docs/CONTRACT.md`.
- Decomposition and register rows for DEL-05-02, SOW-014, OBJ-003, and OBJ-005.
- Read-only implementation evidence in `core/loads/load_case_algebra/README.md` and `core/loads/load_case_algebra/src/lib.rs`.
- Human authorization before implementing a general expression grammar/library, code-specific load combinations/defaults, protected rule content, or rule-pack execution behavior.

#### Steps

1. Confirm the deliverable scope is limited to unit-aware load-case algebra, user-defined explicit combinations, result-state subtraction, and range envelopes.
2. Confirm exclusions: no code-specific load combinations/defaults, no protected standards content, no arbitrary executable rules, no rule-pack evaluator, and no certification or professional-reliance claims.
3. Maintain the data boundary: code-specific combinations are supplied by user rule packs and remain outside bundled public defaults.
4. Verify deterministic implementation evidence for compatible-unit combinations, incompatible dimensions, missing operands, duplicate operands, missing result states, non-finite factors, subtraction/ranging, result-boundary metadata, status propagation, and human-approval rejection.
5. Record unknowns as `TBD`, including general expression grammar/library, final rule-pack evaluator/interface behavior, final result-envelope/persistence integration, and release/CI gate policy.
6. Preserve deliverable evidence in the four documents, semantic files, dependency artifacts, status history, memory, and run records.

#### Verification

| Check | Expected result |
|---|---|
| Four-document kit exists | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present. |
| Implementation evidence present | `core/loads/load_case_algebra/README.md`, `Cargo.toml`, and `src/lib.rs` exist and remain read-only for documentation-alignment runs. |
| Algebra crate tests | `cargo test --manifest-path core/loads/load_case_algebra/Cargo.toml` passes before claiming current implementation evidence is validated. |
| Data boundary preserved | No code-specific combinations, allowables, or protected standard formulas are introduced. |
| Dependency register unchanged | `Dependencies.csv`, `_DEPENDENCIES.md`, and `_STATUS.md` remain read-only unless a separate authorized dependency or status task permits edits. |
| Status safe | `_STATUS.md` is not `ISSUED`. |

#### Records

- Four-document kit.
- `_SEMANTIC.md` and `_SEMANTIC_LENSING.md`.
- `Dependencies.csv` and `_DEPENDENCIES.md`.
- `MEMORY.md`.
- `_run_records/` entries for the requested TASK sequence.

## Component: execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-02_Load-case algebra engine/Specification.md

### Specification: DEL-05-02 Load-case algebra engine

#### Scope

This specification records the bounded implementation evidence for a backend load-case algebra deliverable covering unit-aware user-defined combinations and result-state subtraction/ranging. The implemented crate is `core/loads/load_case_algebra`. It does not define code-specific combinations, choose a general expression grammar/library, bundle protected rule data, execute arbitrary rule-pack code, or claim code compliance.

#### Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-05-02-001 | The deliverable shall preserve unit-aware algebra for user-defined combinations. | SOW-014 |
| REQ-05-02-002 | Combination expressions shall reject or report dimensionally incompatible operations as explicit findings. | OPS-K-UNIT-1; OPS-K-DATA-2 |
| REQ-05-02-003 | Result-state subtraction and ranging shall remain mechanics-result operations and shall not imply code compliance. | DEL-05-02 description; OPS-K-MECH-2 |
| REQ-05-02-004 | Code-specific load combinations shall be supplied by user rule packs, not by bundled public defaults. | SOW-014 notes; OPS-K-DATA-1 |
| REQ-05-02-005 | The algebra surface shall not require arbitrary executable rules. | OPS-K-RULE-2 |
| REQ-05-02-006 | Missing primitive load cases, referenced result states, or rule-required inputs shall be reported explicitly, not silently defaulted. | OPS-K-DATA-2 |
| REQ-05-02-007 | Command/query/job result envelopes shall preserve mechanics solved, user-rule checked, and human-approved state separation. | AB-00-03 |
| REQ-05-02-008 | Diagnostics produced by the algebra layer shall carry provenance-compatible envelope fields when applicable. | AB-00-06 |
| REQ-05-02-009 | Deterministic tests shall cover valid unit-compatible combinations, invalid dimensional mixes, missing operands, subtraction/ranging, and no-default rule-pack boundaries before release use. | OPS-K-SOLVER-1; AB-00-08 |

#### Standards

No external protected standard text is introduced by this deliverable. Governing local standards are the project invariant catalog, the sealed architecture-basis rows AB-00-01, AB-00-02, AB-00-03, AB-00-06, and AB-00-08, and the decomposition/register rows listed in `_CONTEXT.md`.

#### Verification

| Requirement | Verification approach |
|---|---|
| REQ-05-02-001 | Implemented unit test `linear_combination_sums_compatible_quantities` validates explicit factors over compatible mechanics quantities. |
| REQ-05-02-002 | Implemented test `dimension_mismatch_blocks_result` verifies incompatible dimensions block the result and emit `FindingCode::DimensionMismatch`. |
| REQ-05-02-003 | Implemented tests `subtraction_requires_distinct_compatible_result_states` and `range_envelope_selects_extreme_value` verify mechanics-only subtraction and range-envelope behavior. |
| REQ-05-02-004 | Crate README/source boundary states no bundled design-code combinations, public default factors, protected standards content, or professional/code-compliance claims. |
| REQ-05-02-005 | Implementation uses explicit `AlgebraExpression` enum variants and does not include a parser, arbitrary execution path, or rule-pack expression evaluator. |
| REQ-05-02-006 | Implemented tests and finding paths cover missing operands, duplicate operands, missing result states, empty expressions, and non-finite factors as explicit findings or boundary errors. |
| REQ-05-02-007 | Implemented status propagation preserves mechanics/rule statuses, adds `HumanReviewRequired`, and blocks automatic `HumanApprovedForProject` propagation. |
| REQ-05-02-008 | Implemented result-boundary tests verify explicit unit metadata, provenance-compatible record fields, result-schema binding, payload/hash references, and rejection of load-record schema binding for result quantities. |
| REQ-05-02-009 | Targeted crate validation is `cargo test --manifest-path core/loads/load_case_algebra/Cargo.toml`; project CI/release-gate inclusion remains TBD. |

#### Documentation

Required deliverable-local artifacts are `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `Dependencies.csv`, `_DEPENDENCIES.md`, `_STATUS.md`, and `_run_records/`. Implementation evidence is read-only for this TASK run at `core/loads/load_case_algebra/README.md` and `core/loads/load_case_algebra/src/lib.rs`.
