# T6 — Run-wide call (e): DEL-02-01 half A / half B splits (fresh re-examination)

Read `_COMMON.md` first. Also read CONVENTIONS §1, §2.4 (R4-Q4), §2.6 (ACCEPTED_DIVERGENCE needs
a GOVERNING ruling that permits the difference; CONTEXT alone never makes a row
ACCEPTED_DIVERGENCE) and RUN_BASIS Addendum 4.

**Background.** DEL-02-01 was split across two workers by SoW section range and merged
(`R2/PKG-02/DEL-02-01/MERGE_REPORT.md`, halves in `DEL-02-01/A` and `/B`). On the same evidence,
half A read the agent-matrix and PORTAL/loop-first removals as `IMPLEMENTED_DIFFERENTLY` with
`R4-Q4`; half B read sibling units (CLM-017, CLM-020.x, CLM-025) as `ACCEPTED_DIVERGENCE`. The
verifier refuted CLM-017 (the one sampled half-B row of the kind, now corrected only on fields
other than Disposition — check the current cell). CLM-020.3/.4/.5/.8 and CLM-025 were not
sampled. See `R2/PKG-02/VERIFICATION.md` §§ on the split-halves disagreement and
`R2/PKG-02/PACKAGE_SUMMARY.md` items near "Half B rated".

**Task.** You are fresh: do not rely on either half's reasoning. For every DEL-02-01 row about
the agent matrix, the PORTAL / loop-first shell, the Workbench/Pipeline surfaces or the composer
that the 2026-09-09 v3 role adoption (`9b005c23a`) removed — at least CLM-010.1, CLM-017,
CLM-019, every CLM-020.x, CLM-025, and any other DEL-02-01 row whose Notes or evidence name those
surfaces (find them by script in `CLAIM_CONCORDANCE.csv`) — re-examine against the frozen tree:
the SoW text, the governing sources the row names (D-APP-74, D-APP-108, PRD FR-001/FR-007, App
DIRECTIVE, SCA-APP-010), the register, and the code at `00115c719`. Decide the Disposition,
CauseTag and HumanDecisionNeeded a consistent reading gives, and whether a GOVERNING ruling
actually permits the difference (needed for ACCEPTED_DIVERGENCE).

Keep the disagreement visible: where your reading differs from the current cell, the R3 value is
yours, and the current value stays in Notes as `R3_SPLIT(e): half <A|B> read <verdict>`. Where
both readings stay defensible, do not change the Disposition; add the Notes marker only.

**Output 1.** `<RUN>/R3/_work/T6_REMAPS.csv`: `ClaimKey,Field,NewValue,Call,Evidence` (`Call`
= `e`; full new cell for Disposition / CauseTag; for HumanDecisionNeeded use `Field = HDN_TOKENS`
with space-separated token operations such as `-R4 +R4-Q4`; `Field = Notes+` with only
the text to append, starting `R3_SPLIT(e):` or `R3_RUNWIDE(e):`). Only real changes.

**Output 2.** `<RUN>/R3/_work/T6_RUNWIDE_E.md` (≤ 90 lines): **Evidence**, **Call**, **Affected
rows** (a table: key, half, current Disposition/HDN, R3 Disposition/HDN, one-line reason),
**Limits**.
