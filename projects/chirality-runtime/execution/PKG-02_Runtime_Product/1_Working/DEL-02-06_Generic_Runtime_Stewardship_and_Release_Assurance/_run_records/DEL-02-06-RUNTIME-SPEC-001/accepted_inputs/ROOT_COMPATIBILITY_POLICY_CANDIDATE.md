# Root compatibility policy candidate — DEL-02-06 accepted-turn recovery

Status: `FRESH_CURRENT_BASIS_CANDIDATE — NOT ACCEPTED`
PacketCharacter: `FRESH_SYNTHESIS — NOT RECOVERED HISTORICAL BYTES`

## Exact basis

| Basis | Identity |
|---|---|
| Applied current repository basis | `Git HEAD 2b7a7d828e9173836e5b0a71fc015e4f45024215 with exact applied S5/S6 worktree bytes` |
| Applied Root PRD SHA-256 | `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` |
| Applied Root decomposition SHA-256 | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| SCA Decision Log SHA-256 | `d64272d9c25b3ee21d622a7dc16a5cc20dea0979252e0b899f189ff95a51f508` |
| S5 applied validation SHA-256 | `a8bbb5750bbdca7131700aa6c9d92936983f5387038f84cffe5400ab11a85bf8` |
| SCA handoff SHA-256 | `625f5e93c8e657785910e31bfc9e179d4aa83896e5e5f9fe1dca98119a9f23f6` |
| S5 applied-file hashes record SHA-256 | `33ea624ad3396a15f1f242d0d7cebad8dba9a3e5704046d1a4b7f867723ff3de` |
| Fresh AUDIT_DECOMP return SHA-256 | `ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1` |
| Gate 1 owner-confirmation record SHA-256 | `05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f` |
| Accepted DEL-02-06 Scope of Work SHA-256 | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` |
| Continuation ruling SHA-256 | `9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6` |
| TM-ROOT-108 handoff SHA-256 | `da191f8c12207398c676531daf8941148797dc4f206c33ad58797a1e74a77fbc` |
| D-APP-85 route SHA-256 | `0b34cefdc9abd5927db1b6bdda07225c37c42806ff5b3f946bb182227f08dc41` |

This file is a fresh current-basis synthesis. It does not reproduce,
reconstruct, restore, or authenticate the missing historical policy bytes.
Acceptance of the eventual packet makes this exact file a first-activation
planning input only; it does not adopt a runtime compatibility contract.

## Compatibility identity constraints

1. `REQ-001`: one Root compatibility identity denotes one epoch of
   consequential generic daemon/client contract semantics.
2. `REQ-002`: route namespace, package version, runtime fingerprint, source or
   release commit, distributable identity, and Tier-0 Flow-A identity are not
   compatibility identity substitutes.
3. `REQ-003`: Root owns the identity and semantic definition; coordination
   cannot transfer generic-runtime ownership.
4. `REQ-004`: an actually affected client compares the daemon-declared
   identity by exact equality before consequential work.
5. `REQ-005`: mismatch stops the operation with a distinct typed result and no
   downgrade, alternate runtime, alternate daemon/model/transport, or
   transport-success inference.
6. `REQ-006`: range negotiation, downgrade, and concurrent multi-version
   support remain unsupported without a later exact owner act.
7. `REQ-007`: a binding record connects exact identity to contract bytes,
   source/release identities, affected clients and bases, accepted evidence,
   and human release disposition.
8. `REQ-008`: an identity change requires a consequential Root tranche,
   affected-client determination, separate client evidence, regression proof,
   and separate human release disposition.
9. `REQ-009`: only an accepted exact implementation or migration obligation
   permits `AFFECTED`; prospect names create no work or veto.

## TM-ROOT-108 recovery-policy candidate

The later exact semantic gate evaluates these candidate rules:

- enumerate every persisted `turn.accepted` without terminal evidence across
  registered project/session stores before the daemon exposes admission or
  model activation;
- treat `turn.completed`, `turn.failed`, `turn.cancelled`, and
  `turn.interrupted` as the terminal set;
- reconcile each orphan to exactly one owner-ruled recovery terminal without
  provider, engine, model, tool, client, or prompt replay;
- make reconciliation idempotent across repeated restart and replay attempts;
- recover safely from a crash between terminal persistence and derived
  session-status persistence without creating a second terminal;
- fail startup closed on malformed evidence, missing usable turn identity,
  duplicate terminal history, or failed persistence;
- complete recovery before new turn admission, local-model drain transition,
  unload/load, or model activation;
- preserve append-only evidence, redact prompt/credential content from new
  recovery evidence, and emit a bounded reconciliation summary; and
- leave runtime operational state non-authoritative while keeping contract,
  tests, decisions, and acceptance evidence checkout-contained.

## Explicit unresolved decisions

- Exact compatibility identity value and grammar: `UNRESOLVED — TBD-001`.
- Declaration/comparison point: `UNRESOLVED — TBD-002`.
- Mismatch identifier/presentation: `UNRESOLVED — TBD-003`.
- Recovery terminal class and payload: `UNRESOLVED — TBD-006/TBD-016`.
- Recovery event-identity derivation: `UNRESOLVED — later semantic gate`.
- Duplicate-terminal historical posture: `PROPOSED FAIL-CLOSED — later gate`.
- compatibility-epoch effect of recovery: `UNRESOLVED — TBD-015`.
- Actually affected clients: `UNRESOLVED — TBD-005/TBD-009/TBD-011/TBD-013`.

No unresolved field is answered by present bytes, implementation behavior,
matching labels, validation, or packet acceptance.

## No-effect boundary

This candidate creates no implementation authority, client obligation,
dependency, profile, lifecycle, release, publication, reliance, register, Git,
or foreign-loop effect. REQ-027, REQ-029, REQ-032, REQ-035, REQ-036,
REQ-038, REQ-047, and REQ-052 remain controlling.
