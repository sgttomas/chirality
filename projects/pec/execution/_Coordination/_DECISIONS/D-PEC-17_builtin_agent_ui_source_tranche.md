# D-PEC-17 - PROPOSAL: source-tranche authorization for the built-in agent UI (D-PEC-16 O-A, runtime RT-B local sidecar)

**Status:** RULED — O-A, recorded 2026-07-06 under the owner's conditional
standing pre-ruling (Receipt 32 item 4; see Human ruling at the end of this
packet).
**Date prepared:** 2026-07-06
**Decision ID:** D-PEC-17 (opened NOT_PREPARED by the D-PEC-16 O-A ruling mechanism, 2026-07-06)
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: `D-PEC-08_upload_agent_source_tranche_authorization.md`
and its executed tranche record
`../TRANCHE_2026-07-05_D-PEC-08_upload_agent_v1.md` (exact file fence, tests,
RV-obligation dispositions, rollback/verification plan). This packet folds the
tranche detail into the decision packet, since the pre-ruling mechanism selects
the recommended option without a separate tranche-request round trip (RV-20
coordination precedent note: this header names both precedents).

**Verification status (pre-ruling condition a):** two-lens adversarial
verification completed 2026-07-06 (fact lens + governance lens, both told the
result will be pre-ruled without the owner's read). FACT: PASS — 0 BLOCKER /
0 MAJOR; 6 MINORs (FACT M-1..M-6) + 5 NITs (FACT N-1..N-5), all fixed in this
revision. GOVERNANCE: PASS-with-fixes — 0 BLOCKER, 1 MAJOR (GOV MAJOR-1:
conversion-to-approval-records loophole — fixed BOTH ways below: stub
vocabulary exclusion AND engine-independent disposition-payload guard, each
test-pinned), 4 MINORs (GOV MINOR-2 `agent.direct` narrowed; MINOR-3 fence-note
counter-texts disposed; MINOR-4 panel pin named as evidence observation; plus
the bounds-citation minor), 3 NITs (GOV NIT-1 verbatim record string; NIT-2
pre-ruling expiry in the merge gates; NIT-3 clamp scoping citation + unknown-
egress default) — all fixed in this revision. The governance lens's
load-bearing judgment of record: **the two root-manifest fence rows are
lawfully openable by this ruled tranche** (no owner STOP), **conditional on**
(1) the `package-lock.json` zero-new-external-resolutions check and the
manifest-hunk-exact-match check remaining merge-gating, and (2) the receipt
recording the manifest opening explicitly — both conditions are carried as
binding text in the fence note, verification plan, and on-ruling mechanism
below and must not be weakened by any later fix round.

**In-bounds statement (pre-ruling condition b):** the recommendation below
(O-A) lies strictly inside the ruled architecture — D-PEC-16 O-A with runtime
RT-B (local sidecar), the adopted UI brief
`_DomainEngines/proposals/pec/BRIEF_2026-07-05_pec_builtin_agent_ui_design.md`
§§2–7, D-T0-19 (O-1A: single lane + decision-packet authoring scope; O-2A:
localhost transport + person-bound actor model; O-3A: the act mapping that
keeps the human-act boundary structural),
D-T0-20 O-B (enumerated visibility; scratch/demo mutation basis unchanged),
D-PEC-12 (L3 semantics + full-agency amendment), D-PEC-10 (actor model +
agent-act rider), and the RV-13..21 obligations of the adopted upload brief. It
adds no authority anywhere: the panel and sidecar are capability only —
anything the agent cannot do via the raw RBAC'd API it cannot do via them. One
fence honesty item is surfaced loudly rather than buried: the tranche cannot
deliver the ruled "one dev script starts server + sidecar" story without two
root-manifest line-item edits (`projects/pec/package.json`,
`projects/pec/package-lock.json`), which F-PEC-1 names closed ("never … root
manifests"). Opening exactly those rows is part of what this packet asks the
ruling to do — see "Fence note: the F-PEC-1 root-manifest tension" below. If
the owner regards that tension as outside the pre-ruling's bounds, this packet
STOPS at the gate for an explicit ruling instead.

## Authorization chain

1. D-PEC-07 O-C → adopted upload brief (RV-12 rider; RV-13..21 deferred) →
   D-PEC-08 O-A tranche (PR #82): the `import_proposal` seam shipped.
2. D-T0-18 O-A + D-PEC-12 (owner amendment: full agency inside the mechanical
   harnesses; "focus on making a useful agent for now"): L3 imports scope.
3. D-PEC-10 O-A: weekly five-document workflow; agent actor model (own person,
   `is_admin=0`, coordinator-class); agent-act rider; rehearsal-01 evidence.
4. D-T0-19 O-1A/O-2A/O-3A + D-T0-20 O-B (RULED 2026-07-06): the bridge lane +
   authoring scope (O-1A), the localhost transport + person-bound actor model
   (O-2A), the act mapping (O-3A); enumerated OPEN visibility surface (i)–(iv);
   mutation basis unchanged (scratch/demo only).
5. D-PEC-16 O-A, runtime RT-B (RULED 2026-07-06, verbatim in its packet): UI
   brief ADOPTED; this row opened NOT_PREPARED "per the mechanism, then prepare
   and proceed under item 4".
6. Owner session authorization (2026-07-06, Receipt 32 item 4, quoted verbatim
   there): conditional standing pre-ruling for packets prepared this session,
   including D-PEC-17 by name; environment constraint of record: **no
   `ANTHROPIC_API_KEY` exists in this environment and none will be provided
   this session** — every LLM seam goes behind a config-driven engine port with
   a deterministic stub, key-droppable later without source change; all tests
   and evidence key-independent; live-LLM demonstration deferred and its
   absence stated plainly, never worked around.

## Decision to rule

Whether to authorize the bounded source tranche below implementing the adopted
built-in-agent-UI design under runtime RT-B: a zero-runtime-dependency local
Node sidecar hosting the agent behind an engine port (deterministic stub
default), a shell-level agent panel in the pec web app, and a narrow agent
proxy surface in the pec server (the adopted brief's "`/api/agent/*`"
shorthand; exact route shape `/api/projects/:pid/agent/*`) — with the exact
file fence, tests, RV-13..21 dispositions, riders, rollback and verification
plan named here.

## What v1 implements (scope)

1. **Agent sidecar** — new package `@pec/agent-sidecar` at
   `projects/pec/agent-sidecar/` (own manifest; the pec **server** package gains
   zero dependencies — ADR-002 intact; the sidecar itself also ships with zero
   runtime dependencies in v1). A separate local Node process (`node:http`,
   loopback-only, default port 4812, `PEC_AGENT_PORT`) that:
   - logs into pec via `POST /api/auth/login` as the owner-provisioned agent
     person (`is_admin=0`, coordinator-class grant: `import.propose` +
     `intake.triage`, never `import.accept`) using credentials from local
     environment (`PEC_AGENT_EMAIL`/`PEC_AGENT_PASSWORD`), never committed,
     never echoed into responses; holds the `pec_session` cookie in memory
     only (the D-T0-19 O-2A transport, verbatim shape); re-logins on 401 (the
     adopted bridge brief §3 session detail, shared seam);
   - **refuses to operate** if the logged-in person is `isAdmin` or if a
     `can/import.accept` probe answers allowed (misprovisioned actor —
     structural guard on top of RBAC, which remains the real enforcement);
   - drives pec **exclusively through the RBAC'd HTTP API** via a bounded
     client whose method surface IS the adopted UI brief's §4 agent client
     contract (adopted via D-PEC-16): propose / refresh / withdraw-own
     (reject-own); intake open-triage + disposition with grounds; enumerated
     reads. It has **no method** for accept, apply, reject-of-others, `force`,
     or approval/decision/check outcomes, plus a URL-path guard refusing those
     routes (defense in depth; K-DOMAIN-3 stays enforced by pec RBAC, not
     prompt text);
   - **disposition-payload guard (GOV MAJOR-1 fix, engine-independent):** the
     one place pec RBAC does NOT stop the agent is the legitimate disposition
     route — a `converted` disposition body may name records that intake
     conversion creates under `skipPermission`, **including approval records**
     (live at `server/src/services/intake.ts:106-131`), which the D-PEC-10
     rider and the brief's §4 "Never" list forbid the agent to create. The
     acts layer and `pec-client.disposition` therefore refuse, with a typed
     refusal event, ANY disposition payload that would create approval
     records — a structural guard binding every engine (the SDK drop-in
     inherits it), pinned by test;
   - failure semantics per the ruled contract: `409 STALE_PROPOSAL` → refresh
     → report that the human must re-accept (normal flow, never retried
     around); `403` → report, never escalate.
2. **Engine port + deterministic stub** — `AgentEnginePort` (config-selected
   `PEC_AGENT_ENGINE: 'stub' | 'sdk'`, default `'stub'`; port shape mirrors the
   app-dev `harness-contract` `agent-engine-port.ts` for later convergence,
   without importing it — see Options). The stub is deterministic
   intent-routing over the same bounded acts layer the SDK engine will use:
   - dropped/pasted CSV → contract detection by header match against the five
     §16 contracts (ambiguous → ask; user may name the contract) → propose →
     report `IPR-` ref, lifecycle state, full dry-run counts, and a deep-link
     to the Admin "Proposed imports" section for the human accept/apply;
   - refresh / withdraw-own by `IPR-` ref;
   - triage: `open-triage`/`disposition` of a named `INTK-` item with the
     grounds the instruction carries (grounds recorded in the disposition
     note); instructions without grounds or an ungroundable item → refuse and
     leave for the owner (D-PEC-10 rider), stated in the reply. **The v1 stub
     disposition vocabulary is `parked` / `duplicate` / `rejected` only (GOV
     MAJOR-1 fix): `converted` is explicitly refused** with a deterministic
     reply directing the owner to perform the conversion on-screen (conversion
     can create records under `skipPermission`, including approval records the
     agent must never create — D-PEC-10 rider); `merged` is likewise outside
     the v1 vocabulary (disclosed scope, not a silent trim — a future engine
     may exercise `converted`/`merged` for non-approval records only, behind
     the acts-layer payload guard above, under its own evidence);
   - status queries: the agent's open proposals with lifecycle badges, triage
     queue summary, screen-context answers (route + visible record ids only);
   - everything else → a deterministic capability statement. The stub never
     fabricates model output, never emits an accept/apply act, and identical
     input + engine state yields byte-identical events (pinned by test).
3. **SDK engine loader (key-droppable seam)** — `engine/sdk.ts` ships as a
   lazy `await import('@anthropic-ai/claude-agent-sdk')` loader driving the
   same acts layer. **No SDK dependency is added in v1** (see Options /
   verified facts). Selecting `engine: 'sdk'` without the package or key
   fails at startup with a clear message. The later drop-in is: add the
   dependency to `agent-sidecar/package.json`, set `ANTHROPIC_API_KEY`, set
   `PEC_AGENT_ENGINE=sdk` — **no source change**, exactly as the D-PEC-16
   adoption note and Receipt 32 item 4 require.
4. **Visibility clamp (D-T0-20 O-B)** — the acts layer tags every read as
   inside/outside the enumerated surface (i) intake items + dispositions,
   (ii) `import_proposal` records/reports + import-related history, (iii) the
   profile's `chirality_readable_artifacts` set, (iv) owner-dropped files. The
   engine port declares its egress class (`'none'` for stub, `'model-provider'`
   for sdk); reads outside the enumeration are refused whenever egress is
   `'model-provider'`. The egress-keyed reading rests on D-T0-20's own scoping
   sentence — its decision line covers "LLM-hosted agent(s) … — all are
   external-model sessions", and reading-is-routing is the ruling's rationale;
   the stub session is not an external-model session, so under the stub
   nothing routes to any provider and v1 is visibility-lawful by construction.
   **Convention of record (GOV NIT-3):** any future engine subject whose
   egress class is undeclared or unknown defaults to `'model-provider'` (the
   conservative bound — relevant before any convergence with the app-dev
   port's three-subject type). The clamp is pinned by test so the SDK drop-in
   cannot widen the surface.
5. **Server proxy (recommended reachability)** — two narrow routes in the pec
   server, hand-rolled over `node:http` (zero new server dependencies,
   ADR-002 intact by construction):
   - `GET /api/projects/:pid/agent/status` — sidecar health + engine subject +
     agent person's name (for WF-8 attribution rendering);
   - `POST /api/projects/:pid/agent/messages` — forwards `{message, context?,
     attachment?}` to the sidecar; same-origin guard (RV-21, same
     `requireSameOrigin` as proposal mutations); 6 MiB body cap (attachment ≤
     the 5 MiB RV-14 proposal cap); **strips cookies** before forwarding (the
     sidecar acts under its own session, never the human's); sidecar down →
     `503 AGENT_UNAVAILABLE`.
   Both routes require an authenticated **human** session with the new
   `agent.direct` permission (below). The panel therefore works from the one
   pec origin in both dev (Vite proxy) and production (static `web/dist`
   serving) with no CORS surface.
6. **RBAC naming (RV-16 analog, ruled requirement)** — new permission action
   `agent.direct` in `core/src/permissions.ts`: **who may open the panel and
   direct the agent** — `admin`, `pm`, `coordinator`: exactly the roles that
   hold BOTH `import.propose` and `intake.triage` themselves (GOV MINOR-2
   fix). `document_controller` is deliberately EXCLUDED although it holds
   `import.propose`: it lacks `intake.triage` (verified live,
   `core/src/permissions.ts:93-95`), and granting it `agent.direct` would let
   it direct the agent (whose coordinator-class grant CAN triage) to
   disposition intake items — triage-by-proxy for a role that lacks the
   permission. The chosen set keeps directing-the-agent no wider than the
   director's own act families. Also: deliberately NOT `config.manage`
   inheritance and NOT in `PERSONAL_JUDGMENTS`; viewers/contributors refused;
   instance-admin break-glass applies as everywhere. The panel probes it via
   the existing `GET /api/projects/:pid/can/:action` route. Note the two-key
   property: `agent.direct` gates who may *speak to* the agent; what the agent
   can *do* is bounded separately by the agent person's own grant — the panel
   adds capability, never permission.
7. **Agent panel (web, brief §5 exactly)** — `web/src/agent/` components
   mounted in the shell (`main.tsx`): dockable panel with conversation thread;
   file-drop/paste zone routing to the shipped proposal seam via the agent's
   propose act (CSV only, RV-14); live status of the agent's open proposals
   with lifecycle badges; triage queue summary; **screen-context grounding**
   as client-side route + visible record ids only (a `ScreenContext` provider
   derives route + route params; list pages MAY publish visible ids through an
   optional hook — no page file is edited in v1, so v1 context is route +
   route-derived ids; the panel never scrapes the DOM); **no accept/apply/
   reject-of-others control ever renders in the panel** — it deep-links to the
   existing Admin "Proposed imports" components under the human's own session
   and shows their outcomes; every agent act renders with the agent person's
   name exactly as history records it (WF-8).
8. **Dev story** — root scripts: `npm run dev` starts server + sidecar + web;
   `npm run dev:agent` starts the sidecar alone. Unconfigured credentials are
   non-fatal: the sidecar starts, `/agent/health` reports unconfigured, and
   messages return `AGENT_NOT_CONFIGURED` — so `npm run dev` works out of the
   box.

**No database change of any kind:** no new table, column, record type, or
migration. The proposal/intake/history/audit records the agent touches are the
shipped ones, reached only through the API.

Out of scope, unchanged from the adopted brief §7: auto-apply or any
agent-side accept; `force` in any form; agent-initiated imports without an
owner-dropped basis; SSO; non-import write families (each needs its own row
per D-PEC-12 §2); multi-agent orchestration; mobile; SSE streaming (the event
schema is designed to survive that upgrade; v1 is request/response);
cross-project `file:` dependency on `@chirality/harness-contract` (see
Options); the `@anthropic-ai/claude-agent-sdk` dependency itself.

## Verified live-tree facts this packet rests on (2026-07-06)

| Fact | Source |
|---|---|
| pec is an npm workspace (`core`, `server`, `web`); root scripts run `typecheck` (core/server/web) and `test` (core/server) per workspace; `build` is web-only; server package has zero runtime deps. | `projects/pec/package.json`; `server/package.json` |
| ADR-002: zero server runtime deps, `node:http` router, Node ≥ 23.6 type-stripping, erasable-syntax-only TS. | `projects/pec/docs/adr/ADR.md` ADR-002; `tsconfig.base.json` (`erasableSyntaxOnly`) |
| The proposal seam is shipped and RBAC'd exactly as the D-T0-19 mapping table states (propose/list/get/refresh/accept/reject/apply; same-origin guard on mutations; hash+version-bound accept; watermark staleness). | `server/src/api.ts:338-366`; `server/src/services/proposals.ts` |
| Auth is cookie/session only; sessions are person-bound; `rolesFor` is per-project; no token mechanism. | `server/src/auth.ts` |
| `import.propose`: admin/pm/coordinator/document_controller; `import.accept`: admin only; `intake.triage`: coordinator/pm/admin; instance-admin break-glass excludes `PERSONAL_JUDGMENTS`. | `core/src/permissions.ts` |
| The web shell (`main.tsx`) is React 18 + Vite + react-router; Vite dev proxies `/api` → :4810; production serves `web/dist` from the pec server — one origin either way. | `web/src/main.tsx`; `web/vite.config.ts`; `server/src/index.ts:55-66` |
| The Admin page owns the "Proposed imports" accept/apply components (deep-link target `/p/:pid/admin`). | `web/src/pages/Admin.tsx:97` |
| `@anthropic-ai/claude-agent-sdk` is NOT resolvable in the pec tree (absent from `projects/pec/node_modules` and the repo root); it exists only inside `projects/chirality-app-dev/frontend/node_modules`. Adding it to pec would require a network install this session. | `ls` verification 2026-07-06 |
| `@chirality/harness-contract` is a private, src-only, dependency-free workspace package of the app-dev frontend (`frontend/packages/harness-contract`); its `agent-engine-port.ts` exports `AgentEnginePort` with `subject: 'stub' | 'anthropic-direct' | 'claude-agent-sdk'`. Consuming it from pec would need a cross-project `file:` dependency. | that package's `package.json` + `src/agent-engine-port.ts` |
| The agent person is provisioned per scratch run (rehearsal-01: `pec-agent@rehearsal.demo`, personId 16, coordinator, `is_admin=0`) — no committed seed change exists or is needed. | `_DomainEngines/pec/PEC_2026-07-05_DPEC10-rehearsal-01/MANIFEST.md` |
| The server test harness stands up a real HTTP server + temp DB + seeded role cast, reusable by relative import. | `server/test/harness.ts` |
| `data_residency` is `OPEN_ENUMERATED` per D-T0-20 O-B with the (i)–(iv) enumeration recorded in the profile. | `_DomainEngines/profiles/pec.yaml:23` |

Delta vs the adopted brief noted for the record (no contradiction): brief §5.1
says the file-drop zone "routes to the adopted upload seam once its tranche
lands — until then, proposals are filed from pasted/dropped CSV exactly like
the Admin flow". The upload tranche (D-PEC-08) has already landed, so the two
clauses coincide: the panel's drop zone files proposals through the shipped
`import-proposals` routes from day one.

## Exact file fence (the only writable paths for this tranche)

| Path | Change |
|---|---|
| `projects/pec/package.json` | **root manifest (F-PEC-1 tension — see fence note):** add `"agent-sidecar"` to `workspaces`; add `dev:agent` script; extend the `dev`, `test`, `typecheck` script lines to include the new workspace. No other line changes. |
| `projects/pec/package-lock.json` | **root manifest (same note):** regenerated for the new workspace link only; **zero new external packages** (the diff must show no new registry resolution). |
| `projects/pec/agent-sidecar/package.json` | NEW — `@pec/agent-sidecar`, private, `type: module`, zero runtime deps; devDeps `typescript` + `@types/node` only (mirrors `@pec/server`); scripts: `dev`, `start`, `test`, `typecheck`. |
| `projects/pec/agent-sidecar/tsconfig.json` | NEW — extends `../tsconfig.base.json` with the `@pec/core` `paths` mapping + cross-workspace source `include`s the e2e test's harness import needs (mirrors `server/tsconfig.json`'s pattern exactly; content detail in the impl plan §2). |
| `projects/pec/agent-sidecar/README.md` | NEW — run story, env vars, actor provisioning pointer, and the key-droppable-seam statement (stub default; SDK drop-in = dependency + key + config, no source change). |
| `projects/pec/agent-sidecar/src/index.ts` | NEW — entrypoint: config → engine selection → loopback HTTP server. |
| `projects/pec/agent-sidecar/src/config.ts` | NEW — env-driven config (`PEC_AGENT_ENGINE` `'stub'`\|`'sdk'` default `'stub'`, `PEC_BASE_URL` default `http://127.0.0.1:4810`, `PEC_AGENT_PORT` default 4812, `PEC_AGENT_EMAIL`/`PEC_AGENT_PASSWORD`). |
| `projects/pec/agent-sidecar/src/http.ts` | NEW — loopback-only surface: `GET /agent/health`, `POST /agent/messages`. |
| `projects/pec/agent-sidecar/src/pec-client.ts` | NEW — bounded pec API client (the adopted UI brief's §4 contract as a method surface; loopback-only base URL; cookie in memory; misprovisioning refusal; URL denylist guard; disposition-payload guard — no approval-record creation). |
| `projects/pec/agent-sidecar/src/acts.ts` | NEW — the act/tool layer both engines call (propose/refresh/withdraw-own/triage/reads) + the D-T0-20 enumeration clamp keyed on engine egress class + the approval-records disposition guard (GOV MAJOR-1) + 409/403 ruled semantics. |
| `projects/pec/agent-sidecar/src/contract-detect.ts` | NEW — CSV header → §16 contract detection (ambiguous → ask). |
| `projects/pec/agent-sidecar/src/engine/port.ts` | NEW — `AgentEnginePort` types (subject `'stub'`\|`'sdk'`; egress class; event schema). |
| `projects/pec/agent-sidecar/src/engine/stub.ts` | NEW — deterministic intent-routing engine (the v1 default). |
| `projects/pec/agent-sidecar/src/engine/sdk.ts` | NEW — lazy dynamic-import SDK loader; clear startup error when package/key absent; **adds no dependency**. |
| `projects/pec/agent-sidecar/test/engine-stub.test.ts` | NEW — determinism + intent routing + never-accept/apply pins + the `converted` disposition-vocabulary refusal pin (GOV MAJOR-1). |
| `projects/pec/agent-sidecar/test/pec-client.test.ts` | NEW — denylist, loopback refusal, 409/403 semantics, misprovisioning refusal, approval-records disposition-payload guard pin (GOV MAJOR-1). |
| `projects/pec/agent-sidecar/test/sidecar-e2e.test.ts` | NEW — hermetic end-to-end against a harness-spawned scratch server (O-2B-style spawn, tests only, per the D-T0-19 O-2A recommendation sentence). |
| `projects/pec/core/src/permissions.ts` | add `agent.direct` action + rule (admin/pm/coordinator — see scope item 6 for the deliberate `document_controller` exclusion). |
| `projects/pec/core/test/permissions.test.ts` | pin the `agent.direct` matrix. |
| `projects/pec/server/src/agent-proxy.ts` | NEW — narrow `node:http` forwarder to the sidecar (zero deps; cookie-stripping; 6 MiB cap; 503 mapping). |
| `projects/pec/server/src/api.ts` | register the two `/api/projects/:pid/agent/*` routes (authed + `requireCan('agent.direct')` + same-origin guard on the mutation route). |
| `projects/pec/server/test/agent-proxy.test.ts` | NEW — proxy RBAC/guard/forwarding/503 tests against a fake loopback sidecar. |
| `projects/pec/web/src/agent/AgentPanel.tsx` | NEW — the shell-level panel (thread, drop zone, proposal badges, triage summary, Admin deep-links, agent-name attribution). |
| `projects/pec/web/src/agent/api.ts` | NEW — panel client for the `/api/projects/:pid/agent/*` routes (rides the existing `web/src/api.ts` transport). |
| `projects/pec/web/src/agent/context.tsx` | NEW — `ScreenContext` provider/hook (route + visible record ids only). |
| `projects/pec/web/src/main.tsx` | mount the provider + panel + topbar toggle (shown only when `can('agent.direct')`). |
| `projects/pec/web/src/styles.css` | panel styles. |

Everything else — including `pec.db*`, `pec-demo.db*`, `pilot-scratch/**`,
`backups/**`, `fixtures/**`, `tools/**`, `server/src/db.ts`, `repo.ts`,
`services/**`, `import/**`, `core/src/types.ts`, all other web pages, and all
three sub-workspace manifests (`core/`, `server/`, `web/` `package.json`s — the
server package gains **no** dependency line) — stays closed. F-PEC-1 remains
the outer fence; this packet opens exactly the rows above and nothing else.
Coordination-surface writes (this packet, the register row, the receipt, the
evidence snapshot under `_DomainEngines/pec/`) ride the standing
coordination-surface permissions, not this fence.

### Fence note: the F-PEC-1 root-manifest tension (stated, not buried)

F-PEC-1 (D-T0-15, verbatim): "No writes under `projects/pec/**` except
`execution/_Coordination/**`, `AGENTS.md`, and the one-time
`projects/pec/docs/STATUS.md` pointer edit; **never** `pec.db*`, `backups/**`,
source trees, fixtures, tools, **or manifests** …". Every ruled tranche
(D-PEC-08, D-PEC-09) has opened source paths against the same "source trees"
line — a ruled tranche naming an exact fence is precisely the lawful opening
mechanism, and this packet is that mechanism for this tranche. (Precedent
scope stated exactly: D-PEC-08 opened the "source trees" category and
explicitly kept root manifests closed — the precedent supplies the opening
MECHANISM, not the manifest CATEGORY; the category is opened here, by this
ruling.) The new item
here is that the fence includes **two root-manifest rows**. They are
unavoidable for the ruled design: RT-B's dev story (brief §3 RT-B row,
verbatim: "Dev story: one script starts server + sidecar."; the D-PEC-16 O-A
consequence text delegates the matter to this row: "the sidecar's
packaging/start story is a tranche-level design item") and the
verification plan's requirement that `npm run typecheck && npm test` cover the
sidecar both require the workspace registration and script edits in
`projects/pec/package.json`, and npm regenerates `package-lock.json` for the
workspace link. The alternative (an unregistered directory outside the
workspaces array, avoiding the manifest edit) was considered and rejected
because it silently breaks the ruled dev story and leaves the sidecar outside
the standing check set — a hidden scope trim worse than the disclosed tension. The manifest
delta is four script lines + one workspaces entry + a dependency-free lock
regeneration, each named above; the adversarial scope check (verification
plan) diffs the manifest hunks against exactly this description.

**Counter-texts engaged (the strongest objection, carried here on purpose —
GOV MINOR-3):** three texts sketch this tranche's fence as
`projects/pec/{server,web,core}/**`: the D-PEC-16 packet's "What adoption
changes" section ("an exact file fence under `projects/pec/{server,web,core}/**`"),
the adopted brief §8, and the pec register row description. None names root
manifests. Disposal: those sketches are demonstrably **non-exhaustive** — the
brief §8 and the register row each extend the same sketch with "+ sidecar
package location" (a path equally outside `{server,web,core}/**`), and the
D-PEC-16 body text omits even the sidecar package location that its own ruled
O-A requires. The sketches name where the bulk of the fence lands; the ruled
O-A consequence text ("packaging/start story is a tranche-level design item")
delegates the packaging facts — including how the package joins the dev and
check stories — to exactly this packet. The manifest rows are the mechanical
minimum of that delegated, ruled design item, not new scope.

**Conditions of the governance-lens manifest judgment (carried verbatim; may
not be weakened):** the two root-manifest rows are lawfully openable by this
ruled tranche **conditional on** (1) the `package-lock.json`
zero-new-external-resolutions check and the manifest-hunk-exact-match check
remaining **merge-gating** (verification plan), and (2) the receipt recording
the manifest opening **explicitly** (on-ruling mechanism, step 3). Rider 1's
server-manifest no-diff requirement stands unchanged.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | **Authorize the tranche as fenced above** — composite: proxy-via-pec-server reachability (`/api/projects/:pid/agent/*`), stub-only-v1 engine behind the port with the SDK loader shipped but no SDK dependency, sidecar as a registered `agent-sidecar` workspace (the two root-manifest rows opened), `agent.direct` RBAC naming, no DB change. | The ruled RT-B design lands whole and key-independent this session: one origin (no CORS surface; RV-21 guard reused; panel gated by a human-session permission server-side); the SDK/key drop-in later is config + dependency only, zero source change; server package stays zero-dep (ADR-002 by construction); every test and the evidence pack run stubbed/scratch. |
| O-B | Same, but **direct-port panel↔sidecar** (browser fetches `http://127.0.0.1:4812` directly; no server proxy, no `agent-proxy.ts`, no api.ts edit). | Two fewer server-fence rows, but: a second origin needing a CORS allowlist on the sidecar; the `agent.direct` gate becomes client-side-only (the sidecar cannot see pec sessions, so any local browser user could direct the agent); breaks the served-`web/dist` one-origin production story. Weaker than O-A on exactly the properties the brief's §6 constraints name. |
| O-C | O-A **plus the `@anthropic-ai/claude-agent-sdk` dependency now** (stub still default). | Not honestly executable this session: the package is not resolvable in the pec tree and installing it requires network; relying on another project's `node_modules` or a cache hit would be exactly the kind of workaround Receipt 32 item 4 forbids. Deferred: the dependency lands with the key, later, through the shipped loader. |
| O-D | Defer. | The adopted UI brief remains design authority only; the built-in-agent-UI half of the owner's top-priority bridge direction stays unimplemented; the D-T0-19 P3 phase stalls. |

## Recommendation (non-binding)

**O-A.** It is the smallest tranche that delivers the ruled design whole: the
sidecar holds no special power (another RBAC-bounded client, same seam as the
bridge and the loop agents); the engine port makes the no-key constraint a
structural property rather than a promise; the proxy keeps the panel behind a
named human permission on one origin; and nothing touches the database, the
import machinery, or any existing behavior. O-B is the honest second choice if
the owner prefers zero server-source rows, at the cost of a weaker panel gate.

Within the pre-ruling's condition (b): O-A is inside D-PEC-16 O-A/RT-B (the
brief's §3 RT-B row names the proxy option explicitly — "the pec server
proxying a narrow `/api/agent/*` surface (or a configured local port)" — and
names "packaging/lifecycle is the main tranche-level design item", settled
here; the one-origin framing is this packet's own argument for choosing the
proxy over the also-in-bounds port alternative, O-B), inside
D-T0-19/D-T0-20/D-PEC-12/D-PEC-10, and inside
the adopted brief's §6 constraints — except that its fence must open the two
root-manifest rows, which is surfaced in the fence note above as part of what
the ruling authorizes.

## RV-13..21 dispositions for this tranche's surfaces (adopted upload brief obligations; they bind where surfaces overlap)

- **RV-13 (hash/version binding, stale refusal) — discharged by inheritance,
  pinned.** This tranche adds no mutation path: every agent act rides the
  shipped seam whose binding/staleness guards D-PEC-08 discharged. The sidecar
  echoes proposal `version` on refresh/withdraw and surfaces
  `409 STALE_PROPOSAL` as the ruled refresh→human-re-accept flow (pinned by
  test). Accept remains the Admin components' hash+version echo, untouched.
- **RV-14 (CSV-only v1) — discharged.** The panel drop zone and the sidecar
  accept UTF-8 CSV text only (extension/content check; 5 MiB, mirroring the
  server cap); no multipart, no xlsx, no new dependency anywhere.
- **RV-15 (history vs audit) — discharged by inheritance.** No new record
  type; agent acts land as the shipped history/audit rows via the API, under
  the agent person. The panel renders attribution from those records (WF-8).
- **RV-16 (permission naming) — discharged.** `agent.direct` defined as above
  (who opens the panel / directs the agent), explicitly not `config.manage`
  inheritance; the agent's own authority remains its provisioned grant.
- **RV-17 (deterministic contract, stale dry-run, apply-failure) — discharged
  by inheritance.** Unchanged shipped semantics; the panel renders the same
  `ImportReport` the seam returns.
- **RV-18 (report completeness) — discharged.** The panel renders the full
  dry-run/apply report including `intakeCreated`, exactly as the Admin section
  does.
- **RV-19 (upload-store lifecycle) — discharged.** No new store: a dropped
  file's text becomes the proposal `source_csv` through the shipped route; the
  sidecar holds it in memory for the turn only; nothing is written to disk.
- **RV-20 (coordination precedent) — discharged.** Named in this packet's
  header.
- **RV-21 (CSRF posture) — discharged for the new surface.** The proxy's
  mutation route carries the same `requireSameOrigin` guard as the proposal
  mutations; the sidecar binds 127.0.0.1 only and is additionally reached in
  the recommended option only through the authed proxy; the proxy strips
  cookies before forwarding. Extending the guard to pre-existing routes stays
  the recorded candidate follow-up from the D-PEC-08 tranche record
  (`../TRANCHE_2026-07-05_D-PEC-08_upload_agent_v1.md`, RV-21 entry), not
  smuggled in.

## Riders (bind the ruled option)

1. **ADR-002:** the pec server package gains zero runtime dependencies — the
   proxy is hand-rolled `node:http`; `server/package.json` is not in the fence
   and must show no diff. (The sidecar package is also zero-runtime-dep in v1
   by choice, minimizing supply-chain surface until the SDK drop-in.)
2. **Engine port / no-key honesty:** config selects `'stub' | 'sdk'`; the stub
   is the default and the only engine exercised this session; no code path
   sources, hardcodes, or fabricates a key or model output; the evidence pack
   states plainly that live-LLM demonstration is deferred for lack of a key.
   The SDK drop-in later must require no source change (dependency + key +
   config only) — pinned by the loader's existence and its startup-error test.
3. **Actor:** the sidecar authenticates only as an owner-provisioned agent
   person, `is_admin=0`, coordinator-class grant; credentials from local env,
   never committed, never rendered; startup refusal on misprovisioning
   (instance-admin or accept-capable). The agent exercises only the D-PEC-10
   rider's act families (import propose/refresh/withdraw-own; intake
   open-triage/disposition; enumerated reads) even though a coordinator grant
   carries more.
4. **Human-act boundary:** the panel renders no accept/apply/reject-of-others/
   `force` control; those remain the existing Admin components under the
   human's session (deep-linked). The sidecar client has no such methods and
   refuses those URL paths. **Approval records are never agent-created by any
   route (GOV MAJOR-1):** the acts layer and client refuse any disposition
   payload that would create approval records under conversion's
   `skipPermission` (the D-PEC-10 rider's named loophole), and the v1 stub's
   disposition vocabulary excludes `converted` entirely — both pinned by test.
   K-DOMAIN-3 enforcement remains pec RBAC; these guards are the
   defense-in-depth for the one act RBAC does not stop.
5. **Screen context = route + visible record ids only**, read back through the
   API under the agent person's visibility; never DOM scraping.
6. **Visibility:** the D-T0-20 O-B enumeration is the read bound; the acts
   layer's egress-keyed clamp is pinned by test (rider 2's SDK drop-in cannot
   widen it). The egress-keyed reading rests on D-T0-20's own scoping ("all
   are external-model sessions"); any future engine subject with an
   undeclared/unknown egress class defaults to `'model-provider'` (GOV NIT-3
   convention of record).
7. **Mutation basis:** scratch/demo only for every test and evidence act this
   session (temp DBs and the committed fixtures; the live `pec.db*`/
   `pilot-scratch` files are untouched by the PR). The sidecar itself is
   basis-agnostic — it acts wherever the human runs it, under RBAC — but
   operation against the owner's real/non-scratch DB remains its own future
   row (D-T0-20 ruling sentence; Receipt 32 exclusions).
8. **No DB migration:** none exists in this tranche; if execution discovers a
   need, STOP — that is outside this fence and returns as its own row.
9. **No new authority:** the panel and sidecar add capability, never
   permission; anything outside the fence found necessary mid-run comes back
   as a register row, never an in-run widening (D-PEC-12 recorded
   interpretation).

## Tests (ride the same PR; all key-independent)

- `core/test/permissions.test.ts`: `agent.direct` matrix — admin/pm/
  coordinator allowed; **document_controller refused** (the deliberate
  exclusion, scope item 6); viewer/contributor/checker refused;
  viewer-only refusal; instance-admin break-glass; not a personal judgment.
- `server/test/agent-proxy.test.ts`: 401 unauthenticated; 403 for a member
  without `agent.direct` (contributor) and for non-members; cross-origin
  refusal on the mutation route (RV-21); `503 AGENT_UNAVAILABLE` when no
  sidecar listens; round-trip forwarding to a fake loopback sidecar with the
  human's cookie stripped and the body/status relayed intact; body-cap
  refusal.
- `agent-sidecar/test/engine-stub.test.ts`: byte-identical events for repeated
  identical turns (determinism); intent routing for propose (header-detected +
  named contract + ambiguous→ask), refresh, withdraw-own, triage-with-grounds,
  groundless-triage refusal (left for owner), status queries, capability
  fallback; the event stream never contains an accept/apply act; **a
  `converted` (or `merged`) disposition instruction yields the deterministic
  refusal event directing the owner to the screen act, never a disposition
  call (GOV MAJOR-1 pin, non-negotiable)**.
- `agent-sidecar/test/pec-client.test.ts`: method surface = the adopted UI
  brief's §4 contract
  (no accept/apply/reject-of-others/force/approval-outcome methods); URL guard
  refuses denylisted paths; non-loopback base URL refused by construction;
  409 → refresh-and-report semantics; 403 → report-never-escalate; startup
  refusal when the session is instance-admin or `can/import.accept` allows;
  **disposition-payload guard: any conversion payload naming approval records
  is refused with the typed refusal event before any network call (GOV
  MAJOR-1 pin, non-negotiable)**;
  enumeration clamp refuses out-of-enumeration reads when egress is
  `'model-provider'` and permits them under `'none'`.
- `agent-sidecar/test/sidecar-e2e.test.ts` (hermetic, O-2B-style spawn via
  `server/test/harness.ts`, temp DB): provision agent person (coordinator,
  `is_admin=0`); full turn through the sidecar HTTP surface — drop synthetic
  CSV → proposal created **attributed to the agent person** with dry-run
  report; refresh; withdraw-own; seeded intake item triaged with grounds;
  agent's direct accept attempt refused 403 (RBAC pin); human admin accept +
  apply still work over the same server (boundary intact end-to-end).
- `engine/sdk.ts` loader: config `'sdk'` without the package fails with the
  documented error (test asserts the message; no network, no key touched).
- Web: no unit-test framework exists in `@pec/web` (verified); the panel is
  verified by `typecheck` + `build` + the evidence rehearsal below — stated
  plainly, not silently skipped.

## Evidence (scratch-basis; the pack states the live-LLM deferral)

One immutable snapshot `_DomainEngines/pec/PEC_<date>_DPEC17-evidence-01/`
(D-T0-13/L3 convention): scratch `PEC_DB`, seeded cast + provisioned agent
person; server + sidecar via the one dev script; stubbed-engine panel
transcript — file drop → agent proposes (IPR ref + report) → triage with
grounds → status query with lifecycle badges; the accept/apply of the
rehearsal proposal performed as demo-cast human acts on the scratch basis
(permitted and disclosed per the D-PEC-12 full-agency amendment and Receipt 32
exclusions); **named evidence observation (GOV MINOR-4 — the panel-side pin,
since `@pec/web` has no test framework): "the panel renders no
accept/apply/reject-of-others control; the human act was performed through
the Admin deep-link under the human's own session" — captured explicitly in
the manifest's checklist**; history extract showing the agent/human actor
split (WF-8);
manifest stating verbatim that **no ANTHROPIC_API_KEY existed this session,
the engine ran `'stub'`, and live-LLM demonstration is deferred** — the P4
owner-at-the-screen rehearsal (D-T0-19) remains a separate, undischargeable-
agent-side gate and is not claimed by this evidence.

## Rollback plan

- One PR on branch `codex/pec-dpec17-agent-ui-tranche`; rollback before merge
  = close the PR; after merge = `git revert` of the merge commit (owner act or
  item-4c-conditioned agent act, recorded either way).
- **No DB migration exists**; nothing to unwind in any database. The tranche
  is additive: a new workspace, a new permission token (unused after revert),
  two new routes, and panel components; the only edits to existing files are
  the root-manifest script/workspace lines, the `api.ts` route registrations,
  the `permissions.ts` case, and the `main.tsx`/`styles.css` mounts — all
  removed cleanly by the revert. Live scratch/demo DBs are untouched by the
  PR (code-only tranche; tests run on temp DBs).

## Verification plan (workplan step-4 checks)

pec belt-and-braces `npm run typecheck && npm test && npm run build && npm run
drill` green **with the new workspace wired into typecheck/test** (drill/seed
unaffected — `tools/**` untouched); the `package-lock.json` diff shows zero
new external package resolutions; repo-wide harness `self-check` exit 0 with
no unexplained baseline shift; full `tools/` pytest at the final SHA; profile
validator where touched (no profile edit is planned — N/A expected);
`coord-check --diff` on the committed range; `git diff --check`; adversarial
scope check: `git diff --name-only` ⊆ the fence table plus this packet, the
register row, the receipt, and the evidence snapshot — and the two manifest
hunks match the fence note's description exactly. CI green on the PR for every
key-independent check; the known harness-premerge `ANTHROPIC_API_KEY` secret
failure is excluded per item 4c with its key-independent substance run locally
and the exclusion noted in the receipt. **The lockfile-diff check and the
manifest-hunk-exact-match check are merge-gating** (condition of the
governance-lens manifest judgment; may not be demoted to advisory), and the
receipt must record the root-manifest opening explicitly. **Pre-ruling window
(GOV NIT-2):** the item-4 pre-ruling "expires at session end or 24 hours after
this direction, whichever comes first" — the pre-ruled selection, the tranche
execution, and any self-merge must ALL complete inside that window; if the
window lapses first, STOP: record the state, leave the PR open for the owner's
own ruling and merge. Merge per item 4c only when all of the
above hold; otherwise STOP for the owner.

## On ruling (mechanism)

This packet is prepared under the owner's 2026-07-06 conditional standing
pre-ruling (session authorization item 4, quoted verbatim in
`_DomainEngines/pec/LOOP_RECEIPTS.md` Receipt 32), which the D-PEC-16 ruling
directed this row to proceed under. Mechanism:

1. Run the two-lens adversarial verification pass (fact lens + governance
   lens, fable agents at high effort), the verifiers told the result will be
   pre-ruled without the owner's read; fix every BLOCKER and MAJOR (condition
   a). Re-verify the in-bounds statement (condition b) after fixes; if any fix
   moves the recommendation outside the ruled architecture — or if the owner
   treats the root-manifest fence rows as needing an explicit ruling — STOP
   and bring it to the owner.
2. On both conditions passing, record here and in the register row, naming
   O-A alongside (not inside) the quoted string, the exact continuous verbatim
   phrase the direction requires: recommended option "selected by the owner's
   2026-07-06 conditional pre-ruling" — i.e. the record reads: O-A —
   recommended option "selected by the owner's 2026-07-06 conditional
   pre-ruling", with the pointer to pec Receipt 32 (GOV NIT-1). K-AUTH-1
   intact: the ruling act is the owner's, made in that direction; the agent
   only records which option the pre-ruling selected.
3. Execute branch-first per the fence; tests + evidence as named; the
   verification plan gates the merge (item 4c, including the pre-ruling
   expiry window — selection, execution, and self-merge all inside session
   end / 24 h, whichever first, else STOP and leave the PR for owner merge);
   the receipt records the selection, any self-merge, the live-LLM deferral,
   **and the root-manifest opening explicitly** (condition 2 of the
   governance-lens manifest judgment).
4. O-B/O-C/O-D or a STOP under (1) or (3): the row records the outcome and
   waits for the owner; no source change beyond what a lapsed-window open PR
   already carries (which then awaits the owner).

## Human ruling (recorded 2026-07-06)

O-A — recommended option "selected by the owner's 2026-07-06 conditional
pre-ruling", with the pointer to `_DomainEngines/pec/LOOP_RECEIPTS.md`
Receipt 32, where the owner's conditional standing pre-ruling (2026-07-06,
in-session steer, Ryan Tufts) is quoted verbatim. K-AUTH-1 intact: the ruling
act is the owner's, made in that direction; the recording agent only records
which option the pre-ruling selected.

Conditions at recording: (a) the two-lens adversarial verification pass is
complete with every BLOCKER and MAJOR fixed (outcomes in the Verification
status header above; verifiers were told the result would be pre-ruled
without the owner's read); (b) the in-bounds statement was independently
re-checked by the governance verifier, whose load-bearing judgment — the two
root-manifest fence rows are lawfully openable by this ruled tranche, no
owner STOP, under its two carried conditions — is recorded in the header and
bound in the fence note, verification plan, and mechanism step 3. The ruling
act was received with `main` at `4c636e53e` (tag
`pre-bridge-session-2026-07-06`); recorded and published by this tranche's
PR. Execution, checks, self-merge, and the receipt follow mechanism step 3,
inside the pre-ruling's expiry window.
