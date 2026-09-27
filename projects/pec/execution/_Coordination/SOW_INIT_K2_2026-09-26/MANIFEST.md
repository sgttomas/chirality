# MANIFEST — D-PEC-103 act (SOW_INIT_K2_2026-09-26)

- **Act:** D-PEC-103 option A with add-ons C8 and S, run 2026-09-26 (local date, MDT). Add-on M is not part of this act; it is written at the undertaking's closeout (graph node M1).
- **Undertaking / node:** `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node K2.
- **Actor:** one WORKING_ITEMS (Type 1) instance under HELP_HUMAN, brief `../AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2A_D103_SOW_ACT.md` (SHA-256 `bb0d6e3105cd9a221f9adc1572e446c096bb2af04a472a8df267356c6ba48d6b`). Children: one fresh read-only `pec-reviewer` TASK (verifier, agent `a0414fd09eeccb8de`) and one generic-shell `pec-task` TASK (add-on S, agent `a5f3825273b3caa3b`). The host reports the model of all three as Opus 5.5 (`claude-opus-5-5`); roles and the `high` effort are instruction-asserted.
- **Delegation mechanism:** Claude Code harness-native subagents (the Agent tool), each run in the foreground within the manager's turn; parent WORKING_ITEMS, grandparent HELP_HUMAN. Scopes were set by the briefs below. The verifier's agent type has no Edit or Write tool but does have a shell, so its read-only posture, like the S TASK's write boundary, was brief-asserted rather than host-enforced; both were checked afterwards with `git status` and the branch diff.
- **Method:** `chirality-root:bundled:workflow:scope-of-work`, `MODE=INIT`, `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`, `RENDER_HTML=false`; the verifier ran `MODE=VERIFY`. No project or user workflow of that name exists (`.chirality/workflows/` absent in the repository and home directory).
- **Branch / worktree:** `claude/pec-d103-first-sows-act`, cut from fetched `origin/main` `d385b6a19` (PR #989 merge carrying the ruling) in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d103-act`; `origin/main` later moved to `3e861f53c` (PR #983, Piping only) and was merged in as `c0d4098ca` (no rebase).

## Authority and instruction sources (SHA-256 as read)

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `agents/AGENT_TASK.md` (read by both children) | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| Ruling `_DECISIONS/D-PEC-103_RULING_2026-09-26.md` | `67ff8f1e2c66a34032f1cf49ac2d87e6a4d622bc55c9473a3254619be888dfa2` |
| Proposal `_DECISIONS/D-PEC-103_first_sows_del_08_06_10_13_proposal_2026-09-26.md` | `cfc2e65d5ae91f0d62d4ef993bc22a91d2bb4716969d083ae98f0fc948eb5417` |
| `_DECISIONS/_REGISTER.md` (row `D-PEC-103` `RULED A + S + M + C8 / EFFECTIVE ON MERGE`) | `fe2cc825dac72b17b1b2988195acb626dbe50d6b6092adc98d3d25ebd6ac45ea` |
| Prep `PEC_FIRST_SOWS_K2_PREP_2026-09-26/SHA256SUMS` (66 entries, all OK) | `09f637d4b6ff41a9bf79f9054bb24589d18f41de3146e2c3ec991623670863ce` |
| `workflows/index.json` | `2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3` |
| `workflows/scope-of-work/WORKFLOW.md` | `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b` |
| `workflows/scope-of-work/execution.json` (hashed, not needed) | `4ad8b7eb42dba41f1609e6b3c61f14baa15ad82a1342f4ad12a095c4a570a26d` |
| `workflows/scope-of-work/resources/brief.md` | `1696cd9a0c13aeda4151ebdd666fff7d0450450c88ea1aa00f7435fdcbf492bc` |
| `workflows/scope-of-work/resources/checks.md` | `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188` |
| `workflows/scope-of-work/resources/tools.md` | `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7` |
| `resources/representation-migration.md` | not loaded |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` |
| `tools/scope_of_work/validate_scope_of_work.py` / `derive_review_checklist.py` / `check_boundary_owner_resolution.py` / `common.py` | `f0f10590…fecfe` / `bfb64dc9…0109` / `22ef57e0…ae16a` / `61a34722…0389` |
| `tools/scaffolding/write_status.sh` (current; equal to preparation and HELP_HUMAN's review) | `0bf835f54f4bb9a78a51d0b56392a8686d1f255f06d3c2bcaf7e8665f77bece3` |
| `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` / `execution/_Scripts/pec_reliance_hold.py` | `f877d931…cbc` / `b1712e4b…cd0e` |

Interpreter: CPython 3.13.7. All Python ran with `PYTHONDONTWRITEBYTECODE=1`.

## Product writes (paths under `projects/pec/execution/`)

| Item | Path | Preimage | Postimage (verified) | Writer |
|---|---|---|---|---|
| A | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md` | absent | `aecc513161c1e8a5a984dc2f7878b79783170adc1042fb91e816dc649ef50826` | `apply_k2.py`, one run |
| A | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md` | absent | `c7743ee2ab7d795577d08c57d748fa704d3cc58ad55df7eea77bc95fb1b56633` | `apply_k2.py`, one run |
| C8 | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_DEPENDENCIES.md` | `5087e581b00557cac9c245c543d0a690ed2a9fc992a96d8e60769f8a44baeb63` | `609aa807710feef11bf8506324cb2a79996f3d6ce5a6eb623ec9516e3ac65693` | `apply_k2_c8.py`, one run |
| S | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_STATUS.md` | `73e21846186b3ab46d4d11042ecb2bb00d0c69a0d7b4fa70734c75e65a892511` | `75366b6b8a0050c520ab583be927da3960d21df0b8cd3011668b2047db89a127` | S TASK, `write_status.sh`, one run |
| S | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_STATUS.md` | `c7a5705d7203a26f525317e85fa068d29cfeb49b8686eab1b5cd3e782e22543b` | `3771d5262b8f9044a3dbed81af0032a155ec12e876ec90c1f8253a8e5237e567` | S TASK, `write_status.sh`, one run |

Order, one after another: A (commit `96537e934`) → C8 (`ece62f792`) → verifier (verdict committed `83260ef0a`) → S (`5fc8424e1`).

## Run-root contents

- Bound copies, identical to the prep folder (17 files, `shasum -c` against the prep `SHA256SUMS`, 0 mismatches): `apply_k2.py` `b10461fa…257a`, `apply_k2_c8.py` `093130c8…84e9`, `candidates/` ×2, `addons/C8/`, `addons/S/` ×2, `quotes/` ×2, `claims/` ×2, `test_apply_k2.py`, `verify_k2_quotes.py`, `verify_k2_state_claims.py`, `check_cited_ids.py`, `scan_old_s2_text.py`, `run_k2_checks.sh`.
- Method outputs: `checklist_DEL-08-06.json` `2227dbeb…9641`, `checklist_DEL-10-13.json` `8e07ff3e…ba30`, `boundary_DEL-08-06.json` `b2e8ee78…679f`, `boundary_DEL-10-13.json` `d0197ec9…7879`.
- `evidence/`: every command with its exit code and output (see `VALIDATION.md`).
- `state_checks.sh` (`41f4cfe7…d5ef`): the manager's helper that ran the strict-register, harness, receipts and closure checks at each point (not bound).
- `VERIFIER_BRIEF_01.md` (`e49c1daa…c490`) and `VERIFIER_VERDICT_01.md` (`649c5923…aff4`, PASS WITH NOTES, with dispositions).
- `S_TASK_BRIEF.md` (`75d7fb4d…a605`) and `S_TASK_RETURN.md` (`a98ebb56…336b`).
- `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`.

No `_run_records/` entry was written in either deliverable. No `MEMORY.md` was created.
