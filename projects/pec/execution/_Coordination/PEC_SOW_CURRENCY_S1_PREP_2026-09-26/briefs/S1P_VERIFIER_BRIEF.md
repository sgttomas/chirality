# Brief S1P-V — independent MODE=VERIFY of S1 candidates (fresh read-only pec-reviewer, TASK)

Parent: WORKING_ITEMS manager of brief `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1P_SOW_CURRENCY_PROPOSAL.md` (SHA-256 `9718ab73…9b17`), node S1, provisional `D-PEC-104`. You authored nothing in this packet. You are read-only on the repository: never edit, stage, commit or delete a repository file. Model steer: `claude-opus-5-5`, high reasoning.

## Where things are

- Worktree `REPO` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-s1-sow-currency` (branch `claude/pec-s1-sow-currency-proposal`; `origin/main` merged at `3488a236a`).
- Prep folder `PREP` = `REPO/projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/`: `candidates/…/ScopeOfWork.md` ×12, `quotes/`, `claims/`, the verifiers, `apply_s1p.py`, `evidence/run_main/` (the manager's full run: OVERALL PASS), `briefs/S1P_DRAFTER_BRIEF.md` (the drafting rules; read it — it states what "current" means, the common edits C1–C9, the correction-only DEL-03-06 rule).
- Prior contracts: the production files at `origin/main` `125cfacc1` (the observation commit; the S2 `D-PEC-100` postimages are on main there; prior S2 bytes at `9cf863697`).
- Exhibit Part B: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` (`69b646f8…f45e`), node S1 items DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004, DEL-04-05-REM-003.
- Method: `workflows/scope-of-work/WORKFLOW.md` (`84dadde4…bc2b`) and `resources/checks.md` (`44ab41ac…f188`); `MODE=VERIFY` runs the mode-applicable subset (items 1, 3, 4, 8, 9, 13, 16, 18–21).

## Owner-direction constraints relayed by HELP_HUMAN (binding on the candidates)

- DEL-01-03 and DEL-01-05 are `IN_PROGRESS` with produced artifacts verified against their current contracts: their revisions must be **currency only** (basis pins, stale quotations, stale state claims); no REQ, AC or VER that produced artifacts or their recorded evidence were checked against may change; every externally cited ID is kept (`DEL-01-03/CON-001` meaning, `DEL-01-03/REQ-003` verbatim). Anything that would change the verification basis must be an open item, not a change.
- DEL-03-06 is the REM-004 correction only; its other stale text is out of scope (to be disclosed, not changed).
- Nothing may mention or prompt about CHECKING.

## Run (on your own `mktemp -d` exports under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`; delete only inside directories you create; never write into the scratchpad root)

1. Re-run for your assigned deliverables: `validate_scope_of_work.py`, `derive_review_checklist.py` (twice, byte-identical), `check_boundary_owner_resolution.py --show-not-checkable`, `PREP/verify_s1p_quotes.py --tree <export with all 12 candidates copied in> --gitdir REPO --prep PREP --observation 125cfacc1 --obs-exempt DEL-03-06 --only <DEL…>`, `PREP/verify_s1p_state_claims.py --only …`, `PREP/check_qualified_ids.py`.
2. Diff each candidate against its prior (`git show 125cfacc1:<path>`). For every hunk judge: is it true at the commit it names (or at `125cfacc1`)? Is every quotation verbatim at its source (spot-check beyond the JSON too: find quotations the JSON omits)? Does it add scope beyond the ledger rows, `Deliverables.csv` row and PRD v2.4? Are kept IDs' meanings kept and retired IDs not reused? Is every open item a TBD/CON, with no CON resolved by assumption? Is any Remaining section presented as a surface? Any CHECKING mention? Anything stale left in text the candidate otherwise touched?
3. Part B items (where assigned): the replacement strings land byte-exact; directions are met by the authored wording; the gate is respected (the item's loci only for that item; other changes come from the S1 currency causes).
4. For DEL-01-03/DEL-01-05: confirm REQ/AC/VER byte-identity with the prior and that nothing changes the produced artifacts' verification basis.

## Return

A verdict: `PASS`, `PASS WITH NOTES` or `FAIL`, per deliverable and overall. Number each finding (V<n>-<k>), classify it `BLOCKING` (must change before the owner sees the packet: a false statement, a non-verbatim quotation, scope added, an ID meaning broken, a constraint above violated, a failed check) or `NOTE`, cite file:line and the evidence command. List the commands you ran with exit codes and result lines, and the source hashes you relied on. Do not repair anything.
