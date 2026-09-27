# Active SCOPE_CHANGE Snapshot

**Status:** `OPEN_PENDING_DERIVATIVE_CLOSURE`
**Active snapshot:** `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`
**Amendment label:** `SCA-APP-011 Workbench and Pipeline Forms and Deliverable Routes Retirement`
**Accepted:** checkpoint group 3 on 2026-09-27 (`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`); groups 1 and 2 on 2026-09-27 (`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`, `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`)
**Accepted predecessor:** `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/`. Its pointer record, including the 2026-09-22 derivative application and the DEL-02-05 carrier-propagation addendum, is the previous revision of this file (SHA-256 `6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3`) and remains valid history
**Post-change evidence:** `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/Post_Change_Coverage.json` and `Evidence/Group3/` — topology, coverage, lifecycle and dependency closure unchanged from the pre-change baseline; no new finding

SCA-APP-011 applies the owner-directed retirement of the obsolete Workbench and
Pipeline forms and their tests. It also retires three App HTTP routes and their
client fetch functions:
- `GET /api/working-root/deliverable/status`;
- `POST /api/working-root/deliverable/status/transition`;
- `GET/PUT /api/working-root/deliverable/dependencies`.

It retires `POST /api/harness/scaffold`, with its client function and App port
member, as well.

- **DEL-02-02** is rescoped to its right-panel scope.
- **DEL-07-04 and DEL-07-05** name the lifecycle and dependency library as the
  interface, with the Chirality tool contracts retained on the SDK path.
  - Live exposure of the read tools is DEL-06-03's open work.
  - `status_transition` and `deps_write` stay governed by DEL-06-04-REQ-010.
- **DEL-07-02** keeps the scaffold library and closes APP-R058 by removal.
- **Execution roots** are scaffolded through the Root `project-setup` workflow.
- **Unchanged:** topology stays 10 packages, 52 deliverables, 84 scope items
  and 10 objectives. No lifecycle state or dependency register changed.

This snapshot is open pending derivative closure. Each of these remains
separately governed and open:
- dependency re-extraction for the affected deliverables, and
  `analyze_dep_closure`;
- `project-setup` in `INCREMENTAL` mode;
- `audit-decomp` and `audit-scope-closure`;
- the Task Management APP-R058 disposition;
- the Runtime loop's decision on its scaffold API.

It makes no release, signing, notarization, publication, readiness or reliance
claim.
