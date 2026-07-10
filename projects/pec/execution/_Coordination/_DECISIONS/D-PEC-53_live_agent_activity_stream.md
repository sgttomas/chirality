# D-PEC-53 — RULED: live agent activity stream

**Status:** RULED 2026-07-09 — owner-directed execution
**Decision ID:** D-PEC-53

## Owner direction and verified gap

Owner direction of record (Ryan Tufts, in-session, 2026-07-09):

> “I want true live streaming: show the resolved model, turn state, each tool
> starting/completing, refusals, act budget, and final response as they occur.
> Use what the app-dev harness offers.”

The existing PEC panel buffered `/agent/messages` until the engine returned an
entire `AgentEvent[]`. It therefore could not reveal which SDK model actually
resolved, distinguish an active model turn from a stalled request, or show act
execution before the final response. The configured engine/profile disclosed
capability but not live agent evidence.

## Ruled behavior

1. PEC uses the app-dev harness lifecycle vocabulary and SSE wire convention:
   `event: <type>` plus JSON `data:` frames. The selected evidence types are
   `turn.*`, `adapter.initialized`, `model.*`, `message.completed`, and
   `tool.started|completed|failed`.
2. The SDK's `system/init` message is authoritative for the resolved model.
   An environment override may appear before the first turn; an SDK default is
   named only after init reports it. PEC never guesses a provider default.
3. SDK partial text events stream as `model.delta`. The result message remains
   authoritative and reconciles the final response through
   `message.completed`.
4. Every bounded PEC act emits a start and terminal event with the live
   `{used,max,remaining}` act budget. Basis refusals and budget refusals render
   explicitly as failed/refused tool evidence.
5. The sidecar streams to the server over loopback and the server streams to
   the browser without buffering. Human cookies remain stripped at the proxy.
   JSON batch mode remains sidecar-compatible for existing harness tests and
   direct callers.
6. The panel displays current turn state, resolved model, act budget, tool
   activity, refusals, and incrementally arriving prose. It adds no new act,
   authority, data access, or mutation surface.

## Exact fence

- `projects/pec/agent-sidecar/src/engine/{port,sdk}.ts`
- `projects/pec/agent-sidecar/src/http.ts`
- `projects/pec/agent-sidecar/test/{engine-sdk-loop,sidecar-e2e}.test.ts`
- `projects/pec/server/src/{agent-proxy,api,index}.ts`
- `projects/pec/server/test/{agent-proxy.test,harness}.ts`
- `projects/pec/web/src/agent/api.ts`
- `projects/pec/web/src/agent/AgentPanel.tsx`
- `projects/pec/web/src/styles.css`
- this packet, the PEC decision register, standing PEC workplan, and PEC loop
  receipt ledger

No database change and no new dependency. The app-dev contract is transposed
at its dependency-free event/SSE seam; PEC does not take a runtime dependency
on the separate app-dev project.

## Verification and rollback

- Unit tests pin tool start/terminal ordering, tool IDs, budget evidence, SSE
  lifecycle order, proxy streaming, cookie stripping, and non-2xx relay.
- PEC typecheck/tests/build/drill.
- A real SDK/open/broad browser turn verifies init-reported model, live state,
  tool activity/refusal, act budget, partial prose, final completion, and no
  console errors.
- Self-check, coord-check, and `git diff --check`.
- Rollback by reverting this isolated source tranche; no data rollback exists.

## Human ruling

**RULED:** the quoted direct owner instruction authorizes this live activity
stream inside the fence above.
