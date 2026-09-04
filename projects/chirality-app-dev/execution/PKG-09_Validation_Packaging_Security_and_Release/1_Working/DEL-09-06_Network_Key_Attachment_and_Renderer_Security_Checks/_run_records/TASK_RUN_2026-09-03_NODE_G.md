---
run-id: TASK_RUN_DEL-09-06_2026-09-03_NODE_G
timestamp: 2026-09-03
run-status: SUCCESS (frozen for independent review in one local commit; closure recorded at closeout)
control-surface: FILE
scope-path: projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks
task-profile: NONE
task-skill: software-bounded-implementation
resolved-skill-path: skills/software-bounded-implementation
resolved-skill-version: "1"
parent-run: execution/_Coordination/AgentRuns/APPDEV_V3_NODE_G_2026-09-03
executor: Claude Fable 5.1 (claude-fable-5-1), ephemeral Agent 2 under HELP_HUMAN
item: DEL-09-06-V3-05
basis: e59efa4830fb54143c86e511ec35a6d1a476f72e
---

## Requested Tasks

- Close residual R-B of DEL-09-06-V3-01: make the packaged-proof egress-layer probe
  unable to request any destination the REQ-NET-001 egress policy would allow — either by
  refusing allowed URLs or by hard-coding the `:8443` probe and dropping
  `CHIRALITY_EGRESS_LAYER_PROBE_URL` (the brief's preference unless the variable is needed).
- Unit tests proving the probe refuses or cannot be pointed at any allowed URL; the
  packaged proof still observing `egressLayerDiagnostics > 0`; proof script and its test
  updated; whole-directive CSP check untouched; contract pins updated deliberately.

## Outputs Produced

- `frontend/electron/renderer-window-policy.ts`: exported `EGRESS_LAYER_PROBE_URL`
  (`https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked`);
  `runEgressLayerProbe` requests only that constant, reads the environment only for the
  gate and delay, logs the destination with its port and no path. `main.ts` unchanged.
- `frontend/scripts/run-packaged-security-proof.mjs`: exported `EGRESS_PROBE_URL` (same
  literal, the summarizer's expectation) and `EGRESS_PROBE_DECOY_URL`
  (`http://127.0.0.1:9/…`, set in the retired variable as a negative control); exact
  destination match incl. port; `egressProbeUnexpectedDestinations` must be empty.
- Tests: `renderer-window-policy.test.ts` egress block rewritten (65 cases in file);
  `run-packaged-security-proof.test.ts` cross-check and negative cases (10 in file);
  `contract-pins.manifest.ts` pins replaced/added on three targets (listed in
  `Evidence/Node_G_Egress_Probe_Restriction_2026-09-03/EVIDENCE.md` §3).
- Evidence: `Evidence/Node_G_Egress_Probe_Restriction_2026-09-03/` (`EVIDENCE.md`;
  `packaged-security-proof/` with `MANIFEST.sha256`; bundle identity `e716439f…`).

## Design decision (recorded; disposition-class, inside the seated locus)

- **D1 (parent run `COORDINATOR_DECISIONS.md`)** — hard-code the destination and drop the
  variable rather than filter it: the variable is needed by nothing (proof script constant,
  CI passes no override, network proof and docs do not use it); a constant cannot be
  redirected, whereas a refuse-if-allowed predicate would have to mirror the unexported
  `main.ts` policy and could drift. Rejected: option (a) keep-and-filter. The proof keeps a
  loopback decoy in the retired variable so a regression is visible on the wire without
  any request leaving the host.
- Payload shape: the egress-probe log now carries `port` (protocol + hostname + port; no
  path), matching the shape `main.ts` already logs for denied requests, so the proof can
  bind the observation to the non-allowlisted port rather than to the hostname alone.

## Checks

Parent `CHECKS.json`: typecheck pass; full Vitest pass (162 files / 1493 tests, 4
skipped); focused pass (91); build pass; `desktop:pack` pass; packaged security proof pass
in-sandbox (`egressLayerDiagnostics: 1`, probe payload `:8443` rejected,
`egressProbeUnexpectedDestinations: []` with the decoy set); premerge FAIL in the recorded
absent-runtime-daemon-bindings class (8/8 HTTP 503; `FAIL_DEFERRED_TO_PR_CI`, Receipts
172/177), no pass inferred; `git diff --check`, harness self-check, pytest (350), APP-HOLD
dispatch preflight and register-match scan, corpus status (no drift), receipts validator,
and exact change-scope validation pass.

## A1 re-stage declaration

Recorded in the parent run's `STEP0_DISCOVERY.md` §3: this tranche's `frontend/` mutation
invalidates the staged R20 procedure for any future proof claim and requires a newly
staged revision and a fresh owner-executed proof; the 2026-08-23 R20 PASS stands as
historical evidence only.

## Residuals

Recorded in the parent `RETURN.md` §5. No new deliverable residual is named by this
tranche: R-B is closed by construction; R-A (DEL-09-06-V3-04, nonce CSP) is unchanged and
still owner-gated.
