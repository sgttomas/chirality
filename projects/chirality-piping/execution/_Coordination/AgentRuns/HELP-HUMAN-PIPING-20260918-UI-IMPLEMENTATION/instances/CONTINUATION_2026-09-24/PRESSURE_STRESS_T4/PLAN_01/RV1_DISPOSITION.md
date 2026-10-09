# T4 plan 01: dispositions of T4-RV1's findings

**Who:** HELPS_HUMANS (T4), 2026-10-09 UTC.

**Review:** `R4/T4-RV1/REVIEW.md`. It reviewed revision 1 and was BLOCKING on B-1; it confirmed the physics of H-2.

**Plan:** `R4/PLAN_01/PLAN.md`, revision 2.

Every finding is accepted. The table names where each repair is.

| Finding | Disposition | Where in revision 2 |
|---|---|---|
| B-1: self-weight on an arc is `CannotBound`, so the first path and C2 cannot reach Passed | Accepted, repair (a): T4-U1b, a formation certificate for arc load vectors, designed with T3 before the code | §0; §1 C2 and the done criteria; §2 P-D and SP-2; §3.1 T4-U1b; §3.3; §5; D-2 rationale |
| S-1: the rename created a dependency cycle | Accepted: "T3's U3 merged before any T4 code" | §3.2 T3 row |
| S-2: the deletion PR is held behind T4-U2 | Accepted: T4-U2a, the admission seam and v3 identity; T4-U3 depends on it | §2; §3.1; §3.1 Order |
| S-3: the references presuppose the equivalence | Accepted: a direct wall-load integration and a polygon-limit control are required; the other forms are cross-checks | §5, T4-U2's cases |
| S-4: SP-1 against the new recovery form | Accepted: straights keep today's formulas; SP-1 restated (v2 byte-identical; straight-only v3 bit-equal to v2) | §2 SP-1; §3.1 T4-U2; H-2 |
| S-5: excluded effects incomplete | Accepted: static pressure only, and the Poisson mean on the arc, disclosed in D-3 and the v3 approximation text | D-3 |
| S-6: legacy recognition catches annotation joints | Accepted: an explicit `not_solver_consumed` is exempt | §6 |
| S-7: bend end-row frame left to T4-U4 | Accepted: the pressure family's end rows on arcs are in the tangent frame in T4-U2 | §3.1 T4-U2 |
| S-8: effort figures are lower bounds | Accepted: work and gate-inclusive ranges, and a longer calendar | §7 |
| N-1 to N-8 | Accepted: c_b's sign and the orientation-free remainder (H-2); the tangency tolerance (T4-U2); ε_p's rounding and A = As (T4-U2); the station double-count control (§5); the pressure-load basis in D-5; 0.4.0 coverage and chord bends refused anywhere on the exact route (§1 C1, D-2); T4-U0 and T4-U1 together (§2); v2 refuses p < 0 (§4.3 item 2); H-4 reworded | as listed |
| Added risks (RV1 §3 item 6) | Accepted: R9 (the latency of T3's agreements) and R4 (collisions with T3's reader lanes) | §7 |

**Also in revision 2, at HELP_HUMAN's direction:**
- units renamed T4-U0 to T4-U9;
- §3.3 and annex A state the T3 side, from T4-I5;
- H-4 names the corpus generation.

**From T4-I5:** the W4 recommendation changed from deleting T3's tie reduction to keeping it and deleting only the old element's producer (§4.3 item 4, §6, annex A).

## T4-RV1's delta check (`R4/T4-RV1/ADDENDUM_01.md`): CONFIRMED, with one open item

| Item | Disposition | Where |
|---|---|---|
| OI-1: the v2 refusal of p < 0 conflicts with "v2 byte-identical" | Fixed: the carve-out "except T4-U0's declared refusal of p < 0, whose byte evidence follows T3's U3 form" is added | SP-1; H-1; §5, the T4-U2a row |
| Note: the calendar assumes overlap | Stated beside the figure, with the 25–38 working days if run in series | §7 |
| Note: T4-U2a's table | The `pressure-1` table is added as a new file; the reviewed physics-1 table is not edited | §3.1, the T4-U2a row |
| Note: the certificate must add the Wide re-formation's own error to the difference (SF-2) | Carried into T4-U1b's design agreement with T3 | §3.1, T4-U1b in detail |
