---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-03
package_id: PKG-02
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
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
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
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
> | Workspace APIs surfaced by this UI | `/api/working-root/validate`, `/api/working-root/tree`, `/api/working-root/scope`, `/api/project/deliverables` | `docs/SPEC.md` §17.2; `docs/PRD.md` §9.2 |
> | Scope mode vocabulary consumed by scan UI | `DELIVERABLES`, `KNOWLEDGE_TYPES` | `docs/TYPES.md` §4.4 |
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
> | Source warning | D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. | `_REFERENCES.md`; dispatch instruction |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected construction detail | Source |
> |---|---|---|
> | Working-root selector integration | Per-chat typed path, native picker and known-folder selection before the first message; fixed folder identity thereafter. Folder-dependent actions remain unavailable without a valid folder under D-APP-120. | `docs/PRD.md` §7.1 and FR-002 |
> | File tree panel | Render selected working root through bounded tree API results, including skipped and inaccessible/truncated directory feedback | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2 |
> | Scope scan integration | Consume scope scan results for deliverables and knowledge-type directories without inventing missing project truth | `docs/SPEC.md` §17.2; `docs/TYPES.md` §4.4 |
> | Deliverable summary widgets | Present deliverable identity, status/dependency snapshots where available, and routeable deliverable rows for TASK workflows | `docs/PRD.md` §7.5; `docs/PRD.md` FR-010, FR-012 |
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
> | REF-004 | `docs/TYPES.md` | §§1.1-1.2, 4.4 | Package/deliverable and task-scope vocabulary |
> | REF-006 | `docs/PRD.md` | §§7.1, 7.5, 8.1, 9.2, 11.2 | User journeys, functional requirements, endpoint targets, scan limits |
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
> | DEL-02-03-REQ-001 | The UI SHALL select a folder per chat through typed path, known folders or native picker before the first message and hold it fixed thereafter (SCA-APP-010 SOW-002). A new chat establishes a different folder; the old global clear control is not the current mechanism. | `docs/PRD.md` FR-002 |
> | DEL-02-03-REQ-002 | The UI shall present validation failures for non-absolute, missing, inaccessible, non-directory, or instruction-root-contained paths. | `docs/PRD.md` FR-003; `docs/SPEC.md` §1.2 |
> | DEL-02-03-REQ-003 | A chat without a valid folder SHALL truthfully disable folder-dependent actions under D-APP-120; folder changes MUST NOT silently rebind an existing conversation. | `docs/PRD.md` §7.1 |
> | DEL-02-03-REQ-004 | The UI shall render a bounded file tree for the selected working root using the workspace tree API. | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2 |
> | DEL-02-03-REQ-005 | File tree presentation shall account for skipped directories `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`. | `docs/PRD.md` FR-004 |
> | DEL-02-03-REQ-006 | File tree presentation shall indicate inaccessible directories or truncation when reported by the API. | `docs/PRD.md` FR-004 |
> | DEL-02-03-REQ-007 | Scope scan UI shall present deliverables and knowledge-type directories without treating UI-local state as project truth. | `docs/SPEC.md` §17.2; `docs/CONTRACT.md` K-FS-1; `docs/TYPES.md` §4.4 |
> | DEL-02-03-REQ-008 | Dynamic scope scan state shall clear invalid selections when the root changes, deliverables are removed, knowledge markers are disabled, or knowledge targets become stale. | `docs/PRD.md` FR-013 |
> | DEL-02-03-REQ-009 | Deliverable summary widgets shall support routing to PIPELINE `TASK*` with a deliverable preselected when deliverables are present. | `docs/PRD.md` §7.5 |
> | DEL-02-03-REQ-010 | The UI shall consume status and dependency contract snapshots read-only where applicable; transition controls belong only where supported by the active workflow. | `docs/PRD.md` FR-010 |
> | DEL-02-03-REQ-011 | Scan and workspace errors surfaced by the UI shall preserve typed-error information where available. | `docs/PRD.md` NFR-009 |
> | DEL-02-03-REQ-012 | File and scope scans shall avoid runaway traversal by respecting bounded depth/count behavior exposed by the runtime. | `docs/PRD.md` NFR-012 |
> | DEL-02-03-REQ-013 | Stable deliverable IDs, not folder labels alone, shall drive deliverable identity in summary widgets and route targets. | `docs/CONTRACT.md` K-ID-1, K-PATH-1; `docs/TYPES.md` §1.2 |
> | DEL-02-03-REQ-014 | This presentation deliverable consumes formal dependencies read-only; the extracted Dependencies.csv already exists and is not created or altered by these UI controls. | `_DEPENDENCIES.md`; dispatch instruction |
>

D-APP-108 Q4a/b seated viewer detail: the right panel shows one view at a time, with a bounded clickable/expandable file tree and document viewer. In-panel text, Markdown, code and CSV reads stop at 10 MB; PDF uses the in-panel renderer, while DOCX/XLSX/PPTX use macOS Quick Look with Open in default app. PDF and Quick Look previews are outside the text cap. The PDF path remains subject to D-APP-121 isolated proof and no publication/acceptance follows from this clause.

D-APP-108 Q2 seated reference detail: replies and Activity show source path/range chips. Viewer Ask and Attach and composer Quote use existing attachment controls; Quote sends `clientType: 'quote'` with source path and range, adding no harness event type.

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Authority | Applicability | Source |
> |---|---|---|
> | Working-root contract | Governs selected root validity, containment, and project-truth placement | `docs/SPEC.md` §1.2; `docs/CONTRACT.md` K-ROOT/K-FS surfaces |
> | Workspace API contract | Defines the read endpoints this UI consumes | `docs/SPEC.md` §17.2 |
> | PRD current product scope | Establishes working-root selection, file-tree browsing, deliverable scanning, and lifecycle/dependency contract API support as current scope | `docs/PRD.md` §6.1 |
> | Unknown-value discipline | Unsupported facts remain `TBD` rather than guesses | `docs/CONTRACT.md` K-INVENT-1 |
>

### CLM-011 — Verification

> ##### Verification
>
> | ReqID | Verification Approach |
> |---|---|
> | DEL-02-03-REQ-001 | The UI SHALL select a folder per chat through typed path, known folders or native picker before the first message and hold it fixed thereafter (SCA-APP-010 SOW-002). A new chat establishes a different folder; the old global clear control is not the current mechanism. |
> | DEL-02-03-REQ-002 | API/UI integration tests with invalid root cases and typed error display checks. |
> | DEL-02-03-REQ-003 | A chat without a valid folder SHALL truthfully disable folder-dependent actions under D-APP-120; folder changes MUST NOT silently rebind an existing conversation. |
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
> | DEL-02-03-REQ-014 | This presentation deliverable consumes formal dependencies read-only; the extracted Dependencies.csv already exists and is not created or altered by these UI controls. |
>

### CLM-012 — Documentation

Current loci include the composer folder binding and right-panel file tree/document presentation under `frontend/src/components/woven-dialogue/` and `frontend/src/components/shell/chat-panel.tsx`. Retain typed validation errors, bounded/skipped/truncated tree feedback and source identity. Scope-scan/deliverable summary/status/dependency widgets are not demonstrated on the live shell; their exact carrier/compatibility obligations remain open, as do typed-error detail and rename/truncation fixtures. D-APP-121 PDF presentation/security/native qualification remains required. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

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
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
>

### CLM-017 — Purpose

> ##### Purpose
>
> Define the working procedure to produce and verify the Working Root File Tree and Scope Scan UI slice without expanding into filesystem enforcement, dependency extraction, or runtime engine internals.
>

### CLM-018 — Prerequisites

Dependency extraction ran under D-APP-109/D-APP-110 on 2026-09-05. `Dependencies.csv` is the formal extracted register; consult each edge and gate directly. This record repair neither changes an edge nor infers satisfaction from implementation. Read current per-chat SOW-002 and D-APP-120 no-folder restrictions. Response shapes are observable in the workspace API and must be source-bound, not invented. Current reference observations remain distinct from accepted pins. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

### CLM-019 — Steps

1. Verify per-chat folder selection before the first message and fixed identity afterward.
2. Refuse invalid/instruction-root-contained folders and present typed validation errors.
3. Render bounded tree results with skipped/inaccessible/truncated feedback.
4. Test stable deliverable IDs and read-only contract data where those widgets are exposed; keep absent scope-scan/summary/route consumers visible as unresolved carrier work.
5. Verify D-APP-121 document/PDF presentation and its security/native qualification with DEL-09-06.
6. Record current render/browser, typed-error, truncation and rename evidence without claiming unrendered helpers prove the live shell. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-020 — Verification

Current folder checks cover select-before-first-message, fixed binding and truthful no-folder restrictions; a global Clear control is historical. Verify bounded tree/skipped/truncated presentation and typed errors. The missing scope-scan/summary/status/route consumers and their tests remain explicit delivery/alignment work. Preserve stable IDs and read-only project truth. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-021 — Records

Preserve ScopeOfWork.md, source-bound folder/tree/error/UI results, D-APP-121 PDF/security/native witnesses and current reference observations. The old four-document-kit record is historical. Do not infer missing fixture or native outcomes.

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
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
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
> - Keep unsupported facts as `TBD`: response fields and UI copy require source confirmation; current component loci are named in CLM-012. Source: `docs/CONTRACT.md` K-INVENT-1.
>

### CLM-027 — Considerations

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. Dependency extraction ran under D-APP-109/D-APP-110 on 2026-09-05. `Dependencies.csv` is the formal extracted register; consult each edge and gate directly. This record repair neither changes an edge nor infers satisfaction from implementation. Current folder identity is per-chat. Missing live scan/summary consumers and exact compatibility carriers remain separate; absent UI does not retire stable identity or read-only project-truth requirements.

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

A chat chooses a valid folder before its first message and keeps that identity. A tree result marks truncation and skipped/inaccessible content truthfully. A chat without a valid folder has dependent actions unavailable. Scope-scan/deliverable-routing examples from the old Pipeline surface remain unverified current compatibility obligations, not live observations. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-030 — Conflict Table (for human ruling)

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. The former global working-root/clear mechanism is superseded by SCA-APP-010 per-chat binding. Exact scope-scan/summary/route carriers and D-APP-121 native PDF qualification remain unresolved; accepted decomposition pin changes require their owning scope process.

### CLM-031 — Human-Ruling Needed

Component loci are the composer and woven-dialogue right-panel sources named in CLM-012. Missing current typed-error, truncation, rename and PDF/native evidence remain open; the selected reference state is recorded separately. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

### CLM-032 — Pass 3 Disposition Notes

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-002 SOW-003 OBJ-001 OBJ-006 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

## Retired status detail (2026-09-23)

These clauses retain the operative meaning of the named App `Remaining` entries after their one-time retirement. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R022:** D-APP-108 Q4a/b requires the view switcher, bounded expand/drag file tree, in-panel PDF and text/Markdown/code/CSV viewer with a 10 MB text cap, and Office Quick Look with Open in default app. D-APP-121 still gates PDF qualification and publication.

- **APP-R023:** D-APP-108 Q2 requires source path/range chips in replies and Activity, viewer Ask and Attach, and composer Quote using existing attachment controls with clientType quote plus source path/range; no new harness event is implied.

- **APP-R024:** Preserve scope scan, summary, status and route consumers alongside native PDF/security and source-bound evidence. Compare the receiving DEL-02-03/SCA-APP-010 contracts before assigning any orphaned consumer; the unresolved owner mapping is deferred in App Task Management.
