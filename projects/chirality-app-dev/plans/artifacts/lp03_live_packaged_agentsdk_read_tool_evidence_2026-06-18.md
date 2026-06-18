# LP-03 Live Packaged agentSdk Read-Tool Proof Evidence

**Date:** 2026-06-18
**Queue:** `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`
**Procedure:** `plans/artifacts/lp02_live_packaged_agentsdk_read_tool_procedure.md`
**Decision authority:** `execution/_Coordination/_DECISIONS/D-APP-15_RULING_2026-06-18.md`
**Status:** BLOCKED proof outcome; one approved live run consumed.

## Commands Run

All commands were run from `{WORKING_ROOT}/frontend`.

```bash
npm run desktop:pack
```

Result: pass. The packaged app directory was produced under
`frontend/dist/mac-arm64/Chirality.app`, and instruction-root integrity passed.

```bash
npm run harness:validate:agentsdk-packaged-proof -- \
  --bundle-root dist/mac-arm64/Chirality.app/Contents/Resources \
  --output-root artifacts/harness/packaged-agent-sdk/lp03-no-live-baseline-2026-06-18
```

Result: pass. The no-live packaged resolver/HOME baseline resolved the native command
under:

```bash
frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/node_modules/@anthropic-ai/claude-agent-sdk-darwin-arm64/claude
```

```bash
npm run harness:validate:agentsdk-packaged-live-read-tool -- \
  --bundle-root dist/mac-arm64/Chirality.app/Contents/Resources \
  --api-key-file /tmp/chirality-dapp15/anthropic_api_key \
  --output-root artifacts/harness/packaged-agent-sdk-live/lp03-app-dir-2026-06-18 \
  --timeout-ms 180000
```

Result: fail. This command was the single live provider run approved by D-APP-15.

## Live Artifact Summary

Generated ignored local artifact:

```bash
frontend/artifacts/harness/packaged-agent-sdk-live/lp03-app-dir-2026-06-18/summary.json
```

Observed summary fields:

- `status`: `fail`
- `proofMode`: `live-packaged-read-tool`
- SDK package: `@anthropic-ai/claude-agent-sdk` `0.3.150`
- Claude Code version: `2.1.150`
- platform package: `@anthropic-ai/claude-agent-sdk-darwin-arm64`
- expected packaged command exists: `true`
- expected packaged command is a file: `true`
- expected packaged command under `app.asar.unpacked/node_modules`: `true`
- SDK message count: `3`
- `Read` tool observed: `false`
- proof token observed: `false`
- SDK reported error: `true`
- redaction scan passed: `true`
- redaction finding count: `0`

The live proof failed before read-tool execution with this redacted/non-secret failure:

```text
Claude Code returned an error result: There's an issue with the selected model (claude-sonnet-4-20250514). It may not exist or you may not have access to it. Run --model to pick a different model.
```

Consequent failures:

- SDK stream did not report a `Read` tool use.
- SDK stream did not report the proof token read from the target file.
- SDK stream reported an error result.

## Redaction And Key Handling

The script scanned these roots for the API key string and reported zero findings:

- live proof output directory;
- generated proof project root;
- controlled `CLAUDE_CONFIG_DIR`;
- controlled `HOME`.

An additional manual artifact-directory scan over
`frontend/artifacts/harness/packaged-agent-sdk-live/lp03-app-dir-2026-06-18` also reported
zero key-string matches.

The temporary API key file was removed after the proof attempt:

```bash
/tmp/chirality-dapp15/anthropic_api_key
```

No key value is recorded in this evidence artifact.

## Disposition

The app-directory packaged SDK path and native command packaging were proven present, but
the bounded live read-tool proof did not pass. The failure reason is selected-model
availability/access for the supplied key, not a successful read-tool execution.

D-APP-15 approved one live run only; that run has been consumed. Do not rerun with a
different model or key without a new human ruling.

This evidence does not support a D-APP-12 default-provider cutover packet. `agentSdk`
remains opt-in, and default-provider cutover remains held.
