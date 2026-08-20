# Assessment INSP-03: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

Deliverable: DEL-09-06
Package: PKG-09 Validation, Packaging, Security, and Release
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `d0766e0f24b923f7925c711fe05e0cf5d28fd1fb`
Spec source: `Specification.md`

Current calibration (2026-08-20): lifecycle is `IN_PROGRESS`. D-APP-97
packaged-security evidence is current at
`Evidence/Packaged_Security_Proof_2026-08-20_Precedence_Closure/summary.json`;
the historical inspection header above remains the original inspection basis.

## Scope

This assessment inspected API-key resolution and storage, Anthropic base URL validation, renderer network policy, provider/network guardrails, attachment validation, UI retry/draft behavior, and repeatable command-family evidence. The 2026-08-20 calibration adds a fresh unsigned packaged-app network, credential, renderer, instruction-root, and secret-scan proof without changing the unrelated retry/dependency boundary.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ001 - API key resolution uses UI safeStorage first, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` resolves UI/global key, then canonical env, then project env at lines 258-277; IPC status reports UI/env precedence at `frontend/electron/api-key-ipc.ts` lines 51-68; tests cover precedence at lines 1114-1194. | Precedence is implemented. |
| REQ002 - Key is not written to working root/docs/logs/events/git-tracked execution/tool artifacts. | PASS | The compact 2026-08-20 evidence records a final post-write scan of 5,868 files with zero blocked findings; the packaged proof scanned its encrypted fixture and all emitted log/JSON surfaces after stream closure with zero retained credential findings. | Only redacted hashes and compact assertions are retained under D-APP-99. |
| REQ003 - Key stored with Electron `safeStorage` at userData credentials path. | PASS | `frontend/electron/api-key-storage.ts` defines `credentials/api-key.enc` under `app.getPath('userData')` at lines 17-28 and encrypts/decrypts at lines 39-73; tests cover store/retrieve/fail-closed behavior. | Storage path and encryption are implemented. |
| REQ004 - Anthropic base URL accepts only `https://api.anthropic.com` with no credentials and default/443 port. | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` validates protocol, host, credentials, and port at lines 174-249; base URL tests cover invalid host, non-HTTPS, credentials, and ports at lines 300-526. | Provider URL is constrained. |
| REQ005 - Electron renderer outbound is blocked except loopback and Anthropic API. | PASS | The 2026-08-20 packaged proof observed the blocked diagnostic and both blocked/loopback probes across five descendant process/TCP snapshots. | Zero non-allowlisted outbound TCP endpoints were observed. |
| REQ006 - Renderer network policy logs metadata with no secrets. | PASS | The packaged proof closed both GUI and daemon streams before scanning every emitted log/JSON surface; credential and generic metadata leak findings were both zero. | Compact evidence retains assertions and hashes, not raw bulk logs. |
| REQ007 - Node/SDK provider calls do not silently broaden network. | PASS | Focused/full provider-policy tests passed; the packaged proof retained provider isolation and zero non-allowlisted descendant outbound TCP. | No provider scope was expanded and no real credential was used. |
| REQ008 - Attachments revalidate path, extension/type, readability, symlink, regular file, and size. | PASS | `frontend/src/lib/harness/attachment-resolver.ts` validates all listed properties at lines 47-141. | Server-side validation does not trust client metadata. |
| REQ009 - Reject symlinks/directories/special/unsupported/unreadable/>10MB/turn >18MB raw. | PASS | Attachment resolver limits and rejection paths are defined at lines 6-22 and 47-141; resolver tests cover unsupported, symlink, non-file, per-file, and total-limit failures. | Negative cases are covered. |
| REQ010 - Supported extensions are png, jpg, jpeg, gif, webp, pdf, txt, md, csv. | PASS | `frontend/src/lib/harness/attachment-resolver.ts` lists the allowed extensions at lines 6-17. | Matches the spec list. |
| REQ011 - Partial attachment failure is nonfatal when executable content remains. | PASS | `frontend/src/lib/harness/turn-engine.ts` handles partial attachment warnings and continues when executable content remains at lines 231-253; route tests cover partial warnings at lines 789-872 and 898-969. | Partial failure behavior is implemented. |
| REQ012 - Total attachment failure with empty text rejects turn with `ATTACHMENT_FAILURE`. | PASS | `frontend/src/lib/harness/turn-engine.ts` rejects all-failure empty turns at lines 231-253; route tests cover all-failure behavior at lines 789-872. | Error taxonomy is explicit. |
| REQ013 - UI retry preserves draft and attachments on failed send. | PARTIAL | `frontend/src/__tests__/lib/harness-chat-draft.test.ts` covers draft and attachment persistence/sanitization; UI attachment tests cover metadata handling. | End-to-end failed-send retry behavior is not proven by a live UI workflow artifact. |
| REQ014 - Local checks are explicit and repeatable. | PASS | The compact evidence records focused tests, full Vitest, typecheck, build, 350 practitioner-harness tests, root self-check, APP-HOLD, `desktop:dist`, dependency boundary, instruction-root integrity, packaged proof, and secret scan. | Host-only commands and the required mise interpreter are identified in the run record. |
| REQ015 - Release evidence includes command family and artifacts. | PASS | `summary.json` identity-binds the DMG, app executable, `app.asar`, CLI, extracted packaged main, assertions, and results to the accepted N1/N2 inputs; `_run_records/TASK_RUN_2026-08-20_1630.md` records the exact host commands. | Bulk app/DMG/log output remains local and hash-referenced under D-APP-99. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| Failed-send retry is not end-to-end proven | Medium | Draft/attachment persistence helpers are tested, but the failed-send retry workflow lacks a complete UI/route artifact. | UI/runtime validation tranche |

## Source-State Caveat

`docs/PRD.md` is `MATCH` under D-APP-38. Earlier hash-mismatch wording is dated inspection history and does not describe the current source state. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-09-06 still has 10 active dependency rows with `SatisfactionStatus: TBD`; closure remains open.

## Forward Development Recommendation

1. Add an end-to-end failed-send retry test proving draft and attachment preservation across API failure. Type: UI/runtime test. Size: S. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

This deliverable has strong source controls, but issuance should require current proof artifacts because the remaining risks are evidence freshness and whole-product leakage, not just isolated helper behavior.
