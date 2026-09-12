# D-GOV-43 Proposal Packet — Codex Host Re-platform

Status: `PROPOSED — AWAITING OWNER RULING`

Date: `2026-09-11`

Prepared by: `HELP_HUMAN`, Chirality v3 Codex-only MVP trial session

Accepted preparation basis: `main@a75adecf13f055c092ffa92809f66e7817c44242`

This is a candidate governed record. It does not amend `AGENTS.md`, the
ratified standards, Runtime or App governance, product source, packaging,
installations, trial evidence, or any downstream loop. Nothing becomes active
through this packet's authorship, validation, commit, push, or review. Only an
owner ruling can adopt the decision; a later authorized application tranche
must perform the listed propagation, routed notices and validation.

## Packet inventory and SHA-256

| File | SHA-256 convention | SHA-256 |
|---|---|---|
| `D-GOV-43.proposed.md` | Exact file bytes | `314881568d5ad1aa34950c423ce888a72d82ddb3a5732e4e453c54e8c10dc084` |
| `AGENTS.proposed.patch` | Exact file bytes | `c1654cd5c37da71bf9a277a0c7ea066659042af9a591f97581c31526cd8589be` |
| `IMPACT.md` | Exact file bytes | `aedeafbe08d27057d53f7d026bca2b733fdf34570f5428f2de58d57d145fcf1d` |
| `docs/governance_harness/tranche_manifests/ROOT-DGOV43-PROPOSAL-20260911.yaml` | Exact file bytes | `8fe34499027d86ad8102cea54b83fddbc5f277296efa6a12eba50204d31b9a53` |
| `README.md` | Normalized self-hash defined below | `0f2bf4538f0b49f84211eaa4354d3b0df99d0a0a7c8231ba3a20239d505ccb4f` |

### README self-hash convention

The `README.md` row cannot carry the SHA-256 of its own exact bytes. Its
table records a **normalized self-hash**: replace only the 64 lowercase
hexadecimal characters inside the backticks of the `README.md` table row
with 64 ASCII zeroes, preserve every other byte, and calculate SHA-256 over
the resulting bytes. The other four rows are ordinary exact-byte SHA-256
values.

### Patch-context interpretation

The literal `git apply --check` command controls. Each hunk carries the
adjacent unchanged non-blank lines Git needs as anchors. Where the only
adjacent line is blank, that single blank line appears as a removed and
re-added blank pair rather than as a context line, because the candidate
whitespace validator rejects the single-space context line a unified diff
would otherwise carry. No other unchanged line is deleted and re-added, and
no proposed byte is applied to live `AGENTS.md` here.

## Owner direction of record

The owner's verbatim direction to prepare this packet is transcribed in
`plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md`
(non-governing transcription) and quoted in `D-GOV-43.proposed.md`.

## Validation posture

The packet is acceptable for owner review only when:

- the inactive patch applies cleanly with the literal command
  `git apply --check`;
- basis `AGENTS.md` remains SHA-256
  `2f2e5ee53ab227936379ee47169c0e0ff19bf5fd3bcff9086f088f3568adfac7`;
- the tranche manifest validates in candidate-range mode;
- the unchanged agent-instruction and instruction-entrypoint validators pass;
- candidate-whitespace validation against `origin/main` is clean; and
- the hashes above reproduce under their stated conventions.

Structural validation is evidence only. It is not semantic acceptance or an
owner ruling.

## What the owner is asked to rule on

Twelve proposed ruling items in `D-GOV-43.proposed.md`: stock App Server
owned by the App host; faithful transport; the user's own Codex home and
configuration; user-chosen approval and sandbox policy; continuity from
Codex's thread store; Codex-native authentication; daemon retirement; evidence
from the full stream; roles, skills and workflows under native discovery;
local models as Codex providers; the measure of done; exclusions. The impact
assessment lists every Root surface, decision record, Runtime, App and PEC
deliverable affected, and the notices to route after ruling.
