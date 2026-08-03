# Decomposition Coverage Report — SCA-004 pre-change

**Variant:** `SOFTWARE` · **Decomposition:** revision **1.3**
(`current_basis`) · **Scope:** `ALL` · **Status:** `WARNINGS`
(0 blockers / 1 warning / 69 info)

**Expected source:**
`projects/pec/execution/_Decomposition/_LATEST.md` revision 1.3
`current_basis`, supplemented by D-PEC-78 O-A and the confirmed SCA-004 Gate
1 intake. **Expected phase:** `SCA-004 Gate 2 pre-change baseline`.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS` — 11/11 |
| 2 | Forward deliverables | `PASS` — 64/64 |
| 3 | Reverse coverage | `PASS` — no reverse-only package or exact deliverable folder |
| 4 | ID consistency | `PASS` — all folder IDs equal declared IDs |
| 5 | Context fidelity | `PASS` — 64/64 current register mirrors |
| 6 | Artifact presence / contract shape | `WARNING` ×1, `INFO` ×60; 3/64 anticipated sets found; 32 valid `SOW_V1`, 32 absent at `OPEN`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives; `INFO` ×9 accepted unmapped-deliverable residue |
| 8 | Ledger integrity | `PASS` — 94 rows; all 71 `IN` package/deliverable references resolve |
| 9 | Derivative parity | `SKIPPED` — not variant-owned by SOFTWARE |
| 9b | Package-shape conformance | `PASS` — companion inventory and authority roles are explicit and consistent |
| 10 | Active snapshot / handoff state | `PASS` — SCA-003 remains uniquely active, complete, and honest; SCA-004 is separately identified as confirmed Gate 1 intake |
| 11 | Lifecycle distribution | `PASS` — 28 `INITIALIZED`, 32 `OPEN`, 4 `CHECKING` |

Optional comparison mode was not requested and is `SKIPPED`.

## Coverage and objective evidence

All declared packages and deliverables have matching filesystem folders, and
no undeclared exact folder was found. Every `_CONTEXT.md` agrees with
`Deliverables.csv`, including the software-specific `ContextEnvelope` field.

Objective support counts remain internally consistent: OBJ-001 20, OBJ-002
12, OBJ-003 12, OBJ-004 10, OBJ-005 7, OBJ-006 9. Nine deliverables and 11
`IN` rows remain intentionally unmapped residue; every objective has
filesystem-backed support. SCA-004's proposed successor mapping is not applied
or counted in this pre-change snapshot.

## Artifact and lifecycle evidence

Deliverable-local matching found the anticipated ADR set for `DEL-00-01`,
SPEC for `DEL-00-03`, and measurement-method/baseline set for `DEL-10-01`.
Sixty other absences remain informational at `OPEN` or `INITIALIZED`.

`DEL-08-02` is `CHECKING`, while its anticipated "Schema + compatibility
tests" set is not present inside its deliverable folder. The accepted schema,
compatibility test, and fixtures live under the separately authorized v2
source tree; this audit does not dispute those bytes or their acceptance. The
finding is solely the warning required by Check 6's folder-local rule.

## Active snapshot and handoff evidence

`_ScopeChange/_LATEST.md` resolves uniquely to
`SCA-003_2026-07-28_0824/`. The snapshot contains the required SCOPE_CHANGE
artifact set, and its `CLOSED_FOR_SCOPE_CHANGE_ONLY` handoff remains consistent
with the accepted revision-1.3 package. `_Decomposition/_LATEST.md` cites the
same `SOFTWARE_DECOMP.md` SHA-256
`3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.

The confirmed SCA-004 Gate 1 intake is cited as new amendment authority, not
misrepresented as the active accepted snapshot. It preserves topology and
proposes `SOW-077 → PKG-01 → DEL-01-06 → OBJ-004` plus OI-003 resolution.

## Findings and next action

No blocker or structural-coverage defect was found. The one warning is
non-blocking for Gate 2 impact assessment because SCA-004 does not amend
DEL-08-02 or depend on the physical co-location of its accepted source bytes.
SCOPE_CHANGE may consume this immutable snapshot as the pre-change baseline,
record the warning accurately, and complete the Gate 2 impact package.

The audit pointer remains unchanged by sealed-brief override.
