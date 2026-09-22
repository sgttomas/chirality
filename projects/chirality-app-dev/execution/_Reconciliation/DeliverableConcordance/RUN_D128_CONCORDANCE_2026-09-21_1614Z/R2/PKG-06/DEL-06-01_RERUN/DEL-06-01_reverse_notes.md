# DEL-06-01 reverse-pass notes (rerun, pass 2)

This pass answered 413 capabilities from 9 files: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT,
RTCORE, SETTINGS, SHELL and WOVEN.

| Response | Count |
|---|---:|
| CLAIMED_BY | 2 |
| PARTIAL | 17 |
| NOT_MINE | 394 |

- **CLAIMED_BY:**
  - CAP-HARNESS-043 (the permission overlay module) maps to CLM-009.1.
  - CAP-RTCONTRACT-019 (the permission mode to Codex policy mapping) maps to CLM-004.
- **PARTIAL:** these rows cluster on the live approval-mediation chain. The chain runs through
  the UI cards, the client, the App route and proxy, the Runtime route, the Codex server
  requests and the `tool.permission` projection, and maps to CLM-009.7 and CLM-009.10. The other
  PARTIAL rows cover:
  - the mode selector and the dontAsk mapping (CLM-004, CLM-009.6);
  - runtime tool restriction (CLM-009.12);
  - the Agent class (CLM-015.1);
  - the coordination descriptor class (CLM-034.1);
  - the SDK bypass gate (CLM-009.9).
- **Errata:** none. Every forward row read against these capabilities still holds.
- **Coverage gaps:** none in scope.
  - The live default operator mode (workspaceWrite, with approval never) is already recorded as a
    cross-deliverable observation on CLM-027.
  - CAP-SETTINGS-042 (the deprecated harness-contract facade) is answered NOT_MINE because
    DEL-03-01 owns it. CLM-034.1 cites the facade only as a stale evidence pointer.
- **Census:** no errata, so the sealed figures are also the errata-applied figures.
- **Seal:** the claims SHA-256 is unchanged at
  `461799194da83088b879714bf1773517c017d181555efc8aff9749f3cd012d8a`.
