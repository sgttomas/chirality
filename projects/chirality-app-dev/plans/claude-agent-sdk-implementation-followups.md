# Claude Agent SDK — Implementation Follow-ups

**Status:** Implementation-detail follow-ups separated from the PRD-level revision proposal in `plans/prd-revisions-claude-agent-sdk.md`.
**Date:** 2026-05-19
**Scope:** The "how", not the "what". Each item is concrete and actionable but does not change product requirements; it specifies how to realize them once the PRD revision (or a subset of it) is accepted.

**SCA-APP-001 alignment:** This file now describes first-adapter implementation detail for the Claude Agent SDK / Anthropic path. It does not define Chirality's strategic provider ceiling, authorize a Pi adapter/import/spike, or authorize concrete non-Anthropic provider implementation.

This document is organized as a punch list. Items are independently actionable. Sequencing follows the proposed new R-phases in the PRD revision (R1 → R7), but items can be pulled out of order if scoping changes.

---

## 0. Verification before commit (any phase)

For any phase, the gates remain (from `frontend/`):

```bash
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run instruction-root:integrity
```

Plus the packaging dry run:

```bash
npm run desktop:dist
```

Section 9 IDs (proposed in the PRD revision §12.4) are added incrementally as the corresponding phase lands.

---

## 1. Dependency, package, and SDK boot

- Add `@anthropic-ai/claude-agent-sdk` to `frontend/package.json` `dependencies`. Verify the version against `npm view @anthropic-ai/claude-agent-sdk version` at adoption time and pin to a known-good minor.
- Keep `@anthropic-ai/sdk` as a transitive dependency only if still needed for low-level types; remove from direct deps once the SDK-hosted path replaces `anthropic-agent-sdk-manager.ts`.
- Update `frontend/package-lock.json` via `npm install` (do not hand-edit).
- Confirm the SDK ships its CLI subprocess binary inside its own npm package. If electron-builder's `asar: true` causes runtime resolution failures, add an `asarUnpack` rule for `node_modules/@anthropic-ai/claude-agent-sdk/**` and any binary helpers it ships. Test in a built DMG, not just dev mode.
- Confirm Node.js 18+ requirement (we already require `>=20`).
- Add `@anthropic-ai/claude-agent-sdk` to the `extraResources` / instruction-root integrity verifier's allowlist if its presence affects manifests.

## 2. New harness modules to create

Locations under `frontend/src/lib/harness/`:

- `turn-engine.ts` — exposes the same `IAgentSdkManager` interface (`startTurn(...)` and `interrupt(...)`) so `app/api/harness/turn/route.ts` does not need changes. Internally calls `query()` from the SDK.
- `sdk-options-builder.ts` — pure function `buildSdkOptions(session, opts, contentBlocks, hooks) → SdkQueryOptions`. Composes:
  - `model` from `ResolvedOpts.model`
  - `cwd` from `session.projectRoot`
  - `permissionMode` from Chirality mode mapping (see §5 below)
  - `allowedTools` / `disallowedTools` from Chirality mode + `opts.tools`
  - `mcpServers` registering all Chirality in-process MCP servers (see §6)
  - `agents` from `evaluateSubagentGovernance` + frontmatter scan
  - `hooks` registering Chirality `PreToolUse`/`PostToolUse`/`PreCompact`/`Stop` callbacks
  - `systemPrompt` / `appendSystemPrompt` from persona composer
  - `settingSources: []` in shipped mode; `["project"]` only when an explicit dev env var is set
  - `resume` from `session.sdkSessionId` when present
- `sdk-message-mapper.ts` — pure function `mapSdkMessage(message) → UIEvent | HarnessEvent[]`. Maps SDK message types into both the existing `UIEvent` SSE contract (for backwards compatibility) and the richer `HarnessEvent` JSONL records.
- `session-events.ts` — append-only JSONL writer + replay reader for `.chirality/sessions/<id>/events.jsonl`. Tolerates malformed trailing lines (NFR-013).
- `event-schema.ts` — defines `HarnessEvent` (`schemaVersion: 1`, `eventId`, `sessionId`, `turnId?`, `parentEventId?`, `timestamp`, `type`, `data`) and the set of event types listed in PRD §8.12.
- `run-logger.ts` — shared redaction + structured logging used by provider/tool/audit paths. Must redact every variant of API key (existing key-variant logic from `anthropic-agent-sdk-manager.ts` lines ~60–110 can be reused).
- `chirality-hooks.ts` — Chirality hook callbacks:
  - `preToolUse_pathContainment` — denies `Write`/`Edit` outside projectRoot; denies instruction-root writes; rejects symlink writes.
  - `preToolUse_subagentGovernance` — gates `Agent` tool via `evaluateSubagentGovernance`.
  - `preToolUse_writeBudget` / `postToolUse_writeBudget` — large output spill to `.chirality/sessions/<id>/artifacts/`.
  - `postToolUse_provenance` — appends provenance evidence where policy requires.
  - `preCompact_mirror` — records compaction boundary in audit JSONL.
- `canUseTool.ts` — capability-policy function with explicit hard-deny precedence passed to `query()` (or implemented via `PreToolUse` returning `permissionDecision: "deny"`).
- `mcp/` (new directory) — Chirality MCP server implementations:
  - `mcp/status.ts` — `_STATUS.md` reader and transition tool.
  - `mcp/dependencies.ts` — `Dependencies.csv` reader/writer.
  - `mcp/scope.ts` — workspace scope/scan tool.
  - `mcp/scaffold.ts` — wraps the existing scaffold service.

## 3. Persona / system prompt composer (replaces `StubPersonaManager`)

Current `frontend/src/lib/harness/persona-manager.ts:9-13` returns `Persona=...; mode=...; projectRoot=...` as the system prompt. Replace with a real composer:

- Read instruction-root `agents/AGENT_<persona>.md` via `readAgentInstruction(persona)`.
- Read top-level Chirality governance preface (subset of `AGENTS.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md` headers, `docs/SPEC.md` working-root section) — exactly which subset is itself a product question; start with a conservative summary built into a static `chirality_preface.md` in the instruction root.
- Compose: `[Chirality preface] + [persona instruction] + [working-root summary] + [mode policy]`.
- Return `{ systemPrompt, appendSystemPrompt }` so the SDK's default Claude Code system prompt can be replaced (use `systemPrompt: { type: "preset", preset: "claude_code", append: appendSystemPrompt }` if the SDK supports that; otherwise pass full `systemPrompt`).
- `getBootFingerprint` updates to hash persona content + governance preface + mode + tool names + permission-policy version + subagent-policy version (per FR-029).

## 4. Route changes (minimize)

`frontend/src/app/api/harness/turn/route.ts` should NOT need to change in shape:

- It already calls `runtime.agentSdkManager.startTurn(session, message, opts, contentBlocks)` and iterates the resulting async generator emitting SSE events.
- The runtime factory in `runtime.ts` switches the manager based on `CHIRALITY_HARNESS_PROVIDER`.
- Plan: register a new provider mode `agentSdk` (or repurpose `anthropic` once the cutover is complete) that returns the SDK-backed `TurnEngine` as the `agentSdkManager`.
- Keep `stub` provider mode pointing at `agent-sdk-manager.ts` (existing stub) for tests.

Route-level work that IS needed:

- `route.ts:188` already writes `claudeSessionId` back to the session on `session:init` — adjust the event mapper to emit `claudeSessionId` from `SDKSystemMessage` (init) or from the first `SDKResultMessage.session_id` (whichever the SDK exposes first).
- Ensure `turn.accepted` is appended to the audit JSONL **before** `query()` is awaited (currently the route does not write a per-turn record at all).

## 5. Permission mode mapping (Chirality → first-adapter SDK)

Concrete mapping table to implement in `sdk-options-builder.ts`:

| Chirality mode | SDK `permissionMode` | `allowedTools` | `disallowedTools` | `canUseTool` policy |
|---|---|---|---|---|
| `readOnly` | `default` | `Read`, `Glob`, `LS`, `Grep`, Chirality read MCP tools | `Write`, `Edit`, `Bash`, Chirality write MCP tools, `WebFetch`, `WebSearch` | denies any tool not in allowedTools |
| `workspaceWrite` | `acceptEdits` | read tools + `Write`, `Edit`, Chirality write MCP tools | `Bash`, `WebFetch`, `WebSearch` | enforces projectRoot containment, instruction-root block, symlink reject |
| `dontAsk` | `default` | read tools only | write/shell tools | denies write/shell without prompting; never returns `ask` |
| `ask` | `default` | read tools + write tools | `Bash` unless explicitly enabled | returns `ask` for write/shell, propagates to UI prompt |
| `bypass` (dev-only) | `bypassPermissions` | all | none | **still applies** containment for instruction root and symlink writes |

Explicit hard-deny precedence: `canUseTool` or equivalent hooks can override any allow at reliance boundaries, secrets, protected paths, release/professional claims, destructive actions, and unvalidated provider/network expansion.

## 6. Chirality MCP servers (in-process)

Use `createSdkMcpServer()` from the SDK with `tool()` definitions:

- `mcp__chirality__status_read` — reads `_STATUS.md` for a given deliverable path. Input: deliverable absolute path. Output: parsed status snapshot.
- `mcp__chirality__status_transition` — applies an allowed lifecycle transition. Input: deliverable path, target state, actor, approvalSha (required for human gates). Hook layer enforces preconditions.
- `mcp__chirality__deps_read` — reads `Dependencies.csv` for a deliverable. Returns parsed rows + warnings.
- `mcp__chirality__deps_write` — appends/updates rows; preserves schema version `v3.1`.
- `mcp__chirality__scope_scan` — runs the existing workspace scope scanner; respects depth/count limits.
- `mcp__chirality__scaffold` — invokes the existing scaffold service.
- (Future) `mcp__chirality__domain_*` for domain-engine adapters — out of scope until R7 (proposed) / R11 (current PRD).

All MCP tools must:
- Validate paths via the same containment helper used by hooks.
- Emit structured `HarnessEvent`s through `run-logger.ts` redaction layer.
- Be referenced in `allowedTools` by full prefixed name (e.g., `mcp__chirality__status_read`).

## 7. Subagent governance integration

`evaluateSubagentGovernance` in `frontend/src/lib/harness/subagent-governance.ts` already encodes the policy. Integration:

- Generate the SDK `agents` config from `agents/AGENT_*.md` frontmatter (type=Type2 entries) at boot time.
- For each Type 2 entry, set:
  - `description`: from `description` frontmatter
  - `prompt`: agent file body
  - `tools`: from `tools` frontmatter (default to read-only set if missing)
  - `model`: from `model` frontmatter or runtime default
- Add a `PreToolUse` hook with matcher `^Agent$` that:
  - Reads the requested subagent name from `tool_input`.
  - Calls `evaluateSubagentGovernance(parentPersona, governanceMetadata)`.
  - Returns `{ permissionDecision: "deny", reason: <governance reason> }` on any negative condition.
- Audit JSONL records the governance decision regardless of allow/deny.

## 8. Session linkage and migration

- Extend `SessionRecord` in `frontend/src/lib/harness/types.ts` to add `sdkSessionId?: string`.
- On first turn for a session: SDK returns `session_id` in the first `SDKResultMessage`; persist it to `session.json`.
- On subsequent turns: pass `resume: session.sdkSessionId` to `query()`.
- Future canonical session folder layout (per PRD §10.3):
  - `.chirality/sessions/<id>/session.json` (existing fields + `sdkSessionId`)
  - `.chirality/sessions/<id>/events.jsonl` (Chirality audit mirror)
  - `.chirality/sessions/<id>/turns/<turnId>.json` (optional per-turn summary; defer)
  - `.chirality/sessions/<id>/artifacts/` (tool-result spill)
- Migration: continue reading legacy `.chirality/sessions/<id>.json` records during list/resume (FR-077). New sessions write to the new folder layout.
- SDK transcripts at `~/.claude/projects/<encoded-cwd>/<sdk-session-id>.jsonl` are read-only for Chirality. Decide once whether to import-and-purge or treat as secondary source; proposal in PRD-revision §7 is "secondary source only, do not import".

## 9. SettingSources isolation

- Default `settingSources: []` in shipped Electron builds. Empty array means: no SDK settings discovery at all.
- Allow `CHIRALITY_SDK_SETTING_SOURCES=project` (or similar) for development to enable per-project `.claude/settings.json` overrides.
- Never include `"user"` in `settingSources` (would load `~/.claude/settings.json`).
- Add a unit test that asserts `buildSdkOptions(...)` returns `settingSources: []` when `CHIRALITY_SDK_SETTING_SOURCES` is unset.

## 10. Network policy compatibility

- Renderer-side `webRequest.onBeforeRequest` allowlist remains as today (loopback + `api.anthropic.com`).
- SDK makes its API request from the Node side (Next.js server / Electron main); confirm the request target is `api.anthropic.com` and that the SDK respects `ANTHROPIC_API_KEY` resolution from `process.env`.
- Verify the SDK does not phone home or fetch additional resources (telemetry endpoints, model lists, etc.). If it does, add those endpoints to the allowlist with documented rationale — do NOT silently widen the policy.
- Test: run the full DMG with no network access except `api.anthropic.com` and confirm the SDK works for a basic read-tool turn.

## 11. Electron packaging

- Confirm SDK's CLI subprocess is locatable from inside `app.asar`. Likely requires `asarUnpack` for `node_modules/@anthropic-ai/claude-agent-sdk/**`.
- Confirm `process.env.HOME` resolves correctly in the packaged app (so SDK session storage lands in the user's actual home, not a sandboxed Electron path). If it doesn't, set `HOME` explicitly before `query()` is invoked.
- Confirm signed vs unsigned build: SDK CLI binary must be co-signed with the rest of the app under macOS Gatekeeper (or remain in the adhoc-signed unsigned DMG).
- Add an `instruction-root:integrity` check that verifies the SDK package is present in the bundle.
- Test: launch packaged DMG, start a session, send a turn, confirm SDK transcripts appear at `~/Library/Application Support/Chirality/...` OR `~/.claude/projects/...` (depending on how SDK resolves `cwd` and `HOME`).

## 12. Anthropic API key handling

- Existing key resolution (`api-key-store.ts` UI safeStorage → `ANTHROPIC_API_KEY` → `CHIRALITY_ANTHROPIC_API_KEY`) remains the source of truth.
- Set `process.env.ANTHROPIC_API_KEY` to the resolved value **before** invoking `query()` (the SDK reads it from env).
- Restore the prior value after the turn completes (avoid leaking the key into other parts of the Node process if it wasn't there originally).
- Ensure the SDK does not write the key to its session JSONL (verify in `~/.claude/projects/<...>.jsonl` after a test run).
- Redaction in `run-logger.ts` covers all known key encodings (existing key-variant logic).

## 13. Test surface updates

Existing tests under `frontend/src/__tests__/` should keep passing after R1 (no observable behavior change). Add tests:

- `turn-engine.test.ts` — runs `runTurn()` with the stub SDK manager, asserts `UIEvent` sequence matches the existing contract.
- `session-events.test.ts` — append + replay + malformed-trailing-line tolerance.
- `sdk-message-mapper.test.ts` — each known SDK message type maps to the right `UIEvent` and `HarnessEvent`.
- `sdk-options-builder.test.ts` — Chirality mode → SDK options mapping table coverage.
- `chirality-hooks.test.ts` — path containment, instruction-root protection, symlink rejection, subagent governance gating.
- `canUseTool.test.ts` — explicit hard-deny precedence; deny beats allow at protected boundaries.
- `mcp/*.test.ts` — each Chirality MCP server's tool input/output and error cases.
- `persona-composer.test.ts` — real prompt builder content, fingerprint stability.
- `settingSources.test.ts` — default is `[]`; dev env opens `["project"]`; never `"user"`.

Section 9 validation IDs (added to `harness:validate:premerge` as the phase lands):
- `section9.adapter_turn_engine_event_log`
- `section9.session_event_replay`
- `section9.tool_runtime_read_file` (SDK Read + audit event)
- `section9.permission_overlay_hard_deny_precedence`
- `section9.path_containment_hook`
- `section9.instruction_root_protection_hook`
- `section9.subagent_governance_hook`
- `section9.compaction_boundary_recorded`
- `section9.settingsources_isolation`

## 14. Removal / deprecation list

Once the SDK-hosted path is the default (`CHIRALITY_HARNESS_PROVIDER=anthropic` switches to it):

- `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` (897 lines) — delete or shrink to a debug-only direct path.
- `frontend/src/lib/harness/agent-sdk-manager.ts` (stub) — keep, the test path.
- Remove direct `@anthropic-ai/sdk` dependency from `package.json` if no remaining usage.

## 15. Known unknowns to validate empirically

- Whether the SDK exposes a per-call `allowedTools` override or only a global one. (Survey said global; needs verification before committing the "per-mode allowedTools" design.)
- Whether `canUseTool` is a first-class option or must be implemented via `PreToolUse` hook returning `permissionDecision: "deny"`. (Survey was ambiguous.)
- Whether `permissionMode: "dontAsk"` actually exists or only `default | acceptEdits | plan | bypassPermissions`. (Standard CLI options are the latter; `dontAsk` may be a hook/canUseTool pattern.)
- The exact shape of the `SDKResultMessage.session_id` and timing — does it appear in `init` or only in `result`? Affects when we can persist `sdkSessionId`.
- How `cwd` is set programmatically (option vs. `process.chdir` vs. inherited). Affects how we ensure session storage paths are stable across Electron app launches.
- Whether `PreCompact` is fired on context compaction inside `query()` or only on session-level operations.
- How `interrupt` works against an in-flight `query()`: AbortController on the host side, or an SDK-provided control method.

Each of these should be answered by a 30-minute SDK probe before R1 commits to a concrete design. None blocks the PRD revision; all block the R1 file structure.

## 16. Sequencing recommendation

1. Accept the PRD revision (or some subset of it).
2. Run the §15 SDK probe to nail down ambiguous API surface.
3. Cut a feature branch `runtime/sdk-adoption-r1`.
4. Implement R1 modules in §2 above; keep `anthropic-agent-sdk-manager.ts` in place as the default until the SDK manager passes all existing tests + the new Section 9 IDs.
5. Flip the default in `runtime.ts` after the SDK path passes Section 8 + new Section 9 IDs.
6. Open a CHANGE record per `docs/CHANGE_PUBLICATION_GUIDANCE_CONSTRAINTS.md` for the PRD-level edit and the dependency addition. The R1 implementation lands behind the same CHANGE or a follow-on.
7. Continue with R2..R7 in order, each behind its own CHANGE record.

## 17. What does not require any new work

- All `app/api/working-root/*` endpoints.
- Scaffolding logic (already implemented; will be re-exposed via MCP wrapper).
- File tree, scope scan, deliverable status, dependency contract APIs.
- Attachment resolver — keeps its current role of producing `ContentBlock[]` for the SDK input.
- Working-root validation and selection UX.
- Toolkit panel and chat draft persistence.
- macOS DMG packaging steps (modulo the asar-unpack adjustment in §11).
- Instruction-root integrity verifier (modulo the SDK presence assertion in §11).
- Subagent governance evaluator (existing logic; only invocation point changes).
- Persona alias mapping (FR-026).
- API key safeStorage IPC.
- The entire PRD §7 (User Journeys) UX flow.

These elements survive the pivot unchanged.
