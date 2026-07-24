> **Standing plan.** Activated 2026-07-24 under `D-PEC-58`; replaces
> `WORKPLAN_2026-07-09_pec_team_information_hub.md` (superseded, retained on
> disk with its supersession note). Per `LOOP_INIT.md`, the newest
> `WORKPLAN_*.md` in this directory governs.

# PEC Work Loop — coordination-plane standing plan

> **Epistemic status: owner-directed standing plan.** Drafted 2026-07-24 from
> the owner direction ruled in `D-PEC-57` (O-A). On adoption it replaces the
> 2026-07-09 team-information-hub plan as the ordering map for PEC work.
> Accepted decisions and the live tree remain authoritative; this file is not a
> status ledger or an adoption act.

## Owner intent

PEC is to become the **coordination plane** of Chirality: deterministic tooling
over governed file truth, embodying **Step 0 (Discover)** and the deterministic
parts of **Step 1 (gate review and decision-slate presentation)** of the
canonical development loop. Owner direction of record (`D-PEC-57`):

> PEC should morph into the core agentic workflow coordination substrate for
> Chirality — deterministic tooling, data arriving from workflow/agent events,
> the existing pages repurposed as dashboards/analytics. As a human-used
> project-management tool it has no interest. It should embody Step 0 and the
> deterministic parts of Step 1 of the canonical loop; polling is determined by
> the harness, not agent behaviour; ruling capture remains file-native; it does
> not subsume the practitioner harness; it is "the coordination plane that
> doesn't need to exist." Old PEC is superseded wholesale; v2 is a greenfield
> build through the governed pipeline with old PEC as a cited reference corpus.

Bounding every tranche: **graceful absence** — no governed act may require a PEC
read or write; **harness-owned polling** — harnesses poll at moments of
consequence and inject labeled non-authoritative data; **files govern** — the
store is gitignored, rebuildable by one command, and never citable as authority.

## Loop protocol

0. **Discover.** Resolve the repo root; inspect git, receipts, both decision
   registers, the profile, the candidate/adopted PRD, and live checks. Verify
   every inherited claim against the live tree.
1. **Review the product gate.** The product gate — `D-PEC-58` adoption of
   PRD v2 — was satisfied 2026-07-24 (gate-state note). The open owner gates
   are decomposition acceptance (SOFTWARE_DECOMP Gates 1–7), then one packet
   per implementation tranche.
2. **Decompose before building.** After adoption, run PRD v2 through
   `SOFTWARE_DECOMP` (Gates 1–7 per `docs/DECOMPOSITION_STANDARD.md`,
   human-interactive). Gate 7 acceptance is the downstream basis; no tranche is
   scoped from the PRD directly.
3. **Fence source work.** Each implementation tranche requires an owner-ruled
   D-PEC packet naming exact paths, acts, verification, rollback, and any data
   or authority implications. New source trees are named in their own packet.
4. **Preserve human gates.** Adoption, ruling, and direction remain human acts
   (K-AUTH-1). PEC provides no write path that records them; its own gate
   verdicts are advisory and Explain-shaped, never dispositive.
5. **Execute branch-first.** Isolated branches, disjoint write scopes. Never
   treat PEC output, or old-PEC demo state, as production truth.
6. **Check and close.** Run work-type checks including the standing kill test
   and the practitioner-harness parity diff, record a minimal receipt, and
   surface unresolved product decisions rather than inventing them.

## Target sequence after PRD v2 adoption

Phases map to PRD v2 §12.

| Order | Tranche | Completion test |
|---|---|---|
| P0 | Governance | `D-PEC-58` ruled and this plan live at `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` — satisfied 2026-07-24 (gate-state note) |
| D1 | Decomposition (`SOFTWARE_DECOMP` over PRD v2) | Gate 7 accepted; the decomposition is the authoritative downstream basis for all build tranches |
| P1 | One-loop reconciler + orientation store + read-only API | Parity diff vs practitioner harness clean or explained; rebuild-from-scratch within bound; kill test passes |
| P2 | Dashboards across all registered loops | Owner uses PEC in place of manual Step 0 for orientation reads |
| P3 | Harness integration: hooks CLI + daemon polling, presence registry, Git/worktree scanner | Poll adoption measured; overlap warnings fire on seeded conflicts; falsification clause armed |
| P4 | Streams: daemon SSE bridge, hooks push, live hierarchy, optional cmux adapter | Stream loss demonstrably recovered by reconciliation; presence TTLs honest under kill/crash tests |

The first loop the P1 reconciler ingests is PEC v2's own build.

## Parked work and owner gates

- Runtime implementation is parked until `D-PEC-58` is ruled.
- The open product decisions in PRD v2 §16 must not be guessed where they
  materially affect architecture — register structuring at source, the daemon
  global event feed, the loop-registry home, long-term placement, UI packaging,
  auth reuse, and the name. None blocks P0–P2.
- **`F-PEC-1..4` remain in force** as ruled in `D-T0-15` (F-PEC-4 as extended
  by `D-T0-19`); they are amended only by an explicit per-tranche packet clause.
- Implementation writes to `core/`, `server/`, `web/`, or any new source tree
  require their own packets; F-PEC-1 is the outer fence until one opens it.
- Old-PEC source trees (`projects/pec/{core,server,web,agent-sidecar,tools}`)
  are **frozen reference corpus**: read and cite only, never edited, never
  deleted (archival from the working tree once P2 is useful is its own packet).
  Machinery carries as pattern, not as code (PRD v2 §7.3, §13).
- `D-T0` data-residency rows are unchanged; PEC v2 is content-minimal (paths,
  counts, SHAs, states, hashes — never file or diff content).
- No second execution loop: the runtime daemon keeps session, delegation, and
  turn-lock ownership (`D-GOV-20`, `D-PEC-56`). PEC dispatches nothing.
- Rulings stay file-native (K-AUTH-1); PEC renders decision slates authored
  elsewhere and provides no ruling write path.
- **Named open follow-on:** supersession of the `pec.yaml` profile (the L3
  operation-proposal lane sunsets with the old product); the profile is
  superseded when v2 has shape, and the `_DomainEngines/pec` loop continues as
  the governing development loop meanwhile.

## Live pointers

- Product definition: `projects/pec/docs/PRD.md` (v2.0, adopted 2026-07-24,
  `D-PEC-58`); authoring record at
  `projects/pec/execution/_Coordination/PRD_V2_CANDIDATE_2026-07-24_coordination_plane.md`
- Direction/fence packet: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57_coordination_plane_pivot.md`
- Decision registers: `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
  and `_DomainEngines/_DECISIONS/_REGISTER.md`
- Profile: `_DomainEngines/profiles/pec.yaml`
- Project agent posture: `projects/pec/AGENTS.md`
- Loop handoff: `_DomainEngines/pec/LOOP_RECEIPTS.md`
- Frozen reference corpus: `projects/pec/{core,server,web,agent-sidecar,tools}`
- Build pipeline: `docs/DECOMPOSITION_STANDARD.md` and
  `agents/AGENT_SOFTWARE_DECOMP.md`
- Permanent parity peer: `tools/practitioner_harness/README.md`
