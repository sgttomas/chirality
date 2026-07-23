# Return — G3 Pi Adapter

- **RunID:** `PI_OMLX_SECOND_ENGINE_2026-07-21`
- **Node:** `G3_PI_ADAPTER`
- **Verdict:** `PASS_PENDING_FAN_IN`
- **Actual model:** `gpt-5.6-sol` (no substitution)
- **Authority:** `D-APP-72`, `SCA-APP-002`, and accepted G1/G2 gates
- **Adapter/provider identifiers:** `pi` / `omlx` (parent-mediated integration standard)

## Result

- Added an `AgentEnginePort` Pi adapter with exact `@earendil-works/pi-coding-agent` `0.80.10` attribution, typed preflight, streamed turns, interrupt/cancel, and exactly one terminal `process:exit`.
- Added an independent Pi event mapper for lifecycle, text, tools, compaction, usage, provider failures, interruption, and canonical Chirality UI/Harness events.
- Added a real in-process Pi session factory using only in-memory credentials, model catalog, settings, and session storage. Pi built-ins, native subagents, extensions, skills, prompts, themes, context files, AGENTS files, ambient settings, model files, credential files, and global Pi sessions are disabled.
- Added per-turn custom-tool resolution for the runtime's cached adapter. The adapter accepts only the exact turn allowlist and requires one bridge-attested tool with `readOnly === true`, exact `permissions: ['read']`, and `evidenceSource: 'chirality-tool-bridge'`.
- Enforced the milestone at the adapter boundary: approved managed Agent 2 child, parent and approval references present, no write targets, exactly one read-only tool, and no file attachments. Invalid direct/supervisor sessions fail closed.
- Added strict `http://127.0.0.1:<port>/v1` validation and provider-neutral normalization of injected oMLX discovery failures.
- Added an idempotent process fetch guard for Pi's bundled OpenAI transport. It forces `redirect: 'manual'` only for literal loopback `/v1` requests and leaves all non-oMLX fetches unchanged.
- Early interruption after `session:init` does not construct a Pi/provider session or transmit a prompt.

## Integration API

Construct `PiAgentEngineAdapter` with:

- `resolveProvider(input)` returning `{ baseUrl, apiKey, model: { id, contextWindow, maxTokens, ... } }` after exact oMLX discovery;
- `resolveCustomTools(input)` returning the per-turn output of `bindChiralityToolsForPi(...)`;
- `buildSystemPrompt(input)` returning the sealed Chirality prompt;
- optional `createSession(input)` only for tests or an approved alternative isolated transport.

The static `customTools` dependency remains a test/compatibility shortcut. Production fan-in should use `resolveCustomTools` because one cached adapter serves multiple session/turn contexts.

## Changed paths

- `frontend/src/lib/harness/pi-agent-engine-adapter.ts`
- `frontend/src/lib/harness/pi-event-mapper.ts`
- `frontend/src/__tests__/lib/pi-agent-engine-adapter.test.ts`
- `frontend/src/__tests__/lib/pi-event-mapper.test.ts`
- this return

No runtime registry, TurnEngine, contract, package, existing tool/MCP, credential/provider, delegation, Electron, or governance file was edited.

## Validation

| Check | Result |
|---|---|
| Pi adapter/mapper focused suite | PASS: 2 files, 15 tests |
| Full renderer + Electron TypeScript check | PASS: `npm run typecheck` |
| Real in-memory Pi construction | PASS: exact supplied session ID, no transcript file, zero built-in tools |
| Ambient sentinel isolation | PASS: `.pi`, `.agents`, AGENTS, settings, and skills ignored |
| Early interrupt engine conformance | PASS: terminal 130, unique/final exit, no provider construction |
| Redirect behavior diagnostic | Pre-guard Pi/OpenAI loopback 307 probe confirmed redirect following; guard unit proof confirms manual redirect for oMLX and unchanged Anthropic fetch init |
| Scoped trailing-whitespace scan | PASS |

## Fan-in requirements and residuals

1. Runtime integration must adapt `resolveOmlxProviderConfig()` plus exact `requireOmlxModel()` discovery into the adapter provider shape and supply governed `contextWindow` / `maxTokens` metadata required by Pi's model contract.
2. Runtime integration must build the bounded `read_file` definition and Pi binding per input so session/project/turn permission and evidence context is never cached across children.
3. The adapter is intentionally not registered in `runtime.ts`, and managed delegation is intentionally not changed in this disjoint tranche.
4. No live oMLX model, full suite, production build, packaging proof, or Claude-parent/Pi-child end-to-end proof was run here; those remain G4/G5 fan-in checks.
5. Durable Pi resume remains disabled (`durableResume: false`); all Pi session state in this milestone is Chirality-owned evidence plus an in-memory Pi transcript.
