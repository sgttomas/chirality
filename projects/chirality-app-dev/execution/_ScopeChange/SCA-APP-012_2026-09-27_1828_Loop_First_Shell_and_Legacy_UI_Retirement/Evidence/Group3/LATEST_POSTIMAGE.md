# Active SCOPE_CHANGE Snapshot

**Status:** `OPEN_PENDING_DERIVATIVE_CLOSURE`
**Active snapshot:** `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/`
**Amendment label:** `SCA-APP-012 Loop-First Shell and Legacy UI Retirement`
**Accepted:** checkpoint group 3 on {APPLICATION_DATE} (`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/`); groups 1 and 2 on 2026-09-27 (`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`, `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`)
**Accepted predecessor:** `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`. Its pointer record is the previous revision of this file (SHA-256 `904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637`) and remains valid history. Its post-acceptance follow-ups are recorded in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/RECEIPT.md`. The Runtime-scaffold-API item that pointer listed is closed: the Runtime loop retired its scaffold API in PR #1012 (merge commit `49bbc9787238d59fe2945c8e9413206d554e56b7`; `execution/_Coordination/NOTICE_2026-09-27_RUNTIME_SCAFFOLD_API_RETIRED.md`)
**Post-change evidence:** `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Post_Change_Coverage.json` and `Evidence/Group3/` — topology, coverage, lifecycle and dependency closure unchanged by the amendment; no new finding

SCA-APP-012 applies the owner-directed retirement of the loop-first
compatibility UI, the separate owner decision that D-APP-74, PRD KG-033 and
§6.4 and SPEC §17.9 reserved:
- the loop, portal and tertiary shells, their sidebar layout and tab factory,
  and the role-directory panel;
- the discarded `legacy` prop and the `?legacy=1` link;
- the two `lib/portal` matrix helpers.

It also retires `DeliverablesProvider`, `GET /api/working-root/scope`, the
unmounted flat-file workflow view with `GET /api/working-root/workflow`, and
DEL-02-03-REQ-009.

- **`/workbench` and `/pipeline`** stay as unlisted entries into the dialogue
  shell (D-APP-108 Q3).
- **No App-side scaffold entry** and no write-capable scaffold tool is
  planned; the agent scaffolds execution roots through Root `project-setup`.
- **DEL-02-03-REQ-010** is restated: status is read-only from
  `/api/project/deliverables`, with no transition control.
- **Unchanged:** topology stays 10 packages, 52 deliverables, 84 scope items
  and 10 objectives. No lifecycle state or dependency register changed.

This snapshot is open pending derivative closure. Each of these remains
separately governed and open:
- dependency re-extraction for DEL-02-03 and DEL-08-03 (DX-01, DX-02, DX-03,
  DX-05), and `analyze_dep_closure`;
- `project-setup` in `INCREMENTAL` mode;
- `audit-decomp` and `audit-scope-closure`;
- the Task Management TM-APP-051 note.

It makes no release, signing, notarization, publication, readiness or reliance
claim.
