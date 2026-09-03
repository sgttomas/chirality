# D1_IMPLEMENTER — Sealed Launch Brief (verbatim)

Instance: `D1_IMPLEMENTER` (ephemeral Agent 2 generalist, `software-bounded-implementation` method)
Parent: HELP_HUMAN (Agent 0), owner in-session
Received: 2026-09-03
Model: Claude Fable 5.1 (`claude-fable-5-1`)

The brief below is the dispatch prompt reproduced verbatim.

---

You are the sealed implementer for development node D of the Chirality App v3.0.0-rc.1 pathway: one seated, SELECTABLE item, DEL-05-01-V3-01 — v2 session-data lazy non-destructive access fixtures with typed failure.

Repository: the git repo whose worktree is /Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2. DO NOT change that worktree's branch or work inside it. Create your own worktree and keep it until I say the tranche is closed:
```
cd /Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2
git fetch origin
git worktree add /private/tmp/claude-501/-Users-ryan-dev-chirality--claude-worktrees-task-management-gen-pass-518da2/88f4d942-8887-44e9-b9df-8a72e2ed6f30/scratchpad/wt-nodeD -b codex/app-v3-nodeD-v2-session-access-2026-09-03 origin/main
```
Work only there (REPO_ROOT). Never use bare `git stash`. `WORKING_ROOT` = `{REPO_ROOT}/projects/chirality-app-dev`; `FRONTEND` = `{WORKING_ROOT}/frontend`. Basis must be `0c683fb16` or a descendant; record it.

## Read first
`{REPO_ROOT}/AGENTS.md`; `{WORKING_ROOT}/AGENTS.md`; `{WORKING_ROOT}/loop/LOOP_INIT.md`; the standing plan via `git show HEAD:projects/chirality-app-dev/loop/WORKPLAN_2026-09-03_app_dev_loop.md`; Rules + Receipt 205 of `loop/LOOP_RECEIPTS.md`; `skills/software-bounded-implementation/SKILL.md`; the item contract in `execution/PKG-05_.../DEL-05-01_.../_STATUS.md` `## Remaining` (DEL-05-01-V3-01) plus `ScopeOfWork.md` (OUT-001, R003/R004/R015) and `_DEPENDENCIES.md` (DEP-05-01-006); the D-APP-41 ruling under `execution/_Coordination/_DECISIONS/` (canonical session storage); `docs/SPEC.md` sections on session folders (search "sessions" and "events.jsonl"); `{FRONTEND}/src/lib/harness/session-manager.ts` in full (legacy path: `getLegacySessionFilePath`, merge of legacy and canonical records, `inferLegacyClaudeAdapter`), `session-events.ts`, existing tests `src/__tests__/lib/*session*` and `src/__tests__/integration/runtime-canonical-replay-restart*`, and any existing session fixtures under `src/__tests__/`.

## Step 0 (record in the run record before editing)
Clean status; basis SHA; receipts validator VALID; corpus status no drift; APP-HOLD-1 `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-05-01` ALLOW; **A1 re-stage declaration** (quote `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` lines 28-36; this tranche touches `frontend/src/**`). Create `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/` with ORCHESTRATION_PLAN.md, WORK_GRAPH.json, `instances/D1_IMPLEMENTER/LAUNCH_BRIEF.md` (this prompt verbatim), STEP0_DISCOVERY.md; later RETURN.md, CHECKS.json, `instances/D2_REVIEWER/`, HANDOFF_STATE.md, MANIFEST.sha256. `cd {FRONTEND} && npm ci`; stop and report if it cannot complete.

## Objective (exactly the seated scope; nothing more)
Representative v2 (current release 2.0.0) project-local session records must open lazily and non-destructively, with typed failure states, while list, resume, and delete behavior is preserved.
1. Fixtures: create representative legacy/v2 session records under a test fixture directory: (a) readable and well-formed, (b) malformed JSON / truncated, (c) unsupported or missing schema version, (d) a legacy record whose canonical counterpart already exists. Fixtures must contain no real secrets or user data.
2. Typed failure: reading a legacy record yields a typed result (e.g. `{ kind: 'ok' | 'malformed' | 'unsupportedVersion' | 'missing', ... }`) surfaced through the session-manager API without throwing raw parse errors to callers; list and resume must not crash on a malformed sibling record, and the failure state must be observable to the caller (so the UI can label it) rather than silently skipped.
3. Non-destructive: first-touch access never rewrites, truncates, or deletes the legacy file; prove with byte-identity assertions before/after list/resume; any canonical materialization writes only to the canonical folder. No bulk migration pass, no backup/rollback machinery (that is SCOPE_AMENDMENT S-4 and is out of scope).
4. Preserve list/resume/delete semantics: extend existing tests; delete of a session removes what the current contract says it removes and leaves other legacy records byte-identical.
Do not change the canonical folder layout, the `HarnessEvent` schema, `events.jsonl` handling, or any `runtime/**` file. Do not add dependencies.

## Write locus (nothing else may change)
`{FRONTEND}/src/lib/harness/session-manager.ts`, closely related session helper files in `src/lib/harness/` only if a type must be shared, tests and fixtures under `{FRONTEND}/src/__tests__/**`, the DEL-05-01 folder (`_STATUS.md`, `MEMORY.md` if present, `Evidence/**`, `_run_records/**`), the AgentRuns run record, `loop/LOOP_RECEIPTS.md` append at closeout. Validate with `python3 tools/software_workflow/validate_change_scope.py` before freezing.

## Checks (record exact command, cwd, exit, summary in CHECKS.json)
From FRONTEND: `npm run typecheck`; `npm test` (full Vitest; note totals); `npm run build` is not required by the path rules for `src/**` but run it if time permits and record; premerge per `software-workflow.json` (`next dev` stub server on a free port, then `npm run harness:validate:premerge`; the "absent runtime-daemon bindings" class may be deferred to PR CI, anything else repaired). From REPO_ROOT: `git diff --check`; harness self-check; harness pytest; from WORKING_ROOT: hold scan; corpus status.

## Freeze for independent review (do NOT push yet)
Commit locally (message ends with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`), write RETURN.md (behavior, files, evidence refs, byte-identity proof, residual risks, write-scope validation), and stop, returning: local commit SHA, diff stat, check table, and `REVIEW_READY`. Keep the worktree. I dispatch a fresh read-only reviewer and relay findings; remediate and re-freeze until PASS.

## After I send `REVIEW_PASS`
Save the reviewer return under `instances/D2_REVIEWER/`; update DEL-05-01 `_STATUS.md` (remove V3-01 from Remaining, keep V3-02; History line with commit, evidence, checks, A1 declaration; lifecycle lines untouched); HANDOFF_STATE.md; MANIFEST.sha256; append **Receipt 208** (Parent `Receipt-205`; Examined-Through = basis; Owner-Direction pointer to the dev-slate selection in the run record; Pointers; Checks pass/fail only; Model-Attribution "Claude Fable 5.1 (claude-fable-5-1) as ephemeral Agent 2 implementer under HELP_HUMAN (Claude Fable 5.1); reviewer Claude Fable 5.1"; Gate-Outcome `EXECUTED — awaiting owner merge`). Then `git fetch origin && git rebase origin/main` (receipts append only), rerun typecheck + vitest + receipts validator + diff --check, commit, push, `gh pr create` against `main` (body: basis, item closed, behavior summary, byte-identity proof pointer, check table, reviewer verdict; end with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`). Do not merge. Return PR number and head SHA; remove the scratch worktree (keep the branch).
