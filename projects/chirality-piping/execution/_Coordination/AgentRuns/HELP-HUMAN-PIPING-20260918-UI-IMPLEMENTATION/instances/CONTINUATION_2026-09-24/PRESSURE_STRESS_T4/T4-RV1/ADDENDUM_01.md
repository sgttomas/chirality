# T4-RV1 addendum 01: delta check of plan 01, revision 2

**Who and when:** T4-RV1, TASK (Type 2), 2026-10-09 UTC.

**Requested by:** HELPS_HUMANS, by message. This is a delta check of the repairs to my own findings, not a fresh review. The terms are those of `R4/BRIEFS/T4-RV1_PLAN_REVIEW.md`: read only, no build, no commit.

**Bytes checked (sha256 verified):**
- `R4/PLAN_01/PLAN.md`, `902ede80ccc40161e6e3fa0d28a79cf0e0ed288d5dbc20bcd773d5bb4241f359`;
- `R4/PLAN_01/RV1_DISPOSITION.md`, `64e94839db5652251e01b6b9345eea5c8ab40864ec2be2799ec08586b179777a`;
- `R4/PLAN_01/T3_AGREEMENT.md` (annex A), `159356ac1055f50acf1df6c8f384fae9121a03966238786e5e2612e05029db53`;
- its source `R4/T4-I5/RETURN.md`, `4bc9deb361840b500bcede17c082257ab610767a05fcc4c8a316d1688418320b`, read only for the W4 and `REVIEWED_INPUTS` facts.

The review under check is `R4/T4-RV1/REVIEW.md` (`3d38f6cb…`), which the plan's Evidence table cites with the right hash.

## Disposition: CONFIRMED, with one open item (OI-1)

B-1 is cleared. S-1 to S-8 and N-1 to N-7 are repaired as the disposition table says. The repair of N-8 introduced OI-1, a one-line wording conflict. T4-U2a leaves no cycle, the W4 recommendation is consistent, and record hygiene passes.

## Checks

**(1) B-1 is repaired.** T4-U1b, a formation certificate for arc load vectors designed with T3 before any code (§3.1, its detail paragraph, §5 row, §3.3 and annex A item 4), now sits on the critical path: T4-U2 depends on T4-U1, T4-U1b and T4-U2a. These parts now cohere:
- the done criterion (§1: Passed for cases with weight, pressure and temperature);
- C2 (uniform loads on a realized arc are no longer `CannotBound`);
- P-D (every load term on an arc can be certified);
- SP-2 (it fires only after T4-U1 and T4-U1b, for a case with weight);
- D-2's rationale.

The plan also records that D-2 removes the premise of T3's acceptance. The method is to re-form the vector in Wide precision with K-D5's arc machinery and take the exact difference, held to SF-2's conditions. That is sound as a design direction, with one note for T3's design agreement: the difference alone is an estimate. The certificate is a bound only once the Wide re-formation's own error is added, through cond(F), cancellation and libm, which is exactly what SF-2 requires.

**(2) S-1 to S-8 and N-1 to N-8, against the table:**

| Finding | Repair, and where it is in revision 2 |
|---|---|
| S-1 | §3.2 now reads "T3's U3 merged before any T4 code"; no `T4-U3 merged before` remains. |
| S-2 | T4-U2a holds the seam and the v3 identity; T4-U3 depends on T4-U2a (§3.1, Order). |
| S-3 | §5 requires a direct wall-load integration and a polygon limit at k = 1; Σ K·u_free and the thermal analogue are cross-checks only; the anchored closed form is now from the direct integration. |
| S-4 | SP-1 is restated. Straights keep today's formulas (SP-1, T4-U2, H-2). |
| S-5 | D-3 lists static pressure only (no momentum or transient loads) and the Poisson-mean statement, in the limits and in the v3 approximation text. |
| S-6 | §6 exempts an explicit `not_solver_consumed`, and T4-U3 gets a negative control for it. |
| S-7 | Arc end rows of the pressure family are in the tangent frame in T4-U2. |
| S-8 | §7 gives work and with-gates ranges. The work-days sum to 45–67 against the stated "about 45–65", which is fine. |
| N-1 | H-2 states the outward c_b and the orientation-free remainder. The negative control's residual is −pAi(t_in − t_out). |
| N-2 | A tangency tolerance; kinks beyond it are refused as mitres until T4-U7. |
| N-3 | ε_p's rounding and A = As (T4-U2). |
| N-4 | The station double-count control (§5). |
| N-5 | D-5 names the pressure-load basis. |
| N-6 | 0.3.0 and 0.4.0 (C1, §2, §5); chord bends refused anywhere on the exact route (D-2). Today the exact route refuses every component, so this is no regression. |
| N-7 | T4-U0 and T4-U1 start together. |
| N-8 | H-4 is reworded. Signed pressure: see OI-1. |

**(3) The T4-U2a seam.** The edges are:
- T4-U0 ← T3's U3;
- T4-U1 ← T3's U3 and T3's agreement;
- T4-U1b ← T4-U1;
- T4-U2a ← T4-U0 and H-1;
- T4-U2 ← T4-U1, T4-U1b and T4-U2a;
- T4-U3 ← T4-U2a and T3's agreement;
- T4-U4 ← T4-U2;
- T4-U5 ← T4-U2 and T4-U3;
- T4-U7 ← T4-U2 and T4-U5;
- T4-U8 ← T4-U4 and D-6.

The graph is acyclic, and T4-U2 still inherits T4-U0's `.expect` and bend-guard fixes through T4-U2a. No dependency is missing.

**(4) W4.** The recommendation reads the same in all four places: §4.3 item 4, §6's deletion list, §3.3, and annex A items 1 and 5. Keep T3's tie reduction, and delete only the old element's producer (`user_element_tie`, `TieRefusal`, SA's `UserTie`), unless T3 chooses otherwise. The Blocking list and R9 refer to T3's agreement on §3.3, so the old "agreement to the W4 deletion" is gone. This matches T4-I5's §0 (the cheaper alternative, I3's D3, which needs T3's choice).

**(5) Record hygiene.** PASS for the plan, the disposition table, annex A and T4-I5's return. They contain no home, user or temporary-directory path and no machine name; "the owner's Mac" describes a platform.

## Open item

**OI-1. The v2 refusal of p < 0 conflicts with "v2 byte-identical" (introduced by the N-8 repair).**
- **The conflict.** T4-U0 now makes the v2 producer refuse p < 0 by name (§3.1; §4.3 item 2; §5's T4-U0 negative control). But SP-1 says "v2 cases must stay byte-identical … Any other change stops the work", and H-1 and T4-U2a's validation say the same.
- **The consequence.** A v2 case with p < 0 changes from a published envelope (which all three readers reject) to a refusal. Applied literally, SP-1 stops T4-U0.
- **The fix.** Add the carve-out in SP-1, H-1 and the T4-U2a row: "except the declared p < 0 refusal (T4-U0), whose byte evidence follows T3's U3 form". The refusal itself is a sound choice within authority: it aligns the producer with its readers.

## Notes (no action required)

- **Calendar.** The with-gates critical path T4-U1 → T4-U1b → T4-U2 sums to 25–38 working days, about 5 to 7.5 weeks. The stated "about 4–6 weeks" therefore relies on T4-U2's reference, design and authoring overlapping T4-U1 and T4-U1b, as §2 says. Stating that assumption next to the figure would help.
- **T4-U2a and T3's side.** Annex A and §3.3 cover T4-U1, T4-U1b and T4-U3 only. T4-U2a edits the three readers and adds a `pressure-1` table skeleton. `REVIEWED_INPUTS` is a fixed list of 14 files (`PP/src/build_identity.rs:148-163@70e7f49ced`), and it includes `semantic_contract_v0_3_physics_1.json`, which holds the reserved `pressure-1` entry. T4-U2a should therefore add its table as a new file and leave the physics-1 table unchanged. Otherwise it re-registers the profiles, and SP-4 applies. T4-U2a's T3-interface review (§7) is the place to confirm this.
