# D-PEC-98 act — handoff state

Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S3 (the act),
2026-09-26. Actor: WORKING_ITEMS (Type 1), host-reported model `claude-opus-5-5`
(role and `high` effort instruction-asserted). Branch
`claude/pec-d98-first-sows-act`, PR #958 against `main`. Not merged; merge is
HELP_HUMAN's under the standing Git authorization after independent review of
the actual candidate.

## State

| Item | State |
|---|---|
| Question-4 re-pin onto `189f205ff02df4111b33c20be441ce06e65ada7a` | done; checks pass (`REPIN.md`) |
| Act (option A): two `ScopeOfWork.md` created by the re-bound `apply_d98.py`, run once | done; 2 created, 0 modified, 0 removed |
| Finite verification | done; all rows pass (`VALIDATION.md`) |
| Independent verifier (`MODE=VERIFY` plus re-pin checks) | `PASS WITH NOTES`, no blocking defect (`VERIFIER_VERDICT_01.md`) |
| Add-on S: `OPEN → INITIALIZED` for DEL-02-08 and DEL-02-09 by a separate generic-shell TASK | done; postimages equal the proposal's table (`S_TASK_RETURN.md`) |
| Add-on M: the two `MEMORY.md` files | **not done, by design**: written at the undertaking's closeout (graph node M1) with the `{D}`, `{PR}` and link slots fixed then |
| CON-005 | open, routed to the next PEC scope change (owner ruling) |

Lifecycle now: DEL-02-08 and DEL-02-09 `INITIALIZED`, each holding a valid
`SOW_V1` contract. No CHECKING, ISSUED, REVIEW gate, acceptance, registry act or
`CON` resolution occurred.

## Written paths (SHA-256)

| Path (relative to `projects/pec/execution/`) | SHA-256 |
|---|---|
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` (created) | `2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` (created) | `eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_STATUS.md` (S; preimage `d80800a4…0eef`) | `4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_STATUS.md` (S; preimage `3e14313c…d768`) | `e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056` |
| `_Coordination/SOW_INIT_D98_2026-09-26/**` (this run root) | per `MANIFEST.md` |
| `_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S3A_D98_SOW_ACT.md` | `d9a013489faac17c9a9f2ef90c0f5039e061ab098d8bde0e43defc7b65486291` |
| `_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S3A_D98_SOW_ACT.md` | the manager's return (hash in the final commit) |

## For the caller to resolve

1. **Owner disclosure — stale "decomposition pin" label (verifier note 1).**
   DEL-02-08 CLM-013 (line 111) still says "at the decomposition pin
   `c9e5cd87d`"; after the re-pin the decomposition pin is `189f205ff…`. The
   hashes it states at `c9e5cd87d` are correct. Lines 29–31 of both contracts
   ("…did not exist at `c9e5cd87d`") remain true but no longer say that
   `c9e5cd87d` is the former pin. Question 4 allowed only three moves, so the act
   left these bytes. A one-word correction ("former" / "prepared") needs a later
   owner-authorized revision.
2. **Owner disclosure — the observation clause's locus list is not exhaustive
   (verifier note 2).** The re-pinned clause lists the register, decomposition
   and PRD loci that `verify_d98_quotes.py` checks. It omits two other quoted
   loci: each contract's `Deliverables.csv` `AnticipatedArtifacts` quote and
   decision-log `DL-4` "one per feed kind". The verifier checked both by hand:
   verbatim at `189f205ff` and `53145aaeb`. No contract statement is false, but
   the list reads as complete. This is wording the manager authored inside the
   permitted observation clause; the act script may run only once, so it is not
   repaired here. It can be completed in the same later revision as item 1.
3. **Base currency.** `origin/main` advanced after the act to `cb85f85d1` (Root
   PR #956, software-prd registration; under `projects/pec` it adds only
   `NOTICE_2026-09-26_SOFTWARE_PRD_REGISTRATION.md`, and it touches no pinned
   file, tool or `scope-of-work` file). The branch is based on `6b48b6f26`. If CI
   asks to update the PR base, that is reported, not repaired here.
4. **Parallel D-PEC-99 act.** Not merged when this act finished. If it merges
   before PR #958, rerun `verify_d98_quotes.py` and `verify_d98_state_claims.py`
   on the updated base (DEL-02-09 CLM-012 quotes two `projects/pec/AGENTS.md`
   phrases); stop and report if a quoted locus changed.
5. **Method edition.** The proposal bound `scope-of-work` `WORKFLOW.md`
   `d616865a…fbd8b` (the edition at `189f205ff`, which this manager loaded).
   Root PR #955, merged at `6b48b6f26` before the act, added `MODE=REVISE`
   (`WORKFLOW.md` now `84dadde4…bc2b`). INIT text, QA items 1–21 and the tools
   are unchanged; the verifier found no effect. PEC defers action on the
   corresponding notice (`NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md`).
6. **Add-on M at closeout (node M1).** Create both `MEMORY.md` from
   `docs/templates/MEMORY_TEMPLATE.md` with the one tabled `## Runs` row
   (proposal, add-on M), naming this PR once merged and the central receipt.
7. **Records outside this boundary.** The work-graph S3 node, the central
   receipt, and `docs/STATUS.md`/`README.md` under `D-PEC-88` are HELP_HUMAN's.
8. **Minor substrate items.** The run-root `apply_d98.py` comment "(values at
   origin/main 53145aaeb)" is stale for four entries (disclosed in `REPIN.md`).
   The verifier left an ignored `tools/scope_of_work/__pycache__/common.cpython-313.pyc`
   in the worktree (gitignored, untracked, outside this write boundary; not
   removed). The PREP `SHA256SUMS` lists an absent `D-PEC-98_DRAFT.md` (state on
   `origin/main`, outside this PR).

## Rollback

Before merge: close PR #958 and discard the branch. After merge, at owner
direction: a revert PR removes the two contracts and restores the two
`_STATUS.md` preimages (`write_status.sh` is forward-only, so file revert is the
only walk-back); the ruling record and register row are not reverted, and the
rollback gets its own register row and record.
