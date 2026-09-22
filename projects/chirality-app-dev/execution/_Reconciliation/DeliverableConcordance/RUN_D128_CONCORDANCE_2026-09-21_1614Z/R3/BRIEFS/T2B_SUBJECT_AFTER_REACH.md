# T2B — Subject test on rows that lost every LIVE tag under run-wide reach calls (a)/(b)

Read `_COMMON.md` first. Also read CONVENTIONS §2.3 (ImplementationEvidence reachability: a
requirement met only on a LEGACY_ONLY path is judged on the live path — PARTIALLY_IMPLEMENTED,
IMPLEMENTED_DIFFERENTLY or DOCUMENTED_UNIMPLEMENTED; a claim about the retained module itself is
judged at module level), §2.4 "Legacy-versus-live subject test" rules 1, 2 and 4, RUN_BASIS Addenda 6
and 8 (TEST_ONLY code does not meet a product claim), and `<RUN>/R3/_work/T4A_RUNWIDE.md` (R3's
run-wide reach calls: (a) barrel-re-exported contract modules whose relied-on symbols have no live
consumer are TEST_ONLY or LEGACY_ONLY; (b) validation and proof scripts are TEST_ONLY).

**Input.** `<RUN>/R3/_work/CAND_SUBJECT.csv` (99 rows): rows whose sealed Disposition says code
meets the claim in whole or part (ALIGNED, PARTIALLY_IMPLEMENTED, IMPLEMENTED_DIFFERENTLY,
ACCEPTED_DIVERGENCE) and whose ImplementationEvidence had a LIVE tag that calls (a)/(b) removed
(`PreReachTags` → `PostReachTags`). R4-Q1 on these rows is handled by another task; do not change
HumanDecisionNeeded.

**For each row decide:**
- `KEEP_MODULE`: by rule 1 the subject is the module (the claim names a code unit and states only
  its own contract, no product-observable outcome) — judged at module level, the Disposition holds.
- `KEEP_OTHER`: the Disposition does not rest on the re-tagged code (for example the claim is about
  validation tooling itself, or other LIVE evidence in the cell meets it, or the row is about
  documentation text).
- `REDISPOSITION`: the subject is product behaviour (rules 1–2) and, after the reach call, only
  TEST_ONLY or LEGACY_ONLY code meets it. Give the live-path Disposition per §2.3 and add
  `ALSO_MODULE:<sealed verdict>` (rule 4).
- `UNDECIDED`: give both readings.
Check the frozen code where the row does not show whether live code meets the claim. Keep the
disagreement visible: every change carries the sealed reading in Notes.

**Output 1.** `<RUN>/R3/_work/T2B_REMAPS.csv`: `ClaimKey,Field,NewValue,Call,Evidence` — only for
REDISPOSITION rows: one `Disposition` row (full new value), and one `Notes+` row whose NewValue
starts `R3_RUNWIDE(a|b): sealed <verdict> relied on <path> tagged LIVE before the reach call;` and
includes `ALSO_MODULE:<verdict>`. `Call` = `a` or `b`. If the CauseTag must change because the row
was `NONE` (ALIGNED) and is now divergent, add a `CauseTag` row with a vocabulary tag.

**Output 2.** `<RUN>/R3/_work/T2B_VERDICTS.csv`: `ClaimKey,Verdict,NewDisposition,Basis` for all 99.

**Output 3.** `<RUN>/R3/_work/T2B_NOTES.md` (≤ 40 lines): counts and patterns.
