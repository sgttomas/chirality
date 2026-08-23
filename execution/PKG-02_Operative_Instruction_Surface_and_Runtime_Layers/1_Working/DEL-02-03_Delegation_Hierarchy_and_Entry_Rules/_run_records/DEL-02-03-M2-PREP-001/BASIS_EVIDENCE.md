# Basis and Precondition Evidence

Status: `OBSERVED — PREPARATION ONLY`

Observed on 2026-08-22 from the Root worktree at accepted run basis
`main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`.

| Check | Result |
|---|---|
| `git cat-file -t 13201dfe7dc3b97c9aa36f6305cae604b48ef80f` | `commit` — the manifest basis resolves as a commit (TM-ROOT-127). |
| `git cat-file -t 6b0c5219b6a2653e2fc491b1d998abcf78fcf776` | `commit` — the managed-run accepted basis resolves as a commit. |
| DEL-02-03 `ScopeOfWork.md` SHA-256 | `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f` — matches the steer. |
| DEL-02-03 `_STATUS.md` SHA-256 before N2 writes | `9fdd785881eef6ee4f210bcb381dedd757c5748f939743038541dd9e894cbdfa`. |
| Root `AGENTS.md` SHA-256 | `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb` — unchanged basis bytes. |
| N1 `AGENTS.proposed.patch` SHA-256 | `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee` — matches the accepted N1 return and cycle-3 review. |
| Owner G0 record SHA-256 | `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`. |
| Owner Root Phase-0 steer SHA-256 | `c348e9767db4af20787bbcb74c64791ef08d700b08dc19d86289a88a58f067e3`. |

The manifest uses `13201dfe7dc3b97c9aa36f6305cae604b48ef80f`
exactly as directed even though the managed N2 execution basis is the later
`6b0c5219b6a2653e2fc491b1d998abcf78fcf776`. The former is the Revision 3.1
and owner-G0 planning basis; the latter is the accepted branch state for this
preparation run. This distinction is recorded, not reconciled by inference.
