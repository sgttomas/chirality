# DEL-07-06: reverse-pass notes (pass 2)

- **Capability files:** BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, SETTINGS and WORKSPACE, in that order. Together they hold 314 capabilities: 309 are `NOT_MINE`, 5 are `PARTIAL` and 0 are `CLAIMED_BY`.
- **Validation:** the validator passes against each of the seven capability files with 0 errors and 0 warnings.
- **Errata:** none. The sealed ledger is unchanged (SHA-256 `f61e4900…1111fee`), so there are no errata-applied figures to report. The census stays as sealed: 30 ALIGNED, 19 STALE_SPECIFICATION, 7 NOT_AUDITABLE, 2 PARTIALLY_IMPLEMENTED, 1 STALE_ASSESSMENT.

## Why no CLAIMED_BY

DEL-07-06 is a DOC_UPDATE convention deliverable. The code it relies on is owned elsewhere:

| Code DEL-07-06 relies on | Owning deliverable | DEL-07-06 claim it covers |
|---|---|---|
| Document-kit and reference scanner (CAP-WORKSPACE-013 and -017) | DEL-07-03 | REQ-002 and REQ-005 |
| Status-transition approval-SHA gate (CAP-ROUTES-032, CAP-SETTINGS-025, CAP-WORKSPACE-022) | DEL-07-04 | REQ-011 |
| Dependencies.csv reader and writer | DEL-07-05 | — |

Each of the first two rows is marked `PARTIAL`, keyed to the DEL-07-06 claim it covers.

## REACH and STATE agreement

No capability file's REACH or STATE disagrees with my ledger or with the evidence pack:

- **Reference scanner:** CAP-WORKSPACE-013 and -017 are LIVE and ENABLED. This matches my trace from the route handler.
- **Transition gate:** CAP-ROUTES-032, CAP-SETTINGS-025 and CAP-WORKSPACE-022 are LIVE and ENABLED. This matches CLM-010.11.
- **Legacy MCP tool:** CAP-HARNESS-051 is LEGACY_ONLY. This matches the MCP citation `read-tools.ts:938` on CLM-010.11.
- **Transition UI callers:** CAP-WORKSPACE-025, -026, -032 and -034 are STATE=DISABLED, RETIRED-UNMOUNTED. This settles the point CLM-010.11 left unchecked: the only UI callers of the transition route are not mounted, so the live entry is the route handler alone. The row's REACH=LIVE is still correct, and I file no erratum.

## Surface gap (for the manager)

None of the seven files covers the execution-tree governance tooling that REQ-003, REQ-004 and REQ-012 rely on:

- `execution/_Scripts/references_hash_tool.py`: ContentHash compute and verify, plus the `HASH_VERIFICATION_BYPASS.jsonl` writer;
- `execution/_Scripts/validate_dependencies.py`: the Dependencies.csv v3.1 linter;
- `execution/_Reconciliation/References/reconcile_authority_corpus.py`: the D-APP-38 corpus snapshots and apply.

These tools are not product code, so the gap is expected. It does mean that no capability row checks the K-REF-1 tooling, and that the stale corpus (v23 against the live docs) appears only in my REGISTER-1.

CAP-BUILD-036 and CAP-RTCONTRACT-043 are the harness MCP tool catalog. They are not the project tools and scripts registry that REQ-013 and REQ-016 name, so both are `NOT_MINE`.
