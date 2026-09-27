# X1 preparation verdict 03

Reviewer: fresh read-only `pec-reviewer` TASK (agent `ad63f7a86c175b389`, Opus 5.5 as reported by the host), round 2, applying `software-code-review` to the repaired candidates (X1 stand-in for MODE=VERIFY) and backchecking verdict 01. Transcribed verbatim by WORKING_ITEMS from the reviewer's hand-back; dispositions are appended by WORKING_ITEMS after the report.

Reviewed head: `caf8af936` (branch `claude/pec-x1-fixtures-proposal`, PR #996).

---

VERDICT: PASS WITH NOTES

I found no blocking defect. All 35 candidate hashes match the grant table and the bound `apply_x1p.py`. All 19 pins resolve. All 70 golden `source` values occur in their blobs and all 16 `anchor_line` values point at the right construct. No candidate names or scans for the retired sections. The suite passes 10/10 and the negative controls pass 16/16. Verdict 01's single blocking finding is correctly repaired. The notes below are about test strength and wording accuracy. The current golden bytes are correct.

Reviewed HEAD: `caf8af936085a860a08e8b500270a81f3360a8cb` (branch `claude/pec-x1-fixtures-proposal`, PR #996). Since `6c6cc1b00`, every change is under `projects/pec/execution/_Coordination/`. The worktree was clean before and after.

Paths: `<prep>` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26`; `<mod>` = `<prep>/candidates/projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py`.

## Findings (all NON-BLOCKING, most severe first)

**1. The grounding test still accepts some wrong goldens, and the draft overstates what it checks.**
- **Location:** `<mod>` lines 406–415 (anchor check); draft `DRAFT_D-PEC-106_…md` line 44 ("checks every anchor_line against its source values") and line 149.
- **Condition:**
  - The anchor check passes if *any* string source value appears (as a substring) within the 4-line window.
  - 7 of the 16 anchors belong to form expectations that have no `source`, so for them only the line range is checked: the three bullet-form line-5 anchors, DEL-00-08 157, DEL-10-04 16, DEL-12-01 211 and DEL-17-06 123.
  - Nothing checks `equals_folder` or which node carries a state.
- **Evidence:** I applied four single mutations to a scratch copy and each still passed the whole suite:
  - FX-PEC-0 h82 `parenthesized_token` set to `P1_STORE_GUARD_03` (the h109 token);
  - the DEL-00-08 form `anchor_line` moved from 157 to 158;
  - FC-2 `equals_folder` flipped to true;
  - FC-3 terminal `node_id` set to `V1`.
  - A control (the h109 date set to `2026-09-08`) did fail.
- **Impact:** Verdict-01 disposition 2 is only partly done. For goldens the parser packets will rely on, correctness still rests on review.
- **Remediation direction:**
  - Use `all` with word boundaries (every current expectation would still pass).
  - Check source-less form anchors against the source values of sibling expectations on the same entry.
  - Derive `equals_folder` from the pin path.
  - Correct the draft wording.

**2. The widened AST "no write" check still has false negatives and latent false positives.**
- **Location:** `<mod>` lines 121–125 (`WRITE_CALLS`) and 502–524. Draft line 55 claims the check finds "no write, file-creating, copying, permission-changing or process-spawning call".
- **Evidence:** I appended one construct at a time to a scratch copy of the module and ran only this test.
  - Not flagged (test passes): `import subprocess as sp; sp.call(...)`, `os.popen`, `Path.rmdir`, `os.rmdir`, `open(p, m)` with a variable mode, `Path.symlink_to`, `os.execv`.
  - Wrongly flagged (test fails): `open('data.json')` (the letter `a` in the filename is read as a mode), `d.copy()`, `s.replace('a','b')`.
  - The module itself currently contains none of these; I read it in full.
- **Impact:** The claim is overstated. Verdict-01 disposition 12 is partial.
- **Remediation direction:** Take the mode only from the second positional argument or `mode=`. Resolve import aliases. Add `popen`, `exec*`/`spawn*`, `rmdir` and `symlink_to`/`hardlink_to`, or else narrow the claim.

**3. One draft sentence is inaccurate about registry reliance.**
- **Location:** draft line 133: "No DEL-02-08/09 expectation relies on a profile identifier or asserts discovery through the registry."
- **Condition:**
  - `FX-PEC-0.memory.DEL-01-06.no-entries` is fixed with `coverage_limit: true` and bound to DEL-02-09 REQ-001/AC-001. REQ-001 gives that outcome only "for a declared loop". An undeclared loop gets a no-declaration report instead.
  - So this expectation, and the fixed DEL-01-03 run-ID expectations, presuppose that PEC's registry row declares the MEMORY run-index surface. DEL-02-09 TBD-003 and CON-002 say the contract does not rely on that yet.
- **Remediation direction:** Reword line 133, or add this presupposition to the question 2 disclosure (lines 111 and 396).

**4. The SYN-RCP-05 fallback construction does not produce an "unreadable file".**
- **Location:** `<prep>/candidates/.../fixtures/synthetic/MANIFEST.json`, SYN-RCP-05 `construction`.
- **Condition:**
  - A directory or a dangling symbolic link at the ledger path gives a not-a-regular-file or absent condition, not an unreadable one. A parser would likely report it as absent.
  - If the DEL-02-03 parser reads through Git objects, file permissions do not apply at all.
- **Remediation direction:** Say that each parser packet picks an unreadability method that matches its read path. Alternatively, tie the label to REQ-004/AC-004's "explicit limitation" rather than to a specific cause.

**5. Some descriptors are left unclassified, and one binding is loose.**
- `runs_section` (the three FC-2 `no-runs-section` expectations) and the synthetic `placement_folder` are descriptors. The docstring (`<mod>` lines 16–19) and draft line 44 name only `anchor_line` and `equals_folder`, so by elimination these read as outcome labels. Verdict 01 finding 2 named `runs_section` explicitly.
- The `no-runs-section` records bind DEL-02-09 REQ-001/AC-001. REQ-001's coverage limit is for files with no recognizable entry, but these files have a dated-heading entry.

**6. The draft's claim that old Git could not be simulated is wrong.**
- **Location:** draft line 184 ("An old Git (below 2.44) could not be simulated on this host").
- **Evidence:** A PATH shim reporting `git version 2.39.5` simulates it. With the shim:
  - the only Git calls were 5× `version`;
  - all 5 object-reading tests failed with "git older than 2.44 ignores GIT_NO_LAZY_FETCH".
  - With real Git, the logged order was `version`, `rev-parse --is-shallow-repository`, `config --get`, then the first `cat-file blob`.
- **Remediation direction:** Add this shim as a 16th mutation control and correct the sentence. The gate itself is correct.

**7. The draft still claims `SHA256SUMS`, which is absent at HEAD.**
- Draft line 408 says the prep folder has "hashes in `SHA256SUMS`", but the file does not exist at `caf8af936`.
- Verdict-02 disposition 1 defers it to "before publication". It is outside the candidate set, but the claim is untrue at the reviewed revision.

## Verdict-01 dispositions: what I found in the bytes

| # | Status | Evidence |
|---|---|---|
| 1 (blocking) | Implemented and correct | "As-cited token" definition in `<mod>` lines 9–15, draft line 44, Limits line 386. No golden value changed. No representation is fixed. `local_merge_commit` is a warranted full name under DEL-02-08 AC-008. |
| 2 | Partial | See findings 1 and 5. |
| 3 | Implemented by disclosure | `<mod>` lines 21–27, draft line 64. The control was renamed and fails in `test_goldens_are_content_minimal…`. |
| 4 | Implemented | `blob()` gate (`<mod>` lines 234–237). Confirmed with the logging shim. |
| 5 | Implemented | `<mod>` lines 402–405. The three merges are "Merge pull request #876/#873/#868" and ancestors of `d61981ee2`. The `m_merge` control fails. |
| 6 | Implemented | Draft line 48. The docstring defers to the map. The `## Remaining` inspection clause is recorded only in the draft, which is correct, since candidates must not name the sections. |
| 7 | Implemented | FC-1/2/3 `graph.run-identity` bind DEL-02-08 REQ-016/AC-016/VER-016. |
| 8 | Implemented | `FX-PEC-0.ledger.post-marker-entry` / `post-marker-entry-cursor-fields`. |
| 9 | Disclosed | Draft line 111 and question 2. |
| 10 | Reworded | Draft lines 107 and 388. The word check remains only in the prep aid `run_x1p_checks.sh` line 103, as disclosed. |
| 11 | Implemented | Construction texts present. See finding 4 on soundness. |
| 12 | Partial | See finding 2. |

## What I checked

**Reading list.** Root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`, the `software-code-review` skill, the X1P brief, the full DEL-02-08 contract, and every OUT/REQ/AC/VER/CON/TBD line of DEL-02-03 and DEL-02-09. Also both verdicts with their dispositions, the full draft, the full test module, both manifests, all four goldens, and 14 of the 27 synthetic files read in full (the others by targeted greps).

**Hashes (`shasum -a 256`).**
- The three contracts (`c8bb9f1b…`, `2319661b…`, `eab18e17…`) and the three `_STATUS.md` files match the draft and are unchanged since `6c6cc1b00`.
- All 35 candidates equal the grant table and appear in `apply_x1p.py` (`ee731005…3cb4`).
- All aid hashes in the draft match.
- The `software-workflow.json` preimage at `6c6cc1b00` is `8ec9ba6d…8a8b`. The postimage diff adds only the `v2-parsers` check and its path rule.

**Pins and bindings.** `report_x1p_pins.py` gives 19/19: every pin resolves, is an ancestor of the observation commit, has an equal blob, and is unchanged at `6c6cc1b00`. `verify_x1p_bindings.py` gives 433/433.

**Goldens and tiers.**
- A script located all 70 `source` values in their blobs with word boundaries.
- I read in context well over 15 values and all 16 anchors:
  - FC-1 graph: identity at line 5; F1 `ACTIVE` with PR #876 at line 35.
  - FC-1 receipt: Receipt-ID, Examined-Through and Parent-Receipt `none` at lines 39–41; Gate-Outcome is prose at lines 50–53, which supports `gate_outcome_value_emitted: false` as fixed.
  - FC-2 graph: identity at line 5, folder `dec025-…`, F1 `ACTIVE` with PR #873 at line 31.
  - FC-3 graph: identity at line 5, folder `replay-session-…`, "F1 — final PR" at line 27.
  - Registry profiles and states in `loops.json`; `shared-dev-loop` covers `central-receipts` per the schema and adapter.
  - Ledger marker at line 1865: `prefix-bytes=426714`, and I recomputed its sha256 as `153732e3…`. Receipt-197 fields at lines 2187–2190.
  - DEL-01-06 `MEMORY.md` is a template table with no rows.
  - DEL-01-03 headings at lines 3, 16, 82 and 109 carry only decision IDs, prose and parenthesized tokens, which fits DEL-02-09 AC-004/VER-004/CON-004.
  - DEL-00-08 line 157, DEL-12-01 line 211, DEL-17-06 line 123, DEL-10-04 lines 16 and 431, and bullet-form line 5 in all three bullet files.
- I checked all 30 `fixed` expectations against the text they bind, including DEL-02-08 AC-005/AC-006/VER-005/VER-006/REQ-010, DEL-02-03 REQ-007/REQ-014/REQ-015/REQ-016/AC-017/VER-016, and DEL-02-09 REQ-001/REQ-014/AC-004. Each is supported, with the caveats in findings 3 and 5.
- No TBD or CON is pre-empted: DEL-02-03 TBD-007 and TBD-008, DEL-02-08 TBD-003 and TBD-007, and DEL-02-09 TBD-005 and CON-004 are each tiered `observed` or left out.

**Synthetic set.**
- It covers every minimum: DEL-02-08 REQ-017 (6), DEL-02-09 REQ-014 (table form plus 5), and DEL-02-03 REQ-017 (6).
- The six vocabulary states plus `MARINATING` are present. The synthetic marker's prefix sha256 (`936296a7…`, 890 bytes) is genuine.
- My own copy scan against all 301 feed-named blobs at `d61981ee2` and `6c6cc1b00`, net of the two templates, found 0 overlaps at 8 words. At 6 and 5 words the only overlaps are structural (a "## Cursor and pointers - **Receipt-ID:**" heading run and "that is not part of").

**FX-PEC-0.** A case-insensitive grep of all 35 candidates for `remain`, `Remaining` and `_STATUS` returns nothing. No `remaining-loop` source and no `_STATUS.md` pin.

**Test module.**
- Stdlib only, deterministic, one Git call site, read-only allowlist.
- The version, shallow and partial gate runs before the first object read in every test order.
- The merge-subject regex is exact (#87 cannot match #876).

**Runs (TMPDIR set to my mktemp directory; Python 3.13.7; Git 2.54.0).**
- `zsh <prep>/run_fixture_suite.sh <worktree> 6c6cc1b00 <mktemp>/parsers -v`:
  ```
  test_tree_expectations_hold_at_their_pinned_commits (...) ... ok
  ----------------------------------------------------------------------
  Ran 10 tests in 2.546s

  OK
  ```
- `python3 <prep>/negative_controls_x1p.py <worktree> 6c6cc1b00 <prep>`:
  ```
  PASS shallow repository: exit 1; failing tests [5 object-reading tests]
  PASS test missing from the verification map: exit 1; failing tests ['test_loaded_suite_has_exact_verification_mapping']
  RESULT PASS 16/16
  ```

## Residual risk

- The meaning of goldens is still review-verified rather than test-verified (finding 1). I verified the current bytes by hand.
- Partial-clone detection reads only `extensions.partialclone`, not `remote.<name>.promisor`. Egress stays blocked by the Git 2.44+ gate plus `GIT_NO_LAZY_FETCH`, but the clone-type message may not appear in that configuration; the failure would show as `PIN UNREACHABLE` instead.
- The registered `v2-parsers` check fails by design on Git older than 2.44 (for example 2.39.x on older Apple command-line tools or Debian 12) and on shallow or partial clones. Hosted CI does not run it.
- `v2-parsers` path selection covers only `v2/tests/parsers/**` and `software-workflow.json`. The parser packets must widen it.
- A stray `.DS_Store` under `fixtures/synthetic/` would fail the "every synthetic file is listed" check (local false failure only).

## Scratch

My mktemp directory is `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1r2c.ybNMJo`. It holds the candidate copy `parsers/` and the logging Git shim `shim/`. The mutation copies were removed. The suite runner and the negative-control script cleaned up their own temporary directories inside it.

I wrote nothing in any worktree and made no branch operations.

---

## Dispositions (WORKING_ITEMS)

1. **Repaired.** The grounding test now makes three checks. Every source string of an anchored expectation must occur, with word boundaries, at or just after its `anchor_line` (all values, not any). A source-less form anchor must sit on a line that itself carries a source value of another expectation on the same pin. And `equals_folder` must agree with the pin path's folder. New negative controls cover the reviewer's mutations: the h82/h109 token swap, the DEL-00-08 form anchor moved to 158, and FC-2 `equals_folder` flipped. The FC-3 terminal `node_id` change still cannot be caught without parsing; the draft now says which node carries which state rests on review.
2. **Repaired.** The mode is now taken only from the mode position or `mode=`, so `open('data.json')` no longer false-flags. A non-constant mode is flagged. Aliased and `from` imports of guarded modules are flagged. `os` functions are matched on the `os` owner (including `popen`, `exec*`, `spawn*` and `rmdir`). The `Path` methods include `rmdir`, `symlink_to` and `hardlink_to`. Generic names (`copy`, `replace`, `remove`) are no longer matched on arbitrary objects. The draft's claim is narrowed to "a listed set … a guard, not a proof".
3. **Repaired.** The draft sentence now states the presupposition (DEL-02-09 REQ-001 "for a declared loop"; PEC's row declares the run index at the pin; TBD-003/CON-002). Question 2 discloses it.
4. **Repaired.** SYN-RCP-05's construction now says to make the copy unreadable through the parser's own read path (filesystem permission, or a blob the object store cannot supply). Each parser packet names its method, and the required outcome is the explicit limitation, not a particular cause.
5. **Repaired.** The docstring names `runs_section` and `placement_folder` as descriptors. The three `no-runs-section` records are rebound from REQ-001/AC-001/VER-001 to REQ-002/-014, AC-002/-014 and VER-002/-014, with fact `no-runs-section-read-in-dated-heading-form`.
6. **Repaired.** A `PATH` shim reporting `git version 2.39.5` is now a negative control. The five object-reading tests fail on it, and the draft's claim that it could not be simulated is removed.
7. **Repaired before publication.** `SHA256SUMS` is written at the end of preparation.

Clearing verdict 01's blocking finding: this verdict (03) confirms it repaired at `caf8af936`.
