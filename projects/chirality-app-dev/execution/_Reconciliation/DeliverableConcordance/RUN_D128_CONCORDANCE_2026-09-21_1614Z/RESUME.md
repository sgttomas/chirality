# RESUME — RUN_D128 (for a cold HELP_HUMAN session)

1. `git fetch origin`; read `RUN_BASIS.md` (frozen basis, authority map, fences) and the
   D-APP-128 register row cell (open/closed visibility).
2. Read `RUN_STATE.jsonl` (append-only; last line per unit wins) and the AgentRuns
   `WORK_GRAPH.json` beside the owner direction.
3. Recreate the frozen reading tree if absent: `git worktree add --detach <scratch>/frozen-00115c719 00115c71931bcae79909602d653740d3bb72dfa1`
   (outside the repository; never commit its path). Gate transcripts are already recorded.
4. For any unit whose state is `dispatched` without a matching `returned`: check its output
   folder; if outputs exist and `_scripts/validate_ledger.py` passes, record `returned`;
   otherwise re-dispatch from its stored brief (`BRIEFS/`, hash in RUN_STATE).
5. Respect the owner's concurrency cap (16 including Agent 0 unless changed) and drain rather
   than launch when session usage is low.
6. Current phase and next gate: see the last `phase` line in `RUN_STATE.jsonl`.
