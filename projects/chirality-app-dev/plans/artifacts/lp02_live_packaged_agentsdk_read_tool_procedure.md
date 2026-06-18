# LP-02 Live Packaged agentSdk Read-Tool Proof Procedure

**Date:** 2026-06-18
**Queue:** `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`
**Decision authority:** `execution/_Coordination/_DECISIONS/D-APP-15_RULING_2026-06-18.md`
**Status:** LP-02 proof procedure, ready for one LP-03 live proof run after LP-02 validation/commit.

## Scope

D-APP-15 Option A approves one bounded live packaged `agentSdk` read-tool proof run.
This procedure does not approve default-provider cutover, provider expansion, remote MCP,
plugins, broad tool search, domain tools, release readiness, or professional-boundary
changes.

The live proof must exercise the packaged app-directory SDK path first. Mounted-DMG
execution is a parity fallback only if app-directory evidence creates a specific need.

## Exact Package Path

Primary package path:

```bash
frontend/dist/mac-arm64/Chirality.app/Contents/Resources
```

Packaged SDK module expected by the live proof:

```bash
frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/sdk.mjs
```

Expected packaged native command family:

```bash
frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/node_modules/@anthropic-ai/claude-agent-sdk-*/claude
```

The proof script records the resolved platform package and verifies the expected command
is under `app.asar.unpacked/node_modules`.

## Exact Commands

Run from `{WORKING_ROOT}/frontend`.

1. Build the packaged app directory:

```bash
npm run desktop:pack
```

2. Re-run the existing no-live packaged resolver/HOME baseline:

```bash
npm run harness:validate:agentsdk-packaged-proof -- \
  --bundle-root dist/mac-arm64/Chirality.app/Contents/Resources \
  --output-root artifacts/harness/packaged-agent-sdk/lp03-no-live-baseline-2026-06-18
```

3. Run the single approved live read-tool proof:

```bash
npm run harness:validate:agentsdk-packaged-live-read-tool -- \
  --bundle-root dist/mac-arm64/Chirality.app/Contents/Resources \
  --api-key-file /tmp/chirality-dapp15/anthropic_api_key \
  --output-root artifacts/harness/packaged-agent-sdk-live/lp03-app-dir-2026-06-18 \
  --timeout-ms 180000
```

This command is the LP-03 live provider proof. Do not run it more than once under
D-APP-15 without a later human ruling.

## API-Key Supply Method

The approved LP-03 key source is:

```bash
/tmp/chirality-dapp15/anthropic_api_key
```

The script reads the key file directly and supplies it only as `ANTHROPIC_API_KEY` in the
SDK options `env` object. It must not print, echo, log, paste, or write the key value.

The command intentionally refuses ambient key usage unless `--allow-env-api-key` is passed.
LP-03 uses `--api-key-file`; ambient env-key use is not selected.

## Artifact Directory

Primary live proof artifact directory:

```bash
frontend/artifacts/harness/packaged-agent-sdk-live/lp03-app-dir-2026-06-18
```

Primary summary:

```bash
frontend/artifacts/harness/packaged-agent-sdk-live/lp03-app-dir-2026-06-18/summary.json
```

The live summary stores:

- package/module paths;
- expected packaged native command inspection;
- controlled `CLAUDE_CONFIG_DIR`, `HOME`, and proof project paths;
- prompt hash and proof-token hash, not raw prompt transcript or raw proof token;
- SDK message summaries only;
- read-tool observation and proof-token observation booleans;
- redaction scan roots and results.

## Stop Conditions

Stop and record a blocker if any of these occur:

- `npm run desktop:pack` fails;
- the app-directory packaged SDK module is missing;
- the expected native command is missing or resolves outside `app.asar.unpacked/node_modules`;
- the no-live packaged resolver/HOME baseline fails;
- the live proof command refuses the key source or times out;
- the SDK stream does not report a `Read` tool use;
- the SDK stream does not report the proof token read from the generated target file;
- the SDK reports an error result;
- the redaction scan finds the API key string in the proof output, proof project root,
  controlled `CLAUDE_CONFIG_DIR`, or controlled `HOME`;
- the command would require remote MCP, plugins, broad tool search, domain tools,
  write/shell/web tools, or more than one live provider proof run.

## Redaction Checks

The proof script scans these roots for the exact API key string before returning pass:

- live proof output directory;
- generated proof project root;
- controlled `CLAUDE_CONFIG_DIR`;
- controlled `HOME`.

The script writes no raw SDK transcript content to `summary.json`. If a failure message
contains the key value, the script replaces it with `[REDACTED_API_KEY]` before writing or
printing the message.

After LP-03, the operator must also run a manual targeted check before committing any
evidence:

```bash
rg -n --fixed-strings "$(tr -d '\n' < /tmp/chirality-dapp15/anthropic_api_key)" \
  artifacts/harness/packaged-agent-sdk-live/lp03-app-dir-2026-06-18 \
  || true
```

Do not paste the command output into chat if it ever prints a match. A match is a blocker.
