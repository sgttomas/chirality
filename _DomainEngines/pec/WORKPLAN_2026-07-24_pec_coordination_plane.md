> **Standing plan.** Activated 2026-07-24 under `D-PEC-58`; replaces
> `WORKPLAN_2026-07-09_pec_team_information_hub.md` (superseded, retained on
> disk with its supersession note). Per `LOOP_INIT.md`, the newest
> `WORKPLAN_*.md` in this directory governs.
> Consumer-interface posture amended 2026-07-27 under `D-PEC-68`, preserving
> the exact PEC-K-03/-11 rows adopted by `D-PEC-67`.

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

The quoted 2026-07-24 direction is retained as historical provenance.
`D-PEC-67` later replaced its harness-owned polling interpretation with exact
pull-oriented, consumer-owned-use and mode-capable, never-forced PRD rows.
`D-PEC-68` reconciles this standing plan to those later ruled rows.

Bounding every tranche: **graceful absence** — no governed act may require a PEC
read or write; **consumer-owned use** — PEC serves orientation on request,
never claims an external cadence, and injects nothing; an explicitly enabled
consumer owns whether and when to consume and whether to inject labeled PEC
data; **files govern** — the store is gitignored, rebuildable by one command,
and never citable as authority.

## Loop protocol

0. **Discover.** Resolve the repo root; inspect git, receipts, both decision
   registers, the profile, the candidate/adopted PRD, and live checks. Verify
   every inherited claim against the live tree.
1. **Review the product gate.** PRD v2.2 is the product definition of record
   after `D-PEC-68`; its exact PEC-K-03/-11 rows were adopted by `D-PEC-67`.
   No PRD adoption is an implementation or receiving-loop mandate.
2. **Use accepted decomposition truth.** `SOFTWARE_DECOMP` revision 1.3 is the
   accepted downstream basis after SCA-003. Post-acceptance product propagation uses
   SCOPE_CHANGE with its own owner gates; no implementation tranche is scoped
   from the PRD directly.
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

Phases map to PRD v2.2 §12.

| Order | Tranche | Completion test |
|---|---|---|
| P0 | Governance | `D-PEC-58`, `D-PEC-61`, `D-PEC-67`, and `D-PEC-68` ruled; this plan remains live at `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` |
| D1 | Decomposition (`SOFTWARE_DECOMP` over PRD v2) | Gate 7 accepted; revision 1.3 is the authoritative downstream basis after SCA-003 until a separately accepted successor |
| P1 | One-loop reconciler + orientation store + read-only API | Parity diff vs practitioner harness clean or explained; rebuild-from-scratch within bound; kill test passes |
| P2 | Dashboards across all registered loops | Under selected PRD v2.2 P2-B, owner use or non-use is recorded as uptake/falsification evidence; manual Step 0 remains available and no consumer is bound |
| P3 | PEC-side opt-in integration interfaces/adapters usable by hooks CLI or daemon consumers, presence registry, Git/worktree scanner | Capability tests pass; consumer enablement/use measured without external conformance; overlap warnings fire on seeded conflicts; falsification clause armed |
| P4 | PEC-side streams: daemon SSE bridge, optional hook-push interface, live hierarchy, optional cmux adapter; live use remains receiving-owner authorized | Stream loss demonstrably recovered by reconciliation; presence TTLs honest under kill/crash tests |

The first loop the P1 reconciler ingests is PEC v2's own build.

## Parked work and owner gates

- Runtime/source implementation remains parked until an exact per-tranche
  packet opens the applicable PEC and Root fences; PRD adoption alone opens
  none.
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

- Product definition: `projects/pec/docs/PRD.md` (v2.2; v2.0 adopted by
  `D-PEC-58`, directed-bootstrap v2.1 by `D-PEC-61`, exact consumer rows by
  `D-PEC-67`, surrounding concordance by `D-PEC-68`); original authoring
  record at
  `projects/pec/execution/_Coordination/PRD_V2_CANDIDATE_2026-07-24_coordination_plane.md`
- Direction/fence packet: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57_coordination_plane_pivot.md`
- Decision registers: `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
  and `_DomainEngines/_DECISIONS/_REGISTER.md`
- Profile: `_DomainEngines/profiles/pec.yaml`
- Project agent posture: `projects/pec/AGENTS.md`
- Accepted decomposition pointer: `projects/pec/execution/_Decomposition/_LATEST.md` (revision 1.3)
- Accepted scope-change pointer: `projects/pec/execution/_ScopeChange/_LATEST.md` (SCA-003)
- Loop handoff: `_DomainEngines/pec/LOOP_RECEIPTS.md`
- Frozen reference corpus: `projects/pec/{core,server,web,agent-sidecar,tools}`
- Build pipeline: `docs/DECOMPOSITION_STANDARD.md` and
  `agents/AGENT_SOFTWARE_DECOMP.md`
- Permanent parity peer: `tools/practitioner_harness/README.md`
