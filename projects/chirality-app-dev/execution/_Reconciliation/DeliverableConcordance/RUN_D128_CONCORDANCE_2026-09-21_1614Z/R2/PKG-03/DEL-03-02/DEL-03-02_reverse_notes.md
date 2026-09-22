# DEL-03-02 reverse-pass notes

## What was answered

- 370 capabilities from 8 capability files, answered in this order: BUILD, ELECTRON, HARNESS, ROUTES,
  RTCONTRACT, RTCORE, SETTINGS, SHELL.
- Responses: CLAIMED_BY 4, PARTIAL 13, NOT_MINE 353.
- Every file passes `reverse` validation with 0 errors.

## How ownership was decided

- **CLAIMED_BY** covers only the App-side client surfaces the current contract gives this deliverable:
  - the turn route (CAP-ROUTES-007);
  - the port registry that keeps the routes clients of the Runtime service (CAP-SETTINGS-027);
  - the session create/boot proxy (CAP-SETTINGS-030);
  - the legacy App TurnEngine module (CAP-HARNESS-030), which the ledger records as UNREACHED.
- **PARTIAL** covers Runtime-owned behaviour. The SoW's SEC-1 says DEL-03-02 verifies this behaviour but does
  not own it:
  - the one-active-turn lock and terminal handling (CAP-RTCORE-019/020);
  - accepted-turn commit (CAP-RTCORE-017);
  - legacy session migration (CAP-RTCORE-015);
  - Runtime boot (CAP-RTCORE-041).
  PARTIAL also covers surfaces this deliverable shares with a neighbour: the SSE proxy (DEL-03-03) and the turn
  proxy, where interrupt and steer are DEL-03-04's.
- **NOT_MINE** was answered on these surfaces even though they relate to this deliverable:
  - Engine port and conformance contracts (CAP-RTCONTRACT-036/039): DEL-03-01's (upstream edge DEP-03-02-006).
  - Interrupt, attach and turn-state routes: DEL-03-04's.
  - Managed delegation (CAP-HARNESS-056): DEL-08-04's, although REM-1 depends on it.
  - Shell chat lifecycle: UI.

## Errata

None. The reverse pass found no sealed forward row that needs correcting. The claims SHA-256 is unchanged:
`04397db5ee06f1edf64d1e7c4b031ffa5450c9de170353897c948b5fa4627f5f`.

## Coverage gaps

None found. Every PARTIAL or CLAIMED_BY capability maps to an existing forward row.
