# SCA-APP-004 Propagation Plan

**Gate:** 4 — Propagation Plan Approval
**Status:** `APPROVED`
**Date:** `2026-07-23`
**Approved amendment:** `Amendment_Preview.md`, owner-approved 2026-07-23
**Topology:** unchanged — 10 packages / 51 deliverables
**Lifecycle:** unchanged

This plan is limited to the owner-approved Gate-3 amendment. It does not apply
the amendment, authorize implementation, retire the existing UI, or expand
runtime capability.

**Owner approval:** On 2026-07-23 the owner stated, “I approve this exact
propagation plan and what it entails.”

## 1. Gate-5 authority and decomposition writes

### 1.1 Decision ruling and register

| Surface | Role | Gate-5 action |
|---|---|---|
| `execution/_Coordination/_DECISIONS/_REGISTER.md` | Authoritative companion register | Recheck the free decision ID, expected `D-APP-74`, and add the owner ruling. |
| `execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md` | Authoritative companion register | Record the selected Woven Dialogue amendment, non-authority projection invariant, compatibility posture, exclusions, and exact prospective supersession boundaries. |

The ruling will prospectively supersede only the fixed presentation clauses
identified in `Amendment_Preview.md` for `D-APP-28`, `D-APP-30`, `D-APP-31`,
`D-APP-32`, and `D-APP-56` R4-P07. Historical rulings remain unchanged.
Mounted-dialogue, in-flight-turn survival, guarded-selection,
governed-dispatch, deep-link, accessibility, permission, event-contract, and
no-deletion protections remain binding. `D-APP-70` and `D-APP-73` remain in
force unchanged.

### 1.2 App authority corpus

| Surface | Role | Gate-5 direct edit |
|---|---|---|
| `docs/DIRECTIVE.md` | Authoritative companion register | Replace the fixed matrix/PORTAL/WORKBENCH/PIPELINE target-product wording with actual dialogue, provenance-bearing artifacts, and informational Work/Agents coordination. Preserve filesystem/Git truth, human authority, runtime-event non-approval, and runtime ownership. |
| `docs/PRD.md` | Authoritative companion register | Reconcile product goals, non-goals, scope, journeys 7.2/7.4/7.5, FR-001/005/007-013, FR-041-044, replay FR-076, accessibility, acceptance checks, success metrics, known gaps, and package traceability with the approved IA and compatibility period. |
| `docs/CONTRACT.md` | Authoritative companion register | Extend existing `K-FS-1`, `K-NOMEM-1`, and `K-BIND-1` with the approved projection rule and add enforcement references for provenance, stale/unknown, exact-link, and replay-separation tests. Do not add a new `K-*` ID. |
| `docs/SPEC.md` | Authoritative companion register | Add the Woven Dialogue physical/UI contract: mounted primary live dialogue, read-only selected-session replay lens, Work/Agents admitted-source rules, explicit next-turn context references, artifact anchors, local-state migration, compatibility mechanics, and projection validation. Preserve runtime, API, SSE, session, and lifecycle contracts. |
| `docs/TYPES.md` | Authoritative companion register | Reframe matrix vocabulary as legacy compatibility and add projection-only vocabulary for `CoordinationWorkClass`, source reference, status basis, currency, responsible/related references, primary live dialogue, and selected-session replay. These are UI projection types, not an authoritative plan schema. |
| `docs/PLAN.md` | Authoritative companion register | Directly update the current-baseline UI line and product-identity/UX workstream; add the accepted SCA-APP-004 execution order. Preserve historical roadmap records and the D-APP-73 runtime sequence. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Canonical working surface | Apply the exact owner-approved changes in `Amendment_Preview.md`: DEC-020/change log, SOW-001/004-008, OBJ-001/007 traceability, PKG-02, DEL-02-01/02/04, DEL-05-04, DEL-08-02/03, Scope Ledger, and downstream execution note. |

The authority corpus will use one common rule:

> The Work/Agents Coordination Panel is a rebuildable projection over admitted
> project and runtime records. Rendering or locally organizing a plan, task,
> status, assignment, session, or relationship does not create project truth,
> approval, authority, lifecycle, or runtime state. The admitted source remains
> controlling; missing, stale, conflicting, or unrecorded relationships remain
> explicitly unknown.

Because Gate 5 extends three existing invariants rather than creating a new
one, the still-planned `contract_invariant_coverage_register.csv` retains its
existing explicitly deferred status. Gate 5 does not create a partial register
or silently claim full invariant coverage.

### 1.3 Supersession binding

Create `Supersession_Delta.csv` in this SCA snapshot with one
`SUPERSESSION` row for each of:

- `D-APP-28`: fixed loop-first/right-sidebar/matrix-gateway target clauses;
- `D-APP-30`: fixed matrix-cell and `?agent=` target interaction clauses;
- `D-APP-31`: exact right-sidebar Pipeline presentation clause;
- `D-APP-32`: mandatory right-sidebar gateway and tertiary-form placement;
- `D-APP-56` R4-P07: named permanent control-placement clause.

Each row will carry the authority path and section, original presentation fact,
replacement Woven Dialogue fact, new ruling ID, and
`BindingType=SUPERSESSION`. `D-APP-70` and `D-APP-73` receive explicit
`NO_CHANGE` treatment and no supersession row.

## 2. Reliance and delivery propagation

### 2.1 Reliance boundary

| Surface | Role | Gate-5 direct edit |
|---|---|---|
| `docs/harness/reliance_boundary_register.md` | Authoritative companion register | Add a Work/Agents projection boundary defining admitted sources, visible source/authority class, currency, exact identifiers, read-only replay, no inferred plan/task/parentage, separate runtime/project status, and no panel-authored approval. Preserve all existing runtime and professional-reliance boundaries. |

### 2.2 Affected deliverable records

Before reading or editing any `_STATUS.md`, Gate 5 will also read the sibling
`MEMORY.md` as non-authoritative operational context.

| Deliverable | Working surfaces to reconcile | Specific `_CONTEXT.md` change | `_STATUS.md` treatment |
|---|---|---|---|
| `DEL-02-01` | `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` | Replace fixed shell/matrix target with Woven Dialogue physical integration, inline/focused artifacts, Work/Agents hosting, activity shelf, and compatibility navigation; preserve semantic non-ownership. | Remain `IN_PROGRESS`; replace obsolete target-IA Remaining work with the governed implementation tranche and parity/compatibility evidence. |
| `DEL-02-02` | `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` | Add Work/Agents presentation, Workbench/Pipeline re-hosting, provenance/currency/empty-state requirements, and semantic-owner boundaries for DEL-05-04/08-02/08-03/08-05. | Remain `IN_PROGRESS`; add projection and contextual-control implementation/validation work without claiming plan or dispatch authority. |
| `DEL-02-04` | `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` | Add versioned workspace layout, mounted-dialogue preservation, drafts, explicit next-turn context references, artifact anchors, replay selection references, and rollback-safe migration. | Remain `IN_PROGRESS`; add migration, focus, keyboard, draft/context isolation, and rollback evidence. |
| `DEL-05-04` | `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` | Add read-only recorded-session replay lens, rebuildable event projection, exact parentage consumption, attribution, stale/bounded/malformed disclosure, and strict live/replay separation. | Remain `IN_PROGRESS`; replace stale replay-view Remaining wording with the approved projection and regression tranche. |
| `DEL-08-02` | `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` | Replace fixed target-matrix presentation with persona/agent/session routing, guarded recorded-session selection, aliases, and legacy route/query/matrix compatibility; state explicit non-ownership. | Remain `IN_PROGRESS`; add guarded-selection and compatibility evidence. |
| `DEL-08-03` | `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` | State presentation-neutral DECOMP/PREP/TASK/AUDIT and dynamic task-scope ownership; identify DEL-02-02 as presentation consumer. | Remain `IN_PROGRESS`; preserve dispatch behavior and add contextual-presentation regression evidence only. |

Folder names are not renamed in Gate 5. Stable deliverable IDs are controlling,
and physical folder renames would create needless migration risk before
implementation.

`DEL-08-05` is an unchanged semantic provider. Its `ScopeOfWork.md`,
`_CONTEXT.md`, `_STATUS.md`, and references are `NO_CHANGE`; Gate 5 verifies
only that the new corpus cites its existing child-record ownership correctly.

### 2.3 Package and execution planning

| Surface | Role | Treatment |
|---|---|---|
| `plans/chirality-app-future-development-plan.md` | Downstream working plan | `DIRECT_EDIT`: replace the fixed old-IA future direction with the approved concept and staged implementation/cutover order. |
| `plans/PLAN_COMPLETION_LOG.md` | Append-only completion record | `DIRECT_EDIT`: append the Gate-5 governance propagation result; do not rewrite historical loop-first entries. |
| Historical dated plans and reconciliation snapshots | Snapshot/evidence artifacts | `NO_CHANGE`: retain as historical evidence even when their target-UI statements are prospectively superseded. |
| `Amendment_Actions.csv`, `Pre_Change_Coverage.json`, `Amendment_Preview.md` | SCA snapshot/handoff artifacts | Preserve approved evidence; update only the action dispositions/status fields that are explicitly mutable in the active snapshot. |

No new package or deliverable folder is created. PROJECT_SETUP/PREPARATION is
not dispatched.

## 3. Explicit no-change surfaces

- Root, Tier-0/domain, PEC, and public-export governance.
- `AGENTS.md` and agent instruction files.
- `chirality.project.json`.
- `SOW-002`, `SOW-003`, `SOW-011`, `SOW-013`, `SOW-023`, and `SOW-040`.
- Runtime contracts, daemon/core/client/CLI packages, engine adapters,
  credentials, model residency, and Agent 1/2 capability.
- Browser API route shapes, public SSE names/order/replay frames, provider
  singleton composition, and existing deep-link query parameters.
- `DEL-02-03`, `DEL-02-05`, `DEL-03-03`, and `DEL-08-05` semantics and
  lifecycle.
- Every package and deliverable not named in Section 2.2.
- Dependencies, estimates, and schedules during direct propagation; these are
  downstream recomputations, not SCOPE_CHANGE-authored truth.
- Existing UI deletion, route retirement, lifecycle transition, release,
  issuance, publication, or professional-reliance claims.
- Automatic intent summarization, arbitrary Agent 0/1/2 graphs, multi-child
  execution, scheduling, direct child messaging, global AgentRun discovery, or
  model-routing controls.

## 4. Gate-5 validation and recomputation

### 4.1 Governance and structural validation

1. Recheck the decision register and prospective supersession bindings.
2. Reconcile `DIRECTIVE`, `PRD`, `CONTRACT`, `SPEC`, `TYPES`, `PLAN`,
   decomposition, reliance register, decision ruling, and deliverable records.
3. Refresh governed reference hashes for the six affected deliverables.
4. Run decomposition coverage and `AUDIT_DECOMP` for `PKG-02`, `PKG-05`, and
   `PKG-08`.
5. Run instruction-root integrity and contract-pull validation.
6. Validate 10-package/51-deliverable topology, ledger/objective traceability,
   folder resolution, decision IDs, and single active `_LATEST.md`.
7. Re-run the SCA baseline/delta audit and record warnings without converting
   them into lifecycle changes.

### 4.2 Projection and compatibility acceptance delegated downstream

The implementation handoff must require:

- source-class/currency/stale/unknown projection tests;
- no synthesized plans/tasks, inferred parentage, or panel-authored approval;
- exact recorded identifiers and separate runtime/project lifecycle status;
- mounted primary live dialogue and isolated read-only replay projection;
- no draft/context/permission/session transfer and a persistent return action;
- malformed, truncated, bounded, or unavailable replay disclosure;
- persona/alias/query and mid-turn selection guards;
- DECOMP/PREP/TASK/AUDIT dispatch and disabled-option regression;
- child-run, replay, interruption, attribution, route/API/SSE, and provider
  singleton regression;
- one-time local-state migration with rollback-safe retention;
- keyboard region traversal, focus restoration, ARIA landmarks, resize
  controls, target size, contrast, and reduced-motion review;
- large tree/artifact/diff/event projection performance checks;
- component/render, typecheck, build, premerge, and packaged Desktop smoke.

No live oMLX or downloaded model is required for automated frontend
acceptance.

### 4.3 Downstream rerun advisories

- `WORKING_ITEMS`: replan and implement the six affected deliverables after
  Gate-5 closure.
- `dependency-extract`: inspect/recompute dependencies after implementation;
  SCOPE_CHANGE does not edit `Dependencies.csv`.
- `estimate-snapshot` and PROJECT_SETUP scheduling: recompute only when the
  owner later activates the implementation tranche.
- `REVIEW` and independent `EVALUATION`: perform semantic-boundary,
  accessibility, compatibility, and packaged regression review.
- `CHANGE`: own subsequent staging, commits, and PR workflow.

## 5. Gate-5 handoff state

After successful propagation:

- `Decision_Log.md`: Gates 1–4 approved; Gate 5
  `GOVERNANCE_PROPAGATED_IMPLEMENTATION_PENDING`.
- `Handoff_State.md`: immutable summary of current authority, exact
  implementation scope, validation obligations, exclusions, warnings, and
  owner decisions still required.
- `_LATEST.md`: continues to point only to SCA-APP-004 with status
  `GOVERNANCE_PROPAGATED_IMPLEMENTATION_PENDING`.
- All affected deliverables remain `IN_PROGRESS`.
- The existing UI remains the compatibility implementation until the new shell
  passes acceptance and the owner separately authorizes retirement.

## Gate-4 question

Do you approve this exact propagation plan and its `DIRECT_EDIT`, `RECOMPUTE`,
and `NO_CHANGE` classifications, including:

1. direct treatment of `docs/PLAN.md`;
2. extension of `K-FS-1`, `K-NOMEM-1`, and `K-BIND-1` without creating a new
   invariant ID or partial invariant-coverage register;
3. the exact partial supersession of `D-APP-28/30/31/32` and `D-APP-56`
   R4-P07 while preserving `D-APP-70` and `D-APP-73`; and
4. the explicit no-change set, especially `DEL-08-05`, runtime/core,
   compatibility contracts, and old-UI retirement?
