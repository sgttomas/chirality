---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-01
package_id: PKG-02
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-001, SOW-005]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-02-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-02-01` in service of project scope [SOW-001, SOW-005] and package objectives [OBJ-001].

- **OUT-001** — The current Woven Dialogue shell and compatibility-navigation contract for project scope SOW-001 and SOW-005 and package objective OBJ-001, with prior accepted implementation evidence retained as dated compatibility evidence.

## SCA-APP-004 Gate-5 Current Contract (Controlling until SCA-APP-010)

The owner-approved SCA-APP-004 amendment prospectively changes this
deliverable's target presentation while preserving its stable ID, lifecycle,
accepted evidence, routes, query behavior, and compatibility obligations.
Where the older clauses below require a fixed PORTAL/matrix/right-sidebar
target layout, this section controls. Those clauses remain in this record as
dated evidence of the compatibility implementation and are not erased or
recast as current target authority.

### Current responsibility

`DEL-02-01 Woven Dialogue Shell and Compatibility Navigation` composes:

- the persistent primary human-agent transcript and composer;
- provenance-bearing inline artifact objects and focused artifact views that
  return to their dialogue anchors;
- the Navigator, Work/Agents Coordination Panel, and Activity Shelf;
- compatibility navigation for the existing routes, query parameters, and
  matrix-driven launch intents; and
- presentation over existing canonical work, session, replay, artifact, and
  runtime records without creating a second evidence store.

The primary live dialogue remains mounted. A selected recorded-session replay
is observational and read-only, does not resume or replace the primary
session's authority, and provides a persistent return to the primary dialogue.
Visible artifacts do not automatically become next-turn model context.

This deliverable owns shell integration and presentation only. It does not own
canonical work truth, session parentage, transcript reconstruction, artifact
facts, routing semantics, dispatch semantics, runtime capability, lifecycle,
approval, arbitrary orchestration graphs, scheduling, direct child messaging,
or automatic intent inference.

### Current acceptance obligations

1. Preserve `/`, `/chat`, `/workbench`, and `/pipeline`, current deep-link
   intent, known query parameters, and unknown-parameter preservation during
   the compatibility period.
2. Keep the existing loop-first and matrix UI reachable until separately
   retired; the target shell does not require the matrix to remain its fixed
   primary gateway.
3. Keep the primary dialogue mounted across navigation, artifact focus,
   Coordination Panel selection, and read-only replay selection.
4. Show provenance and source links for inline/focused artifacts without
   silently adding visible artifacts to next-turn model context.
5. Render Work and Agents as rebuildable, evidence-conditional projections;
   missing, stale, conflicting, or unrecorded relationships remain unknown.
6. Preserve mid-turn selection guards, drafts, context, permissions,
   attachments, interruption state, and interaction authority on the primary
   live dialogue.
7. Provide component/render, route/query compatibility, focus restoration,
   keyboard-region, accessible-landmark, reduced-motion, and bounded-projection
   evidence for the new shell.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

`DEL-02-01 Woven Dialogue Shell and Compatibility Navigation` (UX_UI_SLICE, applied decomposition row L307):

Compose the persistent primary human–agent transcript and composer with its
context line (folder, agent, permissions, delegation, rung), the header-less
three-panel frame, the left-panel chat navigator with local organisation,
per-chat folder selection over the known-folder set, the account row host, and
compatibility navigation without creating a second evidence store.

Applied row notes: Shell integration owns presentation only; work, hierarchy,
transcript, and artifact facts remain governed by their existing semantic
owners; the direct shell items are seated as Remaining work by the owner, not by
this row.

Applied row outputs: Dialogue shell; composer context line; chat navigator;
account row host; route/query and compatibility tests.

### Current acceptance obligations

1. The centre dialogue is never hidden, unmounted, or replaced; the frame has no header row.
2. The composer context line shows folder, agent, permissions, delegation, and rung from recorded state; a chat may have no folder and says so.
3. Folder selection is live only before a chat's first message and fixed thereafter; invalid or instruction-root-contained paths are refused by DEL-07-01's validation with the refusal visible (Q9: native picker, macOS recent documents, Reveal in Finder, folder drop).
4. Chat organisation acts on local convenience state owned by DEL-02-04 only; deleting a chat hides it locally and never mutates the runtime session record (Q1); derived titles pass the redaction helper (Q6).
5. Existing routes, queries, aliases, and the loop-first UI remain compatibility surfaces; the retired Workbench and Pipeline routes stay reachable by URL and unlisted (Q3).
6. The pop-out panel window is not in scope (Q5); the account row is hosted here and its presentation is DEL-02-05's.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-02-01-V3-01,
DEL-02-01-V3-02, DEL-02-01-V3-03, DEL-02-01-V3-04. Ruled questions applied here:
Q1, Q3, Q5, Q6, Q9. Alignment writes WI-001, WI-002, WI-003, WI-004, WI-005
performed in run `APP_SCA_APP_010_SEATING_2026-09-04`; dependency writes
DEP-001, DEP-002 await the registered dependency-extract pass after owner
acceptance of this alignment. No lifecycle, Checking Approval SHA,
dependency-acceptance, product, or release act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-02-01 Woven Dialogue Shell and Compatibility Navigation

> #### Datasheet: DEL-02-01 Woven Dialogue Shell and Compatibility Navigation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | PackageID | PKG-02 |
> | PackageName | Woven Dialogue Shell, Navigation, and Operator State |
> | DeliverableID | DEL-02-01 |
> | DeliverableName | Woven Dialogue Shell and Compatibility Navigation |
> | ResponsibleParty | TBD |
> | Type | UX_UI_SLICE |
> | ContextEnvelope | M |
> | Current State at P1/P2 authoring | OPEN |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary surface | Loop-first desktop shell navigation: PORTAL as the primary header entry, with WORKBENCH and PIPELINE reachable as right-sidebar tertiary forms and preserved deep links | REF-006 `docs/PRD.md` Section 8.1 FR-001; decomposition DEL-02-01; D-APP-28/D-APP-31/D-APP-32 |
> | Matrix shape | 3 rows by 4 columns | REF-006 Section 8.2 FR-007; REF-004 `docs/TYPES.md` Section 4.3 |
> | Matrix rows | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE` | REF-006 Section 8.2 FR-007; REF-004 Section 4.1 |
> | Matrix columns | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING` | REF-006 Section 8.2 FR-007; REF-004 Section 4.2 |
> | NORMATIVE destination | Mounted live-loop persona context | REF-004 Section 4.1; REF-006 Section 7.2; D-APP-28/D-APP-30 |
> | OPERATIVE destination | PIPELINE sidebar/deep-link intent | REF-004 Section 4.1; REF-006 Section 7.2; D-APP-28/D-APP-31 |
> | EVALUATIVE destination | Mounted live-loop persona context | REF-004 Section 4.1; REF-006 Section 7.2; D-APP-28/D-APP-30 |
> | Shell routes | `/` is the primary header entry; `/pipeline` and `/workbench` are preserved deep-link route entries that open right-sidebar tertiary forms | REF-006 Section 8.1 FR-001; D-APP-28/D-APP-31/D-APP-32 |
> | Active route indication | Required for rendered primary header links; Workbench/Pipeline active context is sidebar-tab state | REF-006 Section 8.1 FR-001; D-APP-28 |
> | Anticipated artifacts | Navigation components; matrix UI tests; route query handling; AMD-01 render tests | `_CONTEXT.md`; decomposition DEL-02-01; D-APP-36 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Scope items covered | SOW-001, SOW-005 | `_CONTEXT.md`; decomposition SSOW and traceability |
> | Objective supported | OBJ-001 | `_CONTEXT.md`; decomposition objective mapping |
> | Inclusions | UI and operator workflow behavior | `_CONTEXT.md`; decomposition PKG-02 package row |
> | Exclusions | Runtime engine internals | `_CONTEXT.md`; decomposition PKG-02 package row |
> | PRD source status | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; dispatch instruction — reconciled under D-APP-38 |
> | Dependency extraction | Deferred; `Dependencies.csv` not produced in this run | Dispatch instruction; `_DEPENDENCIES.md` initial population rule |
>

### CLM-005 — Construction

> ##### Construction
>
> | Item | Required Construction Detail | Source |
> |---|---|---|
> | Header/navigation | Must expose PORTAL in primary header navigation and preserve `/pipeline` and `/workbench` as loop-first deep-link route entries | REF-006 Section 8.1 FR-001; D-APP-28/D-APP-31/D-APP-32 |
> | PORTAL matrix | Must render canonical rows and columns | REF-006 Section 8.2 FR-007; REF-004 Section 4 |
> | Matrix cell routing | Must route NORMATIVE and EVALUATIVE cells to mounted live-loop persona context and OPERATIVE cells to PIPELINE intent | REF-006 Section 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30/D-APP-31 |
> | Route state | Current implementation evidence uses `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys; older source text does not independently name all keys | `_CONTEXT.md`; ADQ-13 implementation evidence |
> | Tests | Matrix, route wrapper, sidebar, and disabled-state render tests are recorded under ADQ-13 | `_CONTEXT.md`; D-APP-36; ADQ-13 evidence |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source Used | Relevant Slice |
> |---|---|---|
> | REF-004 | `docs/TYPES.md` | Section 4 UI Navigation Vocabulary |
> | REF-006 | `docs/PRD.md` | Sections 7.2, 8.1, 8.2, and package mapping |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOW-001, SOW-005, OBJ-001, PKG-02, DEL-02-01 |
> | LOCAL | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` | Deliverable identity, source status, and dependency deferral |
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-105 supersedes run-scoped dependency-extraction deferral wording: the extracted register exists and is live. UPD-106 is implemented by the governed PORTAL active-link render test.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-02-01 Desktop Shell and Matrix Navigation

> #### Specification: DEL-02-01 Desktop Shell and Matrix Navigation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable covers the user-facing desktop shell navigation and canonical matrix routing for `DEL-02-01 Desktop Shell and Matrix Navigation`.
>
> In scope:
>
> - Loop-first access to PORTAL, WORKBENCH, and PIPELINE shell surfaces.
> - Primary header navigation to PORTAL (`/`), plus preserved deep-link route entries for `/workbench` and `/pipeline`.
> - Right-sidebar tertiary tabs for PORTAL, WORKBENCH, and PIPELINE while the live loop remains mounted as the primary pane.
> - PORTAL rendering of the canonical 3x4 agent matrix.
> - Matrix row-semantics routing into live-loop persona context or PIPELINE.
> - Navigation components, matrix UI tests, and route query handling to the extent supported by source evidence.
>
> Out of scope:
>
> - Runtime engine internals.
> - Workbench agent-context detail owned by adjacent deliverables except where routing handoff requires it.
> - Pipeline selector behavior beyond receiving OPERATIVE matrix routes.
> - Dependency extraction and `Dependencies.csv` creation for this run.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Priority | Source | Verification |
> |---|---|---:|---|---|
> | DEL-02-01-REQ-001 | The app shall provide a loop-first desktop shell where PORTAL, PIPELINE, and WORKBENCH are reachable while the live loop stays primary. | P0 | REF-006 Section 8.1 FR-001; SOW-001; D-APP-28/D-APP-31/D-APP-32 | Component render tests confirm all three tertiary surfaces are present in the right sidebar. |
> | DEL-02-01-REQ-002 | Primary header navigation shall expose PORTAL at `/`; `/workbench` and `/pipeline` shall remain deep-link route entries that open their matching right-sidebar tertiary tab. | P0 | REF-006 Section 8.1 FR-001; D-APP-28/D-APP-31/D-APP-32 | Route-wrapper render tests confirm `/workbench` defaults to the Workbench tab and `/pipeline` defaults to the Pipeline tab. |
> | DEL-02-01-REQ-003 | Header navigation shall visually indicate the active primary section for rendered header links. | P0 | REF-006 Section 8.1 FR-001; D-APP-28 | UI assertion confirms active state for the rendered primary header item; Workbench/Pipeline active context is represented by sidebar tab state. |
> | DEL-02-01-REQ-004 | PORTAL shall render the canonical 3x4 agent matrix. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.3 | Matrix UI test confirms 3 rows and 4 columns. |
> | DEL-02-01-REQ-005 | Matrix rows shall be `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.1 | Matrix UI test checks row labels and row order if order is encoded in implementation. |
> | DEL-02-01-REQ-006 | Matrix columns shall be `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.2 | Matrix UI test checks column labels and column order if order is encoded in implementation. |
> | DEL-02-01-REQ-007 | NORMATIVE matrix cells shall focus the mounted live loop with the selected Type-0/Type-1 persona context. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30 | Matrix routing/render tests confirm loop-persona launch kind and mid-turn disabled state. |
> | DEL-02-01-REQ-008 | EVALUATIVE matrix cells shall focus the mounted live loop with the selected Type-0/Type-1 persona context. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30 | Matrix routing/render tests confirm loop-persona launch kind and mid-turn disabled state. |
> | DEL-02-01-REQ-009 | OPERATIVE matrix cells shall open PIPELINE intent in the right sidebar or preserved `/pipeline` deep-link entry. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-31 | Matrix routing/render tests confirm Pipeline launch kind and sidebar destination. |
> | DEL-02-01-REQ-010 | Disabled or unsupported variants shall remain visible as coming soon rather than disappearing when encountered in matrix-adjacent navigation flows. | P0 | REF-006 Section 7.2 acceptance | UI test confirms unsupported variants are visible and non-selectable where this deliverable exposes them. |
> | DEL-02-01-REQ-011 | Stable identifiers shall remain distinct from path or label changes. Current implementation evidence uses `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys. | P1 | REF-002 `docs/CONTRACT.md` K-ID-1 and K-PATH-1; REF-006 Section 8.2 FR-009; ADQ-13 implementation evidence | Matrix identity and deliverable-key render tests confirm selected implementation keys while preserving source warnings for future authority reconciliation. |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or Source | Applicability | Status |
> |---|---|---|
> | `docs/PRD.md` | Product requirements for shell navigation and matrix routing | Accessible; hash is MATCH under D-APP-38 — reconciled under D-APP-38 |
> | `docs/TYPES.md` Section 4 | Canonical UI navigation vocabulary and matrix semantics | Accessible |
> | `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-INVENT-1, K-CONFLICT-1 | Stable identity and epistemic controls relevant to routing and document production | Accessible |
> | `docs/DIRECTIVE.md` Section 4.1 | In-scope statement for local desktop operation and matrix navigation | Accessible |
> | SOFTWARE_DECOMP v3.2 | Deliverable scope, SOW mapping, objective context, and execution note to preserve ResponsibleParty | Accessible |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach | Evidence Record |
> |---|---|---|
> | REQ-001 through REQ-003 | Route/navigation component render tests | `frontend/src/__tests__/components/workspace-sidebar.test.ts`; `frontend/src/__tests__/components/loop-tertiary-routes.test.ts` |
> | REQ-004 through REQ-006 | Matrix rendering tests | Matrix UI test output |
> | REQ-007 through REQ-009 | Matrix launch-kind and route-query tests | `frontend/src/__tests__/lib/agent-matrix-cells.test.ts`; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`; `frontend/src/__tests__/components/agent-matrix-panel.test.ts` |
> | REQ-010 | Disabled-state visibility render tests where unsupported variants are surfaced | `frontend/src/__tests__/components/agent-matrix-panel.test.ts`; `frontend/src/__tests__/components/pipeline-surface.test.ts` |
> | REQ-011 | Identity/route-state review | `frontend/src/__tests__/lib/agent-matrix-cells.test.ts`; `frontend/src/__tests__/components/agent-matrix-panel.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts` |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required or anticipated artifacts:
>
> - Navigation components.
> - Matrix UI tests.
> - Route query handling.
> - Evidence notes identifying any route-state parameters chosen by implementation.
> - ADQ-13 evidence: `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/Evidence_ADQ-13_UI_Specs_Render_Tests.md`.
> - Human ruling if the dispatch path/package rename is material to scope identity.
> - P3 disposition: selected implementation keys are documented above; source-pointer and package-path warnings remain surfaced for future governed reconciliation.
>

### CLM-014 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-105 supersedes run-scoped dependency-extraction deferral wording: the extracted register exists and is live. UPD-106 is implemented by the `ShellFrame` render test asserting the rendered PORTAL link carries `shell-nav-link--active`.
>

### CLM-015 — D-APP-56 shell ownership amendment (2026-07-12)

> ##### D-APP-56 shell ownership amendment (2026-07-12)
>
> R4-P29 assigns the `/chat` direct-chat shell surface and portal persona-picker bar to DEL-02-01 shell scope. The deliverable-rows launcher remains covered by DEL-02-03 REQ-009. DEL-08-02 retains persona-alias ownership and owns the `isMatrixLaunchBlockedByStreaming` persona/matrix launch guard as consumer-side behavior.

- **AC-001** — The DEL-02-01 Scope of Work preserves every legacy source range, has no silent claim loss, and validates under SOW_V1 for SOW-001, SOW-005, and OBJ-001.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-02-01 Desktop Shell and Matrix Navigation

> #### Procedure: DEL-02-01 Desktop Shell and Matrix Navigation
>

### CLM-017 — Purpose

> ##### Purpose
>
> Produce and verify the loop-first desktop shell and matrix navigation slice for DEL-02-01, preserving PORTAL, WORKBENCH, and PIPELINE access while the live loop remains the primary pane.
>

### CLM-018 — Prerequisites

> ##### Prerequisites
>
> - Accessible source references listed in `_REFERENCES.md`.
> - Current deliverable context in `_CONTEXT.md`.
> - Existing implementation workspace for navigation components and tests.
> - Implementation evidence slots are required for later closure: navigation component path, matrix UI test path, and route query handling test path. ADQ-13 records selected paths in the implementation evidence table below.
> - Human acceptance that `ResponsibleParty` remains `TBD` until assigned.
> - Dependency extraction remains deferred; do not create `Dependencies.csv` as part of this procedure.
>
> Declared upstream dependencies:
>
> - TBD - no accepted dependency edges have been extracted yet.
>
> Declared downstream dependencies:
>
> - TBD - no accepted dependency edges have been extracted yet.
>

### CLM-019 — Steps

> ##### Steps
>
> 1. Confirm the deliverable identity from `_CONTEXT.md`: `DEL-02-01 Desktop Shell and Matrix Navigation`, `ResponsibleParty: TBD`, `Type: UX_UI_SLICE`, `ContextEnvelope: M`.
> 2. Confirm authoritative source availability from `_REFERENCES.md`; treat the PRD hash mismatch as a source warning unless a human ruling changes that instruction.
> 3. Preserve the shell's three surfaces: PORTAL at `/`, PIPELINE through the right-sidebar tertiary tab and `/pipeline` deep link, and WORKBENCH through the right-sidebar tertiary tab and `/workbench` deep link.
> 4. Ensure primary header navigation exposes PORTAL and visually indicates the active rendered section; route wrappers for `/workbench` and `/pipeline` must default to their matching sidebar tabs.
> 5. Render the PORTAL matrix with rows `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`.
> 6. Render the PORTAL matrix with columns `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`.
> 7. Route `NORMATIVE` cells to the mounted live loop by updating persona/query context without replacing the primary pane.
> 8. Route `EVALUATIVE` cells to the mounted live loop by updating persona/query context without replacing the primary pane.
> 9. Route `OPERATIVE` cells to PIPELINE intent in the right sidebar or preserved `/pipeline` deep link.
> 10. Preserve unsupported or disabled variants as visible coming-soon options where this deliverable exposes them.
> 11. Add or update matrix UI tests for row/column rendering and row-semantics routing.
> 12. Add or update route query handling tests for selected implementation keys. Current evidence covers `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys while preserving older source warnings.
> 13. Keep runtime engine internals out of this slice; hand off engine or selector-specific behavior to adjacent deliverables.
> 14. Record selected implementation paths for navigation components, matrix UI tests, and route query handling tests in this kit and in the ADQ-13 evidence note.
>

### CLM-020 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | Surface reachability | `/`, `/pipeline`, and `/workbench` remain reachable; `/workbench` and `/pipeline` open matching right-sidebar tertiary forms. |
> | Active surface state | Primary header state covers rendered header links; Workbench/Pipeline active context is represented by sidebar tab state. |
> | Matrix shape | PORTAL shows 3 rows and 4 columns. |
> | Row labels | `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE` are present. |
> | Column labels | `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING` are present. |
> | Loop-persona routing | NORMATIVE and EVALUATIVE cells focus the mounted loop with selected persona context. |
> | PIPELINE routing | OPERATIVE cells route to PIPELINE intent. |
> | Unsupported variants | Unsupported variants visible in this slice are disabled or coming soon, not silently removed. |
> | Scope discipline | No runtime engine internals are changed under this deliverable's authority. |
>

### CLM-021 — Implementation Evidence Slots

> ##### Implementation Evidence Slots
>
> | Evidence Slot | Current Value | Source |
> |---|---|---|
> | Navigation component path | `frontend/src/components/shell/shell-frame.tsx`; `frontend/src/components/shell/sidebar-right-loop-layout.tsx`; `frontend/src/components/shell/loop-tertiary-shell.tsx`; `frontend/src/app/workbench/workbench-client.tsx`; `frontend/src/app/pipeline/pipeline-client.tsx` | ADQ-13 inspection and render tests |
> | Matrix UI test path | `frontend/src/__tests__/components/agent-matrix-panel.test.ts`; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` | ADQ-13 AMD-01 render evidence |
> | Route query handling test path | `frontend/src/__tests__/components/loop-tertiary-routes.test.ts`; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`; `frontend/src/__tests__/lib/loop-first.test.ts` | ADQ-13 AMD-01 render evidence |
>
> P3 disposition: D-001 is now implementation-evidence-backed for the selected paths above. Package path, PRD hash, and source-pointer conflicts remain warning-limited and are not resolved by this procedure update.
>

### CLM-022 — Records

> ##### Records
>
> - Navigation component change notes or diff references.
> - Matrix UI test results.
> - Route query handling test results, with selected query key names documented.
> - Any human rulings resolving the package path mismatch, PRD hash mismatch, or PRD/SPEC/TYPES source-pointer issue.
> - This four-document kit and the TASK run record.
>

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-105 supersedes run-scoped dependency-extraction deferral wording: the extracted register exists and is live. UPD-106 remains withheld for the final code tranche.

- **VER-001** — Validate the DEL-02-01 candidate, generate its complete claim map and parity report, and derive its deterministic review checklist.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-02-01 Desktop Shell and Matrix Navigation

> #### Guidance: DEL-02-01 Desktop Shell and Matrix Navigation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-025 — Purpose

> ##### Purpose
>
> This deliverable preserves the operator's primary movement through Chirality's loop-first desktop shell: PORTAL for the matrix entry point, WORKBENCH as a contract/context review form, and PIPELINE for operative task categories. It supports OBJ-001 by keeping the local desktop harness clear, governed, and navigable while the live loop remains mounted.
>

### CLM-026 — Principles

> ##### Principles
>
> - Keep shell navigation explicit: PORTAL, PIPELINE, and WORKBENCH are first-class surfaces, with PORTAL as the primary header entry and Workbench/Pipeline preserved as right-sidebar tertiary forms and deep-link entries.
> - Treat the agent matrix as canonical product vocabulary. Use `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE` for rows, and `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING` for columns.
> - Route by row semantics: `NORMATIVE` and `EVALUATIVE` focus the mounted live loop with Type-0/Type-1 persona context; `OPERATIVE` opens PIPELINE intent.
> - Preserve stable IDs and route meaning across label or path changes. Current implementation evidence uses `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys; future authority work may still reconcile source wording.
> - Keep unsupported variants visible as coming soon when this slice exposes them, instead of hiding roadmap-aware choices.
> - Do not make runtime engine behavior part of this deliverable; this slice owns navigation and routing presentation.
>

### CLM-027 — Considerations

> ##### Considerations
>
> - `docs/PRD.md` is the main product requirement source for this slice; its observed hash matches the expected REF-006 hash under D-APP-38 and is not a blocker.
> - The PRD says matrix routing follows the `docs/SPEC` contract, while the accessible route semantics for rows and cells are in `docs/TYPES.md` Section 4 and PRD Section 7.2/8.2. Until a human reconciles that wording, use TYPES plus PRD as the concrete source for matrix routing behavior.
> - DEL-08-02 also covers matrix routing contract concerns. DEL-02-01 should focus on the visible shell and matrix navigation behavior, while leaving persona alias and deeper routing-contract ownership to DEL-08-02 unless a human ruling expands this slice.
> - DEL-02-02 and DEL-08-03 own adjacent workbench/pipeline selector details. This deliverable should test that row routing lands on the correct surface without over-specifying downstream controls.
> - Query-state naming for selected agent, row, column, category, task scope, and deliverable key is source-supported as anticipated "route query handling"; ADQ-13 records the selected implementation keys while leaving older source-pointer wording MATCH-verified. (reconciled under D-APP-38).
>

### CLM-028 — Trade-offs

> ##### Trade-offs
>
> | Topic | Direction | Rationale |
> |---|---|---|
> | Canonical matrix vocabulary vs. UI copy flexibility | Prefer canonical row/column values in tests and route state | TYPES Section 4 gives stable terms that reduce routing ambiguity. |
> | Shell scope vs. runtime scope | Keep runtime internals out of this deliverable | PKG-02 excludes runtime engine internals. |
> | Visible disabled options vs. minimal UI | Keep unsupported variants visible when this slice exposes them | PRD Section 7.2 acceptance requires unsupported variants to remain visible as coming soon. |
> | Query parameter specificity | Treat selected implementation keys as evidence-backed, not new source authority | Source slices require active context/query handling but do not independently define this deliverable's full parameter schema. |
>

### CLM-029 — Examples

> ##### Examples
>
> | Example | Expected Result | Source |
> |---|---|---|
> | Operator selects a NORMATIVE matrix cell from PORTAL | The mounted live loop receives the selected persona context without replacing the primary pane | REF-006 Section 7.2; REF-004 Section 4.1; D-APP-28/D-APP-30 |
> | Operator selects an OPERATIVE matrix cell from PORTAL | PIPELINE opens with category context in the right sidebar or preserved deep-link entry | REF-006 Section 7.2; REF-004 Section 4.1; D-APP-28/D-APP-31 |
> | Operator opens `/pipeline` directly | The route opens the loop-first shell with the Pipeline sidebar tab selected | REF-006 Section 8.1 FR-001; D-APP-31 |
>

### CLM-030 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Source A | Source B | Issue | Current Handling | Human Ruling Needed |
> |---|---|---|---|---|---|
> | CONFLICT-001 | Dispatch deliverable path uses `PKG-02_Desktop_UI_and_Local_Experience` | Existing in-repo deliverable folder uses `PKG-02_Desktop_Shell_Navigation_and_Operator_State` and `_CONTEXT.md` package name matches decomposition | Package path segment differs from dispatch, while deliverable ID and name match | Wrote only inside the existing DEL-02-01 folder and recorded this as a scope/path warning. P3 disposition: E-001 already covered as conflict. | Confirm whether the package path rename is accepted and whether future dispatches should use the existing path |
> | CONFLICT-002 | REF-006 expected SHA in `_REFERENCES.md` | REF-006 actual SHA in `_REFERENCES.md` | PRD hash status: MATCH | Treated as source warning, not blocker, per dispatch. P3 disposition: B-001 already covered as conflict. | Confirm whether observed PRD hash should replace expected hash in a later governed reference update — reconciled under D-APP-38 |
> | CONFLICT-003 | PRD FR-008 says matrix routing shall follow the `docs/SPEC` contract | Accessible concrete matrix vocabulary and row destination semantics are in `docs/TYPES.md` Section 4, not in located `docs/SPEC.md` slices | Source pointer appears imprecise or stale | Used PRD Section 7.2/8.2 plus TYPES Section 4 for concrete routing requirements. P3 disposition: F-001 already covered as conflict. | Confirm whether SPEC should be amended or whether TYPES is the intended route-semantics authority |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-001 SOW-005 OBJ-001 | SCA-APP-010 Gate-5 Current Contract; CLM-008 | AC-001 | VER-001 | Woven Dialogue shell evidence, compatibility parity, provenance and primary-dialogue isolation checks |
