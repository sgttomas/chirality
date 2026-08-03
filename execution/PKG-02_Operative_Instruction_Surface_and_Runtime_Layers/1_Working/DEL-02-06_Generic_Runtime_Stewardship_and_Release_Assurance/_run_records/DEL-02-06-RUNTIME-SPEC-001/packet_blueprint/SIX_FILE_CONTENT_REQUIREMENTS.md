# Six-file candidate content requirements

Status: `BLUEPRINT — EXACT FILENAMES RESERVED — NO FILE IS INSTANTIATED`

The future candidate staging directory contains exactly these six regular
UTF-8 files and no symlink, subdirectory, or extra file:

1. `CANDIDATE_SET_MANIFEST.sha256`
2. `ROOT_COMPATIBILITY_POLICY_CANDIDATE.md`
3. `DEGRADED_MODE_CONTRACT_CANDIDATE.md`
4. `OPEN_ITEMS.csv`
5. `OWNER_SELECTION.md`
6. `OWNER_GATE.md`

All text uses LF endings, one terminal newline, no trailing whitespace, no
machine-absolute paths, no credential material, and no unresolved placeholder
after S2 instantiation.

## `CANDIDATE_SET_MANIFEST.sha256`

- Contains exactly five sorted lines, one for every other packet file.
- Line form is lowercase 64-hex SHA-256, two ASCII spaces, basename.
- Does not hash itself and contains no comment or blank line.
- Manifest SHA-256, computed after these exact bytes exist, is the candidate-
  set identity used by the external owner acceptance record.

## `ROOT_COMPATIBILITY_POLICY_CANDIDATE.md`

- Declares `FRESH_CURRENT_BASIS_CANDIDATE — NOT ACCEPTED`.
- Binds the accepted Scope of Work, continuation ruling, applied S2 identities,
  TM-ROOT-108, and D-APP-85.
- Restates REQ-001 through REQ-009 without selecting the compatibility value,
  grammar, declaration point, mismatch identifier, or epoch change.
- Adds a candidate recovery-policy section bounded to TM-ROOT-108:
  persisted accepted-turn census, exactly-one-terminal invariant, startup
  barrier, idempotent restart, no prompt/provider/model replay, drain-account
  convergence, fail-closed contradictory evidence, and redacted audit proof.
- Leaves terminal class, event identity, duplicate-history policy, and
  compatibility-epoch effect as explicit later decisions.
- States that packet acceptance is planning-input acceptance only.

## `DEGRADED_MODE_CONTRACT_CANDIDATE.md`

- Declares the same fresh/current-basis/not-accepted state and exact basis.
- Contains ten independent condition rows corresponding to REQ-017 through
  REQ-026: client configuration/project access, runtime credentials,
  registration, authorization, project adapter, Unix socket, compatibility,
  wire/protocol, provider/engine/model, and daemon operational state.
- For every row records boundary, fail-closed behavior, recovery condition,
  replay posture, retry posture, evidence/redaction, and unresolved exact
  identifier where applicable.
- Contains a separate accepted-turn-recovery candidate section preserving
  indeterminate completion, no silent replay, reconciliation before admission
  or model activation, exactly-one-terminal evidence, and crash/restart
  idempotence.
- Does not claim implementation, executable validation, client conformance, or
  semantic acceptance.

## `OPEN_ITEMS.csv`

- Header is exactly:
  `PacketRowID,ScopeTBDID,ScopeAlias,Status,Question,CurrentBasisDisposition,OwningLaterGate,SourceRef,SourceSha`
- Contains exactly sixteen rows in `TBD-001` through `TBD-016` order.
- Maps one-to-one to `OD6-OPEN-001` through `OD6-OPEN-016` as aliases found in
  the accepted Scope of Work; it does not claim the missing historical CSV was
  recovered.
- Carries the accepted OPEN/PROPOSED status and leaves all exact values
  unresolved until their owning later gate.
- Sources every row to `ScopeOfWork.md#TBD-XXX` and the accepted SOW hash.

## `OWNER_SELECTION.md`

- Records only actual owner acts already present:
  fresh current-basis packet preparation is authorized; historical bytes may
  not be reconstructed; exact packet acceptance remains required; fresh N0
  follows both applied S2 and exact packet acceptance.
- Records the first-activation envelope as specification, read-only inventory,
  evidence design, and change planning only.
- Explicitly records `NO SEMANTIC SELECTION`: no compatibility value, terminal
  state, affected-client result, implementation, lifecycle, or release choice.
- Binds exact continuation-ruling and S2 provenance.

## `OWNER_GATE.md`

- Declares the packet candidate unaccepted and immutable once manifested.
- Distinguishes planning-input acceptance from semantic/runtime acceptance.
- Defines the external acceptance-record path and exact token grammar.
- Names the manifest SHA-256 as the sole candidate-set acceptance identity.
- Lists no owner token or inferred acceptance inside the packet.
- Defines rejection/return posture and states that any content repair produces
  a new manifest identity and a fresh owner presentation.

## Cross-file acceptance

The validator must reject the packet if filenames, file count, S2 identities,
fresh-synthesis statement, Scope-of-Work hash, continuation-ruling hash,
open-item mapping, candidate state, manifest hashes, whitespace, or gate
boundaries disagree. A passing validator is still not owner acceptance.
