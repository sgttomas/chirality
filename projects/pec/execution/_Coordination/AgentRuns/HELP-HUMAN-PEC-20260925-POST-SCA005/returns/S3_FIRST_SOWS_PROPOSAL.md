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
