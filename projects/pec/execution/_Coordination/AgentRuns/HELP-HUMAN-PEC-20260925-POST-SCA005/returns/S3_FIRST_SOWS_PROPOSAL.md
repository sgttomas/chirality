# S3 return: D-PEC-98 draft, transcribed

- **Executor:** `pec-task` (TASK, `claude-opus-5-5`, high). It was read-only, so HELP_HUMAN transcribed its final report verbatim from the host subagent transcript.
- **Brief:** `../briefs/S3_FIRST_SOWS_PROPOSAL.md`, SHA-256 `ef12b7408b68edb283055200de424169878fd3d122df43892d099432a8ea537a`. HELP_HUMAN also steered the task mid-run: the number is provisional, and the draft must be reconciled with `D-PEC-96` revision 4 (work-graph S3 row).
- **SHA-256 of the report text below (UTF-8):** `135037807ac1256ed58c7b052c976908b93421ca257ed1997ec8d9ffa9180b32`.

## Publication (HELP_HUMAN)

- **Proposal.** The draft is published unchanged as `_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md`, SHA-256 `ea7ac1ea3b81e0973b315f7ce3015db239e967115450850b9593a1c3084499b9`. That equals `D-PEC-98_DRAFT.md` in the preparer's `SHA256SUMS`. Its number becomes final with the register row in the same PR.
- **Evidence.** The rest of the `s3/` folder is published unchanged as `../../../PEC_FIRST_SOWS_D98_PREP_2026-09-26/`, including the candidates, `apply_d98.py`, the quote verifier and the evidence. Its `SHA256SUMS` verifies, except for the draft. A folder-local `.gitattributes` was added.
- **Basis.** The draft's basis is `8f9bd314c`. Since then, `origin/main` has moved to `6281273fa`: PR #940 carries the owner directions, and PR #941 publishes `D-PEC-96` revision 4. So revision 4 is now published, but still unruled. The draft cites it as unruled and unpublished, and it depends on no D-PEC-96 identifier.
- **Check.** HELP_HUMAN re-ran `apply_d98.py --check-only` on an export of `6281273fa`. It exited 0 with 2 `RENDER` lines.
- **Independent verification.** The scope-of-work `MODE=VERIFY` step is still outstanding. HELP_HUMAN dispatches a fresh verifier on this PR.

## Report (verbatim)

S3 return: I drafted D-PEC-98, the owner packet for the first Scope of Work contracts for DEL-02-08 (work-graph parser) and DEL-02-09 (MEMORY run-index parser). Both candidates pass every check I could run, but **the independent `MODE=VERIFY` step has not run**: I wrote the candidates, and a TASK cannot delegate. The draft's status line is PROPOSAL / AWAITING_RULING, and it labels the number D-PEC-98 as provisional. Your mid-task basis update (D-PEC-96 revision 4, Remaining sections) is folded in, and all hashes below are the final ones after that revision.

Brief hash verified (`ef12b740…537a`). Basis is `origin/main` `8f9bd314c` after `git fetch`. I started at `7a00a88df`; the only basis file that changed since is `write_status.sh`, and every check was rerun at `8f9bd314c`. I made no edits in the checkout and ran no state-changing git beyond the fetch.

**Draft and hashes**
- Draft: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s3/D-PEC-98_DRAFT.md`, SHA-256 `ea7ac1ea3b81e0973b315f7ce3015db239e967115450850b9593a1c3084499b9`.
- DEL-02-08 `ScopeOfWork.md`: `b28cf13d93851dc875575dafd759171205a75bc4bb63ef67e103fa2094d10b24` (255 lines).
- DEL-02-09 `ScopeOfWork.md`: `c9705ca28da82687e82bccdeb1bca5e271833d267c4afe23526965c4e13c7bd9` (228 lines).
- Both candidates sit under `s3/candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/<DEL folder>/ScopeOfWork.md`. Both files are new, so there are no preimages.
- Bound act script `s3/apply_d98.py`: `0f99d4b931c4e7189d111b96cd7f8c74f93751466b2dd2184a0a50b4e86881da`.
- Everything under `s3/`, including evidence, is listed in `s3/SHA256SUMS`, and it verifies clean.

**Recommendation: option A.** The act creates the two files and changes nothing else — no lifecycle, register, context or dependency file. Two add-ons are separate owner questions:
- **S:** move both deliverables OPEN → INITIALIZED with `write_status.sh` after validation, as D-PEC-63 did. I recommend it, but it is not assumed; with no answer, no status act happens.
- **M:** create both `MEMORY.md` files from the template at closeout. Recommended.

**Lifecycle answer**
- The `scope-of-work` method never touches `_STATUS.md`. Its default is `NO_STATUS_TOUCH`, and QA item 3 requires `_STATUS.md` to stay byte-identical.
- The SOW standard (§8) says INITIALIZED means the contract exists and validates. `project-setup` says recording INITIALIZED "is a separate authorized status act".
- So writing a first SOW only makes the deliverable eligible; the method does not require the transition.
- Without S, both stay OPEN with a valid SOW_V1 contract, which is a valid state. DEL-03-01's edges to them (E-P81, E-P82) stay unmet, but only in the advisory blocker view.
- The S postimages are recorded, with the act date as the only slot. The old and new editions of `write_status.sh` produce identical bytes.

**Dependencies on D-PEC-96 (not presumed ruled)**
- The contracts assume only that a loop's registry row may declare the work-graph and MEMORY run-index surfaces, which PRD v2.3 PEC-RCN-002 and §16.3 already say. They depend on no D-PEC-96 identifier.
- DEL-02-08 CLM-009 and DEL-02-09 CLM-008 cite the revision-4 vocabulary (`shared-dev-loop`, `loop-receipts-ledger`, `agentruns-json`, all v1) as unruled and unpublished. The direction behind it is recorded only on the unmerged branch `claude/pec-owner-directions-20260926` (`c0a668181`), so nothing relies on it.
- The parsers read no `## Remaining` section and depend on no profile that reads one. This is new DEL-02-08 CLM-018 and DEL-02-09 CLM-017, enforced in REQ-001 and the boundary requirement of each contract, with matching acceptance criteria and verification methods.
- The PRD §7.1 "remaining items" field is `_STATUS.md` content, which belongs to DEL-02-01's parser. Neither contract takes a PEC self-ingest fixture (FX-PEC-0) or any Remaining-reading fixture.
- The contract bytes stay valid whether D-PEC-96 is ruled as revision 4, ruled otherwise, or deferred. CON-002 stays open until the DEL-01-06 rebuild.

**Content required by the brief**
- Both contracts state the three fixture classes that SCA-005 §B7 assigns to X1, quoting §B7 verbatim: FC-1 receipt present, FC-2 evidence-only and FC-3 no AgentRuns record. They are pinned at `d61981ee2` as golden-by-reference fixtures with nothing copied into PEC's tree, plus synthetic edge cases.
- Open decisions are recorded as CON/TBD items, not assumed. The most important:
  - **CON-001 (both):** the accepted DEL-01-01 contract has no WorkGraph/WorkNode type and admits only JSON evidence into RunRecord.
  - **CON-002 (both):** no accepted registry declares feed profiles, and no dependency row links either parser to DEL-01-06.
  - **CON-003 (both):** node states, run tokens, dates and abbreviated SHAs fall outside what the DEL-01-03 guard admits.
  - **DEL-02-08 CON-005:** PRD §7.1 routes work-graph dependencies here, but SOW-095's field list does not name them.
  - **DEL-02-09 CON-004:** SOW-096 puts run tokens in dated MEMORY headings in scope, but those headings declare no token position.

**Checks (all at `8f9bd314c`, on scratch copies; outputs in `s3/evidence/`)**
- `validate_scope_of_work.py`: PASS format=SOW_V1 for both.
- `derive_review_checklist.py`: 21 and 17 items, in source order, bound to each candidate's hash; reruns are byte-identical.
- `check_boundary_owner_resolution.py`: 1 requirement checked and 0 failing per contract. The tool cannot check three per-act clauses per contract; I resolved those by hand, and each owner is named in its cited claim.
- Quote fidelity (`verify_d98_quotes.py`): 71/71 quotations match their cited sources. Negative controls fail as they should.
- Duplicate-ID scan (QA 19): clean. One quoted upstream ID was found in an earlier draft and fixed.
- Strict register validator, receipts validator and harness self-check: exit 0 before and after, with identical output.
- `git diff --check`: clean. Containment is exactly the two new files, and both `_STATUS.md` files are unchanged.
- Act-script prototype: check-only, apply and rerun exit 0 / 0 / 1, as designed.
- Reliance-hold preflight, `exact-correction-preparation`, on four targets: ALLOW ×4.
- Checked against the sibling SOWs and the revision-1.5 registers: the frontmatter, headings and ID form match. The basis pin `@c9e5cd87d` resolves on `origin/main`, where the siblings' `@3623b958b` does not.

**Owner questions**
1. A, amend or defer? Recommend A.
2. Add-on S, the status act? Recommended, but explicitly not assumed.
3. Add-on M, the MEMORY files? Recommended.
4. If SCA-006 checkpoint 3 (decomposition revision 1.6, PRD v2.4) merges first, the act script will stop on its pinned hashes. May the same ruling cover a bounded mechanical re-pin? Recommended, conditional on the quote check still passing. The quoted text is unchanged in the revision-1.6 candidate.
5. CON-005: leave it open and route it to the next scope change? Recommended.
6. Model steer.

**Unresolved**
- **Independent verification is outstanding.** The draft asks for a fresh read-only `MODE=VERIFY` on the packet's PR before the owner rules, and again at the act.
- D-PEC-96 is unruled, and revision 4 exists only as a branch record.
- The DEL-01-01 and DEL-01-06 contracts are stale; their rebuilds are graph node S2.
- The checkout moved to `claude/pec-owner-directions-20260926` (`a07f62190`) during my run, not by me.
- I briefly wrote one temp file directly in `/tmp` (hash list) and deleted it. My other scratch trees sit beside `s3/` in the scratchpad, as `s3proto.*`, `s3base.*` and `s3gitmeta.*`.

## Revision 2 (after PR #944 review 01)

The preparer's revision-2 report follows.

- **SHA-256 of the report text (UTF-8):** `7d5bb8e9bfaf6be0f79470fd9ab1f62954badbaa423d0e47504e83a30b330d73`.
- **Publication:** HELP_HUMAN replaced the published proposal with revision 2, SHA-256 `92b6f1a223f5cb6fffc399f16e5e4e63cf5d8aa8f391981d3afcb9f4027a3e40`. It also replaced the preparation folder with the revision-2 `s3/` contents; `SHA256SUMS` verifies except for the draft, and `.gitattributes` was added again. Revision-1 bytes stay recoverable at `47bf0c1c7`.

### Revision-2 report (verbatim)

S3 revision return. D-PEC-98 is revised as revision 2. Both blocking findings (B1, B2) and all six non-blocking ones (C1–C4, C8, C9) are addressed, and every check passes at the new basis. **The fresh independent `MODE=VERIFY` of revision 2 has not run yet**: I am the author and cannot delegate it. I did not see the verifier's report on revision 1; I worked from your relayed findings. The number D-PEC-98 stays marked provisional and the status line is still PROPOSAL / AWAITING_RULING (revision 2).

**Basis.** `origin/main` `53145aaeb`, after `git fetch`. PR #946 merged while I was revising (at `f90320c1d`, 07:31Z), so I moved the observation commit from `5bbc9de22` to `53145aaeb` and reran every check there. PR #947 (the generic `change` workflow) also landed; it changed `workflows/index.json`, but the `scope-of-work` entry is unchanged. I made no edits in the checkout and wrote only under `scratchpad/s3/` and my own temp directories.

**New hashes (SHA-256)**

| File | Hash |
|---|---|
| Draft `s3/D-PEC-98_DRAFT.md` | `92b6f1a223f5cb6fffc399f16e5e4e63cf5d8aa8f391981d3afcb9f4027a3e40` |
| DEL-02-08 `ScopeOfWork.md` (262 lines) | `03cce13f484a9b595b5162bd662af42bcd67aae37a8843304bf03cfbb3badc0a` |
| DEL-02-09 `ScopeOfWork.md` (235 lines) | `aafb54fd6457f09da8304ead444686703d5f8d2c28f4c94ec4eab4d2737b188b` |
| `apply_d98.py` (bound act script) | `19c2ecb6bd40082c2397956dee2e0efb48b7a2aef5ec56e7498d4ed5e2fc419e` |
| `verify_d98_quotes.py` | `9cadc2c44359c9ea2d4d20c6a95122e9be02cf221612032f0c5bf6a06cadb745` |
| `verify_d98_state_claims.py` (new) | `7bb9e6bbe3ad6e2bfa68c19c56c8b2e786b91f2e362c2a5e9e2fdddbc598b673` |
| `test_apply_d98.py` (new) | `ad7dce86b07d5c0fd36fb4ed46324b40be4d30559be2b0c18d258ffcc3e79a7a` |
| `run_d98_checks.sh` | `abc20da2d6fa8e3a590997ef6b15848449869fa23dd492ef5c41c110e9793b8d` |
| Checklist DEL-02-08 | `54c84487…e2db` |
| Checklist DEL-02-09 | `2f495a54…86f3` |

Everything is listed in `s3/SHA256SUMS`, which verifies clean.

**What changed**
- **B1 (false "at the basis" claims).**
  - Each contract now has an "Observation commit" paragraph. The pin `c9e5cd87d` binds only the accepted register and PRD bytes, and every unanchored state claim is an observation at `origin/main` `53145aaeb`. The phrase "at the basis" is gone from both contracts.
  - DEL-02-08 CLM-013 gives the template and workflow hashes at both commits (`4411d0c2…`/`24268f35…` at the pin, `5661c609…`/`3e197c9d…` now) and names the Root commit that changed them (`ea5009d05`).
  - D-PEC-96 now reads: revision 4 merged at `6281273fa`; at `53145aaeb` the register row says `RULED A / EFFECTIVE ON MERGE`, with the ruling record merged at `f90320c1d`. The registry act is not applied yet (`loops.json` is still schema version 1, with no feed profiles). The contracts still rely on no D-PEC-96 identifier.
  - While revising I also found and anchored one more unanchored claim, the fixture-blob "unchanged at `origin/main`".
- **B2 (strict-validator row).** The row now requires the exit code and output to match the pre-act run, and names the 26 pre-existing D-GOV-48 `XRG-013` warnings (0 errors, exit 1 under `--strict`). The notice is recorded as finding 10.
- **C1.** "Entry counts per file" is dropped from DEL-02-09 REQ-003 and AC-003, which now extract only the three SOW-096 fields "and no other field".
- **C2.** Question 4 now names:
  - the three places each candidate changes on a re-pin;
  - how `TARGETS` and `PINNED` are re-bound (new candidate hashes, plus the four register/PRD pins at the new basis; the other four pins stay);
  - the word-diff record and the verifier check on it;
  - why the other "revision 1.5" and "PRD v2.3" mentions stay: each is verbatim accepted text or an observation at a named commit;
  - how the basis moves while the observation commit does not.
- **C3.** Every quote check now requires the text in the candidate and at its source. Building this caught two revision-1 defects:
  - DEL-02-09 cited PEC-K-10 without quoting it, so that check was wrongly applied to it; the check is now DEL-02-08-only.
  - DEL-02-09 quoted a fragment ("S, LOW") too short to verify; the quote is now the full §8 sentence.
- **C4.** The grant table names both `MEMORY.md` paths.
- **C8.** Add-on S runs after the scope-of-work run returns, as one generic-shell TASK dispatched by WORKING_ITEMS (the D-PEC-63 pattern), with only the two `_STATUS.md` files as allowed targets.
- **C9.** `apply_d98.py` now:
  - writes through temporary files and removes any created target and temp on every post-write failure, so on exit 1 nothing is left behind;
  - inventories all of `projects/pec` before and after, and requires the difference to be exactly the two created files.
  - It detects, but cannot revert, a change made by another process; the draft says so.

**Checks** (`evidence/RUN_D98_CHECKS_at_53145aaeb.out`; the method's mechanical checks rerun by me):
- `validate_scope_of_work.py`: PASS format=SOW_V1 for both.
- `derive_review_checklist.py`: 21 and 17 items, in source order, bound to each candidate's hash; reruns byte-identical.
- `check_boundary_owner_resolution.py`: 1 checked, 0 failing, per contract. The three per-act clauses per contract that the tool reports as `NOT_CHECKABLE` are resolved by hand in the draft.
- Quote check: 69/69, two-sided.
- State-claim check: 44/44, read with `git show` at each named commit.
- ID-collision scan: clean.
- Strict register validator: exit 1 before and after, identical output (26 `XRG-013`, 0 errors).
- Receipts validator and harness self-check: exit 0 before and after, identical output.
- `git diff --check`: clean. Containment is exactly the two new files, and both `_STATUS.md` files are unchanged.
- Reliance-hold preflight: ALLOW on all six targets.
- Add-on S prototype: its postimages are identical under three editions of `write_status.sh`.
- Act prototype: check-only, apply and rerun exit 0 / 0 / 1.
- Fault injection: 5/5.
- Negative controls fail as they should: the validator and checklist refuse a broken matrix; source-side quote mutations fail 3 checks; candidate-side mutations fail 2, including a reintroduced "At the basis".

**Unresolved**
- A fresh independent `MODE=VERIFY` of revision 2 is outstanding.
- The draft file carries no filing-name slot for the provisional number; it uses the name already published in PR #944.
- CON-001 and CON-002 stay open until the DEL-01-01 and DEL-01-06 rebuilds (graph node S2) and the D-PEC-96 act are applied.
- If SCA-006 checkpoint 3 lands before the act, question 4's re-pin procedure applies.
