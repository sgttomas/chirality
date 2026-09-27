# Coordination Notice — hosted CI does not run PEC v2's registered checks

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality Root
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260927-RV1-INTAKE`, node TM1 (WORKING_ITEMS, `task-management`)
**Date:** 2026-09-27

## Request

PEC asks Root to consider allocating hosted CI for PEC v2's registered checks,
with a full-history checkout. Whether to take this in, and how, is Root's own
intake decision under its own instruments. PEC opens no Root path and writes
no Root register row.

The PEC owner directed this routing on 2026-09-27 ("CAND-03 promote to
Root"), recorded in
`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md`.
PEC tracks the concern as `TM-PEC-027` in
`projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv`, elevated
to Root. Its intake source is candidate `CAND-PEC-2026-09-27-03` in
`projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md`.
If Root opens a row, it may cite `TM-PEC-027` and this notice.

## Evidence (observed at `origin/main` `acc7d3cc7`)

- `.github/workflows/pec-tests.yml` (SHA-256
  `337611cef97e0c691f5a3cb305b804aef6f5300b7337a3ad23dd2b53689f5a7d`). Its only
  product job, `pec` (L48–82), runs `npm test` in `projects/pec` (L80–82).
  That script runs the workspace suites of `core`, `server` and
  `agent-sidecar` only (`projects/pec/package.json` L21, SHA-256
  `a20d06cbbd95b5b20a7b1355b91fdefe7bed5280c858838300257e5115065b39`, runs
  `projects/pec/tools/run-workspace-tests.ts`, whose `WORKSPACES` at L17 lists
  those three; SHA-256
  `ba5306cb181758c6277515b898df7cbcb0ea9648f685b370ecd740ff26511d01`). Those
  workspaces are part of PEC's frozen reference corpus (`projects/pec/AGENTS.md`,
  "Frozen Reference Corpus"). The job's checkout (L55–63) is sparse and
  blob-filtered and sets no `fetch-depth`, so it fetches a single commit.
- `tools/hosted-ci-routing.json` (SHA-256
  `1850e9a4477eb8198efe2a096f5059e7249230e14a72eb98d422e04a19a08b97`). The path
  rule at L74–94 routes `projects/pec/v2/**` (L80) to the `pec` check only
  (L92), so a change under `v2/**` selects the frozen `npm test` job.
- `projects/pec/software-workflow.json` (SHA-256
  `d55fff77a1d216a7b1ab78b16e3ff3f2747fb3b542a2b269367ec3afa83e0bbd`) registers
  the v2 checks `v2-api-contract`, `v2-loop-registry`, `v2-store-guard`,
  `v2-parsers` and `v2-core-posture`. They are Python `unittest` or script
  checks run from `projects/pec`. No workflow under `.github/workflows/` runs
  them, so every v2 merge relies on locally recorded check evidence.
- Full history: the X1 fixture pins need it. See
  `projects/pec/execution/_Coordination/X1_FIXTURES_2026-09-27/HANDOFF_STATE.md`
  L29 (SHA-256 `c832e9fcc0d5935d0708c5b0e8c11a7e7b471a489ef255d2c8e86d0c6a8cbd9d`):
  "a future hosted job needs full history (Root/CI scope, F-5/X-2)".
- PEC cannot make this change itself. `.github/workflows/**` and
  `tools/hosted-ci-routing.json` are Root/CI scope, and, as the intake
  records, every PEC packet since `D-PEC-87` has excluded them (`D-PEC-91` proposal F-5 (X-2); `D-PEC-106`
  exclusion list). No Root row, notice or undertaking carries it.
  `TM-ROOT-111` (local pre-push guards) and archived `TM-ROOT-110` (G4
  manifest wiring) concern other CI guards.

## PEC's current position

PEC is at a freeze point the owner declared (`D-PEC-107`, "Freeze point").
PEC's state after PR #1014, together with that record's decisions, is the
basis for a later ground-up reassessment, alongside the owner's rewrite of
the App PRD and of Chirality's governance framework. No PEC scope change is
open. This notice asks for nothing on PEC's schedule. Production of PEC v2
continues in a later session, so the exposure grows when parser source lands
under `v2/src/**`.

## Boundary

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. Root may adopt, amend, defer or
decline any part of it under its own instruments. It changes no PEC
product, lifecycle, source, release or reliance state.
