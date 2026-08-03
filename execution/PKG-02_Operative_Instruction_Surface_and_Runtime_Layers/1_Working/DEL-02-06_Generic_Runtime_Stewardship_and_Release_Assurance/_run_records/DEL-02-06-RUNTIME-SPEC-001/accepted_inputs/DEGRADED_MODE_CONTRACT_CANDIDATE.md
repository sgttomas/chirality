# Degraded-mode contract candidate — DEL-02-06 accepted-turn recovery

Status: `FRESH_CURRENT_BASIS_CANDIDATE — NOT ACCEPTED`
PacketCharacter: `FRESH_SYNTHESIS — NOT RECOVERED HISTORICAL BYTES`

## Exact basis

- Applied current repository basis: `Git HEAD 2b7a7d828e9173836e5b0a71fc015e4f45024215 with exact applied S5/S6 worktree bytes`.
- Applied Root PRD SHA-256: `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`.
- Applied Root decomposition SHA-256: `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`.
- SCA Decision Log SHA-256: `d64272d9c25b3ee21d622a7dc16a5cc20dea0979252e0b899f189ff95a51f508`.
- S5 applied validation SHA-256: `a8bbb5750bbdca7131700aa6c9d92936983f5387038f84cffe5400ab11a85bf8`.
- SCA handoff SHA-256: `625f5e93c8e657785910e31bfc9e179d4aa83896e5e5f9fe1dca98119a9f23f6`.
- S5 applied-file hashes record SHA-256:
  `33ea624ad3396a15f1f242d0d7cebad8dba9a3e5704046d1a4b7f867723ff3de`.
- Fresh AUDIT_DECOMP return SHA-256:
  `ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1`.
- Gate 1 owner-confirmation record SHA-256:
  `05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f`.
- Accepted DEL-02-06 Scope of Work SHA-256:
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`.
- Continuation ruling SHA-256:
  `9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`.

This file is a fresh current-basis synthesis, not reconstruction or recovery
of missing historical degraded-mode bytes. Event identifiers, response
envelopes, retry timing, and presentation wording remain unresolved unless an
accepted current source cited below settles them.

## Common floor

Every required precondition is established independently. Failure stops only
the affected runtime-dependent operation, preserves the truthful machine-
readable class through adapters/presentation, authorizes no fallback, and
creates no repair authority in another boundary. Reconnect/rebind reruns all
preconditions and never silently replays consequential work whose completion
is unknown. File-native functions remain available only where their owner
names and proves them.

## Independent condition matrix

| Condition | Boundary | Required behavior | Recovery | Replay posture | Retry posture | Evidence/redaction | Exact identifier |
|---|---|---|---|---|---|---|---|
| Client configuration/project access (`REQ-017`) | Client/project authority | Prevent send; do not recast as socket absence | Client/project repair then full preflight | None | Owner-defined after repair | Preserve class; redact access material | `UNRESOLVED — TBD-007` |
| Runtime credential readiness (`REQ-018`) | Daemon runtime | Reject without transferring credential custody | Daemon-owned credential readiness then preflight | None | Owner-defined | Preserve provider boundary; no secret value | `UNRESOLVED — TBD-007/TBD-008` |
| Registration/currency (`REQ-019`) | Project registry | Prevent project runtime operation | Separately authorized registration/re-registration | None | No automatic registration | Project/manifest identity, secret-free | `UNRESOLVED — TBD-007` |
| Project/operation authorization (`REQ-020`) | Project authorization | Reject exact operation; do not broaden authority | Accepted scope/authorization repair | None | No automatic broadening | Preserve authorization vs provider-auth distinction | `UNRESOLVED — TBD-007` |
| Required project adapter (`REQ-021`) | Owning project/domain adapter | Block only operations requiring adapter | Adapter restored and preflight passes | None | No silent adapter substitution | Preserve adapter identity/authority | `UNRESOLVED — TBD-007/TBD-008` |
| Unix-socket transport (`REQ-022`) | Root transport | Fail operation; no TCP/in-process fallback | Reconnect/rebind and rerun every precondition | No automatic replay | Retry only after full preflight | Socket class without machine path leakage | `UNRESOLVED — TBD-007/TBD-008` |
| Compatibility mismatch (`REQ-023`) | Root contract/client bind | Reject before consequential work; no downgrade/range inference | Accepted compatible pair and new bind | None | No retry with incompatible pair | Preserve exact identities and mismatch class | `UNRESOLVED — TBD-003/TBD-007` |
| Wire/protocol validity (`REQ-024`) | Root protocol | Fail closed as truthful protocol class | Correct contract-valid peer and new operation | None | Owner-defined | Preserve malformed evidence safely | `UNRESOLVED — TBD-007/TBD-008` |
| Provider/engine/model (`REQ-025`) | Execution domain | Preserve execution cause; do not recast as daemon absence | Exact provider/engine/model readiness | No silent alternate model or replay | Owner-defined | Preserve attribution when exposed; redact credentials | `UNRESOLVED — TBD-007/TBD-008` |
| Daemon operational state (`REQ-026`) | Daemon session/delegation/tool/lock/interruption/residency | Reject or halt affected operation; invent no completion, replay, authority, or alternate state | Truthful state re-established; orphan recovery completed | No automatic replay | `UNRESOLVED` | Evidence-bearing state/epoch with missing attribution reported | `UNRESOLVED — TBD-016` |

## Accepted-turn recovery candidate

An accepted turn without terminal evidence after daemon process loss has
indeterminate completion. Before listening for admission or enabling model
activation, a candidate recovery coordinator enumerates all such turns,
validates event history, and appends exactly one later-ruled recovery terminal.
It never invokes the provider/engine/model or resends the prompt.

Repeated startup is idempotent. A crash after terminal append but before
derived status update converges on the existing terminal. Duplicate terminals,
malformed JSONL, missing turn identity, or failed persistence stop daemon
startup closed and preserve evidence. The summary records identifiers, reason,
counts, and result without copying prompts or credentials.

The exact recovery terminal class, payload, deterministic identity, duplicate-
history policy, retry timing, and compatibility-epoch effect remain unresolved
for the later semantic gate. Packet acceptance does not settle them.

## Evidence posture

Positive, negative, and adversarial evidence is required for each row. The
later executable matrix must prove restart/replay idempotence, exactly one terminal,
session/drain convergence, admission/model ordering, no replay,
redaction, malformed-evidence failure, and unchanged existing terminals.
Present source bytes and this design are not executable proof.

## No-effect boundary

No runtime/client bytes, semantic contract, conformance result, lifecycle,
release, register, dependency, profile, or Git state changes through this
candidate or its planning-input acceptance.
