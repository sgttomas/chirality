# T4-I11 RETURN: T4-U2's desktop authoring design

TASK T4-I11 (Type 2), for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I11_U2_AUTHORING_DESIGN.md` (`a2b2f404…`), terms `T4_WI_COMMON.md` (`7d44afd0…`). Code basis `ed012c7ccf`. Design only: no tracked file changed, no cargo, no Git write. The design is `AUTHORING_DESIGN.md`, and the probe is `_run_records/tangency_probe.py` with its stdout.

## Plan, stop rules and T3 conditions

- **No stop rule is triggered.**
  - SP-1: straight runs keep v2's 64ε guard and pre-cancelled ledger, and v2's published texts are unchanged.
  - SP-4: authoring touches no T3 corpus or pin. Preview-physics-1 is untouched. The PP warning text T4-U1 changes (`BEND_GEOMETRY_INPUT_MISSING`) appears in no committed fixture (F, grep).
- **T3's conditions hold.** PP's `Cargo.lock`, the priced layouts and `preview_physics::LIMITATIONS` are unchanged. The one PP facade edit is a call-site `pub use` line.
- **One item changes a ruling's stated scope and needs ROOT (D-E below).** Everything else is within WORKING_ITEMS' authority.

## Findings that drive the design (facts, §0 of the design)

1. **Today's geometry-only bends are corner markers.** The desktop points `bend_pipe_ref` at an incident straight, and the demo marker has none. So "realize in place" would turn a straight into an arc. Realizing a marker needs tangent points.
2. **The applier refuses p < 0 under every profile.** `pressure_profile` accepts only v2, and is locked on 0.4.0. Six sites read "exact" as `mode === exact_straight_pressure_v2`.
3. **The browser cannot solve an edited model.** The solve, and the export of its result, are covered only natively: the src-tauri test and the owner's witness.
4. **`author_type` is never checked**, so "agents never populate k" is unenforced today.
5. **Authoring is file-disjoint from T3's `b2` lanes**, and needs no `previewService.ts` change.

## Decisions

| # | Decision | Recommendation | Authority |
|---|---|---|---|
| D-A | Automatic tangent-point insertion (`insert_bend_at_corner`) | Include it in T4-U2. It is the smallest correct path for corners at any angle and for every existing marker. Fallback: realize spans only, with users authoring tangent points by hand, which is practical only for axis-aligned L lines. | WORKING_ITEMS. The brief allows it when it is the smallest correct path. |
| D-B | `bend_plane_orientation` | Remove the requirement; do not consume the field. The span's `y_reference` is the single plane and side authority. T4-U1 drops the field from PP's warning condition, and T4-U2's authoring stops requiring it. | WORKING_ITEMS. Tell T4-U1's implementer. |
| D-C | Radius and angle authority | R plus the node geometry. The angle is derived and never written by new operations. An existing angle is kept and checked with PP's 1e-6 rule. | WORKING_ITEMS |
| D-D | Solve-time tangency rule | α_tan = 1.0e-3 rad at bend-adjacent junctions, recorded in v3's evidence and approximation text. Margin ≥ 5e3 over representation at UTM scale (probe); admitted kink force ≤ 1.1% of a 5° bend's wall resultant. | WORKING_ITEMS (T4-U2 design). Confirm in T4-U2's reference refutation and the T3-interface review. |
| **D-E** | Kinks between two straights, between the 64ε guard and α_tan | Keep them refused (`PRESSURE_REGION_NONCOLLINEAR`) in T4-U2. Revisit in T4-U7. Admitting them through the remainder would extend H-2 beyond "each interior node next to a bend". | **ROOT** (H-2's scope) |
| D-F | New authoring writes v3 | Enforce it in the applier: refuse none→v2 and v3→v2; allow an explicit v2→v3 upgrade, including a contract-only upgrade on 0.4.0. | WORKING_ITEMS (implements H-1) |
| D-G | k is user data | The new operations, and `set_field` on k, refuse `author_type: "agent"`. This narrows an agent capability that no fixture uses. | WORKING_ITEMS (implements D-2's rationale) |
| D-H | Tangency at authoring | Blocking at single-neighbour span ends, warning at tee ends; corner insertion is exact by construction. | WORKING_ITEMS |
| D-I | Shared definitions | T4-U1 puts `arc_geometry(d, R, y_reference)` and `kink` in CB (square roots only, node-relative). PP re-exports them with the tolerance constants, and the applier uses them through PP. No manifest or lock changes. | WORKING_ITEMS, with T4-U1's implementer. A T3-interface item because it is formation. |
| D-J | v3 identity in the authoring layer | T4-U2a adds the v3 constants and `isExactPressureContract` in TS and in the applier, with no behaviour change, so that lanes P and J share them. | WORKING_ITEMS |
| D-K | CI selection | Add the new e2e spec to `e2e_plan.py`'s authoring selection. Compact coverage comes from the manual dual-viewport dispatch. | WORKING_ITEMS |

## Sequencing (design §6)

- **A1–A6** need only T3's U3 merged:
  - A4 and A5, realize-bend with its tangency check, also wait for T4-U1's shared arc function;
  - A3 lands with T4-U1's `validation.rs` change.

  These steps work on today's contract, since preview-physics-1 already solves realized bends.
- **B1–B2** follow T4-U2a's v3 identity.
- **C1** follows T4-U2's PP admission and its readers: the v3 e2e, the native round trip, blank 0.4.0 under v3, the witness.

Lane-J overlap with T4-U3 is in `componentIntent.ts`, `PropertyInspector.tsx`, component creation in `AP/lib.rs`, `validation.rs` and `types.ts`. Keep T4-U2's logic in new files and small hunks.

## Files

`R4/T4-I11/AUTHORING_DESIGN.md`, `RETURN.md`, `_run_records/tangency_probe.py`, `_run_records/tangency_probe.stdout.txt`, `SHA256SUMS`. Scratch only under `WT/scratch/t4_T4-I11/` (a read-only extract of `ed012c7ccf`).
