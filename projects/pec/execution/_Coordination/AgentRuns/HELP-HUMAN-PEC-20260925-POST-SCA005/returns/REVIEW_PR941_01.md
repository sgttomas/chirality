# Review 01 of PR #941 (D-PEC-96 revision 4; D-PEC-78 §4.3 REVIEW), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `04f6eaecb4c3556f6503d028123d5fe6ed2f90ad`.
- **SHA-256 of the report text below (UTF-8):** `b034fd818417cf37f6e11036f4c272a1ef86b11765b483dc0fb67bfa72b2d9c9`.

## Report (verbatim)

## D-PEC-78 §4.3 review of PR #941, D-PEC-96 revision 4, head `04f6eaecb4c3556f6503d028123d5fe6ed2f90ad`

**Verdict: CHANGES REQUESTED.** There are two blocking findings, and both are text fixes in HELP_HUMAN's records. The revision-4 product bytes, the act script, the tests and the mutation evidence reproduce exactly on my own export of `94e9255b6`. The direction is applied fully and only in the schema, the adapter, the tests, `loops.json` and the scripts.

`gh pr view 941` gives headRefOid `04f6eaecb…` and the base is `origin/main` `94e9255b6`. I did not modify the checkout or switch its branch. Everything ran in `mktemp -d` exports under my scratchpad.

### Blocking findings

**B1. The register row's Decision cell still describes revision 3.**
- **Where:** `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md:113`, column 2.
- **What it says:** "PEC's own row, as a separate owner question: `shared-dev-loop` live, … (recommended), or `remaining-loop` as accepted at SCA-005 Q8 (a); PEC's Remaining sections through a new `remaining-items` profile."
- **Why it is wrong:** revision 4 removes option A-R and both Remaining profiles. The row's own last column says revision 4 is published. So the register describes the packet with exactly the vocabulary the owner told us to drop. A python cell split confirms 6 columns, and that column 2 contains both `remaining-items` and `remaining-loop`.
- **Fix:** rewrite column 2 for revision 4. It should give the three-profile vocabulary, `shared-dev-loop` live with `loop-receipts-ledger` and `agentruns-json` historical as the question-2 row, and the Remaining sections settled by the owner's direction (not read, no profile). Keep the other columns.

**B2. The S2 and X1 carry-forwards the proposal describes are not in the graph.**
- **What the proposal says:** at `D-PEC-96_…proposal_2026-09-25.md:96` it says the stale "declares `remaining-loop` now" text (SOW-094 Notes, the DEL-01-06 description and `_CONTEXT.md`) "is carried to graph node S2 … as before". At :97 it says the FX-PEC-0 / R-05 redefinition "is carried to graph node X1".
- **What the graph has:** `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md:62` (S2) and `:67` (X1) carry neither item. `git log -S'FX-PEC-0'` over `WorkGraphs/` returns nothing, so "as before" was never true either. The items appear only in the G1 return's "Carried forward" list.
- **The stale text is real:** I confirmed it at base in `_CONTEXT.md:17`, `Deliverables.csv:10` and `ScopeLedger.csv:72`. `SOFTWARE_DECOMP.md:630` also still names `remaining-loop` as a vocabulary example.
- **Fix:** add the items to the S2 and X1 rows in this PR. S2 gets the stale DEL-01-06 and SOW-094 sentences. X1 gets FX-PEC-0 without the `## Remaining` sections, plus R-05. Optionally, also record the `SOFTWARE_DECOMP.md` §9 example and the path-normalization residual.

### Non-blocking findings

- **N1 (medium). The proposal's `AGENTS.md` note overstates the correction.**
  - The proposal (:22, :106) says the owner directed a separate correction of "those sentences", meaning the ones that keep the sections as records whose "gate markers still bind that item".
  - The merged record `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md` limits the correction differently. It replaces candidate L261–270 so that PEC adds no new sections and no feed profile reads them. It keeps the status quo for the existing sections: they stay in place and each item's gate markers still bind that item. The owner must also approve the exact hunk before merge.
  - Suggest restating it that way and citing the amendment-1 record.
- **N2 (low). Citation and quotation of the owner's direction.**
  - The proposal gives the owner's words only as "Relayed by HELP_HUMAN" (:5–9). It does not cite `_DECISIONS/D-PEC-96_AMEND_DIRECTION_2026-09-26.md`, which is now on `origin/main`.
  - The second quote (:9) cuts off the owner's sentence ("; yes, ride checkpoint 3.  SCA-006 pinned.") with no ellipsis. The part that is quoted is verbatim. The double spaces in the first quote are preserved byte for byte.
- **N3 (low). The probe test only partly checks its cleanup.** The test asserts cleanup for one key only (`test_json_loop_registry.py:230`, `assertNotIn("probe-ledger", FEED_PROFILE_VERSIONS)`). It does not check `FEED_PROFILE_SURFACES` or `probe-lifecycle`. `patch.dict` restores both dicts in any case. The full suite passing, with `test_schema_documents…` running later in alphabetical order, also shows nothing leaked. The claim that "the probes are removed afterwards" is therefore only partly demonstrated by the test itself.
- **N4 (cosmetic). Leftover option naming.** `apply_d96.py:828` still prints `OK option=A`, and the `mutate_d96.py` docstring says "option A applied". Leave `apply_d96.py` alone, because its bytes are hash-bound.
- **N5 (low). A dropped evidence row.** Revision 4 removed revision 3's "path-rule probe" row from the evidence table, but finding 3 (:192–196) still asserts which paths are accepted.
- **N6 (info). Off-by-one in the G1 report.** The verbatim preparer report (G1 return :341) says `SHA256SUMS` "covers 24 files", but it has 25 entries including the draft. Do not edit it, because the text is verbatim.
- **Editorial changes beyond the direction.** They are justified by A-R's removal or the basis refresh. They include restructuring, the reworked SCA-006 section, removal of the moot "why not literal `remaining-loop`" rationale, and a more accurate triage line for the DEL-08-02 notice in the graph (`WORK_GRAPH.md:114`, which I checked against the notice).

### What I verified

**1. Scope.**
- `grep -ri remaining` finds nothing in the applied `v2/`, in `postimages/`, or in any of the prep scripts. The only hit in the prep folder is CHECKS_SUMMARY's own statement that the grep was run.
- I diffed revision 3 against revision 4 for the proposal and for every postimage, script and evidence file. The product changes are exactly these:
  - `remaining-items` removed from `loops.json`;
  - two `oneOf` options removed from the schema;
  - two keys each removed from `FEED_PROFILE_VERSIONS` and `FEED_PROFILE_SURFACES`, plus a comment;
  - three overlap sub-cases replaced by the disjointness test and the probe test;
  - the A-R paths removed from all four scripts;
  - M11, M16 and M19 replaced, and a TOTAL line added to the runner.
- The port, both `__init__.py` files, the contract test and the fixtures are unchanged.

**2. Design.**
- The surface table (proposal :122–131) matches `FEED_PROFILE_SURFACES` and the schema's "Surfaces:" lists. The three profiles are pairwise disjoint.
- The probe test is sound. It covers live+historical, two live readers and two historical grammars at the right locations, plus a disjoint control. Nested `patch.dict` restores both dicts.
- The at-least-one-live rule is enforced (adapter L200). The "no live profile" sub-case and M15 exercise it.
- The PEC row and its bases match revision 3's, and both basis files exist.
- The schema v2 `$id` `https://chirality.local/pec/v2/config/loops.schema.v2.json` is identical to revision 3's.
- The sub-case counts are 21 for invalid profiles and 6 for no-echo, as claimed.

**3. Reproduction on the `94e9255b6` export** (Python 3.13.7, `PYTHONDONTWRITEBYTECODE=1`).
- **`apply_d96.py`:**
  - `--check-only`: exit 0, 6 UNCHANGED, 11 READ, 11 RENDER, and the tree is unchanged.
  - The act: exit 0. The report matches `evidence/actA.report.txt`, and `diff -rq` shows exactly the 11 paths.
  - Rerun: exit 1 on a preimage mismatch.
  - Drift in `software-workflow.json`: exit 1, and nothing is written or created.
  - `--pec-row remaining` and `--pec-row migrated`: exit 2 each, tree unchanged.
- **Byte equality:** all 11 applied files equal `postimages/optionA_v2/`.
- **Rebuild:** `build_json_postimages.py` regenerates the 4 JSON postimages byte for byte. `build_apply_d96.py` regenerates `apply_d96.py` at exactly `80725b4f…bbf3`.
- **Evidence diff:** my `git diff` matches `evidence/optionA_vs_8f9bd314c.diff` except that the created fixture's hunk is ordered differently.
- **The five registered checks** via `run_registered_checks.py`, in git-backed throwaway clones:
  - base: api 6, registry 12, store 13, posture PASS, harness INFO=14 / NOT_APPLICABLE=1 / REVIEW=4 / WARN=124;
  - applied: api 6, **registry 19**, store 13, posture PASS with 0 findings and core tree `dd7e1dda…6e5a`, harness stdout identical to base (`e5f9ff706de84cc8…`).
  - The selector picks all five checks for the 11 paths.
- **Enforcement suite:** 28 OK. `git diff --check` is clean, and there are 0 non-ASCII bytes in the 11 postimages.
- **`mutate_d96.py`:** baseline OK, **TOTAL 19/19 CAUGHT, RESULT PASS**. The output is identical to `evidence/mutate_optionA.out`.
- **Fail-closed probe:** with M1's anchor made invalid, the runner reports NOT_APPLIED, TOTAL 18/19, RESULT FAIL, exit 1.
- **Reliance-hold preflight:** the register is header-only, and `candidate-validation` returns ALLOW with exit 0 on 6 review targets.

**4. Owner questions and text.**
- There are six questions.
- "Settled by the owner's direction (not a question)" is present (:606–608).
- Question 2 keeps its honest line: the direction "is not itself a ruling … Question 2 therefore still asks for the row explicitly" (:87, :617).
- The first quote keeps the double space; see N2 for the second.
- The carry-forwards are B2, and the `AGENTS.md` note is N1.

**5. Publication.**
- The filed proposal hashes to `4506597b…5180e`, which equals the `D-PEC-96_DRAFT.md` entry in `SHA256SUMS`.
- `shasum -a 256 -c` passes for all 24 other entries; only the draft is missing.
- The folder holds only `.gitattributes` and `SHA256SUMS` beyond the listed files. `.gitattributes` is byte-identical to main's (`58c68d8a…`).
- The G1 return's revision-4 report hash `c3e729d0…9252` reproduces over lines 316–412 with no trailing newline, the same convention as revisions 1–3, all of which also reproduce.
- Revision 3 on main is `2f7d9875…afc4`.

**6. Register, graph and hygiene.**
- The register row has 6 columns and its hashes are correct; its content is B1.
- The graph shows G1 ACTIVE under review and R3 ACTIVE and dispatched. The B6 brief is `8bdc7181…2df4` and the S3 brief is `ef12b740…537a`; both verified.
- `git diff --check origin/main...HEAD` is clean.
- On a HEAD export: receipts validator VALID (exit 0), strict decomposition validator 0 errors and 0 warnings, harness exit 0.
- PR CI: every run check passes (the rest are skipped).

Key paths:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md`

## HELP_HUMAN disposition

The verdict is CHANGES REQUESTED, on two blocking findings in HELP_HUMAN's records. Both are repaired in the next commit. The revision-4 product bytes reproduce exactly and are unchanged.

- **B1:** the register row's Decision cell now describes revision 4.
- **B2:** the S2 and X1 rows now carry the `D-PEC-96` carry-forwards.
- **N1 and N2** are wording in the preparer's hash-bound proposal. They are disclosed to the owner with the presentation rather than re-revising the proposal:
  - N1: the governing record for the `AGENTS.md` correction is SCA-006 group-2 amendment 1. It keeps the existing sections' status quo, and its hunk needs the owner's approval.
  - N2: the direction record is `_DECISIONS/D-PEC-96_AMEND_DIRECTION_2026-09-26.md`, and its second quote is truncated in the proposal.
- **N3–N6** are low or cosmetic. They are noted, with no change, since the hash-bound bytes stay as reviewed.
