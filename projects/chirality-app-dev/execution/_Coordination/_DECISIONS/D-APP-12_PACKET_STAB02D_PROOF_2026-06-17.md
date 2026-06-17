# D-APP-12 Updated Decision Packet - Default Provider Cutover After No-Live Packaged SDK Proof

**Status:** PROPOSAL
**Date:** 2026-06-17
**Decision ID:** D-APP-12
**Supersedes for next ruling:** `execution/_Coordination/_DECISIONS/D-APP-12_PACKET_STAB02D_2026-06-16.md`
**Prior ruling:** `execution/_Coordination/_DECISIONS/D-APP-12_RULING_2026-06-16.md`

## Prior Ruling

The human approved Option B: hold the default-provider cutover until STAB-02(d) packaged
subprocess proof lands or blocks with evidence.

This packet records the new no-live packaged resolver/HOME proof harness and refreshed
validation evidence. It does not change the default provider. `agentSdk` remains opt-in.

## Question

May the app make `agentSdk` the default provider now, or should D-APP-12 remain blocked
until a live packaged read-tool turn proves live provider behavior from the packaged app?

## New Evidence Since The Prior Packet

- Added `npm run harness:validate:agentsdk-packaged-proof`.
- The proof imports the packaged SDK module directly from:
  `app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/sdk.mjs`.
- The proof runs a scripted no-live SDK `query()` turn through the packaged SDK module.
- The packaged directory proof resolved the native darwin-arm64 CLI command from:
  `app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/node_modules/@anthropic-ai/claude-agent-sdk-darwin-arm64/claude`.
- The mounted-DMG proof resolved the same native CLI command from the mounted
  `/Volumes/Chirality 0.1.0-arm64/.../app.asar.unpacked` resources path.
- Both proofs verified the SDK subprocess environment received controlled temp
  `CLAUDE_CONFIG_DIR` and `HOME` paths.
- No live provider call was made, and no stored user API key was loaded.

## Current Evidence State

Proven:

- API-key injection for active SDK turns in dev/scripted route validation.
- Route-level opt-in `agentSdk` scripted dev turn through the real SDK `query()` surface.
- Scripted `agentSdk` network proof without broadening egress.
- Packaged SDK JS package and native platform CLI presence under `app.asar.unpacked`.
- Packaged directory and mounted-DMG no-live SDK resolver behavior.
- Controlled `CLAUDE_CONFIG_DIR` and `HOME` propagation in the packaged SDK proof.
- Section 8 premerge validation and Section 9 deterministic runtime validation are green.

Not proven:

- Live packaged `agentSdk` read-tool turn.
- Live provider behavior from the packaged Electron app.
- Actual SDK transcript file creation under live CLI execution.
- Default-provider readiness by human ruling.

## Options

| Option | Ruling | Effect | Exclusions |
|---|---|---|---|
| A | Approve default-provider cutover now | Future work may make `agentSdk` the default based on no-live packaged resolver/HOME evidence plus existing scripted runtime evidence. | Concrete non-Anthropic providers, provider-network expansion, Pi runtime paths, release-readiness/professional claims. |
| B | Accept STAB-02(d) readiness but continue default hold pending one live packaged proof | `agentSdk` remains opt-in. Future work may request one bounded live packaged read-tool proof before returning to D-APP-12. | Default cutover and governance text declaring SDK default. |
| C | Deny default-provider cutover for this stabilization program | `agentSdk` remains opt-in for this stabilization program; STAB-06 may document dated opt-in posture only. | Any default cutover until a future human ruling. |
| D | Custom ruling | Human supplies alternate constraints. | As specified by human ruling. |

## Recommendation

Choose **Option B** unless the project is willing to accept no-live packaged resolver/HOME
evidence as sufficient substitute for a live packaged read-tool proof. This keeps the
runtime stable and opt-in while preserving a narrow future path to collect live packaged
evidence if the human approves that cost and network use.

Do not choose Option A unless the project accepts live packaged provider behavior and
actual transcript creation as residual risk.

## Validation Run

- `npm run test -- src/__tests__/scripts/verify-packaged-agent-sdk-runtime.test.ts src/__tests__/scripts/dmg-packaging-policy.test.ts`;
- `npm run desktop:pack`;
- `npm run harness:validate:agentsdk-packaged-proof`;
- `npm run typecheck`;
- `npm run harness:validate:agentsdk-dev-turn`;
- `npm run harness:validate:section9`;
- `npm run test`;
- `npm run harness:validate:premerge`;
- `npm run desktop:dist`;
- mounted-DMG `npm run instruction-root:integrity -- --bundle-root '/Volumes/Chirality 0.1.0-arm64/Chirality.app/Contents/Resources' --output-root artifacts/harness/instruction-root-integrity/dmg-mounted-2026-06-17`;
- mounted-DMG `npm run harness:validate:agentsdk-packaged-proof -- --bundle-root '/Volumes/Chirality 0.1.0-arm64/Chirality.app/Contents/Resources' --output-root artifacts/harness/packaged-agent-sdk/dmg-mounted-2026-06-17`;
- `npm run proof:network-policy -- --provider agentSdk --scripted-agent-sdk --runs 1 --idle-seconds 5 --idle-sample-seconds 5 --output-dir artifacts/harness/network-policy-agentSdk-short-2026-06-17`.

## Explicitly Not Proven

- Live packaged provider call.
- Live packaged read-tool result from the Electron app.
- Actual live CLI transcript file creation.
- Default-provider readiness.
