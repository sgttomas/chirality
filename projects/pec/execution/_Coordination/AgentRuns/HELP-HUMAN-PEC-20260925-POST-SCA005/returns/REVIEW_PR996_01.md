# Review 01 of PR #996, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `4f2e4f44a182109e6a5189ef70bc76f1c8b266f0`. The X1P manager's repairs (to `9fa634f1e`) and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `f62d26449122af0a7c580eaf2be6cbd55b670a01db79a2a44b863b65fa345cbc`.

## Report (verbatim)

**Verdict: PASS WITH NOTES.** Nothing blocks. Before HELP_HUMAN publishes, the draft needs two wording fixes (findings 1 and 2), and the trailing-whitespace item (finding 3) needs a decision.

I reviewed PR #996 at head `4f2e4f44a182109e6a5189ef70bc76f1c8b266f0`. Its parents are `6ab42ec4b` and `origin/main` `f0a6159c9`. I read everything with `git show`, `git diff` and `git archive` into a `mktemp -d` directory under the session scratchpad, with `TMPDIR` pointed at it. I made no edits and no git writes, and afterwards I deleted my scratch directory. Below, "prep" means `projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/`.

## Reproduction
- **Full check run.** I ran `run_x1p_checks.sh` against `origin/main` `f0a6159c9` and got **OVERALL PASS**:
  - act: check-only exit 0, apply exit 0, second run refuses with exit 1;
  - containment: `software-workflow.json` modified plus 34 new files, nothing else;
  - all six affected checks exit 0; `v2-parsers` runs 10 tests, all ok;
  - bindings 442/442; pins 19/19; draft claims 67/67;
  - strict, harness and receipts outputs identical before and after. Strict exits 1 because of 26 older `XRG-013` warnings, as the draft says;
  - hygiene PASS; fault injection 11/11; negative controls 20/20.
- **`shasum -a 256 -c SHA256SUMS`.** All 87 files OK. Its coverage equals the prep file list minus `SHA256SUMS` itself.
- **Hashes recomputed.**
  - All 35 grant-table postimages match the candidates, and the candidate set equals the table.
  - Preimage `8ec9ba6d…`, the 12 files the act pins as read-only, the three `_STATUS.md`, `write_status.sh`, the holds register, the aid table and brief `1cefcc48…` all match, at both `6c6cc1b00` and `f0a6159c9`.
  - Draft `c43dbb9f…95e3` and `apply_x1p.py` `452ff66a…2428` confirmed.
- **Candidate stability.** No candidate or act-script byte changed from `082a2a96f` (verdicts 05 and 06) to the head.

## The act and its tests
- **`apply_x1p.py` follows the precedent.** It mirrors D-PEC-100's `apply_s2p.py`: pins, write to a temporary file then rename, rollback, write-set inventory, refusal of a second run, and the run-root guard. The fault injection exercises each of these.
- **The `software-workflow.json` change is purely additive.** One new check and one new path rule. `always_checks` and the other rules are unchanged, and the `v2-core-posture` rule is untouched.
- **Nothing else is affected.** I also ran the unregistered `v2/tests/enforcement` suite on a tree with the change applied: 28 tests OK. Those tests read `software-workflow.json`.
- **Fixture module.** I ran it with the head as `HEAD` (`-v`): 10/10 OK.
- **No parser code.** The only Python file is the stdlib test module, and nothing is added under `v2/src/**`.

## Content, pins, FX-PEC-0 and the draft
- **Pins.** Independently checked: all 19 `(commit, path, blob)` resolve and each commit is an ancestor of `origin/main`.
- **Goldens.** All 70 source values occur verbatim in their pinned blobs. 65 expectations, 30 `fixed` and 35 `observed`.
- **Bindings.** 411 fixture references plus 31 in the verification map make the 442, all defined in the three contracts.
- **Tier sample.** The `fixed`/`observed` split holds against DEL-02-08 TBD-002/003/007, DEL-02-03 TBD-007 and DEL-02-09 AC-004 and CON-004.
  - FC-2's bare-token dated headings are `observed`.
  - FX-PEC-0 headings carrying only a decision ID or a parenthesized token are `fixed` unavailable, as are SYN-MEM-06's.
- **Copied text.** None of the synthetic files shares an 8-word stretch with any of 14,148 `.md` files outside `projects/pec` (net of the templates). At 6 words the only overlaps are structural.
- **FX-PEC-0.** No candidate contains "remaining" in any case, pins a `_STATUS.md` or uses a retired profile. The R-05 reading is sound. D-PEC-99 Part B goes to S1, S2 and S4 only (4+4+4).
- **Add-ons.** Add-on L is offered, not assumed (Q4; option A makes no lifecycle change). The D-PEC-85 clause and SPEC §3.2/§3.3 are quoted verbatim, and the 10 dependency rows are ACTIVE / `INITIALIZED` / `PENDING` as tabled.
- **Draft changes after verdict 06.** Six hunks: currency bullet, add-on L commit step, add-on M paths, verifier item 6, rollback carve-out, verdict table. All check out: 285 PEC paths changed and 8 other contracts, as stated.

## Findings

**NON-BLOCKING**
1. **Draft L65 and Q3 (L404) rest on a false premise.** The draft says PEC-K-10 values, "paths" included, "are single tokens and never trip" the 3-word no-source-text rule. Piping paths contain spaces. Pinned blob `15dcfee1…` (FC-1 DEL-08-01 `MEMORY.md`) cites `execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/…` at L53, L105 and L175. A parser that emits such a path would share 3-word runs with the source. The test module itself exempts `.path` and `.tree` leaves (`test_parser_fixture_integrity.py:210`). The owner is asked to confirm "never three words in a row" as the rule for parser output. Fix: correct the rationale and state how paths are treated before publication.
2. **Draft L62–66, L392 and Q3 L403–407 frame the copy threshold as TBD-assigned.** DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign only the no-source-text threshold (plus golden format and blobs). The 8-word copy threshold operationalizes an absolute rule ("shall contain no text copied": DEL-02-08 REQ-017, DEL-02-09 REQ-014, DEL-02-03 REQ-017). Also, Q3 does not tell the owner that DEL-02-08 TBD-006, unlike the other two, does not hand the threshold to this packet; only L62 and L392 say so. Fix: say this plainly in Q3.
3. **`git diff --check` is not clean.** It flags trailing whitespace at `evidence/run_main/SUMMARY.out:6`. The cause is `run_x1p_checks.sh:66` (`tr '\n' ' '`). The act PR will hit the same problem: finite-verification row 9 (draft L347) requires `git diff --check` to be clean, and the run root will hold this aid's output. Fix: trim the space in the aid, then regenerate the output and `SHA256SUMS`.
4. **The return overstates pin currency.** `returns/X1P_FIXTURES_PROPOSAL.md:94` says every pin "is unchanged at `6c6cc1b00` and at `origin/main` `f0a6159c9`". At `f0a6159c9` the `FX-PEC-0.graph` path has blob `8e32fc0fd`, not the pinned `bf0b0c626`. `report_x1p_pins.py` shows "changed 8e32fc0fd"; this is informational, because the pin is by blob. Draft L149's "so there is no drift today" is similarly loose; L19 handles it correctly.

**NOTE**
5. `COMMON.md` (`51b70e46…`) is cited at draft L3 and in the return, but it is not in the tree. The brief (L8) says it sits "beside this brief". It lives in the manager's scratchpad (`acts2/`), so a reviewer cannot verify it.
6. The preparation aid scans candidate bytes for "remaining" (`run_x1p_checks.sh:103`). This is disclosed at draft L108, with an offer to drop it. It is the owner's call under the no-scanning direction.
7. The grant allows the act to run "once" (L199). The draft does not say whether a rolled-back exit-1 run uses up that one run. Under A + L this matters for the retry path.
8. The aids default to `/tmp` when `TMPDIR` is unset (`run_x1p_checks.sh:9`, `run_fixture_suite.sh:9`). Harmless for the act, but worth knowing for anyone rerunning them.
9. Residuals the return already discloses remain for the first parser packet: gaps in the AST guard, and widening the path rule when parser source lands under `v2/src/**`. Hosted CI does not run `v2-parsers`, and that check needs a full clone.

## Containment and CI
- **Containment.** The diff against `origin/main` touches only the 88 prep files plus the brief and the return.
- **CI at the head.** PR #996 is open, MERGEABLE and CLEAN. Every check ran on `4f2e4f44a` and passed or was skipped. Passing: `pec`, `harness`, Harness pre-merge, Select PEC/App/source coverage, Desktop E2E. Skipped by path selection: PEC workspace tests, App and source suites.

Files:
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/run_x1p_checks.sh
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/evidence/run_main/SUMMARY.out
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/X1P_FIXTURES_PROPOSAL.md

(These paths are as they exist at the PR head; this worktree is on a different branch.)

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. HELP_HUMAN sent the findings and notes back to the X1P manager, which repaired them at head `9fa634f1e`. Its fresh verdict 07 failed on a new path-resolution rule. The manager repaired that, and verdict 08 is PASS WITH NOTES. Both verdicts are in the prep folder. In summary:

- **NB-1:** the false "paths are single tokens" rationale is removed. The draft and Q3 state how paths and tree values are treated. In parser output, a path field is exempt from the word count and checked by shape only.
- **NB-2:** Q3, the body and Limits now say plainly which thresholds each TBD assigns. The 8-word copy threshold operationalizes the absolute no-copy rules, and DEL-02-08 TBD-006 does not assign it.
- **NB-3:** the aid now joins lines with `paste`, the evidence is regenerated, `SHA256SUMS` is updated, and `git diff --check` is clean.
- **NB-4:** the pin-currency statements are corrected: the `FX-PEC-0.graph` path holds `8e32fc0fd` at `f0a6159c9`, and the pin is by blob.
- **Note 5:** the brief's COMMON rules are committed as `briefs/COMMON_PREP_RULES_2026-09-26.md` (`51b70e46…b311`).
- **Note 6:** at HELP_HUMAN's direction, and under the owner's no-scanning direction, the "remaining" byte scan and the draft's offer about it are removed.
- **Note 7:** the grant states when a run consumes the single run.
- **Note 8:** the aids fall back to `.scratch/` beside the script, never `/tmp`.
- **Note 9:** carried to the first parser packet.

The repair head needs a fresh HELP_HUMAN review before merge.
