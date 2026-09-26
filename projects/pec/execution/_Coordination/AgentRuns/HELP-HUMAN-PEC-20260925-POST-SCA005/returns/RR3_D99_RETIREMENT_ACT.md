# RR3 return — D-PEC-99 option-A Remaining retirement act

**From:** WORKING_ITEMS (Type 1), node RR3 of `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`, under `Workflow: chirality-root:bundled:workflow:task-management` (legacy-source retirement). Model: Claude Opus 5.5 (`claude-opus-5-5`); the host set the reasoning level.
**To:** HELP_HUMAN.
**Brief:** `../briefs/RR3_D99_RETIREMENT_ACT.md`, SHA-256 `9f5702bd78384b9233751a50ec88aaa01e2372ad4d681eab400f5a1f593ce547`. Verified before work began and copied unchanged.

## PR

- PR #957, https://github.com/sgttomas/chirality/pull/957, branch `claude/pec-d99-remaining-retirement-act`.
- Basis: `origin/main` `189f205ff` (PR #954).
- Commits:
  - pre-act `3b0231ecc`
  - generator `5066f895c`
  - checks and account `c9ccfb645`
  - containment `10feef34c` (verdict 01 reviewed this commit)
  - verdict 01 transcription `a609758aa`
  - containment rerun `0802a3725` (verdict 02 reviewed `10feef34c..0802a3725`)
  - verdict 02 transcription `ddec1a2f9`
  - this return with the final containment rerun: the commit that adds this file. Its SHA is in the caller hand-back.
- Not merged.
- **CI:** "Select source coverage" and "Desktop E2E (source mode)" fail with `Update the PR base: event target base is missing, unavailable or not integrated into head`. `origin/main` has advanced to `cb85f85d1` (PRs #955 and #956). The brief says to report this and not repair it, so it is not repaired. The `pec` and "App instruction bundle" jobs pass.

## Generator and closure-check reports

- **Generator.** One run of `gen_d99.py` (`1fad0239…7237`) from the run root. Arguments: `--repo . --act-date 2026-09-26 --ruling-date 2026-09-26 --decision D-PEC-99 --q1 s1`. Run at 2026-09-26 12:03 MDT.
  - Output: `WROTE 62 files`; `CHECK write_set 62`; `CHECK status_sections_removed 57`; `CHECK account_keys 92` (closed 9, Part A 71, Part B S1 4 / S2 4 / S4 4).
  - The `--check-only` run gave identical POST lines.
  - 62/62 postimages equal the proposal tables. `{D}` = 2026-09-26, so no slot-rule replay was needed.
- **Closure check `verify_d99.py`** (`c1d50dfd…1865`):
  - `--account-only` before the act: `RESULT PASS`.
  - Act mode, run immediately after the generator against a `git archive` export of `3b0231ecc`, with no `--allow-extra`: `RESULT PASS`. It found 66 `_STATUS.md`, no surviving heading, 57 exact edits, 58 changed paths equal to the grant, 4 new paths equal to the grant, and no protected path changed.
- Records are in `REMAINING_RETIREMENT_D-PEC-99_2026-09-26/checks/`: `gen_check_only.out`, `gen_act.out`, `closure_pre.out`, `closure_post.out`, `posts_vs_proposal.out`, indexed in `COMMANDS.txt`.

## Written paths (SHA-256)

- **57 `_STATUS.md`.** Their postimages are exactly the proposal's tabled postimages, and each is listed with its hash in `checks/gen_act.out` (POST lines).
- **`projects/pec/AGENTS.md`:** `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- **Exhibit** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`: `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`
- **Manifest** `docs/governance_harness/tranche_manifests/PEC-REMAINING-RETIREMENT-20260926.yaml`: `f077b9958d42c9115234aef94c6c7d1d480f767829b552107d729a52412baeef`
- **Root notice** `execution/_Coordination/NOTICE_2026-09-26_PEC_REMAINING_RETIREMENT.md`: `e1b3929fe1a514b361811ffee9b50d1e9f618346524e53b9aa2284fcdca38add`
- **Runtime notice** `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-26_PEC_REMAINING_RETIREMENT.md`: `20aecce99a9835cba3e28f38154852138755ac914a9b42fb85aeba37a2a16aa6`
- **`FINAL_ROW_ACCOUNT.csv`** (Task Management folder): `c2f20bedc285bf8a1a180d12ac610679995526cae08d37ba6453c4cc821581c9`. Only `AppliedResult` differs from the account.
- **Run root** `projects/pec/execution/_Coordination/REMAINING_RETIREMENT_D-PEC-99_2026-09-26/`: the bound scripts (exact bytes), helpers, `checks/`, `HANDOFF_STATE.md`, `VERIFIER_VERDICT_01.md` and `VERIFIER_VERDICT_02.md`.
- **Brief copy** and this return.

## Check results

| Check | Result |
|---|---|
| Preconditions | Ruling, proposal `29e2ff57…6c79`, register row, #954 and #943 on fetched `origin/main`. `AGENTS.md` = `4400c4e9…139c` before the act. All generator pins held. |
| Reliance holds | `dispatch-for-production` 63/63 ALLOW before the act. `rely-for-production` 63/63 ALLOW before fan-in. |
| SOW validation | The 32 deliverable SOWs PASS and are unchanged. `find` also returns the 2 D-PEC-98 candidate copies, so 34/34 overall. Output is identical before and after. |
| Strict registers | Exit 1 both times, 0 errors, 28 warnings, byte-identical output. |
| G4 manifest | PASS in CI mode and in diff mode. |
| Entrypoints; pytest | Entrypoints PASS, identical before and after. pytest: 33 passed. |
| Harness self-check; receipt validator | Exit 0 and VALID, each byte-identical before and after. |
| taskmgmt validate | `REGISTER.csv` and `REGISTER_CLOSED.csv` PASS, identical before and after. No row written. |
| `git diff --check` | Clean. |
| Containment | PASS at `ddec1a2f9`, the commit immediately before this return's own commit (`checks/containment.out`): 62/62 grant paths, 42 run-root files, `FINAL_ROW_ACCOUNT.csv` and the brief. Nothing is outside the boundary and nothing is HELP_HUMAN-owned. This return's commit adds only this file and the updated `containment.out`. |

## Verifier verdicts

- **01**, reviewing `10feef34c`: **PASS WITH NOTES**, no blocking finding. It reproduced all 62 postimages on a fresh export and passed the semantic checks. A trial merge with `6b48b6f26` was clean. The N1–N7 dispositions are in `HANDOFF_STATE.md`.
- **02**, reviewing `0802a3725` (the repair delta `10feef34c..0802a3725`): **PASS WITH NOTES**, no blocking finding. The verdict 01 transcription is byte-identical and the dispositions are true. Two wording overstatements in `HANDOFF_STATE.md` were reworded in `ddec1a2f9`. `origin/main` `cb85f85d1` (#956) touches no granted path or pin, and the trial merge was clean.

## Part B keys per node (for the graph sentences)

- **S1:** DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004, DEL-04-05-REM-003. Name DEL-03-06 for this correction only ("Q1 a").
- **S2:** DEL-02-07-REM-001, DEL-02-07-REM-002, DEL-02-07-REM-003, DEL-02-07-REM-004
- **S4:** DEL-04-01-REM-001, DEL-04-01-REM-002, DEL-04-02-REM-002, DEL-04-03-REM-002

Sentence form (proposal): "Absorbs as exact carry-forwards the `D-PEC-99` exhibit Part B items for this node: <keys>."

## For HELP_HUMAN to resolve

1. Add the three graph sentences, RS1, and the `docs/STATUS.md` / `README.md` lines in this PR. Then have the final candidate independently reviewed; verdicts 01 and 02 cover only this act's commits.
2. CI reports "Update the PR base". It was not repaired here.
3. If the parallel `D-PEC-98` S3A act merges first, re-fetch and confirm that no granted path or pin moved. Neither #955 nor #956 moved one (verdict 01 N5, verdict 02 finding 4). `projects/pec/AGENTS.md` on `cb85f85d1` is still `4400c4e9…139c`.
4. For the S1, S2 and S4 packets: #955 changed `workflows/scope-of-work/WORKFLOW.md` (now `84dadde4c573…`) and `docs/SPEC.md` §3.3/§3.4/§13. #955 and #956 each sent PEC a record-only notice (`NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` and `NOTICE_2026-09-26_SOFTWARE_PRD_REGISTRATION.md`).
5. `verify_d99.py` keeps only the last of repeated `--allow-extra` flags. It fails closed. For any rerun, pass every extra path after a single flag.
6. `FINAL_ROW_ACCOUNT.csv` keeps `HumanDecision=PENDING` because the grant names only `AppliedResult`. The owner decision is the ruling.

## Not claimed

- No lifecycle change and no Scope of Work write.
- No evidence inquiry executed or selected, and no Task Management row.
- No CHECKING, ISSUED, acceptance, readiness or reliance.
- No human ruling recorded beyond the D-PEC-99 ruling already on `origin/main`.
