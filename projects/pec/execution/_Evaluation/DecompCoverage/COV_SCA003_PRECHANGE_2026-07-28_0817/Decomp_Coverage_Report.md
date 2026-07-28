# Decomposition Coverage Report — SCA-003 pre-change

**Variant:** `SOFTWARE` · **Decomposition:** revision **1.2**
(`current_basis`) · **Scope:** `ALL` · **Status:** `OK`
(0 blockers / 0 warnings / 73 info)

**Expected source:** `origin/main@23b3b07d1122ae065affe69346c53bac78289a2e`
containing D-PEC-68 merge `ec3bec922e2e62e32fb283c5873b28b2bb9c510e`.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS` 11/11 |
| 2 | Forward deliverables | `PASS` 64/64 |
| 3 | Reverse coverage | `PASS` |
| 4 | ID consistency | `PASS` |
| 5 | Context fidelity | `PASS` 64/64 |
| 6 | Artifacts / contract shape | `INFO` ×64; 32 valid SOW-v1; no ambiguity |
| 7 | Objective mapping | `PASS` + `INFO` ×9 accepted residue |
| 8 | Ledger integrity | `PASS` |
| 9 | Derivative parity | `SKIPPED` (non-DOMAIN) |
| 9b | Package shape | `PASS` |
| 10 | Active snapshot / handoff | `PASS` — exactly SCA-002, complete and honest |
| 11 | Lifecycle | `PASS` — 32 `INITIALIZED`, 32 `OPEN` |
| 12 | Comparison | `SKIPPED` — no prior label |

Objective support counts agree with the decomposition: OBJ-001 20, OBJ-002
12, OBJ-003 12, OBJ-004 10, OBJ-005 7, OBJ-006 9. The 11 `IN` ledger rows
and 9 deliverables without objective mappings match revision-1.2 telemetry.
Active md5s match `_Decomposition/_LATEST.md`: decomposition
`961e8e959b7d1965cd1d4153c69a9c43`, deliverables
`3f807d502df3ed1f35326baed890832a`, ledger
`9ece6f49fb5fc7f83f72fa897d01a325`.

Top informational issues: anticipated production artifacts are not yet
present; nine deliverables remain intentionally unmapped; semantic
D-PEC-68/PRD-v2.2 concordance remains for SCA-003 intake rather than this
structural audit. Rerun after the authoritative amendment and propagation.
