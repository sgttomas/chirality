# PEC — status & handoff

The single "where are we, what's next" file. **If you're a new agent or contributor, read this first**,
then read deeper docs only as your task requires (read-order below). Keep this file current when you land
substantial work — durable state lives in repo files, not in chat history.

_Implementation history last updated: 2026-07-04 (after the B/C/D pass:
pilot-readiness tooling, ADR-012, and the P2 build). Product direction authored
2026-07-09 in `docs/PRD.md` v1.0 and **adopted 2026-07-10** (`D-PEC-55`); the
v0.4 product framing is deprecated. The T0 rebaseline is the next owner gate._

> **Product-direction note:** the current application is a working prototype. The
> adopted PRD v1.0 defines the target as a team information hub centred on
> recurring discipline declarations, leadership decision support, and
> decision-consequence placement into relied-upon documentation. The implementation
> account below describes the prototype and is not a claim of v1.0 conformance.

## Current state

**P1 is built and adversarially hardened; P2 (planning & capacity) is built.** History:

| Unit | What |
|---|---|
| PR #35 | **P1 build** — six role homes, controlled records, condition-gated lifecycles, derived+explainable status, RBAC, CSV import/export, seed. |
| PR #36 | **Pilot-hardening** — fixed a cross-project history leak (PEC-NFR-007), non-idempotent decisions/risks/RAIL importers (§16), and an O(deliverables×work-items) view blow-up (PEC-NFR-003, ~13 s → ~0.6 s at 10k). |
| PR #39 | **Issues reorientation (ADR-011)** — deliverable status = *workflow completeness*; the Packages page is an *issues cockpit*. |
| PR #41 | **P1 coverage (item A)** — 32 tests over the previously untested surfaces; `export/log.csv`; risk 1–5 fix. |
| this branch | **Items B, C, D** — pilot-readiness tooling + tested restore (PEC-NFR-009); ADR-012 health-explanation carry-through; the **P2 build**: Plan module (Now/Next/Later, six-week lookahead), capacity by discipline with check/approval load (I-9, PEC-PLAN-003), weekly commit → My Week (PEC-PLAN-007), plan shifts with reasons + cross-package lead review (PEC-PLAN-005/006/008), schedule import (§16 P2), interface register aging (PEC-INT-002/PKG-008), weekly package review packs (PEC-PKG-009), role digests + notification severity (PEC-NOT-002/003), supersession links (PEC-AUTH-005). SPEC §14 + ADR-013 document the choices. |

**Health check (should be green):**
```bash
npm install        # node_modules is gitignored — reinstall after any fresh clone/worktree
npm run typecheck  # clean across core/server/web
npm test           # 161 pass (72 core + 89 server), 0 fail
npm run build      # web SPA builds
npm run drill      # pilot pipeline rehearsal on a scratch DB → PASS
npm run seed && npm run dev   # demo project AUR at http://localhost:4811 (all users password: pilot)
```

## Orient yourself (read-order)

1. **`README.md`** — layout + run commands.
2. **This file** — state + next work.
3. **`docs/PRD.md`** — the adopted target product definition (v1.0, `D-PEC-55`).
   `SPEC.md` and `TRACEABILITY.md` retain the historical v0.4 prototype basis until
   the T0 rebaseline.
4. **`docs/TRACEABILITY.md`** — requirement → code → test map, with a **"P2"** section and an honest **"Known P1 gaps"** section. This is the most useful map when picking up a specific requirement.
5. **`docs/adr/ADR.md`** — the *why* behind implementer choices (ADR-001..013). ADR-011/012 explain the status/issues split and why the health derivation stands; ADR-013 the P2 planning choices.
6. **`docs/SPEC.md`** — deep data-model / lifecycle / conditions / API detail; consult per subsystem.

Ground truth for behavior is the **tests** (`core/test/`, `server/test/`) and the pure derivations in `core/src/`.

## Governance & agent harness

PEC's project-local agent rules live in `AGENTS.md`. Human-gated PEC-local
coordination decisions are tracked at `execution/_Coordination/_DECISIONS/_REGISTER.md`.
Tier-0 domain-engine registration is staged under `_DomainEngines/pec/` with
profile `_DomainEngines/profiles/pec.yaml` (ADOPTED; owner Gate-2 ruling 2026-07-05); owner rulings live in
`_DomainEngines/_DECISIONS/_REGISTER.md`.

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

**D. P2 — planning & capacity — BUILT (2026-07-04).** Everything in the STATUS-D list shipped: Plan
module (PEC-PLAN-001..008 — Now/Next/Later, six-week lookahead sourced from plan + schedule import,
capacity by discipline where check/approval hours load capacity per I-9, plan shifts with recorded
reasons and cross-package lead review, weekly commit generating My Week with provenance), package
capacity block (PEC-PKG-003), interface aging → package health via PH-A4 (PEC-PKG-008) and the dedicated
register with aging + filters (PEC-INT-002), weekly package review pack (PEC-PKG-009,
`reports/package-pack/:id`), schedule import/export + lookahead export (§16/§15 P2), role digests +
threshold-driven notification severity (PEC-NOT-002/003), supersession links with affected-record sets
(PEC-AUTH-005), §8.3/§8.4 capacity rules (PH-R3/PH-A3, S-CAP) and the P2 plan-sourced forecast, plus the
schedule-pressure Overview view (PEC-OV-008). Where it lives: `core/src/plan.ts`, `server/src/services/plan.ts`,
`server/src/reports/package-pack.ts`, `web/src/pages/Plan.tsx`; SPEC §14; ADR-013; TRACEABILITY "P2" section
(19 new tests: `core/test/plan.test.ts`, `server/test/p2-plan.test.ts`). Deliberately NOT built (ADR-013):
PEC-AHL-008 duplicate suggestion (wants pilot vocabulary), PEC-NFR-006 SSO (wants an IdP), PEC-NFR-008
single-tenant deploy (deployment posture). The seed demos P2 (walk 4: planner@aurora.dev → Plan).

**E. Run the pilot (now the real next step).** The remaining work is human: provision the pilot project
(PILOT.md §1), shake down and import the real MDL/RAIL/decisions/risks (§0/§2 — `npm run drill
--mdl …`), rehearse one restore against the real DB (§5), then run the weekly cadence — coordinator
triage, package review with the pack, planner commit. Capture feedback as intake items in the pilot
project and fold themes back here; tune the P2 additions (capacity thresholds, digest content, lookahead
cells) on pilot evidence.

**F. P3 — governance (later).** Monthly reconciliation loop (decisions → DBM/SOW/data sheets), archive
views, lessons-learned, authority matrix / approval-route templates, and supersession-impact propagation
(the P2 `supersession_link` rows are its substrate). Also parked for pilot evidence: PEC-AHL-008,
SSO/PEC-NFR-006, PEC-CHK-004 hard block.

## Conventions

- **Git flow:** branch off `main`, open a PR, merge with a merge commit (matches repo history). The workspace is intentionally left committed-and-pushed after each unit of work; don't leave uncommitted work sitting (a worktree can be recreated at its last commit, losing uncommitted edits).
- **Runtime posture:** `core` and `server` have **zero runtime dependencies** (hand-rolled router over `node:http`, `node:sqlite`, `node:crypto`); only `web` has build-time deps. Keep it that way (ADR-002).
- **No memory system:** this project's memory is disabled by user directive; record durable state here and in the docs above.
- **Node ≥ 23.6** for native type-stripping (erasable-syntax-only TypeScript: no enums/namespaces/param-properties; `import type`; explicit `.ts` extensions).
