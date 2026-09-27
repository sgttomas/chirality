# X1 preparation verdict 01

Reviewer: fresh read-only `pec-reviewer` TASK (agent `a06d00c19237ea136`, Opus 5.5 as reported by the host), applying `software-code-review` to the candidates (X1 stand-in for MODE=VERIFY). Transcribed verbatim by WORKING_ITEMS from the reviewer's hand-back; dispositions are appended by WORKING_ITEMS after the report.

Reviewed head: `98af674e8` (branch `claude/pec-x1-fixtures-proposal`, PR #996).

---

VERDICT: FAIL

One blocking finding: the stated meaning of an `observed` expectation fixes value representations that DEL-02-03 TBD-007 leaves to production, and it cannot be met for link targets under DEL-02-09 REQ-003. The fix is textual, or a few value changes. Otherwise the candidates hold up. All 19 pins resolve. All 70 golden `source` values and all 16 `anchor_line` values are correct. The three local merge commits are the right PR merges. The synthetic set covers every contract minimum and copies no text from other loops. The suite passes (10/10) and fails closed.

Paths below are relative to `projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/` (the prep folder). Candidates are under `candidates/projects/pec/v2/tests/parsers/`, shortened here to `<parsers>`.

## Findings

**1. BLOCKING — the `observed` definition pre-empts DEL-02-03 TBD-007 and conflicts with DEL-02-09 REQ-003.**
- **Location:**
  - `DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md` line 42.
  - `FC-1.json`: `FC-1.receipt.parent-receipt`, which has `{"parent_receipt":"none"}` and binds TBD-007.
  - `FX-PEC-0.json`: `FX-PEC-0.ledger.marker-governed-entry`, with `Receipt-197` / `Receipt-196`.
  - `link_target_as_cited` and `evidence_link_target_as_cited`, in six expectations: FC-1 DEL-08-01 and DEL-08-05, FC-2 DEL-10-04, and FC-3 DEL-05-04.
- **Condition:** Line 42 says that if the parser yields the fact, "its value must equal this one".
  - TBD-007 says the representation of a Receipt-ID and of a Parent-Receipt "such as `none`" is not fixed.
  - DEL-02-09 REQ-003 requires link targets to be emitted as normalized repository-relative paths. The golden instead holds the un-normalized relative form, `../../../_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md`.
  - The same equality rule applies, less sharply, to dates under REQ-005, whose form is the grammar's choice.
- **Impact:**
  - A conforming parser that represents `none` as null, or Receipt-197 as its number, fails the golden.
  - A parser that normalizes links as REQ-003 requires can never equal the as-cited value.
  - The packet would therefore settle a TBD, which its own Limits section (line 376) and the verifier checklist (line 342) say it does not do.
- **Remediation direction:** Redefine `observed` as the as-cited source token. A parser that yields the fact must yield the value its declared representation or normalization maps from that token, or mark it unavailable. Alternatively, store normalized link targets, for example `projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md`.

**2. NON-BLOCKING — `expect` mixes output facts, fixture descriptors and invented labels with nothing to tell them apart.**
- **Location:**
  - Goldens: 16 `anchor_line` values (11 under `fixed`), plus `equals_folder` and `runs_section`.
  - Label values: `form` ("bullet", "dated-heading", "table"), `generation` ("central-receipt"), `derived_claims` ("none").
  - Synthetic `limitation` values: "missing-run-identity", "unrecognized-state", "no-node-table", "malformed-ledger". Also `pr_resolution` "unresolved-locally" and `receipt_id_source` "cursor-field".
- **Condition:** A `fixed` expectation means "any conforming parser must produce it" (line 41). Line numbers as anchors, and these label words, are not contract vocabulary: REQ-009 leaves the anchor form open, REQ-009 leaves fault names open, and the grammar declarations and DEL-01-01 own the rest.
  - The pinned drafter's return (`evidence/drafter_returns/PINNED_DRAFTER_RETURN.md` line 1674) says `anchor_line` "is not a parser output field". Neither the committed bytes nor the proposal says so.
  - No test checks `anchor_line`. I checked all 16 by hand and they are correct.
- **Remediation direction:** State in the proposal, and ideally in the schema, that label values are semantic labels and that `anchor_line` and `equals_folder` are locators or descriptors. Or move them into a separate object, and add a test that each anchor line contains its source values.

**3. NON-BLOCKING — the three-word source-run check in the goldens can never fire.**
- **Location:** `<parsers>/test_parser_fixture_integrity.py` line 384, after the check at line 376.
- **Condition:** Line 376 already requires every string to be a single token with no whitespace, so the three-word run set at line 384 is always empty. The negative control that should exercise it (`m_prose`, `negative_controls_x1p.py` line 39, value "Stable run identity") fails at line 376 instead. As a result, `source_run_words` is never exercised.
- **Impact:** The single-token rule does enforce the property for text separated by spaces. Prose joined with hyphens or underscores, up to 200 characters, passes both checks.
- **Remediation direction:** Either say that the token rule is the check actually enforced, or run the source-run check on text with non-alphanumeric characters turned into spaces, and add a negative control that reaches it.

**4. NON-BLOCKING — the no-network guarantee depends on Git 2.44+, which the suite does not enforce.**
- **Location:** `assert_repository_can_hold_pins` (lines 195–199) is called only in two tests, `test_pins_resolve…` and `test_tree…`.
- **Condition:** In alphabetical order those two run 8th and 10th. Three earlier tests read blobs first: `test_golden_source_values…`, `test_goldens_are_content_minimal…` and `test_no_fixture_source…`. On a partial clone with Git older than 2.44, which ignores `GIT_NO_LAZY_FETCH`, `cat-file blob` can fetch over the network before the partial-clone refusal runs.
- **Impact:** The no-egress requirement (DEL-02-08 REQ-019, DEL-02-09 REQ-015, DEL-02-03 REQ-012) holds only under a Git version the proposal states but the suite never checks. The proposal's "The suite checks first" (line 148) is not true for those three tests.
- **Remediation direction:** Run the check in `setUpClass` or inside `blob()`, and optionally check the Git version.

**5. NON-BLOCKING — the `local_merge_commit` check accepts any merge that is an ancestor of the pin.**
- **Location:** Lines 358–365.
- **Condition:** The test confirms the commit is a merge integrated at the pin, but not that it merged the cited PR.
- **Evidence:** The three values are correct. Their subjects are "Merge pull request #876 / #873 / #868", and each is an ancestor of d61981ee2.
- **Remediation direction:** Check the commit subject with `cat-file commit`, which is already allowlisted. Label it a fixture check, not the parser's resolution method, which TBD-003 leaves open.

**6. NON-BLOCKING — the `TEST_TO_VERIFICATION` map names more verification items than the stated scope.**
- **Location:** The docstring (lines 4–5) and proposal line 46 list only DEL-02-03 VER-017, DEL-02-08 VER-016/VER-017 and DEL-02-09 VER-014. The map (lines 56–67) also names:
  - DEL-02-03/VER-016, for the tree test;
  - DEL-02-03/VER-013, DEL-02-08/VER-020 and DEL-02-09/VER-016, for the mapping test.
- **Impact:**
  - Those last three items require every verification item to have an executing test. The mapping test implements only the mapping mechanism.
  - DEL-02-03 VER-017's clause "absence of any `## Remaining` read" can only be met by inspection, because of the carried constraint. No mapped test covers it, and nothing says so.
- **Remediation direction:** Make the docstring and proposal list match the map, or remap. Record that the `## Remaining` clause is met by inspection.

**7. NON-BLOCKING — no record binds DEL-02-08 REQ-016 or AC-016.**
- **Location:** Proposal line 92 says DEL-02-08 pinned expectations bind "REQ-016/AC-016/VER-016 (the pinned suites)".
- **Evidence:** A grep finds no golden or tree record binding DEL-02-08/REQ-016 or AC-016; only the test map names VER-016. The other two deliverables do bind theirs: DEL-02-03 through the tree records (REQ-017/AC-018/VER-017), and DEL-02-09 through the form records (REQ-014/AC-014/VER-014).
- **Remediation direction:** Add the bindings to the FC graph records, or correct the table.

**8. NON-BLOCKING — one fact label assumes which ledger entries the marker governs.**
- **Location:** `FX-PEC-0.json`, `FX-PEC-0.ledger.marker-governed-entry`, fact `marker-governed-entry-fields`.
- **Condition:** Proposal line 44 lists "which ledger entries the marker governs" as grammar-dependent and left out, as DEL-02-03 REQ-003 and TBD-002 require. The fact label assumes Receipt-197 is governed. The `observed` tier softens this.
- **Remediation direction:** Rename the fact neutrally, for example "post-marker entry cursor fields".

**9. NON-BLOCKING, disclosed — FX-PEC-0 records serve DEL-02-08 and DEL-02-09 despite their CON-004 and the d61981ee2 pin.**
- **Condition:** DEL-02-08 CON-004 says the contract "adds no FX-PEC-0 output", and reading PEC's graph depends on the registry declaration (CON-002). DEL-02-08 REQ-016/VER-016 and DEL-02-09 REQ-014/VER-014 pin fixtures at d61981ee2, yet the mapped tests cover a manifest that includes pins at 6c6cc1b00.
- **Status:** The proposal discloses this and puts it to the owner as question 2. It is noted here only so the ruling covers it explicitly.

**10. NON-BLOCKING — "nothing committed repeats it" is not literally true.**
- **Location:** Proposal line 105, against `run_x1p_checks.sh` line 100 (`if "remaining" in t.lower()`).
- **Condition:** `run_x1p_checks.sh` is committed on this branch (commit 50268832c). It is named as "the rerun method", and the grant (line 349) copies the check aids into the run root.
- **Evidence:** No product postimage and no registered check scans for the word. I grepped all 35 candidates case-insensitively for "remain" and found nothing. No candidate names `remaining-loop` or a `_STATUS.md`, and no expectation touches DEL-01-03 MEMORY line 39 (the `REM-001..003` heading).
- **Remediation direction:** Reword to "no product file or registered check". If the owner's "no scanning" covers prep aids too, drop the word check.

**11. NON-BLOCKING — two construction-only cases are loosely specified.**
- **Location:** `<parsers>/fixtures/synthetic/MANIFEST.json`.
- **Condition:**
  - SYN-RCP-05 makes a file unreadable by removing read permission. That does not work when tests run as root, as in many CI containers, so the parser packets need another method.
  - SYN-RCP-07 needs the receipt placed in folder `SYN-RUN-RCP-FOLDER-0702` at test time. The manifest has no `construction` text for it; only the `placement_folder` expect key implies it.

**12. NON-BLOCKING — the AST "no write call" test is narrow.**
- **Location:** `WRITE_CALLS` at line 98 and the scan at lines 452–466.
- **Condition:** The scan misses `.open("w")` called as an attribute, `os.open`, `shutil.*`, `json.dump` and `from subprocess import run`. The current module has no write call (I read it all), so the proposal's claim "No write call (checked by an AST test)" is overstated rather than false.

## What I checked and how

- **Reading list:** Root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`, the X1P brief, the `software-code-review` skill, the full DEL-02-08 contract, and the REQ/AC/VER/CON/TBD/OUT lines of DEL-02-03 and DEL-02-09. From SCA-005 I read Propagation_Plan §B7, Impact_Assessment R-05 and §9.3, and the proposal in full.
- **Recomputed hashes (`shasum -a 256`):**
  - The three contracts and three `_STATUS.md` files match the proposal.
  - Propagation_Plan and Impact_Assessment match (`50cd0b1d…1350`, `0bcbe9bd…39bf`).
  - The `software-workflow.json` preimage at 6c6cc1b00 is `8ec9ba6d…8a8b`.
  - All 35 candidate hashes equal the grant table.
- **Pins and merges:** All 19 pins resolve with `rev-parse`. Each commit is an ancestor of 6c6cc1b00, each blob matches, and each is unchanged at the observation commit. The three tree records match `ls-tree`. The three `local_merge_commit` values are the PR #876, #873 and #868 merges and ancestors of the pin.
- **Golden values:**
  - My own script checked every `source` value against `git show` of its blob (70 values, well over the 15 asked). All occur, and the memory-entry values fall inside their anchor regions.
  - I checked every `anchor_line` against the blob lines.
  - F1 is `ACTIVE` in all three FC graphs. Identity bullets use the plain spelling and name the §B7 IDs. FC-3's F1 cell carries the em-dash suffix.
  - The FC-1 receipt has cursor fields at lines 39–53. The PEC ledger has the marker (its prefix hash verifies) and the Receipt-197 fields. The registry holds `pec`, `shared-dev-loop` live and `loop-receipts-ledger` historical.
- **Tiers:** I read each `fixed` expectation against the requirement, criterion and verification text it cites (for example DEL-02-08 VER-005/VER-006/REQ-010, DEL-02-03 VER-016/REQ-007/REQ-015/CLM-018, DEL-02-09 AC-004/VER-004/CON-004). Apart from findings 1 and 2, the tiers are supported.
- **Bindings:** All 424 references are defined in their contracts at the observation commit. The requirement/criterion/verification pairings match each contract's matrix.
- **Synthetic set:**
  - I read all 27 files. They cover the minimum cases of DEL-02-08 REQ-017, DEL-02-09 REQ-014 and DEL-02-03 REQ-017.
  - The synthetic ledgers' marker prefix bytes and hashes are genuine.
  - Every decoy and marker value in `expect` occurs in its file.
  - I scanned for runs of copied text against every `.md` file outside `projects/pec` at 6c6cc1b00 and d61981ee2. At 8 words, after subtracting the two templates, there are 0 overlaps. At 6 words there are two structural fragments (a "Cursor and pointers" heading run and "that is not part of the").
- **Workflow postimage:** The diff is minimal (one new check, `v2-parsers`, and one path rule) and the JSON is valid. The posture checker, run with the candidate workflow, returns PASS with `core_tree_sha256` `dd7e1dda…6e5a` and `workflow_sha256` `d55fff77…0bbd`. Affected-check selection for `v2/tests/parsers/**` includes `v2-parsers`.
- **Fail-closed behaviour:** I built four scratch repos in my own temp directory. In every case the suite fails with the unreachable-pin or clone-type message; nothing is skipped and nothing errors.
  - HEAD at d61981ee2: the FX-PEC-0 and template pins are not ancestors.
  - No objects: every pin reports commit or blob not present.
  - Shallow marker: refused.
  - `extensions.partialClone` set: refused.
- **Suite run:** `zsh <prep>/run_fixture_suite.sh <worktree> 6c6cc1b00 <mktemp>/parsers -v`, with Python 3.13.7 and Git 2.54.0. Tail:
```
test_tree_expectations_hold_at_their_pinned_commits (...) ... ok
----------------------------------------------------------------------
Ran 10 tests in 3.094s

OK
```
- **Worktree:** Clean afterwards (`git status --short` empty). I made no writes to any worktree and no branch operations.

## Residual risk

- Apart from `source` occurrence, the suite does not check the meaning of goldens: which node carries which state, `anchor_line`, the merge's PR, or synthetic label tokens. Their correctness rests on review; I verified them all by hand at this commit.
- `v2-parsers` is selected only by changes under `v2/tests/parsers/**` and `software-workflow.json`. The parser packets must widen the rule when they add source under `v2/src/**`.
- Hosted CI would need a full, non-shallow, non-partial clone. The proposal discloses this.
- Findings 1 and 2 also bear on owner question 3, golden scope.

## Scratch

My temp directory is `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1rev.nJtYcR`. It holds the candidate copy, the scans and the scratch repos `rA`–`rD`. My first `mktemp -d` ignored `TMPDIR` and created an empty directory under `/var/folders/...`; I removed it at once with `rmdir`.

---

## Dispositions (WORKING_ITEMS)

1. **BLOCKING — repaired.** Golden `source` values are now defined as the tokens exactly as cited, in the test module's docstring and in the draft ("Smallest honest scope"). A parser that yields a fact yields the value its declared representation maps from the cited token (a normalized path, a date form, a TBD-007 representation), or marks the fact unavailable. The tier now fixes only whether yielding is obligatory. No golden value changed; the Limits section now states that no value representation is settled.
2. **Repaired.** The docstring and draft separate outcome labels (fixture-local, not an output vocabulary) from descriptors (`anchor_line`, `equals_folder`, which are never parser output). The grounding test now checks that each `anchor_line` lies in the blob with a source value at or just after it, and a negative control proves this.
3. **Repaired by disclosure.** The docstring and draft say that for goldens the single-token rule is the enforced form, and that the run check is kept for parser output. The negative control is renamed to say which rule catches it. Splitting on non-alphanumerics was rejected, because it would flag every legitimate multi-part identifier.
4. **Repaired.** The repository check (Git 2.44 or later via the allowlisted `git version`, non-shallow, no partial clone) now runs before the first object read in any test (once per class, inside `blob()`) as well as in the two resolution tests.
5. **Repaired.** The grounding test now also requires each `local_merge_commit` subject to read "Merge pull request #N from …" for the cited PR. It is labelled a fixture sanity check, not the TBD-003 method, and a negative control covers it.
6. **Repaired.** The docstring and draft now list every mapped VER as fixture-side only, and the mapping-test VERs as mechanism only. They record that DEL-02-03 VER-017's no-`## Remaining`-read clause is met by inspection.
7. **Repaired.** DEL-02-08 REQ-016/AC-016/VER-016 are bound on the three FC graph identity expectations.
8. **Repaired.** Renamed to `FX-PEC-0.ledger.post-marker-entry`, fact `post-marker-entry-cursor-fields`.
9. **Disclosed.** The FX-PEC-0 section and owner question 2 now say explicitly that FX-PEC-0 records bind DEL-02-08/09 requirements despite CON-004 and CLM-013.
10. **Repaired by rewording.** The draft now says the word check lives in the preparation aid, that no product file, fixture, test or registered check scans for it, and that the line can be dropped if the owner's direction extends to preparation aids.
11. **Repaired.** SYN-RCP-05's construction gives a method for hosts that do not enforce permissions (a directory or a dangling symbolic link), and SYN-RCP-07 gains a construction text for its placement folder.
12. **Repaired.** The AST check now also flags `from subprocess/os/shutil/tempfile import`, `shutil`/`tempfile` imports, `os.open`, any `open` with a write, append, create or update mode, and copy, dump, move, chmod, link, truncate, touch and temporary-file calls.

After these repairs: the candidate suite passes 10/10; negative controls pass 16/16; `run_x1p_checks.sh` gives OVERALL PASS at `6c6cc1b00`.
