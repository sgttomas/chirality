# PREIMAGE — P1_STORE_GUARD_02 (D-PEC-87 C-A)

Observed 2026-09-24 by WORKING_ITEMS on a worktree whose HEAD is fetched
`origin/main` `6b4a0f59d292ed9f5f0ca222986ca95bc01bb0b6` (merge of PR #890,
carrying `D-PEC-87_RULING_2026-09-24.md` and the D-PEC-87 register row).
Command: `shasum -a 256 <path>` from `projects/pec/`.

| Path (relative to `projects/pec/`) | Proposal preimage | Observed | Match |
|---|---|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` | yes |
| `v2/src/pec_v2/core/ports/store.py` | `2f5cdbf50bb1ed8b02ce8b7d820f81b749da4ca2d62e195afec39c78a035a4af` | `2f5cdbf50bb1ed8b02ce8b7d820f81b749da4ca2d62e195afec39c78a035a4af` | yes |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` | yes |
| `v2/tests/storage/test_store_lifecycle.py` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` | yes |
| `v2/tests/storage/test_content_minimal_guard.py` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` | yes |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` | yes |
| `software-workflow.json` | `247eb82715356e1e3f532c577ff0c9babf39c18912b14362bdfb4fc8412f5d3a` | `247eb82715356e1e3f532c577ff0c9babf39c18912b14362bdfb4fc8412f5d3a` | yes |
| `v2/src/pec_v2/adapters/storage/__init__.py` (unopened) | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` | yes |

All eight match. Administrative preimages (not product; recorded for the L-1a
and MEMORY appends):

| Path (relative to the DEL-01-03 folder) | Observed SHA-256 |
|---|---|
| `_STATUS.md` | `73ae042e9204f1884642f74bced1a08a0c0166c6eeec321dbcf91ff08524e5a2` |
| `MEMORY.md` | `6dfbdd3d928cd2471b3f0e4fba84872624bb73cca50d4ad328e3f0f1cd0b15aa` |

## Reliance-hold preflight (dispatch-for-production)

Register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`
SHA-256 `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`;
script `projects/pec/execution/_Scripts/pec_reliance_hold.py` SHA-256
`b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`.
Run from the repository root with `--target projects/pec/<path>` for each of
the seven granted paths and the DEL-01-03 folder: all eight returned
`{"operation": "dispatch-for-production", "status": "ALLOW"}`, exit 0.
