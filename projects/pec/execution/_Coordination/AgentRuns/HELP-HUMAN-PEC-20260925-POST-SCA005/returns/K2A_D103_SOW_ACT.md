# Return K2A — D-PEC-103 act (WORKING_ITEMS)

- **To:** HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node K2.
- **From:** WORKING_ITEMS (Type 1).
- **Brief:** `../briefs/K2A_D103_SOW_ACT.md`, SHA-256 `bb0d6e3105cd9a221f9adc1572e446c096bb2af04a472a8df267356c6ba48d6b`. It was verified and copied unchanged.
- **Method:** `chirality-root:bundled:workflow:scope-of-work`, with `MODE=INIT` and `STATUS_POLICY=NO_STATUS_TOUCH`.
- **Model:** the host reports Opus 5.5 (`claude-opus-5-5`) for the manager and both children. Roles and effort are instruction-asserted.
- **Date:** 2026-09-26 (MDT).

## PR

- **PR:** https://github.com/sgttomas/chirality/pull/992, against `main`. It is **not merged**.
- **Head before this return:** `bb937371d` (full SHA in the hand-back). The commit that adds this return is the final head. HELP_HUMAN adds the graph and STATUS records to this PR.
- **Branch:** `claude/pec-d103-first-sows-act`.
  - It was cut from fetched `origin/main` `d385b6a19`, the PR #989 merge that carries the ruling.
  - `origin/main` moved twice during the act, both times with Piping-only changes: `3e861f53c` (PR #983) and `7004eaeda` (PR #991).
  - Each move was merged in without a rebase (`c0d4098ca`, `c4ae46f6e`).
- **Worktree:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d103-act`.

## Act report

1. **Preconditions: all held.**
   - The ruling and the register row `D-PEC-103` `RULED A + S + M + C8 / EFFECTIVE ON MERGE` are on fetched `origin/main`.
   - The prep `SHA256SUMS` passes all 66 entries. The 17 run-root copies match it.
   - `apply_k2.py --check-only` exits 0 with all 17 pins as tabled.
   - The reliance-hold preflight gave `dispatch-for-production` `ALLOW` ×5.
2. **A.** `apply_k2.py` ran once and exited 0. It created exactly the two tabled contracts: 2 created, 0 modified, 0 removed, and 17/17 pins unchanged.
3. **C8.** `apply_k2_c8.py --check-only` exited 0. Its one real run also exited 0.
   - The write set is exactly DEL-10-13 `_DEPENDENCIES.md`, which now equals `609aa807…5693`.
   - The diff is the one tabled line in the human-owned Tracking Mode section.
4. **Verify.** The proposal's finite-verification table passed. The details are in the Checks section below.
5. **Verifier.** One fresh read-only `pec-reviewer` (opus) ran `MODE=VERIFY`, in the foreground, and returned **PASS WITH NOTES**: 0 BLOCKING, 0 NON-BLOCKING, 6 NOTEs.
   - Its brief and verdict are saved, with dispositions, as `VERIFIER_BRIEF_01.md` and `VERIFIER_VERDICT_01.md`.
   - It also reran `run_k2_checks.sh` on a clean export of `d385b6a19`, with `OVERALL PASS` (fault injection 19/19).
6. **S.** After the verifier passed and both validators printed `PASS format=SOW_V1`, one separate generic-shell `pec-task` (opus, no workflow) ran.
   - It ran the two tabled `write_status.sh … INITIALIZED "TASK+status-advance"` commands once each from the repository root. Both exited 0.
   - Both postimages equal the proposal's table at `{D}` = 2026-09-26, so no slot-rule difference arises.
   - `write_status.sh` is currently `0bf835f54f4bb9a78a51d0b56392a8686d1f255f06d3c2bcaf7e8665f77bece3`, unchanged since preparation and HELP_HUMAN's review.
   - The TASK's brief and return are saved as `S_TASK_BRIEF.md` and `S_TASK_RETURN.md`.
7. **M.** Not done now, by design. It is written at closeout (node M1). No `MEMORY.md` was created.
8. **Records.** `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` and `SHA256SUMS` (92 files) are in the run root.

The steps ran one after another, never concurrently: A `96537e934`, then C8 `ece62f792`, then the verdict `83260ef0a`, then S `5fc8424e1`.

## Written paths and hashes

Product paths (under `projects/pec/execution/`):

| Path | SHA-256 |
|---|---|
| `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md` (new) | `aecc513161c1e8a5a984dc2f7878b79783170adc1042fb91e816dc649ef50826` |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md` (new) | `c7743ee2ab7d795577d08c57d748fa704d3cc58ad55df7eea77bc95fb1b56633` |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_DEPENDENCIES.md` (C8) | `609aa807710feef11bf8506324cb2a79996f3d6ce5a6eb623ec9516e3ac65693` |
| `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_STATUS.md` (S) | `75366b6b8a0050c520ab583be927da3960d21df0b8cd3011668b2047db89a127` |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_STATUS.md` (S) | `3771d5262b8f9044a3dbed81af0032a155ec12e876ec90c1f8253a8e5237e567` |

Coordination paths:

| Path (under `_Coordination/`) | SHA-256 |
|---|---|
| `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2A_D103_SOW_ACT.md` | `bb0d6e3105cd9a221f9adc1572e446c096bb2af04a472a8df267356c6ba48d6b` |
| `SOW_INIT_K2_2026-09-26/SHA256SUMS` (covers all 92 other run-root files) | `d1a493a9f88b96084232c4d2394979c0a07f71926406285cc7f3668be19c845d` |
| `SOW_INIT_K2_2026-09-26/MANIFEST.md` | `054c4fdde9b4aec613a1a2345b3edd419b95556e3f2d18f44a47a77a2b4867dc` |
| `SOW_INIT_K2_2026-09-26/VALIDATION.md` | `81fd636471635dab925507c23ecd2d6324627edf663fe80e795b8beabf9a87fb` |
| `SOW_INIT_K2_2026-09-26/HANDOFF_STATE.md` | `48aa141f2ab86f994b55c97d798a4d44e53929782afc7ee64e83532af8c2aef2` |
| `SOW_INIT_K2_2026-09-26/VERIFIER_VERDICT_01.md` | `649c59235d114581aac45060c160a29af4aa000da0398f79493b2d159b9aaff4` |
| `SOW_INIT_K2_2026-09-26/S_TASK_RETURN.md` | `a98ebb56f880b1ee998a5f63f8a78c3bbca2f0a597478e6b7ce172f2df16336b` |
| `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/K2A_D103_SOW_ACT.md` | this file |

The instruction and method sources are hashed in `MANIFEST.md`:

| Source | SHA-256 prefix |
|---|---|
| Root `AGENTS.md` | `c8ce87ef…` |
| `projects/pec/AGENTS.md` | `df9196d1…` |
| `AGENT_WORKING_ITEMS.md` | `9ae4bea2…` |
| `AGENT_TASK.md` | `1a13a5b0…` |
| Ruling | `67ff8f1e…` |
| Proposal | `cfc2e65d…` |
| `WORKFLOW.md` | `84dadde4…` |
| `brief.md` | `1696cd9a…` |
| `checks.md` | `44ab41ac…` |
| `tools.md` | `fbd07771…` |
| Standard | `26c8254a…` |

## Check results

Evidence for every row is in `SOW_INIT_K2_2026-09-26/evidence/`.

| Check | Result |
|---|---|
| Validator | `PASS format=SOW_V1` ×2. It passed after A, after C8, at the first merged head and at the second merged head. |
| Checklists | 17 and 19 items, equal to the prepared `2227dbeb…9641` and `8e07ff3e…ba30`. Reruns are byte-identical. |
| Boundary owners | Exit 0, 0 failing, 0 `NOT_CHECKABLE`. The hand resolution was checked by the verifier. |
| Quotes | `RESULT PASS 137/137`, on each base: the act base, `3e861f53c` and `7004eaeda`. |
| State claims | `RESULT PASS 482/482`, on each base. |
| Cited IDs | `RESULT PASS 0/0` |
| Old S2 text | `stale=0 current=43` |
| `_STATUS.md` before S | No change. |
| `_STATUS.md` after S | Exactly the two tabled postimages. |
| Strict registers | Exit 1, 0 errors, 26 `XRG-013` (D-GOV-48, deferred). Byte-identical before A, after A, after C8, and at both merged heads. |
| Harness self-check, `validate_pec_loop_receipts.py`, `analyze_dep_closure.py` | Harness and receipts exit 0. Closure: no cycle and 0 bidirectional pairs. Output identical at the same points. The closure stdout was compared without its command-echo line; the summary was compared with timestamp and path keys removed. |
| Pins at the final head | `apply_k2.py`: 14/17 as tabled. The 3 that differ are exactly the granted S ×2 and C8 postimages. `apply_k2_c8.py`: 3/3. |
| Reliance holds | `dispatch-for-production` `ALLOW` ×5 before dispatch; `rely-for-production` `ALLOW` ×5 before fan-in. |
| `git diff --check origin/main...HEAD` | Clean. |
| CI on PR #992 | Running when this return was written; the hand-back reports the observed state. |

## Verifier verdicts

`VERIFIER_VERDICT_01.md` is PASS WITH NOTES, with these dispositions:

1. The pin table differs at head only by the C8 postimage, as intended. This is recorded in `VALIDATION.md`.
2. REQ-016's owner wording (QA 21) is a note for a later revision. The bytes are ruled.
3. The C-08 question DEL-10-13 CON-001 leaves open is now answered by the owner under C8. The central receipt should say so.
4. DEL-08-06 AC-005/VER-005 do not name "unreachable" separately. This is a production-test note.
5. The records were pending when the verifier ran; they are now written.
6. No schema defect was found.

## S TASK result

- Both `write_status.sh` runs exited 0, with empty stderr.
- DEL-08-06 went from `73e21846…2511` to `75366b6b…a127`. DEL-10-13 went from `c7a5705d…543b` to `3771d526…e567`. Both are byte-identical to the prepared postimages.
- Both deliverables are now `INITIALIZED`.
- **Execution note.** The TASK's first guard compared the validator output to the exact string `PASS format=SOW_V1`. The real output has a ` target=…` suffix, so the guard refused before any write. The TASK loosened it to a prefix match, re-verified, and ran each command exactly once.

## Containment

- `git diff --name-status origin/main...HEAD` lists only these paths outside the run root:
  - the two created contracts;
  - the two `_STATUS.md` files (S);
  - DEL-10-13 `_DEPENDENCIES.md` (C8);
  - the brief copy.
- This return is the only later addition.
- Everything else is under `SOW_INIT_K2_2026-09-26/`.
- No `MEMORY.md`, register, `Dependencies.csv`, `_CONTEXT.md`, `_REFERENCES.md`, decomposition, `v2/**`, PRD, `_DomainEngines/**`, `docs/**`, `README.md`, `_DECISIONS/**`, work-graph or foreign path was written.
- Both children worked only inside their own `mktemp -d` directories under the session scratchpad:
  - verifier: `k2verify.pMy3jX/`;
  - S TASK: `s_task.s2l61k/`.
- The manager's scratch is `k2a/`.

## For the caller to resolve

1. **Review and merge of PR #992.** This needs required CI and a fresh independent review of the actual candidate. After that, add the K2 work-graph record, the central receipt and any `D-PEC-88` STATUS/README records to this PR.
2. **The central receipt.** State that DEL-10-13's C-08 classification was made by the owner under `D-PEC-103` C8, even though the contract's CON-001 records it as unmade at `125cfacc1` (verifier Note 3).
3. **Add-on M at node M1.** Create the two `MEMORY.md` files with this PR's number and the receipt link.
4. **Carried open items (unchanged; none decided here):**
   - DEL-08-06 CON-002 and TBD-007, for K3;
   - the ordering against S4 and S1;
   - the two possible dependency amends (DEL-08-06 → DEL-04-03; DEL-10-13 → DEL-02-07);
   - the missing PEC v2 release process (DEL-10-13 CON-004);
   - the DEL-10-02 C-08 wording, which belongs to S1;
   - verifier Notes 2 and 4, for later revision or production.
5. **If `origin/main` moves again before merge:** re-fetch, merge without a rebase, and rerun `verify_k2_quotes.py` and `verify_k2_state_claims.py`. Stop if a pinned file or quoted locus changed.

Nothing here prompts about CHECKING, and no ruling was recorded that did not occur.
