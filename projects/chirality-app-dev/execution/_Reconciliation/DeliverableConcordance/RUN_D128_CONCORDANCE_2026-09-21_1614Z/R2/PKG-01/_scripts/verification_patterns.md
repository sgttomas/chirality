## §4 Patterns (hand-written by the PKG-01 manager from the shard notes)

1. **Authority handling holds across the package.** Every AUTHORITY_CONFLICT row that was checked
   (DEL-01-01 4/4, DEL-01-03_A 3, DEL-01-04 12/12 checked, DEL-01-02 all but two) applies CONVENTIONS §1
   bullet 3 as the verifiers read it. D-GOV-43 names Root DIRECTIVE §5/§7 but never App DIRECTIVE §2.8
   (Claude/Anthropic key-aware default), §2.10 or §4.2, or CONTRACT K-PERM-1/K-PERM-6. App DIRECTIVE §0 ranks
   App documents only; it does not rank a Root ruling against them, so the order resolves none of these rows.
   No checked row lets a Codex-only preamble of PRD or CONTRACT override the unamended DIRECTIVE. That was the
   dispatch concern, and it did not happen.
2. **Split-ledger inconsistency on the same authority question (DEL-01-02, CONTESTED ×2).** The two halves
   were written by independent workers and read the same question differently. S2 marks K-PERM-1 hard-deny
   against D-GOV-43 item 4 as AUTHORITY_CONFLICT (CLM-044), while S1 does not (CLM-006.3,
   IMPLEMENTED_DIFFERENTLY). S2 marks DIRECTIVE §2.8 as AUTHORITY_CONFLICT (CLM-040, S1's STATE-1), while
   CLM-038.3 reads it as STALE_SPECIFICATION. The `cf.` rule kept each half valid but could not force the
   halves to agree. R3 should cluster these rows together.
3. **Reach tags from the module map were over-read.** 4 of the 8 V-DEL-01-02-1 refutations tag code LIVE when
   it is reached only through a barrel re-export (`engine-conformance`, `GovernedAgent1RunCoordinator`). The
   reverse pass already caught most of this: 17 DEL-01-02 errata, plus 1–2 errata each in DEL-01-01,
   DEL-01-03_A and DEL-01-04, are REACH corrections, and all errata rows but one were CONFIRMED. The refuted
   erratum is DEL-01-02#CLM-011.1 RemainingWork, where "all 13 IDs legacy-only" overstates. The dispatch
   lesson (confirm symbol reach) reduced this error but did not remove it.
4. **Human-gate guarantee (CONTESTED ×2, DEL-01-02 CLM-006.5 / CLM-007.6).** The served transition route
   requires actor `HUMAN` and an `approvalSha`. However, the actor is caller-asserted, the SHA is checked for
   format only, and nothing live stops a direct `_STATUS.md` write. Read as a guarantee under the subject test,
   this is PARTIALLY_IMPLEMENTED. It is the R0 §8 item 4 / R4-Q3 pattern on the live route. DEL-01-01's
   reverse pass adds a related gap: no live UI performs lifecycle transitions at all.
5. **R4-Q1 on bundled rows (CONTESTED ×4, DEL-01-04 HumanDecisionNeeded).** Table rows mix a half met on the
   LIVE path (ambient settings) with a half met only on the legacy path (bypass guard). Rule 3 does not
   settle whether R4-Q1 applies. HELP_HUMAN's later clarification ("only when LEGACY_ONLY code is the only
   code meeting the claim on the product path") points toward plain R4 for these rows. That clarification
   arrived after every PKG-01 ledger had sealed.
6. **Other CONTESTED Dispositions.** These are DEL-01-01#CLM-021.6 (STALE_ASSESSMENT vs STALE_SPECIFICATION;
   the same question applies to CLM-009.8), DEL-01-02#CLM-059.3 (tie-break 2(b) vs 1 on a SoW "TBD"), and
   DEL-01-03#CLM-009.7 (ALIGNED vs AUTHORITY_CONFLICT on the live sandbox-mode copy).
7. **Reverse class c:** 36/36 CONFIRMED. Across the package, every response is PARTIAL or NOT_MINE and none is
   CLAIMED_BY, which fits PKG-01's role as governance and register documents.

## §5 Rerun decisions and structural notes

- **No rerun.** The rerun threshold was computed separately on ledger rows and on reverse responses (§2
  per-deliverable table). Every unit shows 0 verdict-field REFUTED (0.0% for ledger rows and 0.0% for
  reverse responses), and no unit has a structural failure. All 13 field-level refutations are in
  `CORRECTIONS.csv`, built by `_scripts/corrections.py`.
- **DEL-01-02 split.** Each half was validated against its subset index before the merge:
  `_split/INDEX_S1.csv` for S1 (24 units, 87 rows, sha256 `fb6c10c8…e7b`) and `_split/INDEX_S2.csv` for S2
  (37 units, 44 rows, sha256 `10b65e9b…ed10`). Both returned `RESULT PASS errors=0 warnings=0`. The merged
  ledger (`59ad30af…2cb2bad`) is cell-identical to S1 followed by S2 (checked by script) and passes against
  the full CLAIM_INDEX. The S1 worker wrote the reverse pass and errata against the merged ledger.
- **DEL-01-03_B** is double-blind comparison only. It passes the structural checks (§1) and was not
  verified.
- **HELP_HUMAN notes received mid-run** (STATE.jsonl): (i) the `OTHER:V3_ROLE_ADOPTION` spelling; (ii)
  out-of-root evidence grades CONTESTED; (iii) the Addendum 6 rule-3 clarification. All three arrived after
  every forward ledger had sealed. Notes (ii) and (iii) went into the verifier brief (grading keys 14–15 and
  4a), and the two V-DEL-01-02 shards then running got them by message. V-DEL-01-01 and V-DEL-01-03_A had
  already returned with 0 REFUTED.
