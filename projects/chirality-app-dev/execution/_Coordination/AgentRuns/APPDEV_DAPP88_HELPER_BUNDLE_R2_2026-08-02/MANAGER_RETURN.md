# WORKING_ITEMS manager return — D-APP-88 Option B R2

## Verdict

`BLOCKED / PARTIAL — STANDALONE TARGET DIAGNOSTIC ACCEPTED; PRODUCT ROLLED BACK`

D-APP-88 Option B remains open. R2 proved that a separately built full Electron helper target is structurally coherent, but it did not produce the mandatory auditable post-GUI first-signal graceful-stop proof. No implementation is accepted and no weakening of the ruling is inferred.

## What R2 established

- A separate electron-builder configuration produced `Chirality Runtime Service.app` with canonical helper bundle ID `com.chirality.app.runtime-helper`, its own product/executable name, `LSUIElement=true`, and four builder-generated Chromium child applications.
- The `Service` name is an exact builder constraint response: electron-builder reserves a terminal `Helper` suffix and strips it from the main executable name.
- The finished helper bundle was embedded whole at the GUI package's `Contents/Library/LoginItems/` location; it was not constructed by copying or mutating the GUI bundle and used no signal wrapper.
- GUI identity remained `com.chirality.app`; exactly one top-level helper was embedded; all 14 links were relative.
- Standalone and embedded derivative trees matched across 812 descendants (446 files, 352 directories, 14 symlinks), canonical SHA-256 `3009a81765d3fd923b6b37d7578367027432b4b1c341bb0170bc247722ef75b3`.
- Focused tests (30/30), typecheck, Electron build, separate helper build, clean desktop package, dependency boundary, instruction-root integrity, package identity/topology/relocatability, and fresh first-signal graceful shutdown passed before the terminal gate.

## Exact blocker and limitations

Final single-process bits directly logged a fresh graceful shutdown. After helper restart and GUI contact, retained logs contain no later daemon-shutdown entry and the GUI later reports transport loss. The run did not preserve a contemporaneous signal command, process-survival snapshot, or socket snapshot, so first-signal survival/socket retention and second-signal termination remain unauditable operator observations. The accepted blocker is therefore narrow: R2 failed to produce auditable evidence that post-GUI first-signal graceful teardown satisfies D-APP-88.

The standard-process arm was also observed to fail but has no retained raw artifact and remains an unauditable observation only.

R2 stopped at the terminal preservation gate. It did not complete full frontend/premerge/release-quality, safeStorage, shared project/session, real LaunchAgent, or later recovery conjuncts. Tool Policy Compliance is `FAIL`: direct npm/Electron/macOS/telemetry commands exceeded the selected skill's five-command allowlist even though the sealed brief requested those validations. This process defect is disclosed and prevents a compliant-run claim.

## Root coordination request

The source sequence and logs support—but do not prove—a Root hypothesis: an active GUI Unix-socket/SSE or other long-lived connection may hold Root's awaited `server.close()` open and prevent App teardown completion. The draft Root investigation request is `DRAFT_NOTICE_TO_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION_2026-08-03.md`. It remains unrouted on the App run surface for `HELP_HUMAN`; no foreign write occurred.

## Integration and preservation

- All R2 product/config/test additions are absent and all touched existing R2 files match the restored D-APP-89 predecessor.
- The only remaining `package.json` delta is D-APP-89's independent removal of `@chirality/harness-contract`.
- Root tracked state and the reversible dependency projection are restored; Attempt 1 is unchanged.
- D-APP-89 zero-consumer/rollback guards hold; all six D-APP-81 UNKNOWN relations remain unchanged.
- DEL-09-04 remains `IN_PROGRESS`; Checking Approval SHA is unchanged.
- No R2 process, launchd job, temporary tree, token/credential artifact, decision/register/TM/receipt/completion-log, PRD/decomposition/SCA, foreign-loop, Git, signing, notarization, publication, distribution, release, or lifecycle effect remains.
- The exact untracked standalone derivative `frontend/dist-runtime-helper/` was removed after verifier hash freeze; it is rebuildable from frozen candidate evidence. Shared ignored `frontend/dist/` was left untouched for concurrent validation and is not current product truth.

## Accepted evidence

- Corrected implementation return: `instances/A2-DAPP88-R2-IMPLEMENT-01/RETURN.md`, SHA-256 `8ae2d74fae740b287e94b5730f0222a3fa4047e0f3e4c591e5af883462dbd49e`.
- Correction return: `instances/A2-DAPP88-R2-IMPLEMENT-01/CORRECTION_RETURN.md`, SHA-256 `279e9ead4f0a9b1e5e402b2420c0331511e364440827181a9b4f09a0a13ad49d`.
- Drill report: `instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/DRILL_REPORT.md`, SHA-256 `0ea6c32de0ed122750d2c759e9aee1a163d4275509c6861258c34f5203c09275`.
- Candidate manifest: `instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/CANDIDATE_SOURCE_MANIFEST.md`, SHA-256 `3825ea84fe0f1a4b3fddfe1d5046bcbfa13dbad688a6475087b3ecac2b0bc204`.
- Package manifest: `instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/PACKAGE_MANIFEST.md`, SHA-256 `599f0b54a057aac8e52e796a2c76724b68b8b1c51452737393f1a07a66d06bad`.
- Whole-tree comparison: `instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/package/WHOLE_TREE_COMPARISON.md`, SHA-256 `3818e3bb8d24fc3ff0a7b7681b2ebe2c4c4cb6c1ba8b06657cb8de16e3f8a282`.
- TASK record: DEL-09-04 `_run_records/TASK_RUN_2026-08-03_0132.md`, SHA-256 `be243a1102b03ba11294dea8402506960b3d11fe3f9bf3352c5fb68f03a8247b`.
- Telemetry: `RUNTIME_EVENTS.jsonl`, SHA-256 `7813cc78c85f65429c4ebb6fea9fc96f712f8da92e0fcd909b9d06c0a17ea94d`; `RUNTIME_SUMMARY.json`, SHA-256 `df14ef2896ca4ec81f6a71f1729d8e311cce5275153e7a857bc8c30a7a3ee991`, status `PASS`.
- Second fresh verifier: `PASS` for truthful `BLOCKED/PARTIAL` fan-in only.

## Return to App HELP_HUMAN

Accept R2 as diagnostic evidence and rollback, not implementation. Route the draft Root investigation request through the parent/Root coordination path. D-APP-88 remains open pending Root's response or a newly evidenced App-side seam; do not retry packaging identity work until the graceful-stop mechanism is dispositioned.
