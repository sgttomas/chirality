# @pec/agent-sidecar

The built-in pec agent (D-PEC-17; D-PEC-16 O-A, runtime RT-B): a separate
local Node process that logs into pec as an **owner-provisioned agent person**
and drives pec exclusively through the RBAC'd HTTP API via a bounded client.
Zero runtime dependencies (mirrors `@pec/server`, ADR-002 posture).

## What it can and cannot do

- Can: file CSV/TSV/plain-tabular and `.xlsx` import proposals (D-PEC-42 O-A:
  zero-dependency workbook parser in `src/xlsx.ts`; unreadable/unsupported
  workbooks refuse with a stated basis; all sheets ride the proposal payload
  verbatim), refresh/withdraw its own proposals, triage
  intake items **with grounds** (`parked` / `duplicate` / `rejected` only),
  report status, read the enumerated surfaces — and, on the owner-selected
  `broad` access basis (D-T0-21 O-B), read everything the agent person's own
  RBAC shows over the existing GET routes: project overview, the registers
  (deliverables, packages, plan, my-week, holds, approvals, decisions, risks,
  tracker, interfaces, log), record history, revision explanations, and the
  sponsor-brief / package-pack report payloads (D-PEC-20).
- Cannot (structurally — no method, URL denylist, payload guard, and pec RBAC;
  **excluded regardless of access basis**): accept, apply, reject others'
  proposals, use `force`, record approval / decision / check outcomes, or
  create approval records via conversion (GOV MAJOR-1). Accept/apply stay
  human acts in Admin.

## Environment

```
PEC_AGENT_ENGINE=stub|sdk      # default stub; sdk needs the package + ANTHROPIC_API_KEY
PEC_AGENT_ACCESS=enumerated|broad   # default enumerated (D-T0-20 clamp exactly as ruled);
                               # broad = RBAC-visible reads for model-provider engines too —
                               # an owner act per launch (D-T0-21 O-B); disclosed in
                               # /agent/health and the panel badge
PEC_BASE_URL=http://127.0.0.1:4810   # loopback only — non-loopback hosts are refused
PEC_AGENT_PORT=4812
PEC_AGENT_EMAIL=...            # owner-provisioned agent person (is_admin=0, coordinator)
PEC_AGENT_PASSWORD=...         # local env only; never committed, never echoed
PEC_AGENT_URL=...              # server-side: where the proxy finds the sidecar (default http://127.0.0.1:4812)
PEC_AGENT_MAX_ACTS=8           # per-turn act budget (owner knob, D-PEC-21 widening direction)
PEC_AGENT_MODEL=...            # model for the SDK engine (default: the SDK's default model)
PEC_AGENT_SESSION=hermetic|open   # default hermetic (the D-PEC-21 session exactly as ruled);
                               # open = the harness's built-in tools + user/project/local
                               # setting sources load — an owner act per launch for
                               # limit-testing (D-T0-22/D-PEC-22); disclosed in /agent/health
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
narrowed) — unless the owner selects the `broad` access basis for the launch
(D-T0-21 O-B), in which case reads widen to the agent person's own RBAC
visibility and any record the model reads may reach the model provider. The
human-only acts do not move with the switch.

## Turn shape (D-PEC-21)

The SDK engine runs the SDK's own agentic loop: the bounded acts are exposed
as in-process MCP tools (nothing accept/apply-shaped exists to expose), each
handler dispatches through the same guarded acts layer, and the model reads →
sees results → reads again (8-act budget per turn) before answering. The
session is hermetic BY DEFAULT (`tools: []` disables every built-in tool —
the load-bearing restrictor; `settingSources: []` keeps `~/.claude`
settings/skills/MCP servers out; pec-tools-only `allowedTools` +
`canUseTool` deny, belt-and-braces) — no filesystem, shell, or other tool
reaches the model. `PEC_AGENT_SESSION=open` (owner per-launch env act,
D-T0-22/D-PEC-22) lifts exactly those two restrictors — built-in tools and
user/project/local setting sources load, and the model can read machine
content as the owner's OS user, egressing to the model provider — for
limit-testing only, never a default. The pec bounded-acts surface, act
budget, access clamp, and human-act boundary are identical in both
profiles.
Conversation memory rides the REQUEST (`history: [{who, text}]`, ≤ 40 entries
≤ 8 KiB each, sent by the panel): the sidecar stores nothing between
requests. The stub engine keeps its deterministic single-directive routing
and ignores `history` by design. The server proxy's message timeout defaults
to 300 000 ms (`PEC_AGENT_MESSAGE_TIMEOUT_MS` overrides).

## Shared runtime migration

D-T0-23/D-PEC-56 prospectively retire this package’s independent LLM,
credential, session, delegation, interruption, and residency ownership. Its
durable role is the PEC project adapter for deterministic acts, RBAC,
reporting, human-act exclusion, visibility, and data boundaries. During one
cycle the existing endpoint may proxy to the root daemon; it must not run a
second production loop. Proofs use scratch/demo data only.
