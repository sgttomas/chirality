# X1 preparation verdict 02

Reviewer: fresh read-only `pec-reviewer` TASK (agent `ade16bb9aa728f67d`, Opus 5.5 as reported by the host), packet review of the draft proposal and prep folder. Transcribed verbatim by WORKING_ITEMS from the reviewer's hand-back; dispositions are appended by WORKING_ITEMS after the report.

Reviewed head: `98af674e8` (branch `claude/pec-x1-fixtures-proposal`, PR #996).

---

VERDICT: PASS WITH NOTES

Scope: I reviewed the packet for work-graph node X1 (provisional D-PEC-106), read-only, on branch `claude/pec-x1-fixtures-proposal` (PR #996). The branch head is `98af674e8`; the observation commit is `6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`. The draft is `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md`, SHA-256 `ff4dced25f0e033b33a087909ee3226b2d57e0486350c2721709f1e243d1607b`. All line numbers below are draft lines unless stated. The worktree was clean before and after the review.

The grant, act script, candidates, checks, lifecycle handling and limits all hold up. Nothing blocks. The findings below are wording and completeness repairs.

## Findings (all NON-BLOCKING)

1. **The evidence section claims files that do not exist yet** (pre-publication must-fix).
   - Location: L24 ("verdicts in this folder"), L146 ("drafter return, saved with the verdicts"), L394–401 ("hashes in `SHA256SUMS`" and `VERIFIER_VERDICT_NN.md`).
   - Condition: at head `98af674e8` the prep folder has no `SHA256SUMS`, no verdict files, and no X1P return under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`. The drafter returns are in `evidence/drafter_returns/`, not beside any verdicts.
   - Impact: the packet describes evidence that is not there. COMMON.md requires `SHA256SUMS` (tracked files only).
   - Remediation: before publication, write `SHA256SUMS` and the verdicts, and correct the L146 location.

2. **"F1 `ACTIVE` ×4 graphs" is false.**
   - Location: L92, DEL-02-08 row of the bindings table.
   - Condition: only FC-1, FC-2 and FC-3 carry a terminal-node-state expectation. PEC's graph (blob `bf0b0c626`, line 77) declares F1 `PLANNED`, and the FX-PEC-0 golden has no terminal-node expectation.
   - Remediation: change to "×3 graphs (FC-1, FC-2, FC-3)".

3. **DEL-02-08 TBD-006 does not assign the golden format or threshold to this packet.**
   - Location: L59 ("The contracts leave … to this packet") and Limits L376 ("that DEL-02-08 TBD-006, DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign to this packet").
   - Evidence: DEL-02-03 TBD-006 ("…under their own packet (graph node X1)") and DEL-02-09 TBD-007 ("…under their own packet") do assign it. DEL-02-08 TBD-006 says only "fixed by no accepted source; the design note … calls it 'a small length threshold'".
   - Impact: the exception in the Limits misstates what one contract says. Question 3 still lets the owner settle the matter.
   - Remediation: say that this packet proposes to settle DEL-02-08 TBD-006 for the fixture suites, subject to question 3, rather than that the contract assigns it.

4. **Add-on L's dependency account is inaccurate and incomplete.**
   - Location: L264.
   - Condition: `DEP-03-01-010/-015/-016` and `DEP-04-05-003` have `RequiredMaturity` `INITIALIZED` but `SatisfactionStatus` `PENDING`, so "remain satisfied" is wrong.
   - Also omitted: `DEP-10-13-009`, `-013` and `-014`. These are ACTIVE PREREQUISITE rows on DEL-02-03, DEL-02-08 and DEL-02-09 at `INITIALIZED`, present at `6c6cc1b00` after the D-PEC-103 act.
   - Remediation: say that `IN_PROGRESS` meets the `INITIALIZED` maturity these rows require, that their `SatisfactionStatus` is not written, and list all seven rows.

5. **Add-on L's timing contradicts its own label and its precedent.**
   - Location: L252 ("At actual production start of X1 — after the act has run, the registered checks have passed and the verifier has passed") and L388.
   - Condition: the D-PEC-85 ruling (L46–60) makes the transition happen "when production actually starts, after fresh source, preimage, dependency and exact-operation hold checks". There, the history records the semantic-step skip, the merged ruling and the activation evidence. Here the transition comes after production is finished, and the history line records only the actor.
   - Remediation: either move the transition before the act (and adjust the `_STATUS.md` pins), or call it a post-act record and stop citing D-PEC-85 as the precedent. Consider carrying D-PEC-85's history content.

6. **The reliance preflight does not cover add-on targets.**
   - Location: Finite verification row 1 (L324): `dispatch-for-production` and `rely-for-production` run "on each of the 35 targets" only.
   - Condition: if L or M is selected, the three `_STATUS.md` and three `MEMORY.md` files are also written, and `projects/pec/AGENTS.md` §"Active Reliance Holds" needs a preflight for each exact target and act.
   - Remediation: add the L and M targets to row 1, conditional on selection.

7. **The VER coverage account is narrower than the test map.**
   - Location: L46 names only DEL-02-03 VER-017, DEL-02-08 VER-016/017 and DEL-02-09 VER-014.
   - Condition: `TEST_TO_VERIFICATION` in the candidate test module also maps DEL-02-03 VER-016 (the tree test) and the test-run mapping VERs DEL-02-03 VER-013, DEL-02-08 VER-020 and DEL-02-09 VER-016. Limits L371 defers to that map, so the two passages disagree.
   - Remediation: list every mapped VER at L46 as partially implemented on the fixture side only.

8. **Contract-wording item 4 is restated as a different issue.**
   - Location: L128.
   - Condition: the graph's carried item (WORK_GRAPH L133 at `6c6cc1b00`) says the sentence "`_CONTEXT.md` and `_REFERENCES.md` name revision 1.5 and PRD v2.3" is true of the two file types together, not of each one. The draft instead restates it as a currency point ("since `D-PEC-101` both name revision 1.6"). At `6c6cc1b00`, `_CONTEXT.md` names both 1.5 (line 30) and 1.6 (line 32); `_REFERENCES.md` names 1.6.
   - The conclusion (no bearing on the fixtures) holds.
   - Remediation: quote the carried item faithfully.

9. **One SPEC citation names the wrong section.**
   - Location: L34.
   - Condition: "Human or WORKING_ITEMS begins work" is in Root `docs/SPEC.md` §3.2 (line 314), not §3.3. The transition row "(when semantic step is skipped)" is correctly §3.3 (line 327).

10. **The threshold wording does not match the contracts.**
    - Location: L62 and question 3.
    - Condition: the contracts say "no run of source text above the threshold". The packet defines `source_run_words = 3` as "three or more", which is at-or-above.
    - Remediation: state the reading explicitly, or set the constant to match "above".

11. **Two statements about the marker are in tension.**
    - L44 lists "which ledger entries the marker governs" as grammar-dependent and left out.
    - The FX-PEC-0 golden has `FX-PEC-0.ledger.marker-governed-entry` (fact `marker-governed-entry-fields`, Receipt-197). It is tiered `observed`, which tolerates "unavailable", but the id asserts that the marker governs Receipt-197.
    - Remediation: rename the fact to something neutral, or add a sentence saying the `observed` tier leaves governance open.

12. **The owner questions need plainer wording.**
    - Question 2 ends "Without an answer, the tabled bytes apply", which reads as silence counting as consent. Better: "Selecting A adopts this FX-PEC-0; to drop it, choose Amend."
    - Question 3 is written in jargon ("contract-fixed and observed facts", "net of shared-template text"). A one-line plain gloss of each threshold would help.
    - Questions 1, 4, 5 and 6 are clear. Question 4 correctly leaves the decision to the owner and assumes nothing.

13. **Informational: no mechanical quote or state-claim verifier ran over the draft.** COMMON.md cites that verifier pattern from the precedents. I checked the load-bearing quotes by hand and all are verbatim at `6c6cc1b00`:
    - R-05 at Impact_Assessment L451 (§8.4);
    - §B7 at Propagation_Plan L884;
    - the fence sentence in `projects/pec/AGENTS.md`;
    - the D-PEC-94 steering sentence;
    - the X1 graph row;
    - "under a later v2 packet" in all three contracts;
    - the DEL-02-03 CON-007 and TBD-006 phrases;
    - the owner's "no need to scan for them" (D-PEC-96_AMEND_DIRECTION L14).

## What I checked

**Check runner rerun.**
- Command: `zsh run_x1p_checks.sh <worktree> 6c6cc1b00 <prep> <mktemp>/out`
- Exit 0, OVERALL PASS. It matches `evidence/run_main/SUMMARY.out` line for line:
  - act: check-only 0, apply 0, rerun refuses 1;
  - containment: `software-workflow.json` modified plus 34 new files, nothing else;
  - affected checks: the six named; all six registered checks exit 0;
  - `v2-parsers`: 10 tests ok;
  - bindings 424/424; pins 19/19;
  - strict registers, harness and receipts identical before and after (strict exit 1 with 0 errors and 26 `XRG-013` warnings, confirmed);
  - candidate hygiene PASS;
  - fault injection 11/11; negative controls 14/14 (13 mutations plus the unmutated suite).

**Grant, act script and candidates.**
- All 35 postimage hashes in the grant table equal `shasum -a 256` of `candidates/`, checked mechanically.
- All 35 appear in `apply_x1p.py`.
- `apply_x1p.py` hashes to `815957272cf3…fe0e`. It regenerates byte-identically from `build_apply_x1p.py` and the template at `6c6cc1b00` (35 targets, 34 creates, 15 pinned).
- The one preimage, `software-workflow.json` `8ec9ba6d…8a8b`, matches `6c6cc1b00`.
- All 15 pinned read-only files match `6c6cc1b00`, including `service_core_posture.json` `20d64ff3…` and `check_service_core_posture.py` `03be20a5…`.
- The failure semantics in the draft match the code: preflight refusals, temp-write-and-rename, rollback order (the modify is written first and restored), a `projects/pec` inventory that leaves out the run root, exit 2 for an incomplete rollback, and the run-root guard. The fault tests cover what the draft says they cover.
- The workflow diff adds only the `v2-parsers` check and its path rule.
- The posture `core_tree_sha256` is unchanged; `workflow_sha256` moves to `d55fff77…`.
- `validate_instruction_entrypoints.py` gives identical PASS output before and after the workflow change (my own extra check).

**Aid and basis hashes.** Every aid hash in the draft matches, as do the brief `1cefcc48…` and COMMON `51b70e46…`. These also match at `6c6cc1b00`:
- `projects/pec/AGENTS.md`, Root `AGENTS.md`, `AGENT_WORKING_ITEMS.md`, `SPEC.md`, the catalog and three workflow or skill files, the software workflow profile;
- the reliance-hold register and script, `write_status.sh`, `_LATEST.md` (revision 1.6, `current_basis`), `ContextBudgetQA.csv`;
- `_REGISTER.md`, the work graph `1ec5719f…`;
- the SCA-005 plan, impact assessment and design note;
- the D-PEC-85, 87, 89, 91, 94, 96 (three files), 98, 99 (with exhibit) and 100 records;
- the three `ScopeOfWork.md` and three `_STATUS.md` files.

**State and count claims.**
- `189f205ff` is an ancestor of `6c6cc1b00`, and the five decomposition/PRD files are identical at both commits.
- All three deliverables are `INITIALIZED`. No `MEMORY.md` exists for them. The register has no D-PEC-104, 105 or 106 row.
- Ruling states D-PEC-96, 98, 99 and 100 are as described. PRs #950, #957, #976 and #992 are merged.
- `d61981ee2` is the PR #881 merge. `0b276a7f`, `c56ae4a2` and `10b672ca` are merges of #876, #873 and #868 and are ancestors of it.
- Manifest counts: 2 template pins, 17 pins, 3 trees, 65 expectations (30 fixed, 35 observed), 24 cases (21 file-backed; SYN-MEM-05, SYN-RCP-05 and SYN-RCP-06 constructed at test time), 27 synthetic files.
- Binding count: 393 JSON bindings plus 31 test-map entries = 424.
- Spot-checked golden anchor lines against their blobs: DEL-10-04 lines 16 and 431, DEL-00-08 line 157, DEL-12-01 line 211, DEL-17-06 line 123, line 5 of the three bullet-form MEMORY files, DEL-01-03 headings, and Receipt-197 fields plus the marker in the ledger.
- The registry row matches the draft. At `6c6cc1b00` PEC has two graphs, one central receipt and two `MEMORY.md` files.
- The Part B routing (12 items, to S1, S2 and S4 only) is confirmed; no item names X1.
- No `Dependencies.csv` cites `software-workflow.json` or `v2/tests`.
- The three DEL-01-01 PREREQUISITE rows are ACTIVE and `PENDING`.
- The hosted CI claims (a sparse, blob-filtered, shallow `pec` job running `npm test`) are confirmed.
- The reliance preflight shows `ALLOW` 41 of 41 under `exact-correction-preparation`.
- Running the add-on L prototype on a scratch export reproduces `935f8885…`, `17d60ae2…` and `24a20b34…`, exit 0 each.

**Rulings and scope.**
- No human ruling is claimed that did not occur; every ruling cited is on `6c6cc1b00`.
- Nothing asks the owner about CHECKING. CHECKING and ISSUED appear only in the limits.
- `MODE=REVISE` appears only as a one-line disclosure and is not put to the owner.
- There is no parser code. The smallest honest scope is argued (the fixed/observed tiers).
- The FX-PEC-0 redefinition does not name `remaining-items` or `remaining-loop` in any candidate; the hygiene check found the word absent.

## Residual risk
- The `observed` and `fixed` tier assignments and the synthetic `expect` labels are judgement calls. Most `fixed` items trace to contract text (AC-004, AC-005, AC-006, AC-008 "unresolved locally", AC-017), but a parser packet may later need a new owner-ruled packet to adjust fenced fixture files.
- FX-PEC-0 pins blobs whose prose mentions the retired sections (49 mentions in the ledger, 13 in the graph, 7 in DEL-01-03 `MEMORY.md`, none as headings). This is disclosed and nothing scans for them, but the owner should know when ruling question 2.
- The `v2-parsers` check fails on shallow or partial clones by design, and hosted CI does not run it.
- I did not re-dispatch `MODE=VERIFY` on individual candidates.

## Scratch
- My mktemp directory: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1prev.OCXIQb`
- The rerun outputs are in `out/` there, with its summary in `run.log`.

---

## Dispositions (WORKING_ITEMS)

1. **Repaired.** `SHA256SUMS`, the verdict files and the return are written before publication. The drafter-return location now reads `evidence/drafter_returns/PINNED_DRAFTER_RETURN.md`.
2. **Repaired.** The count now reads "×3 graphs: FC-1, FC-2, FC-3".
3. **Repaired.** The threshold paragraph and the Limits section now say that DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign these items to this packet, and that for DEL-02-08 TBD-006 the packet proposes the same settlement, subject to question 3.
4. **Repaired.** All seven rows are listed (`DEP-03-01-010/-015/-016`, `DEP-04-05-003`, `DEP-10-13-009/-013/-014`). The text now says `IN_PROGRESS` meets their `INITIALIZED` maturity and that no `SatisfactionStatus` is written.
5. **Repaired.** Add-on L now runs at actual production start: after the fresh preimage, dependency and `dispatch-for-production` checks, and immediately before the act script, as in `D-PEC-85`. Its history line carries the semantic-step skip, the ruling and the evidence location. The act script no longer pins the three `_STATUS.md` (it has 12 pins, not 15). Finite-verification rows 1, 1a and 7 check them instead. The act was rebuilt as `ee731005…3cb4`, and the prototype postimages were recomputed.
6. **Repaired.** Row 1 now covers add-on L's and add-on M's targets where selected.
7. **Repaired.** As verdict 01, finding 6.
8. **Repaired.** The carried item is quoted faithfully, with the state at `6c6cc1b00` stated separately.
9. **Repaired.** "Begins work" is cited to SPEC §3.2 and the transition row to §3.3.
10. **Repaired.** The thresholds are stated as "two words; three or more is above" and "seven words; eight or more is above", with plain glosses.
11. **Repaired.** As verdict 01, finding 8.
12. **Repaired.** Question 2 now ends "Selecting A adopts this FX-PEC-0; to drop it, choose Amend". Question 3 is rewritten in plain terms.
13. **Repaired.** New `verify_x1p_claims.py` runs in the check runner. It makes a two-sided check of all 57 abbreviated hash claims in the draft, and fails on any abbreviation that is not claimed. It also checks 13 load-bearing quotations, both sides. Its first run caught three mistyped hash abbreviations (the catalog, the design note and `software-test-planning`), which are now corrected. The current result is `RESULT PASS 66/66`.
