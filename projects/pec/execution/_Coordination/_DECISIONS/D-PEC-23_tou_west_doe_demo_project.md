# D-PEC-23 — "TOU West Doe" demo project: owner-file import + schema-fit UI tranche

> **Epistemic status: agent-prepared decision packet recording an owner
> direction of record — not agent-invented authority.** The authority is the
> owner's 2026-07-07 launcher steer (verbatim below), received in-session per
> the D-T0-22/D-PEC-22 ruled-by-steer precedent (direction is the owner's act,
> K-AUTH-1; recorded verbatim, executed inside a pinned fence, STOP at owner
> merge). Sources govern on any disagreement.

## Owner direction of record (2026-07-07, launcher steer, Ryan Tufts, verbatim)

> I want to create a new demo project in PEC from these files.  Import the
> data in them and change the ui and ux to fit the schemas therein.
> `/Users/ryan/ai-env/projects/chirality/projects/pec/pilot-scratch/input/`
> call the project `TOU West Doe`

## Recorded interpretation (agent, 2026-07-07 — the ruling is the text above)

1. **New demo project.** A second `project` row in the committed demo database
   basis (`pec-demo.db`, the owner's live demo instance; scratch/demo mutation
   basis per D-T0-20's clarity sentence), named **TOU West Doe**. No in-app
   project-creation route exists; creation is a direct-insert script (the
   `tools/seed.ts` / `tools/pilot-drill.ts` pattern). Clerical defaults ⚑ for
   owner ratification at the import-approval gate: project code `TWD`,
   timezone `America/Edmonton`. The DB files themselves stay uncommitted
   (standing FILE_DROP_RUNBOOK rule; the owner may commit the demo DB churn
   separately if desired).
2. **Import the data.** The six files at `pilot-scratch/input/` —
   `mdl.xlsx`, `rail.xlsx`, `decisions.csv`, `risk.xlsx`, `schedule.csv`,
   `tracker.xlsx` (SHA-256 in the tranche packet) — map to the six §16
   contracts per `IMPORT_TEMPLATES/IMPORT_MAPPING.md`, extended for the new
   optional columns this tranche adds. **The steer is the drop-time
   direction, not the import approval:** FILE_DROP_RUNBOOK v1.1 (owner ruling
   RV-7) requires approval to follow the presented step-3 proposed import, so
   the loop presents the mapping/count/reject proposal and STOPS for the
   owner's in-session approval before any row lands. `risk.xlsx` is an
   unpopulated 100-row scaffold — nothing imports from it; its schema still
   drives the risk-register fit below.
3. **"Change the UI and UX to fit the schemas therein"** = the enumerated
   schema/contract/view/UI extensions in the Design section: source-file
   columns that today are dropped or folded into `remarks`/`rationale`
   composites become first-class, rendered fields. All contract-header
   additions are OPTIONAL columns — existing templates, exports, and pilot
   CSVs remain valid; absent headers change no behavior.
4. **Interaction with the 2026-07-07 simplification addendum (Receipt 51).**
   The addendum indefinitely postponed interface/import *refinement* as a
   standing priority; this steer is the owner's newer, specific direction and
   governs this run's scope. The addendum's general priority is otherwise
   unchanged, and the postponed rows stay postponed — this tranche discharges
   no D-PEC-14 evidence obligation, changes no D-PEC-15 re-import behavior
   (the interim rule stands), and adds no D-PEC-19 tracker edit path (tracker
   stays import-owned/read-only).

## Design (the schema-fit set; file basis = the discovery pass recorded in the tranche packet)

- **MDL → packages/deliverables.** `package` gains `area`, `package_type`
  (additive columns); the `mdl` contract gains optional `package_name`,
  `area`, `package_type` headers that set/update the auto-created package
  (name currently defaults to the code). Deliverables list renders
  Type (`deliverableType`, already modeled, previously unrendered) and Area
  (via package), with an area filter; Packages page renders area/type.
- **RAIL → log/intake.** `work_item` and `intake_item` gain `area`; the
  `rail` contract gains an optional `area` header; the Action & Hold Log
  renders Area with a filter.
- **Decisions.** `decision` gains `open_date`, `area`, `source`; the
  `decisions` contract gains the three optional headers; the Decisions
  register renders Source, Area, Opened.
- **Risks.** `risk` gains `category`, `risk_type`, `treatment`,
  `residual_probability`, `residual_impact` (the owner's risk log carries an
  original + residual scoring pair); the `risks` contract gains the optional
  headers; the Risks register renders Category, Type, Treatment and both
  P/I/P×I pairs.
- **Schedule.** `schedule_activity` gains `row_type`, `outline_level`,
  `parent_activity_id`, `percent_complete`, `duration_days`,
  `baseline_start`, `baseline_finish` (the owner's schedule export carries a
  WBS hierarchy, % complete, and baselines that the flat §16 contract
  drops); the `schedule` contract gains the optional headers; a new
  **read-only Schedule register tab** (`trackerRegisterView` precedent: view +
  one GET route + Registers tab + Admin export entry) renders the
  hierarchy-indented activity list with type, dates, baseline, % complete.
  The Plan page's six-week lookahead is untouched.
- **Tracker.** No schema change (D-PEC-13 was designed from this workbook);
  the register additionally renders the already-modeled, previously
  unrendered `packageTypeApproved`.
- **Exports/templates.** §16 register exports mirror the widened column sets
  (round-trip rule); the five affected `*-template.csv` files and
  `IMPORT_MAPPING.md` gain the new columns and a §TOU-West-Doe mapping
  section.

Everything else is out of scope; in particular: no new act family, no
permission change, no lifecycle/state-machine change, no new dependency
(ADR-002/F-PEC-3), no profile edit, no import-behavior change for existing
columns, accept/apply/`force` remain human acts (K-DOMAIN-3).

## Execution vehicle

`TRANCHE_2026-07-07_D-PEC-23_tou_west_doe_demo.md` (beside this packet's
directory) pins the exact file fence, verification plan, rollback, and
evidence bar. The tranche may not widen this packet; widening returns to the
owner.

## Human ruling

**RULED-by-direction (2026-07-07):** the owner's launcher steer quoted
verbatim above is the direction of record (D-T0-22/D-PEC-22 precedent).
Implementation directed in the same steer; executed branch-first with STOP at
owner merge. The **import approval remains a separate owner act** per the
FILE_DROP_RUNBOOK v1.1 RV-7 ruling — the loop stops at the presented import
proposal. Clerical defaults ⚑ (project code `TWD`, timezone
`America/Edmonton`) ratify or change at that same gate.
