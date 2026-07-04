# PEC — status & handoff

The single "where are we, what's next" file. **If you're a new agent or contributor, read this first**,
then read deeper docs only as your task requires (read-order below). Keep this file current when you land
substantial work — durable state lives in repo files, not in chat history.

_Last updated: 2026-07-04 (after the P1-coverage pass; PRs #35/#36/#39 merged, coverage PR open)._

## Current state

Phase-1 (P1) is built, adversarially hardened, and on `main`, plus a model reorientation. Three merged PRs:

| PR | What |
|---|---|
| #35 | **P1 build** — six role homes, controlled records, condition-gated lifecycles, derived+explainable status, RBAC, CSV import/export, seed. |
| #36 | **Pilot-hardening** — fixed a cross-project history leak (PEC-NFR-007), non-idempotent decisions/risks/RAIL importers (§16), and an O(deliverables×work-items) view blow-up (PEC-NFR-003, ~13 s → ~0.6 s at 10k). |
| #39 | **Issues reorientation (ADR-011)** — a deliverable's status is now *workflow completeness* (gates closed: drafted→checked→approved→issued), decoupled from issues; the Packages page is an *issues cockpit* (holds, interfaces, decisions, risks, rolled-up action items). Issues appear on a deliverable only on drill-down. |

**Health check (should be green):**
```bash
npm install        # node_modules is gitignored — reinstall after any fresh clone/worktree
npm run typecheck  # clean across core/server/web
npm test           # 95 pass (53 core + 42 server), 0 fail
npm run build      # web SPA builds
npm run seed && npm run dev   # demo project AUR at http://localhost:4811 (all users password: pilot)
```

## Orient yourself (read-order)

1. **`README.md`** — layout + run commands.
2. **This file** — state + next work.
3. **`docs/PRD.md`** — the basis document (v0.4). Requirements are IDs like `PEC-DEL-001`; phases P1/P2/P3.
4. **`docs/TRACEABILITY.md`** — requirement → code → test map, with an honest **"Known P1 gaps"** section. This is the most useful map when picking up a specific requirement.
5. **`docs/adr/ADR.md`** — the *why* behind implementer choices (ADR-001..012). ADR-011/012 explain the current status/issues split and why the health derivation stands.
6. **`docs/SPEC.md`** — deep data-model / lifecycle / conditions / API detail; consult per subsystem.

Ground truth for behavior is the **tests** (`core/test/`, `server/test/`) and the pure derivations in `core/src/`.

## What's next (prioritized)

**A. Finish P1 coverage — DONE (2026-07-04).** The previously untested surfaces now have automated tests (`server/test/coverage-*.test.ts`, `core/test/coverage-ph-a2.test.ts`; 32 tests): sponsor-brief render (PEC-OV-006), independence warning (PEC-CHK-004), risk/interface registers (PEC-RISK/INT, PEC-PKG-007), the §15 exports, the PH-A2 rule, the log-change history entry (PEC-AHL-002), notification producers + sweep idempotency (PEC-NOT-001), and PEC-NFR-003 at 250k history rows. Also implemented `export/log.csv` and fixed a real defect (risk API now enforces the 1–5 probability/impact range). Suite is now 127 tests. See `docs/TRACEABILITY.md` "Known P1 gaps" for the few remaining thin spots (checklist/condition-template CRUD is seed/DB-only by design).

**B. Pilot readiness — tooling DONE (2026-07-04); the human rehearsal remains.** The tested restore
(PEC-NFR-009) is now automated (`server/test/coverage-backup-restore.test.ts`: round-trip, corrupt-backup
refusal, retention pruning), and `npm run drill` (`tools/pilot-drill.ts`) rehearses the whole pilot
pipeline against a scratch DB — §16 imports in order with row-level reject reporting, MDL re-import
idempotency, coordinator triage over unanchored intake, derived-view budget, backup → mutate → restore.
Point it at the real spreadsheets with `--mdl/--rail/--decisions/--risks` to shake them down. The runbook
is `docs/PILOT.md` (provisioning, import order, weekly triage script, backup cron, restore procedure).
Still for the pilot team, and inherently manual: import the *real* MDL/RAIL, run one coordinator through
a *real* weekly triage, one restore rehearsal against the real pilot DB (PILOT.md §5), and let pilot
feedback drive P2 scope — the PRD is explicitly pilot-driven.

**C. ADR-011 open thread — DECIDED and closed (2026-07-04, ADR-012).** The §8.3/§8.4 derivation stands
rule-for-rule (PH-A1 is a PRD default; no pre-pilot deviation from the basis document — the full
rationale is ADR-012). What was broken was presentation: PH-R1/PH-A1 drill-downs dead-ended at the
now-invisible per-deliverable RAG label. Fixed: their explanations state the pressure in plain terms and
carry the underlying issue records (holds, overdue items, conditions, comments) into `contributing`, so
drill-down always lands on a cockpit-visible record; and the Overview package rollup now shows the same
log-scoped `openIssues` count as the Packages register/cockpit (PEC-NFR-005 preserved). Tests:
`core/test/status.test.ts` (2 ADR-012 tests), `server/test/coverage-adr-012.test.ts`. Revisit the
derivation only on pilot evidence.

**D. P2 — planning & capacity (the big next theme).** Plan module (Now/Next/Later, six-week lookahead), capacity by discipline where check/approval hours load capacity (I-9), the weekly commit that generates each person's My Week (replacing the P1 interim need-by + manual "commit to this week" flag), the dedicated interface register with aging, weekly package-review packs, supersession links, and role-digest notifications. Builds cleanly on the existing lifecycle/conditions/derivation machinery.

**E. P3 — governance (later).** Monthly reconciliation loop (decisions → DBM/SOW/data sheets), archive views, lessons-learned, authority matrix / approval-route templates, and supersession-impact propagation.

## Conventions

- **Git flow:** branch off `main`, open a PR, merge with a merge commit (matches repo history). The workspace is intentionally left committed-and-pushed after each unit of work; don't leave uncommitted work sitting (a worktree can be recreated at its last commit, losing uncommitted edits).
- **Runtime posture:** `core` and `server` have **zero runtime dependencies** (hand-rolled router over `node:http`, `node:sqlite`, `node:crypto`); only `web` has build-time deps. Keep it that way (ADR-002).
- **No memory system:** this project's memory is disabled by user directive; record durable state here and in the docs above.
- **Node ≥ 23.6** for native type-stripping (erasable-syntax-only TypeScript: no enums/namespaces/param-properties; `import type`; explicit `.ts` extensions).
