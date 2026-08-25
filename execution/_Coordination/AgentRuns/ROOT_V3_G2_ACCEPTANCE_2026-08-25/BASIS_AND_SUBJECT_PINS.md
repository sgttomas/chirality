# Basis and Subject Pins — R15 G2 Acceptance

Date: 2026-08-25

## Git and hosted-state basis

- `origin/main`: `baa29d22fa034784cda221b2929061213e83ec91`
- parents, in order:
  - `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`
  - `b46f41a858938f41e99f3e2abb487238b78ed875`
- merge tree: `bd5fdf75a4c03df9f920a396489a0348cb03431c`
- PR #673: `MERGED`, head `b46f41a858938f41e99f3e2abb487238b78ed875`
- PR #673 remote head branch: absent after `git fetch origin --prune`
- post-merge hosted `harness`: `PASS` in 1m18s

## Accepted packet preservation basis

- packet path:
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_run_records/APP-SERVER-0.149.0-G2-CANDIDATE-2026-08-24/`
- packet Git tree: `20469afce1081ec7da274a359474ddf390d979ec`
- packet file count: 96
- `G2_ACCEPTANCE_SHEET.md`:
  `cec83abc2fc39358037600c883dd7b55ad09b154140d68a4d86346c309cda5ae`
- `README.md`:
  `ff4ed9502b2b4ac843107cf14a9f5ff35983f6e9f70469f80610b960582bd897`
- `SUPPLY_MANIFEST.json`:
  `18a1fa0741b9d6d9466e2c5e4903aa9b87baab1b5259d6a1c2a36664d11ecc39`
- `SUPPLY_UNIT_CANDIDATE.md`:
  `238769718d71d62be8465d5d758c4fdacaf26a62da0aa60e471ce6e56de6890a`
- `CONFIG_METHOD_FEATURE_MATRIX.md`:
  `c44656398ca7d1b5bdf84dbd0be65b32d9f33cba1fc241e05e5ceeab76bfd58d`
- `SCHEMA_TYPES_METHOD_INDEX.md`:
  `d5620ffde7ff42ee824648dfee8c2e02d5f92d370786cf97a692d1bab75ec1cf`
- `OUT-002_ENDPOINT_INVENTORY.md`:
  `fd6bd4e4dd7c2a0dc477e567becd5d2d092514db36dfedaf2fa2a529798d9f47`
- `EVIDENCE_HASH_MANIFEST.csv`:
  `acbc96a61b35f6f5812ece08895586967ac571c5367753035d7def7d46a1ddfb`
- `04_REVIEW/REVIEW.md`:
  `b3bb1f1d2e496c6ed484943033c87fdc9737379cc6c37aac1c571d286e897de9`
- prior run handoff:
  `f470116910ae7432d0f0b634d206bca4edeb08699dbc9ec0b622bb413e6f6fd4`
- pre-transcription receipt ledger:
  `47a0c384578bff69629ca6cbbd94eabcd5625bc645d0f7c44e67706150e2c4b2`

The packet had no worktree diff from `origin/main` before transcription.

## Exact accepted asset identities

| Asset | Size (bytes) | SHA-256 |
| --- | ---: | --- |
| `codex-app-server-aarch64-apple-darwin.tar.gz` | 71843308 | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` |
| `codex-app-server-aarch64-apple-darwin.zst` | 50359498 | `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677` |
| `codex-app-server-package-aarch64-apple-darwin.tar.gz` | 93775517 | `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2` |

All three contain the 179721344-byte arm64 App Server payload at SHA-256
`b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`.

## Cumulative instrument identities

| Instrument | SHA-256 |
| --- | --- |
| `plans/steers/chirality_app_v3_supply_pinning_steer_root_2026-08-24.md` | `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391` |
| `plans/steers/chirality_app_v3_root_ruling_record_r12_2026-08-24.md` | `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd` |
| `plans/steers/chirality_app_v3_supply_resume_steer_root_2026-08-24.md` | `248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701` |
| `plans/steers/chirality_app_v3_root_ruling_record_r13_2026-08-24.md` | `0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960` |
| `plans/steers/chirality_app_v3_supply_resume2_steer_root_2026-08-24.md` | `38b76ca27defd39507f6d9cfe9501d392b1e9ade7c5f107cd67cb4ce420ef164` |
| `plans/steers/chirality_app_v3_root_ruling_record_r14_2026-08-24.md` | `2633637bd68c7f4cb54457a3547b2bcab8933f19e021abf558b1ef2463d1b5e9` |

## New transcription identities

- R15 record:
  `a8463a7f0392978325e8d25558332e72868271e9c4d99ac26c7425bb3a448301`
- owner-carried steer:
  `a0d14e05b7749c06605bdfce5d978058b4bea999569f94d0a918a5f2bad6eb76`

Every identity above was recomputed from repository bytes during this run.
