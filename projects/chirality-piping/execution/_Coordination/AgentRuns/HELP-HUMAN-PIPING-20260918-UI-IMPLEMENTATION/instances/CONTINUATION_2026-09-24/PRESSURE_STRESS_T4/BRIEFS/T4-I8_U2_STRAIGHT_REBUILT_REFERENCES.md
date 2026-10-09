# T4-I8: independent references for T4-U2's rebuilt straight cases (freeze)

**Terms:** `R4/BRIEFS/T4_WI_COMMON.md`. Your ID is T4-I8.

**Purpose.** T3's U3 retired validation cases that rested on the legacy pressure computation. T4 rebuilds them under the exact contract, each with a new case id that records the retired id it rebuilds (plan §4.3 item 3); retired ids stay retired. The rebuilt cases live on PP's public entry and in the VP-STATIC `exact_pressure_1` package, not in the PP-free benchmark crates. You freeze their independent references before any code exists; a second TASK will refute them. A separate TASK (T4-I7) covers the bend cases, including the rebuilt CBPT.

Read plan §4.3 item 3, §5 (the T4-U2 row and "Rebuilt cases"), D-5's text (for what changes later); I4 §2.2–2.5, §4 and §5; `I/CORRECTNESS_DESIGN/PRESSURE_REFERENCE_QUALIFICATION.md` §1–3 and `STRESS_REFERENCE.md` §8; the retired cases at `ec5d397359` (I4 cites the files).

**Independence.** Derive each value from closed forms (Lamé, Hooke with the Poisson term, beam statics); do not take values from the product. You may read the product only for conventions: the exact route's section rule (OD and wall − mill tolerance; Ai from the reduced bore), row kinds and stations, frames and signs.

**Cases.**
1. **`STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS`, membrane values:** exact-route Lamé surface values (radial, hoop inner and outer) and σz, free with transferring closures and axially restrained, on today's section basis. The product has no corrosion-allowance input: state how the old case's allowance is folded into the authored wall, and mark the case to be re-frozen in T4-U6 if D-5 changes the basis.
2. **MECH-TP-PHYS-008/009, the pressure halves:** a new annular exact case (real OD and wall, E/ν): pressure plus thermal plus a partial-span transverse load, with a mixed restraint. The pressure term is wall tension 2νP, opposite in sign to thermal compression. Give displacements, six-component reactions and the five-station rows (N_w, S, membrane, Lamé) and the transverse actions.
3. **`STRESS-PRESSURE-MEMBRANE-ORIGINAL`:** a Lamé case with a thin-wall-limit comparison (state the thin-wall values and their relative difference from Lamé; the Lamé values are the reference).
4. **A straight-only v3 twin** of one existing v2 fixture (choose one from `PP/tests/fixtures/pressure_reference/`): the expectation is bit-equality of numbers with v2 (SP-1). Record the chosen fixture and what "bit-equal" covers.

For each: complete inputs, 0.3.0 and 0.4.0 document sketches (provisional where they depend on v3 fields), rows with frames and signs, both solver modes, relative 1e-9 with an explicit zero-scale floor per quantity.

**Output.** `REBUILT_REFERENCE.md` (derivations, at most about five pages), `rebuilt_reference_cases.json` (decimal strings, at least 17 significant digits, shaped for the `exact_pressure_1` package on T1's `load_reference_1` pattern), and a one-page `RETURN.md`.
