# D-APP-12 Updated Decision Packet - Default Provider Cutover After STAB-02(d) Package Proof

**Status:** PROPOSAL  
**Date:** 2026-06-16  
**Decision ID:** D-APP-12  
**Supersedes for next ruling:** `execution/_Coordination/_DECISIONS/D-APP-12_PACKET_2026-06-16.md`  
**Prior ruling:** `execution/_Coordination/_DECISIONS/D-APP-12_RULING_2026-06-16.md`

## Prior Ruling

The human approved Option B: hold the default-provider cutover until STAB-02(d) packaged
subprocess proof lands or blocks with evidence.

This packet records the STAB-02(d) package-layout evidence and the remaining blocker. It
does not change the default provider. `agentSdk` remains opt-in.

## Question

May the app make `agentSdk` the default provider now, or should D-APP-12 remain blocked
until packaged read-tool turn evidence and transcript/HOME behavior are proven?

## New Evidence Since The Prior Packet

- Electron packaging now unpacks:
  - `node_modules/@anthropic-ai/claude-agent-sdk/**`;
  - `node_modules/@anthropic-ai/claude-agent-sdk-*/**`.
- `instruction-root:integrity` now fails packaged bundles when the SDK JS package or the
  native platform CLI package is missing from `app.asar.unpacked`.
- `npm run desktop:pack` passed and the integrity summary recorded:
  - SDK package present under `app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk`;
  - native CLI package present under
    `app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/node_modules/@anthropic-ai/claude-agent-sdk-darwin-arm64`;
  - native CLI file `claude` present and executable-sized (`213070752` bytes).
- The directory build launched successfully from
  `frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality`.
- The packaged renderer/API served from bundled `app.asar`; `GET /` returned HTTP 200.
- The packaged harness API created a session and completed boot with
  `CHIRALITY_HARNESS_PROVIDER=agentSdk` without invoking a live turn.
- `npm run desktop:dist` passed.
- The generated DMG mounted read-only at `/Volumes/Chirality 0.1.0-arm64`, and
  `instruction-root:integrity` passed against the mounted app Resources directory.

## Remaining Blocker

A packaged read-tool `agentSdk` turn was not run.

Reason: no live-provider proof was explicitly approved, and the packaged Electron app can
load a stored Anthropic API key from the app profile. Running a packaged `agentSdk` turn
could therefore become live-provider use. The existing scripted SDK proof is intentionally
development/test-only and would bypass native CLI resolution, so it is not valid evidence
for packaged SDK subprocess resolution or transcript/HOME behavior.

Therefore:

- packaged SDK presence is proven;
- directory-build and mounted-DMG bundle integrity are proven;
- packaged read-tool turn behavior is not proven;
- transcript/HOME behavior is not proven;
- default-provider cutover remains risky.

## Options

| Option | Ruling | Effect | Exclusions |
|---|---|---|---|
| A | Approve default-provider cutover now | Future work may make `agentSdk` the default despite the missing packaged read-tool turn and transcript/HOME evidence. | Concrete non-Anthropic providers, provider-network expansion, Pi runtime paths, release-readiness/professional claims. |
| B | Continue hold pending packaged turn proof | `agentSdk` remains opt-in. WORKING_ITEMS must obtain explicit live-provider approval for one bounded packaged read-tool proof or implement a non-live packaged resolver/HOME proof harness before returning again. | Default cutover and governance text declaring SDK default. |
| C | Authorize one bounded live packaged proof only | Human approves a single packaged `agentSdk` read-tool proof using a real/stored Anthropic key, solely to close STAB-02(d); default cutover remains blocked until the proof result is recorded and D-APP-12 is ruled again. | Default cutover, release-readiness/professional claims, non-Anthropic providers. |
| D | Deny default-provider cutover for this stabilization program | `agentSdk` remains opt-in for this stabilization program; STAB-06 may document dated opt-in posture only. | Any default cutover until a future human ruling. |
| E | Custom ruling | Human supplies alternate constraints. | As specified by human ruling. |

## Recommendation

Choose **Option B** unless the human wants to spend live-provider budget now. If live
evidence is acceptable, choose **Option C** first, then return to D-APP-12 after the
packaged turn evidence is recorded.

Do not choose Option A unless the project is willing to accept missing packaged
read-tool, transcript, and HOME evidence as residual risk.

## Validation Already Run

- `npm run test -- src/__tests__/scripts/dmg-packaging-policy.test.ts src/__tests__/scripts/verify-instruction-root-integrity.test.ts`;
- `npm run desktop:pack`;
- packaged app launch from the directory build;
- packaged `GET /`, session create, and session boot;
- `npm run desktop:dist`;
- mounted-DMG `npm run instruction-root:integrity -- --bundle-root '/Volumes/Chirality 0.1.0-arm64/Chirality.app/Contents/Resources' --output-root artifacts/harness/instruction-root-integrity/dmg-mounted-2026-06-16`;
- `npm run harness:validate:agentsdk-dev-turn`;
- `npm run proof:network-policy -- --provider agentSdk --scripted-agent-sdk --runs 1 --idle-seconds 5 --idle-sample-seconds 5 --output-dir artifacts/harness/network-policy-agentSdk-short-2026-06-16`;
- `npm run typecheck`;
- `npm run test`;
- `npm run harness:validate:premerge`;
- `npm run instruction-root:integrity`.

## Explicitly Not Proven

- Packaged read-tool `agentSdk` turn.
- SDK transcript path in packaged execution.
- SDK HOME / `CLAUDE_CONFIG_DIR` behavior in packaged execution.
- Live-provider behavior.
- Default-provider readiness.

