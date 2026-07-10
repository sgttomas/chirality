# App-Dev Loop Receipts

> **Epistemic status: derivative handoff ledger — not authority.** Append-only.
> Current state is always re-derived from the live tree, the decision register,
> the owner-adopted queue plans, git history, and the deterministic checks; on
> any disagreement those sources govern (K-AUTH-1). A receipt records only what
> tools cannot re-derive: owner directions given outside governed artifacts,
> gate outcomes and their rationale, deltas found in dated maps (which are never
> edited), and pointers to the authoritative artifacts created elsewhere.

## Rules (fixed — part of the loop protocol)

1. **Pointer, not narrative.** Prefer paths, PR numbers, commit SHAs, decision
   IDs, and queue-item IDs. Work history lives in commits, PRs, decision
   records, plan rows, and project-local files — never here.
2. **Owner directions verbatim.** Any owner direction not otherwise captured in
   a governed artifact is quoted word-for-word with its date. This is the one
   place chat-only directions become durable.
3. **Measurements as check summaries only.** `self-check pass; harness pytest
   pass; typecheck/vitest/build gates pass` is the maximum — counts and tables
   belong in plan rows and evidence artifacts.
4. **Stale-map deltas as one-line pointers.** Dated assessments and plan files
   are never edited to match reality; a receipt line says what disagreed and
   where to verify.
5. **Gate outcomes with reason.** stopped / executed / awaiting owner — and
   why, especially no-op outcomes ("all remaining work is owner-shaped"), so
   the next loop neither rediscovers the stop nor invents work around it.
6. **Capped.** Roughly 6–12 lines per receipt. If it wants more, the detail
   belongs in a decision packet, PR description, or project-local record.

## Receipts

- **2026-07-04 — Receipt 0** (loop creation).
  - Start: local `main` synced with origin at the PR #54 merge; loop artifacts
    authored on branch `claude/pec-init-prompt` (PR #55).
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "I want the
    new init-prompt to be the current leaner convention, not this older one.
    All projects should have the current development loop structure and
    workflow, and therefore same type of init prompt." — with "Dedicated loops
    per project" selected over pointing at the shared bridge loop.
  - Artifacts created: `projects/chirality-app-dev/loop/{LOOP_INIT.md
    (byte-identical copy of the generic loop init), this WORKPLAN, this
    ledger}`; `projects/chirality-app-dev/init/init-prompt.md` rewritten to the
    lean launcher pointing here.
  - Deltas (live tree wins): the legacy entry
    `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` remains in place as a
    dated historical map — status claims inside it (active queue, operating
    mode) are not refreshed by this loop's creation; the live queue state is
    re-derived from the register and plan rows at Step 0.
  - Gate outcome: structure-only tranche; no app-dev queue item selected, no
    register change. First working iteration starts at the next launch's
    Step 0.
  - Parked lanes: owner rulings on the app-dev register's open rows (re-derive
    from `execution/_Coordination/_DECISIONS/_REGISTER.md` at Step 0).

- **2026-07-10 — Receipt 1** (inspection-orphan remediation resumed).
  - Start: clean detached `199c6d545` = `main` = `origin/main`; branch
    `codex/app-dev-orn-remediation`; newest prior receipt Receipt 0.
  - Owner steer (2026-07-10, in-session, Ryan Tufts): "Fan out and fan in with
    subagents where warranted."
  - Live gates: D-APP-01..52 all RULED; D-APP-51/52 already consumed; no open
    app-dev register row. Active queue remains
    `plans/PLAN_2026-06-21_inspection_orphan_remediation.md`.
  - Executed: ORN-02 `71fff1277`; ORN-03 `ed54bbf94`; ORN-04 `658802bd5`;
    ORN-05 `40afda52c`; ORN-07 `2eef3d09c`; ORN-08 `dc9c50ca6`; ORN-09
    `24f40d5d8`; ORN-06 dropped as already closed.
  - Gate outcome: ORN-01 BLOCKED — live CI is repo-root
    `.github/workflows/harness-premerge.yml`, outside D-APP-39 app-dev-only
    staging authority and under newer owner-directed manual-only posture
    `48f622c93`; explicit root-workflow direction required.
  - Deltas: `_LATEST.md` still says D-APP-45 AWAITING_RULING; live register says
    D-APP-45..52 RULED. Standing workplan F-APP-1 wording predates D-APP-44;
    live ruling/active queue govern.
  - Checks: self-check pass; full practitioner-harness pytest pass; frontend
    focused/full Vitest pass; typecheck pass; authority corpus status pass; git
    diff check pass.
  - Parked/next: PEC P4 requires owner-at-screen; ORN-10..13 remain VERIFIED /
    READY; issuance/release/apply/live-binding hard fences unchanged.
