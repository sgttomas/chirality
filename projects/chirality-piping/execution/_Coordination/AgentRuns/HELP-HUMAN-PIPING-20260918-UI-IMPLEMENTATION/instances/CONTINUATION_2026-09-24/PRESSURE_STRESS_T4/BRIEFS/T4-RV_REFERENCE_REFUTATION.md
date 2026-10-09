# T4 reference refutation (independent reviewer)

**Terms:** `R4/BRIEFS/T4_WI_COMMON.md`. Your ID (T4-RV<n>) and the reference set you refute (`R4/T4-I<m>/`, with its SHA256SUMS digest) are in your dispatch prompt.

**Purpose.** Plan §5: each unit's VP-STATIC references are frozen by one TASK and refuted by a second before any code is read. You did not write the reference set; nobody has written T4's code for it. Try to break it. A reference that passes your attack becomes the unit's acceptance basis, so an error you miss becomes a product defect that every test confirms.

**Read:** the reference set and its brief (`R4/BRIEFS/T4-I<m>_*.md`); the plan sections and research that brief names. Verify the SHA256SUMS first; report any mismatch and stop.

**Check, each finding as BLOCKING, SHOULD-FIX or NOTE with the affected claim, evidence and consequence:**
1. **Values.** Re-derive the load-bearing values independently, by a different method from the reference's wherever one exists: for example a stiffness-method solve with your own curved element against a unit-load reference, exact rationals against decimals, or a closed form against a numerical integral. Cover every case family, not a sample of one. Re-run the reference's own scripts and confirm they reproduce the JSON byte for byte.
2. **Independence.** Does any reference presuppose what the code under test must establish (RV1 S-3; for bends: the K·u_free equivalence)? Were values taken from the product?
3. **Formulation match.** Does each reference model what the product is meant to compute under the approved plan (energy terms, k's scope, section rule, closure ledger, D-3's exclusions, frames, signs, stations, units), so that a correct product passes and a reasonable wrong one fails?
4. **Coverage.** Against the plan §5 row and the brief: every case, quantity, solver mode, document version and negative control present; anything missing.
5. **Discrimination.** Each negative control's wrong values differ from the right ones by well over the criterion; criteria and zero-scale floors neither hide a real error nor fail a correct product on rounding.
6. **Transport.** Inputs complete enough to author the documents; JSON shaped as the brief requires; provisional fields marked.
7. **Hygiene.** Placeholders only.

**Output.** `R4/T4-RV<n>/REVIEW.md` (at most about four pages) with a disposition (PASS, PASS WITH FINDINGS, or BLOCKING), and your scripts and their stdout under `R4/T4-RV<n>/_run_records/` with a SHA256SUMS. Do not commit. You will normally be asked to confirm the repair of your own findings.
