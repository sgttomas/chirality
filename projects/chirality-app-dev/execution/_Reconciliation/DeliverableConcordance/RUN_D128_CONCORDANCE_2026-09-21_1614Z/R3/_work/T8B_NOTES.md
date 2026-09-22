# T8B — blind spot check, S1 sample B (PKG-06..PKG-10, EXT)

Input `R3/_work/SPOT_S1_B.csv`: 97 S1 rows. Checked field: `Disposition` on every row. No R3 reasoning
was read (no REMAP_LOG, RUNWIDE_CALLS, T*_ work files or Notes column). Evidence comes from the frozen
tree and the rulebook. Helper scripts are in `R3/_work/T8B_scripts/`.
## Counts
| Verdict | All 97 | PKG-06 | PKG-07 | PKG-08 | PKG-09 | PKG-10 | EXT |
|---|---|---|---|---|---|---|---|
| CONFIRMED | 95 | 14 | 16 | 18 | 18 | 13 | 16 |
| REFUTED | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| UNDECIDED | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
The Disposition refutation rate is 1/97 (1.0%).
## Refuted and undecided
- S1-112 `DEL-06-04#CLM-027` REFUTED: STALE_SPECIFICATION → IMPLEMENTED_DIFFERENTLY. The SoW says what
  SPEC §14.2 names, and SPEC still names it (`docs/SPEC.md:814-823`), so nothing stated is false. The
  live path has no Chirality MCP tools. Legacy gates writes by a handler wrapper instead of the SDK hook sequence.
- S1-172 `DEL-10-03#CLM-025.2` UNDECIDED. The only evidence is a text omission ("ready-for-construction"
  is missing from the K-DOMAIN-4 list). Reading 1 keeps PARTIALLY_IMPLEMENTED. Reading 2: that verdict
  describes code, no product-side claim was checked, and the omission is a text defect.
## HumanDecisionNeeded observations (not checked fields; recorded in Evidence)
- S1-120 `DEL-07-02#CLM-009.11` is clearly inconsistent. Its own verifier correction says "no R4-Q1
  (LIVE code meets part)", but the value is `R4-Q1`.
- S1-116 `DEL-07-05#CLM-012.17` has `NO` and may be missing R4-Q1. SPEC §13.1 governs harness opts, and
  only legacy `frontend/src/lib/harness/options.ts:7-22` warns on unknown keys.
- Systematic: rows with both `REACH=LIVE` and `REACH=LEGACY_ONLY` evidence usually cite R4-Q1 (S1-089, 100,
  101, 102, 105, 106, 121, 135, 141, 142, 151, 154). §2.4 rule 3 cites R4-Q1 only when legacy is the only
  code meeting the claim. Read part by part, those rows are right. Read as whole claims, they are wrong,
  because live code meets part. The rulebook does not say which reading applies. S1-120 shows R2
  verifiers used the whole-claim reading at least once.
## Other things seen
- REF-006 MATCH rows recompute consistently (PRD 17ca3f3c…, CONTRACT 57411f8d…), and STALE_SPECIFICATION
  is applied the same way each time.
- Stale SoW TBD placeholders are handled two ways. S1-156 and S1-157 take REMAINING_STATE_MISMATCH;
  S1-160 takes STALE_SPECIFICATION. Each can be defended, but rule 2(b) names TBD placeholders only
  as register bookkeeping.
- S1-162 and S1-164 depend on amended SPEC text (§16.1 `:881-884`, §11 `:693-703`). MR-11 supports
  STALE_SPECIFICATION there.
- S1-129 (ACCEPTED_DIVERGENCE) and S1-133 (DOCUMENTED_UNIMPLEMENTED, R4-Q4) differ because only DEL-08-03
  carries an SCA-APP-010 Gate-5 controlling section. The difference is consistent with MR-11.
