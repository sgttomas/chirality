# Pi Agent Harness Assessment For Chirality

Date: 2026-06-13

Author: Codex fan-out/fan-in assessment pass

Pi source baseline:

- Local path: `/Users/ryan/ai-env/projects/pi`
- Remote: `https://github.com/earendil-works/pi.git`
- Commit: `9e9fc7947871a913946f727854ae0a57fbce1863`
- Subject: `fix(coding-agent): treat uppercase config values as literals`

Chirality source baseline:

- Local path: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev`
- Existing unrelated dirty worktree item observed outside this app-dev project: `../chirality-piping/init/init-prompt.md`

## Executive Verdict

Pi should **not** be forked or embedded wholesale into Chirality.

Pi should be used in three narrower ways:

1. **Reference implementation** for agent-loop lifecycle, session tree, tool hook, extension, and provider-adapter ideas.
2. **Pattern source** for Chirality-native session/event/tool designs, with attribution in assessment/ADR material.
3. **Possible future backend-adapter spike** only as a constrained, exact-version, no-tools, Anthropic-only `pi-ai` or `pi-agent-core` sidecar/probe behind Chirality's `AgentEnginePort`.

Do not adopt `pi-coding-agent` as Chirality's shipped runtime adapter. It is a strong local coding-agent shell, but its filesystem, shell, extension, provider, and project-trust assumptions are too broad for production app-embedded engineering-domain workflows.

## Basis

Chirality's PRD says the product is a governed desktop harness where project truth lives in git-tracked plain files, humans retain authority, and runtime events remain audit rather than truth (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/PRD.md:21`). It also says the runtime should remain SDK-privileged, contract-owned, and Chirality-governed, with the SDK behind product-owned contracts rather than defining the product runtime contract (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/PRD.md:35`).

Current Chirality has a small `AgentEnginePort` boundary (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/agent-engine-port.ts:12`), a versioned `HarnessEvent` schema (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/event-schema.ts:3`), append-only session events (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/session-events.ts:14`), and a Claude Agent SDK adapter path (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/claude-agent-sdk-manager.ts:21`). Those are the right starting boundaries, but still too Claude/SDK-shaped for direct Pi substitution.

Pi's generic agent core has valuable primitives. It documents an evented agent loop with explicit agent, turn, message, tool, and terminal lifecycle events (`/Users/ryan/ai-env/projects/pi/packages/agent/README.md:54`). It also documents semi-durable harness principles: persist a durable append-only session tree, rehydrate tools/models/hooks from the host, and recover from durable boundaries rather than provider streams (`/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:19`).

Pi's coding shell is not a safety boundary. Its security docs state that project trust is not a sandbox (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:5`) and that built-in tools and extensions run with the process user's permissions (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:31`).

## Primitive Fit Matrix

| Pi primitive | Source | Chirality analogue | Recommendation |
| --- | --- | --- | --- |
| Agent/turn/message/tool event lifecycle | `/Users/ryan/ai-env/projects/pi/packages/agent/README.md:54` | `HarnessEvent` and `sdk-message-mapper` | Adopt as pattern; rename into Chirality terms |
| `beforeToolCall` / `afterToolCall` hooks | `/Users/ryan/ai-env/projects/pi/packages/agent/README.md:111` | Permission overlay, provenance hooks | Adopt as runtime-policy pattern |
| Ordered tool-result persistence | `/Users/ryan/ai-env/projects/pi/packages/agent/README.md:102` | Audit replay determinism | Adopt as conformance requirement |
| Append-only JSONL tree with `id`/`parentId` | `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/session-format.md:1` | `.chirality/sessions/<id>/events.jsonl` | Adopt concept after schema design |
| Semi-durable restore model | `/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:9` | Recoverable Chirality sessions | Adopt principle; implement natively |
| TypeBox tool schemas | `/Users/ryan/ai-env/projects/pi/packages/ai/README.md:90` | Future `HarnessToolDescriptor` | Consider adopting library/pattern |
| Exact edit/diff behavior | `/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/edit.ts:287` | Future file mutation tools | Borrow pattern only after write policy exists |
| File mutation queue | Pi coding-agent tools | Same-file write serialization | Borrow pattern, not code yet |
| Extension lifecycle | `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/extensions.md:3` | Chirality MCP/hooks/profile adapters | Rehouse under Chirality governance |
| Pi project trust | `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:5` | Instruction-root/working-root policy | Do not adopt as safety model |
| Pi built-in bash/write/edit defaults | `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:31` | Deny-first tool surface | Avoid direct adoption |

## Backend Adapter Matrix

| Backend option | Fit | Risks | Decision |
| --- | --- | --- | --- |
| Continue Claude Agent SDK | Best aligned with current PRD and dependency state | SDK-shaped leakage remains; route still owns too much lifecycle | Continue R0/R1 path |
| `pi-ai` Anthropic-only adapter | Possible provider abstraction probe | Provider breadth, Node 22, ESM, custom base URLs/headers must be locked down | Later sidecar spike only |
| `pi-agent-core` with injected stream/tools | Possible custom loop fallback | More runtime ownership; durability incomplete; must supply all policy | Later spike after session/event schema hardens |
| `pi-coding-agent` SDK | Rich programmatic coding harness | Tools/extensions/sessions/resources too broad; default coding assumptions | Do not use for shipped Chirality runtime |
| Fork Pi | Legally possible | Large maintenance burden; shifts identity | No |
| Reference only | Immediate benefit, low risk | No runtime acceleration by itself | Yes, current default |

## Governance Gap Register

| Area | Pi posture | Chirality requirement | Required action |
| --- | --- | --- | --- |
| Filesystem | Absolute/home/cwd path ergonomics | Working-root containment and instruction-root block | Chirality path gate before every operation |
| Shell | Local process command execution | Default denied; explicit human/mode gate | Keep denied until sandbox/audit/timeout exist |
| Extensions | Arbitrary TypeScript in process | Release-managed capabilities | Disable project-loaded extensions in product runtime |
| Provider config | Broad providers, custom endpoints, ambient credentials | Anthropic-only current scope | Hard provider/model/baseURL allowlist |
| Sessions | Useful JSONL traces | Audit mirror plus git-tracked truth | Chirality session/event schema remains canonical |
| Recovery | Provider streams not resumable | Explicit interrupted/retry-safe records | Recover only from durable boundaries |
| Domain state | Coding-agent file edits | Typed proposal/adapters/human gates | DomainEngineProfile and operation proposals |
| Attribution | MIT | Preserve notice for copied code | Prefer pattern borrowing; notice for code copies |

## Domain Fit

Pi's strengths are strongest for coding: local source trees, direct edits, shell use, flexible extensions, and fast iteration. Chirality's non-coding engineering applications need a different center:

```text
piping design proposal
-> deterministic stress analysis
-> structured solver feedback
-> agent proposal revision
-> evidence bundle
-> human engineering review
-> accepted project/domain state
```

That flow should be governed by Chirality profiles, protected paths, deterministic adapters, proposal records, snapshots, and human gates. Pi can inform the event/tool/session mechanics around the flow, but Pi should not own the flow.

## Decision Ranking

1. **Borrow patterns with attribution** - recommended now.
2. **Reference only** - already useful and should remain the default until implementation starts.
3. **Pi-backed adapter spike** - worthwhile later, but only narrow, no-tools, Anthropic-only, exact-version, likely sidecar because Pi requires Node `>=22.19.0` while Chirality currently declares Node `>=20` (`/Users/ryan/ai-env/projects/pi/package.json:51` and `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/package.json:44`).
4. **Borrow selected code** - allowed under MIT, but only for small isolated pieces where pattern borrowing is insufficient.
5. **Do not use Pi** - not recommended; Pi is too useful as a reference to ignore.
6. **Fork Pi** - not recommended.

## Recommended Next Technical Step

Do **not** implement a Pi adapter immediately.

First, harden Chirality's runtime contract:

1. Generalize event and session metadata away from Claude-specific names.
2. Expand `HarnessEvent` to cover message, tool, queue, compaction, branch, and interruption phases.
3. Define a Chirality-owned `HarnessToolDescriptor` with permissions, path scope, idempotence, result budget, provenance, and human-gate metadata.
4. Extract turn lifecycle ownership out of the HTTP route and current SDK manager into a real `TurnEngine`.
5. Add engine conformance tests using deterministic fake provider streams.

After that, run a constrained Pi spike:

- Name: `pi-ai-anthropic-sidecar-spike`.
- Runtime: no built-in tools, no extensions, no project resource discovery, no broad provider registry.
- Provider: Anthropic only, fixed endpoint, Chirality-owned API key resolution.
- Output: map Pi stream events to Chirality UI/events and prove interrupt/terminal behavior.
- Success criterion: passes the same engine conformance suite as the Claude Agent SDK adapter.
- Failure criterion: requires widening provider/network/config/tool permissions or importing `pi-coding-agent` defaults.

## Related Slice Memos

- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/plans/pi-assessment/01_core_session_primitives.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/plans/pi-assessment/02_backend_adapter_feasibility.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/plans/pi-assessment/03_security_governance_fit.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/plans/pi-assessment/04_domain_harness_fit.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/plans/pi-assessment/05_license_maintenance.md`
