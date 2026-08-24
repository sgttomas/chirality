# SCA-APP-008 Phase 2b — Regenerated K-CONTROL-1 Contract-Row Candidate

**State:** `AWAITING_OWNER_APPROVAL`
**Authority effect:** `CANDIDATE_ONLY — NOT_APPLIED`
**ReadyForNextPhase:** `NO`
**Basis commit:** `ef92fab10f40aa95da484701982d83fa1abca874`
**Transaction:** Phase-1 C-01 regenerated from the ratified Root
K-CONTROL-1 design under A6-A

## Boundary and effect

This additions-only artifact replaces the Phase-1 C-01 post-image for later
exact-candidate reconstruction and review. It does not edit the live App
contract, accept or apply a contract row, rebuild or edit the companion
register, move `_LATEST.md`, activate DEL-02-07/WP-03, route a notice, or
create implementation, lifecycle, release, publication, or foreign-loop
authority.

The ratified topology is an accepted two-socket design, not a claim that two
sockets operate today. Exactly one control socket is live today. The private
supervisor socket becomes live only through the separately gated
DEL-02-07/WP-03 pathway. A5-C retains one later Gate-5 act for the
decomposition and contract groups, after owner approval of the exact
regenerated candidates.

## Transaction identity

| Field | Exact value |
| --- | --- |
| Target | `projects/chirality-app-dev/docs/CONTRACT.md` |
| Target full-file pre-image SHA-256 | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` |
| Live citation | line 200 |
| Live row occurrence count | `1` |
| Live row SHA-256, including terminating LF | `2f56b652642874f82c9580574bc88bb6ef0ec1c4e1a91ef4c291ea11da2894c5` |
| Regenerated row SHA-256, including terminating LF | `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616` |
| Phase-2 resolved full-contract reconstruction check | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` (`34317` bytes) |
| Preliminary regenerated full-contract candidate SHA-256 | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` |
| Preliminary regenerated full-contract candidate bytes | `34877` |

The preliminary full-file identity is mechanically reconstructed by applying
the exact Phase-1 C-01 through C-11 transactions to the live App-contract
pre-image, substituting the Phase-2 resolved C-06 row and then substituting
only the regenerated C-01 post-image below. The same reconstruction before
the C-01 substitution reproduces the Phase-2 identity `a7928297…` exactly.
N3 must independently reconstruct and publish the final full-file candidate;
this preliminary identity is its fail-closed N1 input, not a live target.

## Ratified Root grounding

**Owner ruling:**
`plans/steers/chirality_app_v3_app_ruling_record_a6_2026-08-23.md`, SHA-256
`66bd22a1b439979f74bbaedf2c182d222a6ba38952ec046f78fc2091885e4e63`,
A6-A.

**Ratified Root contract:** `docs/CONTRACT.md`, SHA-256
`ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`.
Its line 162 K-CONTROL-1 row is:

```text
| **K-CONTROL-1** | Runtime control uses authenticated, project-scoped HTTP/1.1 over `{userData}/runtime/control.sock` beneath a `0700` directory with a `0600` socket. The accepted design adds exactly one private Unix-domain socket between the daemon and the Delegated-Harness Process Supervisor, never renderer- or CLI-callable, with a `0700` parent directory and a `0600` socket, as accepted by R7-A through the DEL-02-07 scope contract (record SHA-256 `dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53`). The supervisor socket is accepted design, not yet implemented: exactly one control socket is live today, and the second socket becomes live only through the separately gated DEL-02-07/WP-03 implementation pathway. No third socket and no TCP control listener are permitted under any configuration. | Socket-mode, authorization, stale-owner, and listener tests; design-gated supervisor-socket tests activating with DEL-02-07 implementation |
```

The prior Root-contract pin
`ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`
and the ratified contract differ at exactly line 162. The adjacent Root rows
are byte-identical across the prior and ratified identities:

| Root row | Line | Prior/current LF-terminated row SHA-256 | Result |
| --- | ---: | --- | --- |
| K-RUNTIME-1 | 161 | `03985c419f2704e9529c3c9e4247f0dadb4ff47243ceafebd3ae1492dbd741f4` | `BYTE_IDENTICAL` |
| K-STORE-2 | 164 | `ab84004cf36b4ba414c237170396b037744f29d44f1086f09969d4114ed98e09` | `BYTE_IDENTICAL` |

Root K-RUNTIME-1 makes the daemon the exclusive production owner. The App
candidate therefore names the Root daemon as exclusive owner of the
`{userData}/runtime` control surfaces and expressly denies App second-owner or
second-writer status.

## Exact transaction

Apply using the Phase-1 Gate-3 grammar: require the target full-file pre-image
SHA-256, require the PRE-IMAGE bytes exactly once at line 200, replace them
with the POST-IMAGE bytes exactly including the terminating LF, and fail closed
on absence, duplication, line drift, source drift, or reconstructed full-file
hash mismatch.

### PRE-IMAGE

```text
| **K-CONTROL-1** | Runtime control is exposed only over an authenticated project-scoped HTTP/1.1 API on a Unix-domain socket beneath a `0700` parent with a `0600` socket. No TCP control listener is permitted. | Permission/authorization tests; stale-socket recovery; listener inspection. |
```

### POST-IMAGE

```text
| **K-CONTROL-1** | The Root daemon exclusively owns the `{userData}/runtime` control surfaces under Root K-RUNTIME-1; the App is neither a second owner nor a writer of runtime control state. Exactly one control socket is live today: the existing authenticated project-scoped daemon HTTP/1.1 API at `{userData}/runtime/control.sock`. The ratified two-socket design adds exactly one private daemon-to-Delegated-Harness-Process-Supervisor Unix-domain socket that is never renderer- or CLI-callable and becomes live only through the separately gated DEL-02-07/WP-03 implementation pathway. Each live control socket resides beneath a daemon-owned `0700` parent, is mode `0600`, binds to verified same-UID path ownership and owner/generation records, uses rotated high-entropy bearer tokens delivered only through app-private state, fails closed on stale or mismatched identity, and recovers stale sockets explicitly. No peer-credential guarantee is claimed where the runtime cannot inspect peer credentials. No third socket and no TCP control listener are permitted under any configuration. | Live single-socket API permission, authorization, same-UID owner, generation, token, stale-recovery, listener-inventory, no-third-socket, and no-TCP tests; design-gated supervisor-socket permission/identity/token, renderer/CLI denial, and two-listener-inventory tests activating with DEL-02-07 implementation; G-HELPER/G-DUAL/AT-054/058. |
```

## Semantic and verification checks

| Requirement | Result |
| --- | --- |
| Ratified two-socket design preserved | `PASS` |
| Exactly one live control socket stated in present tense | `PASS` |
| Supervisor socket activates only through DEL-02-07/WP-03 | `PASS` |
| Supervisor socket never renderer- or CLI-callable | `PASS` |
| Root daemon exclusively owns `{userData}/runtime` control surfaces | `PASS` |
| No App-owned runtime-directory or second-writer claim | `PASS` |
| `0700` parent and `0600` socket | `PASS` |
| Verified same-UID path ownership and owner/generation records | `PASS` |
| Rotated high-entropy app-private bearer-token delivery | `PASS` |
| Fail-closed stale/mismatched identity and explicit stale recovery | `PASS` |
| No-peer-credential disclaimer | `PASS` |
| No third socket and no TCP listener under any configuration | `PASS` |
| Live single-socket tests retained | `PASS` |
| Supervisor and two-listener tests design-gated | `PASS` |

## Candidate handoff

| State | Value |
| --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `AuthorityState` | `NO_NEW_AUTHORITY` |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` |
| `NextGateState` | `N2_K_EVENT_4_REPIN_THEN_N3_REBUILD` |

`ReadyForNextPhase = NO`.
