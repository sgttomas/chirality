# DEL-03-03 reverse-pass notes (R2, PKG-03)

This pass answered 370 capabilities from 8 files, taken in this order: BUILD, ELECTRON, HARNESS,
ROUTES, RTCONTRACT, RTCORE, SETTINGS and SHELL.

## Responses

| Response | Count |
|---|---:|
| CLAIMED_BY | 9 |
| PARTIAL | 22 |
| NOT_MINE | 339 |

**CLAIMED_BY.**

- Route shapes are claimed by CLM-003.2:
  - CAP-ROUTES-001 to 005;
  - CAP-ROUTES-021.
- The turn route is claimed by CLM-003.3 (CAP-ROUTES-007).
- The browser SSE proxy and re-attach are claimed by REM-1 (CAP-HARNESS-024 and CAP-ROUTES-008).
- Route-side helpers are claimed by CLM-009.2 (CAP-HARNESS-023).

**PARTIAL.** These rows cover Runtime-side or UI-side halves of DEL-03-03 behaviour. Their primary
owners are elsewhere:

- DEL-03-02 owns the lock.
- DEL-03-04 owns the interrupt outcome.
- PKG-05 owns the event vocabulary.
- PKG-04 and DEL-04-03 own the mappers.
- DEL-05-04 and PKG-02 own presentation.

## Errata

There are none. The capability notes agree with the sealed evidence on every point checked:

- **CAP-HARNESS-024 and CAP-RTCONTRACT-006.** The 15 s proxy keepalive and the rule that cancel only
  unsubscribes match E_DISC. The capability describes a 25 s stream-transport inactivity deadline
  "counting heartbeats". This is consistent with the sealed citation of `client.ts:196-212`, which
  describes an opening deadline plus an idle timeout that resets on bytes.
- **CAP-HARNESS-039.** The HARNESS-UI bridge is LEGACY_ONLY and disabled, which matches the sealed
  REACH tags.
- **CAP-RTCORE-029.** Notifications are forwarded unchanged, which supports CLM-003.6 and REM-1.

The sealed ledger SHA-256 is unchanged: `0bf94ffb2073063e9a44ff54aaadf3b0ea20a58356097b6ffddd22cfa5ee993d`.
With no errata, the sealed and errata-applied census figures are identical (see `DEL-03-03_notes.md`
§1).

## Coverage observations for the manager

These are not errata.

- **Live routes outside the SoW and the SPEC 17.1 catalog.** CAP-ROUTES-008 (turn re-attach stream)
  and CAP-ROUTES-009 (turn state) are live v3 `/api/harness/*` routes. The SoW lists neither route,
  and SPEC 17.1 catalogs neither. They are covered only through `_STATUS` V3-01 (REM-1).
- **Steering route.** CAP-ROUTES-010 (mid-turn steering) is also missing from SPEC 17.1. I answered
  it NOT_MINE because it is a native-steering feature, not a compatibility surface.
- **Uncataloged routes generally.** A future SoW revision should decide which uncataloged
  `/api/harness/*` routes DEL-03-03 owns.
- **Legacy validation check IDs.** CAP-BUILD-026, the section-8 live API smoke check, still uses legacy
  Agent SDK check IDs such as `sdk_native_stream`. It is the nearest thing to a route-shape
  regression check. The SoW's fixture-capture and replay verification (CLM-009.1) remains
  unimplemented.
