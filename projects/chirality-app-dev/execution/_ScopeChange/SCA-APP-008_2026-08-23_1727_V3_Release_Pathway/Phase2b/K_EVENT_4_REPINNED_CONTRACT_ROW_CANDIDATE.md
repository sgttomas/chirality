# SCA-APP-008 Phase 2b — Re-pinned K-EVENT-4 Contract-Row Candidate

**State:** `AWAITING_OWNER_APPROVAL`
**Authority effect:** `CANDIDATE_ONLY — NOT_APPLIED`
**ReadyForNextPhase:** `NO`
**Basis commit:** `ef92fab10f40aa95da484701982d83fa1abca874`
**Transaction:** Phase-2 K-EVENT-4 candidate re-grounded under owner ruling A6-B
**Consumed N1 candidate:** `cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`

## Boundary and effect

This addition-only artifact supersedes the Phase-2 K-EVENT-4 transaction
artifact only as its current Root-contract grounding. It does not change the
resolved K-EVENT-4 row or its Phase-2 transaction pre-image, edit the live App
contract, accept or apply a contract row, rebuild or edit the companion
register, recompute the Phase-2b resolved full-contract candidate, move
`_LATEST.md`, activate a carrier, route a notice, or create implementation,
lifecycle, release, or foreign-loop authority.

Root's K-CONTROL-1 amendment is now ratified. A6-B directs this re-grounding
because that ratification changed the Root contract identity while leaving the
K-RUNTIME-1 and K-STORE-2 rows supporting A4-A byte-identical. This removes the
old binding-staleness caveat without introducing a semantic K-EVENT-4 change.
The resolved row remains part of the atomic contract group, and A5-C keeps one
Gate-5 act for the decomposition and contract groups. Owner approval of the
exact regenerated Phase-2b candidates remains separate.

## Transaction identity

| Field | Exact value |
| --- | --- |
| Target | `projects/chirality-app-dev/docs/CONTRACT.md` |
| Target full-file pre-image SHA-256 | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` |
| Live citation | line 72 |
| Live row occurrence count | `1` |
| Live row SHA-256, including terminating LF | `f172b56078f83dcc48019ff0fea3c867f96c3d79ab5143fa9bb668d6937fab2a` |
| Resolved row SHA-256, including terminating LF | `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` |
| Phase-2 resolved contract candidate SHA-256 | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` |
| Phase-2 resolved contract candidate byte count | `34317` |

The Phase-2 full resolved contract relationship is preserved: applying the
approved Phase-1 C-01 through C-11 contract transactions to the exact live
pre-image, substituting the resolved POST-IMAGE below for the question-bearing
C-06 POST-IMAGE, reconstructs `a7928297…` at `34317` bytes. The old unresolved
question occurs zero times and the resolved row occurs exactly once in that
image. N3, not this node, recomputes the Phase-2b resolved contract with the
regenerated C-01 candidate and rebuilds the companion register.

## A4-A identity and A6-B re-grounding

**Selected identity ruling:**
`plans/steers/chirality_app_v3_app_ruling_record_a4_2026-08-23.md`, SHA-256
`14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d`, A4-A.

**Re-grounding ruling:**
`plans/steers/chirality_app_v3_app_ruling_record_a6_2026-08-23.md`, SHA-256
`66bd22a1b439979f74bbaedf2c182d222a6ba38952ec046f78fc2091885e4e63`, A6-B.

A4-A selects this canonical identity:

```text
{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl
where {userData} = ~/Library/Application Support/Chirality
event schema:   chirality.event/v1
session record: chirality.session/v2  (session.json beside events.jsonl)
```

A6-B re-pins the selected identity to these exact current Root source blobs:

| Root source | SHA-256 | Exact evidence |
| --- | --- | --- |
| `docs/CONTRACT.md` | `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83` | Ratified contract. K-RUNTIME-1 line 161 makes the daemon the exclusive session owner; K-STORE-2 line 164 requires JSON/JSONL and lazy non-destructive legacy import. Relative to the A4-A pin `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`, only line 162 changed, for K-CONTROL-1. |
| `runtime/packages/cli/src/config.ts` | `40cec2df6c21fa10a5a053ff6e40ea0b6d9d4a352208660cc01eb22f5fc7523e` | lines 17–21 resolve `{userData}` to `~/Library/Application Support/Chirality` and `runtimeDirectory` to `{userData}/runtime`. |
| `runtime/packages/core/src/session-store.ts` | `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | lines 240–270 preserve legacy provenance and copy `events.jsonl` non-destructively; lines 392–407 define `runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl` with adjacent `session.json`. |
| `runtime/packages/contracts/src/events.ts` | `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` | line 17 fixes event schema `chirality.event/v1`. |
| `runtime/packages/contracts/src/session.ts` | `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51` | line 5 fixes session-record schema `chirality.session/v2`. |

The two cited supporting Root rows are byte-identical between the A4-A and
ratified contract blobs:

| Root row | Line | LF-terminated SHA-256 at both identities |
| --- | ---: | --- |
| K-RUNTIME-1 | 161 | `03985c419f2704e9529c3c9e4247f0dadb4ff47243ceafebd3ae1492dbd741f4` |
| K-STORE-2 | 164 | `ab84004cf36b4ba414c237170396b037744f29d44f1086f09969d4114ed98e09` |

The prior and ratified Root contract byte counts are `20210` and `20905`;
their sole line delta is line 162. The other four Root source identities are
unchanged. If any current source identity or cited byte changes before
application, this candidate is stale and must be regenerated; no inference or
partial application is permitted.

## Exact transaction

Application grammar remains the Phase-1 Gate-3 grammar: require the target
full-file pre-image SHA-256, require the PRE-IMAGE bytes exactly once at line
72, replace them with the POST-IMAGE bytes exactly including the terminating
LF, and fail closed on absence, duplication, line drift, source drift, or any
reconstructed full-file hash mismatch.

### PRE-IMAGE

```text
| **K-EVENT-4** | `.chirality/sessions/<id>/events.jsonl` is the product-owned Chirality runtime audit mirror. | Session store; replay; R0/R1 storage decision. |
```

### POST-IMAGE

```text
| **K-EVENT-4** | The Root-owned shared-runtime session store at `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl`, where `{userData}` resolves to `~/Library/Application Support/Chirality`, using event schema `chirality.event/v1` with adjacent `session.json` session record schema `chirality.session/v2`, is the canonical runtime audit record. The Root daemon is the sole active writer under Root K-RUNTIME-1. Project-local `.chirality/sessions/<id>/events.jsonl` is a legacy App compatibility source read and lazily migrated non-destructively under Root K-STORE-2; it is never a second active writer or an authority replacement. App `UIEvent` streaming and replay remain projections of accepted runtime records. | Root/App storage-contract concordance; canonical-path/schema fixtures; one-writer tests; lazy non-destructive migration/source-preservation; replay/path/version tests; no-dual-store inspection. |
```

## Identity and semantic checks

| Requirement | Result |
| --- | --- |
| Phase-2 resolved POST-IMAGE bytes unchanged | `PASS` — LF SHA-256 `92c9d359…` |
| Transaction pre-image and line cite unchanged | `PASS` |
| Phase-2 resolved full-contract relationship preserved | `PASS` — `a7928297…`, `34317` bytes |
| Root contract re-pinned `ed87eaff…` → `ad0a4e6a…` | `PASS` |
| Root contract changed only at line 162 | `PASS` |
| K-RUNTIME-1 line 161 byte-identical | `PASS` |
| K-STORE-2 line 164 byte-identical | `PASS` |
| Four other Root source pins unchanged | `PASS` |
| Canonical selected Root path named literally | `PASS` |
| `{userData}` resolution named literally | `PASS` |
| Event and session schemas named literally | `PASS` |
| Root daemon is sole active writer | `PASS` |
| Legacy App source is read/migrated lazily and non-destructively | `PASS` |
| No second active writer or authority replacement | `PASS` |
| App `UIEvent` streaming/replay are projections only | `PASS` |

## Candidate handoff

| State | Value |
| --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `AuthorityState` | `NO_NEW_AUTHORITY` |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` |
| `NextGateState` | `N3_RESOLVED_CONTRACT_AND_COMPANION_REGISTER_REBUILD` |

`ReadyForNextPhase = NO`.
