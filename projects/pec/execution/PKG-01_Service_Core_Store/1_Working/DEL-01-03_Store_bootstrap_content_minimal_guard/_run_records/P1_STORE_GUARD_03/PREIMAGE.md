# PREIMAGE — P1_STORE_GUARD_03 (D-PEC-89 A)

Observed 2026-09-24 by WORKING_ITEMS on a worktree whose HEAD is fetched
`origin/main` `9ffc54afcaa287d1b5fdc57dcda2194f6f1e0abf` (merge of PR #895,
carrying `D-PEC-89_RULING_2026-09-24.md` and the D-PEC-89 register row).
Command: `shasum -a 256 <path>` from `projects/pec/`.

| Path (relative to `projects/pec/`) | Opened | Proposal rollback-table SHA-256 | Observed | Match |
|---|---|---|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | yes | `d63932c28dd346581deb0b04bb14841f00eff9481432a379ce67dd8e9d626b33` | `d63932c28dd346581deb0b04bb14841f00eff9481432a379ce67dd8e9d626b33` | yes |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | yes | `05b9846a2baa9a5fe2691196d83d35770b8227f8b653f39c3831dcd4b89eae0a` | `05b9846a2baa9a5fe2691196d83d35770b8227f8b653f39c3831dcd4b89eae0a` | yes |
| `v2/tests/storage/test_content_minimal_guard.py` | yes | `c8e23563c226585c9f557d0c7d14eb880232452ab30541fa034a643afd561c29` | `c8e23563c226585c9f557d0c7d14eb880232452ab30541fa034a643afd561c29` | yes |
| `v2/tests/storage/test_store_lifecycle.py` | yes | `edbd41df5e05573d9992ee9778aba053570b4de6d4a0bf392ff7a888ff42cadf` | `edbd41df5e05573d9992ee9778aba053570b4de6d4a0bf392ff7a888ff42cadf` | yes |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | yes | `e9d65fc77ae3009a3d362eb34c8de527350456fcd7bc7670ef9e95ff9641ed35` | `e9d65fc77ae3009a3d362eb34c8de527350456fcd7bc7670ef9e95ff9641ed35` | yes |
| `v2/src/pec_v2/core/ports/store.py` | no; must remain | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` | yes |
| `v2/src/pec_v2/adapters/storage/__init__.py` | no; must remain | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` | yes |
| `software-workflow.json` | no; must remain | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` | yes |

All eight match. Administrative preimages (not product). `_STATUS.md` is not
touched by this slice; its hash is recorded so its invariance can be checked.

| Path (relative to the DEL-01-03 folder) | Observed SHA-256 |
|---|---|
| `_STATUS.md` | `d9429b4e14f60343dbd9827a0e0a93c99359d8fb64b96c0a612cc7d5dd56555b` |
| `MEMORY.md` | `4e16a24b37b0a74ba3e12247eea6b091f6ad72b3c6abe292dc21d02c4a8a0395` |

## Reliance-hold preflight (dispatch-for-production)

Register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`
SHA-256 `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`
(header only, no rows). Script
`projects/pec/execution/_Scripts/pec_reliance_hold.py` SHA-256
`b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`.
Run from `projects/pec/` as
`python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <path> --operation dispatch-for-production`
for each of the five opened paths. All five returned
`{"operation": "dispatch-for-production", "status": "ALLOW"}`, exit 0.
Interpreter `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
Python 3.13.7.
