# DEL-09-07 — reverse-pass notes

Capability file: `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows, area HARNESS).

## Responses

All 60 capability rows are `NOT_MINE`. This deliverable was a LaunchAgent two-job
installer/migration/rollback transaction. D-APP-127 retired it and no code was ever
built for it. None of the HARNESS capabilities touch launchd, installers, staging,
journals, effective-state inspection or rollback. That set covers:

- the harness client;
- SSE routes;
- engines and adapters;
- the session store;
- permissions and tool policy;
- MCP tools;
- delegation;
- plans and drafts.

The nearest live analogues sit in `frontend/electron`, outside the HARNESS area:

- App-owned Runtime service lifecycle (`runtime-service-host.ts`);
- the restart-only runtime-control IPC (`runtime-control-ipc.ts`).

A `CLAIMED_BY` or `PARTIAL` answer might fit those if another area's capability file
lists them. At most it would be `PARTIAL` against SEC-1.5 or SEC-4.1, the single-owner
value. It would not be a claim on the retired installer outputs.

## Forward-row errors exposed

No forward-row errors were exposed.

## PostReleaseBasis revisit (calibration finding)

In the forward pass, `PostReleaseBasis = NO` was set by assumption, on the basis of
dates. The permitted read-only check below confirms it.

- **Command.** `git show --stat` on each of the four post-v3.0.1 commits: `da95ec194`,
  `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a`.
- **Result.** None of the four commits touches any file the forward ledger relied on.
- **Files checked:**
  - `runtime-control-ipc.ts` and `runtime-service-host.ts`;
  - `api-key-ipc.ts`;
  - `runtime-control-ipc.test.ts`, `runtime-service-host.test.ts` and `runtime-connectivity.test.ts`;
  - `projects/chirality-runtime/packages/cli/test/cli.test.ts`;
  - the DEL-09-07 folder;
  - `APP_HOLD_REGISTER.csv`;
  - the D-APP-127 record;
  - the HANDOFF and APP_EXECUTION_RETURN carriers;
  - the App PRD, SPEC and CONTRACT;
  - the decomposition.

Effect: none. All 31 forward rows correctly carry `NO`.

For calibration, the assumption happened to be right here. This does not make
date-based inference safe in general.
