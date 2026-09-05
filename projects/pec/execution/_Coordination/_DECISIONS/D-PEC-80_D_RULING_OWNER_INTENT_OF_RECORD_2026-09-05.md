# D-PEC-80 D — Owner intent of record after workplan retirement

Status: RULED — owner merge direction 2026-09-05; effective on merge

Ruling: `D-PEC-80_RULING_2026-09-05.md`; the owner directed “merge PR #721”.
This disposition supersedes the preparation-time conditional language below.

Owner: Ryan Tufts

Date: 2026-09-05

Prepared by Codex acting as HELP_HUMAN; role not mechanically enforced.
The supplementary direction is preserved verbatim in the parent packet's
D_RETIREMENT/OWNER_DIRECTION.md. D-APP-114/115 on origin/main supply the form,
not PEC authority. This is item D of D-PEC-80, on the same register row and PR.

## Owner intent of record

Carried verbatim from the complete Owner intent section of
`projects/pec/plans/workplans/WORKPLAN_2026-07-24_pec_coordination_plane.md`,
SHA-256 `70f697f78141f6791c310629ad973309b6560b2f551a5ebfb1dabc66a12b2448`.
The source's qualifiers are carried too, so its earlier polling interpretation
is not revived. On acceptance this is the loop's standing purpose: orientation,
not a grant or selection surface. Exact owner rulings govern on disagreement.

<!-- BEGIN VERBATIM OWNER INTENT SECTION -->
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

<!-- END VERBATIM OWNER INTENT SECTION -->

## Parked lanes — dated history only

The following is the plan's parked list as archived on 2026-09-05, including
its dated 2026-08-03 direction and subsequent historical amendments. It is
quoted as history only; several claims were superseded before retirement.

> - Runtime/source implementation remains parked until an exact per-tranche
>   packet opens the applicable PEC and Root fences; PRD adoption alone opens
>   none.
> - The open product decisions in PRD v2 §16 must not be guessed where they
>   materially affect architecture — register structuring at source, the daemon
>   global event feed, long-term placement, UI packaging, auth reuse, and the
>   name. The loop-registry home and shape is no longer open: D-PEC-78 O-A
>   selected the existing PEC-owned strict-version-1 JSON/schema paths and
>   core-owned typed port. The remaining open decisions do not block P0–P2.
> - **`F-PEC-1..4` remain in force** as ruled in `D-T0-15` (F-PEC-4 as extended
>   by `D-T0-19`); they are amended only by an explicit per-tranche packet clause.
> - Implementation writes to `core/`, `server/`, `web/`, or any new source tree
>   require their own packets; F-PEC-1 is the outer fence until one opens it.
> - Old-PEC source trees (`projects/pec/{core,server,web,agent-sidecar,tools}`)
>   are **frozen reference corpus**: read and cite only, never edited, never
>   deleted (archival from the working tree once P2 is useful is its own packet).
>   Machinery carries as pattern, not as code (PRD v2 §7.3, §13).
> - `D-T0` data-residency rows are unchanged; PEC v2 is content-minimal (paths,
>   counts, SHAs, states, hashes — never file or diff content).
> - No second execution loop: the runtime daemon keeps session, delegation, and
>   turn-lock ownership (`D-GOV-20`, `D-PEC-56`). PEC dispatches nothing.
> - Rulings stay file-native (K-AUTH-1); PEC renders decision slates authored
>   elsewhere and provides no ruling write path.
> - Superseding owner direction of 2026-08-03 sends TM-PEC-023 to a dedicated
>   SCOPE_CHANGE mapping session. Neither mappings nor blanks are ruled; the nine
>   values and COV-062..COV-070 remain open, with no downstream gate or urgency.
>   RF-002 `REVISE` is resolved by exact successor SOW acceptance at
>   `REV_DEL-01-06_2026-08-04_1113`; RF-001 remains resolved and Gate 5 remains
>   HOLD at `INITIALIZED`. Metadata alignment is cleared. Derivative state
>   remains `INCOMPLETE` for exactly two categories: TM-PEC-023 amendment and
>   the SCA-004 / TM-PEC-013/014 DEL-02-07, DEL-03-01, DEL-04-01, and DEL-00-03
>   ordinary SOW/SPEC currency lane. TM-PEC-011 remains `OPEN`/stale pending a
>   separate TASK_MANAGEMENT disposition; no Task Management row closes here.
> - **Named open follow-on:** supersession of the `pec.yaml` profile (the L3
>   operation-proposal lane sunsets with the old product); the profile is
>   superseded when v2 has shape, and the `_DomainEngines/pec` loop continues as
>   the governing development loop meanwhile.

Live parked state is re-derived from the items' own `(gated: ...)`,
`(stage-gated: ...)`, and `NOT_SELECTABLE_UNTIL:` markers and the register,
with the exact later owner records behind those pointers. This quotation is
never a selection or blocking surface.

## Constraint preservation

All paths below are repository-relative. These are source locators and dated
dispositions, not a new status ledger. Re-derive current state at use.

| Plan constraint or temporary claim | Surviving home / disposition |
|---|---|
| Per-tranche source and Root grants; F-PEC-1..4 | projects/pec/AGENTS.md Write Scopes And Fences and loop/LOOP_INIT.md §3 carry exact fences; D-T0-15/19 and D-PEC-57/58 remain source records |
| Old source frozen until separately gated archival | projects/pec/AGENTS.md Frozen Reference Corpus; D-PEC-58; init §3 unchanged |
| Open architectural decisions must not be guessed; no blanket P0–P2 block | projects/pec/docs/PRD.md §16 and exact decision records; D-PEC-78 resolves registry shape/home; adopted-not-applied D-PEC-79 correction is recorded by Receipt 165/166 |
| Accepted revision 1.4 until accepted successor | projects/pec/execution/_Decomposition/_LATEST.md and accepted scope-change pointer; source pins remain exact |
| TM-PEC-023 dedicated owner mapping; no downstream gate/urgency | Receipt 165/166 and projects/pec/execution/_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md; Task Management register/handoff carry concern; no gate added to unrelated deliverables |
| RF-001/002, Gate 5 HOLD at INITIALIZED, metadata/ordinary currency claims | DEL-01-06 own _STATUS.md, exact REV_DEL-01-06_2026-08-04_1113 record, and Receipt 165/166 plus the currency closeout handoff; stale two-category incompleteness is not revived |
| TM-PEC-011 separate disposition/archive | Receipt 165/166 and Task Management register: disposition landed; later ordinary archive remains its own act |
| Profile supersession when v2 has shape | D-T0-27 effective adoption; Receipt 165/166; archived PLAN_CURRENCY_NOTE_2026-08-09_D-T0-27.md; follow-on already complete, not a new hold |
| Data residency, no second loop, file-native rulings | projects/pec/AGENTS.md Data And Residency / Shared Runtime Boundary / Product Posture; exact init fences unchanged |
| Graceful absence, consumer-owned use, files govern | projects/pec/AGENTS.md Product Posture and exact D-PEC-67/68 records |
| First P1 ingestion is PEC's own build; release kill/parity gates | projects/pec/docs/PRD.md §12 and loop/LOOP_INIT.md §8; target sequence is historical, never a work selector |

Temporary constraints without a surviving home requiring a separate owner
choice: **none identified**. D's retirement/intent preservation itself still
awaits the owner's ruling. No constraint is silently waived.

## Remaining-marker audit

All 64 deliverable _STATUS.md files were inspected; none has a `## Remaining`
section or a Remaining item. Thus there is no plan-only Remaining gate to
transfer and no item is made selectable by retirement. Marker edits: **none**;
item list: **empty**. The init requires explicit owner-directed preparation
for missing scope; no scope or lifecycle is changed here.

## Effect and limits on ruling

On the owner's acceptance of D, the intent is retained here and every plan
is history only. This record creates no plan, queue, or status surface and
selects no item. It changes no fence, product, lifecycle, release, or reliance
state. The quoted parked list never overrides a live item's own gate.
