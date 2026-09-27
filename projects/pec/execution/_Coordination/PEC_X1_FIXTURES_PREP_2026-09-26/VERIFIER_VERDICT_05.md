# X1 preparation verdict 05

Reviewer: fresh read-only `pec-reviewer` TASK (agent `adf39dc6cd2bca1a2`, Opus 5.5 as reported by the host), round 3, applying `software-code-review` to the candidates (X1 stand-in for MODE=VERIFY) and backchecking verdict 03. Transcribed verbatim by WORKING_ITEMS from the reviewer's hand-back; dispositions are appended by WORKING_ITEMS after the report.

Reviewed head: `082a2a96f` (branch `claude/pec-x1-fixtures-proposal`, PR #996).

---

VERDICT: PASS WITH NOTES

Nothing blocks. All seven verdict-03 dispositions are in the bytes. Only disposition 1 is partial: form anchors are checked against any expectation on the same pin, not the same entry, as verdict 03 suggested. All 35 candidate hashes match the draft's grant table and `apply_x1p.py`. The goldens are correct at the pins. The suite passes 10/10 and the negative controls pass 20/20. The notes below are about how strong the tests are and how accurately the draft describes them.

Reviewed HEAD: `082a2a96f5f4a46f90263daa7d22a6b399e84842` (branch `claude/pec-x1-fixtures-proposal`, PR #996). Observation commit `6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`; pinned foreign commit `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b`.
- `git status` in the worktree was clean before and after; I wrote nothing there.
- Since verdict 03's head `caf8af936`, the candidate changes are the test module, `FC-2.json` (the three `no-runs-section` rebindings only) and the synthetic `MANIFEST.json` (the SYN-RCP-05 construction only).

Paths used below: `<prep>` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26`; `<mod>` = `<prep>/candidates/projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py`; `<draft>` = `<prep>/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md`.

## Findings (most severe first)

**1. NON-BLOCKING — The grounding test still passes some wrong goldens, and the draft names only part of what rests on review.**
- **Location:** `<mod>` L79 (`BOUNDARY`), L200–203 (`occurs`), L420–438 (anchor checks). `<draft>` L45 (the three descriptor checks; "Which node carries which state … rests on review"), L64 ("checked against the blob with word boundaries") and L185 (negative control "a form anchor moved off its entry").
- **Condition:**
  - A form anchor passes if its line carries a source value of *any* expectation on the same pin, not the same entry.
  - A valued anchor passes if all its values fall anywhere in the 4-line window `anchor..anchor+3`, so the anchor can sit up to 3 lines before the construct.
  - Expectations without an anchor (graph, receipt, ledger, registry) are checked only for occurrence somewhere in the blob, not against their field or entry.
  - `-` is not a boundary character, so a value cut short at a hyphen still passes.
  - The `runs_section: false` descriptor is never checked.
- **Evidence:** I made single mutations of a copy of the candidates and ran them through `run_fixture_suite.sh`. Each of these passed the whole suite (exit 0):
  - m1: FC-2 DEL-10-04 bullet-form `anchor_line` moved from 16 to 431, which is the dated heading.
  - m2: FX-PEC-0 ledger post-marker fields replaced with Receipt-196's values (`Receipt-196`, `961ee105…8c95`, `Receipt-195`).
  - m3: FC-2 `run_identity` cut to `PIP-DEC025-BASELINE-2026-09`.
  - m4: DEL-01-03 h3 `anchor_line` moved from 3 to 1, the title line.
  - m6: the `fixed` FX-PEC-0 `registry.ledger-profile` state and `receipt_label` flipped to `live`.
  - Control m5 (the FC-1 SHA cut to `8645c269`) did fail.
- **Impact:**
  - Verdict-03 disposition 1 is only partly done: the form-anchor check uses the same pin, not the same entry.
  - Most golden meaning (which value belongs to which field or entry, and the `fixed` registry state) still rests on review. The draft discloses this only for node states.
  - L185's phrase "a form anchor moved off its entry" is broader than what the control actually shows (157→158).
  - The current bytes are correct:
    - all 55 string source values occur as complete tokens, even with the stricter boundary set `[A-Za-z0-9_\-./]`;
    - all 16 anchors are on the exact construct line;
    - DEL-00-08, DEL-12-01 and DEL-17-06 have no `## Runs` heading.
- **Remediation direction:** either of the following.
  - Tighten the test:
    - require the anchor line itself to carry the entry's primary value;
    - check a form anchor only against siblings with the same `anchor_line`;
    - add `-` to the trailing boundary;
    - give the ledger, receipt, registry and graph expectations `anchor_line`s;
    - check that `runs_section` agrees with whether the blob has a `## Runs` heading.
  - Or widen the L45 and L185 wording so it says that every value-to-field or value-to-entry association, not only node state, rests on review.

**2. NON-BLOCKING — The AST guard does not fully match the draft's list.**
- **Location:** `<mod>` L124–132 (`PATH_WRITE_METHODS`, `OS_WRITE_FUNCTIONS`) and L545–568. `<draft>` L56 lists "`Path` write, delete, rename … methods; `os` write … functions".
- **Evidence:** I appended one construct at a time to a copy of the module.
  - Not flagged (the test passes):
    - `p.replace('t')`: `Path.replace` is a rename method, dropped along with the generic names;
    - `os.write(1, b'x')`;
    - `sp = subprocess; sp.Popen([...])`: assigning the module to a name escapes the check that allows only one subprocess call site.
  - Wrongly flagged (the test fails): `io.open('data.json')`, because for attribute calls position 0 is read as the mode. This is latent only; the module contains none of these.
- **Impact:** The disclosure "the list is a guard, not a proof" holds, but the list as written names categories the code does not fully cover.
- **Remediation direction:**
  - Add `write`, `ftruncate`, `fchmod`, `fchown` and `lchown` for the `os` owner.
  - Flag `Path.replace` when the receiver is not a string, or narrow the wording.
  - Flag any assignment of a guarded module to a name.
  - Apply the position-0 mode rule only to `x.open(...)`, not to `io`, `codecs` or `builtins`.

**3. NON-BLOCKING (before publication) — `SHA256SUMS` and the X1P return are still absent.**
- **Location:** `<draft>` L408 ("with hashes in `SHA256SUMS`").
- **Condition:** At HEAD, `<prep>/SHA256SUMS` does not exist, and `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/` has no X1 return.
- **Status:** carried from verdict 03 #7 and verdict 04 #4, whose dispositions defer both to the end of preparation.
- **Remediation direction:** Write both, then recheck L408.

## Verdict-03 dispositions backchecked

1. **Partial.** Implemented as described:
   - all-values anchor check at L430–431;
   - form-anchor sibling check at L435–438, same pin;
   - `equals_folder` derived from the pin path at L439–444;
   - new controls fail as stated.

   Gaps are in finding 1.
2. **Implemented.** Also implemented:
   - mode read from its proper position or `mode=`;
   - non-constant mode flagged;
   - aliased and `from` imports flagged;
   - `os`-owner matching including `popen`, `exec*`, `spawn*` and `rmdir`;
   - `Path` `rmdir`, `symlink_to` and `hardlink_to`;
   - generic names dropped, so `open('data.json')` is no longer flagged.

   Residual gaps are in finding 2.
3. **Implemented.** `<draft>` L134 and question 2.
4. **Implemented and sound.** The SYN-RCP-05 construction now depends on the read path, and its outcome is the explicit limitation (DEL-02-03 REQ-004/AC-004).
5. **Implemented.** The docstring (L16–21) names `runs_section` and `placement_folder` as descriptors. The three `no-runs-section` records are rebound to DEL-02-09 REQ-002/-014, AC-002/-014 and VER-002/-014. The rebinding is apt:
   - REQ-002 declares the dated-heading form;
   - REQ-014 and AC-014 require FC fixtures for it;
   - the `nonconformance: false` label rests on AX-002, which the `BIND` pattern cannot name.
6. **Implemented.** The 2.39.5 `PATH` shim control fails all 5 object-reading tests.
7. **Not yet done.** See finding 3.

## What I checked

- **Reading.**
  - Root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`, the `software-code-review` skill and the X1P brief.
  - Verdicts 01, 03 and 04 with their dispositions.
  - The full draft and the full test module.
  - Both manifests, all 65 expectations and 7 synthetic files in full.
  - The relevant REQ/AC/VER/CON/TBD lines of all three contracts.
- **Hashes (`shasum -a 256`).**
  - Contracts: `c8bb9f1b…294b`, `2319661b…dd26`, `eab18e17…6f5e`, as the draft states; unchanged since `6c6cc1b00`.
  - `apply_x1p.py`: `452ff66a…2428`, as bound.
  - All 35 candidates appear in both the draft table and `apply_x1p.py`.
  - The aid hashes match the draft.
  - `software-workflow.json`: the preimage is `8ec9ba6d…8a8b`, and the diff adds only `v2-parsers` and its path rule.
- **Goldens and tiers.**
  - Counts: 70 source values, 65 expectations (30 `fixed`, 35 `observed`), 442/442 bindings (`verify_x1p_bindings.py`), 19/19 pins (`report_x1p_pins.py`).
  - Spot-checks against `git show`, well over 15 values:
    - FC-1: graph identity at L5 and F1 `ACTIVE` #876 at L35; receipt fields at L39–41 with Gate-Outcome prose at L53–55; DEL-08-01 at L5–9.
    - FC-2 (every anchor): graph identity at L5 and F1 `ACTIVE` #873 at L31; DEL-00-08 L157/159, DEL-10-04 L16–21 and L431/433, DEL-12-01 L211/213, DEL-17-06 L123/125.
    - FC-3: identity at L5, F1 #868 at L27, DEL-05-04 at L5–10.
    - FX-PEC-0: registry profiles and states; marker at L1865; Receipt-197 at L2188–2190; bold identity at L7; DEL-01-06 is an empty template table; DEL-01-03 headings.
  - Merges: #876 `0b276a7f`, #873 `c56ae4a2` and #868 `10b672ca` are 2-parent merges with the right subjects and are ancestors of `d61981ee2`.
  - No TBD or CON is pre-empted. The `fixed` DEL-01-03 run-ID-unavailable expectations rest on AC-004 and CON-004, which say declaring a token position is a scope decision.
- **Synthetic set.**
  - Minimums: DEL-02-08 6/6, DEL-02-09 table form plus 5, DEL-02-03 6/6.
  - The marker prefix sha256 is `936296a7…525d` over 890 bytes, recomputed.
  - My own copy scan against 301 feed-named blobs at both commits, net of the templates: 0 overlaps at 8 words. At 6 words the only overlap is the structural "## Cursor and pointers - **Receipt-ID:**".
- **FX-PEC-0.** A case-insensitive grep of all 35 candidates for `remain|_STATUS|retire` returns nothing. There is no `remaining-loop` source.
- **Test module.**
  - Stdlib only; one `subprocess.run` site; allowlisted read-only Git with `GIT_NO_LAZY_FETCH`.
  - The version, shallow and partial gate runs before the first object read in every test.
  - Failures are raised as assertions and nothing is skipped.
  - I found no false failure on Git 2.54 with a full clone. The `.DS_Store` false failure noted by verdict 03 remains.
  - `TEST_TO_VERIFICATION` is honest given the "fixture-side part only" disclosure (`<draft>` L49, Limits).
- **Runs** (TMPDIR set to my directory; Python 3.13.7; Git 2.54.0):
  - `zsh <prep>/run_fixture_suite.sh <worktree> 6c6cc1b00 <mydir>/parsers -v`:
    ```
    test_tree_expectations_hold_at_their_pinned_commits (...) ... ok
    ----------------------------------------------------------------------
    Ran 10 tests in 2.600s

    OK
    ```
  - `python3 <prep>/negative_controls_x1p.py <worktree> 6c6cc1b00 <prep>`:
    ```
    PASS Git older than 2.44 (PATH shim reporting 2.39.5): exit 1; failing tests [5 object-reading tests]
    PASS partial-clone repository: exit 1; ...
    PASS shallow repository: exit 1; ...
    PASS test missing from the verification map: exit 1; failing tests ['test_loaded_suite_has_exact_verification_mapping']
    RESULT PASS 20/20
    ```

## Residual risk

- Golden meaning, meaning which value belongs to which field or entry, is still verified by review rather than by test (finding 1). I confirmed the current bytes by hand and by script.
- Partial-clone detection reads only `extensions.partialclone`. It still fails closed, but the message becomes `PIN UNREACHABLE`.
- `v2-parsers` fails by design on Git older than 2.44 and on shallow or partial clones, and hosted CI does not run it.
- The `.DS_Store` false failure remains a local risk.
- The dated-heading tiers depend on the CON-004 conservative reading: FC-2's bare heading tokens are `observed`, while PEC's parenthesized tokens are `fixed` as unavailable. A later grammar ruling could require re-tiering.

## Scratch

My directory is `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1r3c.XSgi8P`.
- It holds the candidate copy `parsers/` and my helper scripts `anch.py`, `copy.py`, `mut.py` and `tok.py`.
- I deleted the mutation copies.
- I made no branch operations and no network calls.

---

## Dispositions (WORKING_ITEMS)

Nothing blocks. No candidate byte changes after this verdict, so this verdict covers the final candidates.

1. **Accepted as disclosure.** The draft now says the descriptor checks are guards on grounding, not proofs of meaning. Which value belongs to which field or entry, which node carries which state, the `fixed` registry state and `runs_section` all rest on review; verdicts 01, 03 and 05 checked them by hand. The parser packets' golden tests exercise these associations against output. The negative-control wording is narrowed to "a form anchor moved one line off its entry". The suggested test tightenings (same-entry form siblings, a hyphen boundary, anchors for every expectation, a `runs_section` check) are left for a later fixture revision rather than reopening verified bytes. They are recorded as residuals for the first parser packet.
2. **Accepted as disclosure.** The draft's test-module row now names exactly the calls the guard flags, calls it "a guard, not a proof", and lists the constructs this verdict found unflagged (`Path.replace`, `os.write`, a guarded module assigned to a name) and the latent `io.open` false flag. The module contains none of them.
3. **Done.** `SHA256SUMS` and the X1P return are written at the end of preparation.
