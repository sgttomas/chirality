# PREIMAGE — P1_STORE_GUARD_04 (D-PEC-91 A-53)

Observed 2026-09-25 by WORKING_ITEMS on a worktree whose HEAD is fetched
`origin/main` `8b6553850aa8a98cb44aed02e9fe91e23b1234bd` (merge of PR #902,
carrying `D-PEC-91_RULING_2026-09-25.md` and the D-PEC-91 register row).
Command: `shasum -a 256 <path>` from `projects/pec/`.

| Path (relative to `projects/pec/`) | Opened | Proposal rollback-table SHA-256 | Observed | Match |
|---|---|---|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | yes | `2cb21e2d251eeffd164d68ad436cb0b9f0d4b8fdabd41358f33a0d7ed40122b3` | `2cb21e2d251eeffd164d68ad436cb0b9f0d4b8fdabd41358f33a0d7ed40122b3` | yes |
| `v2/tests/storage/test_content_minimal_guard.py` | yes | `3a4c98b32b1e4e07f921d7b567120377c63b7e526e0322480216346828ae8cba` | `3a4c98b32b1e4e07f921d7b567120377c63b7e526e0322480216346828ae8cba` | yes |
| `v2/tests/storage/test_store_lifecycle.py` | yes | `96d9917d6283eeb8fd6310991cd0166ecd24bcf76afccae840afee508ec2fb64` | `96d9917d6283eeb8fd6310991cd0166ecd24bcf76afccae840afee508ec2fb64` | yes |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | yes | `1fc417fc6b5461bd0623780e751bf37354df491f3f28e713b98c7d29417130a3` | `1fc417fc6b5461bd0623780e751bf37354df491f3f28e713b98c7d29417130a3` | yes |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | no; must remain | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` | yes |
| `v2/src/pec_v2/core/ports/store.py` | no; must remain | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` | yes |
| `v2/src/pec_v2/adapters/storage/__init__.py` | no; must remain | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` | yes |
| `software-workflow.json` | no; must remain | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` | yes |

All eight match. Administrative preimages (not product). `_STATUS.md` is not
touched by this slice; its hash is recorded so its invariance can be checked.

| Path (relative to the DEL-01-03 folder) | Proposal SHA-256 | Observed SHA-256 |
|---|---|---|
| `_STATUS.md` | `d9429b4e14f60343dbd9827a0e0a93c99359d8fb64b96c0a612cc7d5dd56555b` | `d9429b4e14f60343dbd9827a0e0a93c99359d8fb64b96c0a612cc7d5dd56555b` |
| `MEMORY.md` | `54f57151e5ad1a3b6d72b2f7ccc23bfae2a9fc567da7d10daf9feee0db0c2b14` | `54f57151e5ad1a3b6d72b2f7ccc23bfae2a9fc567da7d10daf9feee0db0c2b14` |

## Reliance-hold preflight (dispatch-for-production)

Register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`
SHA-256 `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`
(header only, no rows). Script
`projects/pec/execution/_Scripts/pec_reliance_hold.py` SHA-256
`b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`.
Run from `projects/pec/` with `PYTHONDONTWRITEBYTECODE=1` as
`python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <path> --operation dispatch-for-production`
for each of the four opened paths. All four returned
`{"operation": "dispatch-for-production", "status": "ALLOW"}`, exit 0.

Host: interpreter `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
Python 3.13.7 (CPython), SQLite library 3.50.4, `id -u` 501.
