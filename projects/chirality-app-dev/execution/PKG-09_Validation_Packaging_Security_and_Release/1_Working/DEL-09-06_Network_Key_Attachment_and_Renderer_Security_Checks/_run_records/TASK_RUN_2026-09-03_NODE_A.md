---
run-id: TASK_RUN_DEL-09-06_2026-09-03_NODE_A
timestamp: 2026-09-03
run-status: SUCCESS (frozen for independent review in two local commits; closure recorded at closeout)
control-surface: FILE
scope-path: projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks
task-profile: NONE
task-skill: software-bounded-implementation
resolved-skill-path: skills/software-bounded-implementation
resolved-skill-version: "1"
parent-run: execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03
executor: Claude Fable 5.1 (claude-fable-5-1), ephemeral Agent 2 under HELP_HUMAN
item: DEL-09-06-V3-01
basis: 0c683fb1657706316272951e4c3a0f7781b46009
---

## Requested Tasks

Round 1 (commit `4e4c7e9090891fae98bb63ebf1ee8e3561d4f9ac`):
- Adopt the `runtime-control-ipc.ts` sender-origin policy on all six credential IPC
  handlers through one shared module; plumb `rendererOrigin` from `main.ts`; deny with a
  typed secret-free result and a desktop-log line; unit-test every channel both ways.
- Inventory G-CSP renderer-hardening coverage.

Round 2 (coordinator disposition: the seated item's write locus — `frontend/electron/**`
window/CSP policy, packaged security tests — and its Return contract govern over the
narrower launch-brief line; second local commit on the same branch):
- `frontend/electron/renderer-window-policy.ts`: pure policy plus installer for every
  BrowserWindow — asserted web preferences (fail closed), deny-all `setWindowOpenHandler`,
  renderer-origin-only `will-navigate`/`will-redirect`, and the renderer CSP.
- CSP on the packaged renderer server responses and via `onHeadersReceived` for both modes.
- Unit tests, contract pins, and packaged-proof extension showing the CSP header on the
  packaged page and denied `window.open`/navigation attempts.

## Outputs Produced

- Round 1: `ipc-sender-policy.ts`, `api-key-ipc.ts`, `runtime-control-ipc.ts`, `main.ts`
  plumbing; tests (17 + 58; pins).
- Round 2: `renderer-window-policy.ts` (new); `main.ts` window creation from the policy,
  packaged server CSP header, probe hook; `scripts/run-packaged-security-proof.mjs`
  (renderer-hardening evidence summarizer, `:8443` egress probe, three new markers,
  truncating log writer); tests `renderer-window-policy.test.ts` (38),
  `run-packaged-security-proof.test.ts` (+2), pins on three targets.
- Evidence: `Evidence/Node_A_Credential_IPC_Sender_Authorization_2026-09-03/`
  (`EVIDENCE.md`; `packaged-security-proof/` round 1; `packaged-security-proof-2/`
  round 2; each with `MANIFEST.sha256`).

## Design decisions (recorded; disposition-class, inside the seated locus)

- CSP `connect-src` lists `https://api.anthropic.com:*` rather than the exact egress origin
  so the REQ-NET-001 egress layer remains reachable and independently observable in the
  packaged proof (which now drives `https://api.anthropic.com:8443/…`); the egress layer
  still enforces `https:443` exactly. Rejected: an exactly-equal CSP, which would have
  turned the proof's egress observation into a CSP observation without anyone noticing.
- `script-src 'unsafe-inline'` because Next's App Router ships 8 inline flight-payload
  scripts per page and a nonce pipeline needs a middleware outside this locus; `'unsafe-eval'`
  only in development. Rejected: `script-src 'self'` alone (verified to be incompatible
  with the built HTML).
- Navigation policy requires `http(s)` before origin equality because `blob:` URLs carry the
  renderer's own origin — found by the unit matrix, not assumed.
- Proof log writer changed from append to truncate: the new log-derived checks must never be
  satisfiable by a stale earlier run's bytes (observed once during this run and re-run
  into a clean output root).

## Checks

Parent `CHECKS.json` (both rounds): typecheck pass; full Vitest pass (round 2: 158 files /
1408 tests, 4 skipped); focused pass; build pass; premerge FAIL in the absent-runtime-
daemon-bindings class both times (deferred to PR CI, no pass inferred); `desktop:pack`
pass; packaged security proof pass in-sandbox with renderer-hardening evidence; diff
--check, self-check, pytest, APP-HOLD scan, scope validation pass.

## A1 re-stage declaration

Recorded in the parent run's `STEP0_DISCOVERY.md` §3: this tranche's `frontend/` mutation
invalidates the staged R20 procedure for any future proof claim and requires a newly
staged revision and a fresh owner-executed proof; the 2026-08-23 R20 PASS stands as
historical evidence only.

## Residuals

Recorded in the parent `RETURN.md` §5 (development-mode CSP not observable by the packaged
proof harness; `will-redirect` and subframe navigation covered at unit level / by
`frame-src 'none'` only; nonce-based script CSP as a possible follow-on).

## Round 3 (independent review: 0 blocking / 2 major / 4 minor; all applied)

- MAJOR-1 / coordinator decision D2: child windows are still never created; `http(s)`
  targets of the renderer's `target="_blank"` links (`chat-markdown.tsx:26`,
  `navigator.tsx:321`) now open in the system browser via injected `shell.openExternal`;
  other schemes are dropped; logs distinguish `external_opened` / `denied`; the false
  "never opens windows" statements were corrected and the behaviour change disclosed.
- MINOR-2 / D3: packaged `connect-src 'self'` (exact); egress-layer observation moved
  to a main-process `session.fetch` probe (`[egress-layer-probe]`), cancelled by
  `onBeforeRequest` with `ERR_BLOCKED_BY_CLIENT`; the `:*` pin replaced by the exact one.
- MINOR-3: header helper returns `null` when untouched; installer calls `callback({})`.
- MINOR-4: exact `validate_change_scope.py` invocation recorded in `CHECKS.json`.
- NOTE-1: dead probe logger dropped. NOTE-2: inline-script count corrected (8 inline
  elements per page, 6 of them flight pushes). Limitation of `'unsafe-inline'` stated
  plainly in `EVIDENCE.md` §1.
- Proof run 3 retained under `Evidence/.../packaged-security-proof-3/` (identity
  `7f240a36…`); runs 1–2 retained as history.
- Named residuals for the closeout `Remaining`: nonce-based script CSP follow-on (see
  parent `RETURN.md` §5).
