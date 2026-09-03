# APPDEV_V3_NODE_D_2026-09-03 — Orchestration Plan

Status: `ACTIVE — RE-FROZEN AFTER REVIEW ROUND 1 (A13 APPLIED)`
RunID: `APPDEV_V3_NODE_D_2026-09-03`
Parent: HELP_HUMAN (Agent 0), owner in-session; standing plan
`loop/WORKPLAN_2026-09-03_app_dev_loop.md` (selected from committed `HEAD`);
handoff basis Receipt-205.
Selection authority: owner dev-slate selection (2026-09-03, HELP_HUMAN
session chat) of development node D = `DEL-05-01-V3-01` (`SELECTABLE`).
Posture: `SEQUENTIAL_IMPL_THEN_INDEPENDENT_REVIEW` — one ephemeral Agent 2
implementer (`D1_IMPLEMENTER`, `software-bounded-implementation` method),
frozen local commit, then one fresh read-only reviewer (`D2_REVIEWER`,
`software-code-review` method) dispatched by the parent over 100% of the
frozen diff; remediation loops until `REVIEW_PASS`.
Graph version: `1`

## Objective (sealed)

`DEL-05-01-V3-01` — representative v2 (current release `2.0.0`)
project-local session records open lazily and non-destructively through
`frontend/src/lib/harness/session-manager.ts`, with typed failure states
(`ok | missing | malformed | unsupportedVersion`) surfaced through the
session-manager API, while list, resume, and delete behavior is preserved.
Fixtures: readable, malformed/truncated, unsupported-or-missing schema
version, and a legacy record whose canonical counterpart already exists.
No bulk migration, no backup/rollback machinery (`SCOPE_AMENDMENT_REQUIRED`
S-4 is out of scope). No change to the canonical folder layout, the
`HarnessEvent` schema, `events.jsonl` handling, or any `runtime/**` file.
No new dependencies.

## Basis

- Branch `codex/app-v3-nodeD-v2-session-access-2026-09-03` cut from
  `origin/main` at `0c683fb1657706316272951e4c3a0f7781b46009` (required
  basis `0c683fb16` or a descendant — satisfied, equal).
- Worktree: scratch worktree outside the parent's checkout; the parent's
  worktree branch is never changed.

## Write locus (fence)

- `projects/chirality-app-dev/frontend/src/lib/harness/session-manager.ts`
  (and closely related `src/lib/harness/` session helper files only if a
  type must be shared);
- `projects/chirality-app-dev/frontend/src/__tests__/**` (tests and fixtures);
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/**`
  (`_STATUS.md`, `MEMORY.md`, `Evidence/**`, `_run_records/**`);
- this run record `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/**`;
- `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` (append only, at closeout);
- *(added under owner ruling A13, 2026-09-03)* DEL-05-01 `ScopeOfWork.md`
  rows R010 / CLM-012 plus the dated note CLM-032 (inside the DEL-05-01
  root above), and the new ruling record
  `plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md`
  (repo-root `plans/steers/`, the App ruling-record surface).

Validated with `python3 tools/software_workflow/validate_change_scope.py`
before freeze.

## Checks (registered; recorded in `CHECKS.json`)

From `frontend/`: `npm run typecheck`; `npm test` (full Vitest); `npm run
build` (optional per path rules for `src/**`; run if time permits); premerge
per `software-workflow.json` (`next dev` stub server on a free port, then
`npm run harness:validate:premerge`; the absent-runtime-daemon-bindings class
may be deferred to PR CI). From repo root: `git diff --check`; practitioner
harness `self-check`; practitioner harness pytest. From the App working root:
APP-HOLD scan with register match; authority corpus status; receipts
validator.

## Gates

- APP-HOLD-1 dispatch preflight for `DEL-05-01`: `ALLOW` (see
  `STEP0_DISCOVERY.md`).
- A1 re-stage declaration recorded at Step 0 (`frontend/src/**` is touched).
- Independent-review path mandatory (product source changes): no push before
  `REVIEW_PASS`.
- Owner merge only; no self-merge; no lifecycle, release, Root, or
  host-mutation act.
