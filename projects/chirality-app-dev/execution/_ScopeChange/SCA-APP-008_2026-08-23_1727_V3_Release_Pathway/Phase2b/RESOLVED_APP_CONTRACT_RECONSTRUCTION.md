# SCA-APP-008 Phase 2b — Resolved App-Contract Reconstruction

**State:** `AWAITING_OWNER_APPROVAL`
**Authority effect:** `CANDIDATE_ONLY — NOT_APPLIED`
**ReadyForNextPhase:** `NO`
**Basis commit:** `ef92fab10f40aa95da484701982d83fa1abca874`

## Boundary and effect

This additions-only artifact records the exact in-memory full-file App-contract
candidate produced by the approved Gate-3 transactions after substituting the
Phase-2b regenerated C-01 and re-pinned, byte-identical resolved C-06 rows. It
does not edit the live App contract, accept or apply any contract row, move
`_LATEST.md`, activate DEL-02-07/WP-03, route a notice, or create
implementation, lifecycle, release, publication, or foreign-loop authority.

House convention keeps the resolved full-file image reconstructible from its
immutable transaction sources rather than storing a second contract-shaped
file. The exact full-file SHA-256 and byte count below are the candidate
identity used by the rebuilt companion register.

## Consumed transaction identities

| Input | SHA-256 / exact row identity | Result |
| --- | --- | --- |
| Gate-3 C-01 through C-11 package | `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df` | immutable transaction source |
| N1 regenerated K-CONTROL-1 artifact | `cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8` | consumed exactly |
| N1 regenerated C-01 LF-terminated row | `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616` | substituted only after the Phase-2 control replay |
| N2 re-pinned K-EVENT-4 artifact | `c6b6d31497f0399c319b9b1772964b5c003ca1b520289cd7238d14efd84ba463` | consumed exactly |
| N2 resolved C-06 LF-terminated row | `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` | byte-identical to Phase 2 |
| Live App-contract pre-image | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | exact basis pre-image |

## Independent replay

N3 independently extracted each exact Gate-3 transaction and required every
replacement or insertion anchor to occur exactly once. It then:

1. applied C-01 through C-11 to the live App-contract pre-image using the
   original Gate-3 C-01 post-image and the Phase-2 resolved C-06 post-image;
2. reproduced the Phase-2 resolved candidate exactly; and
3. repeated the same replay while substituting only N1's regenerated C-01
   post-image and retaining N2's byte-identical resolved C-06 post-image.

| Reconstruction | Bytes | Lines | SHA-256 | Result |
| --- | ---: | ---: | --- | --- |
| Phase-2 control: old C-01 + resolved C-06 | `34317` | `214` | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` | `PASS — EXACT REPRODUCTION` |
| Phase-2b candidate: regenerated C-01 + resolved C-06 | `34877` | `214` | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` | `PASS — FINAL CANDIDATE` |

The Phase-2b full-file candidate therefore supersedes `a7928297…` only
because C-01 changed. C-06 remains byte-identical. The line count and all
source-anchor positions remain unchanged.

## Exact substitution proof

| Check | Result |
| --- | --- |
| Original Gate-3 C-01 row replayed first | `PASS` — LF SHA-256 `60634f16c23d8ac63818f8b785691a1f3e9d53e5fadc8ec6b25a3627788ef232` |
| Phase-2 resolved C-06 used in both replays | `PASS` — LF SHA-256 `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` |
| Phase-2 control identity reproduced | `PASS` — `a7928297…`, `34317` bytes |
| Only C-01 substituted for final replay | `PASS` |
| N1 regenerated C-01 identity | `PASS` — LF SHA-256 `add623f4…` |
| Final full-file identity matches N1 preliminary identity | `PASS` — `842bf170…`, `34877` bytes |
| Old K-EVENT-4 open question occurrences | `0` |
| Resolved K-EVENT-4 row occurrences | `1` |
| K-CONTROL-1 row occurrences | `1` |

## Candidate handoff

| State | Value |
| --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `AuthorityState` | `NO_NEW_AUTHORITY` |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` |
| `NextGateState` | `N3_COMPANION_REGISTER_REBUILD_THEN_N4_REVIEW` |

`ReadyForNextPhase = NO`.
