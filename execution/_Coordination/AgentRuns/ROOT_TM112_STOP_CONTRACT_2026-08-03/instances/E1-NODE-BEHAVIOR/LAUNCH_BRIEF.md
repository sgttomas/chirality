# SEALED BRIEF — E1-NODE-BEHAVIOR

Agent type/form: Agent 2 ephemeral generalist; no delegation.  
Parent: HELPS_HUMANS.  
Purpose: establish primary installed-runtime behavior relevant to a bounded
RuntimeDaemon graceful-stop contract.

## Authority and context

- Owner ruling transcript SHA-256:
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
- Read: `runtime/package.json`, lockfile, installed Node executable/API/type
  declarations, `runtime/packages/daemon/src/runtime-daemon.ts`, N1 fixtures and
  raw evidence under `../ROOT_TM112_DECISION_PREP_2026-08-03/**`.
- Node bound at launch: v24.18.0; runtime support floor: `>=22.19.0`.

## Objective

Using read-only inspection and bounded disposable `/tmp` probes, determine
exact semantics and ordering consequences of `server.close()`,
`closeIdleConnections()`, `closeAllConnections()`, socket destruction, and
repeated stop/start on Node v24.18.0. Address incomplete HTTP requests, completed
keep-alive, live SSE, upgraded connections if relevant, close callback errors,
and what server APIs do not guarantee. Identify Node-version/platform caveats.

## Permissions and outputs

- Tools: read, shell probes in `/tmp`, write only this instance directory.
- Do not modify runtime source/tests, docs, registers, App content, lifecycle,
  or Git. Do not use network. Do not delegate.
- Output `RETURN.md`, `EVIDENCE.md`, and any small probe fixture/raw output
  needed for reproducibility.
- Calibrate executable observations separately from API declaration inference.

## Acceptance

Every material claim cites a local path, exact command/output, or installed
declaration. Recommendation is allowed but is non-authoritative. State gaps.

