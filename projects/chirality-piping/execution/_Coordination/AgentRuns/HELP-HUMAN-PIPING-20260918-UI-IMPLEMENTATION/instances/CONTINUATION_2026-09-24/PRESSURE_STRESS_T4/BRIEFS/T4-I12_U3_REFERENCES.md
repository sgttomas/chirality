# T4-I12: independent references for T4-U3, the corrected joint (freeze)

**Terms:** `R4/BRIEFS/T4_WI_COMMON.md`. Your ID is T4-I12.

**Purpose.** T4-U3 lands an objective connector (JR's J-A and J-B) and deletes the old user-stiffness element (H-3; owner's M07 option A). You freeze its independent references before any code exists; a second TASK will refute them. Read plan §5 (the T4-U3 row), §4.3 items 4–7, §6; `R4/T4-I10/SLOT_TABLE.md` §1, §2 (S1, S8, S10, S11, S13, S20), §4.2 and §4.6; I3 §3; `I/CORRECTNESS_DESIGN/JOINT_REFERENCE/CONTRACT.md` and `INDEPENDENT_REFUTATION.md` in full; the connector contract I3 cites (`CONNECTOR_CONTRACT_V1.md`).

**Independence.** JR's values are themselves a frozen design. Re-derive every value you freeze from JR's definitions (exact rationals where possible), and say where you agree with JR's stated numbers and where you do not; a disagreement is a finding, not something to smooth over. No product code exists for the connector; do not take values from the old element.

**References to freeze** (each with complete inputs: nodes, Q, offsets aᵢ and aⱼ, K or H with Ls, q_ref; expected B, Ke = BᵀKB, end actions, generalized q and g, energy; signs and frames exactly as JR §2 defines them):
1. JR J1 and J2, including the common-rotation mode giving zero.
2. The B oracle (refutation's Fi, Mi, Fj, Mj).
3. The six rigid motions of the actual nodes in the null space of Ke; rank B = 6; for a positive-definite K the null space of Ke is exactly the rigid motions (the W4 link rule), and a semidefinite K example whose null space is larger (unqualified).
4. Offsets; preload through q_ref (the +BᵀKq_ref load and the recovered g); coupled H (JR's 4/1/9 → 0.075 J); reversal of node order; scale.
5. The finite-rotation value (qt = [L(cos φ − 1), L(sin φ − φ), 0]) as a negative control the small-rotation connector must not claim.
6. A system-level case through PP: the invented demo model's joint re-authored as a v3 connector replacing its span, which formerly left 658.44 N·m unbalanced, now in equilibrium within criterion. Define the connector data and give the reactions and connector actions.
7. Negative controls: JR's raw-difference values (240 N, 0.36 J) as analytical expectations the product must not produce; the replaced span's load ownership (`JOINT_REPLACED_SPAN_LOAD_UNOWNED`) as a refusal test.
8. **NI's four friction tests** (SLOT_TABLE §4.6): the replacement coupling, an ordinary frame element on an off-axis chord with rational direction cosines, and the re-derived expectations of each assertion in `NI/src/lib.rs` at the four call sites (`ed012c7ccf`), in `fractions`, from the frame's own section. The tolerance stays 1e-12.

**Criteria.** Relative 1e-9 in both solver modes for system cases, with explicit zero-scale floors; exact or 1e-12 for FK unit-level identities, stated per item.

**Output.** `U3_REFERENCE.md` (derivations, conventions, limits; at most about six pages), `u3_reference_cases.json` (decimal strings, at least 17 significant digits, or exact rationals as strings), scripts and stdout under `_run_records/`, `SHA256SUMS`, and a one-page `RETURN.md`.
