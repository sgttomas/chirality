# PEC — 9-Domains: Project Execution Control

Web-based, multi-user system of record for multidisciplinary engineering execution control: role homes,
controlled records, condition-gated transitions, and derived (always explainable) status. Implements
`docs/PRD.md` (v0.4), Phase 1 scope.

## Layout

| Path | Contents |
|---|---|
| `docs/PRD.md` | Product requirements (basis document, v0.4) |
| `docs/SPEC.md` | Implementation specification: data model, lifecycles, conditions engine, derived status, API, RBAC |
| `docs/adr/ADR.md` | Architecture decision records (implementer-level; PRD OM-*/D-* taken as given) |
| `docs/TRACEABILITY.md` | P1 requirement → module + test mapping |
| `core/` | Pure domain engine (no I/O): lifecycles, conditions, status, permissions, calendar |
| `server/` | Node 24 + `node:sqlite` API server (zero runtime deps): persistence, history/audit, RBAC, REST, import/export |
| `web/` | React + Vite SPA: six role homes + registers |
| `tools/` | seed script (demo FEED project), backup |
| `fixtures/` | sample CSVs for the §16 import contracts |

## Run

```bash
npm install            # workspace deps (web toolchain; core/server have none at runtime)
npm run seed           # create pec.db with the demo FEED project + users
npm run dev            # server on :4810, web dev server on :4811 (proxies /api)
npm test               # core unit tests + server invariant/integration suite
npm run build && npm start   # production: server serves built web app
```

Demo logins are printed by the seed script (password `pilot` for all).

## Principles the code must keep (from the PRD)

One record, many views (I-1) · no unanchored planned work (I-2) · typed holds (I-3) · derived + explainable
status (I-4) · condition-gated transitions (I-5) · Approval ≠ Check ≠ Decide (I-6) · append-only history
(I-7) · waivers are Decisions (I-8) · (P2: check/approve load capacity, I-9) · supersession never deletes
(I-10). The server invariant test suite names these directly.

## Status

Phase 1 (controlled tracker replacement) under construction in this workspace. Built directly from the
PRD (see ADR-001 for governance posture).
