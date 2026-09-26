# D-PEC-98 act — validation

Run from the repository root of the worktree
`/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d98-first-sows-act`
with `PYTHONDONTWRITEBYTECODE=1` and CPython 3.13.7, on 2026-09-26. Every
command, its exit code and its full output are under `evidence/` (each `.out`
file begins with the command and a `# cwd=… HEAD=…` line and ends with
`exit=N`). Base: `origin/main` `6b48b6f26` (the branch was cut at `189f205ff`
and fast-forwarded to `6b48b6f26` before the act; `evidence/at_189f205ff/` holds
the first baseline).

## Proposal "Finite verification" table

| Check | Command | Exit | Result | Required | Evidence |
|---|---|---|---|---|---|
| Preconditions: ruling and register row | `git fetch`; read `_DECISIONS/_REGISTER.md` and the ruling on `origin/main` | — | `D-PEC-98` row `RULED A + S + M / EFFECTIVE ON MERGE`; ruling `039dc7e2…8361`; proposal `92b6f1a2…3e40` | present | `VERIFIER_VERDICT_01.md` check 1 |
| Preconditions: pins | `sha256` of the four register/PRD files and four deliverable files | — | equal to the re-bound `PINNED` (`REPIN.md`) | as tabled | `REPIN.md`; `evidence/apply_check_only.out` |
| Preconditions: act check-only | `apply_d98.py --repo . --candidates <run root>/candidates --check-only` | 0 | `CHECK write set = grant (2 creates, 0 modifies, 0 removes); nothing written` | as stated | `evidence/apply_check_only.out` |
| Reliance holds, before dispatch | `pec_reliance_hold.py … --operation dispatch-for-production` on both `ScopeOfWork.md` and both `_STATUS.md` | 0 ×4 | `ALLOW` ×4 | `ALLOW` | `evidence/reliance_dispatch.out`; the S TASK reran it for both `_STATUS.md` (`S_TASK_RETURN.md`) |
| Reliance holds, before fan-in | `… --operation rely-for-production` on both `ScopeOfWork.md` and, after S, both `_STATUS.md` | 0 ×4 | `ALLOW` ×4 | `ALLOW` | `evidence/post/reliance_rely.out`, `evidence/post_S/reliance_rely_status.out` |
| Act | `apply_d98.py --repo . --candidates <run root>/candidates`, output captured outside `projects/pec` and copied here after exit | 0 | `WRITE` ×2; `CHECK targets 2/2 byte-exact; write set = grant (2 created, 0 modified, 0 removed under projects/pec); pinned 8/8 unchanged` | as stated | `evidence/apply_run.out` |
| Contract validity | `python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>` ×2 (and `--json`) | 0 / 0 | `PASS format=SOW_V1` ×2; JSON `issues: []` | `PASS format=SOW_V1` ×2 | `evidence/post/validate_DEL-02-0{8,9}.out`, `validate_json_*.out`; again after S: `evidence/post_S/validate_postS_*.out` |
| Checklist | `derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, each twice | 0 ×4 | 21 and 17 items, AC-001… in source order, bound to `2319661b…dd26` / `eab18e17…6f5e`; reruns byte-identical. Hashes `dd05939ddda99d5030ab42dbde77c24171c0a4c20bebddc3860254645248048c` / `0ca3f3ad6220598cb16fe63e1b345d4fd5bc36a0afbdbe0f6c1c26d6cd4a8c2a` | 21 / 17; byte-identical to prepared except through the re-pin | `checklist_*.json`; `evidence/post/checklist_*.out` |
| Checklist vs prepared | field comparison with `../PEC_FIRST_SOWS_D98_PREP_2026-09-26/evidence/checklist_*.json` | 0 | equal after mapping contract SHA-256 old → new and every `line`/`source_line` +10 (08) / +8 (09), the lines the re-pin adds above the matrix; no other difference | only re-pin differences | `evidence/post/checklist_repin_equivalence.out` |
| Boundary owners (QA 21) | `check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL>/ScopeOfWork.md` ×2 | 0 / 0 | 1 checked, 0 failing each; `NOT_CHECKABLE` 08 REQ-009/010/011 and 09 REQ-007/008/009; JSON byte-identical to the prepared reports (`c7afa8dd…`, `dc7beacc…`) | 1 / 0 each | `boundary_*.json`; `evidence/post/boundary_*.out` |
| QA 21 hand resolution | read each `NOT_CHECKABLE` requirement and its cited claim | — | 08 REQ-009→`DEL-04-05`, REQ-010→`DEL-01-03`, REQ-011→`DEL-04-03`, each citing CLM-011 which names that owner; 09 REQ-007/008/009 → the same owners via CLM-010 | as tabled | `evidence/post/qa21_hand_resolution.out`; verifier check 3 |
| Quote fidelity | `python3 <run root>/verify_d98_quotes.py . <08 folder> <09 folder>` | 0 | `RESULT PASS 69/69` | 69/69 | `evidence/post/quotes.out` |
| State claims | `python3 <run root>/verify_d98_state_claims.py .` | 0 | `RESULT PASS 56/56` (44 original + 12 second-pin) | pass at both pins | `evidence/post/state_claims.out` |
| Lifecycle preserved (A) | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` before S | 0 | empty | empty under A | `evidence/post/lifecycle.out` |
| Lifecycle under S | `sha256` of both `_STATUS.md` after the S TASK | — | `4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe` / `e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056`, equal to the proposal's table at `{D}` = 2026-09-26; diff is exactly the slot rule | tabled postimages | `S_TASK_RETURN.md`; `evidence/post_S/lifecycle_postS.out` |
| Strict registers (B2) | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` before the act, after the act, after S | 1 / 1 / 1 | 0 errors, 28 warnings (26 `XRG-013` D-GOV-48, 2 `DRB-008`); output identical in all three runs apart from the two header lines, and identical to the `189f205ff` baseline | identical to pre-act (exit 1, 0 errors, 28 warnings) | `evidence/strict_pre.out`, `evidence/post/strict_post.out`, `evidence/post_S/strict_postS.out`, `evidence/at_189f205ff/strict_pre.out` |
| Every-PR: harness | `python3 tools/practitioner_harness/harness.py self-check`, same three points | 0 ×3 | output identical | exit 0; identical | `evidence/harness_pre.out`, `evidence/post/harness_post.out`, `evidence/post_S/harness_postS.out` |
| Every-PR: receipts | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .`, same three points | 0 ×3 | `VALID … frozen through Receipt-166`; identical | exit 0; identical | `evidence/receipts_pre.out`, `evidence/post/receipts_post.out`, `evidence/post_S/receipts_postS.out` |
| Containment | `git diff --name-status origin/main...HEAD` | 0 | the two created contracts; after S the two `_STATUS.md`; the run root; the brief copy and the return under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/`; nothing else | as stated | `evidence/post/containment.out`; final state in `HANDOFF_STATE.md` |
| Whitespace | `git diff --check origin/main...HEAD` | 0 | clean after the act; at closeout clean with `S_TASK_RETURN.md` marked `-whitespace` in the run-root `.gitattributes`, because its verbatim unified diff has single-space blank context lines (the same exemption covers `evidence/**`, which has no trailing whitespace) | clean | `evidence/post/whitespace.out`; final run in the manager's return |

## Re-pin checks (question 4)

| Check | Result | Evidence |
|---|---|---|
| Copies equal the prepared hashes | yes, all seven files | `REPIN.md` |
| Word diff touches only the three places | yes (frontmatter, Purpose paragraph, observation clause) | `REPIN_WORDDIFF.txt`; verifier check 6a |
| `verify_d98_quotes.py` against the new tree | `RESULT PASS 69/69` at `189f205ff` and at `6b48b6f26` | `evidence/at_189f205ff/repin_quotes.out`, `evidence/repin_quotes.out` |
| `TARGETS` and `PINNED` equal recomputed hashes; nothing else changed in `apply_d98.py` | yes | `REPIN_WORDDIFF.txt`; verifier check 6b |
| State claims at both pins | `RESULT PASS 56/56` | `evidence/repin_state_claims.out` |
| Re-bound act script fault injection | `RESULT PASS 5/5` | `evidence/test_apply_d98.out` |

## Method QA (`scope-of-work` `resources/checks.md`, INIT)

Items 1, 3, 4, 8, 9, 13, 16, 18, 19, 20, 21: PASS (independent `MODE=VERIFY`
in `VERIFIER_VERDICT_01.md`, check 3). Items 2, 5–7, 10–12, 14, 17 (CONVERT)
and 15 (no HTML requested) and 22 (REVISE, added by Root PR #955):
NOT_APPLICABLE.

## Independent verifier

`VERIFIER_VERDICT_01.md`: **PASS WITH NOTES**, no blocking defect, by a fresh
read-only `pec-reviewer` TASK (host-reported model `claude-opus-5-5`). Its
notes are carried in `HANDOFF_STATE.md`; notes 1 and 2 concern contract text
that the ruling did not allow this act to change and go to the owner.

## Checks not run

- Kill test, parity, source and v2 checks: not applicable (no source,
  configuration or capability change).
- Task Management and instruction-entrypoint checks: not applicable (no such
  file changed).
- Decomposition re-audit: not recommended by the proposal (no decomposition
  truth, register or topology change).
