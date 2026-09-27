---
amendment_id: SCA-APP-012
doc_kind: scope_change.run_summary
decomp_variant: SOFTWARE
checkpoint_group: 3
status: CANDIDATE_ready_for_independent_review
created: 2026-09-27
scope_text_candidate_commit: 8a3230d5e
accepted_group2_snapshot: execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/
accepted_group2_commit: dad463311
pointer_posture: ACCEPTED_PREDECESSOR (SCA-APP-011)
---

# SCA-APP-012 — Checkpoint group 3: audited poststate (CANDIDATE)

> **Status: CANDIDATE, ready for independent review.** The accepted scope
> text is written (79 of 80 edits; E26 withheld) and validated. The code
> change of `Propagation_Plan.md` §4 is being prepared on a separate branch
> and is integrated for the joint review (Q-a); §6 lists what it must satisfy.
> After integration, `Evidence/Group3/validate_candidate.py --integrated`
> reruns on the integrated revision, then the independent review covers scope
> text and code together, then this summary goes to the owner. `_LATEST.md`
> still names SCA-APP-011. Nothing is merged.

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
an edited file: all 12 preimages were unchanged at the group-2 act and the
candidate matches every recorded hash.

### What changed

**Scope text** (commit `8a3230d5e`): 79 of the 80 accepted edits, in 12 files:
the decomposition, the PRD, SPEC and PLAN, and the Scopes of Work of DEL-02-01,
DEL-02-02, DEL-02-03, DEL-06-03, DEL-07-02, DEL-07-03, DEL-08-02 and DEL-08-03.
E26 is withheld.

**Code:** to be integrated (§6).

### Checks

| Check | Result |
|---|---|
| Candidate hashes | 12/12 match `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` |
| Edits present | 79/79; E26 withheld; no `{APPLICATION_DATE}` literal |
| Write containment (`dad463311..8a3230d5e`) | 12 paths, exactly the accepted write boundary; no code path; no `_STATUS.md`, `Dependencies.csv`, `_DEPENDENCIES.md`, `_LATEST.md`, companion-register, Task Management, Electron-probe, packaged-proof or contract-pin change |
| Scope of Work validator; retired-item sweep | 8/8 pass; 114 files, 0 uncovered units, 3 listed historical passages |
| Topology, coverage, lifecycle, closure | Unchanged by the amendment: 10/52/84/10; ledger 78/5/1; 53 `IN_PROGRESS`, 1 `OPEN`; 54 nodes, 104 edges, 0 SCCs; `EVQ-006` ×36 only (§3) |
| Supersession map | 85 rows (63 prior + 22), 0 findings; `--check-map` clean; LF line endings |
| Group-3 finalize path | 18/18 on a scratch copy (`Evidence/Group3/check_group3_finalize.py`) |
| Code alignment (scope-text-only candidate) | 19/19 cited live files present; the new role-picker test and the 20 §4 deletions await the code change; `renderer-window-policy.ts` at its pinned hash |
| Root validators | §9 |
| `AuditState` (raw) / `AdjustedAuditState` | `WARNINGS` / `WARNINGS`. Every tool finding was present before the change; 0 new findings |

### Still to come

- The code change, integrated for the joint review (Q-a), and
  `validate_candidate.py --integrated` on the integrated revision.
- The independent review of scope text and code together.
- CI on the PR. It runs when the PR is opened, and it is a merge gate after
  your acceptance.

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
`8a3230d5e`. The branch is on `origin/main` `974bf7da4`.

## 2. Actions taken (group-3 preparation)

| Step (method.md) | Action | Evidence |
|---|---|---|
| Consume group 2 | `SCA-APP-012_GROUP-2_AUTHORIZED.md` resolved; the manifest's 11 hashes verified | `checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/ACCEPTED_MANIFEST.csv` |
| Pointer posture | `ACCEPTED_PREDECESSOR`; `_LATEST.md` (`904c1bd6…85637`) unchanged | `Handoff_State.md` |
| Pre-change refresh | The accepted group-1 builder rerun at `dad463311`, before the candidate, to separate basis movement (G1B-01) from the amendment | `Evidence/Group3/PRE_CHANGE_REFRESH.json` |
| 1–2. Apply | `build_amendment_preview.py --check`, then `--candidate` on the repository tree, both with every `GIT_*` variable removed from the environment (`Decision_Log.md` G2-NOTE-2, N10). 79 edits written; each file matches its candidate hash | commit `8a3230d5e` |
| 5. Supersession | `accumulate_supersession_map.py` over the SCA-APP-011 map and the delta: 85 rows, 0 findings; normalized to LF; a second run with `--check-map` against the written map: 0 findings | `Supersession_Map.csv`, `Evidence/Group3/Supersession_Findings.csv` |
| 5. Post-change baseline | The accepted group-1 builder rerun on the committed candidate | `Post_Change_Coverage.json`, `Evidence/Group3/PRE_POST_COMPARISON.md` |
| 5. Validation | `validate_candidate.py --accepted-commit dad463311 --head 8a3230d5e`: PASS | `Evidence/Group3/CANDIDATE_VALIDATION.md` |
| Acceptance-conditional list | Seven items with exact post-images and the finalize path | `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`, `LATEST_POSTIMAGE.md`, `STATUS_RECORDS_POSTIMAGE.md`, `HANDOFF_STATE_POSTIMAGE.md`, `group3_finalize.py`, `check_group3_finalize.py` |

**Disclosure.** A full `audit-decomp` TASK run was not dispatched from this
bounded session. The post-change baseline reruns the same registered tools as
the accepted pre-change baseline (`Propagation_Plan.md` §6 step 6). A full
`audit-decomp` is a post-acceptance handoff.

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
`dad463311`, and the candidate.

**Basis movement (refresh vs accepted), from main, not the amendment:**
`dependency_rows` (DEP-02-01-006 now `UPSTREAM`/`INTERFACE`) and
`analyze_dep_closure` (103 → 104 edges), exactly G1B-01.

**Amendment effect (candidate vs refresh):**
- `decomposition_sha256` moves to `92926772…fad4e0`;
- `repository_topology.highest_decision_log_id` moves from DEC-026 to
  DEC-027;
- `scope_text_hits` rises, because the retirement text names each retired item
  next to its SCA-APP-012 marker. The sweep in `validate_candidate.py`
  check 5 is the measure of uncovered mentions: 0.

Every other field is equal: topology 10/52/84/10, ledger 78/5/1, forward and
reverse coverage, no scope item or objective without a deliverable, lifecycle
53 `IN_PROGRESS` and 1 `OPEN`, no `ISSUED` or `CHECKING` deliverable, the
affected deliverables and scope items, objective supporters, the frontend
reachability and references (no code changed), the companion register and the
pointer hash, `audit_structure` and `validate_decomposition_registers`.

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
| X1 | The code still carries the retired shells, helpers, provider, routes and view | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: the §4 code change, integrated for the joint review (Q-a) |
| X2 | DEP-02-03-009, DEP-02-03-004 and DEP-08-03-007 still carry the pre-amendment wording | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: group 2, `Propagation_Plan.md` §8 item 2 (DX-01 to DX-03, DX-05) |
| X3 | Coverage and Telemetry still reads "amended by SCA-APP-011 / 2026-09-27" | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: group 2, §6 (E26) |
| X4 | `_LATEST.md` on SCA-APP-011; TM-APP-051 note not recorded | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: the method.md pointer rule; §8 item 5 |

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

## 6. The code change: what it must satisfy

The code change is repository work by the App loop, on its own branch, under
`Propagation_Plan.md` §4 (revision 2, bound in the group-2 manifest). For the
joint review it must also satisfy what the written scope text and the group-3
checks rely on:

1. **Test files the scope text names.**
   - New: `frontend/src/__tests__/components/chat-panel-role-picker-guard.test.tsx`
     (the role picker in `chat-panel.tsx` is disabled while a turn runs). The
     DEL-08-02 Scope of Work cites this exact path.
   - Kept, same path: `loop-tertiary-routes.test.ts` (both cases; only the
     `describe` label changes), `woven-dialogue-route.test.tsx`,
     `persona-resolution.test.ts` (plus the ported registry case and the
     RECONCILING/matrix-label case), `guarded-session-selection.test.ts`,
     `pkg08-compatibility-boundaries.test.ts` (role-boundary and dispatch
     cases kept), `pipeline-dispatch-contract.test.ts`,
     `api/harness/routes.test.ts`, `woven-dialogue-shell.test.tsx`,
     `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`
     and `chat-panel-folder-binding.test.tsx`.
2. **Source files the scope text names, kept:** `components/shell/chat-panel.tsx`
   (`PersonaPicker … disabled={isRunning}`), `lib/shell/persona-resolution.ts`,
   `lib/woven-dialogue/guarded-session-selection.ts`,
   `lib/workspace/task-scope.ts`, `components/woven-dialogue/method-library-view.tsx`,
   `app/api/project/deliverables/route.ts`, `scanProjectScopes`,
   `app/api/working-root/workflow-drafts/**`, and both page routes
   `app/workbench/page.tsx` and `app/pipeline/page.tsx` (P-keep).
3. **The 20 deletions of §4 are all absent**, including the three
   `app/api/working-root/workflow/` files and both tests of the removed view
   and route.
4. **Untouched:** `electron/renderer-window-policy.ts` (SHA-256
   `e2d63d32423d1ef6b0a03259235676ac9cefadde00e4f067be4f13e5ed2cc3ed`, pinned by
   D-APP-121), `electron/main.ts`,
   `scripts/run-packaged-security-proof.mjs`,
   `src/__tests__/contract-pins.manifest.ts`, every scope-text file (docs,
   decomposition, Scope of Work, `_CONTEXT.md`), every `_STATUS.md`,
   `Dependencies.csv` and `_DEPENDENCIES.md`, `_LATEST.md`, the companion
   register and the Task Management register.
5. **Where its records may go:** `frontend/src/**`; the `MEMORY.md` of
   DEL-02-01, DEL-02-02, DEL-02-03 and DEL-08-02; `loop/LOOP_RECEIPTS.md`;
   `exports/chirality-app/**`; and its run-receipt folder and tranche
   manifest, which are named to `validate_candidate.py` with `--code-record`.
   Its records cite the SCA-APP-012 group-2 snapshot.
6. **Gate after integration:**
   `validate_candidate.py --accepted-commit dad463311 --integrated --code-record <run folder> --code-record <tranche manifest>`
   must pass. It then requires the new test file and the absence of all 20
   deleted modules, and it still requires the 12 candidate hashes, so the
   code branch must not rewrite any scope-text file.

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

Branch `worktree-agent-ac8845f197e7cf998`, on `origin/main` `974bf7da4`:

| Commits | Content |
|---|---|
| `660873229` … `530ad4d10` | Group-1 package, revisions 1–4 |
| `230528a0f` | Group-1 acceptance record |
| `68127fa8e` … `a4295f9ed` | Group-2 package, revisions 1–2 |
| `dad463311` | Group-2 snapshot and pointer |
| `8a3230d5e` | Scope-text candidate |
| the commit carrying this file | Group-3 evidence and this presentation |

### Root and repository checks (at `65ecc03e5`, base `origin/main` `974bf7da4`)

| Check | Result |
|---|---|
| G0, G1, G2, G3 (`validate_root_materialization_fence.py`, `validate_root_harness_adapter.py`, `validate_root_surface_ownership.py`, `validate_root_work_graph_dispatch.py`) | PASS |
| G4 (`validate_instruction_tranche_manifest.py --base 974bf7da4 --head HEAD --added-manifests-only`) | Exit 0; 0 changed paths on the instruction surface |
| `validate_conflict_markers.py`, `validate_run_record_leaks.py` (base `974bf7da4`) | PASS; PASS (0 run-record files) |
| `build_workflow_index.py --check` | PASS (78 methods) |
| `git diff --check` (base `974bf7da4`) | PASS |
| `exports/chirality-app/export_public.py`, run twice | No tracked change; staging removed |
| `build_amendment_preview.py --check` (clean environment) | OK before the candidate was written |
| `group3_finalize.py --check` | OK |

The commit that adds this table changes only `RUN_SUMMARY.md`.

## Evidence basis

| Artifact | SHA-256 |
|---|---|
| `Supersession_Map.csv` | `83e5e25fec5dbedee83d184d4b831082169d5a7c46346cd7f3f3a18e45c73eaf` |
| `Post_Change_Coverage.json` | `87821e42e68b5d51b189c21038bb8a460de1296aa63f4484416357fd129e966f` |
| `Handoff_State.md` | `c8f70d678c455f0a6b1e078af5e2ffbf60136e9b4e04f73ed53fa1879e18e51b` |
| `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` | `f443daf776c9d61567b9a8f714655770bae4a2b19cade2f6267bda7620401608` |
| `Evidence/Group3/CANDIDATE_VALIDATION.md` | `0964678b521c9341039ddb9d11e0b90bcd8ffc6b8159dc42ea47eec01c81f927` |
| `Evidence/Group3/validate_candidate.py` | `cd6666281f9c412ebcf4c969e7fe384ce25cd38a35319c1284c9a7bdc8c18a67` |
| `Evidence/Group3/build_post_change_coverage.py` | `c4ee92ad2da7d18a79893e506d3c13f57885a62ace5206c001e9b270cf1943f9` |
| `Evidence/Group3/PRE_CHANGE_REFRESH.json` | `220ecfbaf56cf2f99c27503c86b8207db367264e8d4696caddd2b41cd7d83e91` |
| `Evidence/Group3/PRE_POST_COMPARISON.md` | `ef61cd030aa1b68f62bbd5f7cededfca1f454174fb477ac2c148f3823572d4a1` |
| `Evidence/Group3/Supersession_Findings.csv` | `d288096f20845863777a4b5d0956be5c7783577857e3148e6d174200b74eb8b4` |
| `Evidence/Group3/group3_finalize.py` | `6e519e52b978a8d1388969a908a782ffa7f7bb32fe83b426ae625cc8fa24c412` |
| `Evidence/Group3/check_group3_finalize.py` | `5258b204f68af90965c3f4263c5d6982decbbea4d616f48d22976d5c767e2632` |
| `Evidence/Group3/LATEST_POSTIMAGE.md` | `dc893e66b594446f5099848dad09cc79866e2e5b1f934bc50883bc0e0af2803d` |
| `Evidence/Group3/STATUS_RECORDS_POSTIMAGE.md` | `1807f8d19f3a0381c64115f2940e23b0651ecd491baeea46e457f0d2efb3e59c` |
| `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md` | `ea902c05b03f8b4ea273d951d487fa1e09b6fc6938b79eaef28436ef3dbd8f29` |
