# Canonical replay restart proof — 2026-08-17

- Run: `APPDEV_CANONICAL_REPLAY_RESTART_2026-08-16`
- Candidate: `frontend/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts`
- Frozen blob: `310e0c9539dbac6af89159bd312b2a93a082689b`
- Product result: a real daemon, authenticated Desktop compatibility port, and
  Root `runCli session replay --json` façade with captured/decoded CLI output
  lazily migrate the same legacy manager/child sessions, preserve legacy bytes,
  replay structurally equal parsed canonical records, and do so again after a fresh service
  restart over the same runtime directory. Exact recorded roles,
  `parentSessionId`, event order, and engine attribution are asserted. Woven
  hierarchy reconstruction remains correct with child-first input.
- Source result: no App-owned defect was exposed; no runtime-client or Woven
  source change was necessary. Root runtime remained read-only.
- Focused test: PASS after CLI-boundary remediation, 1 file / 1 test,
  worktree-correct Root aliases, 261 ms total and 76 ms test. The earlier
  RuntimeClient-only candidate is superseded.
- Typecheck: PASS for frontend and Electron configs using worktree-correct Root
  aliases. One temporary alias omission for `@chirality/engine-claude` was
  corrected before the exact passing rerun; this was environment setup, not a
  product defect.
- Narrow checks: change-scope PASS (one path, zero violations), candidate
  whitespace PASS, APP-HOLD integrity PASS, harness self-check PASS.
- Review: the node-local independent `software-code-review` passed over 100% of
  the frozen one-file diff. Integrated review then blocked an evidence-wording
  overclaim and accepted this calibration: parsed replay objects are
  structurally/value equal; only the preserved legacy source files are proven
  byte-identical. A second integrated finding rejected the original use of a
  second `RuntimeClient` as CLI evidence; the accepted fixture crosses the
  actual Root `runCli` argument parsing, client call, JSON rendering, capture,
  and decode boundary before and after restart.
- Review backcheck: PASS with no remaining findings after legacy file capture
  and comparison changed from decoded UTF-8 strings to raw `Buffer`s.
- Containment: temporary alias configs and `frontend/node_modules` symlink were
  removed. Concurrent PKG-08 changes were excluded from this node.
- Residual risk: migration concurrency/races, malformed legacy tails, and CLI
  argument parsing/packaging are outside this sealed proof.
- Rerun triggers: Root daemon/client/session migration/replay contracts; App
  runtime-client compatibility port; Woven recorded-hierarchy logic.
- Verdict: the DEL-05-04 daemon/client replay residual is closed. Lifecycle
  remains IN_PROGRESS; this is not release or lifecycle-transition evidence.
