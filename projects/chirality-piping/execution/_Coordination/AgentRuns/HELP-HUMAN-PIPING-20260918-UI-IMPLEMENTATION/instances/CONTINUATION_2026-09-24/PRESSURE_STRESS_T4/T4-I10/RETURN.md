# T4-I10 RETURN: questions for T3 on T4-U3's slot table

**From** TASK T4-I10, **to** T4's WORKING_ITEMS. The record is `SLOT_TABLE.md` (20 slots, tests, items 1–7), cited @ed012c7ccf; b2 = `e582b61f9e`. WI's five T3 constraints are folded in. Each holds as designed, except where a question below asks T3 to choose.

## For T3's WORKING_ITEMS

1. **`retained_product.rs:1558`.** One unavoidable 1-line hunk: `built.user_stiffness_elements` becomes `built.connectors`. It sits 5 unchanged main lines after b2's insertion and is merge-clean. Alternatively T3 adds a `BuiltModel` predicate in its next edit there. Which?
2. **Site tables.**
   - `s11f_site_test.rs`: a PRODUCERS row after `:221`; TABLE row `:511` replaced by the q_ref producer row (36 lines from b2); a FORMATION_SITES entry after `:1382`.
   - FK `s11_site_table.rs`: row `:194` out; `FK/connector.rs` into `SOURCES`.
   - T8 (`:1475-1480`) forces the producer into `PP/lib.rs`: keep T8 as it is, or widen it?
3. **Texts on T3's surfaces.**
   - The M03 family text (`SA:1539`) reaches every curved (mixed) body. Correcting "user/curved" changes curved-bend outputs and fails `SA/k5_tests.rs:1225` by design.
   - The strict-gap reason (`SA:2577`, pinned `NI/src/lib.rs:4780`, `:4922`) has the same issue.
   - Correct both in T4-U3 as a declared change, or at B7?
4. **W4.**
   - Delete `user_element_tie`, `TieRefusal` and `UserTie`; keep the reduction; pass `&[]` ties.
   - A positive-definite connector is a **link** (null(BᵀKB) = null(B) = rigid modes); a semidefinite one is unqualified and goes to the matrix gate. PD is decided exactly and libm-free.
   - K5-C and the tripwire are deleted; the successor is an exact rank and rigid-mode proof in FK's connector tests.
   - Should B10 scan the definiteness function?
5. **K-D5.** Re-form BᵀKB in Wide<2> from binary64 (xᵢ, xⱼ, aᵢ, aⱼ, Q, K). Is the decode of K from (H, Ls), and of aᵢ = Qᵢ·offset, input representation outside EF? Kill required: connector cases undemoted at ordinary and UTM coordinates, and a perturbed Ke demotes.
6. **S11-G.** +BᵀKq_ref is a formed term, `Formation::Bounded` and self-equilibrated. Connector rows stay outside R-b′, as curved rows do; they are recovered with `ExactAccumulator`, and `RecoveryRecord` is unchanged. Agree?
7. **F1b.** At b ≠ 0, family `objective_connector` is not admitted (`NUMERICAL_INTEGRITY_UNRESOLVED`), as curved is. K2b's census and scaling include the connector. Agree that it fails closed?
8. **No silent skip.** Confirm the classification map (§4.2) and the successors:
   - `…STIFFNESS_INCOMPLETE` → legacy / `OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE`;
   - `…MAPPING_UNRESOLVED` → legacy / `OBJECTIVE_CONNECTOR_TOPOLOGY_UNRESOLVED`;
   - `…EQUILIBRIUM_UNQUALIFIED` and `…MACRO_ELEMENT_INPUT_INVALID` → legacy;
   - the residual shape → legacy with refs `[component]`;
   - the backstops (NI, W1, source, K-D5).

   A T3 reviewer checks this on the diff.
9. **Reviewed inputs.** Connector kinds go only into T4-U2a's new `pressure-1` table. Does it stay outside `REVIEWED_INPUTS` until B7? Readers' retired-code lists are not extended (historical `JOINT_ELEMENT_*`).
10. **SP-4.**
    - The two refused-demo envelopes plus their generation manifest regenerate: + legacy code, − review info. These are 3 files whose `LIMITATIONS` bytes are unchanged. Can T4-U3 carry them?
    - `result_export_v0_2.json` needs no re-pin. This corrects annex A item 3: its joint strings are model-input `completeness` values.
11. **W1 first.** The connector stays `Option<Value>` through `parse` (`PP/src/lib.rs:2258`, before admission at `:2263`) and is decoded in the gate. Agree?

## For WI or HELP_HUMAN

- **SP-1 versus D-4.** Refused v2 envelopes holding a joint change their diagnostics; no admitted v2 case does. Declare an SP-1 exception, or exempt v2 from the precedence?
- **Annotation joints on v3:** admitted as pipe, and exempt from `JOINT_PRESSURE_INTERFACE_UNRESOLVED` (proposed)?
- **Topology scope:** `replaces_span` only; series and parallel refused (proposed)?
- **Code placement:** the producer in `lib.rs` is an exception to plan §4.3 item 8.
- **References:** an independent reference TASK for the NI friction replacement and the J tests, before code.
