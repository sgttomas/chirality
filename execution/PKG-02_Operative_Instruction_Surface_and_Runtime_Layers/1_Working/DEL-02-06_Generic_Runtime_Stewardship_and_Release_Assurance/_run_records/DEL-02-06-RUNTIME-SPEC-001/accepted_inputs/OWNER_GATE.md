# Owner gate — fresh DEL-02-06 accepted-input candidate

Status: `FRESH CURRENT-BASIS CANDIDATE — NOT ACCEPTED — EXTERNAL EXACT-HASH GATE REQUIRED`
PacketCharacter: `FRESH_SYNTHESIS — NOT RECOVERED HISTORICAL BYTES`

## Gate subject

The gate subject is exactly the six-file candidate whose five content hashes
appear in `CANDIDATE_SET_MANIFEST.sha256`. The SHA-256 of the manifest bytes is
the candidate-set identity. The manifest does not hash itself.

Applied basis:

- accepted DEL-02-06 Scope of Work SHA-256
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`
- `Git HEAD 2b7a7d828e9173836e5b0a71fc015e4f45024215 with exact applied S5/S6 worktree bytes`
- PRD SHA-256 `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`
- decomposition SHA-256 `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`
- SCA Decision Log SHA-256 `d64272d9c25b3ee21d622a7dc16a5cc20dea0979252e0b899f189ff95a51f508`
- S5 applied validation SHA-256 `a8bbb5750bbdca7131700aa6c9d92936983f5387038f84cffe5400ab11a85bf8`
- SCA handoff SHA-256 `625f5e93c8e657785910e31bfc9e179d4aa83896e5e5f9fe1dca98119a9f23f6`
- S5 applied-file hashes record SHA-256
  `33ea624ad3396a15f1f242d0d7cebad8dba9a3e5704046d1a4b7f867723ff3de`
- fresh AUDIT_DECOMP return SHA-256
  `ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1`
- Gate 1 owner-confirmation record SHA-256
  `05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f`

## Acceptance meaning

Acceptance means only that the exact candidate bytes may be copied to the
RunID-local `accepted_inputs/` directory and consumed by fresh N0 as planning
inputs. It does not accept either semantic candidate as a runtime contract,
answer any open item, authorize N1–N6 automatically, or authorize runtime/
client implementation, profile adoption, dependency change, lifecycle,
release, reliance, register closure, Git merge, or foreign-loop work.

## External acceptance record

Acceptance is recorded outside the six-file packet at:

`packet_acceptance/PACKET_OWNER_ACCEPTANCE.md`

The exact acceptance line begins `ACCEPT DEL-02-06 INPUT PACKET`, followed by
one space, the exact lowercase 64-hex candidate-manifest SHA-256,
` — Ryan Tufts `, and the ruling date in ISO `YYYY-MM-DD` form.

This packet contains no owner token and claims no inferred acceptance.
Validation, file presence, commit, push, PR, or merge is not acceptance.

## Return and mutation rule

The owner may `ACCEPT`, `RETURN`, or `DEFER`. Any content edit after manifest
creation creates a different candidate, requires full revalidation and a new
manifest identity, and must be presented again. A mismatched or ambiguous
token has no effect.

The missing historical packet remains missing. This candidate begins a fresh
provenance chain and does not rewrite historical evidence.
