---
amendment_id: SCA-APP-012
doc_kind: scope_change.run_summary
decomp_variant: SOFTWARE
checkpoint_group: 3
status: CANDIDATE_ready_for_independent_review
created: 2026-09-27
integrated_scope_and_code_commit: c47b74fd5
scope_text_candidate_commit: 8a3230d5e
integration_base: origin/main 974bf7da4
accepted_group2_snapshot: execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/
accepted_group2_commit: dad463311
pointer_posture: ACCEPTED_PREDECESSOR (SCA-APP-011)
---

# SCA-APP-012 — Checkpoint group 3: audited poststate (CANDIDATE)

> **Status: CANDIDATE, ready for independent review.** The scope text and the
> code change are integrated on one revision, `c47b74fd5` on `origin/main`
> `974bf7da4`, and validated together (Q-a). Next is the independent review of
> that revision, then this summary goes to the owner for the group-3 decision.
> CI on the PR is still to come. `_LATEST.md` still names SCA-APP-011. Nothing
> is merged.

---

## Checkpoint group 3 — what you will be asked to decide

### What accepting group 3 authorizes

In this order, exactly as listed in `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`:

1. **Decision folder.** `checkpoint_snapshots/SCA-APP-012_GROUP-3_{date}/`,
   recording your act. It is committed first.
2. **E26, `_LATEST.md` and the status records**, in one run of
   `Evidence/Group3/group3_finalize.py`. It first rechecks all 12 candidate
   hashes, the SCA-APP-011 pointer hash and the three status records, then:
   - sets the decomposition's Coverage and Telemetry `Revision` and `Date`
     (E26), and changes nothing else in it;
   - moves `_LATEST.md` from SCA-APP-011 to this snapshot, from the prepared
     `Evidence/Group3/LATEST_POSTIMAGE.md`;
   - writes the `Brief.md` status line, the `Decision_Log.md` G3 row and
     `Handoff_State.md` from their exact post-images.
3. **Post-acceptance record** under `_PostAcceptanceValidation/`.
4. **Merge.** One PR lands the scope text and the code change together (Q-a),
   once CI and the review have no blocking finding.
5. **Post-acceptance handoffs**, which are not part of the act:
   `project-setup` in `INCREMENTAL` mode; `dependency-extract` for DEL-02-03
   and DEL-08-03 against DX-01, DX-02, DX-03 and DX-05, then
   `analyze_dep_closure`; `audit-decomp`; `audit-scope-closure`; and the
   TM-APP-051 note.

It authorizes no lifecycle change, dependency-register write or release.

### Corrections

None. There is no group-3 correction of accepted text and no basis refresh of
an edited file: all 12 preimages were unchanged at the group-2 act, and the
candidate matches every recorded hash.

### What changed

**Scope text** (commit `8a3230d5e`): 79 of the 80 accepted edits, in 12 files:
the decomposition, the PRD, SPEC and PLAN, and the Scopes of Work of DEL-02-01,
DEL-02-02, DEL-02-03, DEL-06-03, DEL-07-02, DEL-07-03, DEL-08-02 and DEL-08-03.
E26 is withheld.

**Code** (commits `85f206dae` code, `8df9c3f78` records, `c47b74fd5` export;
App loop, `Propagation_Plan.md` §4). 46 frontend files: 20 deleted, 25
modified, 1 added; 205 lines added and 1,453 removed.

| Change | Files (under `frontend/src/`) |
|---|---|
| Loop-first shell removed | `components/shell/loop-shell.tsx`, `portal-loop-shell.tsx`, `loop-tertiary-shell.tsx`, `sidebar-right-loop-layout.tsx`, `tertiary-sidebar-tabs.tsx` |
| Role-directory panel removed | `components/portal/agent-matrix.tsx` and its test |
| Portal helpers removed (L-lib) | `lib/portal/agent-matrix-cells.ts`, `agent-matrix-launch.ts` and their tests |
| Provider and scope route removed | `components/workspace/deliverables-provider.tsx` and its mount in `app/layout.tsx`; `app/api/working-root/scope/route.ts` |
| Flat-file workflow list and read route removed (W-b) | `components/woven-dialogue/workflows-view.tsx`, `workflow-detail.tsx`, their test; `app/api/working-root/workflow/{route,workflow-store,workflow-read-contract}.ts` and their test |
| `legacy` prop and `?legacy=1` link removed | `WovenDialogueRoute` and its four callers; `legacyHref` in `woven-dialogue-shell.tsx`, the `Navigator` and `ShellFrame` props |
| Symbol residue | `lib/shell/loop-first.ts` keeps only `CHAT_SECTION`; `PersonaPicker` loses `buildHref`; `WorkspaceSidebar` loses the three tab props, constants, panel branches and `SidebarTabId` members |
| CSS | `app/globals.css` loses the 11 legacy-only tokens and 11 dead selector families; `workflows.module.css` keeps only `header` and `tabs` |
| Copy | Layout metadata "Dialogue shell for local agent execution"; the four page Suspense fallbacks read "Loading..." |
| Kept | `/workbench` and `/pipeline` pages (P-keep), `chat-panel.tsx` unchanged, `woven-workspace-state.ts`, `persona-resolution.ts`, `guarded-session-selection.ts`, `task-scope.ts`, `pipeline-dispatch-contract.ts`, `scanProjectScopes`, `/api/project/deliverables`, `workflow-drafts`, `method-library-view.tsx`; `electron/renderer-window-policy.ts`, `electron/main.ts`, the packaged security proof and the contract pins untouched |

**Tests.**
- **Ported:** case 1 of the retired `agent-matrix-cells.test.ts` into
  `persona-resolution.test.ts`, reading `CHIRALITY_ROLES` from
  `@chirality/runtime-contracts/v3`: the three direct-entry roles, HELP_HUMAN
  as the new-chat default, and TASK not direct-entry.
- **Added:** the DEL-08-02-REQ-004 case in the same file. RECONCILING and the
  matrix labels of App `docs/TYPES.md` §4.1–4.2 (rows NORMATIVE, OPERATIVE,
  EVALUATIVE; columns GUIDING, APPLYING, JUDGING, REVIEWING), in upper and
  lower case, each resolve to HELP_HUMAN, and none is a `PERSONA_ALIASES` key.
- **Added:** `__tests__/components/chat-panel-role-picker-guard.test.tsx`. The
  compact role picker is enabled with no turn running, disabled while a turn
  runs, and enabled again when it ends.
- **Replaced:** `workspace-sidebar.test.ts` has one default-tabs case: eight
  tabs, Workflow selected, no Portal, Workbench or Pipeline tab.
- **Trimmed and renamed:** `loop-first.test.ts` keeps one case, on
  `CHAT_SECTION`, under a new name. `pkg08-compatibility-boundaries.test.ts`
  keeps the role-boundary case (now from `CHIRALITY_ROLES`) and the dispatch
  case.
- **Edited as §4 requires, paths kept:** `woven-dialogue-route.test.tsx`,
  `woven-dialogue-shell.test.tsx` and `woven-dialogue-navigator.test.tsx` lose
  the `legacy`/`legacyHref` props and cases, and `historical-chat-reveal.test.tsx`
  loses `legacyHref`. The scope text cites these files by path only; "kept"
  in §6 of the previous revision of this summary meant the paths, because the
  §4 edits are needed for the typecheck.
- **Relabelled:** `loop-tertiary-routes.test.ts` keeps its file name and both
  cases; its `describe` label is "Workbench and Pipeline route clients".

**The guard test really guards.** With `disabled={isRunning}` removed from
`chat-panel.tsx`, the running-turn case of the role-picker test fails
("expected 'false' to be 'true'"). The file was restored and is unchanged in
the diff.

**Records** (commit `8df9c3f78`): the run receipt
`execution/_Coordination/AgentRuns/APP-RETIRE-LOOP-FIRST-UI-2026-09-27/RECEIPT.md`;
Receipt-280 in `loop/LOOP_RECEIPTS.md` (parent 279); the tranche manifest
`docs/governance_harness/tranche_manifests/APP-RETIRE-LOOP-FIRST-UI-20260927.yaml`;
MEMORY rows in DEL-02-01, DEL-02-02, DEL-02-03 and DEL-08-02. The records cite
the group-1 and group-2 snapshots and state that the group-3 snapshot does not
exist yet. The export (commit `c47b74fd5`) is regenerated; its manifest goes
from 1,882 to 1,864 rows.

### Checks

| Check | Result |
|---|---|
| Candidate hashes | 12/12 match `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` |
| Edits present | 79/79; E26 withheld; no `{APPLICATION_DATE}` literal |
| Write containment (`dad463311..c47b74fd5`, integrated) | 84 paths. Scope text is exactly the 12 accepted files. 55 are code-change paths (46 frontend files, 4 MEMORY rows, `LOOP_RECEIPTS.md`, 2 export files, the run receipt and the tranche manifest); 17 are in the SCA folder. No protected path changed; 0 paths in no permitted category |
| Code alignment | 19/19 cited live files present; the new role-picker test present; 0 of the 20 §4 deletions remain; `renderer-window-policy.ts` at its pinned hash |
| Scope of Work validator; retired-item sweep | 8/8 pass; 114 files, 0 uncovered units, 3 listed historical passages |
| Topology, coverage, lifecycle, closure | Unchanged by the amendment: 10/52/84/10; ledger 78/5/1; 53 `IN_PROGRESS`, 1 `OPEN`; 54 nodes, 104 edges, 0 SCCs; `EVQ-006` ×36 only (§3) |
| Removed code references | None left in product, tests, Electron or scripts for the retired routes, provider, shells, helpers, view, `legacyHref` or the old copy; `scanProjectScopes` and `/workbench`, `/pipeline` remain as intended (§3) |
| Supersession map | 85 rows (63 prior + 22), 0 findings; `--check-map` clean; LF line endings |
| Group-3 finalize path | 18/18 on a scratch copy (`Evidence/Group3/check_group3_finalize.py`) |
| TypeScript | `tsc` 0; Electron typecheck 0 (code agent) |
| Full Vitest | 2,560 passed; only the known uid-0 `harness-attachment-resolver` failure (code agent) |
| Build | `npm run build` passes; the two retired API routes are absent from the route table, and `/workbench` and `/pipeline` remain (code agent) |
| `tools/run_affected_tests.py` | 1,156 passed (code agent) |
| Root validators | §9 |
| `AuditState` (raw) / `AdjustedAuditState` | `WARNINGS` / `WARNINGS`. Every tool finding was present before the change; 0 new findings |

### Still to come

- The independent review of the integrated revision (scope text and code
  together, Q-a).
- CI on the PR. The PR branch sits on current `origin/main`, which is
  `5ae22926e`; from `974bf7da4` main changed only `projects/pec/**` and
  `projects/chirality-piping/**`, outside every App path, the write boundary
  and the code-change categories. CI runs when the PR is opened and is a
  merge gate after your acceptance.
- The premerge harness gate (`harness:validate:premerge`) needs a running
  harness server and Codex and could not run in the code agent's environment;
  it runs in CI or on a workstation.

---

## 1. Amendment

SCA-APP-012 retires the loop-first compatibility UI (its shells, the
role-directory panel, the discarded `legacy` prop and `?legacy=1` link, and
the `lib/portal` matrix helpers), `DeliverablesProvider`,
`GET /api/working-root/scope`, the unmounted flat-file workflow view with
`GET /api/working-root/workflow`, and DEL-02-03-REQ-009. It restates
DEL-02-03-REQ-010, keeps `/workbench` and `/pipeline` as unlisted entries into
the dialogue shell, and records that no App-side scaffold entry is planned.
The owner accepted group 1 and group 2 on 2026-09-27.

**Commit identities.** The owner accepted group 2 on the package at
`a4295f9ed`. The group-2 snapshot is `dad463311`, the scope-text candidate
`8a3230d5e`, and the integrated revision `c47b74fd5`. The code was built on
its own branch from `974bf7da4` and cherry-picked here (as `85f206dae`,
`8df9c3f78` and `c47b74fd5`). The evidence in this folder is based on
`974bf7da4`, because `validate_candidate.py` measures containment from
`dad463311`. On the main-based PR branch that measure would also count main's
later PEC and Piping commits.

## 2. Actions taken (group-3 preparation)

| Step (method.md) | Action | Evidence |
|---|---|---|
| Consume group 2 | `SCA-APP-012_GROUP-2_AUTHORIZED.md` resolved; the manifest's 11 hashes verified | `checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/ACCEPTED_MANIFEST.csv` |
| Pointer posture | `ACCEPTED_PREDECESSOR`; `_LATEST.md` (`904c1bd6…85637`) unchanged | `Handoff_State.md` |
| Pre-change refresh | The accepted group-1 builder rerun at `dad463311`, before the candidate, to separate basis movement (G1B-01) from the amendment | `Evidence/Group3/PRE_CHANGE_REFRESH.json` |
| 1–2. Apply | `build_amendment_preview.py --check`, then `--candidate` on the repository tree, both with every `GIT_*` variable removed from the environment (`Decision_Log.md` G2-NOTE-2, N10). 79 edits written; each file matches its candidate hash | commit `8a3230d5e` |
| Code change | App loop, `Propagation_Plan.md` §4 (commits `85f206dae`, `8df9c3f78`, `c47b74fd5`) | run receipt, Receipt-280, tranche manifest |
| 5. Supersession | `accumulate_supersession_map.py` over the SCA-APP-011 map and the delta: 85 rows, 0 findings; normalized to LF; a second run with `--check-map` against the written map: 0 findings | `Supersession_Map.csv`, `Evidence/Group3/Supersession_Findings.csv` |
| 5. Post-change baseline | The accepted group-1 builder rerun on the integrated revision (commit `30e8495ec`, the integrated tree plus its validation report) | `Post_Change_Coverage.json`, `Evidence/Group3/PRE_POST_COMPARISON.md` |
| 5. Validation | `validate_candidate.py --accepted-commit dad463311 --integrated --code-record …/APP-RETIRE-LOOP-FIRST-UI-2026-09-27 --code-record …/APP-RETIRE-LOOP-FIRST-UI-20260927.yaml` at `c47b74fd5`: PASS | `Evidence/Group3/CANDIDATE_VALIDATION.md` |
| Acceptance-conditional list | Seven items with exact post-images and the finalize path | `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`, `LATEST_POSTIMAGE.md`, `STATUS_RECORDS_POSTIMAGE.md`, `HANDOFF_STATE_POSTIMAGE.md`, `group3_finalize.py`, `check_group3_finalize.py` |

**Disclosure.** A full `audit-decomp` TASK run was not dispatched from this
bounded session. The post-change baseline reruns the same registered tools as
the accepted pre-change baseline (`Propagation_Plan.md` §6 step 6). A full
`audit-decomp` is a post-acceptance handoff.

**Coverage wrapper change.** The accepted group-1 builder reads the legacy
components to collect their CSS class tokens, and the code change deletes
them. `Evidence/Group3/build_post_change_coverage.py` therefore now starts the
token set from the accepted baseline's tokens, and still adds any token found
in a legacy component that exists. On a tree where the components exist the
result is unchanged. The refresh at `dad463311` was produced before this
change, on a tree where they existed.

**Git hardening (N10).** The group-2 `--candidate` gate is bound in the
group-2 manifest and was not edited; it was run in a clean environment. The
group-3 tools do not share its weakness:
- `validate_candidate.py` runs every git call with `GIT_*` removed, requires
  the current directory to be the work-tree top, and stops on any git error;
- `build_post_change_coverage.py` removes `GIT_*` before running the builder
  and resolves HEAD with a git call that must succeed;
- `group3_finalize.py` makes no git call; its gate is the committed group-3
  decision folder, the owner's act quoted verbatim in it, and the group-2
  pointer. `check_group3_finalize.py` runs it with `GIT_DIR=/nonexistent` to
  show that no git environment changes its result.

## 3. Pre-change vs post-change

The full comparison is in `Evidence/Group3/PRE_POST_COMPARISON.md`. It has
three columns: the accepted baseline (`adc8bdae1`), the refresh at
`dad463311`, and the integrated candidate.

**Basis movement (refresh vs accepted), from main, not the amendment:**
`dependency_rows` (DEP-02-01-006 now `UPSTREAM`/`INTERFACE`) and
`analyze_dep_closure` (103 → 104 edges), exactly G1B-01.

**Amendment effect (candidate vs refresh):**
- `decomposition_sha256` moves to `92926772…fad4e0`, and
  `repository_topology.highest_decision_log_id` from DEC-026 to DEC-027;
- `frontend_reachability`: 259 → 244 product modules, 211 → 199 reachable.
  Nothing is left that is reachable only through the discarded `legacy`
  element or through `DeliverablesProvider`, and none of the in-scope
  unreached modules remains. `lib/workspace/task-scope.ts` is now test-only,
  as Impact Assessment §3.1 (S2) expected; it stays as a library for
  DEL-08-03. The `/workbench` and `/pipeline` page modules stay (P-keep);
- `frontend_references`: no product, test, Electron or script reference to
  `/api/working-root/scope`, `/api/working-root/workflow?`,
  `DeliverablesProvider`, the `legacy` element, `legacyHref`, the loop-first
  shells, `AgentMatrix`, `WorkflowsView`, `buildPortalPersonaHref`,
  `isRoleSelectionBlocked` or the old layout and loading copy. The only
  remaining hit is "open legacy interface" in the frozen
  `renderer-window-policy.ts` comment, the recorded residual of
  `Propagation_Plan.md` §11;
- `legacy_css_tokens` and `dead_css_candidates`: the 11 legacy-only tokens and
  the 11 dead selector families now have 0 selectors in `globals.css`. Shared
  tokens (`panel*`, `shell-pane*`, `button-muted`) keep their users;
- `scope_text_hits` rises, because the retirement text names each retired item
  next to its SCA-APP-012 marker. The sweep in `validate_candidate.py`
  check 5 is the measure of uncovered mentions: 0.

Every other field is equal: topology 10/52/84/10, ledger 78/5/1, forward and
reverse coverage, no scope item or objective without a deliverable, lifecycle
53 `IN_PROGRESS` and 1 `OPEN`, no `ISSUED` or `CHECKING` deliverable, the
affected deliverables and scope items, objective supporters, the companion
register and the pointer hash, `audit_structure` and
`validate_decomposition_registers`.

- **Coverage.** No coverage regression, no new orphan and no
  parent-partition change.
- **SOFTWARE design rules.** Package flatness, the Scope Ledger (84 rows,
  78/5/1) and the envelopes are unchanged. Stable IDs are preserved and no
  retired ID is reused. DEC-027 and the Change Log line are present.

## 4. Finding classification

| # | Finding | Source | Pre | Post | Class |
|---|---|---|---|---|---|
| F1 | `EVQ-006` ×36 (EvidenceFile cells that resolve in none of the validator's forms) | `validate_decomposition_registers.py` | 36 | 36 | Carried, pre-existing |
| F2 | "partition directory contract is incomplete" | `audit_structure.py` | yes | yes | Carried, pre-existing |
| F3 | "required tool roots are missing" | `audit_structure.py` | yes | yes | Carried, pre-existing |
| F4 | Closure `subject_status` FAIL (2 schema-invalid registers, 2 units without a node) | `analyze_dep_closure.py` | yes | yes | Carried, pre-existing |
| X2 | DEP-02-03-009, DEP-02-03-004 and DEP-08-03-007 still carry the pre-amendment wording | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: group 2, `Propagation_Plan.md` §8 item 2 (DX-01 to DX-03, DX-05) |
| X3 | Coverage and Telemetry still reads "amended by SCA-APP-011 / 2026-09-27" | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: group 2, §6 (E26) |
| X4 | `_LATEST.md` on SCA-APP-011; TM-APP-051 note not recorded | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: the method.md pointer rule; §8 item 5 |
| X5 | `renderer-window-policy.ts` L13-14 still names the "open legacy interface" link | candidate review | yes | yes | Recorded residual, `Propagation_Plan.md` §11 (D-APP-121 frozen file) |

X1 of the previous revision (the code still carried the retired items) is
resolved by the integrated code change.

- **Raw `AuditState`:** `WARNINGS`.
- **`AdjustedAuditState`:** `WARNINGS` (F1–F4, carried).
- **New findings:** 0.

## 5. Acceptance-conditional edits (exact list)

See `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`. None is applied
before acceptance, and any edit not on the list returns to the owner.

1. **Decision folder.** Write `checkpoint_snapshots/SCA-APP-012_GROUP-3_{date}/`
   (`DECISION.md` headed `# SCA-APP-012 checkpoint group 3 — accepted …`, with
   the owner's act as a `> ` quoted line) and commit it first.
2. **Finalize.** Run
   `group3_finalize.py --date {date} --owner-act "{OWNER_ACT_VERBATIM}" --utc {UTC}`
   (optionally `--dry-run` first). It refuses unless the decision folder, the
   verbatim act and the group-2 pointer are present and every before-state
   holds, then writes:
   - E26 in the decomposition; for `{date}` = 2026-09-27 the result is
     `6ac78118…29a577`;
   - `_LATEST.md` from `LATEST_POSTIMAGE.md`; for 2026-09-27 the result is
     `3d7e0352…0bc95d8b`;
   - the `Brief.md` status line and `Decision_Log.md` G3 row
     (`STATUS_RECORDS_POSTIMAGE.md`) and `Handoff_State.md`
     (`HANDOFF_STATE_POSTIMAGE.md`), with `{APPLICATION_DATE}`,
     `{OWNER_ACT_VERBATIM}` and `{UTC}`.

   The post-images apply to a plain acceptance only.
3. **Post-acceptance record.** Write `_PostAcceptanceValidation/SCA-APP-012_{UTC}/`.

## 6. Code change against the scope text

Every requirement the scope text and the group-3 checks place on the code is
met at `c47b74fd5` (`CANDIDATE_VALIDATION.md` checks 3 and 7):
- the new test `frontend/src/__tests__/components/chat-panel-role-picker-guard.test.tsx`,
  cited by the DEL-08-02 Scope of Work, exists;
- every other test and source path the scope text cites keeps its path;
- the 20 §4 deletions are all absent;
- `renderer-window-policy.ts`, `electron/main.ts`, the packaged security proof,
  the contract pins, every scope-text file, `_STATUS.md`, `Dependencies.csv`,
  `_DEPENDENCIES.md`, `_LATEST.md`, the companion register and the Task
  Management register are untouched by the code commits;
- the code records sit only in the permitted categories.

## 7. Recommended downstream reruns (not executed)

1. **`project-setup` in `INCREMENTAL` mode.** It scaffolds nothing; the
   contracts are already written (T-a).
2. **`dependency-extract`** for DEL-02-03 and DEL-08-03 against DX-01, DX-02,
   DX-03 and DX-05, then `analyze_dep_closure.py`.
3. **`audit-decomp`** (full), then **`audit-scope-closure`**.
4. **Task Management TM-APP-051** note, by the row owner.

## 8. Handoff state

See `Handoff_State.md`.

| Field | Value |
|---|---|
| `DecompositionTruthState` | `INCOMPLETE` (E26 pending) |
| `DerivativePackageState` | `INCOMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `WARNINGS` |
| `AdjustedAuditState` | `WARNINGS` |
| `ReadyForNextPhase` | `NOT_APPLICABLE` |

**Closure verdict:** `OPEN_PENDING_DERIVATIVE_CLOSURE`.

## 9. Repository-change evidence

Integration branch on `origin/main` `974bf7da4`:

| Commits | Content |
|---|---|
| `660873229` … `530ad4d10` | Group-1 package, revisions 1–4 |
| `230528a0f` | Group-1 acceptance record |
| `68127fa8e` … `a4295f9ed` | Group-2 package, revisions 1–2 |
| `dad463311` | Group-2 snapshot and pointer |
| `8a3230d5e` | Scope-text candidate |
| `65ecc03e5`, `23b622da8` | Group-3 evidence and presentation (scope-text candidate) |
| `85f206dae`, `8df9c3f78`, `c47b74fd5` | Code, records, export |
| `30e8495ec` | Candidate validation on the integrated revision |
| the commit carrying this file | Post-change coverage on the integrated revision, this presentation and `Handoff_State.md` |

### Root and repository checks (at `a12759dba`, base `974bf7da4`)

| Check | Result |
|---|---|
| G0, G1, G2, G3 (`validate_root_materialization_fence.py`, `validate_root_harness_adapter.py`, `validate_root_surface_ownership.py`, `validate_root_work_graph_dispatch.py`) | PASS |
| G4 (`validate_instruction_tranche_manifest.py --base 974bf7da4 --head HEAD --added-manifests-only`) | Exit 0; 107 changed paths, 1 on the instruction surface, checked against the added tranche manifest `APP-RETIRE-LOOP-FIRST-UI-20260927.yaml` |
| `validate_conflict_markers.py`, `validate_run_record_leaks.py` (base `974bf7da4`) | PASS; PASS (1 run-record file, 0 possible credentials) |
| `build_workflow_index.py --check` | PASS (78 methods) |
| `git diff --check` (base `974bf7da4`) | PASS |
| `exports/chirality-app/export_public.py`, run twice | No tracked change; staging removed |
| `validate_candidate.py --integrated` (at `c47b74fd5`) | PASS |
| `check_group3_finalize.py` | 18/18 PASS |
| `group3_finalize.py --check` | OK |

The group-2 `build_amendment_preview.py --check` is a pre-candidate check: on
the written candidate it reports every file as drifted from its preimage, by
design. Its group-3 counterpart is `validate_candidate.py` check 1 (12/12
candidate hashes).

The commit that adds this table changes only `RUN_SUMMARY.md`.

## Evidence basis

| Artifact | SHA-256 |
|---|---|
| `Supersession_Map.csv` | `83e5e25fec5dbedee83d184d4b831082169d5a7c46346cd7f3f3a18e45c73eaf` |
| `Post_Change_Coverage.json` | `75931b24bba5196ce641094890dfa2b88df064927875683579c3accdd95a6496` |
| `Handoff_State.md` | `5730efb09753ea793768440907be848ff831b559eaebadf35983535bb13a7928` |
| `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` | `cabb96565607e394d656d29e72d4f4b18055a10e12c9b1ae670688f09c1165bb` |
| `Evidence/Group3/CANDIDATE_VALIDATION.md` | `672c90e40612998d56b33c41f2b4c7418a0a3be187d196ac6cdc7d3e3f62986f` |
| `Evidence/Group3/validate_candidate.py` | `cd6666281f9c412ebcf4c969e7fe384ce25cd38a35319c1284c9a7bdc8c18a67` |
| `Evidence/Group3/build_post_change_coverage.py` | `01432c40ea338b170d99e4b599ef0cc49c67cd66dce1873dd6a4536e5f1efec9` |
| `Evidence/Group3/PRE_CHANGE_REFRESH.json` | `220ecfbaf56cf2f99c27503c86b8207db367264e8d4696caddd2b41cd7d83e91` |
| `Evidence/Group3/PRE_POST_COMPARISON.md` | `e8467bdcde4b7ca3ba49c7f5d080b45bf3f647edabdfa6318e1305dcafb8841c` |
| `Evidence/Group3/Supersession_Findings.csv` | `d288096f20845863777a4b5d0956be5c7783577857e3148e6d174200b74eb8b4` |
| `Evidence/Group3/group3_finalize.py` | `6e519e52b978a8d1388969a908a782ffa7f7bb32fe83b426ae625cc8fa24c412` |
| `Evidence/Group3/check_group3_finalize.py` | `5258b204f68af90965c3f4263c5d6982decbbea4d616f48d22976d5c767e2632` |
| `Evidence/Group3/LATEST_POSTIMAGE.md` | `dc893e66b594446f5099848dad09cc79866e2e5b1f934bc50883bc0e0af2803d` |
| `Evidence/Group3/STATUS_RECORDS_POSTIMAGE.md` | `1807f8d19f3a0381c64115f2940e23b0651ecd491baeea46e457f0d2efb3e59c` |
| `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md` | `ea902c05b03f8b4ea273d951d487fa1e09b6fc6938b79eaef28436ef3dbd8f29` |
