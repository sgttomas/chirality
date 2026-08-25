# N1 Official Source and Documentation Currentness

Status: `PASS`

Candidate state: `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

Retrieval date: 2026-08-24 (America/Edmonton)

Basis: `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`

## Authority

This record is bounded by the cumulative supply instruments:

- `plans/steers/chirality_app_v3_supply_pinning_steer_root_2026-08-24.md` — SHA-256 `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`
- `plans/steers/chirality_app_v3_supply_resume_steer_root_2026-08-24.md` — SHA-256 `248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701`
- `plans/steers/chirality_app_v3_supply_resume2_steer_root_2026-08-24.md` — SHA-256 `38b76ca27defd39507f6d9cfe9501d392b1e9ade7c5f107cd67cb4ce420ef164`
- R12 — SHA-256 `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd`
- R13 — SHA-256 `0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960`
- R14 — SHA-256 `2633637bd68c7f4cb54457a3547b2bcab8933f19e021abf558b1ef2463d1b5e9`

No artifact bytes were downloaded and no vendor executable was run by N1.

## Official source channel

Current official OpenAI documentation identifies Codex App Server as the interface used for deep product integrations and links its implementation to `openai/codex/codex-rs/app-server`. The official Open Source page likewise identifies the App Server source as living in the `openai/codex` repository. The exact-pin release channel is therefore the official repository's GitHub release:

- release: `https://github.com/openai/codex/releases/tag/rust-v0.149.0`
- release ID: `374028976`
- state: published, `draft=false`, `prerelease=false`
- published: `2026-08-20T21:04:55Z`

The release still offers all three exact ruled macOS arm64 assets:

| Asset | Size | Channel SHA-256 | State |
| --- | ---: | --- | --- |
| `codex-app-server-aarch64-apple-darwin.tar.gz` | 71,843,308 | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` | uploaded |
| `codex-app-server-aarch64-apple-darwin.zst` | 50,359,498 | `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677` | uploaded |
| `codex-app-server-package-aarch64-apple-darwin.tar.gz` | 93,775,517 | `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2` | uploaded |

This closes N1's version/currentness gate. N2 may download only these exact URLs and must independently verify sizes and digests before use.

## Current official documentation identities

The Markdown representations returned HTTP 200 with `content-type: text/markdown; charset=utf-8`. HTTP `Date` was `Tue, 25 Aug 2026 03:58:13 GMT` for App Server and Configuration Reference and `Tue, 25 Aug 2026 03:58:14 GMT` for Open Source (all 2026-08-24 America/Edmonton).

| Page | Retrieved URL | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Codex App Server | `https://learn.chatgpt.com/docs/app-server.md` | 98,321 | `9194fc63fd56b8f49bf16c5ecc672eb50a4bc9c08370f3289c183d2a1133844a` |
| Configuration Reference | `https://learn.chatgpt.com/docs/config-file/config-reference.md` | 91,395 | `6464159e3897bbda6c81871500497bf79de35c62d7dfd7af354b2a33a158f687` |
| Open Source | `https://learn.chatgpt.com/docs/open-source.md` | 3,701 | `1bd29ea9f6d4148fb7a01d528f4985dc20ec25f109ac500b9f109a032afd399f` |

The App Server page currently documents `config/read` and version-specific `generate-ts` / `generate-json-schema` generation. These current docs are a drift-comparison baseline, not proof that the exact 0.149.0 binaries expose every documented current command.

## Curated-plugin synchronization switch — documentation probe

Result: `NO_DEDICATED_SWITCH_DOCUMENTED`.

A direct, case-insensitive exact search of the current configuration-reference Markdown found:

- zero occurrences of `curated`, `curated-plugin`, `curated plugin`, `plugin sync`, `synchronization`, `api.github.com/repos/openai/plugins`, and `multi_agent_v2`;
- two occurrences of `check_for_update_on_startup`, whose documented meaning is checking for Codex updates on startup, not curated-plugin synchronization;
- general `plugins.*` controls for installed plugin MCP servers, but no setting described as governing catalog synchronization.

This is narrowly a current-documentation absence finding. N3 must probe the exact 0.149.0 configuration surface and report the exact switch, default, and readback—or that none exists—without inferring from documentation absence.

## Upstream signature-defect issue

`https://github.com/openai/codex/issues/37725` is open as retrieved, with three comments and no `closed_at` value. None of the three returned comments has GitHub `author_association` `OWNER`, `MEMBER`, or `COLLABORATOR`. The durable statement is therefore: no maintainer-associated response appears in the retrieved issue thread. This does not claim that OpenAI has made no disposition elsewhere.

The issue directly concerns checksum-verified 0.147.0 canonical CLI bytes. It records the failure class named by R13: Team ID `2DC432GLL2`, strict verification reporting `invalid signature (code or signature have been modified)`, an invalid-entitlements warning, and `spctl` failure. R13—not the issue by itself—authorizes admitting that same observed class on digest-exact 0.149.0 App Server bytes.

## N1 verdict

`PASS`: the official channel still offers exactly 0.149.0 in all three ruled packagings at the ruled identities; current official App Server, configuration-reference, and open-source documentation were identified and hashed; current official docs do not document a dedicated curated-plugin synchronization switch; issue #37725 remains open without a maintainer-associated response in the retrieved thread. No download or execution occurred.
