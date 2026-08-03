# Launch brief — C1 CHANGE open-PR closeout

- Parent: `HELP_HUMAN`, run `ROOT_FOUR_LANES_2026-08-02`, plan v3.
- Role: `CHANGE`; load `agents/AGENT_CHANGE.md` in full.
- Objective: publish the validated current stop-state to a new open PR without
  merging, preserving the owner's merge gate and leaving the PR available for
  later ruled follow-up commits.
- Accepted fan-in: C0 complete; S1 `BLOCKED_AT_GATE_1`; W1 `HELD_AT_N0`; H1
  locally ready for hosted CI; E1 complete at owner-decision hold. No semantic
  stop state may be upgraded by Git closeout.
- Scope: stage only this session's Root workplan/receipt updates, shared run
  records, SCA-003 Gate-1 package, DEL-02-06 planning activation, Pi evaluation,
  and G4 CI implementation/test/manifest paths. Refuse any unrelated path.
- Checks: candidate whitespace, JSON parse, `git diff --check`, focused G4
  positive/negative proof, full `tools/validation/`, and live G4 schema mode.
- Git sequence: commit the coherent candidate on the current local branch;
  once clean, create/switch `codex/root-four-lanes-20260802` at that exact
  commit; push only the new branch; open a PR to `main`. Do not push the old
  branch, merge, rebase, reset, amend, force-push, delete, or rewrite history.
- PR body: state every lane's exact gate status, validation, derivative status,
  owner decision queue, Task Management closure exclusion, and owner merge
  gate. Do not claim G4 hosted evidence until checks complete.
- Return: commit and pushed head SHA, branch/upstream, PR URL/number, changed
  paths, check state, remaining blockers, and clean/dirty state.
