# Launch Brief — G3 Pi Adapter

- **Role:** TASK Pi adapter worker
- **Model:** `gpt-5.6-sol` (record substitutions)
- **Authority:** D-APP-72/SCA-APP-002; G1 and G2 gates PASS.
- **Dependency:** exact `@earendil-works/pi-coding-agent` `0.80.10` is installed and locked.

## Write scope

- New `frontend/src/lib/harness/pi-agent-engine-adapter.ts`
- New `frontend/src/lib/harness/pi-event-mapper.ts`
- New Pi-only tests under `frontend/src/__tests__/lib/`
- `RETURN_G3_PI_ADAPTER.md`

Do not edit runtime.ts, TurnEngine, harness-contract, package files, existing tool/MCP files, credential/provider files, delegation, Electron, or governance.

## Required behavior

- Implement `AgentEnginePort` descriptor `pi` / `omlx-openai`, exact Pi package/version attribution, preflight, startTurn, interrupt, and optional cancel.
- Accept provider dependencies by constructor injection so unit tests require no live server.
- Use a custom resource loader or equivalent explicit session construction that cannot discover ambient `.pi`, `~/.pi`, `.agents`, prompts, extensions, skills, settings, credentials, or sessions.
- Disable Pi built-ins/native subagents; accept only explicitly injected Chirality custom tools.
- Use in-memory credential/model runtime; never read/mutate Anthropic credentials.
- Map Pi lifecycle/text/tool/compaction/error/interruption/terminal output to canonical UI/Harness events with one terminal `process:exit`.
- Persist no global Pi state. Any optional transcript path must be supplied beneath the Chirality session directory by the caller.
- Unit-test bootstrap, success, tool call/result, failure, interrupt, terminal uniqueness, resource isolation, and no-builtins behavior using injected fakes.

Return exact files/checks/risks and actual model.
