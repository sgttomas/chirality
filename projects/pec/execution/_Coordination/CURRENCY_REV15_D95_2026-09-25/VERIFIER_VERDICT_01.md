# VERIFIER_VERDICT_01 — D-PEC-95 P + R currency act (PR #924)

- **Verifier role:** TASK (Type 2). Fresh, read-only, independent verifier. I authored nothing in this change, delegated nothing, and made no edit, stage, commit or push in any checkout.
- **Model:** the host reports Opus 5.5 (`claude-opus-5-5`). The `high` reasoning effort is what the brief asserts; the host does not report it.
- **Reviewed candidate:** PR #924, branch `claude/pec-d95-currency-act`, head `fb030850bb8530c5da3cf083e32610d7b2219d7f`.
  - Act commit: `fdc7a207147c83443f20088b2281cf4da1a298ec`.
  - Base: `origin/main` `590ec52c15f86d812ce3c5d4919b475fe9cf3985`, fetched and equal to the merge base.
  - `gh pr view 924` reports the same head, state OPEN, and all required CI checks SUCCESS or SKIPPED.
- **Date and time:** 2026-09-25, 20:45–20:58 MDT (America/Edmonton).
- **Interpreter:** Python 3.13.7 (`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`).
- **Checkout:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a471961b37f906dd4` (read only). `git status --short` was empty at the end.
- **Scratch:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/u1_verifier/` (referred to as `<SC>` below).

## Authority relied on (SHA-256, recomputed with `shasum -a 256`)

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `_DECISIONS/D-PEC-95_RULING_2026-09-25.md` (the checkout and the `590ec52c1` export give the same bytes) | `51dceb7136c24c1dea2f68c2338f66781de17fb2b63a8caf8bc719dd5a4e2beb` (as expected) |
| `_DECISIONS/D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md` (the checkout and `590ec52c1` give the same bytes) | `9137d3872329cea5093f61fb6c4150121e4ffcc2abe900ca88e7339049064b22` (as expected) |
| `_DECISIONS/_REGISTER.md` (identical at `590ec52c1` and the candidate; row D-PEC-95 at line 112 reads `RULED P + R / EFFECTIVE ON MERGE`) | `50e9ea65b904cc6a6154173af092018db232b4584eaa7791704a3bb59c847211` |
| `workflows/task-management/WORKFLOW.md` / `resources/contract.md` / `resources/method.md` | `db06263d41f2a17e12b965a337dd6ba0baf3bd21c71ed6e5dc0de7997e101e9b` / `e1c97a76b8a411873ca86a6ef4351a7f76303e74331a52307a3705a83827c837` / `7f9e0d5ea7c2b74e7148faf3d2a35efc6ddd0552efd4b577a1c56895f75fe2f8` |
| Root `docs/CONTRACT.md` (K-TM-3) | `64747d2a3c58ae93194bd5c7118d89a591b7b4ebe8cec7e88cb6a95dc55895bd` |
| Bound `gen_d95.py` (run root = preparation folder) | `0e9ede5044b34cc4594836aab73a0a8df02cd4d1de8ae5e1e5625ebb232ebe78` |
| Bound `verify_d95.py` (run root = preparation folder) | `fcf172b5aa2ec6179a5af541f1a01d68a0148590d3b3f6eafbf913e64bfb185f` |
| Bound `t1_tm_pec_023.py` (run root = preparation folder) | `0e0cd6f94448005ecf17f564f35ef72a42f2c2862e97bc33256a3c701b957bec` |
| Preparation `evidence/genP.tsv` / `evidence/genAR.tsv` | `01cd43493a6bb9e138f44ec193c00252dab5c4848cd497e10ec64ea571600c94` / `bb8547f684fc30cd418728063cac6b6ff68e2e37bfb8b1870c52b8e2c9e70dab` |
| `tools/taskmgmt/taskmgmt.py` | `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101` |
| `ACTIVE_RELIANCE_HOLDS.csv` (header only) / `pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| Precedent: D-PEC-93 `closure/closure_summary.json` | `bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a` |

Export tarballs made with `git archive`:
- `base.tar` (`13df8b795`): `ee38659a3b52fdf580121d48c6ab1ad54cab333bca3e596031b269b3eb8cc6ee`.
- `main590.tar` (`590ec52c1`): `152aba22aee83d9b0a76c7265d533f523a0373f43b6e6cda9ac7033ef75a4024`. This equals the `<pre>` tar hash the run records.
- `cand.tar` (`fb030850b`): `60638d9b41c442ee8a3ac8b0fd3443841f03a605ba2b6e5a5bbcbc42f6b4c525`.

## Reproduction (item 2)

**Method.** The local date was still 2026-09-25, so I ran without `--reproduction`.
- I made a fresh `git archive` export of `13df8b795e47ab2284018eeefc9d5473d00c232d` into `<SC>/repro`.
- I copied the bound generator (`0e9ede50…be78`) from the candidate's run root to `<SC>/gen_d95_bound.py`.
- At 20:47 MDT I ran `PYTHONDONTWRITEBYTECODE=1 python3 <SC>/gen_d95_bound.py --repo <SC>/repro --act-date 2026-09-25 --option P --retired-covers`.

**Result.**
- Exit 0 with empty stderr.
- The report has 246 lines: 124 READ, 119 WRITE, 1 CHECK (`active_execution_quotes_verbatim 111 111`), 1 AGGREGATE (`option=P+R files=119`, pre `b8ce2679…e7ed`, post `aab21097…8361`) and 1 PATHLIST (`ebac38d0…dd03`).
- The report is **byte-identical** to the candidate's `gen_d95_report.tsv`.
- All **119/119** written files are byte-identical to the candidate. Each of the 119 differs from its `13df8b795` preimage.
- Across `projects/pec`, every other difference between the reproduction and the candidate is a commit between `13df8b795` and `590ec52c1` or a run-root file. None is a target path.

## Results by item

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Basis | PASS | <ul><li>The ruling (`51dceb71…4beb`) and register row D-PEC-95 (`RULED P + R / EFFECTIVE ON MERGE`) are present in the `590ec52c1` export, and `590ec52c1` is fetched `origin/main`.</li><li>The run-root `gen_d95.py`, `verify_d95.py` and `t1_tm_pec_023.py` hash to the pinned values, and `cmp` finds them identical to the preparation copies.</li><li>The 124 READ pins (119 targets, 3 basis files and 2 SCA-005 files) pass `shasum -c` at both `13df8b795` and `590ec52c1`.</li><li>The T1 preimages are `REGISTER.csv` `d350d007…799d` and `REGISTER_CLOSED.csv` `ea730ae0…afd94` at both commits.</li><li>The act report's READ lines are identical to `genP.tsv`'s.</li><li>PR #919 (merge `7562c4434`) is an ancestor of `590ec52c1`, and the work graph there hashes `f32ab9d2…3802`, as recorded.</li></ul> |
| 2 | Reproduction | PASS | As described above: fresh export, act-date run without `--reproduction`, 119/119 files and the report byte-identical. |
| 3 | Fixed checks | PASS (same results as recorded) | <ul><li>**`verify_d95.py`**, run against `<SC>/main590` and against `<SC>/base`: exit 0 both times. 11/11 PASS, and the output is byte-identical to `checks/verify_d95.out`.</li><li>**Strict registers:** exit 0; 66 registers, 263 rows (ANCHOR 140 / EXECUTION 123), 0 errors / 0 warnings. Output byte-identical to `checks/post_strict.out`, which equals `pre_strict.out`.</li><li>**Closure** (output directory in scratch): exit 0. `closure_summary.json` is `bd73806c…187a`, the same as `closure_pre`, `closure_post` and D-PEC-93's: 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs, 0 orphans, 6 isolated, `subject_status` PASS. Stdout is identical to `closure_post.out`.</li><li>**Schema:** VALID ×10, exit 0 each.</li><li>**Receipts:** exit 0 ("frozen through Receipt-166; versioned receipt contract satisfied"); identical to `post_receipts.out`, which equals `pre_receipts.out`.</li><li>**Harness self-check:** exit 0; identical to `post_harness.out`, which equals `pre_harness.out`.</li><li>**`taskmgmt validate`:** PASS on `REGISTER.csv` (9 rows) and `REGISTER_CLOSED.csv` (16 rows); identical to `t1_06_*`.</li><li>**Byte identity:** 115 postimages equal `genP.tsv` and the 4 retired `_REFERENCES.md` equal `genAR.tsv`. Every checkout file's hash equals its report postimage (119/119), and the MANIFEST table equals the report's WRITE rows (119 rows).</li><li>**Containment:** see item 5.</li><li>**`git diff --check`:** outside the run root, exit 0 with no output. On the whole diff, exit 2 with exactly 291 `trailing whitespace` notices, all in raw run-root tool outputs: 82 + 82 in `checks/closure_{pre,post}/*.csv` (CR-at-EOL), 125 in `gen_d95_report.tsv` (124 READ lines and 1 PATHLIST line with an empty trailing field) and 2 in `checks/verify_d95.out`.<br>The disclosure in `VALIDATION.md` and `checks/diff_check.out` is accurate. It is acceptable: it follows the D-PEC-93 treatment, which verdicts 01/02 accepted (109 notices, same class), and `.gitattributes` line 6 says cosmetic whitespace does not gate CI. The files are hashed or rerun-comparable evidence and should not be normalized.</li><li>**Reliance-hold preflight** (the review entry-path duty in `projects/pec/AGENTS.md`), `candidate-validation` on the 121 targets: 121/121 `ALLOW`, exit 0. The register has a header and no rows. The recorded `dispatch-for-production` and `rely-for-production` files each show 121/121 `ALLOW`.</li></ul> |
| 4 | Semantics | PASS (DEP-10-05-004 recorded, not failed) | <ul><li>**N3.** Exactly 19 rows changed, in `EvidenceQuote`, `LastSeen` (2026-07-25 → 2026-09-25) and `Notes` only. The `Notes` prefix is "Evidence refreshed under D-PEC-95 (…); " with the old Notes kept verbatim after it. `DependencyID`, row order, `EvidenceFile` and `SourceRef` are unchanged.<br>I checked each new quote independently against its locus cell (the named `Deliverables.csv` column, `ScopeLedger.csv` row, or the PRD PEC-RCN-002 / PEC-API-002 row); all 19 are inside it. Each supports its row's `Statement` and target at least as well as the old quote, except DEP-10-05-004 (see its note below). The PEC-RCN-002 fragments name the specific ingested feed rather than a growing prefix, and the other rows keep the target-relevant phrase: "schema every derivation package depends on", "session records", "orientation reads … ≤100 ms", "heartbeat/scan age", "advisory overlap warnings", "orientation and dashboard surfaces", "into DependencyEdge", the SOW-004 statement.</li><li>**N1.** Every statement matches `origin/main` `590ec52c1`, or is the act's own effect:<ul><li>The audit pointer names `COV_SCA005_POSTSETUP_2026-09-25_1606`: `WARNINGS`, 0/3/70, with the 3 warnings `[PRE-EXISTING]` v2 artifacts held outside their folders (COV-004/006/042).</li><li>COV-068/069/072/073 are INFO, with the meanings the text gives.</li><li>The D-PEC-93 closeout path exists, and the D-PEC-93 row effects (20 retired, 1 refreshed, 8 added) support "retired, refreshed and added".</li><li>`projects/pec/AGENTS.md` named PRD v2.2 and D-GOV-20 before `11be80113` (the D-PEC-94 adoption) and names v2.3 and D-GOV-43 after it.</li><li>The open items (SOW currency, derivative review, registry packet, fixtures, D-PEC-90 amendment) match work-graph nodes S1–S4, D1, G1, X1 and R1–R4 at `590ec52c1`.</li><li>Propagation_Plan §B2 is disposed by A6, so "B4–B7 open" is complete.</li><li>Item 14's hashes equal the unchanged SCA-005 files.</li><li>Items 12 and 13 do state revision 1.4, TM-PEC-023 held, and two derivative categories.</li><li>The Notes line is included, as ruled ("include").</li></ul></li><li>**N2.** A line-level diff of all 106 files against `590ec52c1` shows only:<ul><li>42 context anchor replacements;</li><li>64 `SOFTWARE_DECOMP.md` bullet replacements (1.4 → 1.5);</li><li>64 PRD bullet replacements (v2.2 → v2.3);</li><li>4 "covers" bullet rewrites, in exactly DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05. `ScopeLedger.csv` shows SOW-029, SOW-035, SOW-037 and SOW-087 `OUT` (Deferred), and `Deliverables.csv` shows the four deliverables `[RETIRED — SCA-005]`.</li></ul>No other byte changed.</li><li>**Lifecycle.** No `_STATUS.md` changed (item 5).</li><li>**T1.** Replaying the pinned `t1_tm_pec_023.py` on a fresh `590ec52c1` tree gives `d350d007…` → `62f897ab…`. `taskmgmt archive` on that scratch register then gives `634641f0…` and `3c1349ba…`, byte-identical to the candidate.<ul><li>The changed cells are exactly Status, Disposition, EvidenceRef, EvidenceSha, EvidenceQuote, LastReviewed, Closed and Notes, with the old Notes kept as the prefix.</li><li>The live register is the pre register minus that one row (10 → 9 rows), and the archive is the pre archive plus that one row appended (15 → 16). The relocation is mechanical.</li><li>The EvidenceQuote occurs verbatim in `Propagation_Plan.md`.</li><li>The note's row mapping is true: rows 1, 2, 3, 5, 8 and 9 (DEL-00-02, 03-05, 05-01, 07-03, 08-05, 10-08) now carry objectives, and rows 4, 6 and 7 (DEL-07-02, 07-04, 07-05) are RETIRED with blank cells.</li><li>"(question 2)" is true under the ruling's mapping, which states it explicitly: proposal question 2 = presentation question 3 = "confirm TM-PEC-023".</li></ul></li></ul> |
| 5 | Containment | PASS | <ul><li>A whole-repository tree comparison of the `590ec52c1` and `fb030850b` exports gives 121 modified, 63 added and 0 removed files.</li><li>The modified files are the 119 granted paths (no granted path left unchanged) and the 2 Task Management registers. All 63 added files are under the run root.</li><li>Nothing changed under `_Decomposition/` except `_LATEST.md`, and nothing changed in `docs/PRD.md`, any `ScopeOfWork.md`, any `_STATUS.md`, `v2/**`, `checkpoint_snapshots/**`, the SCA-005 snapshot (including `Handoff_State.md` `a86ae910…328a` and `RUN_SUMMARY.md` `e9a0224e…e518`), `_Evaluation/**`, `docs/**`, `README.md`, `_DECISIONS/**`, the work graph, any `MEMORY.md`, or anything outside `projects/pec`.</li><li>`git diff --name-status origin/main...fb030850b` agrees.</li><li>The run's `containment.py origin/main`, rerun at HEAD: 119 product MODIFY / 2 Task Management MODIFY / 63 run-root ADD, `RESULT PASS`.</li></ul> |
| 6 | Run-record accuracy | PASS WITH NOTES | <ul><li>Hashes, counts and exit codes in `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` and `checks/COMMANDS.txt` match what I observed. For example, 57 run-root ADD at `fdc7a2071` and 63 at `fb030850b`; the closeout commit adds exactly the 6 files it names and modifies `COMMANDS.txt`.</li><li>The instruction hashes in `HANDOFF_STATE.md` (`CLAUDE.md` `336cc4fb…ab49`, `AGENT_WORKING_ITEMS.md` `9ae4bea2…9665`) are correct.</li><li>The federation projection names no TM-PEC-023 finding, as recorded.</li><li>No record claims CHECKING, acceptance, readiness or reliance, and none claims that a re-audit ran ("NOT DONE, by ruling").</li><li>The notes are N-1 to N-3 below.</li></ul> |

## Findings

No BLOCKING findings.

**N-1 NON-BLOCKING: a cited record file does not exist.**
- **Where:** `projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/VALIDATION.md` line 42, the Containment row.
- **Problem:** the row says "the final-state record is `checks/containment.out`", but there is no `checks/containment.out` at `fb030850b`.
- **What the run actually saved:** `checks/COMMANDS.txt` line 36 records the containment run as terminal-only, and at `fdc7a2071` (57 ADD), not at the final candidate.
- **Fix:** save `containment.py origin/main` output at the final candidate as `checks/containment.out` and index it in `COMMANDS.txt`, or reword the row to say the result was printed to the terminal. My rerun at `fb030850b` gives PASS: 119 / 2 / 63, 0 outside the boundary.

**N-2 NON-BLOCKING: residual 5 describes as possible something that has already happened.**
- **Where:** `projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/HANDOFF_STATE.md` lines 41–43 (residual 5, "Ordering with SCA-006").
- **Problem:** the residual says a baseline run before this act merges "would again report" the INFO findings. At the act's own basis, `590ec52c1`, this has already happened. The SCA-006 checkpoint-1 package (PR #922) reused `COV_SCA005_POSTSETUP_2026-09-25_1606` as its pre-change baseline: see `_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md` line 21, and `Pre_Change_Coverage.json`, which is a byte copy of that audit's `coverage_summary.json`. So SCA-006's recorded baseline carries COV-068/069/072/073 against the pre-D-PEC-95 state.
- **Consequence:** the proposal's re-audit rationale ("SCA-006's baseline will observe this state") no longer holds. The first audit to observe the D-PEC-95 state will be SCA-006's post-change audit (graph node R3).
- **What it does not affect:** the ruling ("no re-audit") and the act's bytes.
- **Fix:** restate residual 5 as fact, name the reused baseline and R3, and route the note to HELP_HUMAN or the SCA-006 manager.

**N-3 NON-BLOCKING: incomplete helper list and ambiguous wording.**
- **Where:** `MANIFEST.md` lines 224–225 ("Run-root contents") and `VALIDATION.md` lines 12–13.
- **Problem 1:** the MANIFEST helper list omits `containment.py`, which `HANDOFF_STATE.md` line 67 lists.
- **Problem 2:** `VALIDATION.md` says `<pre>` "is the same tree as `590ec52c1` (`diff -rq` over `projects/pec` showed only the new run root)", which is ambiguous about what was compared with what. The `<pre>` tar hash `152aba22…4024` does equal my fresh `git archive` of `590ec52c1`, so the claim itself holds.
- **Fix:** add `containment.py` to the list, and state the tar-hash identity instead of the `diff -rq` wording.

**Observation, no repair needed.** Both `_LATEST.md` N1 texts say COV-073 was "addressed". Under P, the SCA-005 snapshot half of COV-073 stays stale-conservative.
- These are the ruled generator bytes, the same under A and P.
- `_COORDINATION.md` item 14 records the two snapshot files by hash as superseded for current state.
- `HANDOFF_STATE.md` residual 3 discloses it.
- There is no misstatement within the grant.

## DEP-10-05-004 note (the ruling: "accept 10-05-004 as prepared")

`DEP-10-05-004` (DEL-10-05 → DEL-04-01, `IMPLICIT` / `MEDIUM`, Statement "Orientation reads are a logged consultation surface") was refreshed as prepared.
- Its new quote, "Owner use or non-use logging sufficient for the P2-B uptake observation and falsification evidence", is verbatim in its unchanged locus: `Deliverables.csv` DEL-10-05 Description.
- That description no longer names orientation reads, so the quote supports the edge to DEL-04-01 only implicitly. This is the weaker warrant the proposal records as finding 2.
- Per the ruling, I record this and do not fail it. Moving its evidence to `ScopeLedger.csv` SOW-085 ("PEC orientation and dashboard surfaces") remains a carry-forward for a later dependency packet, as `HANDOFF_STATE.md` residual 1 says.

## Overall verdict

**PASS WITH NOTES.** The act reproduces byte for byte from the bound generator on a fresh `13df8b795` export at the act date. Every fixed check gives the recorded result, containment is exact, and the T1 change is exactly what the pinned script produces, followed by a mechanical archive. N-1 to N-3 are record-accuracy notes and none blocks merge.

## Commands run (cwd is the checkout unless stated; exit codes shown)

Git reads:
1. `git -C <checkout> fetch origin main` — 0. This updated `FETCH_HEAD` and remote-tracking refs only; no working-tree change. `git rev-parse origin/main` gives `590ec52c1…`, and `git merge-base origin/main fb030850b` gives `590ec52c1…`.
2. `git -C <checkout> archive --format=tar -o <SC>/base.tar 13df8b795e47ab2284018eeefc9d5473d00c232d` — 0. The same command made `<SC>/main590.tar` from `590ec52c1…` and `<SC>/cand.tar` from `fb030850b…`, each 0. Each was then extracted with `tar -xf` into `<SC>/{base,main590,cand,repro,t1repo}`.

Reproduction:
3. `PYTHONDONTWRITEBYTECODE=1 python3 <SC>/gen_d95_bound.py --repo <SC>/repro --act-date 2026-09-25 --option P --retired-covers > <SC>/repro_report.tsv 2> <SC>/repro_stderr.txt` — 0.
4. `python3 <SC>/cmp_repro.py <SC>` — 0. Result: report identical, 119/119 files identical.

Fixed checks:
5. `PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/verify_d95.py <SC>/main590 . --option P --retired-covers` — 0. The same command with `<SC>/base` — 0.
6. `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` — 0.
7. `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <SC>/closure` — 0.
8. `sh <SC>/schema10.sh <checkout> <SC>/repro_report.tsv` — 10 × `validate_dependencies_schema.py`, each exit 0.
9. `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` — 0.
10. `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` — 0.
11. `python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv` — 0. The same with `REGISTER_CLOSED.csv` — 0.
12. `git diff --name-status origin/main...fb030850bb8530c5da3cf083e32610d7b2219d7f` — 0.
13. `git diff --check origin/main...fb030850bb8530c5da3cf083e32610d7b2219d7f` — 2 (291 notices, all in the run root). With `-- . ':(exclude)projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25'` — 0.
14. `git diff --name-status origin/main...fdc7a2071…` gives 121 M and 57 A. `git diff --name-status fdc7a2071 fb030850b` shows 6 A and 1 M.
15. `PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/containment.py origin/main` — 0 (PASS).
16. `python3 <SC>/contain.py <SC>` — 0 (tree-level containment).
17. `sh <SC>/holds.sh <checkout>/projects/pec <checkout>/projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/checks/hold_targets.txt` — `pec_reliance_hold.py --operation candidate-validation` ×121, all exit 0 and `ALLOW`.

Semantics and T1:
18. `python3 <SC>/n2diff.py <SC>`, `python3 <SC>/n3rows.py <SC>` and `python3 <SC>/locus.py <SC>` — all 0.
19. `PYTHONDONTWRITEBYTECODE=1 python3 <SC>/cand/.../t1_tm_pec_023.py --repo <SC>/t1repo --act-date 2026-09-25` — 0.
20. `python3 tools/taskmgmt/taskmgmt.py archive --register <SC>/t1repo/projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv`, first with `--dry-run` (0), then for real (0). The archive wrote only to scratch.
21. `python3 <SC>/t1rows.py <SC>` — 0.

Hash and content checks:
22. `shasum -a 256` / `shasum -a 256 -c` over the authorities, exports, 124 preimages and 119 postimages, `cmp` against the recorded outputs, and `gh pr view 924 --json …` — all 0. The one exception is `shasum -c SHA256SUMS` in the preparation folder, which exited 1 only because it lists a `D-PEC-95_DRAFT.md` that is not present (the same bytes are filed as the proposal). That predates this PR and is not in its diff.
23. `git status --short` at the end — empty.

The scratch helper scripts (`cmp_repro.py`, `contain.py`, `n2diff.py`, `n3rows.py`, `locus.py`, `t1rows.py`, `schema10.sh`, `holds.sh`) are in `<SC>` for reruns.
