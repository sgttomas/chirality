# PEC — status & handoff

The single "where are we, what's next" file. **If you're a new agent or contributor, read this first**,
then read deeper docs only as your task requires (read-order below). Keep this file current when you land
substantial work — durable state lives in repo files, not in chat history.

_Last updated: 2026-07-04 (after PR #39)._

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
5. **`docs/adr/ADR.md`** — the *why* behind implementer choices (ADR-001..011). ADR-011 explains the current status/issues split.
6. **`docs/SPEC.md`** — deep data-model / lifecycle / conditions / API detail; consult per subsystem.

Ground truth for behavior is the **tests** (`core/test/`, `server/test/`) and the pure derivations in `core/src/`.

## What's next (prioritized)

**A. Finish P1 coverage (small, incremental).** From `docs/TRACEABILITY.md` "Known P1 gaps" — implemented but not automatically tested: sponsor-brief render (PEC-OV-006), independence-warning path (PEC-CHK-004), risk/interface register CRUD (PEC-RISK/INT, PEC-PKG-007), the approvals/interfaces/intake/commitments exports (§15), the PH-A2 package-health rule, the log-change history entry (PEC-AHL-002), and the notification catalog + sweep idempotency (PEC-NOT-001). Also: no server `export/log.csv` (client-side only), and the 250k-history half of PEC-NFR-003 is reasoned but unmeasured.

**B. Pilot readiness (the real next step).** Import a real master deliverables list and RAIL via the §16 importers (`POST import/mdl|rail`), and run one coordinator through a real weekly triage. Rehearse backup/restore against the real pilot DB (`tools/backup.ts`; PEC-NFR-009 wants one tested restore). Let pilot feedback drive P2 scope — the PRD is explicitly pilot-driven.

**C. Open design threads from ADR-011 (decide before they harden).** Deliverable *status* is now workflow completeness, but **package/project health still derive from the issue-driven `deliverableStatus`** (PH-A1 counts amber/red deliverables; PJ-* rolls those up). That coexistence is intentional but is a seam: decide whether package/overview health should be reframed around package-level *issue* signals (hold age, overdue decisions, late interfaces, risks) rather than deliverable-RAG, for consistency with the issues-at-package model — and whether the Overview should adopt the issues framing.

**D. P2 — planning & capacity (the big next theme).** Plan module (Now/Next/Later, six-week lookahead), capacity by discipline where check/approval hours load capacity (I-9), the weekly commit that generates each person's My Week (replacing the P1 interim need-by + manual "commit to this week" flag), the dedicated interface register with aging, weekly package-review packs, supersession links, and role-digest notifications. Builds cleanly on the existing lifecycle/conditions/derivation machinery.

**E. P3 — governance (later).** Monthly reconciliation loop (decisions → DBM/SOW/data sheets), archive views, lessons-learned, authority matrix / approval-route templates, and supersession-impact propagation.

## Conventions

- **Git flow:** branch off `main`, open a PR, merge with a merge commit (matches repo history). The workspace is intentionally left committed-and-pushed after each unit of work; don't leave uncommitted work sitting (a worktree can be recreated at its last commit, losing uncommitted edits).
- **Runtime posture:** `core` and `server` have **zero runtime dependencies** (hand-rolled router over `node:http`, `node:sqlite`, `node:crypto`); only `web` has build-time deps. Keep it that way (ADR-002).
- **No memory system:** this project's memory is disabled by user directive; record durable state here and in the docs above.
- **Node ≥ 23.6** for native type-stripping (erasable-syntax-only TypeScript: no enums/namespaces/param-properties; `import type`; explicit `.ts` extensions).
