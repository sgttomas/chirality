# Return — S3A D-PEC-98 act (WORKING_ITEMS)

Brief `S3A_D98_SOW_ACT.md` (`d9a013489faac17c9a9f2ef90c0f5039e061ab098d8bde0e43defc7b65486291`,
copy at `../briefs/S3A_D98_SOW_ACT.md`). Undertaking
`HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S3, 2026-09-26. Actor:
WORKING_ITEMS (Type 1) under HELP_HUMAN, `Workflow: chirality-root:bundled:workflow:scope-of-work`
(`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`); host-reported model
`claude-opus-5-5` (role and `high` effort instruction-asserted).

**Result: act complete, not merged.** PR #958
(https://github.com/sgttomas/chirality/pull/958), branch
`claude/pec-d98-first-sows-act`, based on `origin/main` `6b48b6f26`. The head
SHA at hand-back is the commit that adds this return (reported in the
hand-back message).

## Act report

1. **Preconditions.** Fetched `origin/main` carries the ruling (`039dc7e2…8361`)
   and register row `D-PEC-98` `RULED A + S + M / EFFECTIVE ON MERGE` (PR #954).
   The four acceptance-commit hashes stated by the brief were verified at
   `189f205ff`. Reliance-hold preflight: `dispatch-for-production` ALLOW ×4 (both
   `ScopeOfWork.md`, both `_STATUS.md`); `rely-for-production` ALLOW ×4 before
   fan-in. Worktree `.claude/worktrees/pec-d98-first-sows-act` on the brief's
   branch, cut from fresh `origin/main` `189f205ff`; `origin/main` then advanced
   to `6b48b6f26` (Root PR #955, which touches no pinned file) and the branch was
   fast-forwarded before the act, with every pin and check rerun there.
2. **Re-pin** (`SOW_INIT_D98_2026-09-26/REPIN.md`). Copies hash-checked; three
   places moved per candidate; `verify_d98_quotes.py` `RESULT PASS 69/69` at
   `189f205ff` and `6b48b6f26` (re-pin not void); `apply_d98.py` re-bound (two
   `TARGETS`, four register/PRD `PINNED`); second `PIN` added to
   `verify_d98_state_claims.py` (`RESULT PASS 56/56`); word diff in
   `REPIN_WORDDIFF.txt`; re-bound script fault injection `RESULT PASS 5/5`.

   | File | Prepared | Re-pinned |
   |---|---|---|
   | DEL-02-08 candidate | `03cce13f…dc0a` | `2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26` |
   | DEL-02-09 candidate | `aafb54fd…188b` | `eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e` |
   | `apply_d98.py` | `19c2ecb6…419e` | `0a28d05d7d285596497a98306f4327909fd3817ac8403f66a1b64f7c86d29343` |
   | `verify_d98_state_claims.py` | `7bb9e6bb…b673` | `65059ce21309dea7ba945db562353c7d45884e6f3bf77aad3b51b244309e835f` |

3. **Write.** Re-bound `apply_d98.py --check-only` then one real run from the
   repository root, output captured in the session scratchpad and copied into
   the run root after exit: exit 0, `CHECK targets 2/2 byte-exact; write set =
   grant (2 created, 0 modified, 0 removed under projects/pec); pinned 8/8 unchanged`.
4. **Verify.** Every row of the proposal's finite-verification table passes
   (`VALIDATION.md`).
5. **Verifier.** One fresh read-only `pec-reviewer` (`claude-opus-5-5`):
   **PASS WITH NOTES**, no blocking defect (`VERIFIER_VERDICT_01.md`). It confirmed
   the three-place word diff, `TARGETS`/`PINNED` equal to recomputed hashes, and
   state claims passing at both pins.
6. **Add-on S.** One separate generic-shell `pec-task` (`claude-opus-5-5`, no
   workflow) ran the two `write_status.sh … INITIALIZED "TASK+status-advance"`
   commands after the verdict: `DONE`, postimages equal the proposal's table at
   `{D}` = 2026-09-26 (`S_TASK_RETURN.md`). It disclosed one gate slip: its first
   string gate rejected the validator's `PASS format=SOW_V1 target=…` line, so
   nothing was written; it re-validated and ran each command once.
7. **Add-on M** not done (closeout node M1), as the brief directs.
8. `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` written in the run root.

## Written paths (SHA-256)

| Path (relative to `projects/pec/execution/`) | SHA-256 |
|---|---|
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` (created) | `2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` (created) | `eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_STATUS.md` (S) | `4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_STATUS.md` (S) | `e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056` |
| `_Coordination/SOW_INIT_D98_2026-09-26/` (66 files plus `MANIFEST.md`) | `MANIFEST.md` `0399d0153b1dd7571afae9b81df9ec00a1ab2e9f90a8537ad0e35d13b125d403` lists each; `REPIN.md` `7ea1b139…08c8`, `VALIDATION.md` `f80def21…21a1`, `HANDOFF_STATE.md` `3f33d44e…982c`, `VERIFIER_VERDICT_01.md` `e1741788…6561`, `S_TASK_RETURN.md` `623dd9da…89c7` |
| `_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S3A_D98_SOW_ACT.md` | `d9a013489faac17c9a9f2ef90c0f5039e061ab098d8bde0e43defc7b65486291` |
| `_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S3A_D98_SOW_ACT.md` | this file |

## Check results (summary)

Validator `PASS format=SOW_V1` ×2 (also after S); checklists 21 / 17 items bound
to the postimages, differing from the prepared ones only by the contract hash and
the re-pin's line offsets (+10 / +8); boundary owners 1 checked / 0 failing each,
QA 21 hand resolution as tabled; quotes 69/69; state claims 56/56; strict
registers exit 1, 0 errors, 28 warnings, identical before the act, after it and
after S; harness self-check and receipts validator exit 0, identical at all three
points; lifecycle unchanged under A, then exactly the two tabled `_STATUS.md`
postimages under S.

## Containment

`git diff --name-status origin/main...HEAD`: the two created `ScopeOfWork.md`, the
two modified `_STATUS.md`, the brief copy, this return, and 67 files under the run
root. Nothing else. `git diff --check origin/main...HEAD` exit 0, with the run-root
`.gitattributes` marking `evidence/**` and the verbatim `S_TASK_RETURN.md` (whose
embedded diff has single-space blank context lines) as `-whitespace`. No
`MEMORY.md`, register, dependency, `_CONTEXT.md`, `_REFERENCES.md`, decomposition,
`v2/**`, PRD, `docs/**`, `README.md`, `_DECISIONS/**`, work-graph or foreign path.

## For the caller to resolve

1. **Owner disclosure (verifier note 1).** DEL-02-08 CLM-013 (line 111) still calls
   `c9e5cd87d` "the decomposition pin"; after the re-pin the pin is `189f205ff…`.
   Its hashes are correct. Question 4 allowed only three moves, so the act did not
   touch it; a one-word correction needs a later owner-authorized revision.
2. **Owner disclosure (verifier note 2).** The re-pinned observation clause lists
   the loci `verify_d98_quotes.py` checks and omits two other quoted loci
   (`AnticipatedArtifacts` cells; `DL-4` "one per feed kind"). Both are verbatim at
   both commits (verifier hand check), so nothing false is stated, but the list
   reads as complete. This is manager-authored wording; the act runs once, so it is
   not repaired here. It can go in the same later revision.
3. **Base currency.** `origin/main` is now `cb85f85d1` (Root PR #956; under
   `projects/pec` only a notice, no pinned file). If CI asks to update the PR base,
   report it; not repaired here.
4. **D-PEC-99.** Not merged at hand-back. If it merges first, rerun both check aids
   on the updated base (DEL-02-09 CLM-012 quotes two `projects/pec/AGENTS.md`
   phrases).
5. **Method edition.** The act loaded the bound `scope-of-work` edition
   (`WORKFLOW.md` `d616865a…fbd8b`); Root PR #955 later added `MODE=REVISE`
   (`84dadde4…bc2b`) without changing INIT text, QA items 1–21 or the tools. PEC
   defers action on its notice.
6. **Records for HELP_HUMAN:** independent review of PR #958 and merge; the
   `D-PEC-98` register row's effective-status wording; the work-graph S3 node; the
   central receipt; `docs/STATUS.md`/`README.md` under `D-PEC-88`; add-on M at M1.
7. **Minor.** Stale comment in the run-root `apply_d98.py` (disclosed in
   `REPIN.md`); an ignored `tools/scope_of_work/__pycache__/common.cpython-313.pyc`
   left by the verifier in the worktree (untracked, gitignored, outside this write
   boundary); the PREP `SHA256SUMS` lists an absent `D-PEC-98_DRAFT.md` (already on
   `origin/main`).

No lifecycle change beyond add-on S's `OPEN → INITIALIZED` per deliverable; CON-005
open; no registry act; no CHECKING, ISSUED, REVIEW gate or acceptance.
