# K14P review 01 — fresh read-only `pec-reviewer` (opus), head `540d2ce2a7fa19bca702dbb98bc5b8d9ac10e978`

Transcribed by the manager from the reviewer's handback (the reviewer is read-only). Verdict: **FAIL** (one BLOCKING, mechanical). Manager dispositions follow the findings.

## Reviewer's findings (as delivered)

**BLOCKING**

- **B1. Eight shortened hashes in the draft do not match the files they name** (prefix right, suffix wrong): L12 D-PEC-94 record `b6814e90…6a5e6b` → `…1e5a6b`; L14 `projects/pec/AGENTS.md` `df9196d1…eb9` → `…eb8`; L15 `Impact_Assessment.md` `93253b7d…b692b` → `…cb691`; L18 project-setup `WORKFLOW.md` `7aa4c30a…d6dd` → `…dd6d`; L18 `contract.md` `e9f0d11b…e218e` → `…c218e`; L18 preparation `execution.json` `dd59f002…c2bd` → `…ec2d`; L18 dependency-extract `WORKFLOW.md` `e5523eba…c18c3` → `…f18c3`; L117 and L417 `_COORDINATION.md` `95ebe344…8d90c` → `…8a90c`. Blocks because the owner rules on these bytes and `projects/pec/AGENTS.md` §"Selection and decisions" requires recomputing pinned hashes and stopping on mismatch; question 4(a) pins `_COORDINATION.md` by a failing hash. The full hashes in the basis table (50) are all correct.

**NON-BLOCKING**

- **N1.** With both parts applied, `verify_d101_k4.py … --covers --allow-k1` exits 1 (containment 149 vs 129), yet the verification table requires PASS. State the exact expected result or verify K4 against the K1-applied tree.
- **N2.** `--actor` (changes both `_STATUS.md` history lines) and `--reproduction` are output-affecting options the draft does not bind; the slot rule says `{D}` is the only varying byte; question 5 invites a different actor without stating the effect on two postimages and the `all_K1` / `created_K1` aggregates.
- **N3.** Provenance records only the first HELP_HUMAN amendment, not the resume amendment (Notes-line question, C-08 drop, rerun at newer `origin/main`).
- **N4.** The claim that the manager ran `dispatch-for-production` on K4's 132 candidate files has no recorded output.
- **N5.** "D-PEC-101" is embedded in K1's output bytes and generator hash; a different final number invalidates the K1 generator and tables — say so.

**NOTES**

1. "read none of each other's targets" is overstated (K1 reads PKG-08/PKG-10 sibling contexts; K4 after K1 reads K1's new files); suggest "neither writes the other's targets".
2. DEL-10-13 → DEL-10-02 points a PREREQUISITE edge into a C-08 standing node (precedent E-A18; the plan names it) — could be disclosed; if K2 classifies DEL-10-13 standing, K2 should name its `_DEPENDENCIES.md`.
3. DERIVED strata for DEL-10-13 are defensible and conservative.
4. The quoted "does **not** open B1 … or any other Lane B item" is `Propagation_Plan.md` L545 (Q-CP2-2 (a)); cite the plan line.
5. Committed evidence CSVs have CRLF (`git diff --check` noise); not a gate.
6. L132 ("one WORKING_ITEMS instance … may run each selected generator") vs L381 (a TASK runs K1) — align.

**Verified** (reviewer's items 1–6): census (K4 129 = 63 + 66; K1 32 = 12 + 20; lifecycle counts); every tabled postimage and aggregate reproduced on fresh exports of `dfb089b8a` and `aca930622`; generator hashes and byte-identical rebuilds; fail-closed reruns, wrong-date refusal, check-only non-writing, 14-file slot rule, order independence; quotes verbatim in their loci; 127/127 currency, mirror invariant 127/127; strict and closure results as stated; COV-080 74/74; git-backed checks; 161/161 `candidate-validation` ALLOW; owner acts verbatim; `fill_draft.py` re-renders byte for byte; `SHA256SUMS` verify; PR containment 132 additions only. Reviewer disclosed one throwaway `/tmp/null_out` briefly written and deleted outside the scratchpad.

## Manager dispositions (applied in the next commit; draft re-rendered)

| Finding | Disposition |
|---|---|
| B1 | Repaired: all eight short hashes corrected in `.src.md`; a check script (`check_short_hashes.py`) now verifies every `xxxxxxxx…yyyy` short hash in the draft against the full hashes it can resolve |
| N1 | Repaired: verification row states that on a combined tree the K4 check is run on the K1-applied tree as its before-state (recommended order K1 then K4), and records the expected single containment FAIL if run against the original export |
| N2 | Repaired: grant and slot rule state the tables assume `--actor TASK+preparation` and no `--reproduction` during the act; a different actor string changes the two `_STATUS.md` postimages and the `all_K1` / `created_K1` aggregates, so question 5 now says so |
| N3 | Repaired: Provenance records the resume amendment |
| N4 | Repaired: the preflight was rerun and saved (`evidence/hold_dispatch_k4_candidates.tsv`) |
| N5 | Repaired: one sentence added — a different final number requires rebuilding K1 (generator, tables, aggregates) and re-review; K4 bytes are number-free |
| Note 1 | Reworded to "neither writes the other's targets" with the reads stated |
| Note 2 | Disclosed as a finding |
| Note 4 | Citation corrected to `Propagation_Plan.md` L545 |
| Note 6 | Aligned: the manager may run K4; a TASK runs K1 |
| Notes 3, 5 | Recorded; no change |
