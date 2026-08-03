# Task Management session init prompt — root register

Launches one `TASK_MANAGEMENT` session bound to the root Action Item
register. Paste-ready as written; replace `<none>` with a per-run steer to
narrow the run (e.g. `deferral review only`, `triage of the open rows`, or
`staleness pass only, no harvest`). In a full generational Task Management phase, run the child-loop
sessions (`projects/*/init/taskmgmt-init-prompt.md`) and land their closeouts
before this one, so root's cross-loop trigger and closure-echo evaluation
sees every sibling closeout.

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_TASK_MANAGEMENT.md` and follow it in full.

Act as `TASK_MANAGEMENT` for the root loop. Register home:
`{REPO_ROOT}/execution/_Coordination/_TaskManagement/`. Write scope is that
register home, routed drafts shipped solely through closeout, and the single
closeout receipt appended to the owning loop's receipts surface per
`AGENT_TASK_MANAGEMENT.md` §Closeout.

Run the generational pass, each step gated on my rulings before the next:

1. Mandatory federation preflight; report per-register status counts.
2. Mode: candidate harvest — full PRD §5.1 sweep: `taskmgmt scan` plus a
   manual sweep of the marker classes the helper does not implement (e.g.
   `TM-CANDIDATE:` lines in notices and reports). Present the Candidate
   Harvest Report; await my promotion rulings; apply exactly what I rule.
3. Mode: deferral review — the full DEFERRED population, including rows
   minted in step 2. Present the classification report; await my rulings;
   apply them.
4. Run `python3 tools/taskmgmt/taskmgmt.py archive --register
   execution/_Coordination/_TaskManagement/REGISTER.csv` (a no-op when no
   rows are CLOSED); validate the live register and REGISTER_CLOSED.csv; run
   a final federation pass and quote its status counts as closeout evidence.
5. Closeout: assemble this session's durable products on a branch — the
   register and archive, reports, and any ruled routed notices with
   reciprocal citations (inbound SHA, row ID, evidence refs); append one
   closeout receipt to `execution/_Coordination/LOOP_RECEIPTS.md` per
   `AGENT_TASK_MANAGEMENT.md` §Closeout. The PR body
   carries the closeout record: every row changed and the ruling it cites,
   archive counts, status totals, federation evidence. Open the PR; do not
   merge — my merge is the gate. Report the PR number and final head SHA,
   then stop.

Never write a foreign register. Where a ruling requires another loop's
action, the response is a draft notice shipped only in the closeout tranche
under my gate.

Steer (this run): <none>
</init-prompt>
