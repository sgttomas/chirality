# D-PEC-99 A — Remaining Retirement Act Handoff State

**Act date:** 2026-09-26 (`{D}` = `{R}` = 2026-09-26, so no slot-rule replay was needed)
**Coordinator:** WORKING_ITEMS (Type 1), node RR3 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`, under `Workflow: chirality-root:bundled:workflow:task-management` (legacy-source retirement)
**Branch / basis:** `claude/pec-d99-remaining-retirement-act` from `origin/main` `189f205ff02df4111b33c20be441ce06e65ada7a` (PR #954 merge, carrying the ruling, the published proposal and register row `D-PEC-99` `RULED A / EFFECTIVE ON MERGE`; PR #943 merge `db9328789` is an ancestor)
**Pre-act commit:** `3b0231eccf65148930d37de91ba545d35f036ff6` (run root, bound scripts, preflights, baselines). **Generator commit:** `5066f895c`.
**Publication:** through its own PR under the standing Git authorization of 2026-09-12; not merged by this act.

## Act ledger

| Item | State after this act |
|---|---|
| Run root and bound scripts | DONE — `gen_d99.py` `1fad0239…7237` and `verify_d99.py` `c1d50dfd…1865` copied byte for byte (`cmp` identical to the Task Management folder copies) |
| Generator, one run | DONE — `--act-date 2026-09-26 --ruling-date 2026-09-26 --decision D-PEC-99 --q1 s1`; `WROTE 62 files`; `CHECK write_set 62`, `CHECK status_sections_removed 57`, `CHECK account_keys 92` (closed 9, Part A 71, Part B S1 4 / S2 4 / S4 4) |
| Postimages | 62/62 equal the proposal tables (`checks/posts_vs_proposal.out`); on-disk hashes equal the report |
| Closure check after | `RESULT PASS` against a `git archive` export of `3b0231ecc`, run before any other write, no `--allow-extra` |
| `FINAL_ROW_ACCOUNT.csv` | DONE — copy of the account with only `AppliedResult` set (`make_final_account.py`) |
| Graph sentences, RS1, `docs/STATUS.md`, `README.md` | NOT DONE here — HELP_HUMAN's, in the same PR |
| `MEMORY.md` | none, by ruling ("no MEMORY") |

## Part B keys per node (for HELP_HUMAN's graph sentences)

- **S1:** DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004 (the S1 sentence names DEL-03-06 for this correction only, per "Q1 a"), DEL-04-05-REM-003
- **S2:** DEL-02-07-REM-001, DEL-02-07-REM-002, DEL-02-07-REM-003, DEL-02-07-REM-004
- **S4:** DEL-04-01-REM-001, DEL-04-01-REM-002, DEL-04-02-REM-002, DEL-04-03-REM-002

Closed on record (9): DEL-01-03-REM-001..003, DEL-06-04-REM-001, DEL-07-02-REM-001, DEL-07-04-REM-001, DEL-07-05-REM-001, DEL-01-05-REM-001, DEL-01-05-REM-002. DEL-01-05-REM-003 is in Part A; no DEL-01-05 file was written.

## Finite verification (proposal table)

| Check | Result | Record |
|---|---|---|
| Preconditions | ruling, published proposal (`29e2ff57…6c79`), register row and #943 on fetched `origin/main` `189f205ff`; `projects/pec/AGENTS.md` = `4400c4e9…139c` before the act; generator pins held | this file; `checks/gen_check_only.out` |
| Reliance holds | `dispatch-for-production` 63/63 ALLOW before the act; `rely-for-production` 63/63 ALLOW before fan-in (register `f877d931…cbc`, header only; script `b1712e4b…cd0e`) | `checks/hold_*.tsv` |
| Closure before | `RESULT PASS` (92 keys, 73 held residuals outside) | `checks/closure_pre.out` |
| Generator | check-only and act both `write_set 62`, `status_sections_removed 57`; identical POST lines | `checks/gen_check_only.out`, `checks/gen_act.out` |
| Closure after | `RESULT PASS`: 66 `_STATUS.md`, no survivor; 57 edits exact; changed 58 = grant; new 4 = grant; protected unchanged | `checks/closure_post.out` |
| Scope of Work validation | 32/32 deliverable SOWs `PASS format=SOW_V1`, unchanged; the run also validated the 2 D-PEC-98 candidate copies (34/34 total), identical before and after | `checks/{pre,post}_sow.out` |
| Strict registers | exit 1 both, 0 errors, 28 warnings, byte-identical output | `checks/{pre,post}_strict.out` |
| Tranche manifest | G4 PASS in CI mode and in diff mode (`--added-manifests-only`) | `checks/post_manifest_*.out` |
| Launcher/posture | entrypoints PASS (identical before and after); pytest 33 passed | `checks/{pre,post}_entrypoints.out`, `checks/post_pytest.out` |
| Every-PR checks | harness self-check exit 0 and receipt validator VALID, each byte-identical before and after (so no new harness finding cites a target path) | `checks/{pre,post}_{harness,receipts}.out` |
| Task Management | `REGISTER.csv` PASS (9 rows) and `REGISTER_CLOSED.csv` PASS (16 rows), identical before and after; no row written | `checks/{pre,post}_tm_*.out` |
| `git diff --check` | exit 0, no output | `checks/post_diff_check.out` |
| Containment | PASS: 62/62 grant paths, run-root files, `FINAL_ROW_ACCOUNT.csv` and the brief copy; nothing HELP_HUMAN-owned or outside. `checks/containment.out` is a saved run at the commit before it is added (so it never counts itself); the RR3 return records the rerun at the final head | `containment.py`, `checks/containment.out` |

## Residuals and disclosures (recorded, not repaired here)

1. **SOW population.** The proposal says 32 SOWs (prepared at `6281273fa`). At the act's basis, `find` returns 34: the 32 deliverable SOWs plus two D-PEC-98 candidate copies under `_Coordination/PEC_FIRST_SOWS_D98_PREP_2026-09-26/candidates/`, added by `47bf0c1c7`. All 34 pass and none changed. If the parallel D-PEC-98 act (S3A) merges first, DEL-02-08 and DEL-02-09 gain deliverable SOWs; neither is in this census.
2. **`HumanDecision` column.** The brief and the proposal's administrative grant set only `AppliedResult` in the copy, so `FINAL_ROW_ACCOUNT.csv` keeps the account's preparation-time `HumanDecision=PENDING`. The human decision is the D-PEC-99 ruling (`D-PEC-99_RULING_2026-09-26.md`), which each `AppliedResult` applies; the column was not rewritten.
3. **Parallel act.** `D-PEC-98` S3A runs on disjoint paths. If it merges before this PR, re-fetch `origin/main` and confirm that no granted path or pin moved before merge; report any conflict to HELP_HUMAN.
4. **Findings carried by the proposal** (DEL-02-01 SOW parser clauses; DEL-04-01 against SOW-004 and `TM-PEC-004`; DEL-07-04 without T-RT; PKG-03 and DEL-04-02/03/05 SOW paraphrases; four Remaining-only claim IDs; "fourteen" entity types; `docs/STATUS.md` lines) stay as disclosed in the proposal; this act addresses none of them.

## Execution disclosures

- **Brief.** `RR3_D99_RETIREMENT_ACT.md`, SHA-256 `9f5702bd78384b9233751a50ec88aaa01e2372ad4d681eab400f5a1f593ce547`, verified before work began; copied to `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/`.
- **Instruction and authority sources read (SHA-256 at `189f205ff`).** Root `AGENTS.md` `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`; `projects/pec/AGENTS.md` `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` (pre-act); `agents/AGENT_WORKING_ITEMS.md` `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665`; `workflows/task-management/WORKFLOW.md` `d5e8eff5742326330c0f933dc322e07fbe6a2bb82ad151aadf803b001a02e654`, `resources/contract.md` `3162f7ed386bcac08c0e16c0feae3b7a7a5109ba4bf4f845acc66bd2d6dfd04e`, `resources/method.md` `d52403c983c92b1c65fe2b621d8c6bdc5c10e1fdb8c9ac99e95614137639c61e`; ruling `D-PEC-99_RULING_2026-09-26.md` `3e34403a59b2ba4893a785586b672786651992cba80c58d02dae7fe32c61c989`; proposal `29e2ff5704d45f0da31f41fd80bf822003743fbf9effdda4ebbc2806306d5c79`; census `b0e25361…6eb4` and account `b240b38d…e7a2` (both pinned by the generator); the D-PEC-95 run root as format precedent.
- **Generator executor.** This manager ran the generator once, as the administrative grant assigns. No TASK author was dispatched.
- **Federation.** The account's federation preflight (`FEDERATION_PREFLIGHT.md`) was done at preparation; this act writes no register row and did not repeat it.
- **Check helpers** written for this run, read-only, committed for rerun: `run_holds.sh`, `run_checks.sh`, `check_posts_vs_proposal.py`, `containment.py`; `make_final_account.py` writes only `FINAL_ROW_ACCOUNT.csv`.
- **Model.** Claude Opus 5.5 (`claude-opus-5-5`) for this manager, as the runtime reports; reasoning level as set by the host.

## Rollback (proposal §Rollback)

- **Before merge:** close the PR and discard the branch and worktree.
- **After merge (owner direction):** a revert PR restores the 57 `_STATUS.md` preimages and `AGENTS.md` `4400c4e9…139c`; deletes the exhibit, manifest, two notices and `FINAL_ROW_ACCOUNT.csv`; removes the graph's "Absorbs … Part B items" sentences; sets the register row to reverted; routes a withdrawal notice to Root and Runtime. This run root stays as non-current evidence with a rollback note.

## Independent verification

- **Verdict 01 (reviewed `10feef34c`): PASS WITH NOTES**, no blocking finding (`VERIFIER_VERDICT_01.md`, transcribed verbatim). One fresh read-only `pec-reviewer` (Claude Opus 5.5) reproduced all 62 postimages on a fresh `git archive` export of `3b0231ecc` without `--reproduction` (byte-identical to the head and to the proposal tables), reran both closure-check modes (PASS), the finite verification table, an independent semantic parse (History lines, verbatim exhibit, gates, Part B carry-forwards, closed set, AGENTS.md rebuild) and the protected-path checks, and a trial merge with `origin/main` `6b48b6f26` (clean; no pin or granted path touched).
- **Dispositions (no product, account or register byte changed):**
  - N1 (graph sentences and RS1 not yet in the PR): HELP_HUMAN's by the ruling and the brief; routed with the keys above. The verdict covers `10feef34c` only; the final candidate after HELP_HUMAN's additions needs its own review under Root's merge rule.
  - N2 (`HumanDecision=PENDING` kept in `FINAL_ROW_ACCOUNT.csv`): kept; the grant names only `AppliedResult` (residual 2).
  - N3 (`verify_d99.py` keeps only the last repeated `--allow-extra`; fails closed): the script's bytes are bound by the ruling; recorded here for any later reuse. Pass all extra paths after one `--allow-extra`.
  - N4 (SOW count): confirmed accurate; no change.
  - N5 (`origin/main` advanced by #955): no overlap. Routed to HELP_HUMAN: #955 changed `workflows/scope-of-work/WORKFLOW.md` (`d616865a…` to `84dadde4c573…`) and `docs/SPEC.md` §3.3/§3.4/§13, which the S1, S2 and S4 packets absorbing Part B should use; #955 also sent PEC a record-only notice.
  - N6 (`containment.out` one commit behind): the Containment row above now says so; the return records the rerun at the final head.
  - N7 (manifest `rollback` says "commit", singular): the manifest bytes are the proposal-tabled postimage; the proposal's revert-PR rollback governs; no change.

## Not claimed

No lifecycle change, no Scope of Work write, no evidence inquiry executed or selected, no Task Management row. No CHECKING, ISSUED, artifact acceptance, readiness or reliance. Nothing here prompts about CHECKING.
