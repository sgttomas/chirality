---
amendment_id: SCA-APP-011
doc_kind: scope_change.run_summary
decomp_variant: SOFTWARE
checkpoint_group: 3
status: CANDIDATE_ready_for_owner_group3_decision
created: 2026-09-27
branch: claude/brave-goodall-wj3hok
integrated_scope_and_code_commit: 3f75abfab
accepted_group2_snapshot: execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/
pointer_posture: ACCEPTED_PREDECESSOR (SCA-APP-010)
---

# SCA-APP-011 — Checkpoint group 3: audited poststate (CANDIDATE)

> **Status: CANDIDATE, ready for your group-3 decision.** The scope text and
> the code change are integrated on one branch, and the independent review is
> complete with no blocking finding. That review was run by an independent
> instance, which neither authored nor applied the candidate, on HEAD
> `3d8ead912` (Q-a). Its results are in §8. CI on the PR is still to come.
> `_LATEST.md` still names SCA-APP-010. Nothing is merged.

---

## Checkpoint group 3 — what you will be asked to decide

### What accepting group 3 authorizes

In this order, exactly as listed in `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`:

1. **Decision folder.** `checkpoint_snapshots/SCA-APP-011_GROUP-3_{date}/`,
   recording your act. It is committed first.
2. **E47.** `Evidence/Group3/group3_corrections.py --finalize` sets the
   decomposition's Coverage and Telemetry `Revision` and `Date` to the
   acceptance date. It first rechecks all 16 candidate hashes and changes
   nothing else.
3. **`_LATEST.md`.** It moves from SCA-APP-010 to this snapshot, from the
   prepared `Evidence/Group3/LATEST_POSTIMAGE.md`.
4. **Runtime notice.** The informational notice about the Runtime's scaffold
   API is sent to the Runtime loop.
5. **Status records.** The `Brief.md` status line, the `Decision_Log.md` G3
   row and `Handoff_State.md` are updated, and a post-acceptance validation
   record is written.
6. **Merge.** One PR lands the scope text and the code change together (Q-a),
   once CI and the review have no blocking finding.
7. **Post-acceptance handoffs**, which are not part of the act:
   `project-setup` in `INCREMENTAL` mode; `dependency-extract` then
   `analyze_dep_closure`; `audit-decomp`; and `audit-scope-closure` after the
   setup and the code change.

It authorizes no lifecycle change, dependency-register write or release.

### Two corrections you are asked to accept with group 3

These follow the same "reopen only what is affected" rule used for the M-a
correction at group 2. Details are in `Evidence/Group3/G3_CORRECTIONS.md`.

- **G3C-01, a correction to accepted text.** The DEL-07-04 Scope of Work
  (line 24, accepted edit E13) said each ported HTTP expectation is restated
  as the library's `WorkspaceValidationError` code and status. The code
  throws `WorkspaceOperationError` for most refusals (gates, rulings,
  amendments, dependency writes) and `WorkspaceValidationError` only for path
  validation. The candidate now says "the thrown workspace error's code and
  status (`WorkspaceOperationError` for most refusals,
  `WorkspaceValidationError` for path validation)". Nothing else in the
  hook, or in any other file, changes. I scanned the other 15 files and every
  path and identifier in the accepted text against the code; nothing else is
  contradicted.

  Accepting group 3 reopens and replaces that one sentence of E13. If you
  returned G3C-01 alone, the accepted group-2 sentence would stand, and the
  text would stay untrue about the code. So G3C-01 comes to you as part of
  group 3: you accept, amend or return group 3 as a whole.
- **G3B-01, a basis refresh (no text change).** Main changed one App SPEC
  paragraph on the recorded-register read (Receipt-270) after group 2. The
  change is outside every SCA-APP-011 edit. The accepted SPEC edits reapply
  unchanged; only the SPEC file's hashes move.

### What changed

**Scope text** (commits `94befbf6c` and `3f75abfab`):
- 126 of the 127 accepted edits are written, in 16 files: the decomposition,
  the PRD, SPEC and PLAN, nine Scopes of Work and three `_CONTEXT.md` files.
- E47 is withheld.
- G3C-01 is applied, and G3B-01 is accounted for.

**Code** (commits `5ba17042b` and `653fdfb72`, App loop):

| Change | Files (under `frontend/src/`) |
|---|---|
| Forms removed | `components/workbench/workbench-surface.tsx`, `components/pipeline/pipeline-surface.tsx`, `components/pipeline/lifecycle-gate-fields.tsx` and their three tests; form-only CSS in `app/globals.css`; the two tabs in `components/shell/tertiary-sidebar-tabs.tsx` |
| Deliverable routes removed | `app/api/working-root/deliverable/status/route.ts`, `…/status/transition/route.ts`, `…/dependencies/route.ts` (`…/content/route.ts` stays) |
| Client module removed | `lib/workspace/deliverable-api.ts` and `__tests__/lib/workspace-deliverable-api.test.ts` |
| Scaffold route removed | `app/api/harness/scaffold/route.ts` and its test; `scaffoldHarnessExecutionRoot` in `lib/harness/client.ts` |
| App scaffold proxy removed | `scaffold` on `DaemonHarnessPort` and `RuntimeDaemonHarnessPort`, their test stubs |
| Route test split | `__tests__/lib/deliverable-contracts.test.ts` (new) and `__tests__/api/working-root/deliverable-content-route.test.ts` (renamed remainder) |
| Kept | the content route, `deliverable-contracts.ts`, `lib/lifecycle`, `lib/dependencies`, the scaffold library, `lib/harness/mcp`, `task-scope.ts`, `pipeline-dispatch-contract.ts`, the loop-first shell, the `/workbench` and `/pipeline` URLs |

Across 27 frontend files, 486 lines were added and 5,366 removed against
main. The records are:
- the run receipt `execution/_Coordination/AgentRuns/APP-REMOVE-LEGACY-FORMS-2026-09-27/RECEIPT.md`;
- Receipt-269;
- the tranche manifest;
- MEMORY rows for the nine deliverables;
- `RouteAdapterTestIndex.md`, which drops its two scaffold rows.

The export is regenerated in the last commit.

**Test port.** The port yields 55 library tests and 10 content-route tests.
The old route test had 57 executed status, transition and dependency tests.
Only two `it.each` rows were dropped:
- `{ ruling: 42 }` and `{ amendment: 7 }`, both of which expected
  `INVALID_REQUEST`;
- they test request-body parsing, and the library's `string` typing rejects
  them at compile time.

Every other case keeps its name, fixtures and assertions.

**The ported tests really exercise the gates.** The code agent broke each
gate temporarily and reran the library test:

| Gate broken | Failures |
|---|---|
| The ruling requirement | 1 |
| Ruling containment | 4 |
| An agent actor allowed to reverse | 1 |
| The amendment check on reopening | 9 |

Every file was restored afterwards.

### Checks

| Check | Result |
|---|---|
| Candidate hashes | 16/16 match their expected group-3 hash: 14 at the group-2 hash, 1 basis refresh re-derived from `4087a4f8c`, 1 correction |
| Edits present | 126/126; E47 withheld; no `{APPLICATION_DATE}` literal |
| Write containment (`e7f6daee1..3f75abfab`) | 74 paths. Scope text is exactly the 16 accepted files. The other 58 fall in §4's code-change categories or the SCA folder. No `_STATUS.md`, `Dependencies.csv`, `_LATEST.md` or companion-register change |
| Scope of Work validator; retired-route sweep | 9/9 pass; 108 contracts and contexts, 0 uncovered lines |
| Topology, coverage, lifecycle, closure | Unchanged from the pre-change baseline: 10/52/84/10; 53 `IN_PROGRESS`, 1 `OPEN`; 54 nodes, 111 edges, 0 SCCs; `EVQ-006` ×592 only. No code reference to the retired routes, client function or forms remains |
| Supersession map | 63 rows, 0 findings |
| Group-3 finalize path | 15/15 on a scratch copy (`Evidence/Group3/check_group3_finalize.py`) |
| TypeScript | `npm run typecheck`: 0 (independent review) |
| Ported tests | 65/65 (55 library, 10 content route) |
| Focused Vitest | The reviewer's focused set: 12 files, 465/465 |
| Full Vitest | Only the known uid-0 `harness-attachment-resolver` failure |
| Root validators | G0–G4, receipts, agent instructions, workflow metadata, instruction entrypoints, conflict markers, run-record leaks, workflow index, affected tests and `git diff --check`: all 0 (§8) |
| `AuditState` (raw) / `AdjustedAuditState` | `WARNINGS` / `WARNINGS`. Every tool finding was present before the change; there are 0 new findings |

### Still to come

- CI on the PR. It runs when the PR is opened, and it is a merge gate after
  your acceptance.

---

## 1. Amendment

SCA-APP-011 retires the following:
- the obsolete Workbench and Pipeline forms and their tests;
- the deliverable status, status-transition and dependency HTTP routes, with
  their client fetch functions;
- `POST /api/harness/scaffold`, with its client function and App port member.

It also rescopes DEL-02-02. It names the lifecycle, dependency and scaffold
libraries as the interfaces. The owner accepted group 1 and group 2 on
2026-09-27.

**Commit identities.** The owner reviewed the group-2 package at `b0295688c`.
It now sits on this branch as `524151c9c`, cherry-picked with identical
content. The group-2 snapshot, candidate text and evidence commits are
`e7f6daee1`, `94befbf6c` and `1cb9ecc56`; they were `ad38c93c6`, `5ca09e2e6`
and `fc875d873` before the move.

## 2. Actions taken (group-3 preparation)

| Step (method.md) | Action | Evidence |
|---|---|---|
| Consume group 2 | `SCA-APP-011_GROUP-2_AUTHORIZED.md` resolved; the manifest's 12 hashes verified | `checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/ACCEPTED_MANIFEST.csv` |
| Pointer posture | `ACCEPTED_PREDECESSOR`; `_LATEST.md` (`6fdba0c9…42c04e3`) unchanged | `Handoff_State.md` |
| 1–2. Apply | `build_amendment_preview.py --candidate` wrote 126 edits (commit `94befbf6c`); G3C-01 applied with `group3_corrections.py --apply` (commit `3f75abfab`) | `Evidence/Group3/G3_CORRECTIONS.md` |
| Code change | App loop, `Propagation_Plan.md` §4 (commits `5ba17042b`, `653fdfb72`); code-side records now bind the group-2 snapshot | run receipt, Receipt-269, tranche manifest |
| 5. Supersession | `accumulate_supersession_map.py` over the SCA-APP-010 map and the delta: 63 rows, 0 findings; LF line endings, `--check-map` clean | `Supersession_Map.csv`, `Evidence/Group3/Supersession_Findings.csv` |
| 5. Post-change baseline | The accepted group-1 builder rerun on the integrated tree at `3f75abfab` | `Post_Change_Coverage.json`, `Evidence/Group3/PRE_POST_COMPARISON.md` |
| 5. Validation | `validate_candidate.py --accepted-commit e7f6daee1 --head 3f75abfab`: PASS | `Evidence/Group3/CANDIDATE_VALIDATION.md` |
| Acceptance-conditional list | Six items, exact | `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`, `Evidence/Group3/LATEST_POSTIMAGE.md` |

**Disclosure.** A full `audit-decomp` TASK run was not dispatched from this
bounded session. The post-change baseline reruns the same registered tools as
the accepted pre-change baseline (`Propagation_Plan.md` §6 step 6). A full
`audit-decomp` is a post-acceptance handoff.

**Disclosed deviations from §4** (records only; see `G3_CORRECTIONS.md`):
- §4's line numbers are against the basis, and the ported route test is the
  version after Receipt-270;
- `loop/LOOP_RECEIPTS.md` also conflicted in the rebase. Receipt-269 sits
  before 270 with parent 268;
- the two `RouteAdapterTestIndex.md` rows were dropped (the preview's option);
- DEP-07-05-025 in `DEL-07-05/Dependencies.csv` still names the dependency
  route, which the §8 `dependency-extract` handoff owns.

## 3. Pre-change vs post-change

The full comparison is in `Evidence/Group3/PRE_POST_COMPARISON.md`. Every field
is equal, except two that differ as intended:
- `decomposition_sha256`, which moves to `dc131463…`;
- `affected_lifecycle`, which gains the DEL-07-01 key (`IN_PROGRESS`).

The scaffold-route references in the frontend are now none, where before they
were the Pipeline form, the client and their tests.

- **Coverage.** There is no coverage regression, no new orphan and no
  parent-partition change.
- **SOFTWARE design rules.** These were checked explicitly. Package flatness
  and the Scope Ledger (84 rows, 78/5/1) are unchanged, as are the envelopes
  (L 2, M 41, S 9). DEL-02-02 keeps its ID, name, type and envelope.
- **IDs and change record.** Stable IDs are preserved, and no retired ID is
  reused. DEC-026 and the Change Log line are present.

## 4. Finding classification

| # | Finding | Source | Pre | Post | Class |
|---|---|---|---|---|---|
| F1 | `EVQ-006` ×592 (deliverable-relative `EvidenceFile` paths) | `validate_decomposition_registers.py` | 592 | 592 | Carried, pre-existing |
| F2 | "partition directory contract is incomplete" | `audit_structure.py` | yes | yes | Carried, pre-existing |
| F3 | "required tool roots are missing" | `audit_structure.py` | yes | yes | Carried, pre-existing |
| F4 | Closure `subject_status` FAIL (2 schema-invalid registers, 2 units without a node) | `analyze_dep_closure.py` | yes | yes | Carried, pre-existing |
| X2 | DEP-02-02-005..009 and DEP-07-05-025 still name the retired forms or route | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: group 2, `Propagation_Plan.md` §8 item 2 |
| X3 | Coverage and Telemetry still reads "amended by SCA-APP-010 / 2026-09-04" | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: group 2, §6 (E47) |
| X6 | Task Management APP-R058 open; `_LATEST.md` on SCA-APP-010 | candidate review | — | yes | `EXPECTED_CONSEQUENCE`: group 2, §8 item 6; the method.md pointer rule |

Three earlier expected consequences are now resolved by the integrated code
change:
- X1: the code still carried the retired items;
- X4: `RouteAdapterTestIndex.md` still listed the scaffold route;
- X5: the `dcd37f9ae` records said the routes were kept.

The export, which was X6's other part, is regenerated in the last commit.

- **Raw `AuditState`:** `WARNINGS`.
- **`AdjustedAuditState`:** `WARNINGS` (F1–F4, carried).
- **New findings:** 0.

## 5. Acceptance-conditional edits (exact list)

See `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`. None is applied
before acceptance, and any edit not on the list returns to the owner.

1. **Decision folder.** Write `checkpoint_snapshots/SCA-APP-011_GROUP-3_{date}/`
   (`DECISION.md` headed `# SCA-APP-011 checkpoint group 3 — accepted …`) and
   commit it first.
2. **E47.** Run
   `group3_corrections.py --finalize --date {date} --group3-decision …/SCA-APP-011_GROUP-3_{date}/DECISION.md`.
   Do not use the group-2 `--finalize`, which refuses the two G3 files.
3. **`_LATEST.md`.** Replace it with `LATEST_POSTIMAGE.md` (`03fb208d…786ba0`),
   with both `{APPLICATION_DATE}` occurrences set to `{date}`. The before hash
   is `6fdba0c9…42c04e3`.
4. **Runtime notice.** Write `Evidence/Group3/RUNTIME_NOTICE_POSTIMAGE.md`,
   with both `{APPLICATION_DATE}` occurrences set to `{date}`, to
   `projects/chirality-runtime/execution/_Coordination/NOTICE_{date}_APP_SCA-APP-011_SCAFFOLD_API.md`.
   It is the draft notice without the "DRAFT — " title prefix and without the
   draft Status paragraph (draft lines 3–6). The `**From:**` line stays, and
   its parenthetical names the acceptance date and decision folder.
5. **Status records.** Apply the exact post-images in
   `Evidence/Group3/STATUS_RECORDS_POSTIMAGE.md`: the `Brief.md` status line,
   the `Decision_Log.md` G3 row, and `Handoff_State.md`, which is replaced by
   `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md`. The slots are
   `{APPLICATION_DATE}`, `{OWNER_ACT_VERBATIM}` and `{UTC}`, and the
   post-images apply to a plain acceptance only.
6. **Post-acceptance record.** Write `_PostAcceptanceValidation/SCA-APP-011_{UTC}/`.

## 6. Recommended downstream reruns (not executed)

1. **`project-setup` in `INCREMENTAL` mode.** It scaffolds nothing; the
   contracts are already written (W-a).
2. **`dependency-extract`** for DEL-02-02, DEL-02-01, DEL-02-03, DEL-07-04,
   DEL-07-05, DEL-08-02 and DEL-08-03, then `analyze_dep_closure.py`.
3. **`audit-decomp`** (full), then **`audit-scope-closure`**.
4. **Task Management APP-R058** disposition, by the row owner.

## 7. Handoff state

See `Handoff_State.md`.

| Field | Value |
|---|---|
| `DecompositionTruthState` | `INCOMPLETE` (E47 pending) |
| `DerivativePackageState` | `INCOMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `WARNINGS` |
| `AdjustedAuditState` | `WARNINGS` |
| `ReadyForNextPhase` | `NOT_APPLICABLE` |

**Closure verdict:** `OPEN_PENDING_DERIVATIVE_CLOSURE`.

## 8. Repository-change evidence

Branch `claude/brave-goodall-wj3hok`, on `origin/main` `4087a4f8c`:

| Commits | Content |
|---|---|
| `a11b81e93` … `524151c9c` | Group-1 and group-2 packages and acceptances |
| `e7f6daee1` | Group-2 snapshot |
| `94befbf6c`, `1cb9ecc56` | Candidate text and evidence |
| `5ba17042b`, `653fdfb72` | Code |
| `3f75abfab` | G3C-01, G3B-01, the group-3 finalize path and code-record binding |
| `9884008cb`, `3d8ead912` | Integrated evidence and presentation; the regenerated export |

After `3d8ead912`, one commit applies the review's non-blocking items. It adds
the post-acceptance templates, corrects counts and wording, and adds these
results. It changes no scope file and no code. If the export changes, it is
regenerated in a final commit.

### Independent review results (HEAD `3d8ead912`)

The reviewer was an independent instance that neither authored nor applied
the candidate. It found no blocking findings. Exit codes:

| Check | Result |
|---|---|
| `validate_candidate.py` | 0; byte-identical on rerun |
| `group3_corrections.py --check` | 0 |
| `check_group3_finalize.py` | 0 (15/15) |
| Supersession `accumulate_supersession_map.py --check-map` | 0 |
| Post-change coverage (`build_post_change_coverage.py`) | 0 |
| `npm run typecheck` | 0 |
| Ported tests | 65/65 |
| Focused Vitest (the reviewer's set) | 12 files, 465/465 |
| Full Vitest | Only the known uid-0 `harness-attachment-resolver` failure |
| `validate_app_dev_loop_receipts.py`, `validate_agent_instructions.py`, `validate_workflow_metadata.py` (70), `validate_instruction_entrypoints.py` | 0 |
| G0, G1, G2, G3 | 0 |
| `validate_conflict_markers.py` and `validate_run_record_leaks.py` against `origin/main` | 0 |
| `build_workflow_index.py --check` | 0 |
| G4 (`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`) | 0 |
| `tools/run_affected_tests.py --base origin/main` | 0 (1147 passed) |
| `git diff --check` | 0 |
| Export freshness | No diff |

The reviewer's own gate mutations each failed the ported tests as expected:

| Gate broken | Failures |
|---|---|
| Ruling requirement | 1 |
| Amendment-admission refusal | 9 |
| Missing-amendment backward gate | 2 |

**Still to come:** CI on the PR.

## Evidence basis

| Artifact | SHA-256 |
|---|---|
| `Supersession_Map.csv` | `9847a4d0d05b65bfbf8d431ba0fb3c24662d73c2574f186e7c259413aa6e65d6` |
| `Post_Change_Coverage.json` | `f62b84a38cc633f6c8f475f92f3025b65b189393ef93f1b0d8a643746feb2f81` |
| `Handoff_State.md` | `f38531ef3e6c5f81388231b470e242c6116389634638f8b039b11871393c8d68` |
| `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` | `2f09fd51b65cd6d03c9e55dd3936728652bed996d2e86f3ef3f755a423ad5e4b` |
| `Evidence/Group3/CANDIDATE_VALIDATION.md` | `7821a03e8618ce27369abaad953422383313cd161c80dbfa93f37f78dd1b7dcd` |
| `Evidence/Group3/G3_CORRECTIONS.md` | `e42342d593efc22d48fd62467a6c5fd31e2fbb2c349ccd83715e26bc8dd9f7e5` |
| `Evidence/Group3/group3_corrections.py` | `ecd97bfba72aa70e189ec9af48674068980246cd8835ccc155055619a25b4071` |
| `Evidence/Group3/check_group3_finalize.py` | `034819f64efe018cfc66c65489100aa658261bea92af27ed3f99836e17155d02` |
| `Evidence/Group3/LATEST_POSTIMAGE.md` | `03fb208dbf0fac87e66c30fab9ca848bd2795f41c2152188528d5c9fca786ba0` |
| `Evidence/Group3/PRE_POST_COMPARISON.md` | `c430a3c2a00730a6d61907b359fbc4ca7879cef7037b0e280771628747276702` |
| `Evidence/Group3/Supersession_Findings.csv` | `d288096f20845863777a4b5d0956be5c7783577857e3148e6d174200b74eb8b4` |
| `Evidence/Group3/build_post_change_coverage.py` | `e96a59f7502df3ee52bb472ad8e3849133b53b5a4f68fe7544c35837fc308ff8` |
| `Evidence/Group3/validate_candidate.py` | `1cbbad7fc2f60b6ca96d39143991af4726347a5790d29694e3df2be43d5297a6` |
| `Evidence/Group3/RUNTIME_NOTICE_POSTIMAGE.md` | `53d7deee8e8e1e2a99c74570f115422b95fdc8649d37199dc494c03fca10b118` |
| `Evidence/Group3/STATUS_RECORDS_POSTIMAGE.md` | `c9771459d8ca9c99e6c5c041fbdb77014670f1f8d0a58cf4c96d5cb6e569d981` |
| `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md` | `83b69791cc11139413776b5806185ff8864dd253cf8ba3c19a7bb1c30272772c` |
