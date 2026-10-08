# Init prompt for the next T3 session (ephemeral, 2026-10-08)

The owner pastes the block below as the first message of the new session, started in the T3 integration worktree (see [the handoff](HANDOFF_2026-10-08_TO_NEXT_ROOT.md)). It is `projects/chirality-piping/init/dev-loop-init-prompt.md` with the steer filled in. Only the steer is specific to this run.

```
<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to
`{REPO_ROOT}/projects/chirality-piping`.

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.

Act as `HELP_HUMAN` for `{WORKING_ROOT}`.

Read `{WORKING_ROOT}/loop/LOOP_INIT.md` and follow it within the owner's
steering and live authority.

Steer (this run): Continue T3, numerical integrity, precision and scale, of the piping undertaking `HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION`. Act as its ROOT (Agent 0), under the owner's standing delegation for T3 ("carry on with T3 in the manner you see fit"), and apply `coordinated-knowledge-work` in proportion to the work.

1. This session runs in the T3 integration worktree, so `{REPO_ROOT}` is that checkout, on branch `codex/piping-numerical-integrity-20260926` (NUM). Its maintained source equals main's, and it carries T3 records that are not yet on main.
2. The work graph is `{WORKING_ROOT}/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md`. Read its T3 row and its "T3 current route" section. They carry T3's route, the owner-held choices, the decisions and rulings in force, the next IDs and the next safe action.
3. T3's records are in `{WORKING_ROOT}/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/`. Read its `HANDOFF_2026-10-08_TO_NEXT_ROOT.md` once, for what was in flight and the machine-local host details. Read other T3 records when the work needs them.
4. **First, verify the host, the heads and the work in flight:**
   - the memory guard is running, and the lock slots are free or held by live jobs;
   - the worktrees the note lists;
   - whether main moved;
   - the free disk space;
   - **the work in flight at handoff:** RV113's held SR-PY addendum (being redacted by its author before first commit) and PR #1118 (the private-term check) under review. Verify each from disk and GitHub.

   Then give the owner a short status that references the graph.
5. **Then follow the graph's next safe action:**
   1. commit RV113's SR-PY addendum once both screens show no hit; merge #1118 when its review and CI pass;
   2. make I4 (RV113 has confirmed all three readers), and rule RV113's three items;
   3. B1's SC (`BRIEFS/B1_SC.md`), then SQ, SG, SB and SK, then PR-B1;
   4. J0, and B2/B3 (B2-C is final for J1);
   5. B7, B8, then S-I2, F2b and F3, with S-I1 alongside.
6. **Hold to these T3 practices.** Their basis is in the T3 rulings the graph lists.
   - **Host jobs:**
     - heavy builds and tests run on this Mac only while the memory guard runs;
     - they use the four lock slots: cargo through `t3_cargo.sh`, other heavy commands through `t3_slot.sh`;
     - T3 may use up to 64 GiB of its own, and jobs start only under the start gate;
     - each agent runs one heavy job at a time, one wait per job, and never signals another job;
     - the product's M stays at or below 12 GiB.
   - **DEC-025, native and solver-at-scale jobs:** TASKs run none of them. ROOT runs DEC-025 with `run_dec025.sh` through `t3_exclusive.sh`, and a run counts only when its `meta.txt` ends with `ALL-DONE`.
   - **Before any freeze,** run the full 40-manifest suite.
   - **Product PRs** take T3's full gate set (RR "T3's gate set and Git rules, consolidated after the handoff was made ephemeral"):
     - an independent complete-diff review;
     - hosted CI with the full-SHA dispatch;
     - GEN-8;
     - an exact-head Mac DEC-025 against a fresh main baseline;
     - Pass B where the D1 call graph is touched.

     They are cut compactly from main, and merged with `--merge --match-head-commit`.
   - **Never merge NUM itself into main,** because its history holds redacted originals.
   - **Records reach main through records-only PRs,** after each main merge and before any handoff:
     - cut the PR from main, taking NUM's execution files;
     - screen with `WT/tools/t3_host_screen.py` and, once #1118 merges, `tools/validation/validate_private_terms.py --from-host --terms-file WT/tools/t3_host_names.private.txt`; a hit stops the commit until ROOT has read it;
     - run main's leak validator, and GEN-8 on the exact head;
     - gate it with the automatic CI and an independent review;
     - squash-merge it with `--match-head-commit`.
   - **Sealed files are never replaced in place.**
     - Redacting a sealed record is the owner's call.
     - Briefs and living documents never spell out screen patterns, machine paths or host names.
     - Pytest junit output reaches records only after its `hostname` attribute is removed.
   - **IDs and returns:**
     - give implementers and reviewers separate, fresh IDs (the next are I100 and RV120);
     - agents from the previous session cannot be resumed;
     - verify every return yourself.
   - **Owner-held choices:** prepare the decisions the graph lists as owner-held, and never decide them.
   - **After merges,** remove regenerable build output with `t3_cleanup.py`: gather, then plan, then apply.
7. Keep the graph's T3 section current as the work moves, in the same commit as any ruling that changes a position. At a handoff, write only an ephemeral note, plus a steer like this one.
</init-prompt>
```
