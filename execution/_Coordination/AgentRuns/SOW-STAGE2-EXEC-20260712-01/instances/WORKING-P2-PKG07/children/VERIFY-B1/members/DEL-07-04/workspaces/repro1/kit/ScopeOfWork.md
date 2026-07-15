---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-07-04
package_id: PKG-07
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@eaad463c0d481f6f1654e6adb5ee718f566176e9
project_scope_refs: [SOW-022]
package_objective_refs: [OBJ-006, OBJ-011]
---

# Scope of Work — DEL-07-04

## Purpose and Objective Traceability

This migration candidate defines `DEL-07-04` in service of project scope [SOW-022] and package objectives [OBJ-006, OBJ-011].

- **OUT-001** — A missing-data warning and blocking-UX contract covering typed findings, solve-blocking and rule-check-blocking separation, affected-object navigation, provenance and unit diagnostics, remediation guidance, and visible professional-boundary status is produced for the declared scope and objectives.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"ce09d04df482ac4eeb44eb2fdd5c645b2792fd85ca77d8925ad4cf67dc9f1b10","target_id":"CLM-001"} -->
#### Datasheet: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":14,"line_start":3,"source_sha256":"ce09d04df482ac4eeb44eb2fdd5c645b2792fd85ca77d8925ad4cf67dc9f1b10","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-07-04 |
| Package | PKG-07 Graphical User Interface and Engineering Workflow |
| Type | UX_UI_SLICE |
| Scope items | SOW-022 |
| Objectives | OBJ-006, OBJ-011 |
| Anticipated artifacts | warning system UI; UX tests |
| Setup status | Setup/document-production only; no GUI source files, tests, schemas, package manifests, or repo-level docs are edited. |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":29,"line_start":15,"source_sha256":"ce09d04df482ac4eeb44eb2fdd5c645b2792fd85ca77d8925ad4cf67dc9f1b10","target_id":"CLM-003"} -->
##### Attributes

This deliverable defines the setup boundary for a future GUI warning and blocking workflow. The future UX must distinguish data that blocks a mechanics solve from data that blocks or qualifies a user-rule check, while keeping provenance, assumptions, nonlinear uncertainty, IP/data-boundary risks, and professional review visible.

| Attribute | Required treatment | Source basis |
|---|---|---|
| Solve-required missing data | Classify as `SOLVE_BLOCKING` and prevent or invalidate the affected mechanics solve rather than supplying defaults. | `docs/SPEC.md` section 7; OPS-K-DATA-2 |
| Rule-check-required missing data | Classify as `RULE_CHECK_BLOCKING`; mechanics results may exist, but user-rule pass/fail or ratios remain unavailable or qualified. | `docs/SPEC.md` section 7; `docs/TYPES.md` analysis-status vocabulary |
| Provenance weakness | Classify as `PROVENANCE_WARNING` when a value exists but source/provenance is missing or weak. | OPS-K-DATA-3; AB-00-06 |
| User/model assumptions | Classify as `ASSUMPTION_WARNING` and keep the assumption visible through result review/report handoff. | SOW-022; OBJ-006 |
| Nonlinear uncertainty | Classify as `NONLINEAR_WARNING` when convergence or active-state uncertainty affects interpretation. | OPS-K-SOLVER-2; `docs/SPEC.md` section 4.4 and section 7 |
| IP or private-data risk | Classify as `IP_BOUNDARY_WARNING`; do not move protected/private data into public artifacts. | OPS-K-IP-1/2/3; `docs/IP_AND_DATA_BOUNDARY.md` quarantine rule |
| Professional boundary | Never present software output as certified, sealed, approved, authenticated, or professionally code-compliant. | OPS-K-AUTH-1; OBJ-011 |
| Warning display access | Warning class, severity, affected object, message, and remediation must be available through text/assistive paths and not color-only signaling. | `_SEMANTIC_LENSING.md` C-001; `docs/SPEC.md` section 7 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":40,"line_start":30,"source_sha256":"ce09d04df482ac4eeb44eb2fdd5c645b2792fd85ca77d8925ad4cf67dc9f1b10","target_id":"CLM-004"} -->
##### Conditions

| Condition | Setup ruling |
|---|---|
| Silent engineering defaults | Prohibited. Unknown engineering values remain `TBD` or become explicit diagnostics. |
| Protected standards/code data | Not included. No code text, code tables, copied formulas, material allowables, SIF/flexibility tables, or proprietary values are introduced. |
| Result-envelope fields | Future warnings must preserve at least code, class, severity, source, affected object, message, remediation, and provenance where applicable. |
| Analysis state separation | Future UX must preserve `MODEL_INCOMPLETE`, `MECHANICS_SOLVED`, `RULE_INPUTS_INCOMPLETE`, `USER_RULE_CHECKED`, `USER_RULE_FAILED`, and `HUMAN_REVIEW_REQUIRED` distinctions; it must not auto-emit `CODE_COMPLIANT`. |
| GUI architecture | Future GUI mutation and state changes route through application-service command/query/job result envelopes and preserve durable/transient state separation. |
| Surface placement | Exact editor, solve-runner, results-view, report-preview, and export-control placement remains implementation-level `TBD`; this setup defines behavior and boundaries only. |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":53,"line_start":41,"source_sha256":"ce09d04df482ac4eeb44eb2fdd5c645b2792fd85ca77d8925ad4cf67dc9f1b10","target_id":"CLM-005"} -->
##### Construction

The setup artifact is a document kit and local evidence bundle. It does not create visual components, application state, tests, schemas, or source-code contracts.

Future implementation work is expected to consume:

- architecture basis AB-00-03 for command/query/job result envelopes and status separation;
- architecture basis AB-00-05 for GUI state, editing, and diagnostic preservation;
- architecture basis AB-00-06 for diagnostics, warning classes, and result-envelope fields;
- DEL-04-06 for solver diagnostic producers;
- DEL-05-04 for analysis status semantics;
- DEL-06-03 for rule-pack required-input completeness signals.

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":63,"line_start":54,"source_sha256":"ce09d04df482ac4eeb44eb2fdd5c645b2792fd85ca77d8925ad4cf67dc9f1b10","target_id":"CLM-006"} -->
##### References

- `_CONTEXT.md` for deliverable identity, scope, objectives, and architecture-basis injection.
- `docs/CONTRACT.md` for invariants OPS-K-DATA-1/2/3, OPS-K-RULE-1/2/3, OPS-K-AUTH-1, OPS-K-IP-1/2/3, OPS-K-PRIV, and OPS-K-AGENT-1..4.
- `docs/SPEC.md` section 7 for GUI warnings and warning classes.
- `docs/TYPES.md` section 4 for analysis-status vocabulary.
- `docs/DIRECTIVE.md` sections 2 and 5 for missing-data, professional-boundary, and stop-rule treatment.
- `docs/IP_AND_DATA_BOUNDARY.md` for provenance and quarantine rules.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` rows SOW-022, OBJ-006, OBJ-011, and AB-00-03/05/06.

<!-- sow-source-end -->

### CLM-007 — D-41 R5 T7 PDU-054 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":66,"line_start":64,"source_sha256":"ce09d04df482ac4eeb44eb2fdd5c645b2792fd85ca77d8925ad4cf67dc9f1b10","target_id":"CLM-007"} -->
##### D-41 R5 T7 PDU-054 current declaration

Earlier setup-era statements on this surface are retained as historical setup context where applicable; this section is the active current-state declaration. The missing-data warning/blocking panel is implemented, including current nonlinear-visibility behavior. It presents existing diagnostics and does not synthesize engineering inputs, resolve warnings, or confer professional approval.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-008"} -->
#### Specification: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":6,"line_start":3,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-009"} -->
##### Scope

This deliverable specifies the setup boundary for a future GUI warning and blocking workflow. It covers warning classification, blocking and qualifying behavior, result-envelope visibility, and professional/IP boundary wording for missing or weak data. It does not implement GUI components, application state, schemas, tests, package manifests, or product source code.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":24,"line_start":7,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-010"} -->
##### Requirements

| ReqID | Requirement | Source basis | Verification approach |
|---|---|---|---|
| R-DEL-07-04-001 | The future GUI shall preserve the warning classes `SOLVE_BLOCKING`, `RULE_CHECK_BLOCKING`, `PROVENANCE_WARNING`, `ASSUMPTION_WARNING`, `NONLINEAR_WARNING`, and `IP_BOUNDARY_WARNING`. | `docs/SPEC.md` section 7; AB-00-06 | UI/result-envelope tests inspect class values from representative diagnostics. |
| R-DEL-07-04-002 | Missing solve-required physical input shall block or invalidate the affected mechanics solve and shall not be replaced by silent defaults. | SOW-022; OPS-K-DATA-2; `docs/TYPES.md` `MODEL_INCOMPLETE` | UX tests show solve action/result state is blocked or marked incomplete with remediation. |
| R-DEL-07-04-003 | Missing rule-check-required user/code/project data shall block or qualify rule-pack check results while preserving any valid mechanics-solve result. | SOW-022; `docs/TYPES.md` `RULE_INPUTS_INCOMPLETE`; DEL-06-03 setup evidence | UX tests show mechanics results can remain reviewable while rule-check ratios/pass-fail are unavailable or qualified. |
| R-DEL-07-04-004 | The GUI shall present diagnostics through result-envelope fields that include code, class, severity, source, affected object, message, remediation, and provenance where applicable. | AB-00-06; DEL-00-06 Specification REQ-06-01 | Contract/UI tests verify required diagnostic fields are rendered or available to assistive tooling. |
| R-DEL-07-04-005 | The warning workflow shall preserve analysis-status distinctions among incomplete model, mechanics solved, rule inputs incomplete, user-rule checked/failed, human review required, and human acceptance records. | AB-00-03; DEL-05-04; `docs/TYPES.md` section 4 | Status-mapping tests prevent collapse into a single automatic pass/compliance state. |
| R-DEL-07-04-006 | Provenance weakness shall remain visible as `PROVENANCE_WARNING`; value presence alone is insufficient to hide source/provenance risk. | OPS-K-DATA-3; `docs/IP_AND_DATA_BOUNDARY.md` section 4 | UX tests show missing/weak provenance is visible for relevant materials, components, rule values, and report/export surfaces. |
| R-DEL-07-04-007 | Assumptions shall remain visible as `ASSUMPTION_WARNING` and shall not be treated as authenticated engineering approval. | OBJ-006; OPS-K-AUTH-1 | Review workflow tests show assumption warnings survive result review and report handoff. |
| R-DEL-07-04-008 | Nonlinear convergence or active-state uncertainty shall remain visible as `NONLINEAR_WARNING` and shall not be hidden behind nominal result display. | OPS-K-SOLVER-2; `docs/SPEC.md` section 4.4 | Solver-result UX tests expose convergence/active-state uncertainty when present. |
| R-DEL-07-04-009 | Suspected protected/private content in public contribution, export, or report flows shall produce `IP_BOUNDARY_WARNING` and route to quarantine or human review rather than public output. | OPS-K-IP-1/2/3; `docs/IP_AND_DATA_BOUNDARY.md` section 5 | Protected-content/export tests verify warning and block/quarantine behavior. |
| R-DEL-07-04-010 | GUI warning text shall not claim certification, sealing, approval, authentication, official endorsement, or professional code compliance. | OPS-K-AUTH-1; `docs/DIRECTIVE.md` sections 2 and 5 | Product-claims wording review and negative tests exclude automatic `CODE_COMPLIANT` or equivalent claims. |
| R-DEL-07-04-011 | GUI state changes that affect solve or rule-check readiness shall route through application-service commands and preserve diagnostics across undo/redo where applicable. | AB-00-05; DEL-00-05 Specification REQ-05-03/05 | Future interaction tests verify warning state updates after editable model changes. |
| R-DEL-07-04-012 | Setup artifacts and future public examples shall use invented/non-code data only and shall not embed protected standards text, copied formulas, protected tables, or proprietary values. | OPS-K-IP-1; OPS-K-RULE-1 | Protected-content review confirms setup and future fixtures remain clean. |
| R-DEL-07-04-013 | Warning class, severity, affected object, message, and remediation shall be exposed through text/assistive paths and shall not rely on color-only signaling. | `_SEMANTIC_LENSING.md` C-001; SOW-036 adjacency via DEL-07-06 | Accessibility-oriented UX tests confirm non-color and assistive access to warning meaning. |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":28,"line_start":25,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-011"} -->
##### Standards

No standards-body formulas, allowables, text, examples, or protected data are included. Code-specific values and rule-pack data remain user-supplied or privately imported with provenance. Any future private project use of licensed standards data remains the user's responsibility and must not be committed as public project content.

<!-- sow-source-end -->

### CLM-012 — External Inputs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":39,"line_start":29,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-012"} -->
##### External Inputs

| Input | Required from | Notes |
|---|---|---|
| Application-service result envelopes and status separation | AB-00-03 / DEL-00-03 | Needed before implementation can bind warnings to command/query/job results. |
| GUI state and diagnostic preservation architecture | AB-00-05 / DEL-00-05 | Needed for undo/redo, editing, and transient/durable state boundaries. |
| Diagnostics and warning-class contract | AB-00-06 / DEL-00-06 | Required source for warning classes and diagnostic field set. |
| Solver diagnostics | DEL-04-06 | Required for solve-blocking and nonlinear warning producers. |
| Analysis status semantics | DEL-05-04 | Required for status distinctions and no-compliance boundary. |
| Rule-pack required-input completeness signals | DEL-06-03 | Required for rule-check-blocking missing-data behavior. |

<!-- sow-source-end -->

### CLM-013 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":53,"line_start":40,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-013"} -->
##### Verification

Future implementation verification must include:

- UI tests for each warning class listed in R-DEL-07-04-001;
- per-class tests proving all six classes remain distinct rather than collapsing into generic alerts;
- tests that `SOLVE_BLOCKING` prevents or invalidates the affected mechanics solve without inventing defaults;
- tests that `RULE_CHECK_BLOCKING` blocks/qualifies rule-check results without erasing mechanics results;
- tests that provenance, assumption, nonlinear, and IP-boundary warnings remain visible through result review and report/export handoff;
- accessibility-oriented checks that warning severity, class, message, affected object, and remediation are available without color-only signaling;
- wording checks that no warning, report preview, or status surface claims certification, approval, sealing, authentication, official endorsement, or professional code compliance;
- protected-content checks for public examples, exported artifacts, and report templates touched by future implementation.
- explicit `IP_BOUNDARY_WARNING` tests for public contribution, export, and report-preview paths using invented fixtures only.

<!-- sow-source-end -->

### CLM-014 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":70,"line_start":54,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-014"} -->
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

Implementation artifacts listed in the register (`warning system UI`, `UX tests`) remain future work outside this setup session's write scope.

<!-- sow-source-end -->

### CLM-015 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":75,"line_start":71,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-015"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified during P1/P2 setup. | N/A | N/A | N/A | N/A | TBD |
<!-- sow-source-end -->

### CLM-016 — D-41 R5 T5 PDU-008 current GUI boundary

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":79,"line_start":76,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-016"} -->
##### D-41 R5 T5 PDU-008 current GUI boundary

Supplied diagnostics whose codes begin `NONLINEAR_` are displayed as `NONLINEAR_WARNING` records with severity, message, source, affected refs, and any supplied class/remediation. The GUI does not create nonlinear outcomes or replace producer evidence.

<!-- sow-source-end -->

### CLM-017 — D-41 R5 T7 PDU-054 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":82,"line_start":80,"source_sha256":"635be990d56afc78b496a4407a9cd920ecd8b3139a73977791738ac58b801f1b","target_id":"CLM-017"} -->
##### D-41 R5 T7 PDU-054 current declaration

Earlier setup-era statements on this surface are retained as historical setup context where applicable; this section is the active current-state declaration. The missing-data warning/blocking panel is implemented, including current nonlinear-visibility behavior. It presents existing diagnostics and does not synthesize engineering inputs, resolve warnings, or confer professional approval.
<!-- sow-source-end -->

- **AC-001** — The contract preserves explicit fail-closed behavior, the distinction between mechanics input completeness and user-rule input completeness, and current warning UX evidence without inventing values, suppressing findings, treating absence as success, or implying code compliance or approval.

## Production and Verification Method — Praxeology

### CLM-018 — Procedure: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"d01c369ce718948b0c7c4cc90220118fe61c1db58ad71aa3db8f11162cf4b363","target_id":"CLM-018"} -->
#### Procedure: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-end -->

### CLM-019 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"d01c369ce718948b0c7c4cc90220118fe61c1db58ad71aa3db8f11162cf4b363","target_id":"CLM-019"} -->
##### Purpose

This procedure defines how future implementation work should use the setup artifact for missing-data warning and blocking UX. It is an operational guide for the deliverable, not an implementation script.

<!-- sow-source-end -->

### CLM-020 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":13,"line_start":7,"source_sha256":"d01c369ce718948b0c7c4cc90220118fe61c1db58ad71aa3db8f11162cf4b363","target_id":"CLM-020"} -->
##### Prerequisites

- Confirm the active sealed scope is DEL-07-04 / PKG-07.
- Read `_CONTEXT.md`, `docs/CONTRACT.md`, `docs/SPEC.md` section 7, `docs/TYPES.md` section 4, and the applicable architecture basis rows AB-00-03, AB-00-05, and AB-00-06.
- Confirm upstream setup evidence for DEL-04-06, DEL-05-04, and DEL-06-03 before writing implementation code.
- Confirm no protected standards text, protected tables, copied formulas, proprietary values, private rule packs, or certification/compliance claims are introduced.

<!-- sow-source-end -->

### CLM-021 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":24,"line_start":14,"source_sha256":"d01c369ce718948b0c7c4cc90220118fe61c1db58ad71aa3db8f11162cf4b363","target_id":"CLM-021"} -->
##### Steps

1. Classify missing or weak data by warning class: `SOLVE_BLOCKING`, `RULE_CHECK_BLOCKING`, `PROVENANCE_WARNING`, `ASSUMPTION_WARNING`, `NONLINEAR_WARNING`, or `IP_BOUNDARY_WARNING`.
2. Map `SOLVE_BLOCKING` conditions to `MODEL_INCOMPLETE` or equivalent incomplete mechanics-solve status without inventing defaults.
3. Map `RULE_CHECK_BLOCKING` conditions to `RULE_INPUTS_INCOMPLETE` or equivalent rule-check-blocked status while preserving valid mechanics results when available.
4. Preserve diagnostic fields from result envelopes: code, class, severity, source, affected object, message, remediation, and provenance where applicable.
5. Present warnings in the GUI where users edit data, run solves, review results, and prepare reports/exports.
6. Keep warning state synchronized through application-service commands and job/result envelopes; do not mutate domain readiness directly from transient UI state.
7. Check wording for professional-boundary compliance before any user-facing message is accepted.
8. Check public examples, screenshots, exports, report previews, and fixtures for protected-content and private-data boundary risks.

<!-- sow-source-end -->

### CLM-022 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":37,"line_start":25,"source_sha256":"d01c369ce718948b0c7c4cc90220118fe61c1db58ad71aa3db8f11162cf4b363","target_id":"CLM-022"} -->
##### Verification

Future verification should confirm:

- each warning class can be rendered from a representative diagnostic envelope;
- all six warning classes remain distinct in tests and are not collapsed into a generic alert state;
- solve-blocking and rule-check-blocking behavior remain distinct;
- missing values are surfaced as `TBD`, diagnostic findings, or blocked/qualified results rather than silent defaults;
- provenance, assumption, nonlinear, and IP-boundary warnings survive result review and report/export handoff;
- keyboard, non-color, and assistive-technology paths can identify warning class, severity, affected object, and remediation;
- warning text does not claim certification, approval, sealing, authentication, official endorsement, or code compliance.
- `IP_BOUNDARY_WARNING` blocks, qualifies, quarantines, or routes public contribution/report/export risk without exposing protected/private data.

<!-- sow-source-end -->

### CLM-023 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":47,"line_start":38,"source_sha256":"d01c369ce718948b0c7c4cc90220118fe61c1db58ad71aa3db8f11162cf4b363","target_id":"CLM-023"} -->
##### Records

Maintain these local setup records:

- four-document kit: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`;
- semantic artifacts: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`;
- dependency artifacts: `Dependencies.csv`, `_DEPENDENCIES.md`;
- run records under `_run_records/`;
- lifecycle record in `_STATUS.md`.

<!-- sow-source-end -->

### CLM-024 — D-41 R5 T7 PDU-054 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":50,"line_start":48,"source_sha256":"d01c369ce718948b0c7c4cc90220118fe61c1db58ad71aa3db8f11162cf4b363","target_id":"CLM-024"} -->
##### D-41 R5 T7 PDU-054 current declaration

Earlier setup-era statements on this surface are retained as historical setup context where applicable; this section is the active current-state declaration. The missing-data warning/blocking panel is implemented, including current nonlinear-visibility behavior. It presents existing diagnostics and does not synthesize engineering inputs, resolve warnings, or confer professional approval.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, diagnostic classes and severity, blocking-state separation, navigation and remediation surfaces, missing/incompatible/unprovenanced data handling, current implementation declarations and residuals, and no-silent-default behavior.

## Governing Values and Decisions — Axiology

### CLM-025 — Guidance: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-025"} -->
#### Guidance: DEL-07-04 Missing-data warning and blocking UX

<!-- sow-source-end -->

### CLM-026 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":6,"line_start":3,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-026"} -->
##### Purpose

This deliverable prepares the warning and blocking UX surface for future GUI implementation. The key distinction is that a mechanics solve, a user-rule check, and a professional acceptance decision are different states. The GUI must help users see missing data, assumptions, provenance weakness, nonlinear uncertainty, and IP/private-data risks without filling engineering gaps silently.

<!-- sow-source-end -->

### CLM-027 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":16,"line_start":7,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-027"} -->
##### Principles

- Missing solve-required or rule-check-required values are findings, not hidden defaults.
- `SOLVE_BLOCKING` and `RULE_CHECK_BLOCKING` are not interchangeable: the former affects mechanics solve readiness; the latter affects rule-check readiness.
- Result displays may show mechanics outputs only with the relevant diagnostics and limitations visible.
- Warnings should carry actionable remediation, affected object identity, source/provenance where applicable, and severity.
- Warning UX must preserve the professional responsibility boundary: software assists analysis but does not certify, approve, seal, authenticate, or declare code compliance for reliance.
- Public-facing examples, report previews, and exports must preserve protected-data and privacy boundaries.
- `HUMAN_REVIEW_REQUIRED` is the appropriate reminder for professional reliance; it is not a substitute for a human approval record and must not be presented as software approval.

<!-- sow-source-end -->

### CLM-028 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":27,"line_start":17,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-028"} -->
##### Considerations

| Warning class | UX implication | Boundary to preserve |
|---|---|---|
| `SOLVE_BLOCKING` | Disable, block, or invalidate the affected solve path and point to the missing physical input. | Do not invent geometry, material, support, load, section, or component values. |
| `RULE_CHECK_BLOCKING` | Keep mechanics results reviewable when valid, but block or qualify user-rule-check results and ratios. | Do not imply code pass/fail, compliance, or professional acceptance. |
| `PROVENANCE_WARNING` | Show that the value exists but its source, license, or review status is missing, weak, or unresolved. | Do not treat a value as public or reliable simply because it is present. |
| `ASSUMPTION_WARNING` | Keep user/model assumptions visible during editing, solving, result review, and reporting. | Do not upgrade assumptions into approved engineering facts. |
| `NONLINEAR_WARNING` | Surface convergence, active-set, gap, lift-off, or friction-state uncertainty when present. | Do not hide uncertainty behind clean-looking result visuals. |
| `IP_BOUNDARY_WARNING` | Warn, block, quarantine, or route to human review for public contribution/report/export risk. | Do not copy protected standards or private project data into public artifacts. |

<!-- sow-source-end -->

### CLM-029 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":35,"line_start":28,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-029"} -->
##### Trade-offs

- Blocking too early can interrupt modeling, but blocking too late can make incomplete engineering states look valid. Prefer allowing model editing while clearly blocking solve or rule-check actions that lack required data.
- A warning list alone is insufficient for engineering review. Future UX should also mark affected model objects/results so the user can locate the issue.
- Severity and class should not rely on color alone; future accessibility work in DEL-07-06 should cover keyboard navigation, screen-reader labels, contrast, and review workflow usability.
- Implementation should avoid duplicating warning logic in UI state. The GUI should consume application-service diagnostics/result envelopes and present them faithfully.
- Exact placement and copy for editor panels, solve execution, result review, report preview, and export controls remain `TBD` for future GUI implementation. This setup fixes warning semantics, not component layout.

<!-- sow-source-end -->

### CLM-030 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":43,"line_start":36,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-030"} -->
##### Examples

The following are invented behavioral examples, not standards-derived cases:

- A component has enough user-entered geometry for mechanics but lacks a private rule-pack required allowable. The GUI may show mechanics results while marking the rule check as blocked with `RULE_CHECK_BLOCKING`.
- A support definition is missing stiffness or restraint direction needed by the solver. The GUI blocks the affected solve path with `SOLVE_BLOCKING` and leaves the missing field visible.
- A value is present but has `source_location = TBD` or unresolved redistribution status. The GUI shows `PROVENANCE_WARNING` or `IP_BOUNDARY_WARNING` depending on the affected workflow.

<!-- sow-source-end -->

### CLM-031 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":49,"line_start":44,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-031"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified during setup. | N/A | N/A | N/A | N/A | TBD |

<!-- sow-source-end -->

### CLM-032 — D-41 R5 T7 PDU-054 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":52,"line_start":50,"source_sha256":"67c8d67ae427609a5cef4c9aa2a3fa3ad0544eabaa75d8d873d8c82c7741d8ec","target_id":"CLM-032"} -->
##### D-41 R5 T7 PDU-054 current declaration

Earlier setup-era statements on this surface are retained as historical setup context where applicable; this section is the active current-state declaration. The missing-data warning/blocking panel is implemented, including current nonlinear-visibility behavior. It presents existing diagnostics and does not synthesize engineering inputs, resolve warnings, or confer professional approval.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-022 OBJ-006 OBJ-011 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
