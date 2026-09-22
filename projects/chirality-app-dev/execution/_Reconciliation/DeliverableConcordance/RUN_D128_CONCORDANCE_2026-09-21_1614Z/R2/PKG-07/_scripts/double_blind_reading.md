## 10. Reading (hand-written by the PKG-07 manager; agent measurement, not a ruling)

- **Disposition overall:** exact 19/31 (61%), overlap 24/31 (77%); on the 23 keys neither worker split,
  18/23 (78%), and ALIGNED-vs-non-ALIGNED 23/23. Most exact-set disagreements come from worker A
  splitting a key into an ALIGNED/PARTIAL row plus a STALE_SPECIFICATION row (CLM-013, 020, 021, 025)
  where B wrote one row, and from DOCUMENTED_UNIMPLEMENTED vs PARTIALLY_IMPLEMENTED on the 501 scaffold
  route (CLM-005, 019, 024: whether the served route counts as partial delivery).
- **STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH (Addendum 5):** no key splits purely between the two.
  Both workers put the REF-006 MATCH restatements and the stale register text in STALE_SPECIFICATION and
  kept REMAINING_STATE_MISMATCH for Remaining/metadata lag (A 1 row, B 2). Compared with DEL-06-02
  (19/35, most splits between these two verdicts), the tie-break removed this source of variance here.
- **HumanDecisionNeeded / R4-Q1 (Addendum 6):** agreement 19/31 (61%); A cites R4-Q1 on 0 rows, B on 22
  (12 base keys). Both workers read the claims as product behaviour and both wrote `ALSO_MODULE:` on
  ~18–19 rows, so the subject test was applied the same way. The split comes from **REACH tagging of
  `scaffold.ts`**: A tagged the parser/plan code TEST_ONLY (only tests call `scaffoldExecutionRoot`), B
  tagged it LEGACY_ONLY (reached via the legacy `scaffold_preview` tool). The verifier of A's ledger
  sided with B's tag on those lines (CORRECTIONS.csv) but held that mixed TEST_ONLY + LEGACY_ONLY
  evidence does not meet rule 3's "only code meeting the claim is LEGACY_ONLY". Addendum 6 therefore
  stabilised the subject reading; the remaining variance is in symbol-level reach and in how rule 3
  treats mixed legacy/test-only evidence.
- **Reverse:** Response agreement 362/364 (99%); same claiming base key 6/6.
- **CauseTag** agreement stays low (15/31): A used PRE_V3_DRIFT for the REF-006 drift (refuted by its
  verifier: the drift is 2026-09-12, DOC_HYGIENE) and A2_TOPOLOGY for the scaffold gap; B spread the same
  rows differently.
