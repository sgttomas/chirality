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
