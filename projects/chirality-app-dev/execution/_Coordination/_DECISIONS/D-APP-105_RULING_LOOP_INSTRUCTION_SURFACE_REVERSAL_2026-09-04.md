# D-APP-105 — Loop instruction surface: reversal of the D-APP-61 / D-APP-64 workplan-centred arrangement

Status: `RULED — owner direction, in-session 2026-09-04`

DecisionID: `D-APP-105`

Date: `2026-09-04`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

Implementing change: PR #706 (`loop/LOOP_INIT.md` rewritten as the generic
loop; `loop/WORKPLAN_2026-09-04_app_dev_loop.md` minted as a narrowing
overlay; `WORKPLAN_2026-09-03_app_dev_loop.md` preserved unchanged).

## Exact owner direction

Given in chat, 2026-09-04, after reviewing PR #706 and its stated conflict
with D-APP-61 and D-APP-64:

<!-- BEGIN OWNER DIRECTION VERBATIM -->
I made a mistake with D-APP-61 and 64. I don't recall why I did that but it goes against what I've been trying to get working through loops acting in the manner we've now defined here.

Merge the PR #706 unless you want you document the reversal of D-APP-61 and 64 first (we should attend to that matter before finishing this tranche)
<!-- END OWNER DIRECTION VERBATIM -->

Earlier in the same session, on the loop's shape (paraphrase of the owner's
direction, recorded in PR #706's description): `LOOP_INIT.md` is the generic
loop; the init prompt is environment setup and orientation; a workplan is
optional and, when used, narrows and orders; agents must be able to discover
work from the deliverables' `## Remaining` sections alone.

## Effect (agent reading of the direction; the owner may amend by reply)

Reversed, effective at the merge of PR #706:

1. **D-APP-61 M2-A placement rule.** The clause that the workplan is "the
   project's single development-loop instruction surface" and that
   `LOOP_INIT.md` is a thin entry that hands off to it. From this ruling,
   `loop/LOOP_INIT.md` is the loop's instruction surface: protocol, posture,
   fences, evidence contract, checks, and pointer index live there.
2. **D-APP-64 mandatory-plan semantics** (§8 workplan re-mint as the carrier
   of protocol; §9 loader as the gate before Step 0). A workplan is an
   overlay that narrows and orders. It never holds a `Remaining` item, never
   widens authority, and never relaxes a fence or gate. Discovery does not
   depend on it.

Retained (not touched by the direction as read):

- D-APP-64 §3, the owner's standing approval for reasoned selection, and
  §5's contract (fast-reject boundary, selection method, attribution
  schema). PR #706 carries these into `LOOP_INIT.md` Steps 1 to 3 unchanged.
- D-APP-64's committed-`HEAD` reading of a plan, kept in `LOOP_INIT.md` §2
  as the way a plan is read when one exists.
- D-APP-61 M1-A (HELP_HUMAN launcher entry), M3-C (model convention
  re-homed to project `AGENTS.md`), M4-A (historical "§7 defaults"
  mapping), M5-A (structural-duplication validator contract).
- Supersession-only editing of ruled workplans: a change is a new dated
  file.

Nothing here changes any F-APP fence, the receipts contract, the
decision-latitude instrument (D-APP-60), or any deliverable's scope.

## Residual (own row, per the residual-work convention)

`tools/validation/validate_instruction_entrypoints.py` required at least one
`WORKPLAN_*.md` per project, and `LOOP_INIT.md` §2 stopped before Step 0
when the loader found none. Recorded as `D-APP-106`. The owner then expanded
this tranche's write scope to Root in-session (2026-09-04, verbatim: "Expand
you write scope to Root also"), and D-APP-106 was applied in the same PR:
the validator no longer reports a missing workplan (test
`test_accepts_project_without_workplan` covers the case), and the loader
runs on deliverables alone when no committed plan exists.

## Attribution

The direction above is the owner's. The reading of its effect and the
retained/reversed split are the agent's (Claude Fable 5.1 acting as
HELP_HUMAN), recorded at the owner's instruction before merge. The merge of
PR #706 is the owner's act; no ruling is attributed to the owner beyond the
verbatim text.
