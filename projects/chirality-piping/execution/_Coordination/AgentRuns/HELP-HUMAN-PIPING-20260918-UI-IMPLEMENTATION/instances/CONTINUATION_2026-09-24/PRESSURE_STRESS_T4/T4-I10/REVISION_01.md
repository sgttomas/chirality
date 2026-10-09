# T4-I10 revision 01: what changed in `SLOT_TABLE.md`, and why

**Revisions.**
- Revision 00: `471ad93f48`, SHA256SUMS `e8e7db1a…`.
- This revision folds in T3's review RV130: NUM `ccdc6119d2`, `NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/REVIEW_RV130/t4_i10_01/REVIEW.md`, sha256 `8408c97f477e74cd…`. The verdict was PASS WITH AMENDMENTS (0 blocking / 9 should-fix / 10 notes).
- It also folds in T3's decisions on items 1–11 and WI's rulings (both as relayed by WI), and `R4/T4_RULINGS.md` at `46aa203c14`.

**Unchanged.** The code basis is unchanged (`ed012c7ccf`). No new code reading changed revision 00's citations; the new sites were checked at `ed012c7ccf`. `RETURN.md` is unchanged and historical; its questions are answered in §0.

## Should-fix

| Amendment | Change | Where |
|---|---|---|
| S-1 | New slot S21: replaced spans are excluded from `pipe_sections` (`PP/src/lib.rs:5568`), `pipe_materials` (`:5571`, `:5585`) and `formation_entity_bodies` (`:1201-1211`). T4-U2a's v3 evidence follows the same rule | §2 S21; §3; §4.7 step 5 |
| S-2 | Annotation joints are refused on the exact route: on v2, `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`; on v3, the proposed seam code **`EXACT_PRESSURE_FAMILY_NOT_ADMITTED`** (refs `[component]`, the family named). The pressure-interface exemption proposal is withdrawn | §4.2; §0.5 |
| S-3 | The binary64 path forms r = (xⱼ − xᵢ) + (aⱼ − aᵢ), never pᵢ = xᵢ + aᵢ. The K-D5 case undemoted at UTM carries inexact offsets, a skew Q and a coupled K, in both modes, plus an ordinary twin and a perturbed-matrix kill with its control | §1; S1; S10; §3 |
| S-4 | `connector_reference_load_bound` uses \|xⱼ − xᵢ\| + \|aⱼ − aᵢ\| for r and the full rounding count, rounded up. It is listed as a T8 token in hunk (c) | S13; §4.4 |
| S-5 | The W4 successor: (a) rank 6 and B·rigid = 0 on the exact B from the binary64 inputs; (b) a `b()` tripwire; (c) a hinge-type PSD mechanism case; (d) B10 widened to `FK/src/connector.rs`. PD is decided on the assembly's K | S11; §3; §4.1 |
| S-6 | Every new joint input rides inside the `objective_connector` Value; no serde-typed field is added; the decoder handles units | §0.3; §4.2 |
| S-7 | The priced list is completed (`StraightPipeElement`, `LinearSupport`, `SpringEntry`, `PrimitiveLoad`, `StationResultants`, and others). S20 and S21 use a lookup set, never a new field | §1; §4.3 |
| S-8 | `f1b_tests.rs:571` (`:597`) is now R, with a v3 connector request in the declared subset | §3; §4.7 step 5 |
| S-9 | Connector rows are a declared coverage limit (outside R-b′ and EF). Each q − q_ref component is one exact sum | S14 |

## Notes

**Required.**
- **N-2:** the legacy-field unit checks and normalization are kept. The five validation helpers are deleted and `is_expansion_joint_component` is kept (S19).
- **N-3:** FK site-table rows for new accumulations in already-scanned files; the reviewer confirms no new PP module pushes, folds or solves (S15; §4.4).
- **N-6:** a connector's `solver_consumption` must be absent or `objective_connector`, otherwise `OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE` (§1; §4.2).
- **N-9:** the authoring surfaces are dispositioned (§4.7 step 7).
- **N-10:** fixtures carrying the M03 text are re-grepped and re-pinned in the text commit (§4.5).

**Adopted as well.**
- **N-1:** the `source_recovery.rs:1630` test site (§3).
- **N-4:** (b) is a pure deletion, at a gap of 32 (§4.4).
- **N-5:** the formed Ke is scaled with `force_scaled_matrix` (S8).
- **N-7:** "no q_ref terms" is decided exactly (S13).
- **N-8:** the PD method is an exact LDLᵀ, or a one-sided certified test (S11).

## T3's decisions and WI's rulings

- **Items 1–11:** recorded in the table at §0.4.
  - The `retained_product.rs` hunk is accepted.
  - s11f (a)–(c) are accepted, with (b) a pure deletion.
  - T8 is unchanged, with the producer beside `PP/src/lib.rs:3897`.
  - The M03 and strict-gap texts are corrected in T4-U3, with `SA/k5_tests.rs:1225-1226` and `NI/src/lib.rs:4780`, `:4922` re-baselined in the same commit (§4.5; §4.7 step 6).
  - `pressure-1` stays outside `REVIEWED_INPUTS` until B7.
  - The retired-code lists are not extended.
  - The 3 files are accepted.
- **SP-1:** a declared exception, (a)–(c) (§0.1).
- **The residual shape:** the legacy code (§4.2).
- **Topology:** `replaces_span` only (§1; §4.2).
- **0.4.0:** the replaced span's resolved state is unused; a nonzero eigenstrain, self-weight or load is refused with `JOINT_REPLACED_SPAN_LOAD_UNOWNED` (S20; §4.2).

## One interpretation for WI to confirm

S20 refuses authored loads on the replaced span by **presence**, zero values included, following the exact route's inventory rule. WI's ruling says "nonzero". Relax this to nonzero-only if WI prefers; nothing else depends on it.
