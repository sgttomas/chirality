# Review 02 of PR #944 (D-PEC-98 revision 2; MODE=VERIFY re-verification), transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 01 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. It authored nothing in the packet. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `be8459f49222d3f59ac125e9294d2e0301fbf5a6`. This file is the only addition after that head.
- **SHA-256 of the report text below (UTF-8):** `9ea2bc8ab9df014f878b290714c11bf0dbb5e1384f3e5c8012df6a676e220015`.

## Report (verbatim)

**PR #944 re-verification (review 02, D-PEC-98 revision 2): overall PASS.** Both candidates pass MODE=VERIFY. Every earlier finding I was asked to recheck is genuinely resolved, and I found no new blocking issue. There are six non-blocking notes: one on contract wording, one on the act script's operation, and four on HELP_HUMAN's records.

Head confirmed: `gh pr view 944` gives `be8459f49222d3f59ac125e9294d2e0301fbf5a6`, OPEN. `origin/main` is `53145aaeb`, which is also the merge-base. I worked read-only in a fresh `mktemp -d` (`rv2.*`), from `git archive` exports of head and base and my scratch `--shared` clone. The checkout is unchanged.

## 1. MODE=VERIFY (bundled `scope-of-work` at `53145aaeb`)

**Method and tools.** The method files are unchanged from review 01: `WORKFLOW.md` `d616865a…`, `execution.json` `4ad8b7eb…`, `brief.md` `a082f1af…`, `tools.md` `2bbb55cc…`, `checks.md` `fbb2c8eb…`. So are the SOW standard (`26c8254a…`) and the tools (`f0f10590…`, `bfb64dc9…`, `22ef57e0…`, `61a34722…`, `7a1f8a12…`). Only `representation-migration.md` changed (`698957a5…`), and it is conversion-only. The `scope-of-work` index entry is identical at `6281273fa` and `53145aaeb`.

**Verdicts:**
- **DEL-02-08** (`03cce13f…dc0a`): **PASS.** Schema and mechanical PASS; project content PASS; no substrate issue.
- **DEL-02-09** (`aafb54fd…188b`): **PASS.** Same.

**QA subset for VERIFY:**
- **Items 1, 3, 4, 8, 9 pass.** Both `_STATUS.md` are unchanged after the act. Validator `PASS format=SOW_V1` ×2, and the JSON equals the evidence files.
- **13 passes.** 21 and 17 items, in source order; reruns are identical and equal the evidence (`54c84487…`, `2f495a54…`).
- **18 passes.** I re-ran the negative control on revision 2: removing a matrix row gives `FAIL format=INVALID`, and the checklist exits 1 with no artifact.
- **19 passes.** 106 and 90 local definitions. The only bare upstream ID is `CON-001` inside the column-0 blockquotes that carry the carve-out (08 L120, 09 L111).
- **20 passes.** One AC per matrix row.
- **21 passes.** Tool: 1 checked, 0 failing, per contract. The hand resolution holds: 08 REQ-009/010/011 → DEL-04-05, DEL-01-03 and DEL-04-03, each named in CLM-011; 09 REQ-007/008/009 → the same owners, each named in CLM-010. 09 REQ-006's join owner stays TBD-006, which is correct because no source names one.
- **15 and the CONVERT-only items are not applicable.**

**Claim-by-claim checks.**
- **Checks I re-ran:** the 69/69 two-sided quote check and the 44/44 state-claim check (`verify_d98_state_claims.py`, run against the checkout's object store). Both outputs are byte-identical to the evidence.
- **Independent checks at `53145aaeb`:**
  - The D-PEC-96 register row reads `RULED A / EFFECTIVE ON MERGE`.
  - The ruling file `852057f0…` is absent at `f90320c1d^1` and present at `f90320c1d`.
  - `loops.json` still has `"schema_version": 1` and no feed profiles.
  - DEL-01-06 is `INITIALIZED` and its SOW is still `5fdcfd96…`.
  - At the pin `c9e5cd87d`, the template (`4411d0c2…`) has the six-token rule but not the second sentence.
  - `_LATEST.md` records the three register hashes at both commits.
  - The `project-setup` quotes hold (`method.md` L158, `contract.md` L72–73).
  - The wave-3 and change-generic notices both say the owner defers action.
  - The five fixture blobs are unchanged.
  - PR #950 (the D-PEC-96 act) is still open, so every claim anchored at `53145aaeb` holds whether or not it merges first.

## 2. Earlier findings: all genuinely resolved

- **B1 (claims false at the named basis): resolved.**
  - The phrase "at the basis" is gone from both contracts, and the quote check fails if it reappears.
  - Each contract now has an Observation-commit paragraph (08 L28–34, 09 L29–35) that anchors unanchored state claims to `53145aaeb`.
  - 08 CLM-013 gives the template and workflow hashes at both commits.
  - The D-PEC-96 wording is exact at `53145aaeb` (08 CLM-009 L94, 09 CLM-008 L85). Neither contract relies on a D-PEC-96 identifier. Anchoring to a named commit makes the claims robust to the act and to later changes.
- **B2 (strict-register row): resolved.** The row (proposal L253) now requires identical exit and output, and names 26 `XRG-013` warnings with exit 1. I reproduced exactly that at base and at head, with identical output.
- **C1: resolved.** DEL-02-09 REQ-003 (L134) and AC-003 (L151) now say "no other field".
- **C2: resolved.** Question 4 now names:
  - the three places that move in each candidate;
  - which "revision 1.5" and "PRD v2.3" mentions stay, and why;
  - how `TARGETS` and the four register/PRD `PINNED` entries are re-bound, with the other four pins unchanged;
  - the word-diff record the verifier checks;
  - the state-script extension.

  The premise holds: the quoted rows are identical in the revision-1.6 candidate.
- **C3: resolved.** Every check requires the text in the candidate and at the source. Candidate-side mutations I made, one per candidate, each failed the right check (67/69).
- **C4: resolved.** The grant table names both `MEMORY.md` paths.
- **C8: resolved.** Add-on S is now a separate generic-shell TASK with no workflow selected, run after the scope-of-work run returns, as in D-PEC-63 §3.2. I reproduced the S postimages with the `53145aaeb` `write_status.sh` edition (`1857ad59…`): `4341d6b2…` and `e67be587…`.
- **C9: resolved.** On a fresh export, `apply_d98.py`:
  - check-only exit 0, prints `CHECK write set = grant`;
  - apply exit 0: "2 created, 0 modified, 0 removed; pinned 8/8";
  - rerun exit 1;
  - `diff -r` shows exactly the two files.

  `test_apply_d98.py` passes 5/5. I read the cleanup paths: a failed temp write, a failed second rename, and a failed post-write check each leave no target and no temp file.

## 3. New in revision 2 (non-blocking)

- **N1. Candidate wording** (08 L33–34, 09 L34–35): "`_CONTEXT.md` and `_REFERENCES.md` name revision 1.5 and PRD v2.3". At `53145aaeb`, `_CONTEXT.md` names only revision 1.5; `_REFERENCES.md` names both. It is true only if read as the two files together, which is how the state check tests it. This wording was carried over from revision 1, and I missed it in review 01. Tighten it if the candidates are respun for any other reason.
- **N2. Act script operation.** The inventory covers all of `projects/pec`, including the run root. So any concurrent write there aborts the act. I showed this: `PYTHONUNBUFFERED=1 … > <run root>/apply.out` exits 1 with `modified=[…/apply.out]` and rolls back cleanly, while buffered output happens to pass. It fails safe, but the proposal should say to capture the act's output outside `projects/pec`, or only after the act exits. Separately, there is a negligible race: a target created by another process between preflight and rename would be overwritten, then removed on rollback.

## 4. Publication fidelity: PASS

- The proposal `92b6f1a2…3e40` equals the `SHA256SUMS` draft entry, and is byte-identical to the drafter's `s3/D-PEC-98_DRAFT.md`.
- `SHA256SUMS` verifies every other entry.
- The prep folder equals `s3/` plus `.gitattributes`.
- The return's revision-2 report hash `7d5bb8e9…` recomputes correctly (text with trailing newline stripped). So does the revision-1 hash `13503780…`.
- `REVIEW_PR944_01.md` hash `31c5010e…` recomputes, and the transcription matches my report.

## 5. HELP_HUMAN's records

**True as written:**
- **Register row:** 6 columns, accurate. It now names the M paths, the revision-2 hashes, and revision 1 superseded.
- **STATUS:** the D-PEC-96 ruling with its act in progress (PR #950 is open), and the retirement undertaking opened.
- **Owner direction record:** quoted verbatim with its date, including "open RS1".
- **Retirement graph:**
  - 57 deliverable Remaining sections at `53145aaeb`: confirmed.
  - The 73 D-PEC-83 residuals (70 held plus 3 conditional) and 92 items match the D-PEC-83 proposal.
  - Precedent commits `82f4a16ce` and `1f78abfd4`, and the Piping `TM_PIP_REMAINING_RETIREMENT_20260922/` folder, exist.
  - It is acyclic.
- **Main graph:** acyclic in substance; the only S2↔S3 loop comes from "as for" wording.
- **Briefs:** G2 and RR1 stay inside their write fences.
- **Review 01 items:** C6 and C7 are applied.

**Stale or inaccurate** (records only, in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`):
- **G-a (L135):** "Next work" still lists "The owner's decision on RS1", though RS1 is COMPLETE.
- **G-b (L142):** "G1: the preparer handed back revision 4 … nothing is running from it" contradicts the G1 row: the act is running under brief G2, PR #950. The L156 evidence row still says the next step for revision 4 is the owner ruling.
- **G-c (L97, L114):** the triage header says "seven later Root notices" and the sub-heading says "Four more", but only three new notices exist and three are listed. The correct figures are six later notices and three more.
- **G-d (L183):** the D-PEC-88 tenth-PR trace names the D-PEC-98 and D-PEC-96 STATUS bullets, but not the rewritten Remaining-retirement bullet (STATUS L249–252). C5 is only partly carried forward.

## 6. Hygiene

- `git diff --check origin/main...HEAD` is clean.
- Harness self-check exits 0 and the receipts validator exits 0, both with output identical at base and head.
- The strict validator exits 1 with 0 errors and 26 `XRG-013` warnings, identical at base and head.
- Reliance preflight `candidate-validation` returns ALLOW on both `ScopeOfWork.md` and both `MEMORY.md` targets.

Main files:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_D98_PREP_2026-09-26/`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/WORK_GRAPH.md`

## HELP_HUMAN disposition

The overall verdict is PASS, and both candidates pass MODE=VERIFY. The PR merges at the reviewed content with this file added.

- **N1** (the candidate wording about contexts and references) is disclosed to the owner. It is tightened only if the candidates are respun.
- **N2** (capture act output outside `projects/pec`) goes into the act brief, and is disclosed.
- **G-a to G-d**, which concern the graph records, are fixed in HELP_HUMAN's next graph update.
