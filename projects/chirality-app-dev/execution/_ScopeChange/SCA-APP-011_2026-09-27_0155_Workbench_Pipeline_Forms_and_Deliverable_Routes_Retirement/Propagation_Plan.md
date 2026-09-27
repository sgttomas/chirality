---
amendment_id: SCA-APP-011
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
checkpoint_group: 2
created: 2026-09-27
status: awaiting_checkpoint_2_acceptance
revision: 2 (group-2 review fixes)
basis_commit: c08be56d6ac1f87e3cc1e2cef75a741098607f05
accepted_group1_snapshot: execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/
workflow: scope-change (bundled)
---

# SCA-APP-011 — Checkpoint group 2: exact amendment and propagation plan

> **Status: PROPOSED, revision 2, awaiting the owner's checkpoint-group-2
> act.** Revision 2 applies the independent group-2 review (see "Corrections
> in revision 2" below). Nothing here is applied. This plan consumes the accepted group-1 snapshot
> `checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`
> (`DECISION.md` SHA-256 `412c78c28db13c245b8c8ebb58ad418c73fb63182dbb4ccfb085343dae449fa9`,
> `ACCEPTED_MANIFEST.csv` SHA-256 `d7f96a8be345841d0fda6b3b20b217416dcecf7133334556637592b0030e3545`).
> It proposes exactly what was accepted there:
> - BASE, DQ-R and S-c;
> - D restate;
> - set L excluded;
> - E no change;
> - M-a;
> - the scaffold library kept.

---

## Checkpoint group 2 — what you are asked to decide

### What accepting group 2 authorizes

Group 2 fixes the exact change. Accepting it authorizes checkpoint-group-3
preparation only:

1. **Scope text.** Writing the **127 exact text edits** in
   `Amendment_Preview.md` to **16 files** (the decomposition, the PRD, SPEC and
   PLAN, nine Scopes of Work, and three `_CONTEXT.md` files) as the group-3
   candidate. 126 are written before group 3 for review; one, E47 (a date
   slot), waits for your group-3 acceptance (§6).
2. **Action register.** Accepting the register `Amendment_Actions.csv` (29
   rows: 28 MODIFY, 1 ADD). `ScopeChanging` is YES on 23 rows. Row 29
   (DEL-07-01) is new in revision 2 and has no intake row (below).
3. **Supersession bindings.** Accepting the 18 rows of `Supersession_Delta.csv`.
   They supersede D-APP-74's route-retention clause, SCA-APP-010's "code
   retained" bindings D-006 and D-015, and SR-06's "the code stays".
4. **Code change.** Preparing the code change specified in §4, based on the
   existing candidate `dcd37f9ae`, for review at group 3.
5. **Handoffs and notice.** The downstream handoffs in §8, and the
   informational Runtime notice in `DRAFT_NOTICE_TO_RUNTIME.md`, which is
   sent after group 3.

Nothing is applied or merged before you accept group 3. `_LATEST.md` stays on
SCA-APP-010 until then.

### Corrections in revision 2

Items 1 and 3–5 correct wording or procedure; they do not change the
substance you accepted at group 1. Item 2 does more: it extends the accepted
impact set. Register row 29 (DEL-07-01) is scope-changing and has no intake
row, so accepting group 2 reopens that part of group 1 and decides it. All
five are listed so that your group-2 act covers them knowingly.

1. **Truth correction to the accepted M-a wording.** The group-1 record says
   "live Codex exposure is DEL-06-03's open work" for all four tool contracts.
   DEL-06-03 is "Initial Chirality MCP Read Tools" and owns only the reads. The
   exact text now says: live exposure of the read tools (`status_read`,
   `deps_read`, scaffold preview) is DEL-06-03's open work; `status_transition`
   and `deps_write` remain retained, governed operations with no live
   registration, and any live registration of them is governed by
   DEL-06-04-REQ-010. The substance of M-a is unchanged: the library is the
   interface, this amendment exposes no tool, and the Root tools are today's
   agent path. The accepted group-1 snapshot is immutable and is not
   rewritten; `Decision_Log.md` G1-NOTE-1 records the correction.
2. **Missed obligations to the retired scaffold route.** DEL-03-03 kept live
   delivery obligations for the scaffold composition (P-15 residual, CLM-008
   gap, CLM-017 step 6, CLM-020 record, CLM-027 delivery task). Its
   SCA-APP-011 section now states that it controls, and those items are closed
   by removal, consistent with APP-R058 (E105, E120-E124). A sweep of every
   deliverable Scope of Work and `_CONTEXT.md` (§9, check 4) found three more
   places: DEL-07-02 (route-test hook and route-level 501 gap, E118-E119),
   DEL-07-05 (evidence-module sentence, E114) and DEL-07-01 (three
   root-validation clauses listing "scaffold, and contract APIs", E125-E127).
   **DEL-07-01 is a group-2 addition** (register row 29, `ScopeChanging` YES,
   no supersession): its root-validation obligation is unchanged, only the list
   of root consumers loses the two retired routes.
3. **Stale text.** PLAN §13.2 step 6 (E117), PRD in-scope line "Deliverable
   status and dependency contract APIs" (E116) and decomposition §10 "this
   retirement" (E115).
4. **Journey 7.3** now follows `project-setup` exactly: your gates first,
   scaffolding after, no decomposition copy, and `_COORDINATION.md` recorded
   as your choice (E108).
5. **Procedure.** The group-3 candidate is now written by a dedicated
   `--candidate` mode, and only E47 and the pointer moves wait for group-3
   acceptance (§6).

### The change in one screen

**Removed:**

| Code | Files |
|---|---|
| Workbench and Pipeline forms | `workbench-surface.tsx`, `pipeline-surface.tsx`, `lifecycle-gate-fields.tsx` and their tests |
| Three deliverable routes | `status`, `status/transition`, `dependencies` under `app/api/working-root/deliverable/` |
| Their client module | `lib/workspace/deliverable-api.ts` and its test |
| Scaffold route | `app/api/harness/scaffold/route.ts` and its test |
| Scaffold client function | `scaffoldHarnessExecutionRoot` |
| App scaffold proxy member | `scaffold` on `DaemonHarnessPort`/`RuntimeDaemonHarnessPort` |

**Kept:**

- `deliverable/content/route.ts`, used by the document viewer;
- `deliverable-contracts.ts`, `lib/lifecycle` and `lib/dependencies`;
- the retained Chirality tool modules;
- the scaffold library and its tests;
- `task-scope.ts` and `pipeline-dispatch-contract.ts`;
- the loop-first shell;
- the `/workbench` and `/pipeline` URLs.

**Tests moved, not lost.** The route test's status, transition,
CHECKING-reversal, ISSUED-reopening and dependency cases move to a
library-level test, `frontend/src/__tests__/lib/deliverable-contracts.test.ts`,
except two request-body parsing rows (`INVALID_REQUEST`), which retire with
the routes (§4).
The content-route cases stay in a renamed route test,
`frontend/src/__tests__/api/working-root/deliverable-content-route.test.ts`.

**Scope text.**

- DEL-02-02 is rescoped, not retired; its right-panel scope is unchanged.
- DEL-07-04, DEL-07-05 and DEL-09-03 name the library, with the retained tool
  contracts. Live exposure of the read tools is DEL-06-03's open work;
  `status_transition` and `deps_write` stay retained, governed operations
  under DEL-06-04-REQ-010 (M-a, corrected wording above).
- DEL-07-02 closes APP-R058 by removal and records the `<project>/execution`
  follow-up.
- DEL-03-03 closes its scaffold-composition items by removal.
- DEL-08-03 and DEL-02-03 drop "code retained" and the retired routes;
  DEL-07-01 drops the retired routes from its list of root consumers.
- The PRD, SPEC, PLAN and decomposition record the separate owner retirement
  in every route-preservation clause.

**Unchanged:** topology, counts, scope-item mappings, context envelopes,
lifecycle states and CONTRACT. No dependency register is written by this
amendment; dependency re-extraction is a downstream handoff (§8).

### Choices that remain

| # | Choice | Options | Recommendation |
|---|---|---|---|
| **W** | Who writes the Scope of Work, PRD, SPEC and PLAN text | **W-a:** this amendment writes the exact text at group-3 preparation. The write boundary names all 16 files (§2). **W-b:** this amendment writes only the decomposition and the three `_CONTEXT.md` files; the Scopes of Work go to `project-setup` INCREMENTAL (`scope-of-work` REVISE), and the PRD, SPEC and PLAN to a separate owner-approved change. | **W-a.** The exact text is ready and validated (§9). One audited poststate is simpler, and W-b would re-derive the same text. |
| **Q** | Sequencing of scope text and code | **Q-a:** group 3 reviews the written scope-text candidate together with the rebased code candidate (§4). After your group-3 acceptance, one PR lands both. **Q-b:** the scope-text PR lands first and the code PR after it. For a short time the hooks would name a test file that does not exist yet. | **Q-a.** It matches your direction ("You accept each of its three checkpoints, then the code removal merges") and avoids any window where text and code disagree. |

Everything else is fixed by your group-1 acceptance, except the revision-2
corrections above. Your group-2 act covers those too, including the group-2
addition of register row 29 (DEL-07-01).

**A short answer is enough**, for example: "Accept SCA-APP-011 group 2: W-a,
Q-a, with the revision-2 corrections and row 29." I then record your words
verbatim in the group-2 decision snapshot, record row 29 there as a reopened
group-1 item, and prepare group 3.

---

## 1. Basis consumed

| Input | Identity |
|---|---|
| Accepted group-1 snapshot | `checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/` (hashes above); pointer `SCA-APP-011_GROUP-1_AUTHORIZED.md` |
| Accepted impact assessment | `Impact_Assessment.md` SHA-256 `5b74f07668e91ae06f89b1dcb0b612c9dd1871d96fa170df39ce8228e9be9af7` |
| Preimages | Every edited file's SHA-256 is recorded in `Evidence/Group2/PREIMAGE_POSTIMAGE.csv`; all equal the group-1 basis (for example decomposition `9261ce30…126ea8a6`, PRD `17ca3f3c…e46054`, SPEC `4c8c9da1…08c2`, PLAN `5e9cb5e5…04dc`) |
| Active pointer | `_LATEST.md` → SCA-APP-010 (SHA-256 `6fdba0c9…42c04e3`); group-3 posture `ACCEPTED_PREDECESSOR` |
| Code candidate | `dcd37f9ae9d22bfedc86b921f6e2ac70b90e1419` (branch `worktree-agent-a0de269a96f5dd4af`, parent `947075c9a`) |

## 2. Write boundary (W-a)

The group-3 preparation writes **only** these files, and only the edits in
`Amendment_Preview.md`:

| File | Package role | Edits |
|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Working surface | E01, E22, E23, E39-E47, E81, E103, E115 |
| `docs/PRD.md` | Authoritative carrier (product requirements) | E48-E67, E106-E109, E116 |
| `docs/SPEC.md` | Authoritative carrier (physical/API contract) | E68-E74, E110, E111 |
| `docs/PLAN.md` | Authoritative carrier (roadmap) | E75-E79, E112, E113, E117 |
| DEL-02-02 `ScopeOfWork.md` / `_CONTEXT.md` | Production contract / working surface | E83-E89 / E82 |
| DEL-02-03 `ScopeOfWork.md` | Production contract | E80 |
| DEL-03-03 `ScopeOfWork.md` | Production contract | E104, E105, E120-E124 |
| DEL-07-01 `ScopeOfWork.md` | Production contract | E125-E127 |
| DEL-07-02 `ScopeOfWork.md` | Production contract | E90-E102, E118, E119 |
| DEL-07-04 `ScopeOfWork.md` / `_CONTEXT.md` | Production contract / working surface | E03-E13 / E02 |
| DEL-07-05 `ScopeOfWork.md` | Production contract | E14-E20, E114 |
| DEL-08-03 `ScopeOfWork.md` / `_CONTEXT.md` | Production contract / working surface | E27-E38 / E24-E26 |
| DEL-09-03 `ScopeOfWork.md` | Production contract | E21 |

The application also writes these snapshot and handoff artifacts under
`_ScopeChange/`:
- the group-2 and group-3 decision snapshots and their `_AUTHORIZED` pointers;
- the candidate snapshot files (`Supersession_Map.csv`,
  `Post_Change_Coverage.json`, `RUN_SUMMARY.md`, `Handoff_State.md`);
- after group-3 acceptance, `_LATEST.md` (§6).

It does **not** write:
- `docs/CONTRACT.md` or the companion register (E: no change);
- `docs/TYPES.md` or `docs/DIRECTIVE.md`;
- any `_STATUS.md` or `Dependencies.csv`;
- any other deliverable.

No lifecycle state changes.

No `ISSUED` or `CHECKING` deliverable is touched. All nine are
`IN_PROGRESS`, so no reopening is involved and `write_status.sh` is not
used.

Under W-b, the table above shrinks to the decomposition and the three
`_CONTEXT.md` files. The nine SOW rows then become `project-setup` INCREMENTAL
handoffs carrying the same exact text, and the PRD, SPEC and PLAN edits go to a
separate owner-approved documentation change.

## 3. Register and exact text

`Amendment_Actions.csv` is the proposed authoritative register. Rows 1-28
map to intake rows 1–20 and 33–40; row 29 (DEL-07-01) is a group-2 addition
from the review sweep. Each row names its exact edits.

`Evidence/Group2/amendment_edits.py` holds every edit as data (exact `old`
and `new` bytes). `Evidence/Group2/build_amendment_preview.py` renders the
preview and records, per file, the preimage hash, the candidate hash (every
edit except E47) and the final hash where it does not depend on the date
(`Evidence/Group2/PREIMAGE_POSTIMAGE.csv`). Its modes:

- default: render `Amendment_Preview.md` and the CSV;
- `--check`: write nothing; fail if a preimage drifted, if the CSV differs
  from what the edit data produces, or if `Amendment_Preview.md` differs from
  the rendering of the edit data;
- `--candidate`: group-3 preparation (§6 step 3);
- `--finalize`: after group-3 acceptance only (§6).

Wording rules applied throughout:

- **Non-destructive.** Retired requirements and clauses are marked
  `[RETIRED — SCA-APP-011]` and kept as dated history. Each affected Scope of
  Work gains a controlling `## SCA-APP-011 Current Contract (Controlling)`
  section, following the SCA-APP-010 precedent.
- **M-a (corrected wording).** The library is named as the interface. The
  Chirality tool contracts are named as retained SDK-path interfaces. Live
  exposure of the read tools is DEL-06-03's open work; `status_transition` and
  `deps_write` remain retained, governed operations with no live registration,
  and any live registration is governed by DEL-06-04-REQ-010. On the Codex
  path an actor records a lifecycle transition with `write_status.sh` or edits
  `_STATUS.md`, and maintains dependency registers through the Root dependency
  workflows or edits them, in each case within the actor authority of Root
  `docs/SPEC.md` (§3.3 for lifecycle, §5 for dependencies).
- **Scope decisions, not code history.** The text states scope decisions
  ("retired by SCA-APP-011"). It does not claim that code has already been
  deleted. Verification hooks name the exact test files the code change in §4
  creates.

## 4. Code change specification (for the responsible current role)

The code change is repository work by the App loop under standing Git
authority. It is not an SCA write. It takes candidate `dcd37f9ae` as its
starting point and must end in exactly this state.

**Start.** Rebase `dcd37f9ae` onto current `main`. The only conflict is the
regenerated `exports/chirality-app/export-report.md`. Drop the candidate's
edits to `docs/SPEC.md` and to the DEL-02-02, DEL-07-04 and DEL-08-03
`ScopeOfWork.md` files. The group-2 text in §3 replaces them. The candidate's
own records are then corrected as listed under **Records** below.

**Delete:**

| Path (under `projects/chirality-app-dev/frontend/src/`) | Why |
|---|---|
| `components/workbench/workbench-surface.tsx`, `components/pipeline/pipeline-surface.tsx`, `components/pipeline/lifecycle-gate-fields.tsx` | Forms (already in `dcd37f9ae`) |
| `__tests__/components/workbench-surface.test.ts`, `__tests__/components/pipeline-surface.test.ts`, `__tests__/components/lifecycle-transition-gates.test.tsx` | Form tests (already in `dcd37f9ae`) |
| `app/api/working-root/deliverable/status/route.ts`, `app/api/working-root/deliverable/status/transition/route.ts`, `app/api/working-root/deliverable/dependencies/route.ts` | Three deliverable routes |
| `lib/workspace/deliverable-api.ts`, `__tests__/lib/workspace-deliverable-api.test.ts` | Client fetch functions `fetchDeliverableStatus`, `transitionDeliverableStatus` (client copy), `fetchDeliverableDependencies`, and their types; no other importer after `dcd37f9ae` |
| `app/api/harness/scaffold/route.ts`, `__tests__/api/harness/scaffold-route.test.ts` | Scaffold route |

**Modify:**

| Path | Change |
|---|---|
| `components/shell/tertiary-sidebar-tabs.tsx` | Already in `dcd37f9ae`: drop the `PipelineSurface` and `WorkbenchSurface` imports and the `pipelineTab`/`workbenchTab` entries, leaving `portalTab` |
| `lib/harness/client.ts` | Remove `scaffoldHarnessExecutionRoot` and the `ScaffoldExecutionRootResponse` import if it has no other use |
| `__tests__/lib/harness-client.test.ts` | Remove the scaffold import and the case "scaffolds execution roots through scaffold route" |
| `lib/runtime-client/daemon-harness-port.ts` | Remove the `scaffold` interface member, its `daemonClientUnavailable` entry, its scope-map entry (`scaffold: 'executionRoot'`) and the now-unused `ScaffoldExecutionRoot*` imports; the `'executionRoot'` scope kind goes too if nothing else uses it |
| `lib/runtime-client/runtime-daemon-harness-port.ts` | Remove `scaffold()` |
| `__tests__/lib/runtime-daemon-harness-port.test.ts`, `__tests__/api/harness/daemon-proxy-boundary.test.ts`, `__tests__/api/harness/turn-route-attachments.test.ts`, `__tests__/api/harness/fake-daemon-harness-port.ts` | Remove the scaffold stubs and the case "uses only the fixed app-dev project for contained scaffold requests" |
| `__tests__/api/working-root/deliverable-contracts.test.ts` | **Split** (below) |
| `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-03_Harness_API_and_SSE_Compatibility_Adapter/RouteAdapterTestIndex.md` (under `projects/chirality-app-dev/`) | Remove the `scaffold-route.test.ts` file row (line 24 at basis) and the `/api/harness/scaffold` route row (line 46), or mark both `[RETIRED — SCA-APP-011]`; the DEL-03-03 SCA-APP-011 section records this |

**Add, and split the route test:**

- **`__tests__/lib/deliverable-contracts.test.ts` (new).** Port every case in
  the current route test's `describe('working-root deliverable contract routes')`
  that exercises status, transition or dependencies (lines 131–1134 at basis)
  to direct calls of `readDeliverableStatus`, `transitionDeliverableStatus`,
  `readDeliverableDependencies` and `writeDeliverableDependencies` in
  `lib/workspace/deliverable-contracts.ts`. The port covers
  every case except request-body parsing (`INVALID_REQUEST`):
  - the "human-ruled CHECKING reversal" block: 10 `it` cases and 2 `it.each`
    tables (lines 391 and 436 at basis);
  - the "reopening ISSUED -> IN_PROGRESS under an accepted amendment" block,
    including "inside a Git work tree": 6 `it` cases and 2 `it.each` tables
    (lines 629 and 645 at basis);
  - the actor, approval-SHA, dependency, recorded-register and symlink cases.

  Where a case asserted an HTTP status and body, assert the thrown
  `WorkspaceValidationError`'s `code` and `status`, or the returned value.
  The only request-body parsing cases are two `it.each` rows:
  `['CHECKING', 'a non-string ruling', { ruling: 42 }, 'INVALID_REQUEST']`
  and `['a non-string amendment', { amendment: 7 }, 'INVALID_REQUEST']`.
  `DeliverableStatusTransitionInput` types `ruling` and `amendment` as
  `string` (`lib/lifecycle/transition.ts` lines 88 and 94), so these inputs
  are compile-time errors against the library and it has no runtime type check
  to test. Drop the two rows from the ported tables (every other row ports
  unchanged) and list them in the run receipt as retired with the routes. If
  the library gains a runtime type check before the port, keep the rows and
  assert its error instead.
- **`__tests__/api/working-root/deliverable-content-route.test.ts`.** This is
  the renamed remainder: the ten `content/route.ts` cases (lines 1139–1283 at
  basis) and the shared fixtures they need.

**Keep:**
- `app/api/working-root/deliverable/content/route.ts`;
- `lib/workspace/deliverable-contracts.ts`, `lib/workspace/filesystem.ts`
  (`workspaceErrorPayload` stays for the content route), `lib/lifecycle/**`
  and `lib/dependencies/**`;
- `lib/harness/scaffold.ts` and `__tests__/lib/harness-scaffold.test.ts`;
- `lib/harness/mcp/**` and its tests;
- `lib/workspace/task-scope.ts` and `lib/pipeline/pipeline-dispatch-contract.ts`;
- every loop-first shell file except the tab-factory change listed under
  **Modify** (set L excluded);
- `app/workbench/*` and `app/pipeline/*` (Q3 URLs).

**Records.** `dcd37f9ae` wrote its records before SCA-APP-011 existed and says
the routes and client fetch functions are kept and that merge is held for the
owner's route choice. Correct them in the rebased candidate:

- `execution/_Coordination/AgentRuns/APP-REMOVE-LEGACY-FORMS-2026-09-27/RECEIPT.md`:
  add the route, client-module, scaffold and test-split changes in this
  section; replace the "kept" list and the merge hold with the SCA-APP-011
  basis (group-2 and group-3 snapshots); list the two dropped `it.each` rows.
- `loop/LOOP_RECEIPTS.md` Receipt-269: amend the Gate-Outcome and the
  Pointers to the same scope and cite SCA-APP-011, or record the correction
  in the next receipt if Receipt-269 has already been relied on.
- `execution/_Coordination/AgentRuns/APP-TRANSITION-FORMS-2026-09-26/RECEIPT.md`:
  the note `dcd37f9ae` added also names SCA-APP-011 as the authority for the
  removal of the forms it built.
- The MEMORY rows `dcd37f9ae` added for DEL-02-02, DEL-07-04 and DEL-08-03:
  restate them to the SCA-APP-011 scope and add MEMORY rows for DEL-02-03,
  DEL-03-03, DEL-07-01, DEL-07-02, DEL-07-05 and DEL-09-03, each pointing to
  SCA-APP-011.
- `docs/governance_harness/tranche_manifests/APP-REMOVE-LEGACY-FORMS-20260927.yaml`:
  add the added deletions and modifications.
- Regenerate `exports/chirality-app/` with the export tooling.
- Write the new run receipt and loop receipt for the rebased candidate
  (LOOP_INIT §5).

**Checks on the actual rebased candidate:**
- frontend typecheck (the `Record<keyof DaemonHarnessPort, …>` scope map
  flags any partial removal);
- the full frontend test suite and the registered harness checks;
- a grep proving that no product import of the deleted modules remains;
- `git diff --check`;
- Root G0–G4.

## 5. Supersession bindings

`Supersession_Delta.csv` has 18 `SUPERSESSION` rows for the 15 register rows
marked `SupersessionBindingPresent = YES`:

| Superseded fact | Register rows |
|---|---|
| D-APP-74 L97-99, deliverable routes | 1, 2, 7, 12, 13, 15 |
| D-APP-74 L97-99, scaffold route | 21, 22, 23, 25, 27, 28 |
| SCA-APP-010 map D-006 "code retained" | 4, 5 |
| SCA-APP-010 map D-015 "code, routes, and tests are retained … deletion remains separately gated" | 4, 20 |
| SR-06 "the code stays" | 4, 20 |

No row binds D-APP-74 line 107 ("Old-UI retirement requires separate owner
acceptance …") directly, although register rows 4, 5 and 20 retire old UI.
SCA-APP-010 map row D-015 (`workbench_pipeline_active_shell_retirement`)
already superseded line 107 for Workbench and Pipeline, and the cumulative map
carries that binding. Binding line 107 again would create a second, competing
replacement for the same fact. This amendment therefore supersedes the D-015
binding itself (delta rows D-004 and D-020), which is the separate gate D-015
reserved for deletion. Line 107 stays in force for everything D-015 did not
cover, including the loop-first shell (set L excluded).

A dry run of `tools/coordination/accumulate_supersession_map.py` with the
SCA-APP-010 map as prior produces 63 rows with 0 findings. At group 3 the same
command writes the candidate `Supersession_Map.csv`.

## 6. Acceptance-conditional edits and group-3 procedure

Acceptance-conditional bytes:

| Item | Rule |
|---|---|
| E47 `{APPLICATION_DATE}` | The decomposition Coverage and Telemetry `Revision` and `Date`. Not written into the candidate. After acceptance it is filled with the date of the group-3 decision folder `checkpoint_snapshots/SCA-APP-011_GROUP-3_{YYYY-MM-DD}/`, whose `DECISION.md` first line is `# SCA-APP-011 checkpoint group 3 — accepted …`; `--finalize` refuses any other date. It is the only slot: every file's candidate hash, and every final hash except the decomposition's, is fixed in `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` |
| `_LATEST.md` | Moved to the accepted SCA-APP-011 snapshot folder only after group-3 acceptance. Its exact post-image is drafted in the group-3 package. The SCA-APP-010 entry becomes the historical predecessor |
| `checkpoint_snapshots/SCA-APP-011_GROUP-2_{date}/` and `SCA-APP-011_GROUP-2_AUTHORIZED.md` | Written from your group-2 act |
| `checkpoint_snapshots/SCA-APP-011_GROUP-3_{date}/` | Written from your group-3 act |
| Runtime notice | `DRAFT_NOTICE_TO_RUNTIME.md` copied to `projects/chirality-runtime/execution/_Coordination/NOTICE_{date}_APP_SCA-APP-011_SCAFFOLD_API.md` after group-3 acceptance |

**Date rule.** The dates written into the candidate text are fixed and are
the owner-direction date, 2026-09-27, not an acceptance date: the DEC-026
row date (E45), the Change Log line (E46), the PLAN §13 table row (E78) and
the "owner direction 2026-09-27" references in the new sections. The only
date tied to acceptance is the E47 slot. `Supersession_Delta.csv` and the
Runtime notice draft likewise cite the direction date and say the retirement
binds on group-3 acceptance, without an acceptance date.

Group-3 preparation, in order:

1. Resolve the group-2 decision snapshot, and verify it binds this
   `Amendment_Actions.csv` by hash.
2. Run `build_amendment_preview.py --check`. No drift is allowed.
3. Write the candidate: `build_amendment_preview.py --candidate`. It needs
   the group-2 pointer `SCA-APP-011_GROUP-2_AUTHORIZED.md` (no group-3
   decision), rechecks every preimage hash, writes every edit except E47, and
   verifies each written file against its recorded candidate hash. This is
   method.md group-3 preparation steps 1 and 2: the candidate is the audited
   poststate the owner reviews. After group-3 acceptance only,
   `build_amendment_preview.py --finalize --date YYYY-MM-DD --group3-decision
   <path>` rechecks the candidate hashes and applies E47; the pointer moves in
   the table above follow, then the post-acceptance record under
   `_PostAcceptanceValidation/`.
4. Generate `Supersession_Map.csv` (accumulator) and `Post_Change_Coverage.json`
   (the baseline builder, rerun).
5. Run `validate_postimage.py` and the SOW validator.
6. Run a fresh `audit-decomp`, or the equivalent deterministic baseline with
   disclosure.
7. Obtain an independent review of the applied candidate together with the
   §4 code candidate (Q-a).
8. Present raw and adjusted `AuditState`, the closure verdict and the
   acceptance-conditional list.

## 7. Deliverable propagation

| Deliverable | Lifecycle | Scope text | `_CONTEXT.md` | Dependencies |
|---|---|---|---|---|
| DEL-02-02 | IN_PROGRESS | MODIFY (DQ-R) | E82 | Retire DEP-02-02-005 to 009 |
| DEL-02-03 | IN_PROGRESS | MODIFY | none | No own-register change; DEP-02-02-006 (its inbound edge) retires |
| DEL-03-03 | IN_PROGRESS | MODIFY | none (no route named) | No change expected |
| DEL-07-01 | IN_PROGRESS | MODIFY (row 29) | none (no route named) | No change expected |
| DEL-07-02 | IN_PROGRESS | MODIFY | none (no route named) | No change expected |
| DEL-07-04 | IN_PROGRESS | MODIFY | E02 | Refresh after DEP-02-02-007 retires |
| DEL-07-05 | IN_PROGRESS | MODIFY | none | Refresh after DEP-02-02-008 retires |
| DEL-08-03 | IN_PROGRESS | MODIFY | E24-E26 | DEP-08-03-010 statement refresh |
| DEL-09-03 | IN_PROGRESS | MODIFY | none | No change expected |

For every deliverable:
- no `_STATUS.md` change;
- no reopening;
- no `CHECKING` hold;
- a MEMORY entry through the loop closeout.

DEL-02-01 (DEP-02-01-007/008, open human graph decision HGD-2) and DEL-08-02
(DEP-08-02-003/005 wording) are dependency neighbours only.

## 8. Downstream reruns and handoffs (not executed by this workflow)

1. **`project-setup` in `INCREMENTAL` mode.** No additions to scaffold and
   no retirements to record. Route the MODIFY rows: under W-a their contracts
   are already written, so it refreshes dependency and coordination records
   for the nine deliverables and their neighbours.
2. **`dependency-extract`.** Run for DEL-02-02, DEL-02-01, DEL-02-03, DEL-07-04,
   DEL-07-05, DEL-08-02 and DEL-08-03, then `analyze_dep_closure.py`.
   - Retire DEP-02-02-005 to 009 and DEP-02-01-007.
   - DEP-02-01-008 follows HGD-2.
   - Refresh the wording of DEP-08-03-010 and DEP-08-02-003/005.
   - Only edges are removed, so no cycle can form.
3. **Audits.** `audit-decomp` (post-change baseline), then `audit-scope-closure`
   after the setup and code change.
4. **Code change** (§4) through the App loop, landed with the scope text under
   Q-a. It includes the DEL-03-03 `RouteAdapterTestIndex.md` rows and the
   correction of `dcd37f9ae`'s own records.
5. **Runtime notice** (`DRAFT_NOTICE_TO_RUNTIME.md`, informational). The Runtime
   loop decides on its scaffold API.
6. **Task Management APP-R058.** Proposed disposition note: "closed by removal
   under SCA-APP-011 (DEL-07-02 SCA-APP-011 section)". The row's owner records
   it; this workflow does not edit Task Management.
7. **DEL-07-02 follow-up.** Recorded in its SCA-APP-011 section (E102): any later
   App-side scaffold entry needs its own amendment and defaults to
   `<project>/execution`.
8. **Export projection.** `exports/chirality-app/` is regenerated with the code
   change.

## 9. Validation performed for this package

Run on the revision-2 package tree (base `68b07a99d`; no scope file, code or
accepted group-1 record changed).

| Check | Result |
|---|---|
| `build_amendment_preview.py` | 127 edits in 16 files. Every `old` passage occurs exactly once, in sequence; candidate and final images dry-run |
| `build_amendment_preview.py --check` | OK: all 16 preimages match `PREIMAGE_POSTIMAGE.csv`; the CSV equals what the edit data produces; `Amendment_Preview.md` equals the rendering of the edit data. A test append to the preview made it FAIL, as intended |
| `check_candidate_mode.py` (scratch copy) | 12/12 PASS: repository-tree `--candidate` refused without the group-2 pointer (tree unchanged); scratch `--candidate` wrote 16 files, each matching its candidate hash, with E47 not applied; rerun refused on preimage drift; `--finalize` refused for a draft heading, a date that differs from the decision folder and a wrong path; one `--finalize` with a test decision filled E47 only; rerun refused; repository tree unchanged |
| `validate_postimage.py` | PASS: 24 edited table rows keep their column count; all 9 edited Scopes of Work validate (exit 0 before and after); every edited paragraph naming a retired path carries an SCA-APP-011 marker; new check 4 swept all 108 deliverable `ScopeOfWork.md` and `_CONTEXT.md` files and found 0 lines naming a retired route or scaffold-route obligation without a marker or a controlling section (`Evidence/Group2/POSTIMAGE_VALIDATION.md`) |
| `accumulate_supersession_map.py` dry run | 63 rows, 0 findings |
| Group-1 baseline builder rerun (at `68b07a99d`) | Output identical to the accepted `Pre_Change_Coverage.json` apart from `basis_commit`: 54 nodes, 111 edges, 0 SCCs. The accepted file was restored unchanged (SHA-256 `ef2eb2f5…ab82`) |
| Root G0–G3 (`validate_root_materialization_fence.py`, `validate_root_harness_adapter.py`, `validate_root_surface_ownership.py`, `validate_root_work_graph_dispatch.py`) | G0, G1, G2 and G3 PASS |
| `git diff --check` | PASS |

## 10. State fields and derivative surfaces

| Field | Value now | After group-3 acceptance (expected) |
|---|---|---|
| `DecompositionTruthState` | `NOT_STARTED` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` | `INCOMPLETE` until dependency re-extraction and audits |
| `ContentRemediationState` | `NOT_REQUIRED` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` | `IN_PROGRESS` |
| `MetadataAlignmentState` | `NOT_REQUIRED` | `NOT_REQUIRED` |
| `AuditState` | `NOT_RUN` | Set by the group-3 audit |
| `ReadyForNextPhase` | `NOT_APPLICABLE` | `NOT_APPLICABLE` |

| Derivative surface | Classification | Owner |
|---|---|---|
| `_Evaluation/DecompCoverage` | STALE_REBUILD_REQUIRED | audit-decomp |
| `_Evaluation/ScopeClosureAudit` | STALE_REBUILD_REQUIRED | audit-scope-closure |
| `_Reconciliation/DepClosure` | STALE_REBUILD_REQUIRED | analyze_dep_closure |
| `exports/chirality-app` | STALE_REBUILD_REQUIRED | export tooling, with the code change |
| Companion register | NO_CHANGE (E) | — |

## 11. Residuals (recorded, not proposed)

- `/api/working-root/scope` loses its only UI caller (the Workbench form).
  Its removal would be a separate owner decision.
- `DeliverablesProvider` in `app/layout.tsx` has no consumer after the forms go
  (candidate receipt). This is a code tidy for the loop, not scope.
- DEL-08-03's type `UX_UI_SLICE` no longer has a UI consumer (Impact
  Assessment §5.4). No change is proposed.

## Evidence basis for this package

| Artifact | SHA-256 |
|---|---|
| `Amendment_Actions.csv` | `416097312beffa47143b2993bfe17721e5c312630789a1101e6cbda688edbc22` |
| `Supersession_Delta.csv` | `33a4d558ba86fd716ec185a56fc47569cf1837ada3bd4692e4d0623548af1030` |
| `Amendment_Preview.md` | `3781bf3e548bb1497e8f74fe2cb0ecd38314aac7834a7d6a4f7d3eeb7f6a6f40` |
| `DRAFT_NOTICE_TO_RUNTIME.md` | `3c8806a7d10ba5b37392cd77acb6fbf8501d9fda2d49c7257b3cb89fd994ad78` |
| `Evidence/Group2/amendment_edits.py` | `190a41df429ef33c70b3cb31cad819abbe2385b7f32d532ec6684452392e3edf` |
| `Evidence/Group2/build_amendment_preview.py` | `e028eb35ee724e19b665e30f2cc9dbc0b99396391bbf20d5d037f9f2e4c0be88` |
| `Evidence/Group2/validate_postimage.py` | `1570fdafa673653448c328a9af75ee415f51d8c2332338e1664d671b66bb80ca` |
| `Evidence/Group2/check_candidate_mode.py` | `acd0d41143761aeb40c4d736dec3389d085709ac5952a35e3c4d9f6ab479fb79` |
| `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` | `db9e647cef23f3c8a9f0cc39ba23c906fcfb6e6fbdd43816995d35a911ff035b` |
| `Evidence/Group2/POSTIMAGE_VALIDATION.md` | `cbfc01d6f9be635eac584746b9dcd6cfc7599f6cf8e8bb2b87c28541542427fb` |
