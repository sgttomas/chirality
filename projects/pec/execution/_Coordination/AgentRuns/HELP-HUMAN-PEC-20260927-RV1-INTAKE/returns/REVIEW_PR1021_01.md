# Review 01 of PR #1021, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `baf3c130894cfdbf5663741e9378dc097cf30fb6`. The repairs listed under Disposition, this file and a merge of `origin/main` follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `4c6c87783d4d434155ed2b1dcfa3de0207dcdfb016ea332ca66826aeef5abb7a`.

## Report (verbatim)

**Verdict: PASS WITH NOTES.** I found no blocking findings, 3 non-blocking findings and 4 notes.

I reviewed PR #1021 (TM1 of HELP-HUMAN-PEC-20260927-RV1-INTAKE) at head `baf3c130894cfdbf5663741e9378dc097cf30fb6`. `git ls-remote` confirms that head for `claude/pec-tm1-intake-dispositions`, and confirms `main` = `bc1ea504d`. The merge-base is `acc7d3cc7` (the PR #1018 merge). Between the merge-base and `origin/main`, nothing changed under `projects/pec`, `execution/_Coordination`, `.github`, `tools/{hosted-ci-routing.json,taskmgmt,validation,practitioner_harness}`, `_DomainEngines` or the other loops' Task Management folders.

I made no edits, no fetch and no checkout in the repository. I read the bytes through `git archive` into my scratch directory. To run the git-dependent validators, I used throwaway scratch-only git repos that borrowed the real object store read-only. I deleted the scratch directory afterwards.

## BLOCKING
None.

## NON-BLOCKING

**N1. The return misdescribes the Piping precedent, and the ELEVATED status departs from it.**
- Locator: `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/TM1_INTAKE_DISPOSITIONS.md:30`. It cites "Piping `TM-PIP-030` (ELEVATED-to-Root form)".
- What the live row says: TM-PIP-030 in `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv` is `Status=OPEN`, with `ElevatedTo=Root`. Its Notes say "Status remains OPEN and ElevatedTo is Root exactly as ruled". TM-PIP-031 has the same form.
- Across all four federated registers, live and closed, TM-PEC-027 is the only `ELEVATED` row. The federation run reports `ELEVATED=0` for ROOT, APP and PIP.
- The choice is still valid and defensible:
  - `taskmgmt.py` L75 lists `ELEVATED`, and L218 requires `ElevatedTo` with it.
  - The workflow contract (`resources/contract.md` L20) names the state.
  - `plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md` §6.2 (L320–325) describes exactly "ELEVATED + ElevatedTo + notice, linked rows not a move".
  - The row discloses the reading as WORKING_ITEMS's (REGISTER.csv L12 Notes).
- The only precedent points the other way, and the return mis-cites it. Correct the return's parenthetical (TM-PIP-030 is OPEN with ElevatedTo Root). Optionally, have the row's disclosure cite PRD candidate §6.2 as the source of "the register's elevation form", which the row currently leaves unnamed.

**N2. The graph contradicts itself on RV1's state.**
- `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md:25` still reads "PLANNED — ready when DIR merges".
- L34 and L36 of the same file say "RV1 is running" and "the RV1 manager is running the REVIEW".
- The branch exists: `claude/pec-rv1-d1-review` is at `d6ed711f6`.
- The RV1 row should read ACTIVE, with the branch named, so that recovering from the table gives the true state.

**N3. The MEMORY grant is recorded only as graph evidence.**
- Locators: `WORK_GRAPH.md:43` and `:27`.
- `projects/pec/AGENTS.md` L292–295 says a MEMORY row "needs the path grant of the undertaking's governing `D-PEC` packet … Name the affected `MEMORY.md` paths in that packet." The same file, L300–306, keeps rulings file-native.
- The owner's words are quoted verbatim and dated, match the brief's supplied quote ("grant the MEMORY rows for DEL-00-01 and DEL-00-03"), and are correctly labelled as evidence. The M1 row (L27) matches.
- However, the grant lives only in the graph. The graph names no exact `MEMORY.md` paths; both files do exist under PKG-00 DEL-00-01 and DEL-00-03. The sentence "This grants one row in each existing `MEMORY.md`" is HELP_HUMAN's reading, stated as fact.
- This does not block TM1, because M1 is later. Before M1 writes, HELP_HUMAN should carry the grant into the governing D-PEC record or its register row with the exact paths, or record why graph evidence suffices, and label "one row each" as an interpretation.

## NOTES

**O1. The intake overstates whose interpretations were applied.** `TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md:171` says "The interpretations applied are the ones `D-PEC-107` records." The two status mappings (ELEVATED and DEFERRED) are WORKING_ITEMS's, not D-PEC-107's. L177 discloses this for CAND-03. The K3 bullet (L181–186) does not; the disclosure sits only in the TM-PEC-028 row Notes.

**O2. The notice's request and boundary wording pull slightly against each other.** `execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md:10` asks Root to "consider allocating" CI. L72 says the notice "asks for no write". This is consistent in substance, since it asks only for consideration and Root decides, and it follows earlier PEC notices' boundary phrasing. It could be tightened.

**O3. The PR #1021 reviews are not transcribed as files.** Review 01 (PASS WITH NOTES) and the backcheck (PASS) are only summarized in the return (L66–78). PR #1018 kept `REVIEW_PR1018_0{1,2,3}.md` in `returns/`. The brief does not require transcription; HELP_HUMAN may transcribe them in line with that practice.

**O4. Check 1, faithfulness to D-PEC-107, holds.**
- **CAND-01 (b):** recorded at INTAKE.md L175 with "None (not promoted)" and no row. The wording matches D-PEC-107 L38, and the freeze rule on RV1 corrections matches L81.
- **TM-PEC-026 (REGISTER.csv L11):**
  - It is `OPEN`.
  - It is marked plainly as a consideration under the freeze, not scheduled work.
  - It carries the consumer-contract design item, stated as HELP_HUMAN's choice.
  - It quotes "I don't want to proceed with the scope change right now" and "CAND-02 promote" correctly.
  - Its items (1)–(5) match the intake's CAND-02 list.
- **TM-PEC-027 (L12):**
  - It is `ELEVATED`, with ElevatedTo `Root` and NoticeRef set to the notice.
  - It invents no Root row ID.
- **TM-PEC-028 (L13):**
  - It is `DEFERRED`. Its trigger quotes D-PEC-107 L43 (TBD-003/004/006).
  - TBD-007 and CON-002 are included. I verified them against the DEL-08-06 SOW L133–137 and L181.
  - The PR #994 review 02 wording notes match POST-SCA005 graph L167.
  - It cites §B6, and I verified the B6 text at L321–340.
  - The provenance disclosure and the departure from "already homed" are present, and it is marked as a consideration under the freeze.
- **D-PEC-96 note:** present at INTAKE.md L200.
- **Owner's words:** no row claims more than the owner said. The owner-quoted strings match D-PEC-107 L9, L28, L71 and L84 verbatim.
- **Status choice for K3:** DEFERRED with a checkable trigger matches the method (`method.md` L19, L43) and PEC's TM-PEC-022 form.

## Evidence

**Hashes.** I recomputed all of these with `shasum -a 256`, and all match their citations:
- D-PEC-107: `403a0497…f346`
- Intake preimage at `acc7d3cc7`: `e2ccf3e3…818a`
- `pec-tests.yml`: `337611ce…5a7d`
- `hosted-ci-routing.json`: `1850e9a4…8b97`
- `software-workflow.json`: `d55fff77…bbd`
- X1 `HANDOFF_STATE.md`: `c832e9fc…c9d`
- `Propagation_Plan.md`: `f95d00d1…d7d8`
- DEL-08-06 SOW: `aecc5131…0826`
- POST-SCA005 graph: `372d5c52…473f`
- `pec.yaml`: `6858d567…314f`
- `taskmgmt.py`: `9c5cdc56…d101`
- Notice: `62f20ec8…4a58`
- Brief: `5b451dd5…ebf8`
- Federation record: `f84379de…a078`
- `REGISTER.csv`: `5141b554…7e92`, was `634641f0…376a`
- `INTAKE.md`: `0c455b97…5bf0`
- `REGISTER_CLOSED.csv`: `3c1349ba…1fd2`, byte-identical to main
- `package.json`: `a20d06cb…b39`
- `run-workspace-tests.ts`: `ba5306cb…d01`
- The return's 13 method and source hashes

**Notice facts (check 2).** Each factual claim is true at the cited lines:
- `pec` job L48–82; `npm test` L80–82.
- The checkout at L55–63 is sparse and blob-filtered with no `fetch-depth`, so it is a single commit.
- `npm test` runs `core`, `server` and `agent-sidecar` (`package.json` L21; `run-workspace-tests.ts` L17).
- The routing rule at L74–94 lists `projects/pec/v2/**` at L80 and routes only to `pec` at L92.
- `software-workflow.json` defines the five v2 checks, and no workflow under `.github/workflows` runs them.
- The X1 L29 quote is exact.
- The F-5/X-2 exclusions appear in D-PEC-87, 89, 91 and 106.
- No Root row or notice carries the concern; TM-ROOT-111 and TM-ROOT-110 cover other guards.

The notice is request-only, states the freeze (L61–67), and follows the header form of the 2026-09 PEC notices to Root: Status / Receiving loop / Sending loop.

**Validation (check 3).** I ran each check on both `head` and `origin/main`:
- `taskmgmt validate`: PASS, 12 rows on REGISTER.csv and 16 on REGISTER_CLOSED.csv at head (main has 9 and 16).
- Federation: COMPLETE on 4 registers with 28 findings, the same classes on both sides. No finding involves a PEC row. PEC counts go from OPEN 8 / DEFERRED 1 to OPEN 9 / DEFERRED 2 / ELEVATED 1, matching the federation record.
- Strict registers: exit 1 (0 errors, 26 warnings), identical between head and main.
- `harness.py self-check`: exit 0, identical once paths are normalized.
- `validate_pec_loop_receipts.py`: exit 0 (VALID, frozen through Receipt-166), identical.
- Reliance-hold `promote` on REGISTER.csv and INTAKE.md: ALLOW.

**Records commit `baf3c1308` (check 4).**
- It touches only `WORK_GRAPH.md`.
- DIR is COMPLETE: PR #1018 merged as `acc7d3cc7`, and review files 01–03 exist.
- TM1 is ACTIVE, and its facts match rows L11–13.
- The MEMORY quote is verbatim.
- The D-PEC-88 trace line is correct: the PR changes no STATUS or README.
- Apart from N2, the recovery lines are correct: the basis `acc7d3cc7`, and PR #1021 plus the RV1 branch as unmerged work.

**Containment, whitespace and CI (check 5).**
- The 7 files are the notice, the brief, the return, the graph, REGISTER.csv, INTAKE.md and DISPOSITION_FEDERATION. All fall within scope, and TM1's three commits do not touch the graph.
- `git diff --check`: clean.
- CI at `baf3c1308`: every run check passes (pec, harness, Harness pre-merge, Desktop E2E, Select App / PEC / source coverage), and the product jobs were skipped by path selection. The PR is OPEN, MERGEABLE and CLEAN.

## Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/DISPOSITION_FEDERATION_2026-09-27.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/TM1_INTAKE_DISPOSITIONS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv (TM-PIP-030 precedent)

(Paths name files as they are at PR head `baf3c1308`. This worktree is on `claude/pec-rr-closeout`, so some of these files do not exist here or differ; read them with `git show baf3c1308:<path>`.)

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **N1 (the return mis-cites TM-PIP-030; ELEVATED departs from it): repaired.**
  - The return's parenthetical now says TM-PIP-030 is `OPEN` with `ElevatedTo` Root, as its owner ruled, with a dated correction note.
  - TM-PEC-027's Notes cite the PRD candidate §6.2 elevation form and name the TM-PIP-030 contrast.
  - The `ELEVATED` status is kept as WORKING_ITEMS's disclosed reading. If the owner wants `OPEN`, a later row-maintenance act can change it.
- **N2 (RV1 row stale): repaired.** It now reads ACTIVE, naming the branch `claude/pec-rv1-d1-review`.
- **N3 (MEMORY grant only in the graph): repaired.**
  - The grant is carried into the governing record as `D-PEC-107` §MEMORY grant, with the owner's words verbatim and the two exact `MEMORY.md` paths.
  - "One row each" is labelled as HELP_HUMAN's interpretation there and in the graph.
  - The `D-PEC-107` register row mentions the grant.
- **O1: repaired.** The intake now says the two status mappings are WORKING_ITEMS's readings, and the K3 bullet discloses the `DEFERRED` reading.
- **O2: no change.** The notice asks Root only to consider the request.
- **O3: no change.** The in-run reviews were the manager's verifier child; this file is HELP_HUMAN's independent review. The return summarizes the in-run verdicts.

After the repair, `taskmgmt validate` passes on `REGISTER.csv`. The repair head needs a fresh review before merge.
