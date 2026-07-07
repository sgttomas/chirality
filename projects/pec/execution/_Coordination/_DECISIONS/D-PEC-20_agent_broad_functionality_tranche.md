# D-PEC-20 - PROPOSAL: agent broad-functionality source tranche (dual access basis + read acts + screen context adoption)

**Status:** PROPOSAL / AWAITING_RULING.
**Date prepared:** 2026-07-06
**Decision ID:** D-PEC-20
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1;
D-GOV-04). Companion tier-0 row: `D-T0-21` (the access-basis ruling this
tranche implements — this row is rulable only with/after it). Packet form per
the D-PEC-17 precedent (tranche detail folded into the packet).

## Why this row exists

Owner direction of record (2026-07-06, in-session, verbatim in `D-T0-21`):
expand agent functionality and data access broadly for designer/sole-user
testing, keeping the narrow controls in place too. The D-PEC-17 v1 sidecar
deliberately shipped: (a) the model-provider read clamp hard-wired to the
D-T0-20 enumeration, (b) a bounded act vocabulary (propose/refresh/withdraw/
status/triage/queue/screen.read/whoami), and (c) screen context publishing
record ids on two detail routes only. All three are the surfaces this tranche
would widen.

## Verified current state

| Fact | Source |
|---|---|
| Clamp: `assertReadInsideEnumeration` throws outside intake/import under `model-provider` egress. | `projects/pec/agent-sidecar/src/acts.ts:36-60` |
| Acts vocabulary is the bounded set in `bindActs`; no register/overview read acts exist. | `projects/pec/agent-sidecar/src/acts.ts:93-` |
| The pec client (`pec-client.ts`) wraps only the routes those acts need. | `projects/pec/agent-sidecar/src/pec-client.ts` |
| Every needed read route already exists server-side, RBAC'd (overview, packages, deliverables, plan, my-week, log, holds, approval-register, decisions, risks, tracker, interfaces, intake, history/:recordType/:id, revisions/:id/explain, reports/*, export/:register). **No server change is required.** | `projects/pec/server/src/api.ts` |
| Screen context: route + ids only; `usePublishScreenContext` exists but no list page adopts it (v1 scope note in the D-PEC-17 packet). | `projects/pec/web/src/agent/context.tsx` |
| Accept/apply/reject-of-others/`force` are structurally out (no method, URL denylist, disposition payload guard, RBAC 403) — each test-pinned. | sidecar test suite; D-PEC-17 evidence |
| Sidecar zero-runtime-dep posture; the SDK engine is the config-selected exception (owner-enabled 2026-07-06, uncommitted). | `projects/pec/agent-sidecar/package.json`; Receipt 43 |

## Decision to rule

Whether to authorize one source tranche implementing the D-T0-21 basis:

1. **Config:** `PEC_AGENT_ACCESS=enumerated|broad` (default `enumerated`) in
   `config.ts`; `/agent/health` reports it; the web panel badge shows it.
2. **Clamp keying:** `assertReadInsideEnumeration` takes the access basis:
   `enumerated` ⇒ exactly today's behavior (regression-pinned); `broad` ⇒
   RBAC-visible reads pass for model-provider engines too.
3. **Read acts** over the existing GET routes, exposed to both engines:
   project overview/governance signals, register reads (deliverables,
   packages, plan, my-week, holds, approvals, decisions, risks, tracker,
   interfaces, log), record history, revision explain, sponsor-brief /
   package-pack report payloads. Read-only; summaries carry record refs.
4. **Screen context adoption:** main list pages publish visible record ids
   via the existing hook (route + ids only — rider 5's no-DOM-scrape rule
   unchanged); detail-route coverage extended to the other record types.
5. **Engine prompt/vocabulary:** stub intent routing + SDK system prompt
   updated to name the new read acts; stub stays deterministic.
6. **Tests:** enumerated-basis regression pins (clamp identical to today);
   broad-basis read acts; boundary pins re-asserted under `broad` (accept/
   apply/reject/`force`/conversion-disposition all still refused + RBAC 403);
   health/badge disclosure.

**Not in scope (unchanged, structural):** accept/apply/reject-of-others,
`force` in any form, approval/decision/check outcome creation, conversion
dispositions, people/config/project mutation, any server route addition, any
new runtime dependency, real/non-scratch mutation basis.

## Fence (exact; STOP outside it)

- `projects/pec/agent-sidecar/src/{config.ts,acts.ts,pec-client.ts,http.ts,index.ts}`
- `projects/pec/agent-sidecar/src/engine/{port.ts,stub.ts,sdk.ts}`
- `projects/pec/agent-sidecar/test/**` (+ new test files)
- `projects/pec/agent-sidecar/README.md`
- `projects/pec/web/src/agent/{AgentPanel.tsx,context.tsx}`
- `projects/pec/web/src/pages/*.tsx` — `usePublishScreenContext` adoption
  lines only
- No `core/**`, no `server/**`, no root manifests, no profile, no DB.

## Options

- **O-A (recommended):** the tranche as specified (items 1–6).
- **O-B:** items 1–3 + 5–6 only (reads, no screen-context adoption).
- **O-C:** defer.

## Verification plan (workplan step-4 bar)

pec `npm run typecheck && npm test && npm run build && npm run drill`; scope
containment `git diff --name-only ⊆ fence`; adversarial review of the clamp
regression + boundary pins; self-check no baseline shift; coord-check on the
range; evidence: a scratch-basis capture of enumerated-vs-broad behavior
(same question, both bases) + boundary refusals under `broad`.

## Rollback

Single revert of the tranche commit(s); default basis is `enumerated`, so
reverting restores today's behavior even mid-run.

## Human ruling

*(open — the owner rules; record verbatim, with date)*
