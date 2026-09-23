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
7. The visual shell uses the Stone palette and left-panel wordmark with measured text/control contrast; verify current composer-context copy for folder, active role, permissions, delegation and rung against D-GOV-43/D-APP-127 and the four-role contract. The older target-spec §10 role/consent labels do not supersede that contract.
8. The navigator lists sessions across registered known roots with each chat's folder and derives the active provider root from the session's registered project identity. `knownRoots` is local convenience state, not a new Runtime root field.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-02-01-V3-01,
DEL-02-01-V3-02, DEL-02-01-V3-03, DEL-02-01-V3-04. Ruled questions applied here:
Q1, Q3, Q5, Q6, Q9. Alignment writes WI-001, WI-002, WI-003, WI-004, WI-005
performed in run `APP_SCA_APP_010_SEATING_2026-09-04`; dependency writes
DEP-001, DEP-002 were performed under D-APP-109/D-APP-110 on 2026-09-05; the extracted register now exists. No lifecycle, Checking Approval SHA,
dependency-acceptance, product, or release act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-02-01 Woven Dialogue Shell and Compatibility Navigation

> #### Datasheet: DEL-02-01 Woven Dialogue Shell and Compatibility Navigation
>
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
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

The current shell has a headerless Navigator, primary centre dialogue, right-panel views and an activity strip. Folder selection is per chat before its first message and fixed thereafter; current no-folder behavior is constrained by D-APP-120. New direct-entry roles are HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS; TASK is delegated. Presentation must preserve recorded identity, selected permissions and visible unavailable states.

The old 3x4 visual matrix and loop-first pane arrangement are dated presentation history under SCA-APP-010. The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; unrendered helper tests do not prove current route behavior, and this record does not silently retire that contract. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-004 — Conditions

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

Dependency extraction ran under D-APP-109/D-APP-110 on 2026-09-05. `Dependencies.csv` is the formal extracted register; consult each edge and gate directly. This record repair neither changes an edge nor infers satisfaction from implementation. ResponsibleParty remains TBD. Runtime internals remain outside this shell deliverable.

### CLM-005 — Construction

Provide navigation, per-chat folder controls, role/permission context and local chat organisation without making UI state project truth. Delegation/rung context fields, full multi-root listing, native Finder/Dock behaviors and exact icon directions retain their separate recorded residuals. The old 3x4 visual matrix and loop-first pane arrangement are dated presentation history under SCA-APP-010. The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; unrendered helper tests do not prove current route behavior, and this record does not silently retire that contract. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

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

The 2026-07-12 UPD-105/106 dependency/header observations describe their then-current source. The dependency register now exists; the old PORTAL header active-state test does not establish the headerless SCA-APP-010 shell. Dependency extraction ran under D-APP-109/D-APP-110 on 2026-09-05. `Dependencies.csv` is the formal extracted register; consult each edge and gate directly. This record repair neither changes an edge nor infers satisfaction from implementation.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-02-01 Desktop Shell and Matrix Navigation

> #### Specification: DEL-02-01 Desktop Shell and Matrix Navigation
>
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
>

### CLM-009 — Scope

The current shell has a headerless Navigator, primary centre dialogue, right-panel views and an activity strip. Folder selection is per chat before its first message and fixed thereafter; current no-folder behavior is constrained by D-APP-120. New direct-entry roles are HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS; TASK is delegated. Presentation must preserve recorded identity, selected permissions and visible unavailable states.

Own navigation and presentation handoff, preserving the primary dialogue and session identity. Adjacent DEL-02-02/03 and DEL-08-02/03 retain selector, workspace and routing semantics. The old 3x4 visual matrix and loop-first pane arrangement are dated presentation history under SCA-APP-010. The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; unrendered helper tests do not prove current route behavior, and this record does not silently retire that contract.

The account-row update presentation consumes the stable update-check/handoff requirement in DEL-09-05 CLM-005. Manual, startup and six-hour unauthenticated fixed-metadata checks refuse credentials/redirects; only an explicit verified browser handoff is supported, with no automatic install, restart or publication (CONTRACT K-NET-1).

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Priority | Source | Verification |
> |---|---|---:|---|---|
> | DEL-02-01-REQ-001 | The woven shell SHALL preserve the centre dialogue as primary, with headerless Navigator and right-panel navigation under SCA-APP-010. The old PORTAL arrangement is dated history. | P0 | REF-006 Section 8.1 FR-001; SOW-001; D-APP-28/D-APP-31/D-APP-32 | Current woven-shell render/browser checks confirm primary dialogue and present navigation regions. |
> | DEL-02-01-REQ-002 | Navigation SHALL preserve current shell entry and recorded-session context. `/workbench` and `/pipeline` remain reachable, unlisted compatibility routes; their exact TYPES §4 query-intent semantics remain keyed with DEL-08-02. | P0 | REF-006 Section 8.1 FR-001; D-APP-28/D-APP-31/D-APP-32 | Current route/query checks confirm reachable unlisted aliases, recorded-session context and unknown-parameter preservation; exact TYPES §4 semantics remain open. |
> | DEL-02-01-REQ-003 | Navigation SHALL truthfully show selected chat and panel context in the headerless Navigator and woven shell. Old PORTAL header-link styling is dated evidence. | P0 | REF-006 Section 8.1 FR-001; D-APP-28 | Current Navigator/woven-shell render and browser checks confirm selection and focus state. |
> | DEL-02-01-REQ-004 | The former 3x4 visual matrix is dated presentation history under SCA-APP-010. Preserve its source identity for compatibility analysis, without imposing its geometry on the current shell. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.3 | Historical matrix UI test only; current shell geometry is checked under REQ-001. |
> | DEL-02-01-REQ-005 | Former matrix row labels and order are dated presentation history. The exact TYPES §4 row/query meaning is retained for source alignment with DEL-08-02. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.1 | Historical row-label tests only; current route/query behavior requires separate source-bound checks. |
> | DEL-02-01-REQ-006 | Former matrix column labels and order are dated presentation history. The exact TYPES §4 column/query meaning is retained for source alignment with DEL-08-02. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.2 | Historical column-label tests only; current route/query behavior requires separate source-bound checks. |
> | DEL-02-01-REQ-007 | The former NORMATIVE matrix-cell launch description is historical. Resolve the exact surviving TYPES §4 row/column query contract with DEL-08-02 before assigning a current compatibility handler. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30 | Historical matrix launch tests only; verify any surviving query contract against current route handling after alignment. |
> | DEL-02-01-REQ-008 | The former EVALUATIVE matrix-cell launch description is historical. Resolve the exact surviving TYPES §4 row/column query contract with DEL-08-02 before assigning a current compatibility handler. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30 | Historical matrix launch tests only; verify any surviving query contract against current route handling after alignment. |
> | DEL-02-01-REQ-009 | The former OPERATIVE matrix-cell Pipeline launch description is historical. Keep `/pipeline` reachable and unlisted under D-APP-108 Q3; resolve any separate TYPES §4 row/column query meaning with DEL-08-02. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-31 | Current route checks cover reachable unlisted `/pipeline`; historical matrix-cell tests do not prove a current launch handler. |
> | DEL-02-01-REQ-010 | Disabled or unsupported variants shall remain visible as coming soon rather than disappearing when encountered in matrix-adjacent navigation flows. | P0 | REF-006 Section 7.2 acceptance | UI test confirms unsupported variants are visible and non-selectable where this deliverable exposes them. |
> | DEL-02-01-REQ-011 | Stable identifiers SHALL remain distinct from paths and labels in current navigation. `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` are retained implementation evidence, pending exact TYPES §4 compatibility alignment. | P1 | REF-002 `docs/CONTRACT.md` K-ID-1 and K-PATH-1; REF-006 Section 8.2 FR-009; ADQ-13 implementation evidence | Current route/query and stable-identity checks; old matrix-key render tests are historical evidence only. |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or Source | Applicability | Status |
> |---|---|---|
> | `docs/PRD.md` | D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. | Accessible; hash is MATCH under D-APP-38 — reconciled under D-APP-38 |
> | `docs/TYPES.md` Section 4 | Canonical UI navigation vocabulary and matrix semantics | Accessible |
> | `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-INVENT-1, K-CONFLICT-1 | Stable identity and epistemic controls relevant to routing and document production | Accessible |
> | `docs/DIRECTIVE.md` Section 4.1 | In-scope statement for local desktop operation and matrix navigation | Accessible |
> | SOFTWARE_DECOMP v3.2 | Deliverable scope, SOW mapping, objective context, and execution note to preserve ResponsibleParty | Accessible |
>

### CLM-012 — Verification

Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

Verify primary-dialogue isolation, current navigation, role/permission/folder context, invalid selection refusal, local organisation and unsupported-state labels. Former matrix/loop-first tests retain historical subject attribution. The exact route/query compatibility keys remain a DEL-08-02 alignment task; missing current behavior is not proved by unrendered components. Verify update presentation against DEL-09-05 CLM-005 and its current update tests.

### CLM-013 — Documentation

> ##### Documentation
>
> Required or anticipated artifacts:
>
> - Navigation components.
> - Dated matrix UI tests, labelled historical presentation evidence; current woven-shell and route/query checks are separate.
> - Route query handling.
> - Evidence notes identifying any route-state parameters chosen by implementation.
> - ADQ-13 evidence: `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/Evidence_ADQ-13_UI_Specs_Render_Tests.md`.
> - Human ruling if the dispatch path/package rename is material to scope identity.
> - P3 disposition: selected implementation keys are documented above; source-pointer and package-path warnings remain surfaced for future governed reconciliation.
>

### CLM-014 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-105/106 are dated 2026-07-12 records: extraction existed and the old ShellFrame active-header test landed. The contradictory procedural claim that UPD-106 remained withheld is superseded by that dated evidence. Current headerless-shell verification is CLM-012.

### CLM-015 — D-APP-56 shell ownership amendment (2026-07-12)

D-APP-56 assigned direct-chat shell presentation to DEL-02-01; current role selection is the composer context line under the four-role instructions. DEL-08-02 owns routing/guarded selection; old persona-picker and isMatrixLaunchBlockedByStreaming identifiers are earlier evidence, not a current required component name. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

- **AC-001** — The DEL-02-01 Scope of Work preserves every legacy source range, has no silent claim loss, and validates under SOW_V1 for SOW-001, SOW-005, and OBJ-001.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-02-01 Desktop Shell and Matrix Navigation

> #### Procedure: DEL-02-01 Desktop Shell and Matrix Navigation
>

### CLM-017 — Purpose

Produce and verify the current woven shell while preserving primary dialogue, recorded session identity and navigation intent. The old 3x4 visual matrix and loop-first pane arrangement are dated presentation history under SCA-APP-010. The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; unrendered helper tests do not prove current route behavior, and this record does not silently retire that contract. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-018 — Prerequisites

Dependency extraction ran under D-APP-109/D-APP-110 on 2026-09-05. `Dependencies.csv` is the formal extracted register; consult each edge and gate directly. This record repair neither changes an edge nor infers satisfaction from implementation.

Read current context and reference observations, confirm the actual source candidate and retain ResponsibleParty TBD. Current conformance requires render/browser and applicable native folder/navigation evidence; old ADQ-13 slot completion does not establish current behavior.

### CLM-019 — Steps

1. Read current SCA-APP-010 scope, four-role applicability and source observations.
2. Verify headerless Navigator/dialogue/right-panel composition and recorded context.
3. Verify folder selection before the first message, fixed session identity afterward and D-APP-120 no-folder restrictions.
4. Verify local search, titles, pins/groups/archive and read-only runtime record boundaries.
5. Check native folder picker, recent documents, Finder reveal/drop and multi-root listing against actual evidence.
6. Carry the exact route/query, delegation/rung and icon/source-handoff residuals with their owners; do not infer retirement from absent UI.
7. Verify update presentation through DEL-09-05 CLM-005 without adding install/restart behavior.
8. Record source-bound render/browser/native results and remaining gaps.

Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-020 — Verification

Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

Current checks cover primary dialogue, navigation/selection, context, folder lifetime, organisation, native folder behavior and update handoff. Old 3x4 rows/columns and loop-first pane snapshots are historical checks. Surviving TYPES §4 route/query intent remains a separate current alignment/verification question, not a claimed live pass.

### CLM-021 — Implementation Evidence Slots

The ADQ-13 paths in earlier revisions are dated evidence for the former shell. Current source loci are `frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx`, `navigator.tsx` beside it, and `frontend/src/components/shell/chat-panel.tsx`. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results. Verification for unimplemented context/native/compatibility details remains open.

### CLM-022 — Records

> ##### Records
>
> - Navigation component change notes or diff references.
> - Dated matrix UI test results, labelled historical presentation evidence; current woven-shell render/browser results are recorded separately.
> - Route query handling test results, with selected query key names documented.
> - Any human rulings resolving the package path mismatch, PRD hash mismatch, or PRD/SPEC/TYPES source-pointer issue.
> - This four-document kit and the TASK run record.
>

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-106 was implemented in the earlier ShellFrame active-link test; the 2026-07-12 withheld statement was stale. This does not prove the current SCA-APP-010 shell. Current checks and residual compatibility are in CLM-012/020.

- **VER-001** — Validate the DEL-02-01 candidate, generate its complete claim map and parity report, and derive its deterministic review checklist.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-02-01 Desktop Shell and Matrix Navigation

> #### Guidance: DEL-02-01 Desktop Shell and Matrix Navigation
>
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
>

### CLM-025 — Purpose

The current shell has a headerless Navigator, primary centre dialogue, right-panel views and an activity strip. Folder selection is per chat before its first message and fixed thereafter; current no-folder behavior is constrained by D-APP-120. New direct-entry roles are HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS; TASK is delegated. Presentation must preserve recorded identity, selected permissions and visible unavailable states. The old 3x4 visual matrix and loop-first pane arrangement are dated presentation history under SCA-APP-010. The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; unrendered helper tests do not prove current route behavior, and this record does not silently retire that contract. The purpose remains clear governed navigation without changing Runtime ownership or project truth.

### CLM-026 — Principles

Keep the primary dialogue invariant, distinguish recorded session state from local convenience state, and preserve stable identity across label/path changes. Use the current four-role entry model and visible unavailable states. The old 3x4 visual matrix and loop-first pane arrangement are dated presentation history under SCA-APP-010. The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; unrendered helper tests do not prove current route behavior, and this record does not silently retire that contract. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-027 — Considerations

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. The old 3x4 visual matrix and loop-first pane arrangement are dated presentation history under SCA-APP-010. The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; unrendered helper tests do not prove current route behavior, and this record does not silently retire that contract. DEL-08-02 owns routing/guarded selection; DEL-02-02/03 own adjacent right-panel/workspace presentation. Implementation parameter names are evidence, not fresh authority.

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

A new chat chooses its folder and permitted direct-entry role in the composer; after its first message that folder identity is fixed. Selecting a recorded chat preserves primary-dialogue and replay isolation. Legacy matrix row/column deep links remain the exact keyed compatibility question with DEL-08-02. Check current navigation/folder cases in CLM-012; no automatic legacy-route restoration is ordered.

### CLM-030 — Conflict Table (for human ruling)

The live package folder and stable DEL-02-01 identity are established; the older dispatch-label mismatch is history. Earlier PRD MATCH/warning and FR-008/SPEC-pointer conflicts are source snapshots, not current acceptance. The surviving exact TYPES §4 route/query compatibility, icon direction/reproducibility and missing context-field questions remain in current Remaining with their actual owning decisions. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-001 SOW-005 OBJ-001 | SCA-APP-010 Gate-5 Current Contract; CLM-008 | AC-001 | VER-001 | Woven Dialogue shell evidence, compatibility parity, provenance and primary-dialogue isolation checks |

## Retired status detail (2026-09-23)

These clauses retain the operative meaning of the named App `Remaining` entries after their one-time retirement. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R013:** Use the Stone palette, measured text/control contrast, left-panel wordmark and current plain-language composer copy under D-APP-108 and the four-role/D-GOV-43 contract.

- **APP-R015:** The session list spans registered known roots with a truthful folder per chat; the active provider root derives from the session registered project identity. Known roots are local convenience state, not a new Runtime root field.

- **APP-R016:** D-APP-108 seats the application icon and defers the pop-out panel. Preserve the owner removal direction for the old renderer icon and the design-source to raster/package integrity handoff with DEL-09-04; exact artwork ownership is a deferred App decision.

- **APP-R017:** The shell acceptance includes current wordmark/copy, Finder and Dock folder actions, route/query/update consumers and source-artwork to packaged-icon trace. DEL-08-02 carries routing and DEL-09-04 carries packaging evidence; unresolved icon-source ownership is deferred in App Task Management.
