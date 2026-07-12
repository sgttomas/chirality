# PKG-02 package summary — Desktop Shell, Navigation and Operator State

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; derived by the orchestrator
  at W1 fan-in from the claim ledgers (plan §7 — a deliverable/package summary
  is derived from claim rows, never a separate verdict).
- **Ledgers:** `R0_CALIBRATION/DEL-02-01_claims.csv` (R0, 21 rows, bound at
  `4c8ed8907`; frontend byte-identical through `fac46e33f`/`052b3c2b2`) +
  `R2_WAVES/PKG-02/DEL-02-0{2,3,4,5}_claims.csv` (W1, 86 rows, bound at
  `fac46e33f`). Verification pass: `R2_WAVES/PKG-02/_VERIFICATION.md`
  (34 rows rechecked; 1 refutation accepted; zero contested).

> **Epistemic status: immutable, source-state-bound evidence artifact — not a
> queue, not authority.** All dispositions are agent judgments.

## Census (5 deliverables, 107 claim rows)

| Disposition | 02-01 (R0) | 02-02 | 02-03 | 02-04 | 02-05 | Total |
|---|---|---|---|---|---|---|
| ALIGNED | 9 | 14 | 18 | 14 | 16 | 71 |
| STALE_SPECIFICATION | 5 | 3 | 2 | 2 | 1 | 13 |
| REMAINING_STATE_MISMATCH | 0 | 1 | 1 | 2 | 3 | 7 |
| IMPLEMENTED_UNDOCUMENTED | 3 | 2 | 2 | 0 | 1 | 8 |
| PARTIALLY_IMPLEMENTED | 0 | 0 | 0 | 3 | 0 | 3 |
| STALE_VERIFICATION | 1 | 0 | 0 | 1 | 0 | 2 |
| STALE_ASSESSMENT | 2 | 0 | 0 | 0 | 0 | 2 |
| IMPLEMENTED_DIFFERENTLY | 1 | 0 | 0 | 0 | 0 | 1 |
| AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW | 0 | 0 | 0 | 0 | 0 | 0 |

## Package-level picture

1. **The behavioral core is current and evidenced.** 71/107 rows are ALIGNED
   with implementation + verification evidence bound to the reviewed source
   state; every INSP-03 PARTIAL that was re-derived traces to pre-pivot
   wording or since-landed work, not to live defects.
2. **The dominant defect class is documentation lag, in two shapes.**
   (a) 13 STALE_SPECIFICATION rows: pre-pivot three-pane/WORKBENCH-routing
   wording (D-APP-28/31/32 loop-first pivot) and "Dependencies.csv
   deferred/not produced" deferral text contradicted by live registers; the
   PRD/TYPES portion is one shared owner-gated corpus-amendment packet
   (parked to R4 per Receipt 16), not per-deliverable repairs.
   (b) 7 REMAINING_STATE_MISMATCH register defects: the REF-006 (docs/PRD.md)
   hash-mismatch state resolved by D-APP-35/D-APP-38 still recorded as
   live in `Dependencies.csv`/`_DEPENDENCIES.md` surfaces, plus TBD-stub and
   traceability lags — all evidence-resolvable R5 metadata repairs.
3. **Unowned implemented surface (8 IMPLEMENTED_UNDOCUMENTED rows):** `/chat`
   surface (02-01); Pipeline scaffold UI and contract/lifecycle panel (02-02 —
   DEL-07-02's spec explicitly excludes the UI layer, so the surface has no
   documented owner anywhere); file-tree auto-refresh and symlink leaf
   handling (02-03); API-key remove/reveal controls (02-05). All routed as
   scope-adoption questions (plan §3 boundary 1), none silently adopted.
4. **Real requirement gap (one product decision):** the Toolkit exposes no
   mode/persona control while the runtime supports both (02-04 REQ-003/REQ-009,
   one underlying gap despite two rows); PRD FR-041's requirement-vs-acceptance
   wording split (docs/PRD.md line 543) is the fact to adjudicate.
5. **Verification texture:** the D-APP-36 render-test gap persists for
   specific surfaces only (AppShell keyboard/separator behavior — 02-04
   REQ-002 STALE_VERIFICATION; FileTreePanel, ShellFrame working-root bar,
   clear-disables states; Toolkit panel density REQ-014). Static render
   coverage that INSP-03 reported missing now exists for pipeline-surface and
   agent-matrix-panel.

## Cross-package flags for R3

- Same-surface double claim: `agent-matrix.tsx` deliverable rows
  (02-01 UNMAPPED-3 vs 02-03 REQ-009).
- Symlink read-tree ownership open until the PKG-07 wave (W3).
- The recurring PRD FR-005/FR-008/TYPES §4.1 pre-pivot wording appears in
  rows of 02-01, 02-02, and 02-04 — count once.
- Requirement-ID style divergence (02-05 uses spec-native `R01..R10`) and the
  run-local `HumanDecisionNeeded = NEW-PACKET` convention — R3 terminology
  sweep items.

## Unknowns / conflicts

None open in this package: zero AUTHORITY_CONFLICT, zero UNKNOWN, zero
DEFERRED_AGENT_WORKFLOW rows; zero contested fan-in verdicts.
