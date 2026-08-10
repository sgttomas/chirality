# Old-root preservation evidence

Status: `PASS — BYTE-PRESERVED; NOT USED AS CONTENT INPUT`

At closeout the manager mechanically enumerated every regular file under each
blocked attempt-3 root. For each root it sorted paths bytewise by root-relative
path, emitted exact lines
`path<TAB>size-bytes<TAB>sha256<LF>`, and SHA-256 hashed the concatenated line
bytes. No file content was surfaced or used as packet-authoring input.

| Root | Files | Bytes | Deterministic inventory SHA-256 |
|---|---:|---:|---|
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_2026-08-09/` | 34 | 119383 | `06e0b64516e691820803c4cb6f0b3961004ff03d5a7c1685802cafbba1c81c4e` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_V2_2026-08-09/` | 20 | 89845 | `c7ff055ae257dfcec4ccbae24251da66321b0a6d06573ef38e9b78e043bf4ea4` |

Read-only Git checks report no tracked, staged, or untracked delta under either
root and both roots match the index and committed HEAD. The recorded v2 blocked
supporting-draft constraint remains exactly nine objects, 59,460 bytes, digest
`9c2af5f241c83d9d0a5ba03d5968c010e431790402eca13d45d43c5c5c8bd9e9`
per its allowed terminal manager-validation record. This run did not open or
semantically inspect those nine objects.
