# PEC — 9-Domains: Project Execution Control

Web-based, multi-user system of record for multidisciplinary engineering execution control: role homes,
controlled records, condition-gated transitions, and derived (always explainable) status. Implements
`docs/PRD.md` (v0.4), Phase 1 scope.

**New here? Start with [`docs/STATUS.md`](docs/STATUS.md)** — current state, what's next, and the read-order for the rest of the docs.

## Layout

| Path | Contents |
|---|---|
| `docs/STATUS.md` | **Status & handoff** — where the project is, what remains; read this first |
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

Run these from `projects/pec/`. The seed guard requires `PEC_DB` to point at a **scratch/demo**
database — a path containing a `scratch` or `demo` token, or one under the system temp dir. Use an
**absolute** path: `npm run seed` and `npm run dev` execute from different workspace directories, so a
relative `./pec-demo.db` resolves to two different files — the server would read an empty one it
auto-creates and every login would fail.

```bash
npm install                        # workspace deps (web toolchain; core/server have none at runtime)
export PEC_DB="$PWD/pec-demo.db"   # absolute path; must contain "scratch"/"demo" (seed guard)
npm run seed                       # create $PEC_DB with the demo FEED project + users
npm run dev                        # server on :4810, web dev server on :4811 (proxies /api)
npm test                           # core unit tests + server invariant/integration suite (own temp DBs)
npm run build && npm start         # production: server serves built web app (also reads $PEC_DB)
```

Demo logins are printed by the seed script (all share password `pilot`) — e.g. `pm@aurora.dev`.

### Rebuild the sponsor demo from dated inputs

`rebuild:demo` creates a fresh TWD-only database from date-prefixed `.xlsx`
files in `pilot-scratch/input`. It uses the same workbook mapper and governed
proposal → accept → apply services as the UI, retains the full workbook capture,
and makes a WAL-safe backup before replacing an existing demo database. Coverage
is mandatory and never inferred.

```bash
export PEC_DB="$PWD/pec-demo.db"
export PEC_DEMO_COVERAGE_START=YYYY-MM-DD   # PE-declared
export PEC_DEMO_COVERAGE_END=YYYY-MM-DD     # PE-declared
npm run rebuild:demo
```

The rebuild fails loudly if a dated input has rejected rows or identity
conflicts; resolve the source/mapping decision rather than silently dropping or
inventing project records. Operational demo personas use password `pilot`.

## Principles the code must keep (from the PRD)

One record, many views (I-1) · no unanchored planned work (I-2) · typed holds (I-3) · derived + explainable
status (I-4) · condition-gated transitions (I-5) · Approval ≠ Check ≠ Decide (I-6) · append-only history
(I-7) · waivers are Decisions (I-8) · (P2: check/approve load capacity, I-9) · supersession never deletes
(I-10). The server invariant test suite names these directly.

## Status

Phase 1 (controlled tracker replacement) under construction in this workspace. Built directly from the
PRD (see ADR-001 for governance posture).
