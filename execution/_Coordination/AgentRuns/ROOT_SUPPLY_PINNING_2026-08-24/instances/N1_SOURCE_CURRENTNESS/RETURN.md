# N1 Return — Official Source and Documentation Currentness

Return: `PASS`

Completed: 2026-08-24

Basis: `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`

Candidate state: `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

## Findings

1. Official OpenAI documentation identifies Codex App Server with the `openai/codex` source repository.
2. Official `openai/codex` release `rust-v0.149.0` remains published, non-draft, and non-prerelease.
3. All three ruled macOS arm64 assets remain uploaded at the exact ruled names, byte sizes, SHA-256 digests, and release URLs.
4. Current official App Server, configuration-reference, and open-source Markdown pages were retrieved, hashed, and searched directly.
5. Current official configuration documentation names no dedicated curated-plugin synchronization switch. It documents general plugin MCP controls and `check_for_update_on_startup`, but describes the latter only as checking for Codex updates. This is a documentation-absence result; N3 must probe exact 0.149.0 behavior.
6. `openai/codex#37725` is open with three comments. No returned comment has `author_association` `OWNER`, `MEMBER`, or `COLLABORATOR`; therefore no maintainer-associated response is present in the retrieved issue thread. No claim is made about dispositions outside that thread.
7. No artifact was downloaded and no vendor code was executed.

## Exact ruled assets reverified

| Asset | Size | SHA-256 |
| --- | ---: | --- |
| `codex-app-server-aarch64-apple-darwin.tar.gz` | 71,843,308 | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` |
| `codex-app-server-aarch64-apple-darwin.zst` | 50,359,498 | `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677` |
| `codex-app-server-package-aarch64-apple-darwin.tar.gz` | 93,775,517 | `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2` |

## Output hashes

| File | SHA-256 |
| --- | --- |
| `01_SOURCE_IDENTIFICATION/OFFICIAL_DOC_CURRENTNESS.json` | `aa69d4727f3af0859bf695f974ec2ae5822a63b1a07727826c0d74d242a15be5` |
| `01_SOURCE_IDENTIFICATION/OFFICIAL_RELEASE_METADATA.json` | `d06aed81de71abeb0148fd961d5dc340ac751b8a8f13c688d817ca295c9ee8e6` |
| `01_SOURCE_IDENTIFICATION/SOURCE_IDENTIFICATION.md` | `67f3f5699329310356f837c0530f257d24f243ba7472a82f6e1fe40e3a940f2f` |
| `01_SOURCE_IDENTIFICATION/UPSTREAM_DEFECT_METADATA.json` | `45d275ff3105bdfac2bf3e9ec3b65fe880d17c6cf5255439e77d5b4470f1c690` |
| `instances/N1_SOURCE_CURRENTNESS/COMMAND_RECORD.md` | `32705e3b9ff1a3d276607dec37d9380486bcff44df4a0f8d60e4a7b50fcf9721` |

## Validation

- JSON parse of all three JSON evidence records: `PASS`
- Instrument SHA verification: `PASS`
- Release identity and three-asset exact-match gate: `PASS`
- Direct official-doc search and identity capture: `PASS`
- No artifact download / no vendor execution: `PASS`
- `git diff --check`: `PASS`
- Write-scope review: `PASS`; writes confined to the N1 instance and candidate `01_SOURCE_IDENTIFICATION/`

## Dependency release

N1 releases the exact-asset download/inventory nodes. N2/N2b must still verify downloaded bytes independently; N3 must probe exact 0.149.0 configuration and egress behavior under R14 containment.
