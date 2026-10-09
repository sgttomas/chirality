# T4-I10: T4-U3's slot table, for T3's agreement

**Terms:** `R4/BRIEFS/T4_WI_COMMON.md`. Your ID is T4-I10.

**Purpose.** T4-U3 lands the corrected expansion joint (an objective connector, JR's J-A and J-B) and deletes the old user-stiffness element and its plumbing in the same PR, with no historical copy (owner's M07 option A; H-3). The old element occupies about 15 reviewed solver slots; each must be implemented for the connector or fail closed (plan §4.3 item 4, §6). The slot table is agreed with T3's WORKING_ITEMS before any code. You write it.

**Read:** plan §3.1 (T4-U3), §3.3, §4.3 items 4–8, §6; annex A's T4-U3 part (`R4/PLAN_01/T3_AGREEMENT.md`); `R4/T4_RULINGS.md` (T3's items 5–7 and H-4); I3 in full; I5 on demand; `I/CORRECTNESS_DESIGN/JOINT_REFERENCE/CONTRACT.md` §2, §3, §5 and slices. The code at `ed012c7ccf`, where I3's lines (cited at `70e7f49ced`) may have moved: re-locate every site.

**For each slot** (dense and sparse assembly; NI linear assembly; NI nonlinear; NI strict gap; the K2b census and force scaling; K-D5's re-formation; K5/W4; S11-G bodies and edges; S11 formation and recovery site tables; F1b admission; retained recovery; source recovery; PP's builder and gate; validation and review rows; and any slot I3 missed), give:
- today's site for the old element (`path:line@ed012c7ccf`) and what it does;
- the decision, as the plan sets it: implement (dense, sparse and NI-linear assembly; the S11-G edge; K2b scaling; K-D5 Wide<2> re-formation of BᵀKB so joint cases are not demoted) or fail closed (NI nonlinear and strict gap until T5; retained and source recovery until T3-F2b), with the refusal code and where it is emitted;
- for implemented slots, the connector's treatment in one or two lines with its JR reference (B, Ke = BᵀKB, offsets, the qref residual as a ledger term, K2b's scaling of K, gp and qref; W4 treating a positive-definite connector as an objective link, a semidefinite one as unqualified);
- the tests deleted, rewritten or added, separating T3-owned tests (annex A's list, re-located) from others.

**Also state:**
1. **W4.** T3's tie reduction stays; only the producer goes (`user_element_tie`, `TieRefusal`, SA's `UserTie`). List what then changes in K5 (K5-C, the T4 tripwire, B10's names, NI's joint cases).
2. **No joint is silently skipped** (T3's item 6). For every input shape (incomplete, unmapped, legacy, annotation-only, connector), name the code or the admitted path; show that nothing falls through. Include D-4's refusal (`LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED`, its recognition rule, the `not_solver_consumed` exemption, its precedence before `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`) and `JOINT_PRESSURE_INTERFACE_UNRESOLVED` for a pressurized model with a joint until T4-U5.
3. **What must not change** (T3's conditions): PP's `Cargo.lock`; the priced layouts (`preview_physics::MemberRecord`, `formation_guard::RecoveryRecord`, the `Preview*` inputs), so connector fields go on component types; `preview_physics::LIMITATIONS`; `REVIEWED_INPUTS` and `REGISTERED_PROFILES`; H-4's summary key and historical row kind. Check each against your plan and say how it holds.
4. **Overlap with T3's `b2`** (`origin/codex/piping-t3-b2-20261008`; read only): which of T4-U3's files `b2` also edits (at least `retained_product.rs` and `PP/tests/s11f_site_test.rs`), and whether the hunks are disjoint.
5. **Published texts** that name the old element (NI's assumption and limitation strings, SA's M03 text, the joint validation text) and their correction; the refusal-code re-pins outside T3's corpora (annex A item 3).
6. **NI's four friction tests** (plan §4.3 item 7): the replacement coupling and how their expectations are re-derived independently.
7. **Commit plan:** an order of commits by slot family that keeps every intermediate commit compiling and every joint refused or solved.

**Output.** `SLOT_TABLE.md` (the table and items 1–7; at most about seven pages) and a one-page `RETURN.md` listing the questions for T3.
