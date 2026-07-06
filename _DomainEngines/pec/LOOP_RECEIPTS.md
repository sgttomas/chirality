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

- **2026-07-05 — Receipt 22** (S-1..S-5 ruled; D-PEC-07 corrigendum + adopted brief + open residual rows).
  - Start: `7e00eca8b` (`origin/main` after PR #80); branch `codex/pec-dpec07-slate-rulings`; tree clean before work.
  - Owner ruling of record (2026-07-05, in-session, Ryan Tufts):

    > I have read projects/pec/execution/_Coordination/REVIEW_2026-07-05_D-PEC-07_artifacts.md
    > and I rule on the slate as follows. Execute the affirmed items branch-first in one PR per
    > the workplan step-4 checks; record these rulings verbatim in the governed artifacts and
    > Receipt 22; stop for my merge — do not self-merge.
    >
    > - S-1 (packet corrigendum): affirmed. Set the D-PEC-07 header status to RULED, add the
    >   `**Ruling SHA:** 1a9e4071c` line, and append a dated corrigendum note correcting RV-1
    >   (a CSV file-upload UI already exists in the Admin page; what is absent is a multipart
    >   endpoint, server-side file storage, and an agent surface), RV-2 (D-T0-13 O-A ruled L2 as
    >   the destination with L3 future-only — not L3 as the destination), and RV-4 (the lifecycle
    >   is the five-state list including `rejected`). Also correct RV-5: annotate that F-PEC-1 is
    >   an absolute write-path fence, not a tranche-unlockable one. Do not rewrite the ruled text
    >   itself — corrections live in the appended dated note.
    >
    > - S-2 (runbook v1.1): affirmed in full. RV-7: approval must follow the Step-3 proposed
    >   import — a drop-time "proceed"/"import it" message is not the approval; remove that
    >   shortcut. RV-8: scope the idempotency claim to the contracts actually evidenced (MDL,
    >   decisions); mark risks and schedule as code-implied but not yet evidenced. RV-9: change
    >   "(later: pilot) PEC_DB" to "pilot only under a future owner ruling." RV-10: add the
    >   export-and-compare verification as a standing rule. RV-11: note the commit-capture rule
    >   rides my 2026-07-05 basis and a materially new data source needs fresh confirmation of
    >   capture limits.
    >
    > - S-3 (brief): I adopt the brief. Change its status from CANDIDATE to ADOPTED and record
    >   this adoption ruling in it. Adoption authorizes NO implementation: I am deferring the
    >   source-tranche gate — do not author or request a tranche, and the F-PEC-1 fence stays
    >   closed. One adoption rider (RV-12): the LLM-backed-mapper step remains gated on a future
    >   D-T0-14 residency ruling; the adopted brief must state that routing instance content to
    >   an external model is not authorized under the current CLOSED residency. All other brief
    >   fixes (RV-13 K-AUTH-2/hash binding, RV-14 CSV-only v1, and RV-15 through RV-21) are
    >   deferred to the tranche packet as named obligations and need not be applied now.
    >
    > - S-4 (register rows): affirmed. Because I adopt the brief this session, open D-PEC-08
    >   scoped to the remaining gate only — the source-tranche authorization for the upload-agent
    >   implementation — AWAITING_RULING. Open D-PEC-09 for the CSV formula-injection repair,
    >   AWAITING_RULING and design-only; it authorizes no source change.
    >
    > - S-5 (IMPORT_MAPPING refresh): affirmed. Update the schedule section to the proven
    >   schedule.csv extractor mapping (evidence-04, SCH-{id}) and add the risks placeholder note.
  - Executed pointers: `D-PEC-07_embedded_upload_agent_pathway.md` corrigendum; `FILE_DROP_RUNBOOK.md` v1.1; adopted `BRIEF_2026-07-05_embedded_upload_agent_design.md` with RV-12 rider and RV-13..21 deferred obligations; PEC register rows + packets `D-PEC-08_upload_agent_source_tranche_authorization.md` and `D-PEC-09_csv_formula_injection_repair.md`; `IMPORT_MAPPING.md` schedule/risks refresh.
  - Gate outcome: S-1..S-5 executed exactly as ruled. D-PEC-08 and D-PEC-09 are AWAITING_RULING; D-PEC-09 is design-only and authorizes no source change. No upload-agent implementation tranche authored/requested; no pec source change; no `force=true`; no non-scratch DB mutation; no self-merge.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 264 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass; `coord-check --diff origin/main..HEAD` pass after precedent notes.
  - Parked lanes: owner merge of this PR; D-PEC-08 source-tranche authorization; D-PEC-09 CSV formula-injection repair ruling; Receipt-20 parked lanes otherwise carry forward.

- **2026-07-05 — Receipt 23** (D-PEC-09 source repair authorized and executed).
  - Start: `eab490eea` on `codex/pec-dpec07-slate-rulings`; PR #81 open; tree clean before D-PEC-09 ruling/execution work.
  - Owner ruling of record (2026-07-05, in-session, Ryan Tufts):

    > I authorize the source change for D-PEC-09.
    >
    > Commit and merge once you're complete.

  - Executed pointers: `projects/pec/server/src/import/csv.ts` neutralizes exported CSV cells beginning with `=`, `+`, `-`, or `@`; `projects/pec/server/test/csv.test.ts` pins the serializer regression; `D-PEC-09_csv_formula_injection_repair.md` and PEC register row record O-A/RULED.
  - Gate outcome: D-PEC-09 narrow source repair executed and merge authorized. D-PEC-08 remains AWAITING_RULING; no upload-agent implementation tranche; no unrelated import behavior change; no data model change; no `force=true`; no non-scratch DB mutation.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; practitioner harness pytest 264 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass (server tests 94, including CSV neutralization); `coord-check --diff origin/main..HEAD` pass/no findings; `git diff --check` pass.
  - Parked lanes: D-PEC-08 source-tranche authorization; Receipt-20 parked lanes otherwise carry forward.

- **2026-07-05 — Receipt 24** (D-PEC-08 O-A ruled; upload-agent v1 tranche prepared and executed).
  - Start: `4a6e9d3ed` (`origin/main` after PR #81 merge); branch `codex/pec-dpec08-upload-agent-tranche`; tree clean before work.
  - Owner ruling of record (2026-07-05, in-session steer, Ryan Tufts): "I authorize `D-PEC-08` with `O-A` for preparation/execution of a bounded upload-agent source tranche, limited to an exact file fence, tests, deferred D-PEC-07 obligations RV-13 through RV-21, and rollback/verification plan." — recorded verbatim in the D-PEC-08 packet; ruling SHA `563a968d3`.
  - Executed pointers: `execution/_Coordination/TRANCHE_2026-07-05_D-PEC-08_upload_agent_v1.md` (exact fence, RV-13..21 discharge, rollback/verification plan); D-PEC-08 packet + register row RULED; implementation inside the fence — `import_proposal` record + `IPR` lifecycle service (`server/src/services/proposals.ts`), propose/refresh/accept/apply/reject routes with same-origin guard, `import.propose`/`import.accept` permissions, RAIL unanchored-intake idempotency repair, Admin "Proposed imports" UI, tests (`server/test/import-proposal.test.ts`, permissions).
  - Gate outcome: tranche executed exactly to the packet fence; dry-run rolls back; accept is hash+version bound with staleness refusal; apply is human-only and transaction-atomic; no LLM call exists (RV-12 rider honored under CLOSED D-T0-14); no `force=true` in any run; no non-scratch DB mutation; no Gate-2/L3-beyond-this-design/pilot-readiness claim; no self-merge — STOP at owner merge of this PR.
  - Checks: profile validator VALID (report byte-identical); self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; full `tools/` pytest 748 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass (core+server 101 server tests incl. 7 new); `coord-check --diff origin/main..HEAD` pass/no findings; `git diff --check` pass; scope check: 13 changed paths = fence + 3 coordination artifacts.
  - Parked lanes: owner merge of this PR; D-PEC-09-style follow-ups named in the tranche packet (origin guard on pre-existing routes, external upload store if sizes demand); Receipt-20 parked lanes (coordinator triage, risk-log population, real-backup restore, Gate 2 per D-PEC-04) carry forward.

- **2026-07-05 — Receipt 25** (owner directions recorded: triage delegated-once-capable; risks deferred; pilot-DB and Gate-2 questions answered).
  - Start: `82afc2829` on `codex/pec-dpec08-upload-agent-tranche`; PR #82 open/unmerged; direction-recording only, no tranche executed.
  - Owner directions of record (2026-07-05, in-session, Ryan Tufts): "I'm going to delegate the intake of those items. I want the agent to do it once it has the capability. I will upload risks but at a later time. Deferred. But can we start the pilot DB now? Finally, what entails Gate 2?"
  - Executed pointers: PEC register row D-PEC-10 opened NOT_PREPARED (agent intake-triage capability; blocks agent triage of the 272 imported intake items).
  - Gate outcome: no triage performed (capability and authorization absent; D-PEC-10 will carry the design + ruling); risks upload deferred owner-side; pilot-DB provisioning NOT started — F-PEC-1 forbids agent runs against a non-scratch DB, so the pilot DB starts either owner-side per `projects/pec/docs/PILOT.md` or via a future owner basis ruling naming DB/backup paths and operator; Gate 2 explained in-session (owner adoption act on `_DomainEngines/profiles/pec.yaml` per D-T0-12; deferred by D-PEC-04 O-B until owner judges pilot evidence sufficient) — remains owner-only.
  - Checks: self-check pass; `git diff --check` pass; receipt/register-only commit rides the open PR branch.
  - Parked lanes: owner merge of PR #82; D-PEC-10 packet preparation at owner direction; pilot-DB basis (owner-side start or basis ruling); risks upload (owner-side, deferred); Gate 2 per D-PEC-04.

- **2026-07-05 — Receipt 26** (PR #82 merged; Gate 2 ADOPTED and executed; pilot DB deferred).
  - Start: `f67ac908e` (`origin/main` after owner-directed PR #82 merge); branch `codex/pec-gate2-adoption`.
  - Owner ruling of record (2026-07-05, in-session, Ryan Tufts): "merge PR #82 now, then I adopt the pec profile for Gate 2, you may execute as you see fit.  We will not start the pilot DB this time.  Another time." — merge executed as directed; adoption recorded verbatim in the D-T0-12 packet's dated Gate-2 adoption note; pilot-DB start deferred owner-side.
  - Executed pointers: `_DomainEngines/profiles/pec.yaml` DRAFT→ADOPTED (+ open-issue annotation, validation report regenerated VALID); `_DomainEngines/_DECISIONS/D-T0-12_pec_profile_lifecycle.md` adoption note; tier-0 register D-T0-12 row; `_DomainEngines/DOMAIN_ENGINE_INDEX.md` banner/row/layout; PEC register pointer row D-PEC-11 RULED; `projects/pec/{AGENTS.md,docs/STATUS.md}` pointer corrections (Receipt-3 precedent); conscious live-pin update `tools/practitioner_harness/test_live_baseline.py` (DRAFT/Gate-2-open pin → ADOPTED/Gate-2-adopted, workplan step-4 convention).
  - Gate outcome: Gate 2 executed as a governance act only — no pec source change, no pilot DB start (owner deferred), no integration-level change (`MANUAL_BRIDGE`/L0 unchanged), no professional/go-live claim (APEGA ceiling); D-T0-14 CLOSED residency and all fences unchanged. STOP at owner merge of this PR.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5 (no baseline shift); bridge-status row `pec | ADOPTED | Gate 2 adopted | MANUAL_BRIDGE`; full `tools/` pytest 748 passed (updated pin green); PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; `git diff --check` pass; coord-check on the range: 2 known REVIEW findings only — COORD_UNRESOLVED_REF ×2 on the D-T0-12 packet's ruled 2026-07-04 text citing the DRAFT-era staged profile path (historical; annotated, never rewritten).
  - Parked lanes: owner merge of this PR; pilot-DB basis (owner: "Another time"); D-PEC-10 agent-triage packet at owner direction; risks upload owner-side deferred.

- **2026-07-05 — Receipt 27** (PR #83 merged; L3 decision slate prepared — D-T0-18 + D-PEC-12).
  - Start: `3e5b240f8` (`origin/main` after owner-directed PR #83 merge); branch `codex/pec-l3-slate`; packet-preparation only, no execution.
  - Owner directions of record (2026-07-05, in-session, Ryan Tufts): "merge PR #83" — executed; and "I want to get to L3." — treated as direction to prepare the L3 gate surface, not as a staging ruling (D-T0-13 ruled L2 destination / L3 future-only; only a tier-0 ruling advances it).
  - Executed pointers: `_DomainEngines/_DECISIONS/D-T0-18_pec_l3_operation_proposal_advance.md` + tier-0 register row AWAITING_RULING (residual of D-T0-13; both named preconditions now discharged — proposal-shaped API via PR #82, evidence via D-PEC-01 runs 01–04); `D-PEC-12_l3_import_proposal_semantics.md` + PEC register row AWAITING_RULING (resolves the profile's L3-semantics open issue for the import scope; single-record-of-authority, human-only accept/apply, CLOSED-residency lines).
  - Gate outcome: STOP at the owner slate — D-T0-18 (staging advance) and D-PEC-12 (semantics) rule together; no profile edit, no integration-level change, no L3 evidence run, no pec source change this iteration.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; full `tools/` pytest 748 passed; coord-check on the range pass; `git diff --check` pass.
  - Parked lanes: owner rulings D-T0-18 + D-PEC-12 (then: one execution PR + first L3 evidence run on an owner-named basis); D-PEC-10 agent-triage packet; pilot-DB basis; risks upload — all carry forward.

- **2026-07-05 — Receipt 28** (PR #84 merged; D-T0-18 O-A + D-PEC-12 ruled and executed; L3 evidence 01 captured).
  - Start: `45ff3e6a7` (`origin/main` after owner-directed PR #84 merge); branch `codex/pec-l3-execution`.
  - Owner ruling of record (2026-07-05, in-session, Ryan Tufts): "1. O-A advance. 2. The agent should have full agency, don't try to use semantics as a replacement for proper governance harnesses (more than just semantics) so focus on making a useful agent for now. Merge the PR first and then proceed accordingly." — recorded verbatim in both packets; interpretation note in D-PEC-12 (mechanical harnesses govern; full agency inside them; useful agent first).
  - Executed pointers: D-T0-18 + D-PEC-12 ruling sections and register rows RULED; `_DomainEngines/profiles/pec.yaml` `integration_level` MANUAL_BRIDGE→OPERATION_PROPOSAL + L3 open-issue resolved-for-imports + import.csv note (validator VALID); `DOMAIN_ENGINE_INDEX.md` row/layout; conscious live-pin update (`test_live_baseline.py` bridge-status row → OPERATION_PROPOSAL); `PEC_2026-07-05_L3-evidence-01/` (IPR-0001 full lifecycle on seeded scratch DB via live API: propose→dry-run→hash-bound accept→atomic apply; apply report identical to dry-run; export round-trip; DB deleted); first proposals mirror `_DomainEngines/proposals/pec/OP_2026-07-05_IPR-0001_mdl_fixture.md`.
  - Delta noted (live tree wins): owner's uncommitted edit to `init/init-prompt.md` (subagent-model guidance) found in the working tree — preserved uncommitted, not ridden into this PR.
  - Gate outcome: L3 reached and evidenced for the imports scope. Demo-basis acts only; no `force`; no real instance content (D-T0-14 CLOSED); no pilot start; no professional/go-live claim. STOP at owner merge of this PR.
  - Checks: profile validator VALID; self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; full `tools/` pytest pass at final SHA; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; coord-check on the range; `git diff --check` pass.
  - Parked lanes: owner merge of this PR; L3 on real/pilot data awaits a pilot DB + basis (owner: "Another time"); D-PEC-10 agent-triage packet (natural next capability for the useful-agent direction); risks upload owner-side.

- **2026-07-05 — Receipt 29** (D-PEC-10 packet prepared per owner steer; AWAITING_RULING; stopped at the gate).
  - Start: `e1c5b080a` (`origin/main`); branch `codex/pec-dpec10-intake-triage-packet`; tree clean before work; no ruling newer than Receipt 28 in either register; no `tools/**` change since Receipt 28's final-SHA checks → discovery self-check only.
  - Owner workflow intent of record (2026-07-05, in-session, Ryan Tufts, verbatim — quoted here per steer item 1):

    > So for now I'm planning to use it myself, on my local machine. I will be using the RAIL, Master Deliverables List, Risk Log, Schedule, and Package Tracker, to update the status by having the agent intake and triage the information therein to the correct database assignments. The interface will also allow the human to make targeted changes within the current screen and what it shows. But the agent is the primary means of making updates. As for how I get the information into those documents, it occurs from weekly updates and work I do within my team. That's the intended workflow, which was more than how I probably initially described it.

  - The owner's full preparation steer (items 1–4: verbatim-intent mandate; obligation decomposition, no silent scope trims; RAIL+MDL synthetic-data rehearsal as the verification bar; standing constraints and AWAITING_RULING stop) is quoted verbatim in the packet's "Preparation direction of record" section.
  - Executed pointers: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-10_agent_intake_triage.md` (intent verbatim; obligations WF-1..11; RAIL+MDL rehearsal gate; agent-act-boundary riders); PEC register row D-PEC-10 → AWAITING_RULING. Packet adversarially verified pre-presentation (multi-agent pass); 1 blocker + 5 majors found and fixed — rehearsal reordered (v2 re-import before triage), WF-3/4 discharge path fenced (no implied source change), 272-item run gated on an owner visibility-basis confirmation, coordinator-grant/`skipPermission`/`is_admin` breadth disclosed, watermark audit-only carve-out pinned.
  - Gate outcome: STOP at the D-PEC-10 ruling per steer item 4 ("Prepare to AWAITING_RULING and stop at the gate."). No rehearsal run, no pec source change, no actor provisioned, no tier-0 row opened (the WF-5 Package Tracker row opens on ruling); no self-merge — owner merges this PR.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5 (no baseline shift); full `tools/` pytest 748 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; coord-check on the range at final SHA; `git diff --check` pass.
  - Parked lanes: owner ruling D-PEC-10 (O-A/O-B/O-C) → rehearsal with the owner at the screen; WF-5 Package Tracker register row on ruling; 272-item triage run basis confirmation after the rehearsal; pilot-DB basis (owner: "Another time"); risks upload owner-side — carry forward.

- **2026-07-05 — Receipt 30** (D-PEC-10 O-A ruled; PR #86 merged; rehearsal-01 executed with the owner at the screen).
  - Start: `9dd310cc3` (`origin/main` after owner-directed PR #86 merge); branch `codex/pec-dpec10-rehearsal`.
  - Owner ruling of record (2026-07-05, in-session, Ryan Tufts, verbatim): "1. I rule `O-A` 2. merge PR #86" — recorded in the D-PEC-10 packet's Human-ruling section; ruling SHA `9dd310cc3`. Merge executed as directed.
  - Executed pointers: D-PEC-10 packet + register row RULED; `PEC_2026-07-05_DPEC10-rehearsal-01/` (synthetic RAIL+MDL, IPR-0001..0006 through the live API: v1 loads, serial v2 idempotent update-in-place, OM-3 conflict reported-not-applied, agent triage — DEC-0001/WI-0001/parked/duplicate, two items left for the owner — forced-and-recovered 409 `STALE_PROPOSAL` with the owner's screen edit as the mover, post-triage re-import observation dry-run-only); mirror `_DomainEngines/proposals/pec/OP_2026-07-05_DPEC10_rehearsal_IPR-0001-0006.md`; `FILE_DROP_RUNBOOK.md` v1.2 (weekly cycle; supersedes the v1.1 full-RAIL-re-import rule with dated provenance); PEC register rows opened `D-PEC-13` (Package Tracker, WF-5), `D-PEC-14` (risks/schedule live evidence, WF-3/4), `D-PEC-15` (post-disposition re-import behavior — rehearsal observation).
  - Gate outcome: rehearsal discharged the D-PEC-10 gate as designed — every accept/apply was the owner's screen act (personId 15); the agent (own person, `is_admin=0`, coordinator, personId 16) drove propose/refresh/triage only; no `force`; scratch DB deleted after capture; D-PEC-01 surfaces untouched; no pec source change; no tier-0 act; D-T0-14 CLOSED (synthetic data throughout). STOP at owner merge of this PR. The 272-item real-data triage run stays gated on the owner's visibility-basis confirmation (packet Scope note 4).
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5; full `tools/` pytest 748 passed; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; coord-check on the range at final SHA; `git diff --check` pass.
  - Parked lanes: owner merge of this PR; D-PEC-13/14/15 rulings at owner direction; 272-item run basis confirmation; pilot-DB basis; risks upload owner-side — carry forward.

- **2026-07-06 — Receipt 31** (pec↔app-dev bridge planning slate prepared per owner steer; stopped at every gate).
  - Start: `e2e30abfa` (`origin/main` after PR #87 merge); branch `codex/pec-appdev-bridge-packets`; tree clean before work; no ruling newer than Receipt 30 in either register; no `tools/**` change since Receipt 30 → discovery self-check only (pass, no baseline shift).
  - Owner direction of record (2026-07-05, in-session steer, Ryan Tufts, verbatim): "the pec ↔ chirality-app-dev bridge is my top priority for both projects: a fully functioning bridge, with a built-in agent UI in pec. This session is detailed planning ONLY — prepare the tier-0 decision packet(s) and the design brief(s) for the lane and stop at every gate; no source tranche in either project this run."
  - Executed pointers: `_DomainEngines/_DECISIONS/D-T0-19_pec_appdev_bridge_lane.md` (lane + transport + tool mapping + cross-loop sequencing) and `D-T0-20_pec_harness_agent_residency.md` (residual of D-T0-14: LLM-hosted-agent visibility) + tier-0 register rows AWAITING_RULING; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-16_builtin_agent_ui.md` + pec register row AWAITING_RULING; CANDIDATE briefs `_DomainEngines/proposals/pec/BRIEF_2026-07-05_pec_appdev_bridge_design.md` and `BRIEF_2026-07-05_pec_builtin_agent_ui_design.md`. Packet set adversarially verified pre-presentation (two-lens multi-agent pass); 4 MAJORs fixed — a misquoted owner verbatim, a real-DB mutation-basis gap (D-T0-20 rules visibility only; the D-PEC-10 scratch rider and deferred pilot-DB basis stand), app-dev ID/write-surface deconfliction for the O-1A grant, receipt anchoring — plus minors.
  - Deltas vs the run steer (live tree wins): `domain_propose_operation`/`domain_proposal_validate` are D-APP-50 descriptor-only registrations, not names pre-reserved for pec (D-T0-19 claims them for pec explicitly); pec has no standalone dry-run route (dry-run computes at propose and via refresh); pec auth is cookie/session-only with no token mechanism (shapes the O-2A person-bound identity design).
  - Gate outcome: STOP at the slate per the steer — D-T0-19, D-T0-20, D-PEC-16 all AWAITING_RULING; briefs CANDIDATE; no source tranche in either project; no app-dev, bridge-loop, or piping write; no D-APP row opened (P1/P2 IDs provisional, renumber-at-authoring); no self-merge — owner merges this PR.
  - Checks: self-check pass at INFO=15/NOT_APPLICABLE=2/REVIEW=28/WARN=5 (no baseline shift); full `tools/` pytest pass at final SHA; PEC `npm run typecheck && npm test && npm run build && npm run drill` pass; coord-check on the range pass/no findings; `git diff --check` pass.
  - Parked lanes: owner rulings D-T0-19 (O-1A also grants + deconflicts the app-dev packet-authoring scope and adopts the bridge brief) / D-T0-20 / D-PEC-16 → next iteration authors the app-dev P1/P2 PROPOSALs and the D-PEC-17-to-be tranche row as ruled; the real/non-scratch-DB mutation-basis row remains future (pilot-DB: "Another time"); D-PEC-13/14/15, 272-item basis confirmation, risks upload owner-side — carry forward.

- **2026-07-06 — Receipt 32** (bridge-lane rulings recorded; reconstruction anchor tagged; session pre-ruling of record).
  - Start: `4c636e53e` (`origin/main` after PR #88, clean); branch `codex/pec-bridge-rulings-2026-07-06`. **Reconstruction anchor (owner steer): tag `pre-bridge-session-2026-07-06` = `4c636e53e5b428e93afddfa1e70a6cd633abcc72`, pushed before any other work.**
  - Owner rulings of record (2026-07-06, in-session steer, Ryan Tufts): **D-T0-19 RULED O-1A + O-2A + O-3A**, **D-T0-20 RULED O-B**, **D-PEC-16 RULED O-A (runtime RT-B)** — each quoted verbatim in its packet's Human-ruling section (rule 2 satisfied there); ruling received with `main` at `4c636e53e`.
  - Owner session authorization of record (2026-07-06, in-session steer, Ryan Tufts, item 4 — quoted verbatim in full as that item itself requires; this receipt and every pre-ruled selection this session rely on it):

    > Session authorization — a conditional standing pre-ruling (this session
    > only; expires at session end or 24 hours after this direction, whichever
    > comes first; quote this item verbatim in the first receipt that relies on
    > it). Development is open across all fronts of this repository, with the
    > bridge lane (D-T0-19 P1→P4, D-PEC-17) as top priority. For any decision
    > packet PREPARED THIS SESSION — including the P1/P2 app-dev packets,
    > D-PEC-17, and the preparation of previously opened NOT_PREPARED rows such
    > as D-PEC-13/14/15 — I pre-rule, now, the packet's recommended option,
    > conditional on all of the following. The agent records each outcome
    > verbatim as "recommended option selected by the owner's 2026-07-06
    > conditional pre-ruling" with a pointer to this direction — K-AUTH-1
    > intact: the ruling act is mine, made here; the agent only records which
    > option this pre-ruling selected.
    >
    > Conditions:
    > a. The packet has passed the two-lens adversarial verification pass (fact
    >    lens + governance lens, fable agents at high effort) with every BLOCKER
    >    and MAJOR finding fixed, and the verifiers were told the result will be
    >    pre-ruled without my read.
    > b. The recommendation lies inside the architecture already ruled (D-T0-19/
    >    D-T0-20/D-PEC-16 and prior rulings). If the honest recommendation falls
    >    outside these bounds, conflicts with an exclusion below, or the agent
    >    finds itself recommending against its own earlier work, STOP and bring
    >    it to me.
    > c. Self-merge is permitted only when the full check set is green at the
    >    final SHA: profile validator where touched; repo self-check with no
    >    unexplained baseline shift; full tools/ pytest; pec `npm run typecheck
    >    && npm test && npm run build && npm run drill`; coord-check on the
    >    committed range; `git diff --check`; and CI green on the PR for every
    >    check that does not require the absent ANTHROPIC_API_KEY — the known
    >    harness-premerge secret failure is excluded from "green," with its
    >    key-independent substance run locally instead and the exclusion noted
    >    in the receipt. Every pre-ruled selection and every self-merge goes in
    >    the receipt.
    >
    > Environment constraint: no ANTHROPIC_API_KEY exists in this environment
    > and none will be provided this session. Build every LLM seam (the RT-B
    > sidecar's engine, any harness-session-dependent path) behind a
    > config-driven engine port with a deterministic stub, so a key can be
    > dropped in later without source change. All tests and evidence this
    > session are key-independent (stubbed engine or direct handler/API
    > invocation); live-LLM demonstration is deferred, and its absence is
    > stated plainly in the evidence packs — never worked around by sourcing,
    > hardcoding, or fabricating a key or its outputs.
    >
    > I note and intend the transitive consequence: this authorization opens
    > source changes in both pec and chirality-app-dev this session, under the
    > ruled designs, the standing fences as amended by item 1, and the checks
    > above.
    >
    > Excluded — still my acts only:
    > - anything lifting the scratch/demo mutation basis toward my real/
    >   non-scratch DB;
    > - any residency expansion beyond the D-T0-20 O-B enumeration;
    > - force=true in any form;
    > - accept/apply on real data (demo-cast accept/apply on scratch bases for
    >   rehearsal evidence is permitted per the D-PEC-12 full-agency amendment
    >   and must be disclosed in the evidence pack);
    > - ruling any NEW tier-0 (D-T0-*) row: prepare it and stop;
    > - ruling rows another loop prepared before this session (e.g., piping
    >   D-12/D-07b);
    > - release/publish/egress acts and professional claims (F-PEC-3,
    >   K-DOMAIN-4) — unchanged;
    > - anything the standing fences reserve to me that this direction does not
    >   explicitly cover.

  - Per-run steer also of record (one line each): orchestration = dependency-ordered tranches, disjoint write scopes in parallel, main loop holds shared surfaces/gates/merges; subagent models = opus for discovery/checks/breadth, fable-high for planning/adversarial verification/governed execution, fable-low for mechanical execution only.
  - Executed pointers (this PR): D-T0-19/D-T0-20 packets + tier-0 register rows RULED; D-PEC-16 packet + pec register row RULED; bridge brief + UI brief CANDIDATE → ADOPTED (dated adoption notes; RT-B of record); O-1A fence-scope grant notes (D-T0-19 packet, D-T0-15 packet, workplan F-PEC-4 bullet); app-dev register preamble deconfliction grant note + bridge-ledger cross-loop note 2026-07-06; `_DomainEngines/profiles/pec.yaml` `data_residency` CLOSED → OPEN_ENUMERATED per D-T0-20 O-B (validator VALID, report byte-unchanged); RV-12 rider annotation in the adopted upload brief; pec register rows opened `D-PEC-17` (NOT_PREPARED) + `D-PEC-18` (pointer, RULED).
  - Gate outcome: rulings recorded exactly as given; no new tier-0 row ruled; the D-PEC-10 Scope-note-4 visibility confirmation for the 272-item run is discharged by the D-T0-20 ruling text; the 272-item run on pilot-scratch is owner-clarified lawful (scratch/demo mutation basis) and parked behind the bridge-lane priority. Self-merge of this PR under item 4c with the full check set green at the final SHA.
  - Checks (at this PR's final SHA): profile validator VALID; self-check pass no baseline shift; full `tools/` pytest pass; pec `npm run typecheck && npm test && npm run build && npm run drill` pass; coord-check on the committed range pass; `git diff --check` pass; CI consulted with the known harness-premerge `ANTHROPIC_API_KEY` secret failure excluded per item 4c (key-independent substance run locally).
  - Parked lanes: P1/P2 app-dev packets + tranches (next, this session, under item 4); D-PEC-17 preparation + tranche (next, this session, under item 4); P4 end-to-end rehearsal (owner at the screen — cannot be discharged agent-side); 272-item triage run on pilot-scratch (lawful, behind bridge priority); D-PEC-13/14/15 preparation (item-4-eligible, behind bridge priority); live-LLM demonstration (deferred — no key this session); pilot-DB/real-basis row, risks upload owner-side — carry forward.

- **2026-07-06 — Receipt 33** (D-APP-51 prepared, pre-ruled selection recorded, tranche executed — bridge-lane P1).
  - Start: `aee453185` (`origin/main` after PR #89); branch `codex/pec-dapp51-registry`; packet authored under the D-T0-19 O-1A decision/coordination-packet grant (app-dev register preamble note; deconfliction honored — ID `D-APP-51` minted next-free from the live register; no other loop's row touched).
  - Pre-ruled selection of record (Receipt 32 item 4): **D-APP-51 O-A, riders 1-8** — recommended option "selected by the owner's 2026-07-06 conditional pre-ruling". Condition (a): two-lens adversarial verification (fable, high effort; verifiers told the result would be pre-ruled without the owner's read) — fact lens PASS 0 BLOCKER/0 MAJOR; governance lens 0 BLOCKER/1 MAJOR (condition-c check-set under-enumeration) — the MAJOR and all lesser findings fixed pre-recording. Condition (b): recommendation independently re-checked inside D-T0-19 O-1A/O-2A/O-3A + D-T0-20 O-B + the adopted bridge brief + D-APP-49/50 riders; the packet's disclosed V-9 fix judged lawful in-scope; STOP clause not fired.
  - Executed pointers: packet + **mandatory** ruling record `D-APP-51_RULING_2026-07-06.md` + register row (app-dev register, RULED) at `78d38945d`; tranche `09aa8c5c8` (closed two-entry registry `domain-profile-registry.ts`; read-tools registry dispatch with pec read-side exposure and exactly the three disclosed open_pipe_stress-visible deltas incl. the V-9 quoted-marker fix; vendored-bytes + live-marker-sync + refusal-path tests; catalog regenerated); repin `623f0c4a4` (`HARNESS_TOOL_REGISTRY_VERSION` v8→v9 `multi-engine-profile-registry`; D-APP-48 pull contract repinned, validator pass).
  - Delta of record (live tree wins; disclosed in packet V-9 and fixed in-tranche): the shipped D-APP-50 gate checked unquoted id markers against quoted live-profile ids — both live read tools refused their own ruled profile; masked by an unquoted test fixture; regression-pinned now.
  - Gate outcome: executed under the recorded pre-ruled ruling; `domain_propose_operation`/`domain_proposal_validate` remain descriptor-only (P2 = D-APP-52); no apply tool; no pec/piping/tier-0 write; no F1/F2/F4 crossing. Self-merge of this PR under Receipt 32 item 4c with the full check set green at the final SHA.
  - Checks (at this PR's final SHA): profile validator — inapplicable (no profile touched; per the check's own qualifier); self-check pass no unexplained baseline shift; full `tools/` pytest 747 passed / 1 skipped (the skip is the test's own environment condition — `test_write_status_guard.py` skips when the untracked `exports/chirality-app/staging` copy is absent, as in a fresh worktree; 748 pass where it exists); pec `npm run typecheck && npm test && npm run build && npm run drill` pass; app-dev typecheck + full vitest 599 + catalog `--check` + contract-deps + premerge pass (**premerge ran fully keyless locally — the item-4c `ANTHROPIC_API_KEY` exclusion was not needed at tranche level**; the repo CI `harness` check governs the PR); pull-contract validator pass; coord-check on the committed range exit 0 (4 REVIEWs, all unresolved-ref human-review class inside the new packet, sibling-packet convention); `git diff --check` pass. Pre-existing, not caused here: app-dev `instruction-root:integrity` fails identically at `origin/main` (requires a packaged desktop bundle absent in every tree).
  - Parked lanes: D-APP-52 execution (next, this session — sequenced behind this merge); D-PEC-17 tranche (parallel branch); P4 rehearsal (owner at the screen); 272-item run on pilot-scratch; D-PEC-13/14/15 preparation; live-LLM demonstration (deferred, no key) — carry forward.

- **2026-07-06 — Receipt 34** (D-PEC-17 prepared, pre-ruled selection recorded, tranche executed — the built-in agent UI, RT-B sidecar).
  - Start: `aee453185` (branch `codex/pec-dpec17-agent-ui`, rebased onto `4dddea6ef` pre-merge); packet folds the tranche detail per the D-PEC-08 precedent.
  - Pre-ruled selection of record (Receipt 32 item 4): **D-PEC-17 O-A** — recommended option "selected by the owner's 2026-07-06 conditional pre-ruling". Condition (a): two-lens verification (fable, high effort; verifiers told the result would be pre-ruled without the owner's read) — fact PASS 0 BLOCKER/0 MAJOR; governance 0 BLOCKER/1 MAJOR (conversion-to-approval-records loophole via `skipPermission`, fixed BOTH ways: stub vocabulary exclusion + engine-independent disposition-payload guard, each test-pinned) — every finding fixed pre-recording. Condition (b): in-bounds independently re-checked; the governance lens's load-bearing judgment: **the two root-manifest fence rows are lawfully openable by this ruled tranche** (D-PEC-08 supplies the mechanism; the ruled design's own text opens the category; item 4's transitive-consequence sentence covers it), conditional on the lockfile/manifest checks staying merge-gating and this receipt recording the opening — both honored.
  - **Root-manifest opening of record (per that judgment):** `projects/pec/package.json` (workspaces + `agent-sidecar` + the named script lines only — hunk-exact-match verified) and `package-lock.json` (regenerated `--package-lock-only`; diff carries only the `@pec/agent-sidecar` workspace entries; grep of added lines for `https://|integrity` = none → **zero new external package resolutions**; F-PEC-3 zero-dep posture intact; `projects/pec/server/package.json` diff EMPTY per rider 1).
  - Executed pointers: governance `55bfd9d0d` (packet + register row RULED); tranche `4f03c6ca5`→`97018d5ec` pre-rebase (core `agent.direct` admin/pm/coordinator — document_controller exclusion test-pinned; sidecar package `@pec/agent-sidecar` zero-runtime-dep with config-driven engine port, deterministic stub, lazy `sdk.ts` loader — key-droppable, both no-key startup errors test-pinned; server proxy `GET/POST /api/projects/:pid/agent/{status,messages}` same-origin-guarded, human cookie stripped; web shell-level agent panel with no accept/apply control of its own); evidence `_DomainEngines/pec/PEC_2026-07-06_DPEC17-evidence-01/` (scratch basis via guarded seed, agent person `is_admin=0` rehearsal-01 pattern; ruled `409 STALE_PROPOSAL` flow fired live unforced and recovered; deterministic `converted` refusal byte-identical twice; WF-8 actor split in history; demo-cast admin accept/apply disclosed, `force` never sent; **live-LLM demonstration deferred — no `ANTHROPIC_API_KEY` this session — stated verbatim in the pack**; scratch DB deleted after capture).
  - Gate outcome: executed under the recorded pre-ruled ruling inside its expiry window; no residency widening (stub egress `none`; O-B clamp keyed on engine egress class, unknown classes default `model-provider`); mutation basis untouched (scratch only); accept/apply remained human screen acts (agent's attempt refused 403 in evidence); no tier-0 act. Self-merge of this PR under Receipt 32 item 4c with the full check set green at the final SHA.
  - Checks (at this PR's final SHA): profile validator — inapplicable (profile untouched); self-check pass no unexplained baseline shift; full `tools/` pytest pass (747/1 environment-conditional skip class, as Receipt 33); pec `npm run typecheck && npm test && npm run build && npm run drill` pass (74+109+37 tests incl. the new proxy + sidecar suites); coord-check on the committed range; `git diff --check` pass; CI `harness` green on the PR (the app-dev harness-premerge secret failure did not arise — repo CI carries no such check; noted per item 4c).
  - Parked lanes: D-APP-52 execution (parallel branch, this session); P4 rehearsal (owner at the screen); sidecar SDK-engine enablement (owner act: dependency + key + `PEC_AGENT_ENGINE=sdk`); the dev-script login/startup race note (future register row candidate, disclosed in the tranche report); 272-item run on pilot-scratch; D-PEC-13/14/15 preparation — carry forward.

- **2026-07-06 — Receipt 35** (D-APP-52 prepared, pre-ruled selection recorded, tranche executed — bridge-lane P2; the bridge is live end-to-end on the scratch basis).
  - Start: `4dddea6ef` (`origin/main` after PR #90); branch `codex/pec-dapp52-transport`, rebased onto `e80c45cdf` (after PR #91) pre-merge; packet authored under the D-T0-19 O-1A grant (ID `D-APP-52` minted next-free; deconfliction honored).
  - Pre-ruled selection of record (Receipt 32 item 4): **D-APP-52 O-A, riders 1-11** — recommended option "selected by the owner's 2026-07-06 conditional pre-ruling". Condition (a): two-lens verification (fable, high effort; verifiers told the result would be pre-ruled without the owner's read) — fact PASS 0 BLOCKER/0 MAJOR; governance 0 BLOCKER/2 MAJOR (item-4c check-set under-enumeration; demo-cast `force` value unpinned) — every finding fixed pre-recording. Condition (b): in-bounds independently re-checked (D-T0-19 O-2A/O-3A implemented exactly as ruled; D-T0-20 O-B bound structural; STOP clause not fired). Sequencing rider satisfied: D-APP-51 landed at `4dddea6ef`.
  - Executed pointers: governance `fb17d91d5` (packet + **mandatory** ruling record `D-APP-52_RULING_2026-07-06.md` + register row RULED); tranche `7353aa16a` (loopback-only endpoint-allowlisted `pec-bridge-client.ts` — login/create/refresh/get only, single-401-re-login, redaction test-pinned; `domain-proposal-tools.ts` live handlers gated on the D-APP-51 pec registry entry `engineKind: 'http-api'`; `domain_propose_operation` live write-graded propose/refresh, `domain_proposal_validate` live read-only never-recomputes test-pinned; 409 `STALE_PROPOSAL` as `normalFlow: true`; descriptors flipped live, `HARNESS_TOOL_REGISTRY_VERSION` v9→v10 `pec-proposal-tools-live`; catalog regenerated; apply-name absence pinned); evidence `400c7625e` (`PEC_2026-07-06_BRIDGE-evidence-01/` — hermetic scratch rehearsal by direct handler invocation, propose→validate→refresh + live 409 recovery; demo-cast admin accept/apply disclosed per act with **`force: false` on both applies, `force=true` nowhere** — driver hard-codes it; proposals mirror `OP_2026-07-06_BRIDGE_rehearsal_IPR-0001-0002.md`; SHA-256 manifest 19/19; scratch DB deleted; **live-LLM demonstration deferred — no `ANTHROPIC_API_KEY` — stated plainly**); repin `b1f175a95` (D-APP-48 pull contract → rebased source `7353aa16a`, validator pass re-run post-rebase).
  - Gate outcome: executed under the recorded pre-ruled ruling inside its expiry window; zero pec source change (`git diff --stat -- projects/pec/` empty on the app-dev commits); no accept/apply/force tool-reachable; visibility bound structural (only the four mapped endpoints); mutation basis untouched (scratch only). With P1+P2+D-PEC-17 merged, D-T0-19 phases P1–P3 are executed; P4 (owner-at-the-screen weekly rehearsal) remains the lane's open rung. Self-merge of this PR under Receipt 32 item 4c with the full check set green at the final SHA.
  - Checks (at this PR's final SHA): profile validator — inapplicable (profile untouched); self-check pass no unexplained baseline shift; full `tools/` pytest pass (747/1 environment-conditional skip class, as Receipts 33/34); pec `npm run typecheck && npm test && npm run build && npm run drill` pass; app-dev typecheck + full vitest 641 passed/4 skipped (skips = the opt-in live-integration file, run separately: `PEC_BRIDGE_IT=1` → 3 passed) + catalog `--check` + contract-deps + secret-scan + premerge pass (**fully keyless — the item-4c key exclusion not needed at tranche level**); pull-contract validator pass (post-rebase repin); coord-check on the committed range; `git diff --check` pass; CI `harness` green on the PR. Pre-existing, not caused here: app-dev `instruction-root:integrity` fails identically at base (missing packaged desktop bundle; stash-verified).
  - Parked lanes: P4 end-to-end weekly rehearsal (owner at the screen — the bridge lane's remaining rung); sidecar SDK-engine enablement (owner act: dependency + key); 272-item run on pilot-scratch (lawful, owner-clarified); D-PEC-13/14/15 preparation (item-4-eligible); live-LLM demonstration (deferred, no key); pilot-DB/real-basis row; risks upload owner-side — carry forward.

- **2026-07-06 — Receipt 36** (D-PEC-10 272-item real-data triage run executed on the standing scratch basis).
  - Start: `c0a3214cf` (`origin/main` after PR #92); branch `codex/pec-dpec10-triage-272`; tree clean at discovery; no `tools/**` change since Receipt 35 → discovery self-check only (pass, no baseline shift). No ruling newer than Receipt 35 in either register. The Receipt-32 item-4 pre-ruling was checked and is EXPIRED by its own terms ("this session only; expires at session end or 24 hours after this direction, whichever comes first") — this later session runs with no pre-ruling and no self-merge; every gate stops for the owner.
  - Owner direction of record (2026-07-06, launcher, Ryan Tufts, verbatim): "Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`. Read `{REPO_ROOT}/_DomainEngines/pec/LOOP_INIT.md` and follow it: pursue the loop's inherent goals — recorded in its standing plan — as far as live authority permits." Per-run steer of record (one line each, Receipt-32 pattern): orchestration = dependency-ordered tranches with explicit write fences, parallel where disjoint, main loop holds shared surfaces/gates/pre-ruling records/merges; subagent models = opus for discovery/checks/breadth, fable-high for planning/adversarial verification/governed execution, fable-low for mechanical execution only.
  - Executed pointers: `_DomainEngines/pec/PEC_2026-07-06_DPEC10-triage-01/` (MANIFEST + TRIAGE_RULES frozen pre-disposition + SUMMARY + DISPOSITIONS.csv + 31 artifact files; SHA256SUMS 35/35 verified) — the D-PEC-10 O-A ruled mechanism on its existing scratch basis (`pilot-scratch/db/pec-scratch-import.db`, retained per its standing role; pre/post backups hashed under `pilot-scratch/backups/{pre,post}-triage-20260706/`), visibility per D-T0-20 O-B (whose ruling text discharges the Scope-note-4 confirmation; the expired item-4 pre-ruling is load-bearing nowhere).
  - Results: 272/272 triaged to the pre-frozen rules (zero plan-vs-actual mismatches) — 2 converted→work item (WI-0001/0002, content verbatim-traced, anchored to their unique pre-scan deliverable matches), 0 converted→decision (no source row names an authority; `authority_id NOT NULL`; F-PEC-2 — decision-shaped items went to the owner list), 0 duplicate, 255 parked with WF-9 grounds (198 are monthly level-of-effort plan rows with no conversion family), 15 left un-dispositioned for the owner with one-line reasons. All 516 run-window history rows (2484–2999) are the agent person (personId 46, `is_admin=0`, coordinator, provisioned fresh script-side per the rehearsal-01 basis-prep precedent; ephemeral credential disabled post-run; the retained role grant is an owner-revocable leftover). Read path disclosed in the MANIFEST: all workflow acts via the live HTTP API as the agent; pre-run scans/rule-grounding via read-only sqlite over scratchpad copies (pre-server, pre-login), content classes inside D-T0-20 O-B (i)/(iii)/(iv).
  - Verification: two-lens adversarial pass on the pack (fable, high effort) — fact PASS (counts, hashes, WF-9 notes on all 257, boundaries all DB-verified; two MINOR disclosures applied pre-publication: the server's schema auto-migration adding the empty `import_proposal` table to the standing instance; the zero-byte work-items export) and governance PASS ("a receipt may record this run as executed lawful discharge of the 272-item triage lane"). SUMMARY observations 1–4 are candidate register rows only, not recommendations of record.
  - Gate outcome: the 272-item triage lane is executed as scratch-basis evidence — no real-record durability (pilot DB remains owner-side, "Another time"); no accept/apply (none arose), no `force`, no import proposal, no pec source change, no tier-0 act, no self-merge — STOP at owner merge of this PR. A companion packet-slate PR (D-PEC-13/14/15 → AWAITING_RULING) follows stacked on this branch with its own receipt.
  - Checks (at this PR's final SHA): self-check pass no baseline shift; full `tools/` pytest pass; pec `npm run typecheck && npm test && npm run build && npm run drill` pass; coord-check on the committed range pass; `git diff --check` pass; profile validator inapplicable (no profile touched).
  - Parked lanes: owner merge of this PR; owner review of the 15 owner-left items and 255 parked dispositions (his screen, his pace); D-PEC-13/14/15 rulings once the stacked slate PR is presented; P4 weekly rehearsal (owner at the screen); sidecar SDK-engine enablement (owner act: dependency + key); pilot-DB/real-basis row; risks upload owner-side; live-LLM demonstration (no key) — carry forward.
