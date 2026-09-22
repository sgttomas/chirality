# DEL-05-02 reverse notes: worker A, pass 2

The sealed ledger is unchanged: SHA-256 `9f8a6a1f3b512e05bd38b657bd95a6c8546b606178f681bbdb8556208a759a99`.

## Scope and totals

- **Capability files answered, in order:** BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL, WOVEN. That is 413 capabilities.
- **Responses:**

  | Response | Capabilities |
  |---|---:|
  | CLAIMED_BY | 3 |
  | PARTIAL | 15 |
  | NOT_MINE | 395 |

- **Errata:** none. The census stays as sealed, so there are no errata-applied figures.

## Ownership reading used

- DEL-05-02 claims three things:
  1. the HarnessEvent envelope and vocabulary (RTCONTRACT-022);
  2. the Runtime event journal and replay (RTCORE-017);
  3. the legacy App `session-events.ts` artifacts (HARNESS-038).
- The SCA-APP-010 applied row makes generic persistence Runtime-owned. The SoW requirements RQ-001..015 still describe these behaviours, so my claim covers what the requirements specify, not code ownership.
- PARTIAL responses cover capabilities that other deliverables own but where one DEL-05-02 row judges a part. Examples:
  - replay diagnostics (DEL-05-04 owns replay);
  - terminals (PKG-03 owns terminal handling);
  - the D-GOV-43 notification representation, which gates REM-1;
  - large-payload artifacts (DEL-05-05).

## Coverage gaps (forward rows missing)

- **CAP-SHELL-039, CAP-WOVEN-033:** the App's normalized views of `codex.notification` are live. The only forward row that covers them is REM-1, which is an open REMAINING_WORK item. No row records the delivered part. This was noted in forward notes §Coverage gaps and stays open for the manager.
- **CAP-RTCONTRACT-024:** closed schema v2 wire validation still ships and is live, although D-APP-127 retired the closed vocabulary. The only forward row touching it is SEC-2, and that row judges the deliverable text, not the retained module. Whether retaining the module is correct is not owned by any DEL-05-02 row.
