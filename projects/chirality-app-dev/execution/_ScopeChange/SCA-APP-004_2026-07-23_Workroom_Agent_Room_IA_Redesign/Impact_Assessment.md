# SCA-APP-004 Impact Assessment — Workroom and Agent Room IA Redesign

**Status:** `GATE_2_ACCEPTED_CONCEPT_SELECTION_HOLD`
**Date:** `2026-07-23`
**Assessment basis:** owner-confirmed Gate-1 action envelope plus three
independent read-only lenses covering authority/decomposition,
frontend/runtime compatibility, and UX/accessibility/migration.
**Expected decision ID at Gate 5:** `D-APP-74`, subject to a fresh register
check when the ruling is authored.

## 1. Impact verdict

The requested change is feasible inside the existing 10-package /
51-deliverable topology. It requires prospective amendment of accepted
frontend information-architecture contracts, but it does not require a new
package, new deliverable, runtime capability, lifecycle transition, release
claim, or authority transfer.

The maximum authorized design envelope is:

1. a calm artifact-centred Workroom;
2. a semantic Agent Room built only from existing session, replay,
   interruption, attribution, permission, and bounded AgentRun evidence;
3. retention of current routes, query parameters, browser APIs, SSE names,
   provider composition, and stored operator state during a compatibility
   period;
4. one of three comparable concepts: Workroom-first, Agent-Room-first, or a
   hybrid;
5. non-destructive migration, with the current loop-first interface retained
   until separately accepted for retirement.

The concept-selection hold occurs after acceptance of this assessment and
before Gate 3. During that hold, concept artifacts are non-authoritative.
Withholding Gate-3 confirmation is the pause mechanism; it does not create a
new governance state.

## 2. Impact summary

| Action | Directly affected authority | Implementation and workflow impact |
|---|---|---|
| A001 — `OBJ-001` | PRD/DIRECTIVE/CONTRACT/SPEC/TYPES and decomposition objective wording | Reframe product success around governed artifact work and semantic operator state; preserve human authority and project-truth rules. |
| A002 — `SOW-001` | Decomposition and app authority | Replace the fixed three-surface shell clause with selected Workroom/Agent Room composition plus compatibility requirements. |
| A003 — `SOW-004/006/007/008` | Decomposition and affected deliverable contexts | Decouple layout, Workbench, Pipeline, toolkit, and local-state functions from current pane/route presentation without removing their semantics. |
| A004 — `SOW-005` | Decomposition, matrix/persona decisions, routing tests | Keep semantic routing available during compatibility; final `MODIFY` versus non-destructive `RETIRE` waits for concept selection. |
| A005 — `PKG-02` | Package scope and WORKING_ITEMS plan | PKG-02 remains shell integration owner; its scope becomes Workroom shell, artifact navigation/canvas, operator state, compatibility, and non-authoritative UI state. |
| A006 — `DEL-02-01/02/04` | Deliverable ScopeOfWork, contexts, status/remaining records | Reframe shell, re-hosted Pipeline/Workbench presentation, and versioned layout persistence. No lifecycle change. |
| A007 — `DEL-05-04` | Replay/transcript view responsibility and reliance boundary | Add only a rebuildable Agent Room projection over canonical evidence; do not make the projection authoritative or create new runtime behavior. |
| A008 — `DEL-08-02` | Persona/matrix routing presentation and related decisions | Final `MODIFY` versus non-destructive `RETIRE` waits for concept selection; semantic compatibility remains until an explicit retirement decision. |
| A009 — `DEL-08-03` | Dispatch presentation and DEL-02-02 shared boundary | Preserve DECOMP/PREP/TASK/AUDIT semantics; DEL-08-03 owns dispatch semantics and DEL-02-02 consumes/presents them. |

## 3. Current-state drift disposition

Implementation drift is disclosed as a condition to resolve, not ratified by
this assessment.

| Surface | Accepted state | Live state | Gate-2 treatment |
|---|---|---|---|
| Primary shell | PORTAL/PIPELINE/WORKBENCH three-surface framing | Loop-first, chat-dominant routes | Interim compatibility baseline only; replace under the selected concept. |
| Matrix routing | Canonical 3x4 routing view | Rectangular sidebar tab with query-param launch | Preserve compatibility during migration; final disposition waits for concept selection. |
| Chat loop shells | Not the accepted permanent IA | Primary live surface | Retain until parity and owner acceptance; do not treat as target architecture. |
| Workbench/Pipeline functions | Accepted | Present and re-hostable | Preserve semantics, tests, and query handling while changing presentation. |
| File tree/scope scan | Accepted | Present | Retain and elevate into the Workroom. |
| Toolkit/operator state | Accepted | Present | Retain; migrate layout state non-destructively. |
| `app-shell.tsx` | Shell-adjacent artifact | Implemented but unused by normal routes | Rework its resizing/persistence mechanics or deliberately remove it in the implementation tranche; do not reactivate unchanged. |
| Providers/API/SSE | Accepted | IA-agnostic and live | Retain unchanged through this SCA. |

## 4. Decomposition treatment

| Entity | Gate-5 treatment if the selected concept stays inside the envelope |
|---|---|
| `OBJ-001` | `MODIFY` — remove fixed primary-surface taxonomy and state artifact-centred governed work. |
| `SOW-001` | `MODIFY` — selected shell plus compatibility-period obligation. |
| `SOW-004` | `MODIFY` — professional layout and non-authoritative convenience state. |
| `SOW-005` | `MODIFY` or non-destructive `RETIRE`, selected at the concept gate. |
| `SOW-006/007/008` | `MODIFY` — retain functions, decouple fixed presentation. |
| `SOW-002/003/011/013/023/040` | `NO_CHANGE`. |
| `PKG-02` | `MODIFY`; package retained. |
| `DEL-02-01/02/04` | `MODIFY`. |
| `DEL-02-03/05`, `DEL-03-03` | `NO_CHANGE`; remain consumers or compatibility owners. |
| `DEL-05-04` | Narrow `MODIFY` for evidence-linked projection only. |
| `DEL-08-02` | `MODIFY` or non-destructive `RETIRE`, selected at the concept gate; never repurpose the ID. |
| `DEL-08-03` | `MODIFY`; dispatch semantics retained. |

No entity is added, moved, merged, split, or renumbered. If concept selection
requires a new stable navigation deliverable or a change to the 10/51
topology, this SCA returns to Gates 1–2.

## 5. Derivative-package status

| Package | Owner after amendment | Status after amendment | Required rerun or closure |
|---|---|---|---|
| `PKG-02` | Existing WORKING_ITEMS manager; one serialized shell integration owner | `IN_PROGRESS`, no lifecycle change | Replan affected deliverables; component/render, route/query, storage migration, accessibility, responsive, build and packaged Desktop validation. |
| `PKG-05` | Existing WORKING_ITEMS manager for `DEL-05-04` | `IN_PROGRESS`, no lifecycle change | Replay, interruption, event ordering, attribution, bounded-buffer and projection correctness tests. |
| `PKG-08` | Existing WORKING_ITEMS manager for `DEL-08-02/03` | `IN_PROGRESS`, no lifecycle change | Persona/query compatibility, dispatch semantics, disabled-state, and delegation-truth regression. |
| `PKG-03` | No ownership change; `DEL-03-03` remains API/SSE adapter owner | `IN_PROGRESS`, unchanged | Compatibility regression only; no contract edit unless Gate 5 discovers a contradiction. |
| `PKG-09` | No ownership change | `IN_PROGRESS`, unchanged | Packaged Electron smoke and security boundary validation only. |

All other packages remain `NO_CHANGE`. No Checking Approval SHA, professional
reliance state, issuance state, release state, or acceptance role changes.

## 6. Derivative-surface classification

| Surface | Class | Authority basis and Gate-5 action |
|---|---|---|
| Six app authority documents (`PRD`, `DIRECTIVE`, `CONTRACT`, `SPEC`, `TYPES`, decomposition) | `DIRECT_EDIT` | Their current frontend clauses must describe the selected IA consistently. |
| App decision register plus new ruling | `DIRECT_EDIT` | Mint the next free ID, expected `D-APP-74`, with prospective supersession only. |
| `docs/harness/reliance_boundary_register.md` | `DIRECT_EDIT` | Record the Agent Room as a rebuildable view over canonical session/AgentRun evidence. |
| Affected deliverable `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md` and package planning records | `DIRECT_EDIT` | Reconcile responsibilities and Remaining work without lifecycle transitions. |
| Browser routes, `/api/harness/*`, deliverable/content APIs, public SSE names | `NO_CHANGE` | Existing compatibility constraint remains binding in this SCA. |
| Runtime contracts and daemon/core packages | `NO_CHANGE` | The UI consumes current capability; frontend convenience does not authorize runtime expansion. |
| Decomposition coverage and instruction-root checks | `RECOMPUTE` | Run after Gate-5 propagation and again after implementation. |
| Contract-pull and authority-corpus validation | `RECOMPUTE` | Required after authority edits. |
| Component/render, a11y, runtime regression, build and packaging evidence | `RECOMPUTE` | Required after implementation and before retirement consideration. |
| Root/domain/PEC governance | `NO_CHANGE` | PEC-derived project control plane remains explicitly deferred. |

## 7. Prospective decision supersession

Historical records remain unchanged. Gate 5 must state prospective
supersession only where presentation clauses conflict with the selected
concept.

| Decision | Prospective treatment |
|---|---|
| `D-APP-28` | Supersede the clause making the live loop the permanent primary application surface; preserve the historical pivot and compatibility evidence. |
| `D-APP-30` | Supersede exact matrix-cell/in-place launch presentation only if the selected concept replaces it; preserve mid-turn safety and launch-guard semantics. |
| `D-APP-31` | Supersede exact Pipeline tertiary-screen presentation; preserve dispatch behavior and disabled-state semantics. |
| `D-APP-32` | Supersede exact sidebar-tab placement; preserve access to the underlying functions during compatibility. |
| `D-APP-56` P07 | Supersede toolkit location/presentation only; preserve permission, enforcement, and evidence substance. |
| `D-APP-70` | Preserve the accepted physical/integration ownership mappings and shared-file boundaries. Gate 5 may update their application record only where source paths actually change; it must not claim unperformed mappings. |
| `D-APP-73` | Retain unchanged. The shared runtime and daemon-client boundary govern the redesign. |

## 8. Runtime and compatibility ceiling

| Contract | Required treatment |
|---|---|
| Routes `/`, `/chat`, `/pipeline`, `/workbench` | Continue resolving through the compatibility period. A feature gate or parallel shell may choose the presentation without breaking deep links. |
| Query parameters | Preserve `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, `targetDeliverableKey`, and unknown parameters. |
| Browser APIs | Preserve `/api/harness/*`, working-root, content, deliverable, and lifecycle route shapes. |
| SSE | Preserve public event names, ordering, replay frame shapes, and terminal semantics. `OperatorProjection` consumes but never redefines them. |
| Provider composition | Keep `WorkspaceProvider`, `DeliverablesProvider`, `ToolkitProvider`, and `HarnessEventsProvider` as singletons above shell switching. |
| Stored state | Preserve `chirality.projectRoot`, `chirality.toolkit.v1`, chat-draft keys, and `chirality.layout.v1`; introduce versioned layout state with forward migration and rollback-safe retention. |
| Credentials/settings | Keep runtime and provider settings reachable; never expose credentials to the renderer. |
| Desktop boundary | Normal GUI remains a daemon client; fixed project token, socket authorization, and packaged startup stay unchanged. |

The Agent Room may show only evidence the current contracts support:

- session role and parentage;
- status and terminal outcome;
- engine, provider, actual model, and residency epoch when present;
- canonical activity and replay;
- interruption and permission evidence;
- the current bounded Agent 1 / one optional read-only Agent 2 pilot.

It must not imply arbitrary Agent 0/1/2 graphs, multiple-child concurrency,
general delegation, scheduling, cross-project control, automatic model
routing, or model-residency authority. Full run-card discovery also remains
bounded because the runtime does not yet expose a global AgentRun list/replay
API.

## 9. Concept-tranche envelope

After Gate-2 acceptance, non-authoritative evidence may be written beneath:

`projects/chirality-app-dev/plans/artifacts/WORKROOM_AGENT_ROOM_CONCEPTS_<timestamp>/`

Every artifact must be marked `NON_AUTHORITATIVE — CONCEPT EVIDENCE`.

Required outputs:

1. current journey audit;
2. current/published-component salvage assessment;
3. three comparable concept packets:
   - Workroom-first;
   - Agent-Room-first within the runtime ceiling;
   - hybrid Workroom with a peer Agent Room;
4. comparison matrix and owner decision memo;
5. keyboard/accessibility direction;
6. state, migration, performance, and compatibility notes.

Minimum artifact types are Markdown/text, Git diff, deliverable view, agent
return/evidence, validation result, and session/replay transcript. PDF,
drawing, rich-binary editing, PEC inbox/control-plane functions, and any new
runtime capability are deferred.

Task-based evaluation must cover:

- find and inspect a deliverable;
- read or compare an artifact while a turn runs;
- launch a TASK-scoped Pipeline action;
- review canonical agent evidence and model attribution;
- recover state after relayout/restart;
- interrupt a turn.

Accessibility evaluation must cover keyboard region traversal, tree and tab
semantics, keyboard-operable resizers, focus restoration, landmarks,
non-colour status communication, restrained live regions, reduced motion,
accessible diff semantics, and WCAG AA contrast.

## 10. Migration, performance, and retirement

- Reuse the calm token foundation in `globals.css`.
- Treat the dormant `app-shell.tsx` and its layout mechanics as rework
  candidates, not production-ready architecture.
- Centralize working-root polling rather than multiplying polling by pane.
- Keep tree loading bounded and lazy.
- Cap or virtualize large artifacts, diffs, event histories, and Agent Room
  projections.
- Build `OperatorProjection` incrementally from canonical events and make it
  rebuildable; it may not overwrite session or AgentRun evidence.
- Preserve old layout and draft values through versioned forward migration.

The old UI may be retired only after route/query/API/SSE compatibility,
task-scenario parity, accessibility, state migration, performance, runtime
regression, packaged Electron smoke, and explicit owner acceptance. Retirement
is not authorized by this SCA's current action envelope and must be recorded
separately.

## 11. Orphan and reliance risk

| Risk class | Current count | Treatment |
|---|---:|---|
| Missing package/deliverable entities | 0 | No action. |
| Deliverable folder/context closure defects in affected packages | 0 | No action. |
| Pre-change folder-local artifact-index warnings | 15 | Carry as warnings; do not infer source ownership from folder locality. |
| Deferred final dispositions | 2 (`SOW-005`, `DEL-08-02`) | Resolve at owner concept selection. |
| Known shared-ownership ambiguity | 1 (`SOW-007`) | Gate 5 records DEL-08-03 semantic ownership and DEL-02-02 presentation consumption. |
| Known traceability omission outside direct IA semantics | 1 (`DEL-02-05` / `SOW-023`) | Preserve as an observation; repair only if authority reconciliation confirms it is in scope. |
| Potential runtime-capability orphan created by this SCA | 0 | Maintained by the explicit capability ceiling. |

## 12. Estimate and schedule risk

The redesign is a multi-tranche frontend program rather than a cosmetic pass.
The primary schedule risks are:

- concept churn before the owner freezes a layout;
- compatibility code living too long beside the new shell;
- shared-file contention in shell composition and `globals.css`;
- large artifact/event rendering;
- accidental capability claims beyond the runtime;
- state migration or packaged-Electron regressions.

Mitigations are the owner concept-selection gate, one serialized shell/type/
style integration owner, disjoint component work packages, a compatibility
matrix, read-only first integration, bounded projection, and staged validation.
No calendar estimate is authoritative at Gate 2.

## 13. Active snapshot, pause, and rebaseline rules

- SCA-APP-003 is closed with owner-accepted `CLOSED_WITH_OBSERVATIONS` evidence.
- SCA-APP-004 is the single active scope-change snapshot.
- After Gate-2 acceptance, the run pauses before Gate 3 while concept evidence
  is produced and selected.
- The concept tranche may not edit decomposition or authority.
- Work touching the assessed decomposition surfaces should remain frozen
  during the hold. If the baseline moves, Gate 1 coverage and a Gate-2 delta
  check must be rerun before Gate 3.
- If the selected concept exceeds this union envelope, changes topology,
  breaks compatibility, expands runtime capability, or authorizes old-UI
  retirement, return to Gates 1–2.
- The pause, exit conditions, selected concept, and any rebaseline must be
  recorded in `Decision_Log.md`.

## 14. Recommended reruns

After Gate-5 authority propagation:

1. authority-corpus reconciliation;
2. `AUDIT_DECOMP` over PKG-02, PKG-05, and PKG-08;
3. instruction-root integrity;
4. contract-pull validation;
5. reliance-boundary and decision-register checks;
6. affected deliverable context/status validation.

After implementation:

1. component and render suites;
2. route/query/deep-link regression;
3. API/SSE/replay/interruption regression;
4. layout and draft-state migration tests;
5. keyboard and accessibility audit;
6. large tree/artifact/diff/event performance checks;
7. runtime and provider regression;
8. full build, premerge, secret scan, network-policy proof;
9. `desktop:pack` and packaged Desktop smoke;
10. independent evaluation and owner acceptance.

## Gate-2 question

Does the owner accept this impact assessment as the maximum envelope for the
three-concept tranche and the later governed amendment?

**Owner response:** Accepted on 2026-07-23.
