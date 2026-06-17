# Source Pack: SRC-DEL-DEL-06-03-REQUIRED-INPUT-COMPLETENESS-CHECKER

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-03_Required-input completeness checker/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-03_Required-input completeness checker/Datasheet.md

### Datasheet: DEL-06-03 Required-input completeness checker

#### Identification

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

#### Attributes

| Attribute | Source-grounded value |
|---|---|
| Primary behavior | Identify missing rule-pack-required user inputs and prevent rule-check status from advancing when those inputs are absent. |
| Protected-data boundary | The checker must not bundle protected standards text, code tables, allowables, SIF/flexibility factors, proprietary formulas, or code-specific defaults. |
| User-data boundary | Code-specific and project-specific values remain user-supplied or privately imported data with provenance. |
| Status vocabulary | The relevant analysis state is `RULE_INPUTS_INCOMPLETE`; software must not emit automatic `CODE_COMPLIANT` status. |
| Warning class | Missing rule-pack input is a `RULE_CHECK_BLOCKING` condition, distinct from solve-blocking physical data. |
| Professional boundary | Checker output is a software finding; professional acceptance remains outside solver/rule code. |

#### Conditions

| Condition | Handling |
|---|---|
| Required code/project input missing | Emit an explicit missing-input finding and block user-rule-check completion. |
| Required physical input missing | Keep classified separately as solve-blocking, not rule-check-blocking. |
| Input exists but provenance is absent or weak | Surface provenance warning; do not silently accept as reliable. |
| Rule pack requests protected bundled data | Treat as data-boundary/IP issue and escalate rather than fill a default. |
| Completeness cannot be determined | Mark as `TBD` or equivalent unresolved finding; do not infer engineering values. |

#### Construction

The setup artifact defines the future feature boundary only. It does not create executable completeness rules, code formulas, material allowables, design-code tables, or checker implementation files.

The future implementation is expected to consume a rule-pack schema contract from DEL-06-01, analysis-status semantics from DEL-05-04, and diagnostics/result-envelope constraints from the architecture basis. Those dependencies are recorded as information-flow dependencies, not as schedule decisions.

#### References

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

## Component: execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-03_Required-input completeness checker/Guidance.md

### Guidance: DEL-06-03 Required-input completeness checker

#### Purpose

The required-input completeness checker protects the boundary between an open mechanics solve and a user-defined rule-pack check. A mechanics result may exist while a rule-check result is blocked because the user has not supplied required code-specific or project-specific data.

#### Principles

1. Missing rule-check data is a finding.
2. Code-specific defaults are not invented by the public project.
3. User rule packs are user-owned or private design-basis artifacts unless explicitly contributed with redistribution rights.
4. The checker gates software status only; it does not certify code compliance or professional acceptability.
5. Provenance is part of completeness whenever reliance on the supplied value may affect engineering judgment.

#### Considerations

The checker should eventually be strict about required-input declarations while staying neutral about the content of private rule packs. It can say that a required value is absent, unit-incompatible, unprovenanced, or unresolved. It must not embed standards-body tables, quote protected clauses, derive protected formulas, or silently choose engineering values.

Completeness should be machine-checkable from declarative metadata. If a future rule pack needs code-specific formulas or allowables, those belong in the user's private rule pack or another lawfully redistributable source with provenance.

#### Trade-offs

| Trade-off | Guidance |
|---|---|
| Strict blocking vs. user convenience | Prefer explicit blocking for missing declared required inputs. Convenience must not create hidden defaults. |
| Provenance warning vs. missing input | Distinguish "value absent" from "value present but source weak or unknown." |
| Public examples vs. realistic code data | Use invented non-code examples in public artifacts. Do not approximate protected standards data. |
| Software finding vs. professional judgment | Report a machine finding and keep professional acceptance outside the rule engine. |

#### Examples

This setup artifact intentionally includes no engineering example values. Later public tests should use invented/non-code placeholder rule packs that demonstrate missing-input behavior without resembling protected standards content.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CF-DEL-06-03-001 | Exact future expression grammar/library for rule-pack declarations is not selected. | `execution/_Decomposition/SOFTWARE_DECOMP.md` OI-006 | `docs/SPEC.md` rule-pack evaluator section | Specification External Inputs; Procedure Prerequisites | Treat grammar/library as `TBD` and do not encode executable rules in setup artifacts. | TBD |

## Component: execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-03_Required-input completeness checker/Procedure.md

### Procedure: DEL-06-03 Required-input completeness checker

#### Purpose

Define the setup-time procedure and future implementation checks for the required-input completeness checker without writing implementation files or executable rules in this session.

#### Prerequisites

| Prerequisite | Status for setup | Notes |
|---|---|---|
| Sealed DEL-06-03 context | Available | `_CONTEXT.md` identifies SOW-004, OBJ-002, and OBJ-005. |
| Governing data/IP boundary | Available | `docs/CONTRACT.md`, `docs/DIRECTIVE.md`, and `docs/IP_AND_DATA_BOUNDARY.md`. |
| Rule-pack schema contract | Future dependency | DEL-06-01 must define required-input declarations before checker implementation. |
| Analysis status semantics | Future dependency | DEL-05-04 supplies status vocabulary such as `RULE_INPUTS_INCOMPLETE`. |
| Rule expression grammar/library | TBD | Open issue OI-006; not resolved here. |

#### Steps

1. Confirm the deliverable identity and scope match `DEL-06-03`, `PKG-06`, and SOW-004.
2. Preserve the protected-data boundary by excluding standards text, tables, code formulas, allowables, SIF/flexibility data, vendor proprietary data, and private rule-pack content.
3. Define required checker behavior in terms of declarative required-input metadata, missing-input findings, provenance expectations, and status gating.
4. Keep solve-required missing data separate from rule-check-required missing data.
5. Require future tests to verify that missing rule-pack inputs produce `RULE_CHECK_BLOCKING` / `RULE_INPUTS_INCOMPLETE` behavior without asserting professional compliance.
6. Record dependencies on schema/status/diagnostic contracts in `Dependencies.csv`.
7. Leave implementation code, checker modules, schemas, and tests untouched for this setup-only run.

#### Verification

For this setup run, verify:

- the four-document kit exists;
- `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` exist and preserve lens-not-authority language;
- `Dependencies.csv` validates against the v3.1 schema;
- `_DEPENDENCIES.md` counts match the CSV;
- `_STATUS.md` remains within the allowed setup lifecycle and reaches `SEMANTIC_READY` only after semantic and dependency artifacts exist;
- no files outside the DEL-06-03 write scope were edited.

#### Records

The setup records are the deliverable-local documents, dependency register, semantic artifacts, status history, and run records under `_run_records/`.

## Component: execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-03_Required-input completeness checker/Specification.md

### Specification: DEL-06-03 Required-input completeness checker

#### Scope

This deliverable specifies the setup boundary for a required-input completeness checker for user-defined rule packs. The future checker must connect a rule pack's declared required inputs to project/model/user-supplied data and prevent a user-rule-check status from being reported when required rule-check data is missing.

This setup run does not implement code, schemas, executable completeness rules, code-specific formulas, allowables, or standards-derived defaults.

#### Requirements

| ID | Requirement | Source basis | Verification approach |
|---|---|---|---|
| R-DEL-06-03-001 | Missing rule-check-required values must be explicit findings, never silent defaults. | `docs/CONTRACT.md` OPS-K-DATA-2; `docs/DIRECTIVE.md` no silent engineering defaults | Future unit tests for missing required inputs and explicit findings. |
| R-DEL-06-03-002 | Code-specific and project-specific values must be user-supplied or privately imported, not bundled as public defaults. | `docs/CONTRACT.md` OPS-K-DATA-1; `docs/IP_AND_DATA_BOUNDARY.md` private user data | Protected-content and default-data review of checker fixtures. |
| R-DEL-06-03-003 | Rule-pack values, materials, components, SIF/flexibility factors, allowables, and related inputs must carry provenance where relied upon. | `docs/CONTRACT.md` OPS-K-DATA-3; `docs/TYPES.md` provenance labels | Schema/provenance validation in future feature tests. |
| R-DEL-06-03-004 | Completeness must be machine-checkable from declarative rule-pack input declarations, not arbitrary executable code. | SOW-004; `docs/SPEC.md` rule-pack `required_inputs`; OPS-K-RULE-2 | Future tests bind rule-pack required-input declarations to missing-input diagnostics without executing arbitrary code. |
| R-DEL-06-03-005 | Missing rule-pack input must map to a rule-check-blocking condition distinct from solve-blocking physical input. | `docs/SPEC.md` warning classes; `docs/TYPES.md` `RULE_INPUTS_INCOMPLETE` | Status/diagnostic tests verify `RULE_CHECK_BLOCKING` classification. |
| R-DEL-06-03-006 | The checker must not assert code compliance, certification, approval, sealing, or professional reliance. | OPS-K-AUTH-1; `docs/TYPES.md` analysis-status vocabulary | Report/API text review and future status tests exclude automatic `CODE_COMPLIANT`. |
| R-DEL-06-03-007 | Suspected protected or proprietary data requests must be surfaced and escalated, not translated into public data. | OPS-K-IP-1/2/3; `docs/IP_AND_DATA_BOUNDARY.md` quarantine rule | Protected-content lint and quarantine-path tests in later implementation. |

#### Standards

No standards-body formulas, allowables, tables, text, examples, or code-specific interpretations are included in this setup artifact. Any future private project use of licensed standards data must remain user-controlled and provenance-marked.

#### External Inputs

| Input | Required from | Notes |
|---|---|---|
| Rule-pack schema required-input declarations | DEL-06-01 Rule-pack schema | Needed before executable completeness checking can be implemented. |
| Analysis status semantics | DEL-05-04 Analysis status semantics | Needed to bind missing inputs to `RULE_INPUTS_INCOMPLETE` without compliance claims. |
| Diagnostics/result envelope contract | Architecture basis AB-00-06 | Needed for `RULE_CHECK_BLOCKING` findings and remediation text. |
| User/project rule data | User-controlled private rule pack/project files | Must not be bundled into the public repository by this deliverable. |

#### Verification

Future implementation verification must include:

- rule-pack missing-input tests using invented/non-code data only;
- unit-aware binding checks where the rule-pack schema declares dimensions or units;
- tests that missing code/project inputs block rule-check status but do not block the mechanics solve status by default;
- tests that no protected defaults, code-specific formulas, or material allowables are shipped;
- tests that output messages preserve the professional responsibility boundary.

#### Documentation

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
