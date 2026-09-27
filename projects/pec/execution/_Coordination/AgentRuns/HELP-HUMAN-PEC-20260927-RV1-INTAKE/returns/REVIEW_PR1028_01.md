# Review 01 of PR #1028, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `ec0d54798fde979564b8994534955d5af71006dd` (the full candidate `31a90f3e6..ec0d54798`). HELP_HUMAN's repairs and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `f02de42e41ff70420f4d7decd5b4677c3b104d55dbe6fb35ee1e4be2fef946ad`.

## Report (verbatim)

**Verdict: PASS WITH NOTES.** I reviewed PR #1028 at head `ec0d54798fde979564b8994534955d5af71006dd` (the full diff `31a90f3e6..ec0d54798`, 34 paths). Nothing blocks. Notes 1 and 2 should be fixed before merge; they are small.

I worked read-only. I made no repository writes and no git fetch. I did run read-only `gh pr view` and `gh pr checks`. The PR head equals `ec0d54798`, the PR is MERGEABLE, and every CI check is pass or skipped.

One process deviation. My first `mktemp -d` ignored TMPDIR and created a directory under `/var/folders`. I deleted it straight away. All checks below ran in a `mktemp -d` under the scratchpad, which I have since removed.

## Findings

1. **NON-BLOCKING (fix before merge): the PR description is not the receipt's account.**
   - `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/RECEIPT.md:45` says "Its description is this receipt's result, checks and limits". `projects/pec/AGENTS.md` requires the same of the final PR description.
   - The live PR body is still the manager's text. It has a "HELP_HUMAN (to follow on this branch)" section, has no receipt limits, and does not mention `D-PEC-108` or the receipt.
   - It also says "No … register byte changes", but HELP_HUMAN's commit adds a row to `_DECISIONS/_REGISTER.md`.
   - Fix: replace the PR body with the receipt's result, checks and limits.

2. **NON-BLOCKING: a notice path in the receipt does not resolve.**
   - `RECEIPT.md:18` cites `../../NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md`. From the receipt's folder that means `projects/pec/execution/_Coordination/NOTICE_…`, which does not exist.
   - The notice is at the Root path `execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md`. The graph (`WORK_GRAPH.md:24`) cites it correctly.

3. **NON-BLOCKING: the receipt's checks line claims evidence that does not exist.**
   - `RECEIPT.md:41` says strict, harness, receipts, `taskmgmt validate` and `git diff --check` "give output identical to the basis", with "Evidence in … evidence/".
   - The run folder holds no `taskmgmt` output, and the manager's MANIFEST does not list that check. `git diff --check` has no basis comparison.
   - I ran both myself (below), so the claims are true. But the evidence pointer overstates what the folder holds.

4. **NON-BLOCKING: the erratum is accurate, but its stated reason is weaker than it needs to be (check 9).**
   - **Accuracy:** `RECEIPT.md:40` is correct. `D-PEC-96_AMEND_DIRECTION_2026-09-26.md:5-6` calls itself a direction "on the D-PEC-96 proposal, which is not yet ruled". The corrected wording matches the reviewer's fix in `REVIEW_PR1021_03.md:21-24`.
   - **The pin is real:** `MANIFEST.md:12` pins the grant at `89d5ce4a…bc3`. My `shasum` reproduces that hash, and no other file pins it.
   - **Why the reason is weak:** that pin was created in this same PR, in commit `f80654104`, after the Q1 disposition. The stronger ground is that the grant is a merged owner-direction record, and the convention the grant itself cites is a new record rather than an edit of a merged one. Editing it would also turn the manifest's authority hash into a stale preimage.
   - **Changed disposition:** `REVIEW_PR1021_03.md:104` said "the wording becomes …" in the closeout PR. That was changed to an erratum held only in the receipt. Nothing in the grant file or its register row points to the correction.
   - **Attribution:** the receipt's "It found" credits C1 with an error that PR #1021 review 03 found. The citation is correct.
   - I judge leaving the grant's bytes unchanged as justified.

5. **NON-BLOCKING: two phrases in D-PEC-108 are HELP_HUMAN's additions but are not labelled as interpretation (checks 1 and 7).**
   - `D-PEC-108_D1_REACCEPTANCE_2026-09-27.md:60` adds "no architecture is imposed on another loop". This is not in the brief's account of option 1. It narrows the act, so there is no enlargement, but it is unlabelled.
   - `:66-72`, "Grant and records", derives the write grant (the `_REVIEW.md`, CSV, snapshot and `_LATEST` writes) from the method. The owner's words named no write targets. The sibling record `D-PEC-107_MEMORY_GRANT` labels the equivalent section "(HELP_HUMAN interpretation)".
   - The grant is not wider than the owner's act. Recording an exact-byte acceptance is the method's ordinary Gate 4 consequence, and it excludes Gate 5, ISSUED, lifecycle, P1, production, C-05, SOW, artifact, `_STATUS.md` and `v2/**`.
   - Two further notes:
     - The grant names no rollback or verification clause, which `projects/pec/AGENTS.md` lists for packets.
     - It is written after the manager's writes were made. They publish together at merge.
   - `:13` also leaves out the presentation's "MAJOR is the conservative reading" (per `REVIEW_PR1023_01.md:107`). That is minor.

6. **NON-BLOCKING: `_LATEST.md` and the other records disagree on the order of hashing and preflight.**
   - `projects/pec/execution/_Evaluation/Reviews/_LATEST.md:10` says both hashes were "reproduced exactly after their PEC `promote` preflights returned `ALLOW`". That phrase is copied from the 2026-08-09 pointer.
   - The Decision_Logs (line 5 in each snapshot) and `MANIFEST.md:58` give the order as hashes first, then writes, then preflights.
   - No evidence shows a second hashing after the preflights. The register is header-only, so the outcome is unaffected.

7. **NON-BLOCKING, informational: absolute paths are committed.**
   - They appear in the copied brief (line 64) and in `evidence/receipts_*.out`.
   - The harness absolute-path check still passes, and PR #1023 note 7 accepted the same pattern.

## The 11 checks

1. **Faithful transcription (K-AUTH-1): passes, with notes 4 and 5.**
   - The owner's words are quoted verbatim in both `_REVIEW.md` files, all snapshots, `D-PEC-108:7`, the register row, the receipt and the graph.
   - The option-1 content is labelled as HELP_HUMAN's presentation and matches the brief line for line: AC-007, the contract's first acceptance, AC-011 (birth and currency bases, OBJ-001 LOW confidence, alternatives unadopted), findings accepted as known limitations, CU-001 retired, exact-bytes scope, no C-05 act.
   - RF-001 stays MAJOR and no severity call is claimed.
2. **Hashes: all four reproduce at the head.** ADRs `ad6bab7e…c49e`, DEL-00-01 SOW `3757632b…a647`, DEL-00-03 SOW `0fed4ecb…e843`, SPEC `f84c067b…f617`.
3. **Prior bytes: preserved.**
   - Per column, only `HumanDisposition` changed (TBD to ACCEPT_AS_IS) and `Status` changed (OPEN to RESOLVED), on DEL-00-01 RF-001..005 and DEL-00-03 RF-004..010. DEL-00-03 RF-001..003 are byte-identical.
   - Setting RESOLVED is supported by the pinned method at `2f825f180` (`resources/method.md`, Gate 4 step 2): "Update `Status` to `RESOLVED` if disposition is final". I reproduced all four method-file hashes.
   - In the `_REVIEW.md` files, the only deletions are the stage lines (1 in DEL-00-01; 2 lines replaced by 3 in DEL-00-03). The old stage text is quoted in the new sections.
4. **Snapshots: follow the precedent.** Each has the same five files and form as `REV_DEL-00-03_2026-08-09_2156`, and `_LATEST` moved to `_1658`. See note 6.
5. **MEMORY rows: correct.** One row was appended to each file, in the existing 3-column format. Both links resolve at the head, and prior bytes are unchanged.
6. **Out-of-bounds writes: none.** No `_STATUS.md`, `ScopeOfWork.md`, artifact or `v2/**` path is in the diff, and there is no lifecycle change.
7. **D-PEC-108 grant: not wider than the owner's act.** See note 5.
8. **Receipt, graph and STATUS claims: true, except notes 1–3.**
   - The PR merges are correct: #1018 `acc7d3cc7`, #1021 `56f7d4602`, #1023 `31a90f3e6`.
   - Review files exist and match: REVIEW_PR1018_01–03, PR1021_01–03, PR1023_01–02. RV1 verifier verdicts 01 and 02 are PASS WITH NOTES.
   - TM-PEC-026 is OPEN, 027 ELEVATED to Root, 028 DEFERRED. Finding counts and the preflight count (22 runs, 22 ALLOW) are correct.
   - STATUS reads present-current.
9. **Erratum: accurate.** Leaving the grant's bytes unchanged is justified. See note 4.
10. **Validators: all match expectations** (outputs below).
11. **No CHECKING prompt** appears in the added lines or the PR body.

## Check outputs

All ran on a `git archive ec0d54798` export. I gave the export a temporary git repo (object alternates, HEAD at `ec0d54798`, index read from the tree) so the git-dependent tools could run.

| Check | Result |
|---|---|
| Strict registers (`validate_decomposition_registers.py --strict`) | exit 1; 0 errors, 26 warnings (XRG-013); byte-identical to `evidence/strict_candidate.out` |
| `harness.py self-check` | exit 0; identical to `evidence/harness_candidate.out` apart from its appended exit line |
| `validate_pec_loop_receipts.py --repo-root .` | exit 0; "VALID … frozen through Receipt-166; versioned receipt contract satisfied" |
| `taskmgmt.py validate` | exit 0; PASS, 12 rows; identical at base `31a90f3e6`, and the register file is byte-identical |
| `git diff --check 31a90f3e6..ec0d54798` | exit 0, clean |
| `shasum -a 256 -c SHA256SUMS` (run folder) | all 9 entries OK, exit 0 |

Without the temporary repo, the harness exited 2 and the receipts validator exited 1 (COMMIT_NOT_FOUND). Both are environment artifacts of an export with no git.

## Files cited

All under `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-rv1-intake-closeout/projects/pec/execution/`:
- `_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/RECEIPT.md`
- `_Coordination/_DECISIONS/D-PEC-108_D1_REACCEPTANCE_2026-09-27.md`
- `_Coordination/_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md`
- `_Coordination/RV1_ACCEPTANCE_RECORD_2026-09-27/MANIFEST.md`
- `_Evaluation/Reviews/_LATEST.md`
- `_Evaluation/Reviews/REV_DEL-00-01_2026-09-27_1655/` and `_Evaluation/Reviews/REV_DEL-00-03_2026-09-27_1658/`
- `_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md`

The Root notice is at `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-rv1-intake-closeout/execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md`.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **1 (PR description): repaired.** The PR body is replaced with the receipt's result, checks and limits. It names `D-PEC-108`, the receipt and the register row.
- **2 (notice path): repaired.** The receipt now links the Root notice by a path that resolves.
- **3 (checks evidence): repaired.** The receipt now names which checks have saved evidence in the run folder: strict registers, harness, receipts and preflight. It says `taskmgmt validate` and `git diff --check` were run by HELP_HUMAN and by this review, with no evidence file saved.
- **4 (erratum reason): repaired.** The receipt now gives the stronger ground: the supplement is a merged owner-direction record, and the convention it cites keeps a merged record unedited. It also notes that the manifest pin was written in this PR, credits the finding to PR #1021 review 03, and says the intended in-place edit became an erratum.
- **5 (unlabelled interpretation in `D-PEC-108`): repaired.**
  - The "no other loop" clause is labelled as HELP_HUMAN interpretation. It is sourced to the RV1 return's owner-decision draft and marked as narrowing.
  - "Grant and records" is labelled as HELP_HUMAN interpretation and states that the owner named no write targets.
  - Verification and rollback clauses are added.
  - The presentation's "MAJOR is the conservative reading" is restored.
- **6 (`_LATEST.md` ordering): repaired.** The first repair said the preflights ran "after the record writes". Review 02 (N2) showed that the order was mixed. The pointer now reads "reproduced exactly before any write; … preflights returned `ALLOW` (order disclosed in the run manifest)". No file pins the pointer's hash.
- **7 (absolute paths): recorded, no change**, as for PR #1023 note 7.

The repairs and this file follow the reviewed head. They need a backcheck before merge.
