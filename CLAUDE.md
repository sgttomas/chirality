# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Chirality is a filesystem-native agent operating system for deliverable-heavy professional work. The repo contains the private canonical source tree: instruction architecture, agent contracts, skills, deterministic tools, domain workspaces, and the tooling to produce the sanitized public `chirality-app` package.

The core design principle: the filesystem is the database. Authoritative project state lives in git-tracked plain files. Agents propose; humans decide. No agent may certify, approve, sign, or issue work for reliance.

## Reading Order for Orientation

Start with these in order:

1. `INIT.md` — bootstrap and document map
2. `AGENTS.md` — agent index, matrix, and governance integration rules
3. `docs/DIRECTIVE.md` — founding philosophy
4. `docs/SPEC.md` — physical structures, file formats, folder layouts
5. `docs/TYPES.md` — stable IDs, enums, lifecycle states
6. `docs/CONTRACT.md` — 21 K-* binding invariants
7. `skills/README.md` — skill system contract
8. `tools/REGISTRY.md` — deterministic tool index

## Key Architecture Concepts

**Agent types:** Type 0 = canonical standards, Type 1 = interactive personas (open in WORKBENCH), Type 2 = bounded task shells (open in PIPELINE). `TASK` is the canonical Type 2 execution shell; it hydrates skills via `TaskSkill: <name>`.

**Skills vs agents:** Skills are method packs for recurring task shapes. Use a skill when role, write scope, and interaction model are the same but the method changes. Do not create a new agent for that. Skills live under `skills/<name>/` with four required files: `SKILL.md`, `BRIEF_SCHEMA.md`, `TOOL_POLICY.md`, `QA_CHECKS.md`.

**Derivative-package rule:** Any package assembled from accepted upstream truth (aggregations, audit snapshots, concordance packages) is a derivative package. It must cite its upstream snapshot and must never substitute for decomposition truth.

**Snapshot rule:** Every phase-boundary decision must produce an immutable snapshot. Later phases consume accepted snapshots, never mutable working state.

**Write scope:** Agents have explicit, bounded write scopes. Skills must never widen scope beyond what the agent shell and brief allow.

**Epistemic labels:** Claims carry `FACT`, `ASSUMPTION`, `PROPOSAL`, or `TBD` labels. `TBD` markers are surfaced, not silently resolved.

## Surfaces and Their Roots

| Surface | Root(s) | Notes |
|---|---|---|
| Agent instructions | `AGENTS.md`, `agents/AGENT_*.md` | Change via live registry, not narrative |
| Skills | `skills/` | Each immediate subfolder containing `SKILL.md` is one skill; treat the live folder as the index |
| Tools | `tools/` | Registry at `tools/REGISTRY.md`; subfolders group by function (scaffolding, validation, pdf2md, aggregation, etc.) |
| Frontend harness snapshot | `frontend/` | Public-export snapshot only; dev work goes in `projects/chirality-app-dev/` |
| Domain workspaces | `domains/` | Private; large corpora excluded from git |
| Project workspaces | `projects/` | Private; not exported |
| Public export profile | `exports/chirality-app/` | Controls what goes into the public package |
| Plans / archives | `plans/`, `.archive/` | Non-governing; historical context |

## Validation and Testing Commands

```sh
# After skill changes
python3 tools/validation/validate_skill_metadata.py skills

# Discover test surfaces (tools, frontend, OpenPipeStress)
python3 tools/validation/discover_test_surfaces.py . --text

# Run Python tests across root tools
python3 -m pytest -q tools

# Run Chirality App dev frontend tests
cd projects/chirality-app-dev/frontend && npm test

# Run OpenPipeStress Python tests
cd projects/chirality-piping && python3 -m pytest -q tests

# Run OpenPipeStress desktop tests (Vitest)
cd projects/chirality-piping && npm test --workspace apps/desktop

# Run OpenPipeStress Rust tests (per-crate)
cargo test --manifest-path <crate>/Cargo.toml

# Build and check the public export (run before publishing or after changing exported files)
python3 exports/chirality-app/export_public.py

# Apply the public export to a local checkout
python3 exports/chirality-app/export_public.py --apply-target /path/to/chirality-app
```

## Frontend Development

```sh
cd frontend
npm install
npm run dev              # Next.js dev server
npm run build            # Production build
npm run lint             # ESLint
npm run desktop:dev      # Run Electron desktop app (dev mode)
npm run desktop:pack     # Package Electron app (no publish)
npm run desktop:dist     # Build distributable (signed)
npm run desktop:dist:unsigned   # Build distributable (unsigned, for local testing)
```

Requires `ANTHROPIC_API_KEY` in the shell running the dev server.

Harness validation (pre-merge) — server must be running first:
```sh
# Shell 1
cd frontend && npm run dev -- --hostname 127.0.0.1 --port 3000

# Shell 2
cd frontend
npm run harness:validate:toolkit
npm run harness:validate:premerge
```

Summary artifact: `frontend/artifacts/harness/section8/latest/summary.json`. Diagnostics log to `.chirality/logs/harness.log` in the project root.

The Electron app bundles `agents/`, `skills/`, `tools/`, `docs/`, and `init/` as `extraResources` under `instruction-root/` at package time.

## Change Workflow

- **Agent/routing changes** → `AGENTS.md` and `agents/`
- **Skill changes** → `skills/` then run `validate_skill_metadata.py`
- **Tool changes** → `tools/` and update `tools/REGISTRY.md` when it changes the curated tool contract
- **Governance changes** → root `docs/`, not project-local docs
- **App/frontend development** → `projects/chirality-app-dev/`, promote only reviewed material to root/export surfaces
- **Public export** → regenerate manifest after changing any exported file

When live folders, indexes, and narrative documents disagree, treat the live registry/discovery surface as authoritative and surface the discrepancy rather than silently preserving stale prose.

## Governing Invariants (Selected)

The full set of 21 K-* invariants is in `docs/CONTRACT.md`. The most commonly relevant:

- **K-AUTH-1:** Only humans author binding approval records.
- **K-WRITE-1 / K-SNAP-1:** Agents write within explicit scope; every phase-boundary decision produces an immutable snapshot.
- **K-PROV-1:** All governed claims require mandatory provenance. Unsourced assertions are marked `TBD` or `ASSUMPTION`, not silently asserted as fact.
- **K-STATUS-1:** `_STATUS.md` is the canonical lifecycle state file for each deliverable. No other file determines deliverable state.
- **K-HIER-1:** Projects decompose as packages containing deliverables (flat; no nesting; no phases layer).
