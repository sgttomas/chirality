# Decomposition Coverage Report — SCA-002 post-change (final pass)

**Variant:** `SOFTWARE` · **Basis:** revision **1.2** (`current_basis`) ·
**Scope:** `ALL` · **Status:** `OK` (0 blockers / 0 warnings / 73 info)

| # | Check | Verdict |
|---|---|---|
| 1 | Forward coverage — Packages | `PASS` 11/11 |
| 2 | Forward coverage — Deliverables | `PASS` 64/64 |
| 3 | Reverse coverage | `PASS` 100% |
| 4 | ID consistency | `PASS` |
| 5 | Context fidelity | `PASS` 100% — all 64 `_CONTEXT.md` match the amended registers, including the 17 restated `SupportsObjectives` lines |
| 6 | Artifact presence | `INFO` ×64 — expected, all deliverables `OPEN` |
| 7 | Objective mapping | `PASS` + `INFO` ×9 — no unsupported objective; 9 residue deliverables intentionally unmapped under O-A |
| 8 | Ledger integrity | `PASS` — every IN row's package and deliverable refs resolve |
| 9 | Derivative parity | `SKIPPED` (non-DOMAIN) |
| 9b | Package-shape conformance | **`PASS`** — W-1 resolved by A007; §5 prose now agrees with the registers and §7 |
| 10 | Active snapshot / handoff state | **`PASS`** — `_ScopeChange/_LATEST.md` names exactly one snapshot (SCA-002) carrying the full required artifact set |
| 11 | Lifecycle distribution | `PASS` — 64 `OPEN` |
| 12 | Comparison | vs `COV_SCA002_PRECHANGE`: warnings 1 → 0; unmapped deliverables 26 → 9; package-shape `WARN` → `PASS` |

## Objective-evidence integrity — `PASS`

§3's objective-side view and `Deliverables.csv` agree exactly for all six
objectives after the amendment (OBJ-001 20, OBJ-002 12, OBJ-003 12, OBJ-004 10,
OBJ-005 7, OBJ-006 9).

## What to fix for a cleaner rerun

Nothing inside SCA-002's scope. Standing items: `OI-B` (64 `_REFERENCES.md`
still pin revision 1.1 — fence-excluded, deferred to resumed `PROJECT_SETUP`),
`OI-013` (no durable register validator), `OI-A` (agent binding-table drift).
