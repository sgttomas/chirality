# Return — N1 HELPS_HUMANS D-GOV-35 Proposal Packet

Verdict: `REPAIRED — READY FOR FRESH INDEPENDENT REVIEW CYCLE 3`

RunID: `ROOT_V3_PHASE0_2026-08-22`

Node: `N1`

Role: `HELPS_HUMANS`, managed by `HELP_HUMAN`

AcceptedBasis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`

ClaimStatus: `PROPOSED — AWAITING OWNER RULING`

BriefVersion: `2` (N1 amendment version 2)

## Result

The complete D-GOV-35 proposal packet is prepared within the sealed N1 write
scope. It proposes a second `delegated-harness-native` class while preserving
managed children as the sole Chirality-managed path, records untyped primary
native entry, refuses automatic native-descendant Agent 2 classification,
quotes G0 A3 owner text verbatim, and records Codex Agent 0/1/2 role-entry
parity plus the `role not mechanically enforced` and `instruction-asserted`
evidence labels.

The proposal expressly states that delegated-harness-native K-SUBAGENT
non-delegation is instruction+config asserted rather than mechanism-proven. It
prospectively frames the TM-ROOT-126 Workflow-Component Standard concordance
decision, names the required App authority/SOW/code surfaces, enumerates every
exact App/Piping evidence file found at the accepted Root `AGENTS.md` hash,
both identified historical process-input maps, and the Root-owned stale
Chirality App public-export projection. It names the projection's governing
regeneration profile and routes later regeneration or explicit deferral,
application, App WP-06, notice, evidence-regeneration, and historical-record
handling to their lawful later owners. N1 did not edit or regenerate the
export.

The version-2 repair also calibrates the cited App code claim to what its bytes
prove: lines 205-213 deny untyped/generalist delegation requests that reach the
existing governance gate. Native-class integration remains App WP-06 work.

No proposal is self-adopting. D-GOV-35 remains blocked on an owner ruling, and
no live instruction, standard, contract, App/Piping file, hold, lifecycle,
pointer, pin, product source, release, publication, or merge state changed.

## Content write set and hashes

| Path | Hash convention | SHA-256 |
|---|---|---|
| `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/D-GOV-35.proposed.md` | Exact bytes | `924c1b098f1510bca9189e1ac06e4c2fd8e9d358a9fc3c4e42fdd04a53b69c88` |
| `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch` | Exact bytes | `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee` |
| `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/IMPACT.md` | Exact bytes | `565e651963b08f74622ca0e0d32b66d6d301c3ef95c159867b4e41a6fbd98435` |
| `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/README.md` | Exact bytes | `c972a3111c5eab5dfd5092210af3e8127b7270f0dfe18b78223e5c8ee1e8ef02` |
| same `README.md` | Normalized self-hash under its documented convention | `59bd2cd2b3e8a0812e5d509f22d52009048b0314dd8cf9ec9c7a43efe524c32d` |

Control-plane writes are this `RETURN.md` and sibling `STATUS.json` only.

## Basis and source identities

- `git rev-parse HEAD` returned
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`.
- `git cat-file -t 6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
  returned `commit`.
- Accepted-basis and live `AGENTS.md` both reproduce SHA-256
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`.
- Owner steer SHA-256:
  `c348e9767db4af20787bbcb74c64791ef08d700b08dc19d86289a88a58f067e3`.
- Owner G0 record SHA-256:
  `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`.
- D-GOV-14 SHA-256:
  `9d6dd7e4fdf96219c74a6fc728f441ecc2eabbde9bc141b5cc40d909e088f74e`.
- Workflow-Component Standard SHA-256:
  `5de31f552bea356629ad29af9bc664f33d49392d1c63fc2fb4dc70614abd7df9`.
- Decomposition Standard SHA-256:
  `9e356ea11d4ab09264b3526e368b7acdb59fd0accaa70a21808da796b5252cea`.
- Cited App code SHA-256:
  `2b2d750be8fb3974593599631f64f920bc3b3fd4512640545bf1a22e61ec215c`.

## Validation

| Check | Result |
|---|---|
| `git apply --check docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch` | `PASS` |
| `git apply --numstat .../AGENTS.proposed.patch` | `23` additions, `5` deletions; unchanged rules are not deleted/re-added to manufacture context. |
| Patch context | `PASS`: four minimal literal-Git-compatible hunks use only adjacent unchanged anchors inside the named section, with zero context outside it; the artifact does not claim conventional `-U0`. |
| `sha256sum AGENTS.md` | `PASS`: exact basis hash; proposed patch was not applied. |
| `python3 tools/validation/validate_agent_instructions.py` | `PASS`: 34 files, 0 errors, 0 warnings. |
| `python3 tools/validation/validate_instruction_entrypoints.py` | `PASS`: root instruction entrypoints are canonical. |
| N1-scoped `git diff --check` and packet whitespace scan | `PASS`. |
| Packet exact hashes and normalized README self-hash reproduction | `PASS`. |

Amendment N1 version 2 records that conventional `-U0` and the required literal
default `git apply --check` are incompatible under this repository's Git
behavior. The literal command controls. The patch uses only the minimum
adjacent unchanged anchors needed by its four hunks, all inside the target
section, and adds no context outside it.

Global `validate_candidate_whitespace.py --base-ref origin/main` passes after
the previously reported sibling N2 EOF finding was repaired by its owner.

## Blockers, reruns, and next lawful owner

N1 repair blockers: `NONE`. Fresh independent review cycle 3 is required
before N1 may be accepted at fan-in.

Decision blocker: D-GOV-35 requires the owner's explicit ruling. The Root
instruction application tranche and all App WP-06 changes remain blocked until
their respective authority gates open.

Fan-in rerun: HELP_HUMAN reproduces global candidate-whitespace validation and
the packet hashes, and byte-verifies `AGENTS.md` before endorsement.

Next lawful owner: fresh independent reviewer cycle 3, then `HELP_HUMAN` for
semantic fan-in if that review passes. If accepted for presentation, the human
owner rules D-GOV-35; no N1 act substitutes for that ruling.

No commit, push, PR, merge, adoption, implementation, lifecycle, release,
publication, or reliance act was performed by N1.
