---
amendment_id: SCA-APP-011
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
checkpoint_group: 2
created: 2026-09-27
status: awaiting_checkpoint_2_acceptance
basis_commit: c08be56d6ac1f87e3cc1e2cef75a741098607f05
accepted_group1_snapshot: execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/
workflow: scope-change (bundled)
---

# SCA-APP-011 — Checkpoint group 2: exact amendment and propagation plan

> **Status: PROPOSED, awaiting the owner's checkpoint-group-2 act.** Nothing
> here is applied. This plan consumes the accepted group-1 snapshot
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

1. **Scope text.** Applying the **113 exact text edits** in
   `Amendment_Preview.md` to **15 files**: the decomposition, the PRD, SPEC and
   PLAN, eight Scopes of Work, and three `_CONTEXT.md` files. One date slot
   is filled at application.
2. **Action register.** Accepting the register `Amendment_Actions.csv` (28
   rows: 27 MODIFY, 1 ADD). `ScopeChanging` is YES on 22 rows.
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
library-level test, `frontend/src/__tests__/lib/deliverable-contracts.test.ts`.
The content-route cases stay in a renamed route test,
`frontend/src/__tests__/api/working-root/deliverable-content-route.test.ts`.

**Scope text.**

- DEL-02-02 is rescoped, not retired; its right-panel scope is unchanged.
- DEL-07-04, DEL-07-05 and DEL-09-03 name the library, with the retained tool
  contracts. Live Codex exposure of those tools is DEL-06-03's open work, per
  M-a.
- DEL-07-02 closes APP-R058 by removal and records the `<project>/execution`
  follow-up.
- DEL-08-03, DEL-03-03 and DEL-02-03 drop "code retained" and the retired
  routes.
- The PRD, SPEC, PLAN and decomposition record the separate owner retirement
  in every route-preservation clause.

**Unchanged:** topology, counts, scope-item mappings, context envelopes,
lifecycle states, dependencies and CONTRACT.

### Choices that remain

| # | Choice | Options | Recommendation |
|---|---|---|---|
| **W** | Who writes the Scope of Work, PRD, SPEC and PLAN text | **W-a:** this amendment writes the exact text at group-3 preparation. The write boundary names all 15 files (§2). **W-b:** this amendment writes only the decomposition and the three `_CONTEXT.md` files; the Scopes of Work go to `project-setup` INCREMENTAL (`scope-of-work` REVISE), and the PRD, SPEC and PLAN to a separate owner-approved change. | **W-a.** The exact text is ready and validated (§9). One audited poststate is simpler, and W-b would re-derive the same text. |
| **Q** | Sequencing of scope text and code | **Q-a:** group 3 reviews the applied scope-text candidate together with the rebased code candidate (§4). After your group-3 acceptance, one PR lands both. **Q-b:** the scope-text PR lands first and the code PR after it. For a short time the hooks would name a test file that does not exist yet. | **Q-a.** It matches your direction ("You accept each of its three checkpoints, then the code removal merges") and avoids any window where text and code disagree. |

Everything else is fixed by your group-1 acceptance.

**A short answer is enough**, for example: "Accept SCA-APP-011 group 2: W-a,
Q-a." I then record your words verbatim in the group-2 decision snapshot and
prepare group 3.

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
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Working surface | E01, E22, E23, E39-E47, E81, E103 |
| `docs/PRD.md` | Authoritative carrier (product requirements) | E48-E67, E106-E109 |
| `docs/SPEC.md` | Authoritative carrier (physical/API contract) | E68-E74, E110, E111 |
| `docs/PLAN.md` | Authoritative carrier (roadmap) | E75-E79, E112, E113 |
| DEL-02-02 `ScopeOfWork.md` / `_CONTEXT.md` | Production contract / working surface | E83-E89 / E82 |
| DEL-02-03 `ScopeOfWork.md` | Production contract | E80 |
| DEL-03-03 `ScopeOfWork.md` | Production contract | E104, E105 |
| DEL-07-02 `ScopeOfWork.md` | Production contract | E90-E102 |
| DEL-07-04 `ScopeOfWork.md` / `_CONTEXT.md` | Production contract / working surface | E03-E13 / E02 |
| DEL-07-05 `ScopeOfWork.md` | Production contract | E14-E20 |
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

No `ISSUED` or `CHECKING` deliverable is touched. All eight are
`IN_PROGRESS`, so no reopening is involved and `write_status.sh` is not
used.

Under W-b, the table above shrinks to the decomposition and the three
`_CONTEXT.md` files. The eight SOW rows then become `project-setup` INCREMENTAL
handoffs carrying the same exact text, and the PRD, SPEC and PLAN edits go to a
separate owner-approved documentation change.

## 3. Register and exact text

`Amendment_Actions.csv` is the proposed authoritative register. Its 28 rows
map to intake rows 1–20 and 33–40, and each row names its exact edits.

`Evidence/Group2/amendment_edits.py` holds every edit as data (exact `old`
and `new` bytes). `Evidence/Group2/build_amendment_preview.py` renders the
preview and records pre-image and post-image hashes. Its `--check` mode
detects drift before application. Its `--apply` mode refuses to run without an
accepted SCA-APP-011 group-3 `DECISION.md`.

Wording rules applied throughout:

- **Non-destructive.** Retired requirements and clauses are marked
  `[RETIRED — SCA-APP-011]` and kept as dated history. Each affected Scope of
  Work gains a controlling `## SCA-APP-011 Current Contract (Controlling)`
  section, following the SCA-APP-010 precedent.
- **M-a.** The library is named as the interface. The Chirality tool
  contracts are named as retained SDK-path interfaces, with their live Codex
  exposure left to DEL-06-03. On the Codex path, agents use the Root tools.
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
`ScopeOfWork.md` files. The group-2 text in §3 replaces them.

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
| `lib/harness/client.ts` | Remove `scaffoldHarnessExecutionRoot` and the `ScaffoldExecutionRootResponse` import if it has no other use |
| `__tests__/lib/harness-client.test.ts` | Remove the scaffold import and the case "scaffolds execution roots through scaffold route" |
| `lib/runtime-client/daemon-harness-port.ts` | Remove the `scaffold` interface member, its `daemonClientUnavailable` entry, its scope-map entry (`scaffold: 'executionRoot'`) and the now-unused `ScaffoldExecutionRoot*` imports; the `'executionRoot'` scope kind goes too if nothing else uses it |
| `lib/runtime-client/runtime-daemon-harness-port.ts` | Remove `scaffold()` |
| `__tests__/lib/runtime-daemon-harness-port.test.ts`, `__tests__/api/harness/daemon-proxy-boundary.test.ts`, `__tests__/api/harness/turn-route-attachments.test.ts`, `__tests__/api/harness/fake-daemon-harness-port.ts` | Remove the scaffold stubs and the case "uses only the fixed app-dev project for contained scaffold requests" |
| `__tests__/api/working-root/deliverable-contracts.test.ts` | **Split** (below) |

**Add, and split the route test:**

- **`__tests__/lib/deliverable-contracts.test.ts` (new).** Port every case in
  the current route test's `describe('working-root deliverable contract routes')`
  that exercises status, transition or dependencies (lines 131–1134 at basis)
  to direct calls of `readDeliverableStatus`, `transitionDeliverableStatus`,
  `readDeliverableDependencies` and `writeDeliverableDependencies` in
  `lib/workspace/deliverable-contracts.ts`. The port covers:
  - the whole "human-ruled CHECKING reversal" block (10 cases);
  - the whole "reopening ISSUED -> IN_PROGRESS under an accepted amendment"
    block, including "inside a Git work tree" (6 cases);
  - the actor, approval-SHA, dependency, recorded-register and symlink cases.

  Where a case asserted an HTTP status and body, assert the thrown
  `WorkspaceValidationError`'s `code` and `status`, or the returned value.
  Cases that only exercised request-body parsing (missing field or wrong
  type → `INVALID_REQUEST`) have no library equivalent and are retired with the
  routes. List them in the run receipt.
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
- every loop-first shell file (set L excluded);
- `app/workbench/*` and `app/pipeline/*` (Q3 URLs).

**Records.**
- Update `docs/governance_harness/tranche_manifests/APP-REMOVE-LEGACY-FORMS-20260927.yaml`
  for the added deletions.
- Regenerate `exports/chirality-app/` with the export tooling.
- Write the run receipt, the loop receipt and the MEMORY entries (LOOP_INIT §5).
  Each affected deliverable's MEMORY entry points to SCA-APP-011.

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

D-APP-74 L107 stays in force for the loop-first shell, since set L is
excluded.

A dry run of `tools/coordination/accumulate_supersession_map.py` with the
SCA-APP-010 map as prior produces 63 rows with 0 findings. At group 3 the same
command writes the candidate `Supersession_Map.csv`.

## 6. Acceptance-conditional edits and group-3 procedure

Acceptance-conditional bytes:

| Item | Rule |
|---|---|
| E47 `{APPLICATION_DATE}` | The decomposition Coverage and Telemetry `Date`. Filled with the date in the group-3 `DECISION.md` heading (`YYYY-MM-DD`). It is the only slot; every other post-image hash is fixed in `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` |
| `_LATEST.md` | Moved to the accepted SCA-APP-011 snapshot folder only after group-3 acceptance. Its exact post-image is drafted in the group-3 package. The SCA-APP-010 entry becomes the historical predecessor |
| `checkpoint_snapshots/SCA-APP-011_GROUP-2_{date}/` and `SCA-APP-011_GROUP-2_AUTHORIZED.md` | Written from your group-2 act |
| `checkpoint_snapshots/SCA-APP-011_GROUP-3_{date}/` | Written from your group-3 act |
| Runtime notice | `DRAFT_NOTICE_TO_RUNTIME.md` copied to `projects/chirality-runtime/execution/_Coordination/NOTICE_{date}_APP_SCA-APP-011_SCAFFOLD_API.md` after group-3 acceptance |

Group-3 preparation, in order:

1. Resolve the group-2 decision snapshot, and verify it binds this
   `Amendment_Actions.csv` by hash.
2. Run `build_amendment_preview.py --check`. No drift is allowed.
3. Apply the edits with the group-3 date. This needs the `--apply` gate, so
   application happens only after acceptance. The group-3 package instead
   shows the applied candidate on a branch, built by applying the same edits
   with a placeholder date, and reviews that.
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
   for the eight deliverables and their neighbours.
2. **`dependency-extract`.** Run for DEL-02-02, DEL-02-01, DEL-02-03, DEL-07-04,
   DEL-07-05, DEL-08-02 and DEL-08-03, then `analyze_dep_closure.py`.
   - Retire DEP-02-02-005 to 009 and DEP-02-01-007.
   - DEP-02-01-008 follows HGD-2.
   - Refresh the wording of DEP-08-03-010 and DEP-08-02-003/005.
   - Only edges are removed, so no cycle can form.
3. **Audits.** `audit-decomp` (post-change baseline), then `audit-scope-closure`
   after the setup and code change.
4. **Code change** (§4) through the App loop, landed with the scope text under
   Q-a.
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

| Check | Result |
|---|---|
| `build_amendment_preview.py` | 113 edits in 15 files. Every `old` passage occurs exactly once, in sequence; post-images dry-run |
| `build_amendment_preview.py --check` | All 15 preimages match `PREIMAGE_POSTIMAGE.csv` |
| `validate_postimage.py` | PASS: 24 edited table rows keep their column count; all 8 edited Scopes of Work validate (exit 0 before and after); every edited paragraph that names a retired path carries an SCA-APP-011 marker (`Evidence/Group2/POSTIMAGE_VALIDATION.md`) |
| `accumulate_supersession_map.py` dry run | 63 rows, 0 findings |
| `--apply` guard | Refuses without an accepted group-3 `DECISION.md` |
| Group-1 baseline builder rerun (at `c08be56d6`) | Output identical to the accepted `Pre_Change_Coverage.json` apart from `basis_commit`: 54 nodes, 111 edges, 0 SCCs. The accepted file was restored unchanged (SHA-256 `ef2eb2f5…ab82`) |
| Root G0–G3 (`validate_root_materialization_fence.py`, `validate_root_harness_adapter.py`, `validate_root_surface_ownership.py`, `validate_root_work_graph_dispatch.py`) | G0, G1, G2 and G3 PASS on the package tree |
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
| `Amendment_Actions.csv` | `f571b75ae7043c92ac7dafb7f09abfed270b07baae27d0585a95e530f2d8e610` |
| `Supersession_Delta.csv` | `0dda716e70bbf0c19e74b9ec5ee82ab7dac760eabb343cbc21cdf8f9450d311b` |
| `Amendment_Preview.md` | `991d22294037aae3d78e381cde3cd10373380e06c7a7095a937345569de7e79a` |
| `DRAFT_NOTICE_TO_RUNTIME.md` | `7a7facf59435eac6425ebba013c33575734917eb86bcbac7dfa7e68aed6b559e` |
| `Evidence/Group2/amendment_edits.py` | `c3a8c3fa1e0c72c3b065728bb9503c6f20e5403299c96441d4945eba72686e0e` |
| `Evidence/Group2/build_amendment_preview.py` | `9ec350f89adff7d172584312faa0a871022ac1c41af3676d842c6e9dc201b668` |
| `Evidence/Group2/validate_postimage.py` | `444365e69856097dab4f18c468de4c1ee5833b60f9d964fd1aab9763eaa58319` |
| `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` | `52c035e7613d6f4ff3199daaaae83f7b2320d45aaccfc90566999d35c5a1252b` |
| `Evidence/Group2/POSTIMAGE_VALIDATION.md` | `e52f7dcab2da5f8b05e43c6b77ab570933d31700f281a0cb8fe005755cf99408` |
