# TASK run — Node N packaged renderer CSP nonce

Date: 2026-09-04
Run: `APPDEV_V3_NODE_N_2026-09-04`
Basis: `307addfc259b046aeb2ed07d47086cd5686c35b8` (PR #694 merge)
Item: `DEL-09-06-V3-04` only
State: implementation frozen for independent review; no completion or acceptance claim

## Execution calibration

HELP_HUMAN directly dispatched a bounded Agent-2 implementer through delegated-harness-native execution. Agent-2 role was not mechanically enforced; governed-workflow role evidence is instruction-asserted; K-SUBAGENT/non-delegation is instruction+config asserted, not mechanism-proven. The implementer did not delegate and observed no descendants.

## Result

The packaged custom Next server now generates a cryptographically strong 128-bit base64 nonce for every request. One CSP value is built from that nonce, set on the request before Next renders, and attached byte-identically to the response. Next and the root layout read the same request CSP, so framework inline scripts and the app-owned theme bootstrap carry the enforced nonce without a second nonce-bearing header. Packaged `script-src` contains `'self'` plus the nonce and excludes `'unsafe-inline'` and `'unsafe-eval'`; every other directive is preserved. Development retains its prior exact static policy and HMR posture.

The packaged proof now launches real hardened BrowserWindows for `/`, `/chat`, `/pipeline`, and `/workbench` only when its existing probe environment is enabled. It requires one result per route, two fresh responses per route, globally unique observed nonces, matching inline-script nonces, exact directive closure, the deliberate enforced connect denial, no unexpected/own-resource CSP violations, and enough window-open/navigation denials for the full route set. The ordinary desktop path still launches one root window.

Implementation decision: use the CSP request header itself as the single nonce source for Next and the layout. A companion nonce header was prototyped and removed before the final proof because it could disagree with the enforced policy. Static Electron packaged fallback and hash/SRI were rejected for the reasons recorded in `Evidence/Node_N_CSP_Nonce_2026-09-04/EVIDENCE.md`.

## Evidence and checks

- `Evidence/Node_N_CSP_Nonce_2026-09-04/packaged-security-proof/`: final real packaged PASS. Four route payloads; 12 observed nonces all unique; every inline script nonce matches; packaged unsafe script allowances absent; unexpected violations none; non-allowlisted TCP none; cleanup PASS. Unsigned artifact identity `21caf9abd8b0d90a31c6d784e48575e5a276a1ae9131106fd418790aa4be0686`.
- `Evidence/Node_N_CSP_Nonce_2026-09-04/section8-local/`: final Node H lifecycle PASS on the frozen candidate bytes; premerge and release-quality exit 0; coalition cleanup PASS.
- `Evidence/Node_N_CSP_Nonce_2026-09-04/timing-observations.json`: same-method pre/post static-to-dynamic timing observations with no threshold or pass/fail inference.
- `Evidence/Node_N_CSP_Nonce_2026-09-04/secret-scan-summary.json`: PASS, zero blocked findings.
- Focused Vitest PASS (three files, 97 tests); full Vitest PASS (165 files + one skipped; 1,567 tests + four skipped); typecheck PASS; build PASS; `desktop:pack` PASS; registered premerge/release-quality PASS; D-APP-36 packaged render bar PASS; harness self-check and 350-test pytest PASS; APP-HOLD ALLOW/integrity PASS; corpus v20 no drift; receipts validator VALID read-only; ScopeOfWork PASS; exact change scope PASS; F-APP-2 scan PASS; manifests and `git diff --check` PASS. Initial operational failures and their successful rerun dispositions are recorded without passing inference in `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_N_2026-09-04/CHECKS.json`.

## A1 and remaining gates

This `frontend/` mutation invalidates the staged R20 procedure for future proof reliance. Historical R20 remains historical only; a newly staged revision and fresh owner-executed proof are required before future reliance. Node N does not perform or claim the separate `DEL-09-01-V3-01` revision 3 that becomes owed only after this change lands.

DEL-09-06 `_STATUS.md`, `MEMORY.md`, and `loop/LOOP_RECEIPTS.md` remain unchanged pending fresh independent review and separately authorized closeout. No signing, notarization, publication, external distribution, release-readiness, lifecycle issuance, or owner-merge act occurred.
