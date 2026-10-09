# T4-I9 return: T4-U1b's certificate design

**Who and when:** T4-I9, TASK (Type 2), to T4's WORKING_ITEMS. 2026-10-09 UTC.

**Brief:** `R4/BRIEFS/T4-I9_U1B_CERTIFICATE_DESIGN.md` (`6a15cd3c…`), with T3's five added constraints. The design is `DESIGN.md`, and the evidence is in `_run_records/`. No Git writes. No tracked file was changed. No cargo was run.

## Outcome

**The design.** The arc's consistent uniform-load vector of T4-U1's objective element is re-formed in midpoint–radius arithmetic, with `Wide<2>` midpoints at p = 128 and binary64 radii rounded upward.
- **Proved enclosure.** |f − m| ≤ r, by Lemmas L0–L7 and Theorem 1.
- **Exact defect.** S11-G gets `v − m` exactly in A_net, and `r` in B.
- **SF-2.** cond(F) is covered by a residual-verified inverse (ρ < 1/2); cancellation by absolute radii; libm is not used, and its effect on `v` is measured.
- **Failure.** Any failed precondition stays `CannotBound`.

**The interface.**
- one new `Formation::Certified` arm in FK `load_ledger.rs`;
- one new FK module, `structural/arc_certificate.rs`;
- one inline call-site hunk in PP `add_uniform_element_loads`.

These are unchanged: `LIMITATIONS`, reviewed inputs, PP's `Cargo.lock`, the priced layouts, `retained_product.rs`, `tests/s11f_site_test.rs`, `formation_guard.rs`, SA, CB, and K-D5's `formation_check.rs`.

**The probe** (an emulation, not a product run):
- **Enclosure:** 84 of 84 certified cases are enclosed by an independent 70-digit reference. The radius is ≤ 4.4e-29 relative for φ ≥ 1°.
- **Guard statistic** with the objective binary64 element:
  - ≤ 2.3e-2 of the threshold in the L line, and 0.30 in a bend-dominated body, for φ ≥ 1°, at ordinary and UTM coordinates;
  - ≤ 3e-3 for φ ≥ 5°.
- **φ = 0.1°:** the binary64 element itself fires at 1.7–37×, a true catch.
- **k = 1e40:** refused, `CannotBound`.

**SP-2.** Nothing in the certificate stops Passed. The residuals are listed plainly in DESIGN §7: arcs under about 0.5–1°, K-D5 after T4-U1, T4-U2's pressure terms (not probed), and acceptance of R-1.

## Points for ROOT (T3's constraint 5: a narrowing of a check)

**R-1.** S11-G was selected with "CannotBound for curved consistent vectors" as a condition (RR, "Selection: the S11-G design"). T4-U1b replaces it, for certified terms, with the proved certificate.
- That is sound under Theorems 1 and 2, but it narrows where S11-G demotes.
- T3's item 4 accepts T15's change only through this design. ROOT confirms the change of condition.

**R-2 (conditional).** If no model with a Passed ordinary report can be built that fails the certificate naturally, T15c and M16's kill move to a `#[cfg(test)]` seam plus unit tests. That reduces test power.

**Not narrowing:** O-3 adopted (a strengthening), O-9 (no token is removed), and the rebuilt `ruling1` test (the same assertions).

## Open questions for T3

| ID | Question |
|---|---|
| O-1 | Is R-SF2 (DESIGN §1) the right reading of RR, "S11-G after V1's S11G_CHECK", item 3? In particular: is libm "included" when its effect on `v` is measured exactly and nothing relies on its accuracy? |
| O-2 | Should `Formation::Certified` be a new variant, or is the equivalent no-type-change form, `Exact { scale: 1 }` with `operand_bound = r`, preferred? |
| O-3 | Lemma 3: with `Bounded` and `Certified` terms, n′ and S\* use intended values within B. If no row fires, the effective criterion is c/(1 − c), a 10⁻¹⁸ relative excess, already true for the exact-pressure operands today. Either accept it, or set `CRITERION` = RD(10⁻⁹/(1 + 10⁻⁹)) in `formation_guard.rs` (a strengthening, one constant and one test) |
| O-4 | `atan_positive` is labelled "later-slice API (W1c; K3 Q6)" (wide.rs:938-939). May T4-U1b be its first product caller, or should it use `included_angle(S, C)` (K-D5's path, 23.55u)? |
| O-5 | For the pressure identity K̃·u_free(ε_p), keep the thermal identity's convention, with K̃ and the chord held and K̃'s formation left to K-D5. ε_p's own error enters as an operand bound. Certifying against K_int is possible, but it is not proposed |
| O-6 | Caps: certify the tangents and P from held operands. This is stricter than the old held-tangent caps family. Agreed? |
| O-7 | T15c: is a natural certificate failure with a Passed ordinary report constructible? If not, the seam applies (R-2) |
| O-8 | Rebuild `ruling1_both_guards…` (s11g_tests.rs:1780) with a straight UDL-W1e8-type load-row trigger? |
| O-9 | T8's class string ("curved CannotBound") goes stale but still passes. Update it in T4-U2's T8 edit, which must add the caps site anyway, or in B7? |
| O-10 | Pass B and G7: the certificate adds statically reachable constant-bounded loops under `solve_load_case`, although W1 refuses curved models first. Does G7's TEXT mapping need rules for them, and so a re-registration? If it does, that is SP-4-like and goes to HELP_HUMAN |
| O-11 | Adding the FK `SOURCES` extension for `arc_certificate.rs` to FK's `tests/s11_site_table.rs`, on K1's precedent: agreed? |
| O-12 | T3's reviewer is asked to check L0–L7, Theorems 1 and 2, Lemma 3, and identities (I1)–(I4) |
| O-13 | Observation, no T4-U1b action: R-b′ does not cover arc end rows (S11G §4). D-2 makes arcs the normal bend, so T3 may want an arc analogue |

## Files

- `DESIGN.md`
- `RETURN.md`
- `_run_records/arc_cert_probe.py`, with its stdout
- `_run_records/opcount.py`, with its stdout
- `SHA256SUMS`
