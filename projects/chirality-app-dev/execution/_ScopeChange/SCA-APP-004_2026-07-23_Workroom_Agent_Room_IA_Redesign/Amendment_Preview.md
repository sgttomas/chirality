# SCA-APP-004 Amendment Preview

**Gate:** 3 — Amendment Approval
**Status:** `PENDING_HUMAN_APPROVAL`
**Date:** `2026-07-23`
**Selected concept:** Woven Dialogue with Work/Agents Coordination Panel
**Topology:** unchanged — 10 packages / 51 deliverables
**Lifecycle:** unchanged

This is the exact proposed amendment to
`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
No decomposition or authority file has yet been changed.

## Selected product constraints

- The real human–agent dialogue is the primary workspace.
- Shared intent is emergent and is not a stored, authoritative, or required UI
  object.
- Artifacts and evidence may appear as provenance-bearing inline objects and
  open into focus views that return to their dialogue anchor.
- Visible artifacts are not automatically next-turn model context.
- The right Coordination Panel toggles between Work and Agents.
- Work displays plans/task lists only when explicitly recorded and always
  distinguishes governed, human-approved, agent-authored, and ephemeral
  runtime work.
- Agents displays only recorded sessions and exact canonical parentage.
- Selecting a recorded session may replace the main region's visible content
  with a clearly labelled, read-only replay lens. It does not resume, switch,
  merge with, or mutate the primary live dialogue.
- The primary live dialogue remains mounted and retains its own draft,
  attachments, context, permissions, interruption state, and interaction
  authority. A persistent action returns the operator to it.
- Runtime expansion, global AgentRun discovery, arbitrary graphs, scheduling,
  direct child messaging, and automatic intent summarization remain excluded.

## Common coordination-projection invariant

The Work/Agents Coordination Panel is a rebuildable projection over admitted
project and runtime records. Rendering, grouping, linking, filtering,
selecting, or locally annotating a plan, task, status, assignment, session, or
relationship does not create project truth, approve a plan, assign authority,
transition lifecycle, authenticate a human act, or change runtime state. The
admitted source remains controlling. Missing, stale, conflicting, or
unrecorded relationships remain explicitly unknown.

All session, role, status, parentage, task, plan, return, approval, model, and
workflow presentations are evidence-conditional. Missing optional fields
render as absent or unknown; contradictory sources remain
provenance-labelled; and frontend projections never synthesize runtime
authority or overwrite canonical session, event, AgentRun, filesystem, or Git
evidence.

Structured Work items must identify their source class and source reference,
status basis, currency, and any recorded responsible or related references.
Governed project records, human-approved execution bases, agent proposals, and
ephemeral runtime state remain visibly distinct. Conversational prose is never
silently converted into a structured plan or task, and runtime completion is
never presented as deliverable acceptance.

## 1. Decision Log / Change Log

### Add decision row

```markdown
| DEC-020 | 2026-07-23 | SCA-APP-004 replaces the fixed surface/matrix target UI with owner-selected Woven Dialogue and a Work/Agents Coordination Panel while preserving routing, dispatch, runtime, compatibility, and human-authority boundaries. | The owner selected dialogue as the primary human–agent collaboration surface; structured work and agent hierarchy remain evidence-conditional projections, with no topology, runtime capability, lifecycle, or old-UI retirement change. |
```

### Add change-log entry

```markdown
- 2026-07-23: SCA-APP-004 prospectively selected Woven Dialogue with a Work/Agents Coordination Panel, replacing fixed target-shell presentation while preserving legacy route/query/matrix compatibility, runtime capability limits, and the existing package/deliverable topology.
```

## 2. SSOW amendments

### `SOW-001`

**Before**

```markdown
| SOW-001 | IN | REF-006 Section 8.1 | Provide a desktop shell with PORTAL, PIPELINE, and WORKBENCH navigation. | Current baseline preserved. |
```

**After**

```markdown
| SOW-001 | IN | REF-006 Section 8.1 | Provide a dialogue-centred desktop shell with persistent human–agent conversation, provenance-bearing artifact views, and Work/Agents coordination surfaces. | Existing routes and the loop-first UI remain compatibility surfaces until separately retired; shared intent is not a stored UI object. |
```

### `SOW-004`

**Before**

```markdown
| SOW-004 | IN | REF-006 Section 8.1, Section 8.7 | Support professional pane layout, resize/collapse, and local UI state. | Local state is non-authoritative. |
```

**After**

```markdown
| SOW-004 | IN | REF-006 Section 8.1, Section 8.7 | Support professional resizable Navigator, dialogue, coordination, artifact-focus, and activity layouts with versioned local UI state. | Layout, focus, transcript selection, anchors, and panel state are non-authoritative convenience state and migrate non-destructively. |
```

### `SOW-005`

**Before**

```markdown
| SOW-005 | IN | REF-006 Section 8.2, REF-004 Section 4 | Render canonical 3x4 matrix and route cells by row semantics. | NORMATIVE/EVALUATIVE to WORKBENCH; OPERATIVE to PIPELINE. |
```

**After**

```markdown
| SOW-005 | IN | REF-006 Section 8.2, REF-004 Section 4 | Preserve semantic agent/session routing, guarded dialogue selection, canonical aliases, and legacy matrix-route compatibility without requiring a fixed matrix in the target shell. | Legacy matrix/query behavior remains compatible; hierarchy and replay evidence retain their separate semantic owners. |
```

### `SOW-006`

**Before**

```markdown
| SOW-006 | IN | REF-006 Section 8.2 | Present active WORKBENCH agent context from route state. | Includes selected agent, row, and column. |
```

**After**

```markdown
| SOW-006 | IN | REF-006 Section 8.2 | Present active dialogue/persona context and a Work/Agents Coordination Panel over explicitly recorded work, canonical session parentage, and selectable recorded-session replay. | The selected-session replay lens is read-only and distinct from the mounted primary live dialogue; missing plans, tasks, relationships, or transcripts remain explicitly absent or unknown. |
```

### `SOW-007`

**Before**

```markdown
| SOW-007 | IN | REF-006 Section 8.2 | Expose PIPELINE category and task-scope selectors. | Unsupported options visible and disabled. |
```

**After**

```markdown
| SOW-007 | IN | REF-006 Section 8.2 | Expose presentation-neutral PIPELINE category and task-scope controls for DECOMP/PREP/TASK/AUDIT dispatch. | Unsupported options remain visible and disabled; DEL-08-03 retains dispatch semantics independently of Coordination Panel presentation. |
```

### `SOW-008`

**Before**

```markdown
| SOW-008 | IN | REF-006 Section 8.7 | Expose per-turn toolkit options and preserve local drafts/presets. | Must not override runtime governance. |
```

**After**

```markdown
| SOW-008 | IN | REF-006 Section 8.7 | Expose per-turn toolkit options and preserve dialogue drafts, presets, explicit next-turn context references, artifact anchors, and panel selections as local convenience state. | Visible artifacts are not automatically model context; local state must not override runtime governance, rewrite sent-turn history, or transfer primary-session context to a selected replay. |
```

## 3. Objective amendment

### `OBJ-001`

**Before**

```markdown
| OBJ-001 | Preserve a governed local desktop harness with clear WORKBENCH, PIPELINE, PORTAL, file-tree, toolkit, and operator-state behavior. | SOW-001-SOW-008, SOW-023 | UI and operator workflow objective. |
```

**After**

```markdown
| OBJ-001 | Provide a governed local desktop harness centred on actual human–agent dialogue, with explicit turn context, provenance-bearing inline and focused artifacts, recorded Work/Agents coordination, and evidence-derived supervision. | SOW-001-SOW-008, SOW-023 | Dialogue, artifact collaboration, and operator workflow objective; shared intent remains emergent rather than a stored UI authority object. |
```

## 4. Package amendment

### `PKG-02`

**Before**

```markdown
| PKG-02 | Desktop Shell, Navigation, and Operator State | User-facing shell, matrix routing, file tree, toolkit, API key UI, local UI state. | UI and operator workflow behavior. | Runtime engine internals. |
```

**After**

```markdown
| PKG-02 | Woven Dialogue Shell, Navigation, and Operator State | Dialogue-centred shell, Woven Dialogue artifact presentation, Navigator, Work/Agents Coordination Panel, activity shelf, re-hosted Workbench/Pipeline/toolkit/settings, compatibility surfaces, and non-authoritative local UI state. | Human–agent dialogue, artifact collaboration, coordination presentation, and operator workflow behavior. | Runtime engine internals, canonical session/evidence ownership, arbitrary orchestration graphs, automatic intent inference, and project-control-plane authority. |
```

## 5. Deliverable amendments

### `DEL-02-01`

**Before**

```markdown
| DEL-02-01 | Desktop Shell and Matrix Navigation | TBD | UX_UI_SLICE | Maintain PORTAL, WORKBENCH, and PIPELINE shell navigation and canonical matrix routing. | Navigation components; matrix UI tests; route query handling | SOW-001, SOW-005 | OBJ-001 | M | One UI domain with several route states. |
```

**After**

```markdown
| DEL-02-01 | Woven Dialogue Shell and Compatibility Navigation | TBD | UX_UI_SLICE | Compose the persistent primary human–agent transcript and composer, provenance-bearing inline/focused artifact views, Navigator, Work/Agents Coordination Panel, Activity Shelf, and compatibility navigation without creating a second evidence store. | Dialogue shell; inline artifact/focus views; Work/Agents panel; activity shelf; route/query and compatibility tests | SOW-001, SOW-005 | OBJ-001 | M | Shell integration owns presentation only; work, hierarchy, transcript, and artifact facts remain governed by their existing semantic owners. |
```

### `DEL-02-02`

**Before**

```markdown
| DEL-02-02 | Workbench and Pipeline Selection UX | TBD | UX_UI_SLICE | Preserve active agent context, category controls, task-scope selectors, and disabled coming-soon variants. | Workbench context UI; pipeline selector behavior; stale selection tests | SOW-006, SOW-007 | OBJ-001 | M | Coherent navigation/routing slice. |
```

**After**

```markdown
| DEL-02-02 | Work/Agents Coordination, Workbench, and Pipeline UX | TBD | UX_UI_SLICE | Re-host Workbench and Pipeline around central dialogue and present explicitly recorded plans/tasks and agent/session selections with source, authority class, responsible reference, currency, and evidence while preserving disabled states and deep-link intent. | Workbench/Pipeline views; Work/Agents coordination presentation; provenance labels; stale/empty-state and query compatibility tests | SOW-006, SOW-007 | OBJ-001, OBJ-007 | M | DEL-08-02 retains routing, DEL-08-03 retains dispatch, DEL-08-05 retains child records, and DEL-05-04 retains replay/projection semantics; this deliverable only composes their presentation. |
```

### `DEL-02-04`

**Before**

```markdown
| DEL-02-04 | Toolkit Options and Local UI State | TBD | UX_UI_SLICE | Expose runtime options and preserve pane layout, drafts, and local presets as non-authoritative convenience state. | Toolkit controls; pane resize/collapse state; draft/preset storage guards | SOW-004, SOW-008, SOW-016 | OBJ-001, OBJ-004 | S | Focused local UI state slice. |
```

**After**

```markdown
| DEL-02-04 | Dialogue Toolkit, Context, and Local UI State | TBD | UX_UI_SLICE | Expose runtime options and preserve versioned layout, drafts, explicit next-turn context references, artifact anchors, selected replay references, panel state, and local presets as non-authoritative convenience state with rollback-safe migration. | Toolkit controls; workspace-state schema; resize/focus/anchor behavior; context-reference, draft/preset, and migration guards | SOW-004, SOW-008, SOW-016 | OBJ-001, OBJ-004 | S | Convenience state stores references and presentation only; it never stores authoritative workflow, hierarchy, permission, or acceptance conclusions. |
```

### `DEL-05-04`

**Before**

```markdown
| DEL-05-04 | Runtime Replay and Transcript View | TBD | BACKEND_FEATURE_SLICE | Reconstruct accepted turns, assistant output, tool summaries, terminal states, and SDK transcript links from Chirality events. | Replay parser; transcript reconstruction tests; malformed-tail tests | SOW-042, SOW-046 | OBJ-003 | M | Replay/reporting slice over one event store. |
```

**After**

```markdown
| DEL-05-04 | Runtime Replay, Dialogue, and Agent Transcript Projection | TBD | BACKEND_FEATURE_SLICE | Reconstruct accepted turns, recorded-session transcript/replay, tool summaries, terminal states, attribution, and evidence-conditioned Agent projections from canonical Chirality records without replacing the primary dialogue or evidence store. | Replay parser; transcript reconstruction; bounded/stale projection; selected-session read-only replay lens; exact-parentage and malformed-tail tests | SOW-006, SOW-042, SOW-046 | OBJ-001, OBJ-003 | M | Projection is rebuildable and provenance-labelled; live versus replayed state and primary versus observational interaction authority remain explicit. |
```

### `DEL-08-02`

**Before**

```markdown
| DEL-08-02 | Persona Alias and Agent Matrix Routing Contract | TBD | UX_UI_SLICE | Keep UI aliases, canonical agent names, matrix routes, and persona resolution consistent. | Alias resolver tests; route fixtures; matrix mapping tests | SOW-005, SOW-006, SOW-017 | OBJ-001, OBJ-007 | S | Focused routing/alias slice. |
```

**After**

```markdown
| DEL-08-02 | Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract | TBD | UX_UI_SLICE | Keep UI aliases, canonical agent names, persona resolution, guarded dialogue/session selection, route/query mappings, and legacy matrix behavior consistent. | Alias resolver tests; guarded session-selection tests; route/query fixtures; legacy matrix compatibility and unavailable-persona tests | SOW-005, SOW-006, SOW-017 | OBJ-001, OBJ-007 | S | Does not own shell presentation, work-plan authority, dispatch semantics, replay evidence, or parent-child records. |
```

### `DEL-08-03`

**Before**

```markdown
| DEL-08-03 | Pipeline Category and Task Scope Dispatch | TBD | UX_UI_SLICE | Dispatch DECOMP/PREP/TASK/AUDIT lanes and dynamic task scope from deliverables and knowledge-type buckets. | Pipeline selector tests; knowledge-type discovery; disabled option handling | SOW-007, SOW-026 | OBJ-001, OBJ-007 | M | UI dispatch slice tied to agent architecture. |
```

**After**

```markdown
| DEL-08-03 | Pipeline Category and Task Scope Dispatch | TBD | UX_UI_SLICE | Own presentation-neutral DECOMP/PREP/TASK/AUDIT lane semantics, category/task-scope interpretation, dynamic scope, and disabled-option rules for contextual Run consumers. | Dispatch contract tests; Pipeline selector tests; knowledge-type discovery; dynamic-scope and disabled-option handling | SOW-007, SOW-026 | OBJ-001, OBJ-007 | M | Semantic dispatch owner; DEL-02-02 owns presentation and may not infer plans/tasks from conversational prose. |
```

## 6. Scope Ledger amendments

Only these row fields change. Stable IDs, `IN` status, source refs, decision
refs, and objective mappings remain.

| Scope item | New `ScopeItemStatement` | Package / deliverable mapping | New note |
|---|---|---|---|
| `SOW-001` | Woven Dialogue shell with persistent transcript/composer, inline and focused artifacts, Work/Agents coordination, and secondary Agent Room presentation. | `PKG-02` / `DEL-02-01` | Existing routes and loop-first UI remain compatibility surfaces. |
| `SOW-004` | Resizable dialogue/navigation/coordination/focus layout and non-authoritative local UI state. | `PKG-02` / `DEL-02-04` | Versioned migration preserves prior state for rollback. |
| `SOW-005` | Semantic persona/agent/session routing, guarded dialogue selection, and legacy route/query/alias/matrix compatibility. | `PKG-02` / `DEL-02-01, DEL-08-02` | DEL-02-01 presents; DEL-08-02 owns aliases, routing, selection guards, and legacy compatibility. |
| `SOW-006` | Active dialogue/persona plus Work/Agents coordination over provenance-labelled recorded work, canonical hierarchy, and selected-session replay. | `PKG-02` / `DEL-02-02, DEL-05-04, DEL-08-02` | Selected replay is observational and read-only; DEL-08-05 remains the unchanged parent-child record owner. |
| `SOW-007` | Contextual Pipeline category/task-scope controls for DECOMP/PREP/TASK/AUDIT dispatch. | `PKG-08` / `DEL-08-03, DEL-02-02` | DEL-08-03 is semantic owner; DEL-02-02 is presentation consumer. |
| `SOW-008` | Toolkit, drafts, explicit next-turn context references, artifact anchors, and dialogue workspace state. | `PKG-02` / `DEL-02-04` | Visible artifacts are not automatic context; convenience state does not transfer session authority. |

### Objective traceability correction

The existing Scope Ledger maps `SOW-005`, `SOW-006`, and `SOW-017` to
`OBJ-007`, while the `OBJ-007` row lists only `SOW-030-SOW-031, SOW-063`.
Gate 5 will reconcile that row prospectively as follows without changing the
objective statement:

```markdown
| OBJ-007 | Maintain agent-suite integrity and enable governed subagent delegation without expanding authority. | SOW-005-SOW-006, SOW-017, SOW-030-SOW-031, SOW-063 | Agent governance objective. |
```

## 7. Downstream execution-note addition

```markdown
- SCA-APP-004 selects Woven Dialogue with a Work/Agents Coordination Panel as the target information architecture. Work plans/tasks are shown only from explicitly recorded sources with visible authority/provenance classes; agent hierarchy and selected-session replay are canonical-evidence-conditioned; replay is read-only and cannot mutate the mounted primary live dialogue. The tranche adds no runtime capability, does not define shared intent as a stored UI object, and preserves existing routes, query parameters, browser APIs, SSE names, provider composition, state rollback, and the loop-first UI through a compatibility period.
```

## 8. Prospective decision supersession boundaries

Historical decision files remain unchanged. The Gate-5 ruling will
prospectively supersede only:

- the fixed loop-first shell as the permanent target, fixed right-sidebar
  tertiary forms, fixed matrix-cell gateway, and fixed route/matrix
  presentation clauses of `D-APP-28`;
- the fixed matrix-cell click and `?agent=` presentation target of
  `D-APP-30`;
- the exact right-sidebar Pipeline presentation of `D-APP-31`;
- the right multi-view sidebar as mandatory gateway and exact tertiary-form
  placement of `D-APP-32`;
- only the named permanent UI location for persona picker and session controls
  in `D-APP-56` R4-P07.

It preserves those rulings' mounted-dialogue, in-flight-turn survival,
guarded-selection, governed-dispatch, deep-link, accessibility, permission,
event-contract, and no-deletion protections through the compatibility period.
`D-APP-70` integration mappings and `D-APP-73` runtime ownership remain in
force unchanged.

## 9. Semantic ownership partition

| Deliverable | Responsibility in this amendment | Explicit non-ownership |
|---|---|---|
| `DEL-02-01` | Physical shell composition, Work/Agents tabs, responsive/keyboard behavior, and cross-link presentation. | Project-plan truth, replay truth, aliases, dispatch, parentage, lifecycle, or approvals. |
| `DEL-02-02` | Re-hosted Workbench/Pipeline and Coordination Panel presentation. | Source authority, dispatch semantics, replay persistence, or child records. |
| `DEL-05-04` | Rebuildable transcript/replay and semantic runtime projection. | Project plans, approvals, assignments, aliases, dispatch, or child-record persistence. |
| `DEL-08-02` | Alias resolution, navigation intent, guarded recorded-session selection, and legacy compatibility. | Work status, dispatch, parentage, transcript persistence, or shell layout. |
| `DEL-08-03` | DECOMP/PREP/TASK/AUDIT lane and dynamic task-scope semantics. | General plan authority, shell ownership, runtime checklist truth, or child parentage. |
| `DEL-08-05` | Unchanged canonical child-run record semantics supplying exact parentage and return cross-links. | Panel UI, editable graphs, scheduling, aliases, project-plan authority, or direct child messaging. |

## 10. Acceptance impacts

- Add projection tests proving source-class and currency labels, explicit
  stale/unknown states, no synthesized work items, exact parentage/cross-links,
  separate runtime and project-lifecycle status, and no panel-authored
  approval.
- Add selected-session replay tests proving the primary live session remains
  mounted and unchanged, drafts/context/permissions do not transfer, malformed
  or bounded replay is disclosed, historical controls are disabled, and the
  operator can return to the primary dialogue.
- Preserve and rerun persona/alias/query compatibility, guarded mid-turn
  selection, Pipeline dispatch, child-run/replay, public route/API/SSE,
  accessibility, state-migration, runtime-regression, and packaged Desktop
  tests.
- Require task-based walkthroughs for artifact/dialogue collaboration,
  recorded-work inspection, agent hierarchy, replay selection, interruption,
  deep links, and recovery across relayout.
- Old-UI retirement remains a separate owner decision after parity,
  accessibility, and compatibility evidence.

## 11. Explicit no-change set

- No package or deliverable is added, removed, moved, split, merged, or
  renumbered.
- `SOW-002/003/011/013/023/040` remain unchanged.
- `DEL-02-03`, `DEL-02-05`, `DEL-03-03`, and `DEL-08-05` remain unchanged
  semantic owners/consumers.
- Runtime contracts, daemon/core packages, APIs, SSE names, credentials,
  permissions, model residency, and Agent 1/2 capability remain unchanged.
- No lifecycle, release, issuance, reliance, or old-UI retirement action occurs.
- `DEL-08-05` remains the unchanged semantic owner of canonical child-run
  records; the panel consumes but does not amend that contract.

## Gate-3 question

Does the owner approve these exact amendments to the decomposition document?
