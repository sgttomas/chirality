# X1 preparation verdict 04

Reviewer: fresh read-only `pec-reviewer` TASK (agent `a559ba905d619a872`, Opus 5.5 as reported by the host), round 2 packet review of the repaired draft, backchecking verdicts 01 and 02. Transcribed verbatim by WORKING_ITEMS from the reviewer's hand-back; dispositions are appended by WORKING_ITEMS after the report.

Reviewed head: `caf8af936` (branch `claude/pec-x1-fixtures-proposal`, PR #996).

---

VERDICT: FAIL

One blocking finding: verdict 02's disposition 5 was only partly carried out, so the grant now gives two different times for the add-on L lifecycle write. The repair is one phrase. Everything else I checked holds.

Reviewed HEAD: `caf8af936085a860a08e8b500270a81f3360a8cb` (branch `claude/pec-x1-fixtures-proposal`, PR #996). The worktree was clean before and after, and I wrote nothing in it.
Observation commit: `6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`.
Draft: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md`, SHA-256 `b425c8973e527cda9b5856c7be4d58e5acf1da87f5bbc529e1c747aba791eee2`. Line numbers below are draft lines.

## Findings

**1. BLOCKING — the Administrative grant still runs add-on L after the verifier.**
- **Location:** draft L358 (§Administrative grant, Scope): "add-on L if selected (after the verifier passes)".
- **Condition:** Three other places now run add-on L before the act:
  - the add-on L section (L252 and L256: "immediately before the act script");
  - finite-verification row 1a (L334: "immediately before row 2");
  - owner question 4 ("at actual X1 production start").

  The verifier runs only after the act and the registered checks. So L358 keeps the post-act timing that verdict 02 finding 5 objected to, and its disposition 5 says "Repaired".
- **Impact:** A ruling that selects A + L would adopt two contradictory instructions on when a lifecycle write happens relative to production. The executor could not follow both. Faithfulness to `D-PEC-85` ("when production actually starts") holds in one place and fails in the other.
- **Evidence:** `grep -n 'verifier pass'` on the draft returns only L358. The `apply_x1p.py` template and the dropped `_STATUS.md` pins (12 pinned files, confirmed by regeneration) match the before-act design.
- **Remediation direction:** Change L358 to match L256, for example "add-on L if selected (at actual production start, immediately before the act, after row 1)". Then re-check the neighbouring text (finding 3).

**2. NON-BLOCKING — row 1 lacks the dependency check that add-on L attributes to it.**
- **Location:** L256 says add-on L runs "after the fresh preimage, dependency and `dispatch-for-production` hold checks of finite-verification row 1". Row 1 (L333) lists the ruling and register row, `--check-only`, the `_STATUS.md` preimages and the hold preflights, but no dependency check.
- **Impact:** `D-PEC-85`'s clause requires "fresh source, preimage, dependency and exact-operation hold checks". As written, the dependency check is claimed but not specified.
- **Remediation direction:** Add a row-1 step that re-reads the ACTIVE PREREQUISITE rows L35 and L271 rely on:
  - `DEP-02-0{3,8,9}-003`;
  - the seven reverse rows;
  - no new blocking row on the three targets.

  Name the required result.

**3. NON-BLOCKING — the "During execution" rollback does not account for add-on L running before the act.**
- **Location:** L366: "On exit 1 the tree under `projects/pec` is as before … If a later check fails, discard the branch or worktree."
- **Condition:** Under A + L, the three `_STATUS.md` changes come before the act. The act's rollback does not restore them, so the tree is not "as before". L272 says that after a failed act the deliverables "stay `IN_PROGRESS` with the history line truthful … The run records the failure". Discarding the branch would silently drop that record, and L272 forbids that.
- **Remediation direction:**
  - Say "as before the act".
  - State whether the L commits are kept, and the failure recorded, before any discard.

**4. NON-BLOCKING (fix before publication) — `SHA256SUMS` and the X1P return are still missing.**
- **Location:** L408 ("Artifacts, all in this prep folder with hashes in `SHA256SUMS`"). COMMON's Produce clause requires both files.
- **Condition:** At HEAD there is no `SHA256SUMS` in the prep folder. There is also no X1P return under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`.
- **Status of verdict 02 disposition 1:**
  - The verdict files exist, which makes L24 true.
  - The L149 location fix is done.
  - The disposition commits to writing the other two before publication, and that has not happened yet.
- **Remediation direction:** Write both after the final verdict, then recheck L408.

**5. NON-BLOCKING — the `anchor_line` check is described as stronger than it is.**
- **Location:** L44 ("the grounding test checks every `anchor_line` against its source values") and L149.
- **Condition:** 7 of the 16 anchors belong to form expectations with no `source`:
  - FC-1 DEL-08-01 and DEL-08-05, line 5;
  - FC-2 DEL-00-08 line 157, DEL-10-04 line 16, DEL-12-01 line 211 and DEL-17-06 line 123;
  - FC-3 DEL-05-04, line 5.

  For these, the test's `if values:` branch checks only that the line is in range. I checked all seven by hand and they are correct.
- **Remediation direction:** Either reword to "against its source values where it has any", or have form expectations borrow a sibling expectation's source token.

**6. NON-BLOCKING — the AST claim is broader than the check.**
- **Location:** L55: the test finds no "process-spawning call other than the one `subprocess.run`".
- **Condition:** `WRITE_CALLS` and the subprocess scan in the candidate `test_parser_fixture_integrity.py` do not catch:
  - `os.exec*`, `os.spawn*` and `os.popen`;
  - `import subprocess as sp`.

  The module currently contains none of these, so the claim is overstated, not false.
- **Remediation direction:** Soften the wording, or extend the set.

**7. NON-BLOCKING — the repaired candidates have no candidate-level verdict after verdict 01's FAIL.**
- **Condition:** After verdict 01, the test module (+94 lines), the four goldens and the synthetic manifest all changed. No `MODE=VERIFY` candidate verdict was saved after the repairs. COMMON says to "loop until nothing blocks".
- **What I did:** I backchecked verdict 01's blocking finding and dispositions 2–12 against the current bytes, and all are implemented. Disposition 12 carries the caveat in finding 6.
- **Remediation direction:** Have the packet record which saved verdict clears verdict 01 finding 1. This one, if transcribed, would serve.

**8. NON-BLOCKING — minor accuracy and wording.**
1. Row 1a (L334) says "postimages as the slot rule states". "Slot rule" is not defined in this draft.
2. L266–269 say each `_STATUS.md` changes "in exactly three ways". When `{D}` equals the existing `Last Updated` (2026-09-26, as in the prototype), only two lines change.
3. The DEL-02-03 row of the bindings table (L96) leaves out the REQ-001/-005, AC-001/-005 and VER-001/-005 bindings that FC-1.receipt.generation carries.
4. The precedent for add-on L is the `D-PEC-85` ruling (`67167dc5ec68…`), but the draft hashes only the `D-PEC-85` proposal (`7389826d…7def`). The ruling should be added to the basis table.

**9. Informational — `origin/main` has moved past the observation commit.**
- `origin/main` is now `78e74f590` (the D-PEC-102 ruling, graph, STATUS and register edits).
- None of these changed at `78e74f590`: the 12 act-pinned files, `software-workflow.json`, the three `_STATUS.md` or `ScopeOfWork.md` files, `write_status.sh`, the holds register or script, any PEC `Dependencies.csv`, or `docs/SPEC.md`. The grant would still apply.
- The register still has no D-PEC-104, 105 or 106 row. Every statement in the draft is correctly anchored to `6c6cc1b00`.

## Disposition backcheck

**Verdict 02.**

| Finding | Result |
|---|---|
| 1 | Partly done (finding 4) |
| 2 | Done ("×3 graphs", L94) |
| 3 | Done (L61, L386) |
| 4 | Done; I confirmed all seven reverse rows, INITIALIZED/PENDING |
| 5 | Mostly done; L358 not updated (finding 1) |
| 6 | Done (row 1) |
| 7 | Done (L48 matches `TEST_TO_VERIFICATION` exactly) |
| 8 | Done (L131; `_CONTEXT.md` lines 30/32 and `_REFERENCES.md` line 3 confirmed) |
| 9 | Done (SPEC §3.2 L314, §3.3 L327) |
| 10 | Done |
| 11 | Done (`post-marker-entry-cursor-fields`) |
| 12 | Done (question 2's closing sentence; plain question 3) |
| 13 | Done (verifier present; 66/66) |

**Verdict 01.**

| Finding | Result |
|---|---|
| 1 (blocking) | Repaired: as-cited token semantics in the docstring and L44; Limits L386 |
| 2 | Done; the anchor test and its negative control exist (but see finding 5) |
| 3 | Done: disclosed, and the control renamed |
| 4 | Done: the repository check runs in `blob()` and in the two resolution tests |
| 5 | Done: merge-subject check and negative control |
| 6 | Done |
| 7 | Done: DEL-02-08 REQ-016/AC-016/VER-016 bound on the three FC identity expectations |
| 8 | Done |
| 9 | Done (L111, question 2) |
| 10 | Done (L107) |
| 11 | Done (SYN-RCP-05 and SYN-RCP-07 construction text) |
| 12 | Done, with the caveat in finding 6 |

## What I checked

**Check runner rerun.**
- Command: `zsh <prep>/run_x1p_checks.sh <worktree> 6c6cc1b00 <prep> <mktemp>/out`, with `TMPDIR` set to my mktemp directory.
- Result: exit 0, OVERALL PASS. `SUMMARY.out` is byte-identical to `evidence/run_main/SUMMARY.out`:
  - act: check-only 0, apply 0, rerun refuses 1;
  - containment: 1 modified file and 34 created;
  - six affected checks, and all six registered checks exit 0;
  - `v2-parsers`: 10 tests ok;
  - bindings 433/433; pins 19/19; claims and quotes 66/66;
  - strict registers, harness and receipts identical before and after (strict exit 1, 0 errors, 26 `XRG-013` warnings);
  - hygiene PASS; fault injection 11/11; negative controls 16/16.
- These outputs are also byte-identical to the stored evidence: `verify_claims`, `verify_bindings`, `pins.md`, `negative_controls`, `test_apply_x1p`, `strict_pre` and `apply`.

**Grant table against the act script.**
- I copied the template and candidates into my mktemp directory and ran `build_apply_x1p.py <worktree> 6c6cc1b00 <copy>`. It reported targets=35, creates=34, pinned=12.
- The regenerated `apply_x1p.py` is byte-identical (`cmp`) to the prep copy. Both hash to `ee731005e91adb90cadd62684e01cad7591c8120df27f662ab8c9bd24e213cb4`, which is the bound hash in the draft.
- I parsed the draft's grant table (35 rows, with the `…/synthetic/` prefix expanded) and compared it with `TARGETS` in `apply_x1p.py`: they are exactly equal.
- All 35 postimages recompute (`shasum -a 256` / hashlib) to the tabled values, and the candidate file set equals the table.
- The 12 pinned files in the script equal the draft's list, and all match at `6c6cc1b00`.

**More than 25 claims spot-checked.**
- **All 66 full 64-hex values** in the draft recompute. This covers the preimages, `_STATUS.md`, `ScopeOfWork.md`, `write_status.sh`, the holds register and script, Root and PEC `AGENTS.md`, SPEC, the catalog, the workflows and skill, the profile, the brief `1cefcc48…` and COMMON `51b70e46…`. It also covers all 8 aid hashes, `build_apply_x1p.py` / `apply_x1p.template.py`, and the negative-control files.
- **Abbreviated hashes:** the `D-PEC-94`/`96`/`98`/`99`/`100` records, the exhibit `69b646f8…`, the graph `1ec5719f…` and the register `fe2cc825…` all match.
- **Lineage:** `189f205ff` is an ancestor of the observation commit, and the five decomposition/PRD files are identical at both commits.
- **Merges:**
  - `d61981ee2` is the PR #881 merge.
  - `0b276a7f`, `c56ae4a2` and `10b672ca` are the merges of #876, #873 and #868. All three are two-parent commits and ancestors of `d61981ee2`.
  - PRs #950, #957, #976, #992, #979 and #958 are merged.
- **Lifecycle:** all three deliverables are INITIALIZED at `6c6cc1b00`.
- **Manifest counts:**
  - 2 template pins, 17 source pins, 3 tree records;
  - 65 expectations (30 fixed, 35 observed);
  - 24 cases (21 file-backed; SYN-MEM-05, SYN-RCP-05 and SYN-RCP-06 constructed at test time), 27 synthetic files;
  - 402 JSON bindings plus 31 test-map entries = 433.
- **Golden grounding in the blobs:**
  - FC-1, FC-2 and FC-3: F1 is ACTIVE with PRs #876, #873 and #868, and the identity bullets are at line 5.
  - FC-1 receipt cursor fields and Parent-Receipt "none".
  - Ledger marker at L1865; Receipt-197, `eb56e108…` and Receipt-196 at L2188–2190.
  - `loops.json` states.
  - DEL-01-03 headings at lines 3, 16, 82 and 109.
  - All 8 memory anchor lines.
- **Registers and records:**
  - The three DEL-01-01 PREREQUISITE rows and the seven reverse rows are ACTIVE, INITIALIZED, PENDING.
  - No `Dependencies.csv` cites `software-workflow.json` or `v2/tests`.
  - At `6c6cc1b00` PEC has 2 graphs, 1 central receipt and 2 `MEMORY.md` files.
  - The catalog lists `software-bounded-implementation` under `historicalOnly`.
  - Part B (12 items) routes only to S1, S2 and S4.
  - The R-05 quote is at Impact_Assessment L451 under §8.4.
  - Q5 (a) appears in the Decision_Log as "SELECTED VIA CP1-B".
  - `D-PEC-85` ruling L46–50 matches the quoted clause.
  - The DEL-02-03 TBD-006, DEL-02-08 TBD-006 and DEL-02-09 TBD-007 wording is as the draft states, as is DEL-02-03 CON-007, DEL-02-08 CON-004 and DEL-02-09 CLM-013 ("takes no FX-PEC-0 output").
  - The workflow diff adds only the `v2-parsers` check and its path rule.
- **Reliance preflight:** the evidence file shows 41 ALLOW. I reran the preflight on an export for `exact-correction-preparation`, `dispatch-for-production` and `rely-for-production` on sample targets: ALLOW, exit 0. The holds register has a header and no rows.
- **Add-on L prototype:** reproduced on an export: `35ba885f…34b7`, `012e905d…ce60`, `ffe81899…edb8`, exit 0 ×3.

**Composite A + L (my own extra check).** On a full export I ran add-on L's three commands, then `apply_x1p.py`:
- the act passed (35/35, write set = grant, pinned 12/12);
- strict register output is byte-identical to before;
- harness exit 0, receipts VALID;
- `v2-parsers` OK.

So the add-on L restructure works mechanically with the act script, the finite verification and the limits. The inconsistencies are textual (findings 1–3).

**Scope and conduct (item 6).**
- Status is AWAITING_RULING, and no ruling is recorded that did not occur.
- The only CHECKING mentions are in Limits and in add-on L's "implies no … CHECKING". Nothing asks the owner about CHECKING.
- `MODE=REVISE` appears only in a one-line disclosure (L25).
- Owner questions 1–6 are plain. Question 4 leaves the decision to the owner and assumes nothing.
- There is no parser code, and the smallest-honest-scope argument is present.
- No candidate contains "remaining".
- The branch diff against `6c6cc1b00` touches only the prep folder and the brief copy.

## Residual risk
- The fixed/observed tiers are judgement calls. The FX-PEC-0 DEL-01-03 headings that carry parenthesized run-record IDs are `fixed` as run-ID-unavailable. That rests on DEL-02-09 CON-004's conservative reading, and a later grammar decision could require a new owner-ruled packet.
- No test simulates a pre-act `_STATUS.md` change inside the fault-injection suite. My composite run covers the happy path only.
- The `v2-parsers` check fails by design on shallow and partial clones, and hosted CI does not run it (disclosed).
- An old Git (below 2.44) was not simulated.

## Scratch
mktemp directory: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1r2p.z04fdd`
- `run.log` and `out/`: the check-runner rerun;
- `regen/`: the regenerated act script;
- `lexp/`, `hexp/`, `fullL/`: the exports for the add-on L prototype, the preflight and the composite A + L run.

---

## Dispositions (WORKING_ITEMS)

1. **BLOCKING — repaired.** The administrative grant now reads "add-on L if selected (at actual production start: after row 1, immediately before the act)", matching the add-on L section, row 1a and question 4.
2. **Repaired.** Row 1 now includes a fresh dependency read with a named required result: `DEP-02-0{3,8,9}-003` and the seven reverse rows as tabled (ACTIVE, `PENDING`), and no other ACTIVE `PREREQUISITE` row whose target the work needs at `TBD`, `PENDING` or `IN_PROGRESS`.
3. **Repaired.** "During execution" now says "as it was before the act". Under A + L, the three `_STATUS.md` changes are committed before the act and kept if it fails; the failure is recorded in the run root, graph and receipt, and a walk-back happens only on owner direction. Only under A alone is a discard enough.
4. **Repaired before publication.** `SHA256SUMS` and the X1P return are written at the end of preparation.
5. **Repaired.** As verdict 03, finding 1: the test is strengthened and the wording made exact.
6. **Repaired.** As verdict 03, finding 2.
7. **Recorded.** The draft's new "Preparation verdicts" table records that verdict 03 (candidates, round 2) confirms verdict 01's blocking finding repaired. A round-3 candidate verdict covers the round-2 repairs.
8. **Repaired.**
   1. "Slot rule" is replaced.
   2. The postimages now change "in at most three ways" (`Last Updated` is unchanged when `{D}` equals it).
   3. The DEL-02-03 bindings row now includes REQ-001/-005, AC-001/-005 and VER-001/-005.
   4. The `D-PEC-85` ruling (`67167dc5…4851`) is cited under Precedents and in the basis table.
9. **Recorded.** A "Currency after the observation commit" bullet names `origin/main` `c26677c8a` and states that no target, pin, `_STATUS.md`, contract, tool or holds file changed. HELP_HUMAN re-verifies at publication.

After the repairs: candidate suite 10/10; negative controls 20/20; `verify_x1p_claims.py` 67/67; `run_x1p_checks.sh` OVERALL PASS at `6c6cc1b00`.
