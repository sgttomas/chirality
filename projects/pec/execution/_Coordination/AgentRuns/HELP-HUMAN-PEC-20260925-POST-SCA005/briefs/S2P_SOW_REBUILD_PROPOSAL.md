# Brief S2P — prepare the S2 Scope of Work rebuild packet (provisional D-PEC-100) (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S2. Role: WORKING_ITEMS (Type 1), with `Workflow: chirality-root:bundled:workflow:scope-of-work` resolved from `workflows/index.json` (record identity and hashes; note the edition now carries `MODE=REVISE`, Root PR #955). Model steer: `claude-opus-5-5`, high reasoning, for you and every child.

## Why and authority

The owner directed on 2026-09-25 (`D-PEC-94`): "You can continue with all the open work you identified." Graph node S2 (rebuild class outside the S4 set) is READY for packet preparation. `projects/pec/AGENTS.md` fences every `ScopeOfWork.md` behind an owner-ruled D-PEC packet with exact paths, acts, verification and rollback. You prepare that packet; you write no production file. HELP_HUMAN publishes it in `_DECISIONS/` with its register row and brings it to the owner. The number `D-PEC-100` is provisional.

## Scope

- **Deliverables (7):** DEL-01-01, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07 and DEL-01-06 (G1, the registry act, merged as PR #950). Confirm against the S2 row and the SCA-006 accepted §7.1 AFFECTED set that none belongs to S4; report any that does.
- **What "rebuild" means here:** bring each contract current with decomposition revision 1.6 (`_Decomposition/_LATEST.md`), PRD v2.4, the SCA-005 feed model and the ruled `D-PEC-96` registry (schema v2, the closed three-profile vocabulary, PEC's row migrated), and the D-PEC-99 retirement (no `## Remaining` surface exists). Read graph row S2 in full: the parser carry-forward (CON-001 cases for RETIRED, node states, run tokens), and for DEL-01-06 the stale "declares `remaining-loop` now" text, which in the decomposition waits for a later scope change but which the DEL-01-06 contract must state as the current registry row.
- **Carry-forwards the packet must absorb exactly:** the `D-PEC-99` exhibit Part B items for S2 — DEL-02-07-REM-001, -002, -003, -004 — verbatim from `_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`, each with its gate. Show where each lands in the DEL-02-07 contract.
- **Method choice as an owner option.** Root's `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` adds `scope-of-work` `MODE=REVISE`; the owner defers adopting new modes in PEC. Recommend the method (for example `MODE=INIT` rebuild on the D-PEC-98 precedent, or `REVISE` per deliverable), and put the choice to the owner; do not assume adoption.
- **Lifecycle.** Say exactly what the method does to each `_STATUS.md` and put any transition to the owner. Five of these are `INITIALIZED`; check each one's state. No CHECKING deliverable may be touched; if one is in scope, stop and report.

## Produce (published as a PR; nothing applied)

Work in your own isolated git worktree on branch `claude/pec-s2-sow-rebuild-proposal` from fresh `origin/main`. Write only under `projects/pec/execution/_Coordination/PEC_SOW_REBUILD_S2_PREP_2026-09-26/` (default-writable) plus your return `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S2P_SOW_REBUILD_PROPOSAL.md` and a copy of this brief under `…/briefs/`:
- `DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md` in the D-PEC-96/98/99 format: provenance, what preparation found, options (A recommended; alternatives such as per-deliverable splits), exact product grant (paths, preimage hashes, postimage hashes), bound generation method (an act script like `apply_d98.py`: pinned preimages, temp-write-and-rename, rollback on failure, write-set inventory, refuses a second run), finite verification (validator `PASS format=SOW_V1` each; checklists; boundary owners; a two-sided quote verifier; commit-anchored state-claim checks; strict registers identical before and after under D-GOV-48; harness and receipt validators identical; containment), independent verifier, administrative grant, rollback, limits, owner questions.
- The candidate contracts, the act script and its fault-injection test, the quote and state-claim verifiers, check outputs and `SHA256SUMS`.

Run the checks on a `git archive` export or scratch copy, never the checkout. Run `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) with `exact-correction-preparation` on every target. Before returning, dispatch one fresh read-only `pec-reviewer` (opus) for the method's `MODE=VERIFY` on every candidate plus a packet review (claim grounding, quotes, Part B fidelity, lifecycle, limits); loop until nothing blocks; save each verdict in the prep folder. Commit and push early; open a PR against `main` (body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`; commits end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`); do not merge. Report, do not repair, any "Update the PR base" failure.

## Limits

No production write: no `ScopeOfWork.md`, `_STATUS.md`, `MEMORY.md`, register, dependency, context, reference, decomposition, `v2/**`, PRD, `AGENTS.md`, `_DECISIONS/**`, work graph, `docs/**` or foreign path. No CHECKING, ISSUED or acceptance claim; do not ask the owner about CHECKING. No CON item resolved by assumption.

## Return

PR URL and head; draft path and hash; candidate hashes per deliverable; recommended option and method choice; lifecycle answer; Part B landing table; check results; verifier verdicts; owner questions; anything unresolved.
