# App-Notice Claim Drift Check — N1 Notice Ingestion

- **Run:** `ROOT_NOTICE_INGESTION_2026-09-03`
- **Instance:** `N1_NOTICE_INGESTION`
- **Basis:** `8140daec7ab7165f8972451dbdd3a67b8bb2fd38` (PR #680 merge; `HEAD` = `origin/main`)
- **Checked UTC:** `2026-09-03T19:27:01Z`
- **Verdict:** `NO_EXACT_DIVERGENCE`

Every SHA-256 below was recomputed from live bytes at the basis with
`shasum -a 256`; Git facts were observed with `git`/`gh`. Nothing was
repaired, adopted, or amended.

## Basis and copy identity

| Object | Observed | Required | Result |
|---|---|---|---|
| PR #680 state / merge commit | `MERGED` / `8140daec7ab7165f8972451dbdd3a67b8bb2fd38` | `MERGED`; merge = branch basis | `MATCH` |
| `origin/main` and `HEAD` | `8140daec7ab7165f8972451dbdd3a67b8bb2fd38` | equal to the merge commit | `MATCH` |
| Merge parents | `1537ddad1f9227dee1ba3233c0146694a779026a`, `795900e5ad66758cab8db8e3a7e53df5f9233fcb` | first parent = PR #679 merge (the notice's stated basis) | `MATCH` |
| Source notice (App surface) | `b68ed592b310fa996bb10d2aaf6889a25eb0481e6a57ce3fb2e414b775e4ee2b` (5228 bytes) | exists on the basis; SHA recomputed | `MATCH` |
| Destination notice (Root surface) | `d7eb52af3fd3833b6af949e218c6c90b7566a751c90331fa643a1cc86bc40d78` (7357 bytes = 2129-byte header + 5228-byte body) | header + byte-identical body | `BODY_BYTE_IDENTICAL` (`tail -c 5228 \| cmp` exit `0`) |
| A11 | `6197bae1aad25e6fd7dfa6befb0212acb5da24654f49f97536dbc2d365aeca27` | same (task-stated) | `MATCH` |

## Claim-by-claim check of the App notice

| # | App-notice claim | Live observation at basis | Result |
|---|---|---|---|
| 1 | Answers Root notice `NOTICE_2026-08-03_ROOT_TM-ROOT-122_ELECTRON_AUTHORITY_DRIFT.md`, SHA-256 `f806474b…d5951e` | `f806474b4500b2b081a49d759a0c0793fe65bce860d7efd146147abc38d5951e` | `MATCH` |
| 2 | Authorizing App ruling A11, SHA-256 `6197bae1…eca27` | `6197bae1aad25e6fd7dfa6befb0212acb5da24654f49f97536dbc2d365aeca27` | `MATCH` |
| 3 | Candidate source `ELECTRON_DRIFT_DISPOSITION_CANDIDATE.md`, SHA-256 `f9008f3c…9cca0` | `f9008f3cd2076e38572fc849c749c82aa8afbeec1863353944f721d4a3e9cca0` | `MATCH` |
| 4 | D-APP-98 SHA-256 `71dfc1ae…c020`, records Electron `43.2.0` as App authority and D-APP-72 successor for that single fact | `71dfc1ae6369acea1e49f71d68e45aaf9da8f14c5f6a77733845c43f3ee7c020`; ruling text: "Electron `43.2.0`, as pinned in `frontend/package.json` on `main`, is the App's recorded Electron authority and the D-APP-72 successor for that single fact." | `MATCH` |
| 5 | D-APP-72 (`43.1.1`, historical) SHA-256 `c7dcbb5a…6577` | `c7dcbb5aaa0f82481fb76825c7099c4e355c4ada80232c51f3a3cf6ba2076577` | `MATCH` |
| 6 | `frontend/package.json` SHA-256 `17c87d52…ad0cc`, pins `43.2.0` | `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc`; line 68 `"electron": "43.2.0"` | `MATCH` |
| 7 | Lockfile agrees on `43.2.0` | `frontend/package-lock.json` line 40 `"electron": "43.2.0"` | `MATCH` |
| 8 | `frontend/scripts/verify-electron-dist.mjs` SHA-256 `e4e9aa12…8457`; frozen supply `electron-v43.2.0-darwin-arm64.zip`, size `122090802`, SHA-256 `ad4a0ae3…ffe28` | `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`; lines 9–12: `version: '43.2.0'`, `filename: 'electron-v43.2.0-darwin-arm64.zip'`, `size: 122090802`, `sha256: 'ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28'` | `MATCH` |
| 9 | Content commit `cd45390a…8c55` on branch `codex/app-electron-concordance-2026-09-03`, basis `1537ddad…026a` | `cd45390ae3331ea2748f5df5d934922ec90e8c55` and `1537ddad1f9227dee1ba3233c0146694a779026a` are both ancestors of `HEAD`; PR #680 head branch was `codex/app-electron-concordance-2026-09-03` | `MATCH` |
| 10 | `docs/CONTRACT.md` post-image `51ec0d48…8517` | `51ec0d4872dd1eba7921e9419231c0d3dc1b3fb368fe6040623a28a16f788517` | `MATCH` |
| 11 | `docs/DIRECTIVE.md` post-image `50b816d5…6099` | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | `MATCH` |
| 12 | `docs/PLAN.md` post-image `3741bb7e…5187` | `3741bb7ec389c12f0856cf64acc27d4d17b77d1683275564b75182fcdbab5187` | `MATCH` |
| 13 | `docs/SPEC.md` post-image `c2fb9ecb…a12b` | `c2fb9ecbbc37a98577a64a3e7e641de8c26b3145ad8cc40dc4a9a014aa66a12b` | `MATCH` |
| 14 | `docs/PRD.md` post-image `87ced649…c586` | `87ced649beae245e7b0290b3ef8afb46681d04e671964a0583fdce83a7ccb586` | `MATCH` |
| 15 | `docs/TYPES.md` post-image `a8cdc94d…d56c` | `a8cdc94d39e16271ec4ef7fde5be76969f23ca3fe9e1663ac53ad1915eefd56c` | `MATCH` |
| 16 | `docs/VALIDATION_STRATEGY.md` post-image `37b6d1da…ea73` | `37b6d1da8af4ace680673af7a22621b076c0138fcbebf6db897d98c9fbee9a73` | `MATCH` |
| 17 | `docs/harness/reliance_boundary_register.md` post-image `5e53c5bd…0b6b` | `5e53c5bd18ceefd164a8ab3003f0c3ce174b412ef534da4ccf18cbb16950eb6b` | `MATCH` |
| 18 | Authority corpus v19 SHA-256 `eaec3c0a…10ef` (pre-image) | `AUTHORITY_CORPUS.json` at the merge's first parent `1537ddad…` recomputes to `eaec3c0a3a1b7bf76a9a3ec922bf826772e9097441d5631126cb7a5e025e10ef` | `MATCH` |
| 19 | Authority corpus v20 SHA-256 `8b5b5d21…b3b4`, dated 2026-09-03, reason "D-APP-98 Electron authority concordance (A11 E2)" | `8b5b5d21287144a03fdd5c204f0c473219d3f183f58974c6679c368c2e21b3b4`; `current_version` = `v20`; date string and reason string present in the file | `MATCH` |
| 20 | "The final identity of this concordance is the merge commit that lands the branch on `main`", unnamed | PR #680 merge commit `8140daec7ab7165f8972451dbdd3a67b8bb2fd38`, recorded in the Root ingestion header | `SUPPLIED_BY_ROOT_HEADER` |

Claims about the corpus tool "reporting no drift and no mismatched rows" and
about the reconciliation of every deliverable `_REFERENCES.md` are App-side
process claims recorded by the App loop; they were not re-executed here and
are neither confirmed nor contradicted by this check. Root's act relies on
the recomputed identities above, not on those process claims.

## Precedent divergence recorded

The 2026-08-24 ingestion (Receipt 128) recorded a pure `/bin/cp` copy with
no header. R18 requires a Root ingestion header carrying the merge identity
and Root's adoption disposition, so this destination is header + body. The
body identity check above is the equivalent of the precedent's whole-file
identity check.

## Ledger and register disposition

The only Root artifact styled as a notice-status ledger remains the
historical `PROGRAM_ARCH_REMEDIATION_NOTICE_STATUS_2026-07-28.{md,csv}`
inventory; it is not a standing inbound-notice ledger and was not mutated.
Unlike R11, R18-B rules a register disposition: the `TM-ROOT-122` act is
performed in N2 under `TASK_MANAGEMENT` and recorded at
`execution/_Coordination/_TaskManagement/RULING_2026-09-03_ROOT_TM-ROOT-122_DISPOSITION.md`.
N1 itself writes no register byte.

## Blockers

None.
