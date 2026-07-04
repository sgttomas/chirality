# PEC Loop Receipts

> **Epistemic status: derivative handoff ledger — not authority.** Append-only.
> Current state is always re-derived from the live tree, the decision registers,
> the pec profile (staged path; DRAFT until owner Gate 2), git history, and the
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
