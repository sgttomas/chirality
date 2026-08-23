# Orchestration plan — R20 owner-proof closeout

- RunID: `APPDEV_LOGIN_PROOF_R20_CLOSEOUT_2026-08-23`.
- Package: PKG-09; selected deliverable: DEL-09-04.
- Basis: branch `codex/app-login-proof-r20-closeout`; HEAD/origin/main `75c4e2ba401a6f5ad0c2f38846c39db6ab157405`; frontend tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`; clean at activation.
- Selection authority: explicit owner direction in `CHAT_TRANSCRIPTION.md`.
- Posture: mixed, serialized fan-in. WORKING_ITEMS owns deliverable integration; TASK_MANAGEMENT is a sibling Agent-1 invocation owned by HELP_HUMAN and writes only the App Task Management register home.

## Nodes

1. `WP-01 EVIDENCE_CLOSEOUT`: one non-delegating Agent 2 reads only the exact Desktop source directory metadata and three named JSON files; verifies source safety/hashes/semantics; copies only those files to a private DEL evidence snapshot; authors successor R21, minimal status update, WP-00/G0.25 evidence-only assessment, and its instance return.
2. `WP-02 TASK_MANAGEMENT`: HELP_HUMAN invokes TASK_MANAGEMENT with mandatory federation preflight. It closes/updates only rows supported by accepted proof/repair evidence, harvests unsupported candidates without disposition, and preserves human-only judgment. Its writes are restricted to the App register home plus a unique return under this run.
3. `WP-03 FRESH_REVIEW`: after WP-01 and WP-02 freeze, a fresh non-delegating Agent 2 reviews proof snapshot identity/semantics, R21/status/gate calibration, Task Management legality, containment, and all fences without reading Desktop/private root or executing proof/product commands.
4. `WP-04 GOVERNANCE`: WORKING_ITEMS runs governance-only pre-push gates, freezes the Receipt-excluded content candidate, and hands it to CHANGE.
5. `WP-05 RECEIPT`: after CHANGE returns the immutable content commit, WORKING_ITEMS appends Receipt 194 and runs receipt-only gates.

No node may sign, notarize, deploy, distribute, publish, claim release readiness or owner acceptance, mutate frontend/package/procedure/operator state, query `com.chirality.runtime`, or read/stat/list/traverse `/private/tmp/ch-r18-91499728-51dd`.
