# SCA-APP-008 Phase 2 — Resolved K-EVENT-4 Contract-Row Candidate

**State:** `AWAITING_OWNER_APPROVAL`
**Authority effect:** `CANDIDATE_ONLY — NOT_APPLIED`
**ReadyForNextPhase:** `NO`
**Basis commit:** `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Transaction:** Phase-1 C-06 regenerated from the owner-selected A4-A identity

## Boundary and effect

This addition-only artifact replaces the question-bearing Phase-1 C-06 candidate for later exact-candidate review. It does not edit the live App contract, accept or apply a contract row, rebuild or edit the companion register, move `_LATEST.md`, activate a carrier, route a notice, or create implementation, lifecycle, release, or foreign-loop authority.

The resolved row remains part of the Phase-1 atomic contract group. A4-B and A5-B keep that group ineligible for Gate-5 application until Root's K-CONTROL-1 design amendment is ratified. A5-C keeps one Gate-5 act for the decomposition and contract groups. Owner approval of these exact candidate bytes remains separate.

## Transaction identity

| Field | Exact value |
| --- | --- |
| Target | `projects/chirality-app-dev/docs/CONTRACT.md` |
| Target full-file pre-image SHA-256 | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` |
| Live citation | line 72 |
| Live row occurrence count | `1` |
| Live row SHA-256, including terminating LF | `f172b56078f83dcc48019ff0fea3c867f96c3d79ab5143fa9bb668d6937fab2a` |
| Resolved row SHA-256, including terminating LF | `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` |
| Full resolved contract candidate SHA-256 | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` |
| Full resolved contract candidate byte count | `34317` |

The full resolved contract candidate identity is produced in memory by applying the approved Phase-1 C-01 through C-11 contract transactions to the exact live pre-image, substituting only the resolved POST-IMAGE below for the question-bearing C-06 POST-IMAGE. The old unresolved question occurs zero times and the resolved row occurs exactly once in that reconstructed full-file image.

## A4-A grounding

**Owner ruling:** `plans/steers/chirality_app_v3_app_ruling_record_a4_2026-08-23.md`, SHA-256 `14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d`, A4-A.

A4-A selects this canonical identity:

```text
{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl
where {userData} = ~/Library/Application Support/Chirality
event schema:   chirality.event/v1
session record: chirality.session/v2  (session.json beside events.jsonl)
```

The selection is bound to these exact Root source blobs:

| Root source | SHA-256 | Exact evidence |
| --- | --- | --- |
| `docs/CONTRACT.md` | `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679` | K-RUNTIME-1 line 161 makes the daemon the exclusive session owner; K-STORE-2 line 164 requires JSON/JSONL and lazy non-destructive legacy import. |
| `runtime/packages/cli/src/config.ts` | `40cec2df6c21fa10a5a053ff6e40ea0b6d9d4a352208660cc01eb22f5fc7523e` | lines 17–21 resolve `{userData}` to `~/Library/Application Support/Chirality` and `runtimeDirectory` to `{userData}/runtime`. |
| `runtime/packages/core/src/session-store.ts` | `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | lines 240–270 preserve legacy provenance and copy `events.jsonl` non-destructively; lines 392–407 define `runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl` with adjacent `session.json`. |
| `runtime/packages/contracts/src/events.ts` | `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` | line 17 fixes event schema `chirality.event/v1`. |
| `runtime/packages/contracts/src/session.ts` | `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51` | line 5 fixes session-record schema `chirality.session/v2`. |

If any source identity or cited byte changes before application, this candidate is stale and must be regenerated; no inference or partial application is permitted.

## Exact transaction

Application grammar remains the Phase-1 Gate-3 grammar: require the target full-file pre-image SHA-256, require the PRE-IMAGE bytes exactly once at line 72, replace them with the POST-IMAGE bytes exactly including the terminating LF, and fail closed on absence, duplication, line drift, source drift, or any reconstructed full-file hash mismatch.

### PRE-IMAGE

```text
| **K-EVENT-4** | `.chirality/sessions/<id>/events.jsonl` is the product-owned Chirality runtime audit mirror. | Session store; replay; R0/R1 storage decision. |
```

### POST-IMAGE

```text
| **K-EVENT-4** | The Root-owned shared-runtime session store at `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl`, where `{userData}` resolves to `~/Library/Application Support/Chirality`, using event schema `chirality.event/v1` with adjacent `session.json` session record schema `chirality.session/v2`, is the canonical runtime audit record. The Root daemon is the sole active writer under Root K-RUNTIME-1. Project-local `.chirality/sessions/<id>/events.jsonl` is a legacy App compatibility source read and lazily migrated non-destructively under Root K-STORE-2; it is never a second active writer or an authority replacement. App `UIEvent` streaming and replay remain projections of accepted runtime records. | Root/App storage-contract concordance; canonical-path/schema fixtures; one-writer tests; lazy non-destructive migration/source-preservation; replay/path/version tests; no-dual-store inspection. |
```

## Semantic checks

| Requirement | Result |
| --- | --- |
| Canonical selected Root path named literally | `PASS` |
| `{userData}` resolution named literally | `PASS` |
| Event and session schemas named literally | `PASS` |
| Root daemon is sole active writer | `PASS` |
| Legacy App source is read/migrated lazily and non-destructively | `PASS` |
| No second active writer or authority replacement | `PASS` |
| App `UIEvent` streaming/replay are projections only | `PASS` |
| Question-bearing C-06 text removed from resolved full-file candidate | `PASS` |

## Candidate handoff

| State | Value |
| --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `AuthorityState` | `NO_NEW_AUTHORITY` |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` |
| `NextGateState` | `N2_COMPANION_REGISTER_REBUILD_THEN_FRESH_REVIEW` |

`ReadyForNextPhase = NO`.
