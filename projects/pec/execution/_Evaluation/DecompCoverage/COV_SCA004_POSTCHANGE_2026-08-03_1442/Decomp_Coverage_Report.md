# Decomposition Coverage Report — SCA-004 post-change

**Variant:** `SOFTWARE` · **Decomposition:** revision **1.4** · **Scope:**
`ALL` · **Status:** `WARNINGS` (0 blockers / 1 warning / 69 info).

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS` — 11/11 |
| 2 | Forward deliverables | `PASS` — 64/64 |
| 3 | Reverse coverage | `PASS` — no reverse-only folder |
| 4 | ID consistency | `PASS` |
| 5 | Context fidelity | `PASS` — 64/64, including DEL-01-06 successor mirror |
| 6 | Artifact presence / contract shape | `WARNING` ×1, `INFO` ×60; unchanged from baseline |
| 7 | Objective mapping | `PASS`; all six objectives supported; `INFO` ×9 accepted residue |
| 8 | Ledger integrity | `PASS` — 94 rows, all 72 IN package/deliverable refs resolve |
| 9 | Derivative parity | `SKIPPED` — not SOFTWARE-variant-owned |
| 9b | Package-shape conformance | `PASS` |
| 10 | Active snapshot / handoff sequencing | `PASS` — candidate complete-before-pointer sequencing observed; final pointer parity separately required |
| 11 | Lifecycle distribution | `PASS` — 28 INITIALIZED / 32 OPEN / 4 CHECKING |

## Pre/post comparison

The intended delta is exact: SOW-077 moves TBD→IN and maps reciprocally to
PKG-01 / DEL-01-06 / OBJ-004; SOW-094's authority note changes; DEL-01-06's
description and covered-scope set change in place; OI-003 is retained and
resolved; revision becomes 1.4. Counts change from `71/14/9` to `72/14/8`,
PKG-01 from 7 to 8 mapped scope items, OBJ-004 from 10 to 11, and open/resolved
issues from 11/2 to 10/3.

No package, deliverable, objective, stable ID, filesystem path, lifecycle,
source byte, dependency row, execution edge, envelope, or phase changed. The
known DEL-08-02 artifact-location warning remains the only warning. There is
no blocker and no SCA-004-induced regression.

This snapshot is derivative audit evidence. It authorizes no downstream
repair and accepts no deliverable artifact.
