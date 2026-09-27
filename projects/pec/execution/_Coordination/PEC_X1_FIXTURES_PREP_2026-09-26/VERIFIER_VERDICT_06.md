# X1 preparation verdict 06

Reviewer: fresh read-only `pec-reviewer` TASK (agent `a5ec1c41968939d08`, Opus 5.5 as reported by the host), round 3 packet review, backchecking verdict 04. Transcribed verbatim by WORKING_ITEMS from the reviewer's hand-back; dispositions are appended by WORKING_ITEMS after the report.

Reviewed head: `082a2a96f` (branch `claude/pec-x1-fixtures-proposal`, PR #996).

---

VERDICT: PASS WITH NOTES

Nothing blocks. Verdict 04's blocking finding is repaired. Add-on L now has one timing everywhere it appears: at actual production start, after row 1, immediately before the act. That timing is faithful to the `D-PEC-85` ruling. The act script regenerates byte for byte, the grant table equals TARGETS, and the check runner passes. The six notes below are wording, pre-publication and edge-case items.

Reviewed HEAD: `082a2a96f5f4a46f90263daa7d22a6b399e84842` (branch `claude/pec-x1-fixtures-proposal`, PR #996). The worktree was clean before and after, and I wrote nothing in it.
Observation commit: `6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`.
Draft: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md`, SHA-256 `ede8b2d5ae1ba372ec47b9c5ef86b9cfc7fc15addfc2aabb221e70214f3fc537`. Line numbers below are draft lines.

## Findings (most severe first)

**1. NON-BLOCKING (fix before publication) — the publication artifacts are still missing, and the verdict record overstates the repairs.**
- **Location:** L421 ("Artifacts, all in this prep folder with hashes in `SHA256SUMS`"); L416 (verdict 04 row: "All repaired"); L417 (row "`VERIFIER_VERDICT_05.md` onward | round 3 | see file | see file | see file"); verdict 04 disposition 4 ("Repaired before publication").
- **Condition:**
  - At HEAD the prep folder has no `SHA256SUMS`.
  - There is no X1P return under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`.
  - Disposition 4 calls this "Repaired", but nothing has been written. This is the third round in which the item is deferred (verdict 03 finding 7, verdict 04 finding 4).
  - Verdict 04 dispositions 7 and 9 were "Recorded", not repaired, so "All repaired" is inaccurate.
  - L417 points at files that do not exist.
- **Impact:** The published packet would claim artifacts it lacks. COMMON's Produce clause requires both files.
- **Remediation direction:**
  - After the final verdict, write `SHA256SUMS` (tracked files only) and the return.
  - Replace L417 with the actual round-3 rows.
  - Change the verdict 04 disposition cell to match the dispositions (4 deferred; 7 and 9 recorded).

**2. NON-BLOCKING — the "Currency after the observation commit" bullet is stale.**
- **Location:** L19.
- **Condition:**
  - Local `origin/main` (no fetch) is `f0a6159c9440557d18a728416166cc1e3e0c862d`. PR #998, the `D-PEC-102` act, merged at 2026-09-27 00:13:54 -0600. That is before the HEAD commit (00:16:12).
  - `git diff --name-only 6c6cc1b00 origin/main -- projects/pec` now lists 285 paths. Besides those the bullet names, they include:
    - eight other `ScopeOfWork.md` files: DEL-03-04, DEL-04-01/02/03, DEL-08-01/03/04 and DEL-10-03;
    - the `SOW_CURRENCY_S4_2026-09-26/` run root;
    - the S4A brief and return, and `REVIEW_PR998_0*`.
  - The bullet says "When round-2 review ran, `origin/main` had moved … to `c26677c8a`". Verdict 04 (round 2) actually observed `78e74f590`; `c26677c8a` merged later, at 23:44.
- **Substance still holds at `f0a6159c9`:**
  - None of these changed: the 35 targets, the 12 act-pinned files, the three `_STATUS.md` or `ScopeOfWork.md` files, `write_status.sh`, the holds register and script, any `Dependencies.csv`, `docs/SPEC.md`, the workflows or the skill.
  - The register tops out at D-PEC-103, so there is no D-PEC-104 to 106 row.
  - `report_x1p_pins.py . origin/main` gives `RESULT PASS 19/19`. The FX-PEC-0 graph drift is informational only.
  - The reliance preflight gives `ALLOW` at `origin/main`.
- **Remediation direction:** Re-anchor the bullet to the current `origin/main` at publication, name PR #998, and correct the round-2 revision.

**3. NON-BLOCKING — the rollback text leaves the A + L failed-act case partly unspecified.**
- **Location:** L367 ("They are committed before the act runs…"); L368 ("Before merge. Close the PR and discard the branch."); L273.
- **Condition:**
  - The obligation to commit the L changes before the act appears only in Rollback. The add-on L section (L257–274) and row 1a (L335) do not state it.
  - L368 has no A + L carve-out. After a failed act, discarding the branch would silently drop the committed `_STATUS.md` changes and the failure record, which L273 and L367 say "stay".
  - No path is given for landing those commits on `main` when the act PR itself cannot merge.
- **Impact:** A narrow edge case, but an executor could follow L368 and lose a truthful lifecycle record.
- **Remediation direction:**
  - Put the commit step in the add-on L section and row 1a.
  - In L368, exclude the A + L failed-act case: keep the L commits and failure evidence, and route to the owner or merge them as the record.

**4. NON-BLOCKING — add-on M does not name its three `MEMORY.md` paths.**
- **Location:** L276–289; question 5 (L404).
- **Condition:** `projects/pec/AGENTS.md` §"Deliverable records and loop ownership" says "Name the affected `MEMORY.md` paths in that packet." The draft names the deliverables but not the paths. The `D-PEC-100` add-on M tabled full paths. The paths can be worked out from the add-on L commands and `evidence/reliance_hold_preflight.out`.
- **Remediation direction:** Table the three repository-relative paths in add-on M.

**5. NON-BLOCKING — the add-on L and M byte checks are not in the verifier's list.**
- **Location:** L271 ("The verifier checks that no other byte departs from the preimage"); L289 (the same for M); the Independent verifier list (L351–355).
- **Condition:** The verifier's item 5 points only to rows 7–8. Those rows check which files changed, not their bytes. The L postimages are date-dependent and are not hashed in the grant.
- **Remediation direction:** Add a verifier item: under L, the `_STATUS.md` diffs are exactly the add-on L changes; under M, the `MEMORY.md` diffs are exactly the tabled row.

**6. NON-BLOCKING — the candidate changes after verdicts 03 and 04 have no saved candidate-level verdict yet.**
- **Condition:** `git diff caf8af936 HEAD` shows these changes:
  - `FC-2.json`: three `no-runs-section` expectations rebound from DEL-02-09 REQ-001/AC-001/VER-001 to REQ-002/-014, AC-002/-014 and VER-002/-014, and the fact renamed;
  - the SYN-RCP-05 `construction` text in the synthetic manifest;
  - `test_parser_fixture_integrity.py`: +92 lines (the form-anchor sibling check and the widened AST list);
  - the act script, moving from `ee731005…` to `452ff66a…`.

  Verdict 04 disposition 7 relies on a round-3 candidate verdict, which is not in the folder at HEAD.
- **My light check:** I found no defect in these bytes. The rebinding matches verdict 03 finding 5, and bindings are 442/442. One small gap: the AST list does not flag `Path.replace`, a rename method, although L56 lists rename methods. L56 already hedges ("a guard, not a proof").
- **Remediation direction:** Publish only after the round-3 `MODE=VERIFY` candidate verdict is saved. Optionally note the `Path.replace` gap.

## Verdict 04 dispositions: what I found in the bytes

| Disposition | Result |
|---|---|
| 1 (blocking) | Done. L359 reads "at actual production start: after row 1, immediately before the act". This matches L257, row 1a (L335), question 4 (L403) and Limits (L385). `grep 'verifier pass'` finds nothing. |
| 2 | Done. Row 1 (L334) includes the fresh dependency read with a named result. I confirmed the three DEL-01-01 rows and the seven reverse rows are ACTIVE, INITIALIZED, PENDING at `6c6cc1b00`. |
| 3 | Done. L367 says "as it was before the act" and states that the L commits are kept. See finding 3 for the remaining gap. |
| 4 | Not done at HEAD (finding 1). |
| 5 | Done. The source-less anchor check is in the test, and L45 describes all three checks. |
| 6 | Done. L56 matches `PATH_WRITE_METHODS`, `OS_WRITE_FUNCTIONS`, the `exec`/`spawn`/`posix_spawn` prefixes and the alias checks. |
| 7 | Recorded; see finding 6. |
| 8.1–8.4 | Done: "slot rule" is gone; "at most three ways"; the DEL-02-03 bindings row now includes REQ-001/-005; the `D-PEC-85` ruling `67167dc5…4851` is in the Precedents and basis table. |
| 9 | Recorded; see finding 2. |

**Add-on L against `D-PEC-85`.** The quoted clause matches the ruling (`D-PEC-85_RULING_2026-09-08.md`, `67167dc5ec68…4851`). The draft also meets the ruling's other conditions:
- the history line carries the semantic-step skip, the ruling, the evidence path and the date;
- a pre-state mismatch stops and routes;
- no CHECKING, ISSUED or acceptance is implied.

SPEC §3.2 (L314) and §3.3 (L327) match the draft's citations. The §3.4 "Lifecycle corrections are human-authorized administrative acts" supports the rollback. `write_status.sh` (`0bf835f5…ece3`) is unchanged, and the prototype output is as stated.

## What I checked

**Check runner.**
- Command: `zsh <prep>/run_x1p_checks.sh <worktree> 6c6cc1b00 <prep> <mydir>/out`, with `TMPDIR` set to my directory.
- Result: exit 0, OVERALL PASS:
  - act: check-only 0, apply 0, rerun refuses 1;
  - containment: `software-workflow.json` modified plus 34 created files;
  - six affected checks, and all six registered checks exit 0;
  - `v2-parsers`: 10 tests ok;
  - bindings 442/442; pins 19/19; claims and quotes 67/67;
  - strict registers (exit 1, 0 errors, 26 `XRG-013` warnings), harness and receipts identical before and after;
  - hygiene PASS; fault injection 11/11; negative controls 20/20.
- `SUMMARY.out` and 17 other outputs are byte-identical to `evidence/run_main`. The other 5 differ only in temp paths and timings.

**Act script and grant.**
- `build_apply_x1p.py <worktree> 6c6cc1b00 <copy>` reported targets=35, creates=34, pinned=12. The regenerated `apply_x1p.py` is `cmp`-identical to the prep copy: `452ff66af71b7d3de9814301a8e45ca070137d5e577b4e73c202b713d2102428`, which is the draft's bound hash.
- The parsed grant table equals TARGETS exactly (35 rows).
- All 35 postimages recompute, and the candidate file set equals the table.
- The 12 PINNED entries equal the draft's read-only list.
- The `software-workflow.json` diff adds only the `v2-parsers` check and its path rule.

**More than 40 claims spot-checked with `shasum -a 256` and git.**
- Every full hash in Provenance and Method, and the basis-table abbreviations, recompute. This covers:
  - Root and PEC `AGENTS.md`, `AGENT_WORKING_ITEMS.md`, SPEC, the catalog, the three workflows and the skill, the profile;
  - the holds register and script, the `software-workflow.json` preimage;
  - the decomposition files and `_LATEST.md`, the graph and `_REGISTER.md`;
  - the `D-PEC-85/87/89/91/94/96/98/99/100` records and the exhibit;
  - Propagation_Plan, Impact_Assessment and the design note;
  - the brief `1cefcc48…` and COMMON `51b70e46…`;
  - all aid hashes.
- **Lineage:** `189f205ff` is an ancestor of the observation commit, and the five decomposition/PRD files are identical at both commits. `d61981ee2` is the PR #881 merge.
- **Merges:** `0b276a7f`, `c56ae4a2` and `10b672ca` are two-parent merges of #876, #873 and #868, all ancestors of `d61981ee2`. PRs #950, #957, #976, #979 and #958 are merged. The observation commit is the PR #992 merge.
- **Pins:** all 19 `(commit, path, blob)` entries resolve, and the tree records are as stated.
- **Goldens:** 65 expectations (30 fixed, 35 observed); 70 source values; 16 anchors.
- **Synthetic set:** 24 cases (21 file-backed; SYN-MEM-05, SYN-RCP-05 and SYN-RCP-06 constructed at test time); 27 `.md` files; U+2014 is the only non-ASCII character; PR numbers start at #9001; no candidate contains "remaining".
- **Quotations:** the §B7, R-05 (Impact_Assessment L451), Q5 (a) (Decision_Log L24), graph X1 row, SPEC, DEL-02-03 CON-007, DEL-02-08 TBD-006 and DEL-02-03/09 "own packet" texts are all verbatim. The owner's "no need to scan" direction is at `D-PEC-96_AMEND_DIRECTION` L14.
- **Other records:**
  - Part B has 12 items, routed only to S1, S2 and S4.
  - No `Dependencies.csv` cites `software-workflow.json` or `v2/tests`.
  - Hosted CI claim: `pec-tests.yml` runs only `npm test` on a sparse, blob-filtered, default-depth checkout.
  - The reliance preflight evidence shows 41 ALLOW. I reran `exact-correction-preparation`, `dispatch-for-production` and `rely-for-production` on sample targets at `origin/main`: ALLOW, exit 0.
  - The S1 and D1 prep branches touch no X1 target or pin.

**Completeness against the brief and COMMON.** All required sections are present:
- inventory with REQ/AC/VER bindings;
- pinned-reference verification, including the four unreachable cases;
- the FX-PEC-0 redefinition and the R-05 reading;
- the wording-items table;
- lifecycle as add-on L, not assumed;
- `dispatch-for-production` in the packet and `exact-correction-preparation` in preparation;
- the smallest-honest-scope argument and no parser code;
- exact files with postimages, the bound script, the registered v2 check, rollback;
- the Part B landing table (none for X1), old-S2 quotes, external anchors, add-on M, limits and owner questions.

The gaps are findings 1 and 4.

**Conduct.** Status is AWAITING_RULING, and no ruling is recorded that did not occur. CHECKING appears only in the Limits clause and in L272's "implies no … CHECKING"; nothing prompts the owner about CHECKING. `MODE=REVISE` appears only as a one-line disclosure (L26). Owner questions 1–6 are plain, and question 4 leaves the decision to the owner.

## Residual risk
- The fixed/observed tier assignments and which node carries which state rest on review, not tests (disclosed at L45).
- `v2-parsers` fails by design on Git older than 2.44 and on shallow or partial clones, and hosted CI does not run it (disclosed).
- `origin/main` is moving, and HELP_HUMAN must re-verify at publication. Any change to the 12 pinned files before the act makes the preflight refuse, and no re-pin is pre-authorized.
- I did not simulate the A + L failure path.

My directory: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1r3p.Wv6ZLZ`
- `run.log` and `out/`: the check-runner rerun;
- `regen/`: the regenerated act script;
- `hexp/`: the preflight export at `origin/main`.

---

## Dispositions (WORKING_ITEMS)

Nothing blocks. All repairs are to the draft only; no candidate or act byte changes.

1. **Done.** `SHA256SUMS` and the return are written at the end of preparation. The verdicts table now has real rows for verdicts 05 and 06, and its verdict 04 cell states which findings were repaired, deferred and recorded.
2. **Done.** The currency bullet is re-anchored to `origin/main` `f0a6159c9` after a fresh `git fetch`. It names PR #998, the eight other contracts and the S4 records, and restates that no target, pin, `_STATUS.md`, tool or holds file changed (rechecked with `git rev-parse` per file; pins 19/19). The wrong round-2 revision attribution is removed.
3. **Done.** The add-on L section and row 1a now require committing the three `_STATUS.md` changes on the act branch before the act. The "Before merge" rollback carves out the A + L failed-act case: the commits and failure evidence are kept and routed to the owner.
4. **Done.** Add-on M now tables the three repository-relative `MEMORY.md` paths.
5. **Done.** Verifier item 6 now checks the add-on bytes (the `_STATUS.md` diffs under L; the `MEMORY.md` row under M).
6. **Done.** Verdict 05 is the round-3 candidate verdict (PASS WITH NOTES). The `Path.replace` gap is disclosed in the test-module row.

After these edits, `verify_x1p_claims.py` gives 67/67. The draft edits made after this verdict were not re-reviewed by a further fresh reviewer; HELP_HUMAN's PR review covers them.
