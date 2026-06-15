# PLAN — Active Roadmap

> **Status: DRAFT skeleton pending human authoring.** This re-establishes the monorepo-root `docs/PLAN.md` (root `docs/` was hollowed out during the four-repo merge; see `plans/monorepo_root_governance_and_path_anchoring_2026-06-15.md`). The structure follows the prior root canon (`.archive/PLAN.md`); §1 carries only the established architectural direction. **Roadmap themes and detail (§2–§4) are maintainer-owned and intentionally left for you to populate** — agents must not invent roadmap content (K-INVENT-1).

## Control-Plane Boundary

This document is the active **framework roadmap**. It is strategic and non-governing: `DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, and `TYPES.md` govern; this file records direction and intended work, not binding requirements. Tactical sequencing, blocker policy, and completed-work detail live in issue/branch/release records — not here. Working roots (`projects/*`, `domains/*`) maintain their own `docs/PLAN.md` for project-level roadmaps; this file does not supersede them.

---

## 1. Current Architectural Direction

The established direction (reflected in `AGENTS.md` and the agent suite):

- **`TASK` is the canonical Type 2 execution shell.** It hydrates reusable methods via `TaskSkill: <name>`. A new bespoke task agent is not added when role, write scope, and interaction surface are unchanged and only the method differs — that is a skill.
- **Method logic lives in `skills/`; deterministic operations live in `tools/`; Type 1 personas handle human-facing orchestration.** `ORCHESTRATOR` is the grandfathered orchestration persona.
- **Governance is two-layered.** The framework root (`AGENTS.md`, root `docs/`, `agents/`, `skills/`, `tools/`) defines Chirality-wide rules; working roots specialize them without weakening framework invariants (`CONTRACT.md` K-AGENTS-1).
- **One shared instruction root serves many working roots** under `projects/*` and `domains/*`; path anchoring and task write-scope containment make per-working-root and git-worktree isolation safe (`SPEC.md` §0.2; `CONTRACT.md` K-WRITE-2).

Details of in-flight work live in issue/branch/release records, not in this planning surface.

---

## 2. Active Roadmap Themes

> _Maintainer-owned — populate. Suggested shape: a `Theme | Status` table plus an "unsplit backlog" list of items not yet promoted into a theme._

| Theme | Status |
|---|---|
| _(to be filled)_ | |

---

## 3. Roadmap Detail

> _Maintainer-owned — group by area. The first item below is seeded because it is active, grounded work (this session's plan); the rest are for you to add._

### Architecture and Governance

- **Root governance restoration + path anchoring.** Ratify the root `docs/` governance set (DIRECTIVE/SPEC/TYPES/CONTRACT/PLAN); wire the `K-WRITE-2` ScopePath-containment rule (`SCOPE_OUTSIDE_WORKTREE`) into `AGENT_TASK.md`; derive `REPO_ROOT` in `init/init-prompt.md` and de-absolutize coordination/handoff files. Basis: `plans/monorepo_root_governance_and_path_anchoring_2026-06-15.md`.

### Workflow Normalization

- _(to be filled)_

---

## 4. Known Risks

> _Optional, maintainer-owned — populate with current top risks and mitigations._

---

## 5. Historical Record

Completed roadmap slices are historical and are not tracked as active surface here; they live in git history, release records, and per-project completion logs.
