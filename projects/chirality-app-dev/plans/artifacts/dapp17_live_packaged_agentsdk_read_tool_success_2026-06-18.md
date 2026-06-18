# D-APP-17 Live Packaged agentSdk Read-Tool Proof Success Evidence

**Date:** 2026-06-18
**Queue:** `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`
**Base procedure:** `plans/artifacts/lp02_live_packaged_agentsdk_read_tool_procedure.md`
**Ruling:** `execution/_Coordination/_DECISIONS/D-APP-17_RULING_2026-06-18.md`
**Status:** PASS

## Scope

D-APP-17 approved bounded app-directory packaged live proof troubleshooting with the
temporary key file retained and model aliases documented by the packaged Claude Code CLI
help. The first approved alias, `sonnet`, passed. The fallback `opus` attempt was not run.

This evidence does not approve default-provider cutover, mounted-DMG parity, provider
expansion, remote MCP/plugins/tool search/domain tools, release readiness, or
professional-boundary changes.

## Commands Run

All commands were run from `{WORKING_ROOT}/frontend`.

The packaged SDK path was present before retry:

```bash
dist/mac-arm64/Chirality.app/Contents/Resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/sdk.mjs
```

No-live baseline:

```bash
npm run harness:validate:agentsdk-packaged-proof -- \
  --bundle-root dist/mac-arm64/Chirality.app/Contents/Resources \
  --output-root artifacts/harness/packaged-agent-sdk/dapp16-no-live-baseline-2026-06-18
```

Result: pass.

Live packaged read-tool proof:

```bash
npm run harness:validate:agentsdk-packaged-live-read-tool -- \
  --bundle-root dist/mac-arm64/Chirality.app/Contents/Resources \
  --api-key-file /tmp/chirality-dapp15/anthropic_api_key \
  --output-root artifacts/harness/packaged-agent-sdk-live/dapp17-sonnet-app-dir-2026-06-18 \
  --model sonnet \
  --timeout-ms 180000
```

Result: pass.

## Live Artifact Summary

Generated ignored local artifact:

```bash
frontend/artifacts/harness/packaged-agent-sdk-live/dapp17-sonnet-app-dir-2026-06-18/summary.json
```

Observed summary fields:

- `status`: `pass`
- `proofMode`: `live-packaged-read-tool`
- `model`: `sonnet`
- SDK package: `@anthropic-ai/claude-agent-sdk` `0.3.150`
- Claude Code version: `2.1.150`
- platform package: `@anthropic-ai/claude-agent-sdk-darwin-arm64`
- expected packaged command exists: `true`
- expected packaged command is a file: `true`
- expected packaged command under `app.asar.unpacked/node_modules`: `true`
- SDK message count: `7`
- `Read` tool observed: `true`
- proof token observed: `true`
- SDK reported error: `false`
- redaction scan passed: `true`
- redaction finding count: `0`
- failures: none

Expected packaged command:

```bash
frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/node_modules/@anthropic-ai/claude-agent-sdk-darwin-arm64/claude
```

## Transcript And Redaction Notes

The proof used controlled temporary paths. The summary redaction scan covered:

- live proof output directory;
- generated proof project root;
- controlled `CLAUDE_CONFIG_DIR`;
- controlled `HOME`.

The controlled `CLAUDE_CONFIG_DIR` contained a generated SDK transcript file:

```bash
/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T/chirality-live-packaged-agent-sdk-proof-mxZaVx/claude-config/730a879e-fe35-4a37-8b4c-ef37b5d3718b.jsonl
```

Transcript content was not copied into the repository. The redaction scan reported zero
API-key findings across the controlled proof roots, including this directory. An
additional artifact-directory scan over
`frontend/artifacts/harness/packaged-agent-sdk-live/dapp17-sonnet-app-dir-2026-06-18`
also reported zero key-string matches.

Per user direction, the temporary key file was retained:

```bash
/tmp/chirality-dapp15/anthropic_api_key
```

No key value is recorded in this evidence artifact.

## Disposition

The app-directory packaged live `agentSdk` read-tool proof is now proven with model alias
`sonnet`: the packaged SDK path loaded, the expected native command remained under
`app.asar.unpacked/node_modules`, the SDK stream reported `Read` tool use, the proof token
was observed, and redaction checks passed.

This satisfies the live packaged read-tool proof prerequisite requested by the D-APP-12
hold ruling, but it does not itself approve default-provider cutover. D-APP-18 has been
prepared as the next human decision packet for default-provider disposition.
