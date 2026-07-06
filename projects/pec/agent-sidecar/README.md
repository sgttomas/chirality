# @pec/agent-sidecar

The built-in pec agent (D-PEC-17; D-PEC-16 O-A, runtime RT-B): a separate
local Node process that logs into pec as an **owner-provisioned agent person**
and drives pec exclusively through the RBAC'd HTTP API via a bounded client.
Zero runtime dependencies (mirrors `@pec/server`, ADR-002 posture).

## What it can and cannot do

- Can: file CSV import proposals, refresh/withdraw its own proposals, triage
  intake items **with grounds** (`parked` / `duplicate` / `rejected` only),
  report status, read the enumerated surfaces.
- Cannot (structurally — no method, URL denylist, payload guard, and pec RBAC):
  accept, apply, reject others' proposals, use `force`, record approval /
  decision / check outcomes, or create approval records via conversion
  (GOV MAJOR-1). Accept/apply stay human acts in Admin.

## Environment

```
PEC_AGENT_ENGINE=stub|sdk      # default stub; sdk needs the package + ANTHROPIC_API_KEY
PEC_BASE_URL=http://127.0.0.1:4810   # loopback only — non-loopback hosts are refused
PEC_AGENT_PORT=4812
PEC_AGENT_EMAIL=...            # owner-provisioned agent person (is_admin=0, coordinator)
PEC_AGENT_PASSWORD=...         # local env only; never committed, never echoed
PEC_AGENT_URL=...              # server-side: where the proxy finds the sidecar (default http://127.0.0.1:4812)
```

Unconfigured credentials are non-fatal: the sidecar starts, `/agent/health`
reports `configured: false`, and messages return `503 AGENT_NOT_CONFIGURED` —
so `npm run dev` works out of the box.

## Actor provisioning

Provision the agent as its **own person** (never a human's account, never an
instance admin): `is_admin=0`, coordinator-class project grant
(`import.propose` + `intake.triage`, never `import.accept`) — the
rehearsal-01 pattern (`_DomainEngines/pec/PEC_2026-07-05_DPEC10-rehearsal-01/`).
The sidecar refuses to operate if the logged-in person is an instance admin or
if a `can/import.accept` probe answers allowed.

## Run

From `projects/pec`: `npm run dev` (server + sidecar + web) or
`npm run dev:agent` (sidecar alone).

## The key-droppable seam (no source change)

The engine is config-selected behind `AgentEnginePort`. The default `stub`
engine is deterministic intent routing over the bounded acts layer — no model,
no key, no egress. The later live-LLM enablement is dependency + key + config
only, **zero source change**:

```
npm i @anthropic-ai/claude-agent-sdk -w agent-sidecar
export ANTHROPIC_API_KEY=...    # never committed
PEC_AGENT_ENGINE=sdk
```

Selecting `sdk` without the package or the key fails at startup with a message
naming exactly those steps. The SDK engine's egress class is
`model-provider`, which arms the D-T0-20 O-B enumeration clamp in the acts
layer (reads outside the enumerated surface are refused, never silently
narrowed).
