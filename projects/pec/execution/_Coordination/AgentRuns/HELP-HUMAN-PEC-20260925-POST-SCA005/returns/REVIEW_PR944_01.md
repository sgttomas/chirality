# Review 01 of PR #944 (D-PEC-98; scope-of-work MODE=VERIFY and packet review), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the packet. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `47bf0c1c7f24e76902e21ef6b7305d921aaf29d4`.
- **SHA-256 of the report text below (UTF-8):** `31c5010e268380cf1c99227a1a764c62dd1371c8eda14756367d399672504345`.

## Report (verbatim)

**PR #944 review (D-PEC-98 first SOWs, DEL-02-08 / DEL-02-09): overall FAIL.** There are two blocking findings. Both have narrow fixes. Everything else checked holds, and the act script behaves exactly as bound.

Head confirmed: `gh pr view 944` gives `headRefOid` `47bf0c1c7f24e76902e21ef6b7305d921aaf29d4`, state OPEN. Base is `origin/main` `6281273fa`, which is also the merge-base. I authored nothing in this packet. I worked read-only, on `git archive` exports and a `git clone --shared` in my scratchpad; I changed nothing in the checkout.

## A. Independent MODE=VERIFY (bundled `scope-of-work` at `6281273fa`)

**Method files and their SHA-256:**
- `WORKFLOW.md` `d616865a…6fbd8b`
- `execution.json` `4ad8b7eb…a26d`
- `resources/brief.md` `a082f1af…5145`
- `resources/tools.md` `2bbb55cc…0f3f`
- `resources/checks.md` `fbb2c8eb…76b8`
- `representation-migration.md` `43459252…6729` (not applicable)

**Standards:**
- SOW standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` `26c8254a…433c`.
- Transition contract: D-GOV-16 item 4 (`D-GOV-16_deliverable_scope_of_work_stage2.md` `67921b04…ef38`), recorded as RULED APPROVED in the governance register.

**Tools** (hashes equal the packet's): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py` `61a34722…0389`, `id_catalog.json` `7a1f8a12…757`.

**Verdicts (the method has no separate content verdict, so I use checks.md: "any failure produces a failed return and rerun requirements"):**
- **DEL-02-08** (`b28cf13d…0b24`): **FAILED.** Schema and mechanical checks PASS. Project content FAILS on claim grounding (B1: CLM-009, CLM-013). Rerun is required after repair.
- **DEL-02-09** (`c9705ca2…7bd9`): **FAILED.** Schema and mechanical checks PASS. Project content FAILS on claim grounding (B1: CLM-008).
- Execution substrate: no issue. CPython 3.13.7, no network. Tools run on my own apply of `6281273fa`.

**QA subset for VERIFY:**

| QA item | Result |
|---|---|
| 1 | PASS, by interpretation. New PROJECT/SOFTWARE deliverables use SOW_V1 under D-GOV-16 item 4; no pilot variance applies post-activation. |
| 3 | PASS. Both `_STATUS.md` byte-identical after the act: `d80800a4…`, `3e14313c…`, state `OPEN`. |
| 4 | PASS. `PASS format=SOW_V1` ×2; `--json` output equals the evidence files. |
| 8, 9 | PASS. Every OUT carries SOW-095/096 and OBJ-001/002. Every AC maps to a VER or `HUMAN_REVIEW`. |
| 13, 18 | PASS. 21 and 17 items, in source order, bound to the candidate hashes. Reruns are byte-identical and equal the evidence `aec6d9bf…b0e5` and `a66599e4…e1c8`. Negative control (matrix row removed): `FAIL format=INVALID`, and the checklist refuses with no artifact. |
| 19 | PASS. My own scan: the only bare upstream ID is `CON-001` inside the column-0 blockquotes that carry the carve-out (08 L113, 09 L104). All other cited IDs are qualified. |
| 20 | PASS. One AC per matrix row. |
| 21 | PASS. Tool: 1 checked, 0 failing, per contract; boundary JSON equals the evidence. Hand resolution of the NOT_CHECKABLE clauses: 08 REQ-009→DEL-04-05, REQ-010→DEL-01-03, REQ-011→DEL-04-03 (each named in CLM-011); 09 REQ-007/008/009 → the same owners (CLM-010). 08 REQ-005 (completion→DEL-04-01, lag→DEL-03-03) also resolves via CLM-011. Note: 09 REQ-006's excluded join has no owner. It is disclosed as TBD-006, which is correct, since no accepted source names one. |
| 15 | Not applicable (no HTML). |
| 2, 5–7, 10–12, 14, 17 | Not applicable (INIT). |
| 16 | This report keeps schema, content and substrate findings separate. |

**Claim-by-claim checks. These passed:**
- SOW-095/096 ledger rows, verbatim.
- Deliverables.csv DEL-02-08/09 fields (Type, envelope, PhaseHint, artifacts, notes, ResponsibleParty `TBD`).
- ContextBudgetQA: MEDIUM/"Hold as M…" for DEL-02-08; LOW/None for DEL-02-09.
- Every PhaseHint in 08 CLM-010 and 09 CLM-009.
- Every sibling and consumer SOW mapping in CLM-011 and CLM-010.
- Dependencies.csv DEP-02-08/09-001..003, DEP-03-01-015/016, and E-P79..82. No edge to DEL-01-06.
- §B7 verbatim at Propagation_Plan L884, including the FC-1/2/3 names. §B4 carry-forward at L867.
- IA §9.3 and R-01, R-02, R-08, R-09.
- DL-4 "one per feed kind".
- PRD text for PEC-RCN-002, §7.1, K-10, ORI-004/006, RCN-004/006, SVC-001/002, and C6/C7/C8.
- Upstream SOW, guard and state facts for DEL-01-01, DEL-01-03 and DEL-01-06.
- The five IA §9.3 blobs resolve at `d61981ee2` and are unchanged on main.
- 08 CLM-017 corpus facts at `7a00a88df`: 5 canonical graphs; the spelling split; 2 of 3 trials with folder name ≠ run ID; the T0R/B3A/D72/M01 node IDs and Deferred/ROUTE/PARTIAL/REFERENCE tokens; 53 `WORK_GRAPH.md` files at `d61981ee2`.
- 09 CLM-016 corpus facts: 156 = 54/101/1; 4 bullet `## Runs`; 145 dated; 7 neither.
- 09 CLM-013: exactly 4 `## Runs` files at `d61981ee2` (App DEL-05-04; Piping DEL-08-01, 08-05, 10-04).
- D-PEC-96: in both revisions, `shared-dev-loop` covers `work-graphs` and `memory-run-index`.
- The definition counts in the proposal's table.

## B. Blocking findings

**B1. "At the basis" claims are false at the basis the contracts name.** Affects both candidates.
- **Where:**
  - DEL-02-08 `ScopeOfWork.md` L87 (CLM-009) and L94 (CLM-013).
  - DEL-02-09 L78 (CLM-008).
  - Candidate paths: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_D98_PREP_2026-09-26/candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/<DEL>/ScopeOfWork.md`.
- **Why it fails:** each contract's Purpose (L19–26) defines the basis as the pin `c9e5cd87d`, then says "At the basis, …". At `c9e5cd87d`:
  - the PEC register has no D-PEC-96 row, so 0 matches (revision 3 arrived in PR #928, `6721457be`, which is not an ancestor of the pin);
  - the work-graph template hashes to `4411d0c2…`, not `5661c609…`, and the workflow to `24268f35…`, not `3e197c9d…`. Wave 2A (`ea5009d05`) is after the pin.
- **Consequence:** these claims are true only at `8f9bd314c`, a commit the contracts never name. They are also already stale on this PR's own base: PR #940 merged the direction record, and PR #941 published revision 4 (`4506597b…`). Yet CLM-009/008 say "revision 4 is unpublished". The proposal's robustness argument (L76, "written as of the basis … dated, not false") depends on an anchor the contract text does not carry. The contracts' dependency on D-PEC-96 (none on its identifiers) is stated correctly; only these state claims are mis-anchored.
- **Fix:** anchor each statement explicitly, the way CLM-017/016 already do with "At `origin/main` `7a00a88df`". Either write "at `origin/main` `8f9bd314c`", or restate the current fact: revision 4 published at `6281273fa`, still `PROPOSAL / AWAITING_RULING`. Then rehash, and update:
  - the proposal tables;
  - `apply_d98.py` `TARGETS`;
  - `SHA256SUMS`;
  - the checklist hashes;
  - the register row.

**B2. The strict-register check in Finite verification can no longer pass on current main.**
- **Where:** proposal L205 (`/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md`). It requires "exit 0, 0 errors / 0 warnings, output identical to the pre-act run".
- **Evidence:** at `6281273fa` and at head, `validate_decomposition_registers.py --strict projects/pec/execution` exits 1 with 0 errors and 26 `XRG-013` warnings. This comes from D-GOV-48 (PR #942, validator commits `91f423ab8`…`de2a3b078`). `NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md` confirms "exit 1 only under `--strict`" and that the owner defers action.
- **Consequence:** the act's own verification row would fail on a condition the act did not cause.
- **Fix:** restate the required result as "exit code and output identical to the pre-act run (at `6281273fa`: exit 1, 0 errors / 26 pre-existing XRG-013 warnings)". This is a proposal-text change: rehash the proposal and update `SHA256SUMS` and the register row. Record the D-GOV-48 notice in Findings item 7 or in the graph.

## C. Non-blocking findings

1. **DEL-02-09 adds "entry counts per file".** REQ-003 (L127) and AC-003 add it, beyond SOW-096's extraction set. This contradicts its own CLM-005 ("the extraction set is run-ID tokens, dates, link targets … not strengthened") and the proposal's L44 ("exactly"). Drop it, ground it, or mark it TBD. Best folded into the B1 re-preparation.
2. **Question 4 (conditional re-pin) is bounded but incomplete.** Its premise holds: I overlaid the SCA-006 CP2 candidate registers and PRD v2.4, and `verify_d98_quotes.py` still passes 71/71. The quoted rows are identical in the candidate. But:
   - Q4 does not say how the bound `apply_d98.py` `TARGETS`/`PINNED` hashes get re-bound.
   - It should state that the other "revision-1.5" and "PRD v2.3" mentions stay by design: 08 L43, 45, 86, 118, 177, 181; 09 L45, 47, 77, 109, 160; and the `_CONTEXT`/`_REFERENCES` sentence.
   - After a re-pin, "the basis" would become the revision-1.6 commit, which compounds B1.
3. **The quote verifier's coverage is narrower than 71/71 suggests.** Many of its checks search the source for hard-coded phrases without confirming the candidate contains them (`verify_d98_quotes.py` L67–74, 77–79, 86–120). My independent spot-checks found no defect. The act-time rerun, and any Q4 re-pin, should rely on a stronger check.
4. **Register row incomplete.** `_REGISTER.md` L115 "Blocks" says "exactly the two new `ScopeOfWork.md` paths" but omits add-on M's two `MEMORY.md` paths. D-PEC-96's row names its MEMORY path "on the owner's answer".
5. **D-PEC-88 trace incomplete.** `WORK_GRAPH.md` L178 names only the D-PEC-98 STATUS line. The same PR also rewrites the D-PEC-96 bullet in `docs/STATUS.md` L233–235.
6. **Graph misses the D-GOV-48 notice.** The graph's checked basis (L126) is `6281273fa`, which includes PR #942. Its notice is not in the triage, and the D-GOV-47 entry (L112, "No action") is now superseded.
7. **S2 row wording.** The S2 row (L62) calls `_CONTEXT.md` a "decomposition surface" (it is deliverable-local). It also says "waits for the next PEC scope change", where D-PEC-96 revision 4 L96 says the text is carried to S2 "as before". Graph-only; outside the D-PEC-98 act.
8. **Add-on S actor differs from its precedent.** D-PEC-63 §3.2 used a separate generic TASK with no skill loaded. D-PEC-98 has the same WORKING_ITEMS instance run `write_status.sh`. State that S runs after, and outside, the scope-of-work run, so `NO_STATUS_TOUCH` holds literally.
9. **Nits in the proposal and act script:**
   - `apply_d98.py` and proposal L191 say "nothing written on any failure"; that is true only before the write.
   - "Write set equals the grant" is enforced by the hard-coded `TARGETS`, not by a check.
   - Proposal L62 and L109 are present-tense as of `8f9bd314c`; the return's Basis bullet corrects them.

## D. Owner-decision review items

1. **Truthfulness.** Holds as listed under A, except B1 and C1.
2. **Remaining sections: confirmed.**
   - Neither contract reads `## Remaining`: 08 REQ-001/015, AC-015, VER-015; 09 REQ-001/013, AC-013, VER-013.
   - Neither contract depends on a profile or surface that reads Remaining sections. Revision 4 removes `status-remaining`.
   - FX-PEC-0 is excluded (08 CON-004, 09 CLM-013). The only Remaining text left is the verbatim §B7 quote.
3. **D-PEC-96.** No reliance on its identifiers (TBD-004 and TBD-003). The contracts are robust to any ruling: REQ-001 falls back to "no declaration → nothing discovered, reported". The state description is the B1 defect.
4. **CON and TBD items are genuine open decisions, grounded in sources:**
   - CON-001: the fourteen-type DEL-01-01 contract with RunRecord limited by REQ-006, versus the revision-1.5 row.
   - CON-002: DEL-01-06 is strict v1, and no edge links the parsers to it.
   - CON-003: the guard admits only `OPEN`..`ISSUED` and 40/64-hex digests.
   - 08 CON-005: the PRD DependencyEdge text and the SOW-015 Notes, versus the Needs column in prose.
   - 09 CON-004: SOW-096's dated-heading scope, versus observed headings with no declared token position.
5. **Lifecycle answer: correct.**
   - The method is `NO_STATUS_TOUCH`; standard §8 agrees; `project-setup` `method.md` L157 matches the quote.
   - Add-on S is not assumed: with no answer, no status act happens.
   - I reproduced S with the `d2c4def1` edition of `write_status.sh` (identical at `8f9bd314c` and `6281273fa`). It gives `4341d6b2…04fe` and `e67be587…1056` at 2026-09-26.
6. **Act script (on my export of `6281273fa`).**
   - `--check-only` exit 0, 2 RENDER lines. Apply exit 0: "targets 2/2 byte-exact; pinned 8/8 unchanged". Rerun exit 1, nothing written.
   - `diff -r` shows exactly the two new files. Both `_STATUS.md` unchanged.
7. **Grant, rollback, limits, questions.**
   - Nothing grants a register, context, dependency, `v2/**` or PRD change. CHECKING appears only as a non-grant with no prompt.
   - Rollback is sound.
   - Q4 is appropriate in kind but should be tightened (C2).
8. **Publication fidelity.**
   - The proposal equals the draft entry `ea7ac1ea…99b9`; it is byte-identical to the drafter's `s3/D-PEC-98_DRAFT.md`.
   - `SHA256SUMS` verifies every other entry.
   - The prep folder equals `s3/` plus `.gitattributes`. The only other addition is the return.
   - The return's report-text hash `13503780…0b32` matches (UTF-8, trailing newline stripped).
9. **Register row, graph, STATUS.**
   - Register row: 6 columns, accurate apart from C4.
   - Graph: the S3 ACTIVE and G1 BLOCKED states are truthful. The dependencies are acyclic in substance; the only textual S2↔S3 loop is from "as for" wording. The D-PEC-88 trace is present (C5).
   - Hygiene: `git diff --check origin/main...HEAD` is clean. Harness self-check exits 0 and receipts validator exits 0, both with output identical to base. The strict validator exits 1 identically at base and head (B2).
   - Reliance preflight `candidate-validation` on both targets: ALLOW. The holds register has only its header row.

Main files:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_D98_PREP_2026-09-26/`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md`

## HELP_HUMAN disposition

FAIL. MODE=VERIFY failed both candidates on claim grounding (B1), and the packet failed on the strict-validator row (B2). HELP_HUMAN returned the packet to the S3 drafter with B1, B2, C1–C4, C8 and C9. The drafter produced revision 2, which replaces revision 1 in this PR.

HELP_HUMAN fixes C5–C7 in its own records: the D-PEC-88 trace, the D-GOV-48 notice triage and the S2 wording. Revision 2 gets a fresh MODE=VERIFY.
