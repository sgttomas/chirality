# Decomposition Coverage Report — SCA-003 post-change final

**Variant:** `SOFTWARE` · **Decomposition:** revision **1.3**
(`current_basis`) · **Scope:** `ALL` · **Status:** `OK`
(0 blockers / 0 warnings / 73 info)

**Expected source snapshot:**
`/private/tmp/chirality-pec-sca003-exec/projects/pec/execution/_ScopeChange/SCA-003_2026-07-28_0824`.
**Expected phase:** Gate 5 final.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS` — 11/11 |
| 2 | Forward deliverables | `PASS` — 64/64 |
| 3 | Reverse coverage | `PASS` — no reverse-only package or exact deliverable folder |
| 4 | ID consistency | `PASS` — all folder IDs equal declared IDs |
| 5 | Context fidelity | `PASS` — 64/64 exact current register mirrors |
| 6 | Artifact presence / contract shape | `INFO` ×64; 32 valid `SOW_V1`, 32 absent at `OPEN`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives; `INFO` ×9 accepted unmapped-deliverable residue |
| 8 | Ledger integrity | `PASS` — 94 rows; all 71 `IN` package/deliverable references resolve |
| 9 | Derivative parity | `SKIPPED` — not variant-owned by SOFTWARE |
| 9b | Package-shape conformance | `PASS` — companion inventory and authority roles are explicit and consistent |
| 10 | Active snapshot / handoff state | `PASS` — SCA-003 is uniquely active, complete, and its limited closure claims match evidence |
| 11 | Lifecycle distribution | `PASS` — 32 `INITIALIZED`, 32 `OPEN` |

Optional comparison mode was not requested and is `SKIPPED`.

## Coverage and objective evidence

All declared packages and deliverables have matching filesystem folders, and
no undeclared exact folder was found. Every `_CONTEXT.md` agrees with
`Deliverables.csv`, including the SCA-003 descriptions for `DEL-00-01`,
`DEL-10-05`, and `DEL-10-12`. `DEL-10-12` retains its canonical
`Poll-adoption measurement` name and existing path.

Objective support counts remain internally consistent: OBJ-001 20, OBJ-002
12, OBJ-003 12, OBJ-004 10, OBJ-005 7, OBJ-006 9. Nine deliverables and 11
`IN` rows remain intentionally unmapped residue; every objective has
filesystem-backed support.

## Active snapshot and handoff evidence

`_ScopeChange/_LATEST.md` resolves uniquely to
`SCA-003_2026-07-28_0824/`. The snapshot contains all required artifacts:
Brief, impact assessment, amendment preview/actions, propagation plan,
decision log, pre/post coverage records, supersession map, handoff state, and
run summary.

Its closure is accurately limited to `CLOSED_FOR_SCOPE_CHANGE_ONLY /
REGEN_ONLY`: excluded ScopeOfWork contracts and `_REFERENCES.md` remain
downstream regeneration/re-pin obligations; dependencies, lifecycle,
implementation, and `PEC-HOLD-001` remain unchanged; production reliance is
not released. `_Decomposition/_LATEST.md` and the SCA snapshot both cite the
current `SOFTWARE_DECOMP.md` postimage SHA-256
`3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.

## Issues and next action

The 73 findings are informational only: 64 anticipated production artifact
sets absent at pre-production states and nine accepted unmapped
deliverables. No structural remediation is required. SCOPE_CHANGE may copy
this final summary into `Post_Change_Coverage.json`, finish its immutable
snapshot record, and proceed to CHANGE closeout without widening scope.
