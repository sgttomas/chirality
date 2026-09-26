# Maintainability as the governing criterion — analysis

Standing: **interpretation and proposal (agent).** Written in response to
D-16 ("code maintainability is top of my concerns … The best ability is
maintainability"). It proposes principles and an architectural seam for the
v4 basis; nothing here is accepted until the owner says so. Facts about
external projects come from their published documentation and repository
metadata, read on 2026-09-25/26, and from T7 and T8; none has been tested
locally.

## 1. What maintainability has to mean here

The owner maintains Chirality through agents, as one accountable person
(AT §1 items 2 and 4). So maintainability is not a property of code alone. It
is **the ongoing cost and risk, for agents directed by one person, of keeping
the product correct and current while its suppliers, host applications and
the owner's own understanding keep changing.** That cost has six parts:

| Part | The question it asks |
|---|---|
| Owned code | How much must Chirality itself write, read, test and repair? |
| Imported change | How often do suppliers change something Chirality must follow, and how much work does each change cause? |
| Coupling | Where Chirality touches a supplier, is the seam a published, versioned, multi-vendor contract — or a product's internal API or a private modification? |
| Replaceability | If a supplier fades, changes terms or falls behind, what does it cost to swap it? |
| Comprehensibility | Can a fresh agent (or the owner) understand a part from the repository alone — conventional stack, standard formats, small modules? |
| Process weight | How much record-keeping, review and evidence work does every change carry? |

"Ability" (what a harness can do today) is a snapshot. Maintainability is
the rate at which that ability stays available at acceptable cost. That is
the sense in which "the best ability is maintainability."

## 2. Where Chirality's maintenance cost actually came from

The record is unusually clear. Across four generations the cost came from
the same four sources — **none of them a lack of capability**.

| Source | Evidence |
|---|---|
| **Owning what a supplier already does** | v1 ran a custom Anthropic loop, then a CLI subprocess, then cut over wholesale to the Claude Agent SDK "with no dual runtime path" to avoid "regression drift and duplicated maintenance" (`ORIG/.archive/frontend/docs/harness/harness-decisions.md` D-017; T4). v2's daemon re-derived state that Codex already persists (D-GOV-43 finding 5). |
| **Privately modifying a supplier** | The v3 daemon ran a patched Codex App Server "with private protocol extensions" that had to be re-patched on every upstream release and fell five releases behind (D-GOV-43 finding 3; T3, T5). |
| **Generality before need** | A provider-neutral engine vocabulary "retained from the Claude SDK and Pi eras" left Codex items with nothing to render them (D-GOV-43 finding 4); about 6,000 lines of multi-engine harness code remain reachable only from tests, and two engine packages compile but are wired to nothing (T3 R3; T5 §1.5). A2 kept about 2,600 lines of transport for future embedders that do not exist yet (T3 R1). |
| **Process weight** | About 1,022 governance artifacts by 2026-08-01, 30.1 % of changed lines in the one measured window; an early estimate of ~75 % of agent tokens spent on context, documentation and audits; 54 App deliverables never issued; 1,044 of 3,217 deliverable claims found stale (T3 §4–5; T4 §4). |

And the one change that most improved things was the opposite of all four:
D-GOV-43 deleted the daemon, the patches, the filters and the configuration
veto, hosted the supplier **stock** through its **published protocol**, and
the release followed within days (T3 §5; `APP_V3_CODEX_HOST_REPLATFORM_20260912/RUN_LOG.md`).

## 3. Proposed maintainability principles

| # | Principle | Lesson it answers |
|---|---|---|
| M-1 | **Own only what is distinctively Chirality's**: the workflow layer, the human–agent interface, the host-integration contracts, and the records of human acts. Everything a capable harness already does belongs to the harness. | Owning supplier functions |
| M-2 | **Meet every supplier at a published, versioned contract** — preferably one several vendors implement. Never at a product's internal API; never through a modified build. | Private modification; T3 Code's alpha internal API |
| M-3 | **Keep knowledge in open, harness-neutral formats**: `AGENTS.md`, `SKILL.md`, `WORKFLOW.md` (with its declared checkpoints, D-03), MCP tool schemas. Methods then survive any harness change. | Engine-specific vocabularies |
| M-4 | **Do not fork fast-moving upstreams.** Wrap them through their protocols, or contribute. | Re-patching every release |
| M-5 | **Generality only through standards.** Build for the harness in hand; let a standard protocol, not Chirality code, supply the ability to change harness later. | Speculative multi-engine layers |
| M-6 | **Few stacks, mainstream tools.** Every additional language, runtime or framework is a maintenance surface for agents; prefer what agents already read and write reliably, and avoid release-candidate frameworks. | Electron + Next + Node service + daemon for one consumer |
| M-7 | **Seams tested without live models.** Record real protocol exchanges once; test Chirality's side against them deterministically; keep live-model checks few and deliberate. | CI that could not exercise the real path |
| M-8 | **Records proportionate to decisions.** Keep what a later reader needs to reconstruct a human act or a reliance claim; nothing that no one reads. | Process weight; emission without consumption (L-06) |

## 4. Where the seams should be

Applying M-1 to M-5 to what Chirality must do puts two seams around the
harness, and both already have multi-vendor standards:

```text
 Professional
     │  (the application's own interface + the Chirality panel)
     ▼
 ┌──────────────────────────────┐
 │ Chirality client             │  owns: conversation and plan view, workflow
 │ (in each host, and the       │  selection and declared checkpoints, the
 │  standalone Workflow App)    │  four roles as instructions, records of
 └──────────────┬───────────────┘  human acts
                │  Agent Client Protocol (ACP)   ◄── seam 1
                ▼
 ┌──────────────────────────────┐
 │ Any ACP agent (the harness)  │  Codex (codex-acp), Claude Code
 │                              │  (claude-agent-acp), OpenCode, goose,
 │                              │  Gemini CLI, Copilot, Cursor, …
 └──────────────┬───────────────┘
                │  Model Context Protocol (MCP)  ◄── seam 2
                ▼
 ┌──────────────────────────────┐
 │ Host tools, per application  │  SWBPIPE: inspect, preview, submit
 │ (and connectors)             │  proposal, status; Domains: search;
 └──────────────────────────────┘  PEC: read-only coordination state
```

**Seam 1 — Chirality to the agent: ACP.** Verified from the protocol's
documentation and repositories (2026-09-26):

- A client starts a session with a working directory **and a list of MCP
  servers the agent should connect to**; the specification says clients
  "MAY use this ability to provide tools directly to the underlying language
  model by including their own MCP server." Every ACP agent must support MCP
  servers over stdio; HTTP is optional.
- The protocol carries what Chirality's interface needs: prompts and
  streamed updates (messages, tool calls, **plans**, mode changes),
  **permission requests** answered by the client, cancellation, optional
  session loading (resume), modes, authentication, and optional client-side
  file and terminal access.
- 37 agents are listed as implementing it natively (among them Gemini CLI, GitHub
  Copilot, goose, OpenCode, OpenHands, Cursor, Cline, JetBrains Junie, Mistral
  Vibe, Qwen Code); Claude Code, Codex and Pi through adapters.
- The adapters are maintained in the protocol's own organisation:
  `claude-agent-acp` (Apache-2.0) and `codex-acp` (Apache-2.0, copyright
  JetBrains). `codex-acp` offers **ChatGPT login, API key, or a custom
  OpenAI-compatible gateway**, a configurable model provider, plans,
  permission requests, skills, and client-provided MCP servers over stdio
  and HTTP. `claude-agent-acp` offers permission requests, nested subagent
  transcripts and client MCP servers.
- Rust and TypeScript SDKs exist (Apache-2.0), which fits a Tauri host
  (Rust) and a web interface (TypeScript) alike. The protocol is at version 1;
  it originated at Zed, and JetBrains became co-lead maintainer in February
  2026 (T7, from a third-party report).

**Seam 2 — the agent to the host: MCP.** The host's typed operations become
an MCP server. SWBPIPE's owner-accepted "CLI first over the live controller"
seam (inspect, preview, submit, status; no agent Apply; basis binding) maps
onto this directly: a small stdio MCP server can be a thin shim over the same
private bridge. Connectors fit the same seam: Domains as a search tool, PEC
as a read-only tool (PEC's own agent access class is designed for tool
calls, D-PEC-90). The owner's condition on SWBPIPE applies: any MCP adapter
must meet the current stateless protocol, which some bundled clients have
failed.

**What the owner's requirements become under this seam:**

| Requirement | How it is met | Chirality code needed |
|---|---|---|
| Not locked to one provider (D-05) | Any ACP agent; the user chooses per conversation | None beyond the ACP client |
| OAuth, API key and local, possibly at once (D-06) | Codex via `codex-acp` (ChatGPT, API key, custom gateway/provider); Claude Code via `claude-agent-acp` (the user's own sign-in or key); local through an agent with native local-model support (OpenCode, goose) or Codex's custom provider or Claude Code's base URL | Configuration only |
| Local model server required (D-05) | As above; the local server is the user's choice (oMLX, LM Studio, Ollama) | Configuration only |
| Host tools in SWBPIPE (D-02) | Host MCP server passed at session start | The host's MCP server (owned by the host project) |
| Declared checkpoints enforced (D-03) | Permission requests arrive at the client, which knows the workflow's declared checkpoints; the host enforces its own acts (Apply, Checked) | Chirality's checkpoint handling |
| Graduated autonomy (D-04) | Per-session agent modes and permission policy, chosen by the user; the client answers or forwards permission requests | Small |
| Records (D-07) | One normalised event stream (ACP `session/update`) for every agent, linked to host receipts | One recorder, not one per vendor |

## 5. The options, scored against the six parts

Qualitative; the reasoning is in the cells. "Owned code" counts only what
Chirality maintains.

| Option | Owned code | Imported change | Coupling | Replaceability | Comprehensibility | Notes |
|---|---|---|---|---|---|---|
| **A. ACP client + MCP host tools** | Smallest: an ACP client and the Chirality layer | Adapter and protocol releases, absorbed by their maintainers; Chirality follows protocol versions | Multi-vendor standard, versioned | A different harness is a configuration change | Standard formats and SDKs in mainstream languages | Lowest common denominator: vendor-only features beyond ACP are not used (see §6) |
| **B. Stock Codex App Server directly (the v3 path)** | Moderate: a Codex client plus v3's Runtime service if kept | Weekly Codex releases with schema drift (T7); Chirality regenerates and adapts | One vendor's published protocol | Changing harness means a second client | Known to this project | Richest Codex features (application tools, per-conversation provider, native plan mode); Claude models unreachable |
| **C. T3 Code as a gateway (`t3 serve`)** | Small, but a client for T3's API | Very high: alpha 0.0.x, ~1,500 commits a month, a pending rewrite of ~+341k/−171k lines, API not declared stable (T8) | A product's internal API, built on a release-candidate framework | Good across providers, but only through T3 | Large, unfamiliar framework (Effect 4 RC) | T3 itself uses ACP for several providers and is adding a generic ACP provider in its rewrite |
| **D. Fork T3 Code** | Very large (~0.5M lines of TypeScript) | Continuous rebasing against that churn | Private modification | Poor | Poor | The v3 patched-supplier lesson at a larger scale |
| **E. Own agent loop on a framework** | Largest: tools, sandbox, approvals, sessions | Model and framework APIs | Low-level, many | Good for models, poor for everything else | Depends on the team | Recreates what harnesses provide (M-1) |

On this reading, **option A serves the owner's reasons for liking T3 Code**
— many agents, no provider lock-in, less code in Chirality — **better than
T3 Code itself does**, because it reaches the same agents through the
standard T3 is itself converging on, rather than through T3's internal API.
T3 Code remains valuable as MIT-licensed reference code (provider-instance
and credential handling, the Codex sign-in overlay v3 already borrowed, UI
patterns) and as an app users may choose on their own.

## 6. What option A gives up, and what would answer it

| Given up or uncertain | Consequence | How to settle it without experiments |
|---|---|---|
| Vendor features beyond ACP: Codex application tools, per-conversation provider switching inside one server, Codex's native plan mode | Host tools move to MCP (the more portable route anyway); plans arrive as ACP plan updates; provider choice is per agent session | Read the adapters' feature lists and ACP's extension mechanism (both adapters already publish extensions for permissions and configuration) |
| Adapter lag behind vendor releases | New vendor features arrive later | Read the adapters' release history against the vendors' |
| Subagent visibility is a draft capability | Delegation inside the agent is less visible to the client | Read the draft and the adapter notes (claude-agent-acp documents its interim mechanism) |
| ACP began in editors (files, terminals, diffs) | Engineering objects do not fit ACP's primitives | They do not need to: domain objects travel over MCP, not ACP |
| MCP version support differs by agent | A host server may fail with an older client (SWBPIPE saw this) | Read each candidate agent's MCP support; require the current protocol |
| Terms for third-party clients using consumer sign-ins | Unchanged by the protocol choice: the adapter still uses the user's sign-in | Written confirmation from OpenAI and Anthropic, if and when v4 is distributed to others |
| Local-model quality | Outside Chirality's control under every option | Not a maintainability question |

## 7. Consequences for the rest of the architecture

- **The v3 Runtime service may no longer be needed.** With ACP, a host
  launches the agent (or its adapter) as a subprocess and speaks to it
  directly; Chirality's layer can live in the client. Removing a Node
  service from every host is itself a maintainability gain (M-1, M-6).
  To confirm by reading the Runtime's current responsibilities against ACP.
- **One interface component set for all hosts.** SWBPIPE is Tauri (Rust +
  React). If the Chirality panel is a React component set and the ACP client
  logic is small, the same pieces serve SWBPIPE and the standalone Workflow
  App. Building the standalone app on the same stack (Tauri) rather than v3's
  Electron + Next would leave one stack across every Chirality application.
  This is an option, not a finding.
- **Host integration belongs to each host project.** SWBPIPE owns its MCP
  server, as it owns its live controller today; Chirality owns the contract
  shape they share (inspect, preview, submit, status, basis binding).
- **Records get simpler.** One normalised stream from ACP for every agent,
  plus the host's own receipts (D-07), instead of one vocabulary per vendor.
- **Process weight is part of maintainability.** The build-method
  conversation (Q-11) should be judged by the same measure: every record
  should serve a decision, a reliance claim or recovery (M-8).

## 8. Questions for the owner

1. Do these eight principles express what you mean by maintainability, or
   would you change or rank them?
2. Should the v4 basis adopt the two seams — ACP to the agent, MCP to the
   host — as the architectural direction, with the particular agent left to
   the user's configuration?
3. Should the standalone App for Creating Workflows share SWBPIPE's stack
   (Tauri + React), so every Chirality application runs on one stack?
