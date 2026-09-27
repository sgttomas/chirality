# X1 preparation verdict 08

Reviewer: fresh read-only `pec-reviewer` TASK (agent `addfc736bb8883a0a`, Opus 5.5 as reported by the host), backchecking the verdict-07 repairs (`c49817153..4db36e6de`) and HELP_HUMAN's eight requested repairs. Transcribed verbatim by WORKING_ITEMS; dispositions appended after the report.

Reviewed head: `4db36e6de`.

---

VERDICT: PASS WITH NOTES

Nothing blocks. The blocking finding from verdict 07 is fixed: the path rule now checks a path's shape, not whether the file exists. Findings 2–5 are also fixed. No candidate or act byte has changed since `4f2e4f44a`, and HELP_HUMAN's eight repairs still hold at HEAD. The edits leave three small non-blocking inconsistencies and some informational notes, listed below.

Reviewed HEAD: `4db36e6de0c2bb1aa15f6f400e765e1fb7524fe7` on branch `claude/pec-x1-fixtures-proposal` (the local `origin/claude/pec-x1-fixtures-proposal` ref points at the same commit). Delta reviewed: `c49817153..HEAD`, which is two commits, `13a430474` and `4db36e6de`. Local `origin/main` is `f0a6159c9`. I did not fetch.

## Findings

**1. NON-BLOCKING: Rollback says a failed preflight never uses up the grant, but the grant says less than that.**
- **Where:** draft Rollback "During execution" (line 377), against the Exact product grant (line 204).
- **Condition:**
  - Line 377 says: "An exit 1 at preflight (drift, a missing candidate, a changed pin) writes nothing and consumes nothing either".
  - Line 204 only protects an exit-1 run "with every target at its preimage, `v2/tests/parsers` absent and no temporary file left". It is silent on other exit-1 runs.
  - Two preflight refusals listed under Failure semantics (line 322 area) fall outside line 204's condition:
    - `software-workflow.json` not at its preimage (the "drift" that Rollback names);
    - a created target, or the new directory, already existing.
  - So Rollback grants something the operative grant text does not state. The drift case is the exact gap verdict 07 finding 4 raised. It was answered in Rollback only.
- **Impact:** low in practice, because drift is routed to the owner and no re-pin is pre-authorized. Still, the owner-facing grant and Rollback now read differently on whether the grant is used up.
- **Evidence:** line 204 text; line 377 text; the preflight list in Failure semantics.
- **Remediation direction:** state the preflight exit-1 rule in the grant itself, or narrow Rollback's parenthetical to the cases line 204 covers (a missing candidate or a changed pin). Also state whether a transient drift that is corrected locally may be rerun.

**2. NON-BLOCKING: both documents cite a verdict 08 file that does not exist yet.**
- **Where:**
  - draft verdicts table, line 430: `VERIFIER_VERDICT_08.md` | backcheck of verdict 07 | see file | see file | see file;
  - return verdicts table, line 176: "see `VERIFIER_VERDICT_08.md`".
- **Condition:** no `VERIFIER_VERDICT_08.md` exists at HEAD. The prep folder holds verdicts 01–07 only.
- **Impact:** a dangling pointer in the owner packet. Filling it in will change the draft's SHA-256 and `SHA256SUMS`.
- **Remediation direction:** when verdict 08 is transcribed:
  - replace the placeholder cells with head, result and dispositions;
  - regenerate `SHA256SUMS`;
  - give the new draft and `SHA256SUMS` hashes in the handback. The return now defers both hashes to the handback.

**3. NON-BLOCKING (low): a rerun under A + L on a later day leaves `{D}` and the run-root date unclear.**
- **Where:** Finite verification row 1a (line 344), together with the add-on L commands and postimages (the section after line 250) and Rollback line 377.
- **Condition:** on a rerun, row 1a says row 1's `_STATUS.md` precondition becomes "the three files hold their tabled add-on L postimages". Those postimages embed `{D}` ("the act date"), and the L history line points at `execution/_Coordination/X1_FIXTURES_{D}/`. Nothing says whether a rerun on a later date keeps the first attempt's `{D}` and run root.
- **Impact:** a later-day rerun could open a new `X1_FIXTURES_{D'}` root. The committed history line would then point at the first root, or the precondition could be read against `{D'}`.
- **Remediation direction:** one clause stating that a rerun reuses the original run root, and that the postimages are those produced with the original `{D}`.

**4. INFORMATIONAL.**
- **DEL-02-03 is not cited.** The parser-output path rule (line 68) cites only DEL-02-09 REQ-003/REQ-007 and DEL-02-08 REQ-007/REQ-009. The rule applies to all three parser packets, and two DEL-02-03 rules fit it: REQ-007 admits "repository-relative paths", and REQ-004 forbids silently omitted fields. Citing them is optional.
- **Weaker guard.** A shape check cannot tell a real path from prose placed in a path-typed field. The old "resolves" rule gave some of that protection. A parser packet may want to require that a path field carry the target of a link construct its declared grammar recognizes. This is not a defect in X1.
- **Hashes outside the claims tool.** The new prefix-only blob abbreviation `7c683795…` (line 68), like the older `15dcfee1…` (line 65), is outside `verify_x1p_claims.py`. That tool matches only the `pppppppp…sss` SHA-256 form. I checked both by hand (see "What I checked").

## Check 1: verdict 07 finding 1 (BLOCKING in verdict 07) is repaired
- Body line 68 and Q3 (line 409) now:
  - exempt path fields from the word count by type;
  - check shape only: "one normalized repository-relative path, with no link text and no URL";
  - say that whether the file exists is not checked;
  - leave normalization to each parser's declared choice, which matches Limits line 397.
- This agrees with the contracts at HEAD:
  - DEL-02-09 REQ-003 (line 142): link targets as normalized repository-relative paths or PR numbers, never with link text.
  - DEL-02-09 REQ-007 (line 146): a silently omitted entry or field is prohibited.
  - DEL-02-08 REQ-007 (line 157): linked paths as normalized repository-relative paths only, never with link text.
  - DEL-02-08 REQ-009 (line 159): a silently omitted field is prohibited.
- The cited examples are true:
  - `git rev-parse d61981ee2:<DEL-12-01 MEMORY.md>` gives `7c683795ca7b8fb842d6b4e206703e3e3df50060`. Its lines 33–34 cite `…/Specification.md` and `…/Guidance.md` under `PKG-12_Security, Privacy, and Private Data Handling`. `git ls-tree` of that folder has neither file.
  - DEL-08-01 is `15dcfee1a37df36eb2e73935a5a1c31971bbb46e`. Its line 103 cites `DEV-001_DISPATCH_DEL-08-01.md`, and no `DEV-001_DISPATCH*` file exists under Piping `_Coordination` at `d61981ee2`. Its lines 53, 105 and 175 contain a spaced path.
  - The synthetic link fixtures use invented targets, for example `links_in_each_form_bullet.md` line 9 links `../../../_Coordination/WorkGraphs/SYN-RUN-MEM-0821/SYN_GRAPH.md`.
- No text relying on existence remains: `grep -i resolv` finds only pin-resolution uses.

## Check 2: verdict 07 findings 2–5 are repaired
- **Return (finding 2).**
  - No stale values remain. `c43dbb9f`, `45854c55`, `7d4d3d3c`, `6e5622c24`, "87 tracked" and "110 files" are absent from the draft and the return.
  - The draft and `SHA256SUMS` hashes are now deferred to the handback, with "covers every tracked prep file".
  - Line 90 scopes the thresholds correctly: the no-source-text threshold is TBD-assigned for DEL-02-03/09 and proposed for DEL-02-08; the copy threshold is assigned by no TBD.
  - Line 150 cites both `run_main` and `run_origin_main`. "Identical results" holds: the two `SUMMARY.out` files differ only in the basis-commit line.
  - The PR line 6 description of `4f2e4f44a` is accurate (parents `6ab42ec4b` and `f0a6159c9`).
- **Limits (finding 3).** Line 397 now names two settlements. The first is the golden format, the pinned blobs and the no-source-text threshold (TBD-assigned for DEL-02-03/09, proposed for DEL-02-08). The second is the copy threshold, assigned by no TBD, as the operational test of DEL-02-08 REQ-017, DEL-02-09 REQ-014 and DEL-02-03 REQ-017. This matches body lines 62 and 69 and Q3.
- **Rerun semantics (finding 4).** The grant (204), "Second run" (322), Rollback (377) and row 1a (344) now agree on the rolled-back exit-1 case, and row 1a states how the A + L rerun precondition works. Residuals are findings 1 and 3.
- **Evidence list (finding 5).** Line 440 names `run_origin_main/` at `f0a6159c9`.

## Check 3: bytes, hashes and hygiene
- **Candidates and act unchanged.** `git diff --stat 4f2e4f44a HEAD` over `candidates/`, `apply_x1p.py`, `build_apply_x1p.py` and `apply_x1p.template.py` is empty. `apply_x1p.py` SHA-256 is `452ff66af71b7d3de9814301a8e45ca070137d5e577b4e73c202b713d2102428`.
- **`SHA256SUMS`.** `shasum -a 256 -c SHA256SUMS` is all OK. It has 111 entries, which equal `git ls-files` of the prep folder minus `SHA256SUMS` exactly. Its own SHA-256 is `04c494f49526a9ae4c6da9a6945167f1bdb905861fabf243f381bcc739adcd19`.
- **Diff hygiene.**
  - `git diff --check origin/main...HEAD` and `git diff --check c49817153 HEAD` are both clean.
  - `origin/main...HEAD` touches only the prep folder and `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005`.
  - The evidence changes in the delta are scratch paths and timings only.
- **`evidence/run_origin_main/SUMMARY.out`.** It ends with OVERALL PASS, has basis `f0a6159c9`, and has no trailing whitespace. No file in `run_origin_main/` has trailing whitespace.
- **`__pycache__`.** It is no longer present.

## Check 4: HELP_HUMAN's eight repairs still hold
- None of the aids changed in the delta. Their live hashes equal the draft's table: `test_apply_x1p.py` `5585a6f1…`, `run_x1p_checks.sh` `88193621…`, `run_fixture_suite.sh` `5ffca7d4…`, `verify_x1p_bindings.py` `039e4f56…`, `report_x1p_pins.py` `1177a020…`, `verify_x1p_claims.py` `2fdb5ed0…`, negative controls `5a9ccf10…5c1a` and `06f8fec3…5ee`, build `b30e0caf…8e91`, template `99cd6c9b…a80e`.
- Specific markers:
  - The runner uses `paste -sd ' ' -` (line 68).
  - No "remaining" word check remains in the runner, the fixture-suite script or the negative controls.
  - The TMPDIR fallback to `.scratch/` is present in all four aids, and no `/tmp` literal remains.
  - `COMMON_PREP_RULES_2026-09-26.md` is `51b70e46…b311` and the X1P brief is `1cefcc48…bbac`, both as cited.
- Repair 1 now appears in its amended, shape-based form. Repairs 2, 4 and 6 still read as verdict 07 recorded, as refined in Check 2.

## Other checks
- Read Root `AGENTS.md`, `agents/AGENT_TASK.md`, verdict 07 with its dispositions, and the full `git diff c49817153 HEAD`.
- Read the draft's affected sections: thresholds, grant, failure semantics, finite verification, independent verifier, administrative grant, Rollback, Limits, owner questions, verdicts table and evidence list.
- Read the full return, and the three contracts' relevant REQ and TBD lines.
- `projects/pec/AGENTS.md` (460 lines): I checked its length but did not read its body. Please account for that in your reliance.
- **Verifier checklist and owner questions.** No conflict with the new path rule, which is scoped to the parser packets. Q3 and the return's owner questions match the body. Row 07 of the verdicts table matches verdict 07 (1 blocking, 4 non-blocking).

## Commands I ran
- `python3 <prep>/verify_x1p_claims.py <worktree> <prep>` against the HEAD draft: RESULT PASS 67/67.
- `zsh <prep>/run_fixture_suite.sh <worktree> f0a6159c9 <my copy of candidates/.../parsers>`: 10 tests, OK.
- Both ran with TMPDIR set to my directory and `PYTHONDONTWRITEBYTECODE=1`. `git status --ignored` of the prep folder was clean afterwards.
- I did not rerun the full check runner.

## Boundaries
I wrote nothing in any worktree, did no checkout, used no network, and made no repairs.

My directory: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1r5.ro2sqP` (contains `tracked.txt`, `sums.txt` and `parsers_copy/`).

## Key paths
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/VERIFIER_VERDICT_07.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/SHA256SUMS`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/X1P_FIXTURES_PROPOSAL.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md`

---

## Dispositions (WORKING_ITEMS)

1. **Repaired.** The grant itself now states the preflight exit-1 rule. Such a run writes nothing and does not consume the grant. A missing candidate or a transient local problem may be fixed without changing any bound byte and rerun. Preimage or pin drift, or an existing target, goes to the owner. Rollback now defers to the grant.
2. **Repaired.** The verdicts tables in the draft and the return now carry this verdict's real row. The draft and `SHA256SUMS` hashes are regenerated and given in the handback.
3. **Repaired.** A rerun reuses the original run root `X1_FIXTURES_{D}` and the original `{D}`. Row 1a's rerun precondition names the add-on L postimages produced at the first attempt.
4. **Informational, taken up.** The path rule now also cites DEL-02-03 REQ-007 and REQ-004, and it notes that a shape check cannot tell a path from prose in a path-typed field, which a parser packet may tighten. Prefix-only blob abbreviations stay outside `verify_x1p_claims.py`; the reviewer checked both by hand.

These edits change draft text only. No candidate, act or aid byte changed. They were not reviewed by a further fresh reviewer.
