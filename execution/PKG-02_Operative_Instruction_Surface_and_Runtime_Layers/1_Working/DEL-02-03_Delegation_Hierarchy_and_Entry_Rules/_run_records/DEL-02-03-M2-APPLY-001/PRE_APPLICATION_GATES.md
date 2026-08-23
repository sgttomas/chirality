# Pre-Application Gates

Status: `PASS`

Observed from the Phase-0b branch at
`b143444bd497eae1b1b638670a33e6df756d9084` on 2026-08-22.

| Gate | Result |
|---|---|
| `git cat-file -t 13201dfe7dc3b97c9aa36f6305cae604b48ef80f` | `commit` — historical draft-manifest basis resolves (TM-ROOT-127). |
| Branch basis | `origin/main` and branch `HEAD` both resolved to `b143444bd497eae1b1b638670a33e6df756d9084`; PR #620 merge `abf3c1bf5996cd9333ad706df14e62df32fbbf0f` is an ancestor. |
| Pre-application `AGENTS.md` SHA-256 | `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb` — PASS. |
| `AGENTS.proposed.patch` SHA-256 | `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee` — PASS. |
| Literal `git apply --check docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch` | PASS; no output before application. |
| R1-A / R1-B authority | Owner record `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`, SHA-256 `a9879a87faaeb4cd4d5f16b2b4b0364543dff117e1b51c7e17d1efdcb20f377d`. |
| DEL-02-03 `ScopeOfWork.md` SHA-256 | `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f` — PASS and unchanged after application. |
| DEL-02-03 pre-application `_STATUS.md` SHA-256 | `9fdd785881eef6ee4f210bcb381dedd757c5748f939743038541dd9e894cbdfa`. |
| Historical N2 draft manifest SHA-256 | `59f0ed42ce498a6d3fbed9148b70691a0e4ceda49e37c890ed8391c4861ef7da` — unchanged; its `basis: 13201dfe7...` remains historical run evidence. |

These gates authorized only the bounded application candidate. They did not
authorize self-merge, merge, release, reliance, lifecycle acceptance, or a
hold lift.
