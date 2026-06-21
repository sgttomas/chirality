# Assessment INSP-03: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

Deliverable: DEL-09-06
Package: PKG-09 Validation, Packaging, Security, and Release
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `d0766e0f24b923f7925c711fe05e0cf5d28fd1fb`
Spec source: `Specification.md`

## Scope

This assessment inspected API-key resolution and storage, Anthropic base URL validation, renderer network policy, provider/network guardrails, attachment validation, UI retry/draft behavior, and repeatable command-family evidence. It did not run a live network proof or package the app.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ001 - API key resolution uses UI safeStorage first, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` resolves UI/global key, then canonical env, then project env at lines 258-277; IPC status reports UI/env precedence at `frontend/electron/api-key-ipc.ts` lines 51-68; tests cover precedence at lines 1114-1194. | Precedence is implemented. |
| REQ002 - Key is not written to working root/docs/logs/events/git-tracked execution/tool artifacts. | PARTIAL | Redaction helpers and live packaged proof tests assert no key in stdout/stderr/summary at `frontend/src/__tests__/scripts/run-live-packaged-agent-sdk-read-tool-proof.test.ts` lines 142-204. | No current whole-worktree/log/event/artifact secret scan was run for this assessment. |
| REQ003 - Key stored with Electron `safeStorage` at userData credentials path. | PASS | `frontend/electron/api-key-storage.ts` defines `credentials/api-key.enc` under `app.getPath('userData')` at lines 17-28 and encrypts/decrypts at lines 39-73; tests cover store/retrieve/fail-closed behavior. | Storage path and encryption are implemented. |
| REQ004 - Anthropic base URL accepts only `https://api.anthropic.com` with no credentials and default/443 port. | PASS | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` validates protocol, host, credentials, and port at lines 174-249; base URL tests cover invalid host, non-HTTPS, credentials, and ports at lines 300-526. | Provider URL is constrained. |
| REQ005 - Electron renderer outbound is blocked except loopback and Anthropic API. | PASS | `frontend/electron/main.ts` defines loopback/Anthropic allowlist at lines 27-29, evaluates protocol/host/port at lines 61-103, and registers webRequest blocking at lines 105-128. | Renderer egress policy is implemented. |
| REQ006 - Renderer network policy logs metadata with no secrets. | PARTIAL | `frontend/electron/main.ts` logs blocked network metadata at lines 105-128 and probe metadata at lines 130-219. | The blocked-request log includes the URL; sanitization of query/userinfo is not independently proven. |
| REQ007 - Node/SDK provider calls do not silently broaden network. | PARTIAL | Provider base URL validation constrains Anthropic calls; `frontend/scripts/run-network-policy-proof.mjs` captures remote traffic and fails non-allowlisted connections at lines 370-411 and 670-885. | No current live or packaged proof artifact was present. |
| REQ008 - Attachments revalidate path, extension/type, readability, symlink, regular file, and size. | PASS | `frontend/src/lib/harness/attachment-resolver.ts` validates all listed properties at lines 47-141. | Server-side validation does not trust client metadata. |
| REQ009 - Reject symlinks/directories/special/unsupported/unreadable/>10MB/turn >18MB raw. | PASS | Attachment resolver limits and rejection paths are defined at lines 6-22 and 47-141; resolver tests cover unsupported, symlink, non-file, per-file, and total-limit failures. | Negative cases are covered. |
| REQ010 - Supported extensions are png, jpg, jpeg, gif, webp, pdf, txt, md, csv. | PASS | `frontend/src/lib/harness/attachment-resolver.ts` lists the allowed extensions at lines 6-17. | Matches the spec list. |
| REQ011 - Partial attachment failure is nonfatal when executable content remains. | PASS | `frontend/src/lib/harness/turn-engine.ts` handles partial attachment warnings and continues when executable content remains at lines 231-253; route tests cover partial warnings at lines 789-872 and 898-969. | Partial failure behavior is implemented. |
| REQ012 - Total attachment failure with empty text rejects turn with `ATTACHMENT_FAILURE`. | PASS | `frontend/src/lib/harness/turn-engine.ts` rejects all-failure empty turns at lines 231-253; route tests cover all-failure behavior at lines 789-872. | Error taxonomy is explicit. |
| REQ013 - UI retry preserves draft and attachments on failed send. | PARTIAL | `frontend/src/__tests__/lib/harness-chat-draft.test.ts` covers draft and attachment persistence/sanitization; UI attachment tests cover metadata handling. | End-to-end failed-send retry behavior is not proven by a live UI workflow artifact. |
| REQ014 - Local checks are explicit and repeatable. | PARTIAL | `frontend/package.json` exposes test, network-policy, packaged proof, instruction-root, build, pack, and dist scripts at lines 12-27; release docs describe sequencing. | Not all security checks were rerun in this wave. |
| REQ015 - Release evidence includes command family and artifacts. | PARTIAL | Script families exist, including `proof:network-policy` and packaged SDK proof; no current release evidence package with all artifacts was present. | Needs release-quality run evidence. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| No current all-artifact secret scan | High | Redaction tests exist, but no current scan covered working root, docs, logs, events, execution, and tool artifacts. | Security validation tranche |
| Renderer blocked-URL logging is not proven sanitized | High | The policy log records request URL metadata; query/userinfo redaction is not independently evidenced. | Electron security tranche |
| No current network-proof artifact | Medium | Network proof tooling exists, but no fresh live or packaged proof summary was present. | Security validation tranche |
| Failed-send retry is not end-to-end proven | Medium | Draft/attachment persistence helpers are tested, but the failed-send retry workflow lacks a complete UI/route artifact. | UI/runtime validation tranche |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-09-06 still has 10 active dependency rows with `SatisfactionStatus: TBD`; closure remains open.

## Forward Development Recommendation

1. Add a repeatable secret scan that covers working root, docs, logs, events, execution artifacts, tool-result artifacts, CI logs, and release records. Type: security validation. Size: M. Strategic fit: ON-STRATEGY.
2. Sanitize renderer network policy log URLs or add proof that query/userinfo/key-like values cannot be emitted. Type: Electron security. Size: S. Strategic fit: ON-STRATEGY.
3. Run and archive network-policy proof for local and packaged contexts. Type: security validation. Size: M. Strategic fit: ON-STRATEGY.
4. Add an end-to-end failed-send retry test proving draft and attachment preservation across API failure. Type: UI/runtime test. Size: S. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

This deliverable has strong source controls, but issuance should require current proof artifacts because the remaining risks are evidence freshness and whole-product leakage, not just isolated helper behavior.
