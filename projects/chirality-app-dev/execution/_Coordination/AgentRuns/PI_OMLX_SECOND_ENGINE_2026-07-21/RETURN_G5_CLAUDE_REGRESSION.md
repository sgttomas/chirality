# G5 Claude / Stub Regression Review

**Verdict:** `PASS_AFTER_INDEPENDENT_BACKCHECK`
**Posture:** independent read-only review; production source and tests were not changed
**Actual model:** `gpt-5.6-sol` (no substitution)

## Actionable findings

1. **P1 — Ambiguous legacy stub sessions are silently converted to Anthropic.** `session-manager.ts:133-149` infers `anthropic-direct` for every legacy record that has `claudeSessionId` but no SDK-specific field. The pre-existing stub wrote exactly that shape (`agent-sdk-manager.ts:82-96`), so a keyless user's old stub session becomes pinned to Anthropic on first read and its next turn fails for a missing key or changes engines. The new test at `session-manager.test.ts:107-145` codifies the unsafe inference instead of covering the legacy-stub case. Preserve SDK-specific migration when `sdkSessionId`/SDK attribution exists, but leave ambiguous `claudeSessionId`-only records unselected so the existing environment/key-aware default resolves them; add explicit legacy stub, direct-Anthropic, and SDK migration cases.

2. **P1 — The public stub contract still emits Claude-only metadata.** `agent-sdk-manager.ts:82-96` creates and publishes a `claudeSessionId` for provider `stub`; `session/boot/route.ts:59-64,103-109` then returns it in boot metadata without checking the provider. This contradicts the accepted requirement that `claudeSessionId` be optional and Claude-only, even though persistence was partly corrected. Give stub a provider-neutral engine ID only, omit `claudeSessionId` from stub `session:init`, and include the boot field only when `providerId === 'anthropic'`.

3. **P1 — The required mixed-engine concurrency/no-leakage acceptance proof is absent.** `harness-runtime.test.ts:126-153` only resolves Pi and the default adapter sequentially; `pi-omlx-wire.integration.test.ts:110-224` runs one Pi child fixture whose parent is only an ID string. No test concurrently runs a Claude/stub parent and Pi child through `TurnEngine`, checks separate active-engine interruption, and proves session/model/event attribution cannot cross between cached adapters. Add that wire-level/runtime integration before accepting G4.

4. **P1 — The passing secret-scan receipt does not cover this tranche.** `scan-secret-evidence.mjs:180-203` scans actual values for only the two Anthropic environment variables and omits `CHIRALITY_OMLX_API_KEY`. More importantly, `candidateFiles` at `:242-264` uses tracked files plus generated artifacts but excludes ordinary untracked files; all new Pi/oMLX production modules are currently untracked, so `security/latest/secret-scan-summary.json` did not scan them. Include the oMLX credential and Git untracked/non-ignored source files, rerun, and require the resulting manifest to name the new adapter/provider/tool files.

5. **P2 — The provider-neutral migration is incomplete at the core boundary and attribution record.** `turn-engine.ts:47-56,379-436` retains `IAgentSdkManager`, provider-mode, environment, and Anthropic-key fallback logic, so `AgentEnginePort` is not yet the sole runtime interface and Anthropic policy still lives in `TurnEngine`. `runtime-fingerprint.ts:22-50` accepts only a descriptor and therefore cannot record the selected/actual model required by the plan. Additionally, `turn-engine.ts:451-470` and the boot route replace `adapterSession` wholesale, dropping migrated opaque transcript/store/config metadata. Move compatibility behind a `LegacyAgentEngineAdapter`/registry resolver, pass selection/model into the fingerprint, and merge existing adapter-session metadata when saving.

6. **P2 — The amended SPEC remains stale against the accepted contract.** `docs/SPEC.md:515-535` omits `engineSelection` and `adapterSession`, while `:625-634` still documents an interface with no descriptor or preflight and optional interruption. Reconcile these normative sections with the implemented D-APP-72 port before closeout.

## Evidence and positive checks

- Focused regression suite passed: 6 files / 79 tests covering routes, runtime selection, session storage, TurnEngine, Electron credential storage, and credential IPC.
- Recorded Section 8 and Section 9 summaries are `pass`; packaged Claude resolution and packaged Pi scripted summaries are `pass`.
- Electron `43.1.1`, embedded Node `24.18.0`, builder `26.15.3`, Node floor, secure window preferences, startup credential loading, loopback packaged Next lifecycle, and controlled shutdown have positive G1/package evidence.
- Existing HTTP route names, SSE event names, key-aware Claude-or-stub default, explicit provider environment mappings, and no automatic engine fallback remain intact in the production registry path.

G5 cannot return PASS until the four P1 findings are repaired and covered by tests. The P2 items are contract-closeout defects and should be repaired in the same fan-in rather than carried as undocumented divergence.

---

## Independent remediation backcheck — 2026-07-21

**Backcheck verdict:** `BLOCKED_ON_ONE_REMAINING_ACCEPTANCE_PROOF`

Five of the six original findings are closed in source and tests:

- **Legacy migration — CLOSED.** `session-manager.ts:139-239` now infers Claude only from SDK-specific, explicit adapter-package, or runtime-fingerprint evidence. A `claudeSessionId` by itself remains readable but unselected. `session-manager.test.ts:99-235` separately proves ambiguous legacy stub, explicitly attributed direct-Anthropic, legacy stub-boot, and SDK-specific migration behavior.
- **Stub neutrality — CLOSED.** `agent-sdk-manager.ts:82-96` now emits a `stub_*` provider-neutral engine ID with no `claudeSessionId`. `session/boot/route.ts:52-66,107-119` gates the Claude field on `providerId === 'anthropic'`. The direct adapter test at `agent-sdk-manager.test.ts:25-48` and route assertions at `routes.test.ts:283-355` pass.
- **Secret scan — CLOSED.** `scan-secret-evidence.mjs:180-205` includes `CHIRALITY_OMLX_API_KEY`; `:223-287` includes non-ignored untracked files. The fresh summary (`2026-07-22T05:55:11.682Z`) reports `pass`, 2,621 tracked plus 73 untracked files, the oMLX environment input, zero blocked findings, and explicitly names the new Pi adapter, mapper, oMLX provider, neutral bridge, and packaged-proof script in `scannedFilePaths`.
- **Provider-neutral TurnEngine/fingerprint/session metadata — CLOSED.** `turn-engine.ts:42-49,155-165,352-361` now accepts only a required `resolveEngine`/`AgentEnginePort` path and contains no provider-mode, credential, or package fallback. `:261-300` persists accepted input and a typed `turn.failed` before/recovering from preflight failure; `turn-engine.test.ts:297-360` covers every provider-neutral failure class and a later successful turn. `:372-396` preserves opaque adapter-session fields. `runtime-fingerprint.ts:23-58` records actual model with adapter/provider/package, and the boot route preserves adapter metadata while saving it. Structural provider-neutral error normalization is exhaustive at `harness-contract/src/errors.ts:17-39`.
- **SPEC reconciliation — CLOSED.** `docs/SPEC.md:515-540` now documents `engineSelection`, opaque `adapterSession`, managed-child attribution, and Claude-only compatibility fields; `:630-659` matches the descriptor/preflight/start/interrupt port.

### Remaining P1 acceptance gap

The new isolation test is materially useful but does not prove the exact accepted **Claude-parent/Pi-child** path. `pi-omlx-wire.integration.test.ts:163-206,544-665` registers the parent as adapter `stub`, provider `stub`, and manually constructs both sessions. It proves cached-adapter separation and targeted child interruption, but neither a Claude/Anthropic adapter nor managed delegation launches that child. The packaged production-route proof likewise seeds a Pi session whose `parentSessionId` is only the literal `sess_packaged_claude_parent` (`run-packaged-pi-runtime-proof.mjs:302-326`); it does not execute a supervisor turn or delegation launch.

Close this by running the same concurrent registry/TurnEngine proof with `ClaudeAgentSdkManager` driven by a scripted SDK stream, or an equivalent scripted port attributed `claude-agent-sdk` / `anthropic`, and retain the parent/Pi model, session, interrupt, and terminal no-cross-talk assertions. If the first-milestone claim is meant to include the full launch chain, add one managed-delegation integration that produces the persisted Pi child rather than manually seeding it.

### Independent validation

- `npm run typecheck`: PASS.
- Focused Claude/stub/session/route/error/redaction backcheck: 7 files, 79 tests, PASS.
- Real loopback Pi wire plus expanded reusable conformance backcheck: 2 files, 21 tests, PASS. This covers discovery/auth/model/protocol failures, malformed SSE/tool calls, context exhaustion, hung timeout/interruption, disconnect/restart recovery, tool evidence, redaction, and cached stub/Pi isolation.
- Fresh Section 8 (`2026-07-22T05:54:28.050Z`) and Section 9 (`2026-07-22T05:54:35.178Z`) summaries: PASS.
- Recorded full suite: 106 files passed, 1 skipped; 853 tests passed, 4 skipped. Recorded premerge, typecheck, build, `desktop:pack`, contract dependency, instruction-root, secret-scan, network-policy, and Pi supply-chain gates: PASS.
- Packaged production-route summary: PASS. It loads the packaged turn route and Pi `0.80.10`, performs exact model discovery and two authenticated completions, invokes only governed `read_file`, persists canonical permission/tool/terminal evidence, records model/package attribution, and proves raw fixture content and credential are absent from session evidence.
- `git diff --check`: PASS.

Remaining non-blocking residuals are unchanged: the live oMLX proof awaits an owner-selected tool-capable model and configured credential; the packaged optional-provider closure remains large; remote advisory refresh was not authorized; and instruction-root source completeness remains advisory while the tranche is uncommitted. No release authority is implied.

---

## Final acceptance-proof backcheck — 2026-07-21

**Final verdict:** `PASS`

The single remaining P1 acceptance gap is closed.

- `pi-omlx-wire.integration.test.ts` now runs an equivalent scripted Claude Agent SDK port attributed to adapter `claude-agent-sdk`, provider `anthropic`, package `@anthropic-ai/claude-agent-sdk`, a Claude-only session ID, and the exact parent model concurrently with the real Pi/oMLX adapter through one `TurnEngine`.
- The test retains cached-adapter identity assertions and proves targeted Pi-child interruption does not interrupt or complete the Claude parent. It separately verifies each engine's session initialization, provider/model attribution, chat/terminal outcome, and absence of cross-talk.
- `managed-delegation.test.ts` supplies the complementary governed launch-chain proof: an approved and sealed Agent 1 request launches only the bounded Agent 2 Pi/oMLX shape with one `read_file` tool and an exact model, then persists the selection, brief, approval-backed status, and attribution.

### Final independent validation

- `npm run typecheck`: PASS.
- Managed delegation: 1 file, 16 tests, PASS.
- Real loopback Pi/oMLX wire and concurrent Claude-parent/Pi-child isolation: 1 file, 11 tests, PASS.
- The malformed-provider diagnostic remained redacted as `[REDACTED_PROVIDER_PAYLOAD]`.
- Production source and tests were not changed by G5; only this receipt was updated.

All six original findings are closed. No blocking Claude/stub regression or mixed-engine isolation defect remains in the reviewed scope. The previously recorded live-model, package-size, remote-advisory, instruction-root, and release-authority residuals remain non-blocking.
