# Step 0 — Discovery (recorded before any product edit)

Run: `APPDEV_V3_NODE_H_2026-09-03` · Implementer: Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · Date: 2026-09-03

## 1. Git state, basis, validators

| Check | Command (cwd) | Result |
|---|---|---|
| Worktree creation | `git -C $REPO fetch origin && git -C $REPO worktree add <scratch>/wt-nodeH -b codex/app-v3-nodeH-section8-preservation-2026-09-03 origin/main` | branch created; HEAD `e59efa4830fb54143c86e511ec35a6d1a476f72e` = PR #686 merge |
| Basis | `git merge-base --is-ancestor e59efa483 HEAD` (REPO_ROOT) | true — basis is exactly `e59efa483` |
| Git status | `git status --porcelain` (REPO_ROOT) | empty (clean) |
| Receipts validator | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` (REPO_ROOT) | `VALID … frozen through Receipt-52; versioned receipt contract satisfied`, exit 0 |
| Authority corpus (D-APP-38) | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` (WORKING_ROOT) | `corpus current_version: v20`, all eight `[MATCH]`, `no drift.`, exit 0 |
| Pinned completion reference | `shasum -a 256 plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (REPO_ROOT) | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` — matches the workplan pin |
| Standing plan | `git ls-tree HEAD projects/chirality-app-dev/loop/` → `WORKPLAN_2026-09-03_app_dev_loop.md` (bytewise last, mode 100644 blob); read with `git show HEAD:` | selected; Step 0 / selectability rule quoted in §4 |
| Newest receipt | `loop/LOOP_RECEIPTS.md` | Receipt 212 (node A; `Examined-Through 0c683fb16…`, Parent Receipt-205, Gate-Outcome `EXECUTED — awaiting owner merge`); PR #686 has since merged at `e59efa483` |
| Harness self-check | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` (REPO_ROOT) | exit 0; pre-existing repo-wide findings only (INFO 14, REVIEW 4, WARN 43) |
| Routed Root notices | `ls execution/_Coordination/NOTICE_*` | newest `NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`; none bears on DEL-09-01-V3-01, whose named act is an App merge, not a Root acceptance |
| Toolchain | `node --version` / `npm --version` (FRONTEND) | v24.18.0 / 11.16.0 |
| Dependencies | `npm ci` (FRONTEND); `npm ci && npm run build` (runtime) | both exit 0; no lockfile edit; outputs gitignored |

## 2. APP-HOLD-1 dispatch preflight

Command (WORKING_ROOT):
`python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-09-01`

Result: `"verdict": "ALLOW"`; `DEL-09-01` `contract_status: CLEAR`, `hold_status: NOT_HELD`, `verdict: ALLOW`; `active_hold_deliverables: []`; `register_sha256 e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; `scan_fingerprint_sha256 a9bfb75515b8c4ced2707b38b5b31e1f9b6c272f5262ceea3064f7196bd75b9b`; `repo_head e59efa4830fb54143c86e511ec35a6d1a476f72e`; exit 0. Register-match scan (`app_hold.py scan --require-register-match`): 53 contracts, held_count 0, exit 0.

## 3. A1 re-stage declaration (mandatory — this tranche mutates `frontend/`)

Quoted verbatim from `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` lines 28–36:

> ```
>   Recorded form: G0.25 is PASSED and WP-00 is closed. The standing
>   frontend-freeze guard from G0 C2 is replaced by the recorded re-stage rule:
>   any mutation under `projects/chirality-app-dev/frontend/` invalidates the
>   staged procedure for any future proof claim and requires a newly staged
>   revision and a fresh owner-executed proof. This ruling makes no signing,
>   notarization, DMG, deployment, distribution, publication,
>   release-readiness, or acceptance claim beyond the login-session proof
>   itself; DEL-09-04's remaining scope stays `IN_PROGRESS` and separately
>   gated.
> ```

Declaration: this tranche's method writes the stable premerge artifact `frontend/artifacts/harness/section8/latest/summary.json` (and its Section 9 / release-quality siblings) inside `projects/chirality-app-dev/frontend/` — those paths are gitignored (`frontend/.gitignore` lines 18–20; root `.gitignore` `**/frontend/artifacts/`) so they never enter the commit, but a mutation under `frontend/` is a mutation under the rule regardless of tracking. Any change to `frontend/scripts/validate-harness-*.mjs`, Section 8 fixtures, or tests is likewise declared here if it occurs (see RETURN.md §2 for the exact touched set). Under the A1 re-stage rule this **invalidates the staged R20 procedure for any future proof claim** and **requires a newly staged revision and a fresh owner-executed proof** before any such claim is made. The R20 PASS of 2026-08-23 is unaffected as historical evidence of the bytes it was executed against.

## 4. Selectability re-derivation (live tree, not the brief)

Seated item text on `main` at basis (`DEL-09-01/_STATUS.md` `## Remaining`, verbatim tag):

> `NOT_SELECTABLE_UNTIL: the first v3 product change merges on a sibling carrier (any of DEL-02-05-V3-01, DEL-04-05-V3-01, DEL-09-06-V3-01)`

Named condition, checked on `main`: PR #686 (`codex/app-v3-nodeA-credential-ipc-2026-09-03`) merged as `e59efa4830fb54143c86e511ec35a6d1a476f72e`, landing DEL-09-06-V3-01, DEL-04-05-V3-01, and DEL-02-05-V3-01 (Receipt 212; each carrier's `_STATUS.md` History line 2026-09-03 on `main`). All three sibling carriers — not merely one — have merged.

Governing rule (`WORKPLAN_2026-09-03_app_dev_loop.md`, committed `HEAD` bytes, Step 1, verbatim):

> A `Remaining` item is *selectable* when it carries no `(gated: ...)` / `(stage-gated: ...)` suffix and no `NOT_SELECTABLE_UNTIL:` state, or its named gate is ruled or its named act has occurred on `main` *(A12)*; […] an item whose gate is a Root acceptance, a Root implementation act, a held DEL-02-06 binding, an owner act, or a release act stays parked until that gate or act is observable on `main` (a routed Root notice, a ruling record, or a merged act).

and (non-negotiable 3): *"Gate state is register-derived — open `D-APP-XX` rows, per-item `(gated: ...)` suffixes, and per-item `NOT_SELECTABLE_UNTIL: <gate or act>` states in `Remaining` sections are re-derived each iteration, never assumed."*

Finding: selectability under this rule is a **derived state** — the item is selectable the moment its named act is observable on `main` as a merged act, which it is (`e59efa483`). The rule does not reserve the textual tag update to a seating or owner act; the owner's act was the merge of PR #686, and the plan's Step 5 already makes `_STATUS.md` `Remaining` upkeep (reflecting what landed) a closeout write of the executing tranche. The A12 note *"Merge of the seating candidate confers selectability only"* concerns what the seating merge confers, not who may record a later condition's satisfaction. Therefore the dispatched implementer may record the flip. Rejected alternative: treat the tag text as owner-owned and stop with `BLOCKED_SELECTABILITY` — rejected because it would convert a re-derivable fact into an owner act the plan does not name, contrary to the D-APP-64 asymmetry (over-slating costs owner attention where no boundary is touched).

Action taken (first and only `_STATUS.md` edit before closeout): the tag was replaced by `SELECTABLE` plus the one-line note "condition met by PR #686 / e59efa483 / Receipt-212". Nothing else in `_STATUS.md` changes until `REVIEW_PASS`.

Dependencies: `Depends: A merged v3 product change on a sibling carrier; DEP-09-01-005/008/010` — DEP-09-01-005 (required local checks, EXTERNAL constraint) and DEP-09-01-008 (`HARNESS_BASE_URL` reachable server, EXTERNAL prerequisite) are satisfied procedurally by this run's method; DEP-09-01-010 (CI upload handoff owned by DEL-09-05) is `SATISFIED` in `Dependencies.csv`. Accepted DepClosure snapshot: `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z` (`_LATEST.md`); no newer closure. No `(gated: …)` suffix on the item.

## 5. Write locus and method decision

Write locus (seated): `frontend/scripts/validate-harness-*.mjs`, Section 8 fixtures, `frontend/artifacts/harness/section8/**` evidence, and deliverable-local state; the brief adds DEL-09-01 `Evidence/**`, `_run_records/**`, this run record, and the receipts ledger (append, closeout).

Live-tree facts that shape the method:

- `frontend/artifacts/**` is gitignored at both levels (above), so durable evidence bytes must be copied into DEL-09-01 `Evidence/**`; the stable artifact path is still exercised and verified in place.
- The local premerge failure class recorded by Receipts 172/177 and by nodes A/B (`HTTP 503` on every session route, `HARNESS_PREMERGE_TEST_COUNT=0`) is exactly the absence of the shared-runtime binding lifecycle that `.github/workflows/harness-premerge.yml` performs before the wrapper: start `dist-electron/main.js --runtime-daemon` under a disposable `--user-data-dir`, register `chirality.project.json` through `dist-runtime/chirality-cli.mjs project register`, then start `next dev` with `CHIRALITY_RUNTIME_{TOKEN_FILE,PROJECT_ID,PROJECT_ROOT}` and `HARNESS_PROJECT_ROOT` bound. `src/lib/runtime-client/daemon-harness-port.ts` returns `ENGINE_UNAVAILABLE 503` when those variables are unset — the observed class.
- The unpackaged daemon (`app.isPackaged === false`) resolves its instruction root from the process, installs no LaunchAgent, and derives socket/token paths from `userData` (`electron/runtime-host.ts` `startRuntimeHost`, `electron/main.ts` `runtimeControlPaths`), so a scratch `--user-data-dir` isolates it from the operator's real daemon.

Decision: reproduce the CI lifecycle locally on macOS (no xvfb needed) against a disposable user-data root under the scratch directory, run `npm run harness:validate:premerge` (the deliverable's core evidence) and `npm run validate:release-quality`, retain the bytes, and prove cleanup. Produce the evidence without changing any `validate-harness-*.mjs` script; only if a script defect blocks the run is a minimal test-backed change made. Corroborate with the CI-produced `harness-validation-summaries` artifacts from the pre-landing (PR #681) and post-landing (PR #686) workflow runs, and with a local run of the identical method at the pre-landing basis `0c683fb16` in a second scratch worktree so the "unchanged behaviour" claim is an A/B over recomputable bytes rather than a prose assertion.
