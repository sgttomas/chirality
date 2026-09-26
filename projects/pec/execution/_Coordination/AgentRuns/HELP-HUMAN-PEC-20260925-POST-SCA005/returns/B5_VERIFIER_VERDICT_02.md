# B5 verifier verdict 02 — backcheck of the SCA-006 checkpoint-2 repairs

**Reviewer.** The same `pec-reviewer` instance as verdict 01, resumed. It is a read-only TASK run through the Claude Code Agent tool with `model: opus`, which the host maps to claude-opus-5-5.

**Candidate.** `9815ba867da8e728ea91c8d6f33a47cacc02efdb`.

**Transcription.** The manager transcribed the verdict below from the reviewer's hand-back. The text is verbatim apart from Markdown headings and list layout. The manager's dispositions follow it.

---

**Verdict 02: PASS WITH MINOR.** This backchecks the SCA-006 checkpoint-2 repairs at `9815ba867da8e728ea91c8d6f33a47cacc02efdb`. Nothing is blocking. The three MINOR findings from verdict 01 are resolved. There is one new MINOR, and it is in the verdict-01 record, not in the package.

Candidate: the remote branch head is `9815ba867` (from `ls-remote`). The worktree is clean. I claim no owner act.

## Backcheck

1. **Scope of change — PASS.** `git diff --name-status 87a3f29b7 9815ba867` shows exactly six paths:
   - added: `returns/B5_VERIFIER_VERDICT_01.md`;
   - modified: `Amendment_Actions_CP2.csv`; `Amendment_Preview.md` (L65 only); `Decision_Log.md` (four hash rows); `Propagation_Plan.md` (hashes in the front matter and two tables, plus one new paragraph in §A4); and `Supersession_Delta.csv`.

   No byte changed in any candidate, the PRD, `AGENTS.md`, the decomposition, `Handoff_State.md` or the intake. `git diff --check` over the same range is clean.
2. **MINOR-1 — RESOLVED.**
   - All 54 rows keep the intake's values for ActionSeq, ActionType, EntityType and EntityID.
   - No Description still contains "DQ-b", "DQ-c", "recommended", "all options" or "graph node B3".
   - For Seq 24–27, the statement, SourceRef and Notes are exact substrings of the candidate ScopeLedger rows.
   - For Seq 38–40, the vocabulary rows are exact substrings of the candidate SOFTWARE_DECOMP.
   - Seq 32 reads "S -> M (accepted intake …)". Seq 54 cites `Propagation_Plan.md` §B3. The sentence at preview L65 is reworded.
   - `check_csv.py` exits 0, and the 16 DecisionIDs equal the 16 YES rows. `prove_preview.py` exits 0.
3. **MINOR-2 — RESOLVED.**
   - Every SupersededFactTextOrValue, except the four "(absent)" rows, is a whitespace-normalized substring of the live preimage.
   - Every ReplacementFactTextOrValue is a substring of its candidate.
   - No elisions remain.
   - A dry run of `accumulate_supersession_map.py` into scratch gave 45 rows and 0 findings.
4. **MINOR-3 — ACCEPTED as deliberate.** The new paragraph in `Propagation_Plan.md` §A4 records the reason. Adding a D-PEC number stays conditional on the owner's act. The candidate hashes are unchanged.
5. **Hash integrity — PASS.**
   - These values match every place they are quoted: the Decision_Log table, the plan front matter, the file table and the Q-CP2-A table.

     | File | SHA-256 |
     |---|---|
     | preview | `737af0e690688be00c479d1a5e54f2fa82b2c4e25e777abbe07670836473ecf4` |
     | plan | `abeeedb477505b5c277e97c19496bd6376b299a3128d4aa9a9693de69e429859` |
     | CP2 CSV | `dc69afb7796d84b92c4ed225560945a64aa86576c30e723b93aa149e4d5c0d2a` |
     | supersession delta | `e69f97814294ccd993fceff12cdf992623156c33ca4993adb103b61774e5977b` |

   - None of the pre-repair hashes remains in the snapshot folder or in `returns/`.
   - The unchanged files still match:
     - the PRD diff `a743a527`;
     - the AGENTS diff `7c57a1b2`;
     - all eight `CP2_CANDIDATE` files;
     - `Handoff_State.md` `0043e9b1`;
     - the intake, Impact Assessment, `Brief.md` and `Pre_Change_Coverage.json` at their accepted hashes.

## Findings

1. **MINOR.** `returns/B5_VERIFIER_VERDICT_01.md` L7 says the manager transcribed the verdict verbatim, and the verifier brief requires a verbatim save. The saved text is lightly reworded throughout:
   - L13 reads "There are 3 MINOR findings and 5 NOTEs", where I wrote "I found 3 MINOR issues and 5 NOTEs";
   - L17 reads "appear in PRD §8", where I wrote "are in PRD §8";
   - several lists are restructured.

   The substance is faithful: no finding, severity or locus is altered. Repair: paste the exact hand-back text, or change L7 to say the text is lightly edited with substance unchanged.
2. **NOTE.** In `Amendment_Actions_CP2.csv` L4 (Seq 3), the text "…§16.6 decision.." has a double period. This is cosmetic.
3. **NOTE.** In the dispositions table of the verdict-01 record, the disposition for NOTE 6 says the PRD diff attributes the PEC-API-007 tier-0 sentence to Seq 7 "with the SOW-099 notes as its source". `PRD_V2_4_SUCCESSOR_DIFF.md` H-11 (L251–255) attributes only intake Seq 7 and does not mention SOW-099. Reword the disposition, or leave it as "noted".
4. **NOTE.** Remote main has moved again, to `6721457be`. I did not fetch it, so I could not check whether it touches PEC preimages. The checkpoint-3 preconditions table already requires a recheck of the live preimages. The branch is still behind main, so CI may ask for a base update; report that rather than repair it.

## What I ran

Interpreter: Python 3.13.7.

- **Git (`git -C` on the worktree):** `rev-parse`, `log`, `diff --stat` and `--name-status` for `87a3f29b7..9815ba867`, targeted diffs, `diff --check`, `status --short` and `ls-remote`. All exited 0, except one diff against the unfetched `6721457be`, which exited 128 (unknown revision).
- **Hashing:** `shasum -a 256` over the snapshot and `CP2_CANDIDATE/**`, exit 0.
- **Stale hashes:** `grep` found no hits.
- **Comparisons:** read-only Python comparisons of the CP2 and supersession rows against the intake, the preimages and the candidates.
- **`check_csv.py`:** `python3 check_csv.py <package>` (cwd `B5/mgr`), exit 0.
- **`prove_preview.py`:** `python3 prove_preview.py` (cwd `B5/decomp`), exit 0. It rewrites the scratch file `proof_result.json`.
- **`accumulate_supersession_map.py`:** run with its output in `scratchpad/verifier_v/`; 0 findings.

I wrote no repository file and made no Git state change.

---

## Manager dispositions (B5 WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| 1 (MINOR) | **Repaired.** The L7 attribution in `B5_VERIFIER_VERDICT_01.md` now says the text is lightly edited for wording and list layout, with no finding, severity, locus or check result altered. |
| 2 (NOTE) | **Repaired.** `gen_cp2.py` strips the trailing period after the option-clause removal. The regenerated `Amendment_Actions_CP2.csv` hashes to `d901b432b9401dca0478a2ff73015273c387d29a1149ae66f5c6fbb2162fc1de` and has no ".. Origin" string. Only the Seq 3 row changed. `check_csv.py` exits 0. The plan, now `f95d00d154610d44a37d4aeabfae3fff29aac6c0a0c016bb1241810ebc87d7d8`, and `Decision_Log.md` were rehashed. |
| 3 (NOTE) | **Repaired.** The verdict-01 disposition for NOTE 6 is reworded to say H-11 cites Seq 7 only. |
| 4 (NOTE) | **Noted.** The branch was not merged again. A possible base update is reported to HELP_HUMAN and not repaired. |

With these repairs, no finding is open. Nothing was blocking in verdict 01 or verdict 02.
