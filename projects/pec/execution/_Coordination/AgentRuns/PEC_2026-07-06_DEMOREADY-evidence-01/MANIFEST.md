# PEC agent-path demo-readiness combined smoke — evidence 01 (2026-07-06)

> **Epistemic status: immutable evidence capture** (D-T0-13 capture convention).
> Owner steer of record (2026-07-06, launcher, Ryan Tufts): prioritize getting
> the PEC agent path demo-ready on scratch/demo basis — verify and, where
> lawful, enable the app-dev harness bridge plus PEC sidecar together; no pilot
> DB; no real/non-scratch PEC data; accept/apply/force remain human-only.
> This pack is a smoke/evidence capture only — **no pilot-readiness, go-live,
> or correctness claim** (F-PEC-2).

## Basis

- Code SHA: `0513640a5` (branch `codex/pec-demoready-smoke`, byte-identical to
  `main` at capture — the pack itself is the branch's only delta).
- Scratch basis: fresh OS-temp SQLite DB, seeded via the D-PEC-06-guarded
  `seed.demo`, **deleted with its WAL/SHM after capture**. No pilot DB
  touched; no real/non-scratch PEC data anywhere in the run; the owner's
  `pec-demo.db` dev instance untouched.
- One instance, both clients (the steer's "together"):
  - pec server on `127.0.0.1:4917` (`PEC_DB` = the scratch path), with
    `PEC_AGENT_URL=http://127.0.0.1:4918` wiring the D-PEC-17 agent proxy;
  - `@pec/agent-sidecar` on `127.0.0.1:4918`, **stub engine** (`egress: none`),
    logged in as the run-provisioned agent person
    `pec-demo-agent@rehearsal.demo` (`is_admin=0`, coordinator-class grant —
    the rehearsal-01 actor pattern; random per-run password, never captured);
  - app-dev harness live handlers (`domain_propose_operation`,
    `domain_proposal_validate`, D-APP-52) invoked directly with a real session
    context against the same server, as the same agent person.
- Human-side acts (login as seed-demo `admin@aurora.dev`, synthetic persona)
  are **reads and agent-directing messages only** — `agent.direct` via the
  server proxy. **No accept, no apply, no reject, no `force` was performed by
  anyone in this run** (steer: those remain human-only; both proposals are
  left `ready_for_review`, `appliedAt = null` — artifact 12).
- Driver: session-scratchpad script (uncommitted, deterministic re-run;
  corrected once for an evidence-only endpoint typo and fully re-captured on a
  fresh scratch DB). Synthetic CSV rows only (`SYN-D-3xx`).

## What each artifact proves

| Artifact | Seam proven |
|---|---|
| `01_sidecar_health_direct.json` | Sidecar up: `engine: stub`, `egress: none`, `configured: true`, agent person identified. |
| `02_harness_propose_mdl.json` | Harness → PEC: `domain_propose_operation` files IPR-0001 (mdl, 2 would-create) via the live HTTP seam — `ready_for_review`. |
| `03_harness_validate_readonly.json` | `domain_proposal_validate` returns the stored report with `version`/`dryRunAt` unchanged (read-only, rider 7 — never recomputes). |
| `04_harness_refresh.json` | Version-guarded refresh recomputes the dry-run (v↑, still `ready_for_review`). |
| `05_proxy_agent_status.json` | Human → server proxy `GET /api/projects/:pid/agent/status` → sidecar health through pec's RBAC (`agent.direct`), human cookie never forwarded. |
| `06_agent_msg_status.json` | Sidecar → PEC: agent `status` reports **the harness-filed IPR-0001** — both clients share the one agent identity and API seam. |
| `07_agent_msg_capabilities.json` | Capabilities reply states the boundary verbatim: "Accept, apply, and reject-of-others happen in Admin, by you — never by me." |
| `08_agent_msg_propose_csv.json` | Human pastes CSV to the agent → sidecar files IPR-0002 through its own session (`act:result import.propose`, `ready_for_review`), reply carries the WF-8 signature + human accept/apply pointer. |
| `09_agent_msg_proposals.json` | Agent lists both proposals (IPR-0001 harness-filed, IPR-0002 sidecar-filed) with lifecycle states. |
| `10_agent_msg_accept_refused.json` | "accept and apply IPR-1 now" → no accept/apply act exists in the stub's vocabulary (D-PEC-17 GOV MAJOR fix); the reply restates the human-only boundary. No accept occurred (artifact 12). |
| `11_agent_msg_queue.json` | Agent intake-queue read (empty on this scratch basis). |
| `12_admin_proposals_list.json` | Human-side API cross-check: exactly IPR-0001/IPR-0002, both `ready_for_review`, `appliedAt = null` — nothing accepted/applied/forced. |

`SHA256SUMS` covers all 12 artifacts.

## Same-day deterministic verification (run in-session, same SHA)

- pec belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill` — pass (incl. the 37-test sidecar suite; drill 17/17 on its
  own OS-temp scratch DB).
- D-APP-52 opt-in live seam test: `PEC_BRIDGE_IT=1 npx vitest run
  src/__tests__/integration/pec-bridge.integration.test.ts` — 3/3 pass
  (hermetic scratch server, deleted after).

## Live-LLM status (stated plainly; nothing faked)

**Live-LLM demonstration remains DEFERRED.** No `ANTHROPIC_API_KEY` exists in
this environment and `@anthropic-ai/claude-agent-sdk` is **not installed** in
the pec workspace (verified at capture; the `@anthropic-ai` package under the
app-dev frontend's `node_modules` is the harness's own dependency, not the
sidecar's). Every event in this pack is the deterministic stub engine or a
direct API response. The owner-only enablement slate (dependency + key +
config, zero source change — D-PEC-17 key-droppable seam):

```
cd projects/pec
npm i @anthropic-ai/claude-agent-sdk -w agent-sidecar   # owner act: new external package (F-PEC-3 posture — sidecar only, server stays zero-dep)
export ANTHROPIC_API_KEY=...                             # owner-held; never committed
PEC_AGENT_ENGINE=sdk                                     # selects the SDK engine; egress class 'model-provider' arms the D-T0-20 O-B read clamp
```

Selecting `sdk` without the package or key fails at startup naming exactly
those steps (test-pinned in the sidecar suite).
