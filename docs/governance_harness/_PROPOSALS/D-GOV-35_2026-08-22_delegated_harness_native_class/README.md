# D-GOV-35 Proposal Packet — Delegated-Harness-Native Class

Status: `PROPOSED — AWAITING OWNER RULING`

Date: `2026-08-22`

Prepared by: `HELPS_HUMANS`, managed by `HELP_HUMAN`

Accepted preparation basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`

This is a candidate governed record. It does not amend `AGENTS.md`, the
ratified standards, App governance, App product source, or any downstream
loop. No delegation class becomes active through this packet's authorship,
validation, commit, push, or review. Only an owner ruling can adopt the
decision; a later authorized application tranche must perform the listed
propagation and validation.

## Packet inventory and SHA-256

| File | SHA-256 convention | SHA-256 |
|---|---|---|
| `D-GOV-35.proposed.md` | Exact file bytes | `924c1b098f1510bca9189e1ac06e4c2fd8e9d358a9fc3c4e42fdd04a53b69c88` |
| `AGENTS.proposed.patch` | Exact file bytes | `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee` |
| `IMPACT.md` | Exact file bytes | `565e651963b08f74622ca0e0d32b66d6d301c3ef95c159867b4e41a6fbd98435` |
| `README.md` | Normalized self-hash defined below | `59bd2cd2b3e8a0812e5d509f22d52009048b0314dd8cf9ec9c7a43efe524c32d` |

### README self-hash convention

The `README.md` row cannot truthfully carry the SHA-256 of its own exact bytes
without requiring an impossible recursive fixed point. Its table therefore
records a **normalized self-hash**: replace only the 64 lowercase hexadecimal
characters inside the backticks of the `README.md` table row with 64 ASCII
zeroes, preserve every other byte, and calculate SHA-256 over the resulting
bytes. The other three rows are ordinary exact-byte SHA-256 values.

## Validation posture

The packet is acceptable for owner review only when:

- the inactive section-anchored patch applies cleanly with the literal command
  `git apply --check`;
- basis `AGENTS.md` remains SHA-256
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`;
- the unchanged agent-instruction and instruction-entrypoint validators pass;
- candidate-whitespace validation against `origin/main` is clean; and
- the hashes above reproduce under their stated conventions.

Structural validation is evidence only. It is not semantic acceptance or an
owner ruling.

### Patch-context interpretation

Amendment N1 version 2 records that a conventional `-U0` unified hunk is
incompatible with Git's literal default check in this repository. The literal
`git apply --check` command controls. The patch therefore uses four minimal
hunks, with only the adjacent unchanged lines Git needs as anchors; every
anchor is inside `## Delegation and Entry Rules`, and there is zero unchanged
context outside that section. It does not delete and re-add unchanged rules to
manufacture context and does not claim to be a conventional `-U0` patch. No
proposed byte is applied to live `AGENTS.md` here.
