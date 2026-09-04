# RETURN — H1_IMPLEMENTER (closed out after REVIEW_PASS; three local commits)

- **Run:** `APPDEV_V3_NODE_H_2026-09-03` · **Executor:** Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · **Skill method:** `software-bounded-implementation`
- **Basis:** `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge; exactly the required basis) · **Branch:** `codex/app-v3-nodeH-section8-preservation-2026-09-03`
- **Commits:** round 1 `021e1f1863670f30cf81df909a417bf550cbc370` (125 files, +5,720 −1; reviewed: `instances/H2_REVIEWER/REVIEW_01_2026-09-03_over_021e1f186.md`, FAIL on one MAJOR H1-F1, zero BLOCKER); round 2 `da3ceb310ebf4bcf4cc51f3e493467c45bfd201f` (review-1 remediation under coordinator decision D1; reviewed: `instances/H2_REVIEWER/REVIEW_02_2026-09-03_over_da3ceb310.md`, **PASS**, 0/0/0, five NOTEs); rebased for publication onto `origin/main` `1d9b37970` (PR #689 merge) as `faf5005aa` + `efad64029` with no conflict; round 3 = the closeout commit containing this file (coordinator decision D2).
- **Item:** DEL-09-01-V3-01 (`SELECTABLE` after the Step 0 flip; revised, not removed, at closeout)
- **Status:** `REVIEW_PASS` received on `da3ceb310`; closed out under D2. Every registered check passes — including the premerge, which this tranche runs daemon-bound and does **not** defer to PR CI. Review-1 findings applied: H1-F1 (MAJOR), F2, F3 (MINOR), F4, F5, F6, F7, F8, F10, F12 (NOTE); H1-F9 carried to closeout; H1-F11/F13 needed no change. Nothing pushed; no `_STATUS.md` History line, receipt, `HANDOFF_STATE.md`, or `MANIFEST.sha256` for this run record written yet (those follow `REVIEW_PASS`).

## 1. Behavioural summary

**No product source changed.** `frontend/scripts/validate-harness-*.mjs`, the Section 8 fixtures (`src/__tests__/scripts/validate-harness-*.test.ts`), `.github/workflows/harness-premerge.yml`, `runtime/**`, `package.json`, and the lockfiles are byte-identical to the basis; `EVALUATOR_BYTES.tsv` additionally proves those evaluator bytes are unchanged across the four landings PRs 683–686 (only `package.json` changed on `main`, by three unrelated node-B script entries).

**What was produced (DEL-09-01 `Evidence/Node_H_Section8_Preservation_2026-09-03/`):**

1. **Stable premerge summary bytes at HEAD, from a daemon-bound run.** `rerun-section8-local.sh` reproduces `.github/workflows/harness-premerge.yml` step for step on macOS (build the runtime host + CLI; start `dist-electron/main.js --runtime-daemon` under a disposable `--user-data-dir`; register `chirality.project.json` through `dist-runtime/chirality-cli.mjs`; start `next dev` bound through `CHIRALITY_RUNTIME_*`; run the wrapper). Result at `e59efa483`: `HARNESS_PREMERGE_STATUS=pass`, `TEST_COUNT=8`, Section 9 16/16 report-only; `npm run validate:release-quality` on the same daemon `pass` (full Vitest 1489/1489, typecheck, Section 9, premerge; summary consistency pass). The stable artifact `frontend/artifacts/harness/section8/latest/summary.json` was written and is retained as `run-head-e59efa483/artifacts/stable/section8-latest-summary.json` (`386a0f18…`) together with the whole Section 8 run tree (API captures, SSE captures, per-check logs, session cleanup), wrapper stdout/stderr, machine lines, environment, built-bundle hashes, containment observations, and teardown and cleanup proof. Manifests: each run folder's `MANIFEST.sha256` pins `artifacts/**` and `logs/**` and is itself pinned by the bundle `MANIFEST.sha256`. Round-1 defect (H1-F1): the script wrote the per-run manifest before its EXIT-trap teardown finished the logs and wrote `teardown.txt`/`cleanup.txt`, so the shipped per-run manifests failed `shasum -c` on three logs; round 2 makes the per-run manifest the last act of teardown, regenerates both retained per-run manifests from the unchanged retained bytes (no rerun of those trees), and adds a premerge-only round-2 run at HEAD (`run-head-e59efa483-round2/`, port 51842) whose script-written manifest verifies.
2. **Preservation proof as an A/B over recomputable bytes.** The identical method at the pre-landing basis `0c683fb16` (second scratch worktree) passes 8/8; `compare-section8-summaries.py` projects each summary onto its behaviour-bearing fields and reports `BEHAVIOUR_PROJECTIONS_EQUAL=true` over HEAD-local, basis-local, and the two CI `harness-validation-summaries` artifacts (PR #681 pre-landing, PR #686 post-landing, both downloaded with `gh run download` and retained under `ci-artifacts/`). `COMPARE_RESULT.txt` holds the full output.
3. **RQG §13 rows this deliverable owns** — `EVIDENCE.md` §6 maps each of the six Shared Runtime Gate bullets to exactly what this bundle contributes (stub-path preservation; one daemon exercised by the CLI and the Desktop-side routes incl. interruption state; 0600 control socket, 0700 runtime dir, no TCP socket on the daemon, project-scoped `WORKING_ROOT_INACCESSIBLE`; app-dev path with stub attribution) and what it does not (Claude/Pi live behaviour, model switching, PEC, export boundary — with owners).
4. **Bounded rerun method** — the script's header documents inputs, outputs, exit status, and the two host facts a rerunner needs; §9 of `EVIDENCE.md` names the next revision trigger.

**Two host findings (recorded, not product changes):**

- The registered local premerge's long-standing `HTTP 503` class (Receipts 172/177; nodes A and B) is exactly the absence of the CI binding lifecycle; performing it removes the class. No `runtime-client` or route behaviour was touched.
- With the lifecycle in place the unsigned development `Electron.app` blocked forever in `safeStorage.isEncryptionAvailable()` on the macOS Keychain (headless daemon, no prompt possible), wedging the daemon on the first `session/create`. Isolated by `probe/safe-storage-probe.js`: hangs in-sandbox **and** under a sandbox-escalated run (so it is not a sandbox restriction), returns in 1 ms with Chromium's `--use-mock-keychain`. The disposable evidence daemon is started with that switch; CI's Linux runner has no real keychain either, so the evidence class is unchanged, and the operator's Keychain is never addressed.

## 2. Files (basis → HEAD)

Round-2 changes since `021e1f186` (all evidence/record; no product source): `rerun-section8-local.sh` (manifest last in teardown; port fail-fast; kills restricted to the started dev server and processes under the disposable root; caller-supplied `USER_DATA` never removed; `checkout_leftovers=` cleanup line; header docs), `compare-section8-summaries.py` (asserts `pass` overall and per row), `COMPARE_RESULT.txt` (regenerated; byte-identical output), `run-head-e59efa483/MANIFEST.sha256` and `run-base-0c683fb16/MANIFEST.sha256` (regenerated from retained bytes), `run-head-e59efa483-round2/**` (new premerge-only run), `probe/RUNNER.md` (new), `EVIDENCE.md` (§2 pointer, §7 manifests/provenance, leftovers, host-identifying strings), bundle `MANIFEST.sha256`, `_run_records/TASK_RUN_2026-09-03_NODE_H.md` (DRAFT banner), `ORCHESTRATION_PLAN.md` ("push"), `COORDINATOR_DECISIONS.md` (D1), `CHECKS.json` (round 2; `--head` form), `instances/H2_REVIEWER/REVIEW_01_2026-09-03_over_021e1f186.md` (verbatim), this file.

Product: none. Tests/fixtures: none.
Evidence/state: DEL-09-01 `_STATUS.md` (one line: the Step 0 selectability flip), `_run_records/TASK_RUN_2026-09-03_NODE_H.md`, `Evidence/Node_H_Section8_Preservation_2026-09-03/{EVIDENCE.md, rerun-section8-local.sh, compare-section8-summaries.py, EVALUATOR_BYTES.tsv, FRONTEND_PATHS_CHANGED_0c683fb16..e59efa483.txt, COMPARE_RESULT.txt, .gitattributes, MANIFEST.sha256, run-head-e59efa483/**, run-base-0c683fb16/**, run-head-e59efa483-round2/**, COMPARE_RESULT_round2.txt, ci-artifacts/{pr681,pr686}/**, probe/** incl. RUNNER.md}`; closeout adds `_STATUS.md` (History line quoting the pre-flip tag; V3-01 revised; V3-02 seeded), `MEMORY.md`, `HANDOFF_STATE.md`, this run record's `MANIFEST.sha256`, `instances/H2_REVIEWER/REVIEW_02_*`, and Receipt 216 in `loop/LOOP_RECEIPTS.md`; this run record (`ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`, `STEP0_DISCOVERY.md`, `COORDINATOR_DECISIONS.md`, `CHECKS.json`, `RETURN.md`, `instances/H1_IMPLEMENTER/LAUNCH_BRIEF.md`).

## 3. Check evidence (full table with commands, cwd, exit codes: `CHECKS.json`)

| Check | Round 1 |
|---|---|
| `npm run typecheck` | pass |
| `npm test` (full Vitest) | pass — 162 files / 1489 tests (4 skipped) |
| `npm run build` | pass |
| premerge (`harness:validate:premerge`, daemon-bound via the rerun script) | **PASS** — `HARNESS_PREMERGE_STATUS=pass`, 8/8, Section 9 16/16 report-only; stable artifact written; not the deferral class |
| `npm run validate:release-quality` (same daemon) | pass — `RELEASE_QUALITY_STATUS=pass`, all four commands and summary consistency pass |
| Section 8 at the pre-landing basis `0c683fb16` + four-way comparator | pass — 8/8; `BEHAVIOUR_PROJECTIONS_EQUAL=true` |
| `git diff --check` | pass (captured `*.sse`/`*.log` evidence bytes retained raw under a folder-local `.gitattributes` exemption; authored files clean) |
| harness `self-check` / pytest | pass / 350 |
| APP-HOLD preflight / scan | ALLOW / PASS |
| corpus status / receipts validator | v20 no drift / VALID |
| `validate_change_scope.py` (exact command in `CHECKS.json`) | PASS, 0 violations |

## 4. Write-scope validation and implementer-latitude decisions

Every changed path is inside the seated locus plus the brief's additions (exact `validate_change_scope.py` invocation in `CHECKS.json`; PASS, `violations: []`). Not touched: `frontend/scripts/**`, `frontend/src/**`, `.github/**`, `runtime/**`, `package.json`/lockfiles, `docs/**`, register, receipts, Root surfaces.

Decisions taken inside the sealed brief (recorded here; none is a coordinator or owner act):

- **Selectability flip** under the committed workplan rule rather than `BLOCKED_SELECTABILITY` — rationale and rejected alternative in `STEP0_DISCOVERY.md` §4.
- **Run the daemon lifecycle instead of deferring the premerge** — the item's core return is the stable summary bytes; deferring would have left the claim unproven locally. The method is CI's own lifecycle; no product change.
- **`--use-mock-keychain` on the disposable daemon** — chosen over (a) an escalated run (proved not to help), (b) a product change to bypass the Keychain (outside locus and unwanted), (c) reporting `HOST_RERUN_REQUIRED` (the rule reserves that for a declined escalation, and no escalation was declined). Consequence stated in `EVIDENCE.md` §8: the real Keychain path of `safeStorage` is not exercised by this evidence — it is not part of Section 8.
- **Round-2 smoke run instead of a full rerun** — the coordinator permitted regenerating manifests from retained bytes; a premerge-only run at HEAD was added anyway because the script's teardown ordering changed and the claim "the rerun method reproduces a verifying manifest" deserved a fresh byte, at ~40 s cost. The round-1 trees are unchanged.
- **Evidence bytes retained raw** with a folder-local `.gitattributes` whitespace exemption for `*.sse`/`*.log`, rather than normalising captured bytes (which would invalidate the per-run manifests). Node A normalised one log and recorded raw/retained hashes; here the retained bytes *are* the raw bytes.
- **CI summaries retained as corroboration only**; the recomputable proof is the local A/B on one host with one evaluator byte set.

## 5. Residual risks and follow-ups (reported, not taken silently)

1. **A1 re-stage rule** applies: the method writes gitignored artifacts under `frontend/` (`STEP0_DISCOVERY.md` §3). No proof claim is carried forward.
2. **`frontend/artifacts/harness/section8/**` is gitignored** at both levels, so the seated write locus names a path that cannot carry committed evidence; the bundle lives under DEL-09-01 `Evidence/**` as the brief anticipates. If the loop wants the stable artifact tracked, that is a `.gitignore` change outside this locus — surfaced, not taken.
3. **`safeStorage` Keychain block in the dev binary** is a host-environment fact any future local daemon-bound evidence run must handle; the script does, and it is worth a line in `docs/BUILD_AND_RELEASE.md` / `docs/RELEASE_QUALITY_RUNBOOK.md` (docs are outside this locus — surfaced for HELP_HUMAN).
4. **Registration attribution** in the disposable daemon registry (`--approved-by claude-fable-5-1-nodeH --approval-reference APPDEV_V3_NODE_H_2026-09-03`) names the run, not an owner; the registry was deleted at teardown and the tracked manifest is unchanged. No project-authority act occurred.
5. **Not proven:** live Anthropic/Pi behaviour, packaged-app behaviour, G5 acceptance — `EVIDENCE.md` §8. Premerge PR CI remains additional evidence and will rerun on the PR.
6. **Scratch baseline worktree** (`<scratch>/wt-base`, detached at `0c683fb16`) is kept until the tranche closes so a reviewer-requested baseline rerun is cheap; it is removed with `wt-nodeH`.
7. Concurrent nodes F, G, I: no shared write path except the append-only receipts ledger; at rebase time Receipts 213 (I), 214 (G), 215 (F) were on `main`, so this node's receipt is 216 (Parent-Receipt Receipt-212).
8. **Review-2 NOTEs carried as residuals** (no reviewed script byte changed after PASS): H2-F1 — teardown signals only direct children of `$NEXT_PID`, so a wedged `next` whose server grandchild survives would outlive teardown (observable as a non-zero `port_<PORT>_listeners_after_stop`); H2-F3 — the port precondition runs after the daemon start, so an occupied port still costs one daemon start/teardown before `exit 72`; H2-F4 — the `pgrep -f -- "--user-data-dir=$USER_DATA"` pattern is unanchored (unreachable with the mktemp default; relevant only to a caller-supplied prefix path). Seeded together as DEL-09-01-V3-02 (`SELECTABLE`, evidence-only, write locus limited to the rerun script and its evidence). H2-F2/F5 narrative clauses applied in the closeout commit.
9. **Revision 2 already owed:** the sibling landings PRs 687–689 (through `1d9b37970`, the publication basis) touched `frontend/electron/renderer-window-policy.ts` (node G) and `src/__tests__/scripts/run-packaged-security-proof.test.ts`, which fall under the trigger surfaces this item names; V3-01 is therefore left `SELECTABLE` with revision 2 owed rather than parked. This closeout does not run it (the reviewed evidence is for `e59efa483`; a revision is one bounded rerun of the same method at the new `main`).

## 6. Coordination notices

None owed beyond this return: no `agents/**`, corpus, register, `.github/**`, or Root surface changed.
