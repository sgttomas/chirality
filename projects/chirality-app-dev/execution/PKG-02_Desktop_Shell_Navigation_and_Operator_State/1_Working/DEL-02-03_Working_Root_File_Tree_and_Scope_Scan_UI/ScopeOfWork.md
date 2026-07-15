---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-03
package_id: PKG-02
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
project_scope_refs: [SOW-002, SOW-003]
package_objective_refs: [OBJ-001, OBJ-006]
---

# Scope of Work — DEL-02-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-02-03` in service of project scope [SOW-002, SOW-003] and package objectives [OBJ-001, OBJ-006].

- **OUT-001** — Working-root file-tree and scope-scan UI contract for DEL-02-03, traceable to SOW-002, SOW-003, OBJ-001, and OBJ-006.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-02-03 Working Root File Tree and Scope Scan UI

> #### Datasheet: DEL-02-03 Working Root File Tree and Scope Scan UI
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value | Source |
> |---|---|---|
> | DecompositionVariant | SOFTWARE_DECOMP | `_CONTEXT.md` |
> | DecompositionRevision | v3.2 | `_CONTEXT.md` |
> | PackageID | PKG-02 | `_CONTEXT.md` |
> | PackageName | Desktop Shell, Navigation, and Operator State | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-02 |
> | DeliverableID | DEL-02-03 | `_CONTEXT.md` |
> | DeliverableName | Working Root File Tree and Scope Scan UI | `_CONTEXT.md` |
> | ResponsibleParty | TBD | `_CONTEXT.md` |
> | Type | UX_UI_SLICE | `_CONTEXT.md` |
> | ContextEnvelope | M | `_CONTEXT.md` |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary UI responsibility | Working-root selector integration, bounded file tree display, deliverable summaries, and scan-state feedback | `_CONTEXT.md`; decomposition row for DEL-02-03 |
> | Covered scope items | SOW-002, SOW-003 | `_CONTEXT.md`; decomposition SOW ledger |
> | Supported objectives | OBJ-001, OBJ-006 | `_CONTEXT.md`; decomposition row for DEL-02-03 |
> | Anticipated artifacts | File tree panel; deliverable summary widgets; scope scan integration | `_CONTEXT.md`; decomposition row for DEL-02-03 |
> | Workspace APIs surfaced by this UI | `/api/working-root/validate`, `/api/working-root/tree`, `/api/working-root/scope`, `/api/project/deliverables` | `docs/SPEC.md` §17.2; `docs/PRD.md` §13 |
> | Scope mode vocabulary consumed by scan UI | `DELIVERABLES`, `KNOWLEDGE_TYPES` | `docs/TYPES.md` §8.2 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Working root validity | Must be an absolute existing directory, readable and writable by the app, and not inside the instruction root | `docs/SPEC.md` §1.2; `docs/PRD.md` FR-003 |
> | File tree traversal | Must be bounded; tree API skips `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`; inaccessible directories mark truncation | `docs/PRD.md` FR-004 |
> | Dynamic selection behavior | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selection state | `docs/PRD.md` FR-013 |
> | Scan runaway protection | File scans enforce depth/count limits | `docs/PRD.md` NFR-012 |
> | Authority boundary | UI consumes workspace APIs but remains presentation-focused | `_CONTEXT.md`; decomposition row for DEL-02-03 |
> | Source warning | PRD expected and observed PRD hashes match under D-APP-38; content using PRD is accepted for this run only as a warned source | `_REFERENCES.md`; dispatch instruction |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected construction detail | Source |
> |---|---|---|
> | Working-root selector integration | Allow path entry, Electron folder selection, apply, and clear actions; clearing the root disables runtime actions that require `projectRoot` | `docs/PRD.md` §7.1 and FR-002 |
> | File tree panel | Render selected working root through bounded tree API results, including skipped and inaccessible/truncated directory feedback | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2 |
> | Scope scan integration | Consume scope scan results for deliverables and knowledge-type directories without inventing missing project truth | `docs/SPEC.md` §17.2; `docs/TYPES.md` §8.2 |
> | Deliverable summary widgets | Present deliverable identity, status/dependency snapshots where available, and routeable deliverable rows for TASK workflows | `docs/PRD.md` §7.2; `docs/PRD.md` FR-010, FR-012 |
> | Error feedback | Surface typed validation and scan errors in the UI; exact error copy is TBD | `docs/PRD.md` FR-003, NFR-009 |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | SectionRef | Use |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | §§2, 5, 6 | Working-root truth and instruction-root separation context |
> | REF-002 | `docs/CONTRACT.md` | K-HIER-1, K-ID-1, K-PATH-1, K-FS-1, K-INVENT-1 | Governance invariants for identity, path, and unknowns |
> | REF-003 | `docs/SPEC.md` | §§1.2, 3.1, 17.2 | Working-root rules, deliverable files, workspace APIs |
> | REF-004 | `docs/TYPES.md` | §§1.1-1.2, 8.2 | Package/deliverable and task-scope vocabulary |
> | REF-006 | `docs/PRD.md` | §§7.1-7.2, 8.1, 13, 11.2 | User journeys, functional requirements, endpoint targets, scan limits |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PKG-02 row; DEL-02-03 row; SOW ledger | Deliverable identity and decomposition scope |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-02-03 Working Root File Tree and Scope Scan UI

> #### Specification: DEL-02-03 Working Root File Tree and Scope Scan UI
>

### CLM-008 — Scope

> ##### Scope
>
> DEL-02-03 covers the UI slice that connects the desktop shell to working-root selection, validation feedback, bounded file-tree browsing, deliverable summaries, and scan-state feedback.
>
> Included:
>
> - Working-root selector integration in the desktop shell.
> - Presentation of bounded file tree data for the selected working root.
> - Presentation of scope scan results for deliverables and knowledge-type directories.
> - Deliverable summary widgets sufficient for operator routing and read-only inspection.
> - UI handling for root changes, stale scan selections, invalid roots, and scan truncation.
>
> Excluded:
>
> - Runtime engine internals.
> - Filesystem policy enforcement internals owned by PKG-07.
> - Dependency extraction; `Dependencies.csv` creation is deferred.
> - Domain-engine future-scope behavior.
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-02 and DEL-02-03; `docs/PRD.md` §§7.1, 8.1, 13.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ReqID | Requirement | Source |
> |---|---|---|
> | DEL-02-03-REQ-001 | The UI shall expose working-root selection globally through path entry, Electron folder selection, apply, and clear controls. | `docs/PRD.md` FR-002 |
> | DEL-02-03-REQ-002 | The UI shall present validation failures for non-absolute, missing, inaccessible, non-directory, or instruction-root-contained paths. | `docs/PRD.md` FR-003; `docs/SPEC.md` §1.2 |
> | DEL-02-03-REQ-003 | Clearing the working root shall disable runtime actions that require `projectRoot`. | `docs/PRD.md` §7.1 |
> | DEL-02-03-REQ-004 | The UI shall render a bounded file tree for the selected working root using the workspace tree API. | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2 |
> | DEL-02-03-REQ-005 | File tree presentation shall account for skipped directories `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`. | `docs/PRD.md` FR-004 |
> | DEL-02-03-REQ-006 | File tree presentation shall indicate inaccessible directories or truncation when reported by the API. | `docs/PRD.md` FR-004 |
> | DEL-02-03-REQ-007 | Scope scan UI shall present deliverables and knowledge-type directories without treating UI-local state as project truth. | `docs/SPEC.md` §17.2; `docs/CONTRACT.md` K-FS-1; `docs/TYPES.md` §8.2 |
> | DEL-02-03-REQ-008 | Dynamic scope scan state shall clear invalid selections when the root changes, deliverables are removed, knowledge markers are disabled, or knowledge targets become stale. | `docs/PRD.md` FR-013 |
> | DEL-02-03-REQ-009 | Deliverable summary widgets shall support routing to PIPELINE `TASK*` with a deliverable preselected when deliverables are present. | `docs/PRD.md` §7.2 |
> | DEL-02-03-REQ-010 | The UI shall consume status and dependency contract snapshots read-only where applicable; transition controls belong only where supported by the active workflow. | `docs/PRD.md` FR-010 |
> | DEL-02-03-REQ-011 | Scan and workspace errors surfaced by the UI shall preserve typed-error information where available. | `docs/PRD.md` NFR-009 |
> | DEL-02-03-REQ-012 | File and scope scans shall avoid runaway traversal by respecting bounded depth/count behavior exposed by the runtime. | `docs/PRD.md` NFR-012 |
> | DEL-02-03-REQ-013 | Stable deliverable IDs, not folder labels alone, shall drive deliverable identity in summary widgets and route targets. | `docs/CONTRACT.md` K-ID-1, K-PATH-1; `docs/TYPES.md` §1.2 |
> | DEL-02-03-REQ-014 | ASSUMPTION: The UI should not expose dependency extraction as part of this deliverable; dependency extraction remains a later `TASK + dependency-extract` step. | `_DEPENDENCIES.md`; dispatch instruction |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Authority | Applicability | Source |
> |---|---|---|
> | Working-root contract | Governs selected root validity, containment, and project-truth placement | `docs/SPEC.md` §1.2; `docs/CONTRACT.md` K-ROOT/K-FS surfaces |
> | Workspace API contract | Defines the read endpoints this UI consumes | `docs/SPEC.md` §17.2 |
> | PRD current product scope | Establishes working-root selection, file-tree browsing, deliverable scanning, and lifecycle/dependency contract API support as current scope | `docs/PRD.md` §6.2 |
> | Unknown-value discipline | Unsupported facts remain `TBD` rather than guesses | `docs/CONTRACT.md` K-INVENT-1 |
>

### CLM-011 — Verification

> ##### Verification
>
> | ReqID | Verification Approach |
> |---|---|
> | DEL-02-03-REQ-001 | UI test or manual acceptance showing type path, choose folder, apply, and clear states. |
> | DEL-02-03-REQ-002 | API/UI integration tests with invalid root cases and typed error display checks. |
> | DEL-02-03-REQ-003 | State test confirming root-dependent actions become disabled after clear. |
> | DEL-02-03-REQ-004 | API/UI integration test with representative tree data from `/api/working-root/tree`. |
> | DEL-02-03-REQ-005 | Fixture tree test proving skipped directories are absent or marked according to API shape. |
> | DEL-02-03-REQ-006 | Fixture or mocked response test for inaccessible/truncated directory indicators. |
> | DEL-02-03-REQ-007 | Scope scan fixture test using deliverables and knowledge-type directories. |
> | DEL-02-03-REQ-008 | State reset tests for root change, removed deliverable, disabled knowledge marker, and stale target cases. |
> | DEL-02-03-REQ-009 | Routing test from deliverable row to PIPELINE `TASK*` preselection. |
> | DEL-02-03-REQ-010 | Read-only contract snapshot rendering test; transition-control behavior TBD by owning workflow. |
> | DEL-02-03-REQ-011 | Error rendering test preserving type/status/message/details where available. |
> | DEL-02-03-REQ-012 | Runtime/API tests own depth/count enforcement; UI test verifies bounded-result feedback. |
> | DEL-02-03-REQ-013 | Rename/path-label fixture test confirming route identity uses stable deliverable ID. |
> | DEL-02-03-REQ-014 | Review check confirming no `Dependencies.csv` is created by this deliverable. |
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required deliverable artifacts:
>
> - File tree panel.
> - Deliverable summary widgets.
> - Scope scan integration.
> - UI tests or acceptance notes for selector, scan, truncation, stale-selection reset, and deliverable routing.
>
> TBD:
>
> - Exact component/module paths.
> - Exact API response shape details for skipped-directory, truncation, and inaccessible-directory markers.
> - Exact status/dependency summary widget fields; unsupported fields remain deferred rather than inferred.
>

### CLM-013 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | B-001 | Converted to `TBD` / already covered: implementation-level component paths, API field names, and UI copy remain unresolved. | `Specification.md` Documentation; `Guidance.md` Human-Ruling Needed; `Procedure.md` Steps. |
> | X-001 | Incorporated as `TBD`: skipped-directory response-shape details were added to the API response shape unknowns. | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2. |
> | X-002 | Already covered: verification binds error rendering to preserving type/status/message/details where available. | `docs/PRD.md` NFR-009; `Specification.md` Verification for DEL-02-03-REQ-011. |
> | E-001 | Converted to `TBD` / deferred: exact status/dependency summary fields remain unresolved and unsupported fields must not be inferred. | `docs/PRD.md` FR-010; `docs/SPEC.md` §17.2. |
>

### CLM-014 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-108 supersedes run-scoped extraction deferral wording: the nine-row derivative register exists; the file-tree UI still does not own dependency extraction.
>

### CLM-015 — D-APP-56 launcher confirmation (2026-07-12)

> ##### D-APP-56 launcher confirmation (2026-07-12)
>
> R4-P29 confirms that the portal deliverable-rows launcher is within the existing DEL-02-03 REQ-009 claim. This is an ownership confirmation, not a new lifecycle or implementation claim.

- **AC-001** — The DEL-02-03 Scope of Work preserves every legacy source range and its traceability to SOW-002, SOW-003, OBJ-001, and OBJ-006 without changing lifecycle, dependency, or authority state.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-02-03 Working Root File Tree and Scope Scan UI

> #### Procedure: DEL-02-03 Working Root File Tree and Scope Scan UI
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-017 — Purpose

> ##### Purpose
>
> Define the working procedure to produce and verify the Working Root File Tree and Scope Scan UI slice without expanding into filesystem enforcement, dependency extraction, or runtime engine internals.
>

### CLM-018 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Note | Source |
> |---|---|---|
> | Accepted SOFTWARE_DECOMP v3.2 entry for DEL-02-03 | Available | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
> | Working-root validation API contract | Available at contract level; implementation details TBD | `docs/SPEC.md` §17.2; `docs/PRD.md` FR-003 |
> | File-tree API contract | Available at contract level; response shape details TBD | `docs/SPEC.md` §17.2; `docs/PRD.md` FR-004 |
> | Scope-scan API contract | Available at contract level; response shape details TBD | `docs/SPEC.md` §17.2; `docs/PRD.md` FR-013 |
> | Declared upstream dependencies | TBD; no accepted dependency edges extracted yet | `_DEPENDENCIES.md` |
> | PRD source hash acceptance | Human ruling needed; mismatch is warning for this run | `_REFERENCES.md`; dispatch instruction |
>

### CLM-019 — Steps

> ##### Steps
>
> 1. Confirm the active deliverable identity.
>    - Use `PackageID=PKG-02` and `DeliverableID=DEL-02-03` as stable identity.
>    - Preserve `ResponsibleParty: TBD`.
>    - If folder labels disagree with stable IDs, surface the mismatch rather than renaming during this deliverable.
>
> 2. Wire or verify working-root selector integration.
>    - Provide path entry, folder selection, apply, and clear controls.
>    - On apply, call the working-root validation surface.
>    - On clear, remove selected-root dependent UI state and disable root-dependent runtime actions.
>
> 3. Render working-root validation feedback.
>    - Show failures for non-absolute, missing, inaccessible, non-directory, or instruction-root-contained paths.
>    - Preserve typed-error details when available.
>    - Use exact error copy from implementation or UX source when available; otherwise mark copy as `TBD`.
>
> 4. Render the bounded file tree.
>    - Consume `/api/working-root/tree` or the local equivalent.
>    - Display tree nodes within the bounded result set.
>    - Reflect skipped, inaccessible, or truncated directories when represented in the API result.
>    - Do not perform unbounded renderer-side traversal.
>
> 5. Integrate scope scan results.
>    - Consume `/api/working-root/scope` or the local equivalent.
>    - Present deliverables and knowledge-type directories using canonical scope vocabulary.
>    - Clear invalid selections after root changes, removed deliverables, disabled knowledge markers, or stale knowledge targets.
>
> 6. Add deliverable summary widgets.
>    - Show stable deliverable ID, name, package context, lifecycle state where available, and dependency snapshot status where available.
>    - Route deliverable rows to PIPELINE `TASK*` with the deliverable preselected when supported.
>    - Keep dependency extraction deferred; do not create `Dependencies.csv` as part of this procedure.
>
> 7. Verify ownership boundaries.
>    - Confirm UI code consumes workspace APIs rather than duplicating filesystem policy enforcement.
>    - Confirm runtime/filesystem deliverables retain ownership of path containment, traversal bounds, status parsing, dependency parsing, and lifecycle transition enforcement.
>
> 8. Record unresolved facts.
>    - Mark missing implementation details as `TBD`.
>    - Raise source/path/hash conflicts for human ruling.
>

### CLM-020 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | Working-root selection | Path entry, folder selection, apply, and clear states are available. |
> | Invalid root feedback | Invalid roots produce visible feedback with typed-error information where available. |
> | Clear root behavior | Root-dependent actions and stale scope selections are disabled or cleared. |
> | File tree bounds | Skipped directories and truncation/inaccessible indicators match API behavior. |
> | Scope scan reset | Removed or stale deliverable/knowledge selections are cleared. |
> | Deliverable routing | Deliverable summary row routes to PIPELINE `TASK*` with stable deliverable identity. |
> | Project truth boundary | UI state is not treated as authoritative project truth. |
> | Dependency deferral | No `Dependencies.csv` is created by this deliverable procedure. |
> | Unknown discipline | Unsupported facts remain `TBD`, `ASSUMPTION`, conflict, or human-ruling-needed. |
> | Acceptance evidence | Test or acceptance evidence for selector, invalid-root feedback, bounded tree behavior, scope reset, and deliverable routing is required; evidence artifact location is TBD until implementation/test output exists. |
>

### CLM-021 — Records

> ##### Records
>
> - UI implementation artifacts: file tree panel, deliverable summary widgets, scope scan integration.
> - Test or acceptance evidence for root selection, invalid root display, bounded tree behavior, scope reset behavior, and deliverable routing; artifact location TBD.
> - Conflict/human-ruling record for package-folder label MATCH and PRD hash status: MATCH. (reconciled under D-APP-38).
> - This four-document kit: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
>

### CLM-022 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | F-001 | Incorporated as required evidence with `TBD` artifact location: Procedure now preserves acceptance evidence as required without implying it already exists. | `Procedure.md` Verification and Records; `Specification.md` Verification. |
>

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-108 supersedes run-scoped extraction deferral wording: the nine-row derivative register exists; the file-tree UI still does not own dependency extraction.

- **VER-001** — Run deterministic schema validation, complete source mapping and parity checks, repeated checklist derivation and render stability checks, then conduct human review against the accepted legacy basis.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-02-03 Working Root File Tree and Scope Scan UI

> #### Guidance: DEL-02-03 Working Root File Tree and Scope Scan UI
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-025 — Purpose

> ##### Purpose
>
> This deliverable gives the operator a trustworthy, bounded view of the selected working root and the scanned deliverable scope. It supports the desktop shell by making filesystem project truth visible enough for routing and inspection while leaving enforcement and data mutation to the runtime and workflow-specific APIs.
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §DEL-02-03; `docs/PRD.md` §§7.1-7.2 and FR-002 through FR-004.
>

### CLM-026 — Principles

> ##### Principles
>
> - Treat the filesystem as project truth: render what the workspace APIs report; do not create hidden UI-only project truth. Source: `docs/CONTRACT.md` K-FS-1; `docs/PRD.md` §5.
> - Preserve stable identity: deliverable summaries and routing should key on deliverable IDs, not mutable labels or paths alone. Source: `docs/CONTRACT.md` K-ID-1, K-PATH-1.
> - Keep enforcement in the runtime: the UI should surface validation, containment, and scan-limit outcomes, while PKG-07/runtime slices own the underlying filesystem policy. Source: `_CONTEXT.md`; `docs/SPEC.md` §1.2; decomposition SOW-002 note.
> - Prefer visible boundedness over silent omission: skipped directories, inaccessible nodes, and truncated scans should be visible enough for operator judgment when the API reports them. Source: `docs/PRD.md` FR-004, NFR-012.
> - Reset stale operator choices: root and scan changes must clear invalid selections rather than carrying stale scope into TASK dispatch. Source: `docs/PRD.md` FR-013.
> - Keep unsupported facts as `TBD`: exact component paths, response field names, and UI copy require source or implementation confirmation. Source: `docs/CONTRACT.md` K-INVENT-1.
>

### CLM-027 — Considerations

> ##### Considerations
>
> - Working-root validation is a shared boundary. DEL-02-03 should integrate with validation feedback, but the security-control implementation is attributed to DEL-07-01 by the decomposition SOW ledger.
> - Scope scan results bridge PKG-02 and PKG-07. The UI is responsible for presentation and selection behavior; deterministic filesystem scanning and contract data belong to runtime/filesystem deliverables.
> - Deliverable summaries may need to show `_STATUS.md` and dependency snapshot information, but dependency extraction is explicitly deferred for this run.
> - The PRD source has a recorded hash status: MATCH. Use PRD requirements as warned local source material for this run; do not treat the MATCH as resolved. (reconciled under D-APP-38).
> - The dispatch path named `PKG-02_Desktop_UI_and_Local_Experience`, but the accessible scaffolded folder is `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. Stable IDs match; package folder-name mismatch needs human confirmation.
>

### CLM-028 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance | Source |
> |---|---|---|
> | Dense scan UI vs. operator clarity | Favor a dense but readable operational panel; avoid hiding truncation or invalid-selection states behind decorative UI. | `docs/PRD.md` FR-006, FR-013 |
> | UI convenience state vs. project truth | Local UI state can remember view preferences, but project truth remains in working-root files and accepted git history. | `docs/DIRECTIVE.md` §2; `docs/CONTRACT.md` K-FS-1 |
> | Presentation ownership vs. runtime ownership | DEL-02-03 should not duplicate root validation, scan traversal, dependency parsing, or lifecycle transition logic; it should consume and represent API results. | `_CONTEXT.md`; `docs/SPEC.md` §17.2 |
> | Deliverable display by path vs. ID | Use paths for navigation context, but use stable IDs for identity and dispatch preselection. | `docs/CONTRACT.md` K-ID-1, K-PATH-1 |
>

### CLM-029 — Examples

> ##### Examples
>
> | Scenario | Expected UI behavior | Source |
> |---|---|---|
> | User clears the working root | Root-dependent runtime actions become disabled and stale scope selections clear. | `docs/PRD.md` §7.1, FR-013 |
> | Tree API reports skipped folders | The file tree omits or marks skipped folders according to API output; skipped set includes `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`. | `docs/PRD.md` FR-004 |
> | Scope scan no longer contains selected deliverable | The prior selection is cleared rather than dispatched. | `docs/PRD.md` FR-013 |
> | Deliverables are present | A deliverable row can route to PIPELINE `TASK*` with that deliverable preselected. | `docs/PRD.md` §7.2 |
>

### CLM-030 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | DEL-02-03-CONFLICT-001 | Dispatch path uses stale package folder label `PKG-02_Desktop_UI_and_Local_Experience`; scaffolded folder uses `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. | Dispatch brief `DeliverablePath / ScopePath` | `_CONTEXT.md`; `docs/CONTRACT.md` K-ID-1/K-PATH-1; decomposition PKG-02 | Datasheet Identification; run record; final report | Treat stable IDs `PKG-02` and `DEL-02-03` plus accessible scaffold as controlling for this run. | TBD |
> | DEL-02-03-CONFLICT-002 | PRD hash status: MATCH exists for REF-006. | `_REFERENCES.md` expected/actual hash row for REF-006 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | All PRD-derived requirements | Proceed with warned PRD source for P1/P2 drafting; leave hash acceptance unresolved. | TBD — reconciled under D-APP-38 |
>

### CLM-031 — Human-Ruling Needed

> ##### Human-Ruling Needed
>
> - Confirm whether the package-folder label mismatch should be normalized, renamed, or left as a path-history artifact.
> - Resolve or explicitly accept the PRD hash status: MATCH for future closure. (reconciled under D-APP-38).
> - Confirm exact UI component/module paths and API response field names before implementation-level acceptance.
>

### CLM-032 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | A-001 | Already covered as conflict: the package-folder label mismatch remains in the Conflict Table for human ruling. | `Guidance.md` Conflict Table; `_CONTEXT.md` Identity; `docs/CONTRACT.md` K-ID-1/K-PATH-1. |
> | X-003 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; `Guidance.md` Conflict Table; `Datasheet.md` Conditions; `Procedure.md` Prerequisites. — reconciled under D-APP-38 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-002 SOW-003 OBJ-001 OBJ-006 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
