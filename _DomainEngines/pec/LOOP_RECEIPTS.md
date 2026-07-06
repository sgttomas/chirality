# PEC Loop Receipts

> **Epistemic status: derivative handoff ledger — not authority.** Append-only.
> Current state is always re-derived from the live tree, the decision registers,
> the pec profile (`_DomainEngines/profiles/pec.yaml`; DRAFT until owner Gate 2), git history, and the
> deterministic checks; on any disagreement those sources govern (K-AUTH-1). A
> receipt records only what tools cannot re-derive: owner directions given
> outside governed artifacts, gate outcomes and their rationale, deltas found in
> dated maps (which are never edited), and pointers to the authoritative
> artifacts created elsewhere.

## Rules (fixed — part of the loop protocol)

1. **Pointer, not narrative.** Prefer paths, PR numbers, commit SHAs, and
   decision IDs. Work history lives in commits, PRs, decision records, and
   project-local files — never here.
2. **Owner directions verbatim.** Any owner direction not otherwise captured in
   a governed artifact is quoted word-for-word with its date. This is the one
   place chat-only directions become durable.
3. **Measurements as check summaries only.** `self-check pass; harness pytest
   pass; pec health check pass` is the maximum. Until the harness tranche lands
   there are no pec `status`/`drift` measurements — do not invent them.
4. **Stale-map deltas as one-line pointers.** Dated assessments and plan files
   are never edited to match reality; a receipt line says what disagreed and
   where to verify.
5. **Gate outcomes with reason.** stopped / executed / awaiting owner — and
   why, especially no-op outcomes ("all remaining work is owner-shaped"), so
   the next loop neither rediscovers the stop nor invents work around it.
6. **Capped.** Roughly 6–12 lines per receipt. If it wants more, the detail
   belongs in a decision packet, PR description, or project-local record.

## Receipts (append-only)

- **2026-07-04 — Receipt 0** (loop creation).
  - HEAD at writing: `98dfde1d1` on local `main` (ahead of origin; the
    app-dev↔piping bridge loop is concurrently mid-flight — keep write scopes
    disjoint). Untracked planning artifacts present under `plans/`.
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "I want to
    create a new development loop to implement this plan." — "this plan" =
    `plans/pec_bridge_integration_plan_2026-07-04.md`. Owner supplied the
    launcher template and pointed at the bridge `LOOP_INIT.md` as the example:
    "I consider this init prompt to be sufficient for most needs."
  - Artifacts created (working tree, publication pending):
    `_DomainEngines/pec/{LOOP_INIT.md (byte-identical copy of
    bridge/LOOP_INIT.md), WORKPLAN_2026-07-04_pec_loop.md, LOOP_RECEIPTS.md}`;
    `init/init-prompt.md` §4 (pec launcher).
  - Delta vs the registration plan (map not edited, per rule 4): the loop
    scaffolding + launcher land NOW at owner direction, ahead of PR-A, and the
    launcher lands ACTIVE rather than "STAGED — activates on D-T0-15"; D-T0-15
    still ratifies the standing goal wording and the F-PEC fence set. The
    plan's Lane A loop-file rows are thereby already satisfied.
  - Gate outcome: loop created; no tranche executed this session. Next
    iteration starts at Step 0 and authors the registration package (PR-A
    tier-0, PR-B pec-side) per the plan, terminating in the D-T0-11..16 slate
    (renumber from the live register) for the owner.

- **2026-07-04 — Receipt 1** (registration package authored).
  - Start: `6a3fe012c`; branch `codex/pec-registration-package`; tree clean before work; no `tools/**` changes since Receipt 0 at discovery, so discovery self-check only.
  - Owner direction of record: "Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`. Read `{REPO_ROOT}/_DomainEngines/pec/LOOP_INIT.md` and follow it: pursue the loop's inherent goals — recorded in its standing plan — as far as live authority permits. Steer (this run): <none>"
  - Live gates checked: tier-0 register current through D-T0-10; no PEC-local register existed at discovery; bridge Receipt 24 says D-T0-10/D-APP-49/D-APP-50 are ruled and the remaining bridge lane is app-dev F3 execution.
  - Executed pointers: `_DomainEngines/pec/profile/pec.DRAFT.yaml` + validation report; `_DomainEngines/pec/PEC_2026-07-04_tier0-prep/`; D-T0-11..16 proposal packets + register rows; `_DomainEngines/proposals/pec/.gitkeep`; `projects/pec/AGENTS.md`; `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`; `projects/pec/docs/STATUS.md` pointer section; harness backlog/live-baseline pin updates.
  - Deltas (live tree wins): `init/init-prompt.md` already had the PEC launcher ACTIVE; the companion plan path named by the registration plan is absent; repo self-check entrypoint is `python3 tools/practitioner_harness/harness.py self-check`.
  - Gate outcome: registration package authored only; STOP at owner rulings D-T0-11..16. No `HumanRuling` filled, no profile adoption, no harness tranche, no profile move into `_DomainEngines/profiles/`, no PEC server/non-scratch DB mutation, no release/egress/professional claim.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=1/REVIEW=28/WARN=2; full practitioner harness pytest 259 passed / 1 skipped; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass after `npm install`; `git diff --check` pass.
  - Parked lanes: owner rulings on D-T0-11 registration shape, D-T0-12 profile lifecycle/Gate 2, D-T0-13 integration staging, D-T0-14 data residency, D-T0-15 standing goal/fences, and D-T0-16 harness-tranche authorization.

- **2026-07-04 — Receipt 2** (owner rulings recorded; harness tranche held).
  - Start: `60e0f63b8`; branch `codex/pec-registration-package`; PR #51 open/unmerged/green at discovery; tree clean before ruling-publication edits.
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "Bottom line: **I affirm all six recommendations**" and "I rule as above, the loop's next lawful tranche is exactly one thing: the TOOLMAKER harness PR under D-T0-16." Per-decision wording and D-T0-16 riders are recorded in D-T0-11..16.
  - Executed pointers: D-T0-11..16 packet ruling sections; `_DomainEngines/_DECISIONS/_REGISTER.md`; `PEC_2026-07-04_tier0-prep/{BRIEF_human_decisions.md,Handoff_State.md,TOOLMAKER_BRIEF-harness_pec_registration.md}`; `tools/practitioner_harness/BACKLOG.md`.
  - Gate outcome: D-T0-11 O-A, D-T0-12 O-A, D-T0-13 O-A with D-T0-14 residency gate note, D-T0-14 deferred with O-A CLOSED default, D-T0-15 O-A, D-T0-16 O-A with sequencing + DRAFT/Gate 2 open riders.
  - Not executed: no harness code change, no profile move, no ADOPTED status, no PEC server/non-scratch DB mutation, no instance-content capture or egress.
  - Checks: profile validator VALID; self-check pass; full practitioner harness pytest pass; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: owner merge of PR #51; after merge, TOOLMAKER harness PR under D-T0-16 is the next lawful tranche. Real data/export authorization remains for future D-PEC-01.

- **2026-07-04 — Receipt 3** (PR #51 merged; D-T0-16 harness tranche executed).
  - Start: `57307cac1` (`origin/main` after PR #51 merge); branch `codex/pec-harness-tranche`; PR #51 merged by owner direction.
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "merge PR #51".
  - Executed pointers: `tools/practitioner_harness/{adapter_domain_engines.py,cmd_bridge_status.py,cmd_self_check.py,harness.py}` + tests; `_DomainEngines/profiles/pec.yaml` + validation report; `_DomainEngines/DOMAIN_ENGINE_INDEX.md`; D-T0-11..16 publication-status updates; PEC `AGENTS.md`/`docs/STATUS.md` pointer corrections; harness backlog.
  - Gate outcome: D-T0-16 O-A tranche executed after PR #51 merge; bridge-status reports `pec` as `DRAFT` with `Gate 2 open`. No ADOPTED status, no `status`/`drift`/`next`/`brief --project pec` citizenship, no PEC runtime/server/non-scratch DB mutation, no instance-content capture or egress.
  - Checks: profile validator VALID; bridge-status pass; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; full practitioner harness pytest 263 passed / 1 skipped; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass.
  - Parked lanes: owner merge of the D-T0-16 harness PR; profile Gate 2 adoption remains owner-only; real data/export authorization remains for future D-PEC-01.

- **2026-07-04 — Receipt 4** (PR #53 merged; ladder-as-core-goal direction recorded).
  - Start: `d0924a926` (`origin/main`); direction-recording only, no tranche executed.
  - Gate outcome (closes Receipt 3's parked merge lane): owner direction (2026-07-04, in-session, Ryan Tufts): "I want you to carry this forward. Proceed as you recommend. I approve the merge." — PR #53 merged `904715d4d`; post-merge checks on `main`: validator VALID, self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5, harness pytest 264 passed (live DRAFT/Gate-2-open rider test ran green).
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts), said of the ruled D-T0-13 staging: "That's exactly the progression this needs to follow from L1, L2 to L3. It's one of the core inherent goals of the project now." — recorded durably in the standing plan's owner-intent addendum (same PR).
  - No ruling changed: D-T0-13/D-T0-14 govern staging and residency; Gate 2 open, owner-only; fences F-PEC-1..4 unchanged.
  - Next lawful tranches under the addendum: L1 read-only evidence inside CLOSED residency (committed fixtures/scratch DBs only, immutable capture manifests per D-T0-13), and D-PEC-01 packet preparation when the owner directs the real-data case.
  - Checks (this PR, loop-file-only change): self-check pass; harness pytest pass.

- **2026-07-04 — Receipt 5** (first L1 evidence capture — deterministic-check seam).
  - Start: `090cd4efb` (`origin/main` after PR #56); isolated worktree; pec subtree unmodified.
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "approved to merge and proceed from there." — PR #56 merged `090cd4efb`; proceeding = first lawful ladder tranche under the Receipt-4 addendum.
  - Executed pointers: `_DomainEngines/pec/PEC_2026-07-04_L1-evidence-01/` (MANIFEST.md + typecheck/test/build/drill logs) — immutable snapshot per the D-T0-13 capture convention; committed inputs and scratch DB only; no server start, no instance content, no egress (D-T0-14 CLOSED respected).
  - Evidence summary: typecheck/test/build/drill all exit 0 at `090cd4efb`; 161 tests pass (core 72, server 89); drill 17/17 on scratch DB. Not a pilot-readiness or correctness claim (F-PEC-2).
  - Gate outcome: L1 deterministic-check seam exercised; remaining L1 seams (exports, reports, Explain) need an owner-provisioned session and, for instance content, D-PEC-01/D-T0-14. Gate 2 adoption remains owner-only.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5 (no baseline shift); harness pytest pass.

- **2026-07-04 — Receipt 6** (L1 evidence 02 — owner-provisioned demo session; L1 seams complete).
  - Start: `8e42b126c` (`origin/main` after PR #57); isolated worktree; pec sources unmodified.
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "provision the demo basis: scratch DB, seeded demo data, capture as admin@aurora.dev" — the actor/visibility basis for this capture.
  - Executed pointers: `_DomainEngines/pec/PEC_2026-07-04_L1-evidence-02/` (MANIFEST + 18 hashed artifacts): authenticated session, all 11 register exports, sponsor-brief + package-pack renders, revision-gate Explain payloads, plan view — over the live HTTP API against a seeded scratch DB, deleted after capture.
  - Residency: D-T0-14 CLOSED respected — demo seed content only; no real project data existed in the DB at any point; no egress.
  - Delta found (tool gap, recorded in the manifest): `tools/seed.ts:43` ignores `PEC_DB` (server honors it) — compounds the profile's `seed.demo` open issue; candidate repair rides the future `pec_api_adapter`/harness work, not this loop's write scope (F-PEC-1).
  - Gate outcome: with evidence 01 (deterministic checks) + 02 (API seams), the L1 rung is exercised end-to-end at demo scope. Next rungs are owner-shaped: L1 acceptance → per-operation L2 (D-T0-13), D-PEC-01 for any real-data basis, Gate 2 adoption.
  - Checks: self-check pass; harness pytest pass.

- **2026-07-04 — Receipt 7** (L1 accepted as proven; loop handed to the standing agent).
  - Start: `fa0cdf3b8` (`origin/main` after PR #58 merge, owner-directed).
  - Owner ruling of record (2026-07-04, in-session, Ryan Tufts): "I accept L1 as proven. Once you've accounted for that ruling and what it entails, I want to hand-off the rest of the work to the other agent."
  - Executed pointers: `_DomainEngines/_DECISIONS/D-T0-17_pec_l1_acceptance.md` (acceptance record, D-T0-10 precedent; evidence commit-bound to PR #57 `8e42b126c` and PR #58 `fa0cdf3b8`); D-T0-17 register row RULED; ruling SHA backfill rides this branch.
  - What it unlocks: per-operation L2 of the D-T0-13 O-A path — `backup.create` first, each act human-confirmed, demo/scratch basis until D-PEC-01. Unchanged: D-T0-14 CLOSED, profile DRAFT/Gate 2 open, fences F-PEC-1..4, L3 future-only.
  - Handoff: no session-bound state exists — the next iteration (any agent) re-derives from this ledger, the registers, and the live tree per LOOP_INIT. Next lawful tranche: demo/scratch-basis `backup.create` L2 evidence, or D-PEC-01 packet preparation at owner direction.
  - Checks: self-check pass; harness pytest pass.

- **2026-07-04 — Receipt 8** (L2 `backup.create` evidence captured).
  - Start: `a20ce9c6c` (`origin/main` after PR #60); branch `codex/pec-l2-backup-create-evidence`; tree clean before evidence work.
  - Owner direction of record: "Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`. Read `{REPO_ROOT}/_DomainEngines/pec/LOOP_INIT.md` and follow it: pursue the loop's inherent goals — recorded in its standing plan — as far as live authority permits. Steer (this run): <none>"
  - Live gates checked: D-T0-17 RULED/ACCEPTED unlocks per-operation L2 with `backup.create` first; D-T0-14 CLOSED remains in force; D-PEC-01 is NOT_PREPARED; profile `pec` remains DRAFT/Gate 2 open.
  - Executed pointers: `_DomainEngines/pec/PEC_2026-07-04_L2-backup-create-01/` (MANIFEST + logs + scratch SQLite backup artifact `artifacts/pec-20260704-213204.db`, SHA-256 `8f538eac51c1376e2e96efe65f593eca2b96b69af7ec89434ae9a0122e2e8fb3`).
  - Gate outcome: L2 `backup.create` evidence executed on scratch/demo basis only; no PEC source edit, no server start, no non-scratch DB mutation, no real instance-content capture/egress, no restore/import/Gate-2/L3 claim.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 263 passed / 1 skipped; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass after `npm install`; `git diff --check` pass.
  - Parked lanes: `backup.restore`/`seed.demo`/`import.csv` L2 acts require their applicable human-confirmation/data basis; D-PEC-01 remains the real-data authorization packet; profile Gate 2 adoption and L3 remain owner-only/future.

- **2026-07-04 — Receipt 9** (PR #61 merged; L2 `backup.restore` evidence + D-PEC-01 packet).
  - Start: `c7d754174` (`origin/main` after PR #61 merge); branch `codex/pec-after-l2-backup`; tree clean before continuation work.
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "I approve merger of the PR.  Then continue with the remaining work." — PR #61 merged `c7d754174`.
  - Live gates checked: D-T0-17 keeps per-operation L2 open; D-T0-14 CLOSED remains in force; profile `pec` remains DRAFT/Gate 2 open; D-PEC-01 was NOT_PREPARED at discovery.
  - Executed pointers: `_DomainEngines/pec/PEC_2026-07-04_L2-backup-restore-01/` (MANIFEST + scratch restore logs/artifacts; restored/source DB SHA-256 `c0fda65d6897d918d1dd27ce83503bd1a6d399aaf348cb29fc0a73b5c23d278b`); `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-01_pilot_rehearsal_real_data_authorization.md`; D-PEC-01 register row `AWAITING_RULING`.
  - Gate outcome: L2 `backup.restore` evidence executed on scratch/demo basis only; D-PEC-01 packet prepared only. No real instance-content capture/egress, no real import/restore, no `force=true`, no Gate-2/L3/pilot-readiness/go-live claim.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 263 passed / 1 skipped; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: owner ruling on D-PEC-01; `import.csv` over real data and real-pilot restore remain gated by that ruling; `seed.demo` remains parked behind the scratch/demo guard gap; profile Gate 2 adoption and L3 remain owner-only/future.

- **2026-07-04 — Receipt 10** (PR #63 merged; stopped at D-PEC-01 owner gate).
  - Start: `d9a266311` (`origin/main` after PR #63 merge); branch `codex/pec-after-dpec01-packet`; tree clean before receipt-only work.
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "I approve merger of the PR.  Then continue with the remaining work." — PR #63 merged `d9a266311`.
  - Live gates checked: D-PEC-01 is `AWAITING_RULING`; D-T0-14 CLOSED remains in force; profile `pec` remains DRAFT/Gate 2 open; no new tier-0 or PEC-local ruling appeared after Receipt 9.
  - Gate outcome: stopped after merge accounting because all remaining advancement is owner-shaped. No D-PEC-01 `HumanRuling` filled, no real instance-content capture/egress, no real import/restore, no `force=true`, no Gate-2/L3/pilot-readiness/go-live claim.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; closeout checks ride this receipt-only branch.
  - Parked lanes: owner ruling on D-PEC-01; profile Gate 2 adoption; L3/proposal-shaped apply path; `seed.demo` guard repair remains outside the PEC loop's current write fence.

- **2026-07-05 — Receipt 11** (PR #64 merged; stopped at D-PEC-01 owner gate).
  - Start: `24e9a8374` (`origin/main` after PR #64 merge); branch `codex/pec-after-pr64-merge`; tree clean before receipt-only work.
  - Owner direction of record (2026-07-05, in-session, Ryan Tufts): "I approve merger of the PR.  Then continue with the remaining work." — PR #64 merged `24e9a8374`.
  - Live gates checked: D-PEC-01 is `AWAITING_RULING`; D-T0-14 CLOSED remains in force; profile `pec` remains DRAFT/Gate 2 open; no new tier-0 or PEC-local ruling appeared after Receipt 10.
  - Gate outcome: stopped after merge accounting because all remaining advancement is owner-shaped. No D-PEC-01 `HumanRuling` filled, no real instance-content capture/egress, no real import/restore, no `force=true`, no Gate-2/L3/pilot-readiness/go-live claim.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; closeout checks ride this receipt-only branch.
  - Parked lanes: owner ruling on D-PEC-01; profile Gate 2 adoption; L3/proposal-shaped apply path; `seed.demo` guard repair remains outside the PEC loop's current write fence.

- **2026-07-05 — Receipt 12** (PR #65 merged; stopped at D-PEC-01 owner gate).
  - Start: `935a7493c` (`origin/main` after PR #65 merge); branch `codex/pec-after-pr65-merge`; tree clean before receipt-only work.
  - Owner direction of record (2026-07-05, in-session, Ryan Tufts): "I approve merger of the PR.  Then continue with the remaining work." — PR #65 merged `935a7493c`.
  - Live gates checked: D-PEC-01 is `AWAITING_RULING`; D-T0-14 CLOSED remains in force; profile `pec` remains DRAFT/Gate 2 open; no new tier-0 or PEC-local ruling appeared after Receipt 11.
  - Gate outcome: stopped after merge accounting because all remaining advancement is owner-shaped. No D-PEC-01 `HumanRuling` filled, no real instance-content capture/egress, no real import/restore, no `force=true`, no Gate-2/L3/pilot-readiness/go-live claim.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; closeout checks ride this receipt-only branch.
  - Parked lanes: owner ruling on D-PEC-01; profile Gate 2 adoption; L3/proposal-shaped apply path; `seed.demo` guard repair remains outside the PEC loop's current write fence.

- **2026-07-05 — Receipt 13** (PR #66 merged; PEC slate rulings recorded).
  - Start: `d14fb7e87` (`origin/main` after PR #66 merge); branch `codex/pec-record-rulings`; tree clean before ruling-accounting work.
  - Owner direction of record (2026-07-05, in-session, Ryan Tufts): PR #66 merge approved and the PEC slate ruled; full verbatim rulings live in D-PEC-01 and D-PEC-04..06.
  - Executed pointers: D-PEC-01 RULED O-A with hash-permitted rider and owner-basis-before-run rider; D-PEC-04 RULED O-B Gate 2 remains DRAFT/open; D-PEC-05 RULED O-B L3 deferred; D-PEC-06 RULED O-A `seed.demo` guard repair authorized as a later separate PR; PEC-local register rows updated.
  - Gate outcome: real-data rehearsal authorized only in principle; not executable until owner supplies exact paths, actor/visibility basis, scratch DB/backup locations, and capture limits. `force=true` remains prohibited absent separate ruling. No Gate-2/L3/pilot-readiness/go-live claim.
  - Checks: closeout checks ride this ruling-accounting branch.
  - Parked lanes: owner-supplied D-PEC-01 execution basis; merge of this accounting PR; then separate narrow `seed.demo` guard PR.

- **2026-07-05 — Receipt 14** (PR #68 merged; D-PEC-06 `seed.demo` guard repair executed).
  - Start: `73091e8be` (`origin/main` after PR #68 merge); branch `codex/pec-seed-demo-guard`; tree clean before guard work.
  - Owner direction of record (2026-07-05, in-session, Ryan Tufts): "I approve merger of the PR.  Then continue with the remaining work." — PR #68 merged `73091e8be`.
  - Executed pointers: `projects/pec/tools/seed.ts`; `projects/pec/server/test/seed-guard.test.ts`.
  - Gate outcome: D-PEC-06 O-A executed narrowly — `seed.demo` now requires explicit `PEC_DB`, refuses non-scratch/non-demo targets, and seeds only explicit temp/scratch/demo targets. No D-PEC-01 real-data rehearsal, no `force=true`, no Gate-2/L3/pilot-readiness/go-live claim.
  - Checks: profile validator VALID; self-check pass; practitioner harness pytest pass; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: D-PEC-01 evidence run awaits owner-supplied exact paths, actor/visibility basis, scratch DB/backup locations, and capture limits; profile Gate 2 remains DRAFT/open; L3 remains deferred until after D-PEC-01 evidence.

- **2026-07-05 — Receipt 15** (PR #69 merged; D-PEC-01 basis surface prepared).
  - Start: `bc77dec2c` (`origin/main` after PR #69 merge); branch `codex/pec-pr69-l3-basis`; tree clean before accounting work; rebased before PR onto `433a50edc` after unrelated piping PR #67 merged.
  - Owner direction of record (2026-07-05, in-session, Ryan Tufts): "Proceed accordingly" toward and through L3; lawful interpretation is D-PEC-01 basis preparation because D-PEC-05 parks L3 until pilot evidence exists.
  - Executed pointers: `_DomainEngines/profiles/pec.yaml` + validation report; `_DomainEngines/pec/PEC_2026-07-05_DPEC01-execution-basis/{OWNER_INPUTS.md,RUNBOOK.md,MANIFEST_TEMPLATE.md}`.
  - Gate outcome: PR #69 merge accounted; stale `seed.demo` profile open issue resolved; D-PEC-01 owner-input checklist/runbook/manifest template prepared. No D-PEC-01 evidence run, no raw real-content capture, no `force=true`, no Gate-2 adoption, no L3 design/execution tranche.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 263 passed / 1 skipped; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: D-PEC-01 evidence run awaits owner-supplied exact paths, actor/visibility basis, scratch DB/backup locations, and capture limits; L3 remains deferred until after that evidence is captured.

- **2026-07-05 — Receipt 16** (pilot input files discovered on the rehearsal surface; stopped at the D-PEC-01 basis gate).
  - Start: `59d1e4c7c` (`origin/main`); branch `codex/pec-receipt16-dpec01-basis-gate`; tree clean; discovery-only iteration.
  - Live gates checked: no new tier-0 or PEC-local ruling after Receipt 15 (registers end at D-T0-17 / D-PEC-06); D-T0-14 CLOSED, profile DRAFT/Gate 2 open (D-PEC-04 O-B), L3 deferred (D-PEC-05 O-B).
  - Delta found (live tree vs Receipt 15's "awaits owner-supplied" state): PR #74 (`01a5df1b9`) gitignored `projects/pec/pilot-scratch/` as the owner-designated D-PEC-01 rehearsal surface, and real input files now sit untracked at `projects/pec/pilot-scratch/input/{mdl,rail,decisions,risk}.xlsx` + `schedule.pdf`. Paths are thereby observable, but the D-PEC-01 rider's remaining basis — actor/visibility, scratch DB/backup locations, raw-content-view permission, capture limits, restore scope — is still unsupplied (`OWNER_INPUTS.md` all TBD); no owner in-session direction this run (steer `<none>`).
  - Gate outcome: stopped — the evidence run must not begin per the D-PEC-01 rider ("do not start the rehearsal until I provide them"); file placement alone is not the supplied basis. Demo-basis `seed.demo`/`import.csv` L2 rungs also parked: profile flags them `requires_human_confirmation: true` and no in-session confirmation exists this run. Proposed basis values presented to the owner in-session and in this PR's description for one-shot confirmation.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; harness + source_audit pytest 370 passed (run at discovery because `tools/**` changed since Receipt 15 — piping's `tools/equation_audit`/`source_audit`); `git diff --check` pass.
  - Parked lanes: owner supplies the remaining D-PEC-01 basis (or confirms proposed values); optional per-act confirmations for demo-basis `seed.demo`/`import.csv` L2; profile Gate 2 and L3 remain owner-only/deferred per D-PEC-04/05.

- **2026-07-05 — Receipt 17** (D-PEC-01 basis supplied; rehearsal evidence 01 + `seed.demo` L2 executed).
  - Start: `4477c8554` on `codex/pec-dpec01-pilot-evidence` (stacked on the Receipt-16 branch; base `59d1e4c7c` = `origin/main`).
  - Owner directions of record (2026-07-05, in-session, Ryan Tufts): "For the Optional demo-basis L2 rungs, I approve they can run on scratch/demo basis independently of D-PEC-01." — and the full D-PEC-01 execution basis (paths, actor `ryan@chirality.ai`/full visibility, scratch DB/backup/restore locations, real backup OUT OF SCOPE this run, raw-view + unredacted-commit permissions, no capture limits beyond hashes) — recorded verbatim in `PEC_2026-07-05_DPEC01-execution-basis/OWNER_INPUTS.md`.
  - Executed pointers: `PEC_2026-07-05_DPEC01-pilot-evidence-01/` (input hashes, verbatim conversions, as-is drill + API import shakedown — all four contracts reject at the §16 required-column gate — column-gap analysis, scratch backup→restore over owner paths, §16 export template); `PEC_2026-07-05_L2-seed-demo-01/` (seed on scratch/demo target exit 0 + non-scratch refusal exit 1).
  - Deltas (live tree wins): basis `risks.xlsx` → live `risk.xlsx`; drill always uses its own OS-temp scratch DB (owner scratch import DB exercised via API seam instead); owner dev server live on `:4811` (capture used `:4899`); import layer is CSV-only so xlsx went through verbatim conversion; `schedule.pdf` not importable verbatim (CSV/XER contract).
  - Gate outcome: rehearsal executed to the honest boundary — the workbooks are not §16 contract-shaped, and column mapping is owner/pilot-team judgment (F-PEC-2 posture), so no row-level real import was performed and no record state invented. No `force=true`, no real-DB mutation, no Gate-2/L3/pilot-readiness/go-live claim.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 263 passed / 1 skipped; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: owner supplies §16 contract-shaped exports (template: evidence-01 `api/exports/mdl.csv`) or rules a column mapping → evidence-02 row-level real import; real-backup restore rehearsal awaits a real pilot DB; Gate 2 and L3 per D-PEC-04/05.

- **2026-07-05 — Receipt 18** (owner mapping direction; templates authored; evidence 02 row-level real import).
  - Start: branch `codex/pec-dpec01-evidence-02` (stacked on evidence-01 branch; base `59d1e4c7c`).
  - Owner directions of record (2026-07-05, in-session, Ryan Tufts): "Save copies of the files I provided. Create the templates you need that take the best of what I've provided and adds what else you need." and "Secondly my intention was to provide you with the real data for testing. So each document except risk was already populated."
  - Executed pointers: originals preserved byte-identical at `pilot-scratch/originals-2026-07-05/` (uncommitted); `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/` (five §16 template CSVs + `IMPORT_MAPPING.md`, F-PEC-1 coordination surface); `PEC_2026-07-05_DPEC01-pilot-evidence-02/` (import reports, exports, overview, sponsor brief, post-import backup log).
  - Results: MDL 457/457 accepted, re-import 457 updated/0 duplicated (idempotency), export byte-identical to import input; RAIL 272 and decisions 62 rejected row-level with one substantive blocker — no person roster exists (owner/authority match no person); clerical mapping defaults flagged ⚑ in `IMPORT_MAPPING.md` for owner ratification.
  - Gate outcome: real-data import testing executed to the instance's limit; no `force=true`, no real production DB (none exists), no Gate-2/L3/pilot-readiness/go-live claim, no reserved PEC human act. Roster creation is owner-shaped (identity records) — options presented in `IMPORT_MAPPING.md`.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 264 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: owner rules roster (mapping table or placeholder-person policy) → RAIL/decisions re-import; ⚑ mapping-default ratifications; risk-log population and schedule CSV/XER export (owner-side); real-backup restore once a real pilot DB exists; Gate 2 / L3 per D-PEC-04/05.

- **2026-07-05 — Receipt 19** (stack merged; roster + evidence 03; D-PEC-07 packet).
  - Start: `d80cccf5d` (`origin/main` after owner-directed merges of PR #75/#76/#77); branch `codex/pec-dpec01-evidence-03`.
  - Owner directions of record (2026-07-05, in-session, Ryan Tufts): "1. Create placeholders 2. Proceed with this as-is unless you recommend changes now (do it!) else we can always change later. 3. Yes merge the stack. 4. Will do. In order to do so I want the embedded agent to accept a file upload from me and take action accordingly to update things. That's one end goal. Proceed accordingly."
  - Executed pointers: PR #75/#76/#77 merged; `IMPORT_TEMPLATES/ROSTER_PLACEHOLDERS.csv` (44 placeholders; `None` excluded); `IMPORT_MAPPING.md` ruling + applied-changes + seam-behavior sections; `PEC_2026-07-05_DPEC01-pilot-evidence-03/`; `D-PEC-07_embedded_upload_agent_pathway.md` + register row AWAITING_RULING.
  - Results: RAIL 254/272 in instance as unanchored intake (238 + 16 after fixing the quoted-CSV roster-application error), 18 residual data-gap rejects; decisions 52/62 accepted, 10 residual; applied ratified changes (raised_date default on 199 rows, package←AREA). Seam finding recorded: RAIL re-import duplicates unanchored intake rows (not idempotent by item_id) — avoided by fix-batch-only re-import; candidate harness/tool backlog item.
  - Gate outcome: rehearsal exercised end-to-end on populated workbooks; STOP at D-PEC-07 for the upload-agent pathway (L3-shaped; D-PEC-05's evidence precondition now met — recommendation O-C, design-only). No pec source change, no `force=true`, no Gate-2/L3 act, no intake triage or other reserved human act.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 264 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: D-PEC-07 ruling; owner-side data gaps (17+1 RAIL dates, 10 decision authority/status, risk-log population, schedule CSV/XER export); coordinator triage of 254 intake items (reserved human workflow); real-backup restore awaits a real pilot DB; Gate 2 per D-PEC-04.

- **2026-07-05 — Receipt 20** (PR #78 merged; D-PEC-07 O-C ruled + executed; full dataset loaded; evidence 04).
  - Start: `main` after owner-directed PR #78 merge; branch `codex/pec-dpec01-evidence-04`.
  - Owner directions of record (2026-07-05, in-session, Ryan Tufts): "1. Merge PR #78 2. This is all test data so you can make up whatever dates you want to fill in what you need at this point. 3. I approve `O-C`: formalize the zero-code pathway today (user drops a file, agent maps → proposed import → user approves import) 4. I've put `schedule.csv` in place of the PDF schedule file. Proceed accordingly."
  - Executed pointers: PR #78 merged; `PEC_2026-07-05_DPEC01-pilot-evidence-04/`; `IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md` (O-C zero-code pathway formalized); `_DomainEngines/proposals/pec/BRIEF_2026-07-05_embedded_upload_agent_design.md` (CANDIDATE, design-only); D-PEC-07 ruling section + register row RULED (ruling SHA backfilled same-branch).
  - Results: schedule 127/127 accepted (owner-dropped extractor CSV, mapped `SCH-{id}`); RAIL date-fix batch 18→intake (272/272 in instance); decisions full re-import 10 accepted + 52 updated (62/62). Zero outstanding rejects. Test-data fills tagged in-row per ruling 2 (need_by 2026-12-31; authority `Project`; status `identified`).
  - Gate outcome: D-PEC-01 rehearsal complete on the populated dataset; D-PEC-07 O-C executed to its design gate — the CANDIDATE brief awaits owner adoption; implementation stays gated on adoption + pec source tranche authorization. No `force=true`, no pec source change, no reserved human act (272 intake items await coordinator triage).
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 264 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: owner adoption of the upload-agent design brief (then tranche packet); risk-log population (owner-side); coordinator triage; real-backup restore awaits a real pilot DB; Gate 2 per D-PEC-04; placeholder→real roster swaps at owner's pace.

- **2026-07-05 — Receipt 21** (adversarial review of the D-PEC-07 artifacts; report + slate published, fixes gated).
  - Start: `41744fe6d` (`origin/main` after PR #79); branch `codex/pec-dpec07-review-report`; tree clean; no ruling newer than Receipt 20 in either register.
  - Owner directions of record (2026-07-05, in-session, Ryan Tufts): "Thorough adversarial review of the D-PEC-07 artifacts created 2026-07-05 (Receipts 19–20) … Findings as a report + slate; fix-worthy items only on my ruling — do not amend the ruled packet." and "Consider what has merit from this assessment performed by another agent … Incorporate what's warranted into your own work and write your output to `projects/pec/execution/_Coordination/`."
  - Executed pointers: `projects/pec/execution/_Coordination/REVIEW_2026-07-05_D-PEC-07_artifacts.md` (24 verified findings RV-1..24, merged from this loop's two-lens-verified multi-agent review + an owner-supplied second assessment re-verified against the live tree; refuted claims recorded; decision slate S-1..S-5).
  - Gate outcome: review executed to the report; STOP at the S-1..S-5 slate — packet corrigendum, runbook v1.1, brief v1.1, new register rows (adoption-gate residual; CSV formula-injection repair authorization), IMPORT_MAPPING refresh are all owner-ruling-gated. Ruled packet not amended; no pec source change; no reserved human act.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 264 passed; coord-check re-run on both Receipt 19/20 ranges (confirms COORD_PRECEDENT_NOT_NAMED on packet + brief); PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass.
  - Parked lanes: owner ruling on slate S-1..S-5; all Receipt-20 parked lanes carry forward unchanged.
