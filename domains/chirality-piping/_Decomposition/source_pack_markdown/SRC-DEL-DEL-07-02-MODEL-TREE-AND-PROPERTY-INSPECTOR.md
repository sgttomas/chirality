# Source Pack: SRC-DEL-DEL-07-02-MODEL-TREE-AND-PROPERTY-INSPECTOR

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-02_Model tree and property inspector/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-02_Model tree and property inspector/Datasheet.md

### Datasheet: DEL-07-02 Model tree and property inspector

#### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-07-02 |
| Package ID | PKG-07 |
| Package | Graphical User Interface and Engineering Workflow |
| Type | UX_UI_SLICE |
| Scope items | SOW-020, SOW-021 |
| Objective | OBJ-006 |
| Context envelope | M |
| Anticipated artifacts | model tree; property inspector; UI tests |

#### Attributes

| Attribute | Setup value |
|---|---|
| UI surface | Single GUI work surface for tree navigation and selected-entity property inspection. |
| Primary entities | Project, Model, Node, Element, Component, Material, Section, Support, LoadCase, Combination, RulePackRef, Result, and diagnostics where applicable. |
| GUI baseline | Tauri 2 desktop shell, TypeScript/React/Vite GUI, and Three.js viewport where viewport-facing. Exact component and state libraries are `TBD`. |
| State boundary | Durable project/model state is separate from transient session, viewport, selection, and job-progress state. GUI mutations route through application-service commands. |
| Missing-data posture | Missing solve-required and rule-check-required values are surfaced as explicit findings, not defaulted silently. |
| Data boundary | Private project, material, component, and rule-pack data remain user-controlled and are not transmitted or committed publicly by default. |

#### Conditions

| Condition | Status |
|---|---|
| Tree hierarchy and grouping rules | `TBD`; must be derived from accepted domain/schema contracts, not invented in this setup pass. |
| Property editor field inventory | `TBD`; must preserve unit-bearing fields, provenance, private/public status, and missing-data findings. |
| Selection synchronization contract | `TBD`; must align model tree, property inspector, and 3D viewport selection without storing transient state as durable model state. |
| Command/query contract | `TBD`; edits must route through application-service commands and reads through governed queries or result envelopes. |
| UI tests | `TBD`; future tests should cover tree navigation, selection, editable/read-only property state, missing-data visibility, and protected/private data boundaries. |

#### Construction

This setup kit describes the future UI slice boundary only. It does not implement product UI, edit GUI source files, choose unresolved UI libraries, create tests, introduce engineering default values, or move any artifact to `ISSUED`.

The future model tree and property inspector are expected to consume accepted schema/service contracts for object identity, unit-bearing fields, provenance, diagnostics, rule-pack/private-library status, and command/query/result-envelope behavior. Missing or unresolved engineering data remains visible as `TBD` or diagnostic state.

#### Setup Slot Checklist

| Slot | Setup status | Owner/source status |
|---|---|---|
| Tree grouping and hierarchy rules | `TBD` | Expected from accepted domain/schema and GUI state contracts. |
| Inspector field inventory | `TBD` | Expected from accepted domain/schema contracts for model entities and library references. |
| Unit display and edit hooks | `TBD` | Expected from accepted unit and command/query contracts. |
| Provenance and redistribution/private-status display | `TBD` | Expected from material/component/rule-pack/library contracts. |
| Diagnostic classes and affected-object display | `TBD` | Expected from diagnostics/result-envelope contract. |
| Fixture, screenshot, and UI test data policy | `TBD` | Must remain synthetic, public-domain, or otherwise cleared. |

#### References

- `_CONTEXT.md` for deliverable identity, scope, artifacts, and architecture-basis injection.
- `docs/_Registers/Deliverables.csv` row `DEL-07-02`.
- `docs/_Registers/ScopeLedger.csv` rows `SOW-020` and `SOW-021`.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7, `PKG-07`, `OBJ-006`, and architecture basis IDs `AB-00-03`, `AB-00-05`, `AB-00-06`, `AB-00-07`, and `AB-00-08`.
- `docs/CONTRACT.md` invariants `OPS-K-DATA-1`, `OPS-K-DATA-2`, `OPS-K-DATA-3`, `OPS-K-UNIT-1`, `OPS-K-RULE-1`, `OPS-K-RULE-3`, `OPS-K-PRIV-1`, `OPS-K-PRIV-2`, `OPS-K-IP-1`, `OPS-K-IP-2`, `OPS-K-IP-3`, and `OPS-K-AGENT-1..4`.
- `docs/SPEC.md` sections 1, 3, 6, 7, 10, and 11.
- `docs/TYPES.md` sections 3, 4, 5, 6, 7, 8, and 9.

#### Open Setup Questions

| Question | Status |
|---|---|
| Which accepted schema version supplies the property inspector field inventory? | `TBD` |
| Which GUI state library, if any, is accepted for transient selection and inspector state? | `TBD` |
| Which application-service commands and queries are accepted for model tree edits and property reads? | `TBD` |
| Which diagnostics contract shape is accepted for inline missing-data and provenance warnings? | `TBD` |
| Which UI test framework conventions apply to this slice beyond the architecture-basis Playwright/Vitest expectation? | `TBD` |

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-02_Model tree and property inspector/Guidance.md

### Guidance: DEL-07-02 Model tree and property inspector

#### Purpose

This deliverable exists to bound the navigation and inspection work surface for the OpenPipeStress GUI. The future implementation should help users see model structure, selected-entity data, missing inputs, assumptions, provenance, and private/rule-pack status early in the workflow.

#### Principles

- Treat the model tree as navigation and visibility, not a second durable model store.
- Route edits through application-service commands and keep selection, expansion, filtering, and panel focus as transient GUI state.
- Show missing solve-required and rule-check-required values as explicit findings instead of silently filling defaults.
- Preserve unit and provenance context for editable engineering fields.
- Keep rule-pack checks, private-library values, and professional acceptance distinct from the open mechanics model.
- Keep implementation choices that remain unresolved, including component/state libraries and exact command/query names, as `TBD`.

#### Considerations

The tree and inspector will likely depend on upstream domain schema, persistence, command/query/job envelope, diagnostics, rule-pack, material/component/library, unit, and GUI state contracts. This setup pass records those dependencies but does not resolve them.

The inspector should support workflows that make engineering gaps visible before solve execution or rule checking. It should not turn missing code-specific, material, component, SIF/flexibility, allowable, or rule-pack values into public defaults. Private project and library data should remain local/user-controlled unless a later export or contribution path is explicitly authorized with documented rights.

#### Trade-offs

| Topic | Guidance |
|---|---|
| Tree richness vs scope control | Include the navigation and inspection concepts needed by DEL-07-02, but leave specialized editors to DEL-07-03 and missing-data blocking UX to DEL-07-04 unless an accepted brief expands scope. |
| Convenience vs data boundary | Do not prefill protected/code-specific values for convenience; use visible `TBD`, diagnostics, or incomplete-state UI. |
| Selection state vs durable data | Keep current selection, tree expansion, filters, and panel focus out of durable project state unless a persistence contract later authorizes a view-state record. |
| Editable inspector vs command boundary | Inspector edits should be command-backed and validation-aware; direct mutation of durable model objects from UI state should be avoided. |
| Rule status vs professional judgment | Show user-rule/check readiness or diagnostics only as software findings; do not present them as professional code compliance. |

#### Boundary Rationale

The inspector is a convenience surface over governed model and service contracts. Command-backed edits keep validation, unit checks, diagnostics, provenance handling, undo/redo scope, and result-envelope behavior in the application-service boundary instead of allowing UI state to become an alternate authority.

The split with adjacent GUI deliverables remains explicit: DEL-07-02 owns navigation and selected-entity inspection setup, DEL-07-03 owns specialized material/component/rule-pack editor implementation, and DEL-07-04 owns missing-data warning and blocking UX unless a later sealed brief or human ruling changes that boundary.

#### Examples

Concrete UI examples, screenshots, and fixtures are `TBD`. Future examples must use synthetic, public-domain, or otherwise cleared model data and must not reproduce protected standards content, proprietary project data, or protected code examples.

#### Conflict Table (for human ruling)

| Conflict ID | Issue | Contenders | Human ruling |
|---|---|---|---|
| None | No setup conflict found. | N/A | N/A |

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-02_Model tree and property inspector/Procedure.md

### Procedure: DEL-07-02 Model tree and property inspector

#### Purpose

Define the bounded procedure for a future implementation task to produce and verify the model tree and property inspector without expanding scope during this setup pass.

#### Prerequisites

- Confirm the sealed brief names `DEL-07-02` and the approved implementation write scope before any GUI source or test file is edited.
- Confirm upstream architecture basis constraints from `AB-00-03`, `AB-00-05`, `AB-00-06`, `AB-00-07`, and `AB-00-08`.
- Confirm accepted domain/schema contracts for entity identity, unit-bearing values, provenance, diagnostics, rule-pack references, and private-library references.
- Confirm accepted application-service command/query contracts for inspector edits and tree/selection reads.
- Confirm all UI fixtures, screenshots, and examples are synthetic, public-domain, or otherwise cleared for repository use.

#### Steps

1. Re-read `_CONTEXT.md`, `Specification.md`, `_DEPENDENCIES.md`, and any accepted upstream schema/service contracts.
2. Identify the entity types and field groups that DEL-07-02 owns for tree navigation and selected-entity inspection.
3. Define tree-to-viewport-to-inspector selection behavior using transient GUI state and stable model identities.
4. Define property inspector read-only/editable states and command-backed mutation paths.
5. Preserve unit display/edit hooks, dimensional validation, provenance, private/public status, and rule-pack checksum/source status in the inspector where relevant.
6. Add visible findings for missing solve-required inputs, missing rule-check inputs, provenance warnings, assumptions, and IP-boundary warnings without creating defaults.
7. Implement the UI slice only after a separate implementation brief authorizes GUI source and test edits.
8. Add UI tests for tree navigation, selection synchronization, inspector field groups, missing-data visibility, provenance/private status, and command/query boundary behavior.

#### Verification

| Check | Expected evidence |
|---|---|
| Scope boundary | Changes are limited to the approved implementation scope for DEL-07-02. |
| Tree/selection behavior | UI tests confirm model tree selection updates the inspector and stays aligned with stable model identity. |
| Inspector behavior | UI tests confirm selected entity type controls visible field groups and command-backed edit behavior. |
| Missing-data behavior | UI tests confirm missing solve-required and rule-check-required values are explicit findings. |
| Unit/provenance behavior | Tests or review evidence confirm unit, provenance, checksum, and private/public status are not dropped. |
| IP/privacy boundary | Fixtures and UI text contain no protected standards content, proprietary values, private project data, or compliance claims. |

#### Records

- Implementation notes or pull request summary when code work is authorized.
- UI test results.
- Command/query boundary review evidence.
- Fixture and screenshot provenance notes.
- Protected-content review evidence where applicable.
- Missing-data, provenance, and private-status UI evidence.
- Any human rulings for `TBD` items.

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-02_Model tree and property inspector/Specification.md

### Specification: DEL-07-02 Model tree and property inspector

#### Scope

This deliverable specifies setup evidence for the future model tree and property inspector GUI slice. It covers tree navigation, selected-entity property presentation/editing, selection synchronization with the 3D centerline workflow, missing-data visibility, provenance/private-data presentation, and UI test expectations at a setup level.

This setup pass does not implement GUI source, edit tests, select unresolved component/state libraries, introduce engineering defaults, embed protected standards content, or claim professional approval/code compliance.

#### Requirements

| Req ID | Requirement | Source basis | Verification hook |
|---|---|---|---|
| DEL-07-02-RQ-001 | The model tree shall expose navigation for centerline model entities and piping component visualization without duplicating durable model truth in transient UI state. | SOW-020; AB-00-05; docs/SPEC.md section 7 | Future UI tests for tree rendering, selection, and model identity consistency. |
| DEL-07-02-RQ-002 | The property inspector shall present selected-entity fields for materials, sections, components, load cases, supports, rule-pack references, and private-library references where this slice owns the inspector surface. | SOW-021; docs/SPEC.md sections 3 and 7 | Future UI tests for entity-specific inspector panels and read-only/editable state. |
| DEL-07-02-RQ-003 | Unit-bearing values shown or edited through the inspector shall preserve unit awareness and dimensional validation hooks. | OPS-K-UNIT-1; docs/TYPES.md object registry | Unit/display/edit validation tests once schema and service contracts are accepted. |
| DEL-07-02-RQ-004 | Missing solve-required or rule-check-required values shall be visible as findings and shall not be silently supplied by the tree, inspector, or UI defaults. | OPS-K-DATA-2; OBJ-006; docs/SPEC.md section 7 | Negative UI tests for missing physical inputs and missing rule-pack inputs. |
| DEL-07-02-RQ-005 | Provenance and redistribution/private status shall remain visible for materials, sections, components, and rule-pack references where inspector fields expose them. | OPS-K-DATA-3; OPS-K-RULE-3; OPS-K-PRIV-1; docs/TYPES.md sections 7 and 8 | UI tests for provenance/status display and private/public boundary indicators. |
| DEL-07-02-RQ-006 | GUI mutations from the property inspector shall route through application-service commands; tree/inspector reads shall use governed query or result-envelope boundaries. | AB-00-03; AB-00-05 | Service-boundary review and command/query interaction tests. |
| DEL-07-02-RQ-007 | Diagnostics shown in the inspector shall use governed diagnostic/result-envelope concepts and shall not claim certification, sealing, professional approval, or automatic code compliance. | AB-00-06; OPS-K-AGENT-4; docs/TYPES.md analysis statuses | Diagnostic presentation tests and protected/professional-claim review. |
| DEL-07-02-RQ-008 | Public examples, screenshots, fixtures, and test data for the UI slice shall not contain protected standards text, protected tables, proprietary commercial data, or private project data. | OPS-K-IP-1; OPS-K-IP-3; OPS-K-RULE-1; OPS-K-PRIV-1 | Protected-content and fixture provenance review. |

#### Standards

No protected standard text, protected tables, protected examples, material allowables, SIF/flexibility tables, proprietary component values, or proprietary project data are available in this deliverable-local setup context. Any future standards or owner-code basis must remain a private/user-supplied input or a non-protected pointer with provenance. Clause-level requirements are `TBD`.

#### Verification

| Verification area | Minimum setup expectation |
|---|---|
| Tree navigation | Tests should confirm tree nodes represent accepted model entities and preserve stable identity through selection. |
| Property inspector | Tests should confirm selected entity type controls visible field groups and editability. |
| Missing data | Tests should show missing solve-required and rule-check-required values remain visible and classified. |
| Unit safety | Tests should cover unit-bearing value display/edit pathways and dimensional validation failures once contracts exist. |
| Provenance/privacy | Tests should show provenance and private/public redistribution status are visible where relevant. |
| Command/query boundary | Tests or review evidence should show inspector edits do not bypass application-service commands. |
| Professional boundary | UI text, diagnostics, and fixtures must not claim code compliance, certification, approval, or sealing. |

#### Verification Coverage Slots

| Coverage slot | Required future evidence |
|---|---|
| Tree navigation and stable identity | UI test or review evidence that tree entries map to accepted model identities. |
| Selection synchronization | UI test or review evidence that tree, viewport, and inspector selection remain aligned without durable-state drift. |
| Inspector field groups | UI test or review evidence that selected entity type controls visible field groups and editability. |
| Transient/durable state split | Review evidence that selection, expansion, filters, and panel focus remain transient unless a persistence contract authorizes otherwise. |
| Command-backed edits | UI/service test or review evidence that inspector mutations route through application-service commands. |
| Missing-data visibility | Negative UI tests for solve-required and rule-check-required gaps. |
| Provenance/privacy visibility | UI tests or review evidence for provenance, checksum/source status, and private/public redistribution indicators. |
| Protected/professional-boundary review | Evidence that fixtures and UI text avoid protected data and compliance/certification claims. |

#### Documentation

Expected future artifacts, when implementation is separately authorized, are:

- model tree;
- property inspector;
- UI tests.

Exact source paths, component library, state library, schema version, command/query names, test filenames, and screenshot fixture policy are `TBD`.

#### Conflict Table (for human ruling)

| Conflict ID | Issue | Contenders | Human ruling |
|---|---|---|---|
| None | No source conflict identified in setup evidence. | N/A | N/A |
