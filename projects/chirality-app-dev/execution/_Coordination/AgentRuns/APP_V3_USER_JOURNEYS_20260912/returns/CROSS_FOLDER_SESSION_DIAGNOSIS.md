# Cross-folder session diagnosis

Status: source diagnosis complete; repair and runtime/browser validation pending. TASK / Type 2 read-only descendant, delegated-harness-native, no delegation. Actual dispatch: gpt-6-astra, medium reasoning, explicitly selected by the parent with no history fork (parent tool-confirmed attribution). Source reads and Git read-only comparison only; no live state, logs, authentication, tokens, browser, API, supplier/model calls, tests, builds, or product writes. Only this return was written.

## Finding

The App's process-global harness-port registry is a single replaceable project binding. Selecting J03 replaces the port previously used by J02. The next J02 session-only request is sent with J03's project ID and scoped client. This directly explains the reported `Unknown session` without session deletion. Both origins reach the same global server registry; origin distinction is not needed to cause this defect. The same failure can affect old/background sessions inside one renderer.

Source references below are relative to `projects/chirality-app-dev/frontend/` unless indicated:

1. `src/lib/runtime-client/daemon-harness-port.ts:366-396` stores one `daemonPort` and `daemonBinding` on `globalThis`, under a Symbol shared across Next route module loads. `getDaemonHarnessPort()` has no request, root, or session selector.
2. `src/lib/runtime-client/runtime-daemon-harness-port.ts:728-753`: `initializeProject` verifies the selected root, then calls `verifyAndBind(..., true, ...)`. At lines 947-953 the verified port is installed with replacement allowed and `this.binding` becomes the selected project. Registry lines 450-452 overwrite the old port/binding rather than retaining project or session routing.
3. `src/app/api/harness/turn/route.ts:16-19` gets the global current port. `RuntimeDaemonHarnessPort.turn`, lines 313-324, supplies `this.projectId` plus the incoming `request.sessionId` to `client.turnSession`. A J02 session ID therefore travels through the J03 client after replacement.
4. Runtime `projects/chirality-runtime/packages/core/src/turn-coordinator.ts:112` loads the session by the supplied project/session pair. `packages/core/src/session-store.ts:120-145` looks only in that authorized project's central/legacy session locations and emits `SESSION_NOT_FOUND: Unknown session` when absent. This is correct project isolation; do not weaken it to repair App routing.
5. Other session routes use the same global accessor: replay, events, request answers, interrupt, methods/context, native plan and candidate steering are also vulnerable. Existing active stream objects retain their captured old client, explaining how an older running turn can continue while later requests fail.
6. Hosted bootstrap also retains one `binding`; `resolveAndBind` (lines 839-846) rejects another root once bound. Retaining old session routes alone would still leave old-folder status and root-bearing create/list operations conflicted after another folder selection.

## Frozen baseline comparison

Read-only `git diff 26657ff90 --` for both runtime-client port files shows only the current campaign's steering addition (import/interface/unbound method and a seven-line adapter method). The single global binding, replacement and project-bound turn routing are unchanged from frozen baseline 26657ff90. Thus this is a pre-existing baseline defect, not evidence that the current native interaction changes caused it. Active HEAD inspected: `6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f`; concurrent working changes are not claimed frozen.

## Smallest coherent repair

Keep project-scoped `RuntimeDaemonHarnessPort` objects and all their authorization/root checks. Replace the single effective route target with a small routing facade/registry that retains verified bindings by canonical root/project and session ownership learned from trusted create/list/replay responses. Route root-bearing requests by their verified root, and every session-bearing request by its owning project; capture that port before awaiting. Changing the selected folder may update a default selection for genuinely unscoped catalog operations, but must not erase other bindings or mutate existing session ownership.

For a session absent from the local ownership cache (reload, historical session, native child), require an authoritative scoped ownership lookup rather than silently forwarding to the selected project or creating a new session. Runtime already exposes `RuntimeClient.resolveSessionOwner` (`projects/chirality-runtime/packages/client/src/client.ts:401-419`); use only through an actually authorized client, or probe retained verified project ports, and cache only successful verified ownership. Do not grant a project client access to other projects, fabricate tokens, or bypass manifest drift/containment. If owner resolution needs a selector passed through HTTP, explicit project/root request context is an alternative, but must be checked against the session's actual owner and cover every session endpoint.

Hosted bootstrap's verified-binding cache must likewise preserve old roots for root-specific status/bind calls. Generation ordering can continue governing the active selection without deleting already verified usable roots. Avoid repairing just `turn`: Stop and answering a pending old-folder request need the same owner routing.

## Regression coverage required

- Use actual registry + RuntimeDaemonHarnessPort + HTTP route functions with fake scoped RuntimeClients (not a fake single all-project harness port). Initialize A, create/complete A1, initialize B and start B1, then submit A1 again. Assert the second A turn is sent only to client A with project A, while B remains running and no interrupt/delete is invoked.
- Repeat old-session get/replay/events, state/stream, request answer, interrupt and steering after B binding; assert each exact owning project/client. Include a native child/history session not initially cached.
- After selecting B, create/list/status for root A must use A, not conflict with or silently select B. Test overlapping A/B requests resolving in reverse order without owner corruption.
- Preserve failures for unknown sessions, wrong session-owner selectors, unverified roots, cross-root paths, manifest drift and scoped-client authorization rejection. A stale or failed rebind must not corrupt established routes.
- Run existing initialization-race tests and focused HTTP/client tests, then parent repeats ordinary J02/J03 browser journey. No execution claims in this return.

Existing tests explain the gap: `src/__tests__/lib/runtime-daemon-harness-port.test.ts:698-805` cover latest-selection races and explicitly expect old-root `getStatus` conflict. `src/__tests__/api/harness/hosted-bootstrap.test.ts:186` verifies global binding survives route module reload, but only for one project. Neither exercises an old session after second-project replacement. Some old-root-conflict expectations need deliberate revision for multi-folder semantics; preserve validation failures for genuinely mismatched registrations.

## Coordination and handoff

Implementation is not authorized to this child. Parent was notified before proposal that both runtime-client files overlap the native steering author's current changes. Assign one owner or serialize integration. No Runtime core/session-store repair appears necessary from this finding. Source diagnosis supports the causal path, not a new live reproduction or proof of persisted J02 data. Parent's supplied browser observation is the runtime evidence; accepted upstream source basis is frozen 26657ff90. This return is derivative diagnosis, not authority or release acceptance. Closure: diagnosis complete, product defect open; rerun requirements and checks above remain with parent.

Instruction/brief basis SHA-256:

- Root `AGENTS.md`: `59d8454064101253c829799ad8a6fc068cec97c6cce017fa133cb5bedc7203ed`
- App `AGENTS.md`: `00663c45ca2deb9a21df273d3e8412f609c435f0a8f7746822a51c7f45006f9a`
- `agents/AGENT_TASK.md`: `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- Launch brief: `4e018d73d57866462d20a94cafaf6e35053874ba69b1023ff3db423eb546db6f`
