# TRANCHE 2026-07-07 — D-PEC-23 TOU West Doe demo project v1

> **Epistemic status: execution vehicle for a directed decision — not new
> authority.** The authority is the owner's 2026-07-07 launcher steer,
> verbatim in `_DECISIONS/D-PEC-23_tou_west_doe_demo_project.md` (ruled-by-
> direction, D-T0-22/D-PEC-22 precedent). This packet pins the fence for
> execution and **may not widen it**; any needed widening returns to the
> owner. Precedent: `TRANCHE_2026-07-06_D-PEC-13_tracker_contract_v1.md`.

## Input file basis (SHA-256, captured 2026-07-07 at `pilot-scratch/input/`)

```
a5207b320fa2dcd81d9b31e28cff0d4623bbd2981b9cb8e06a825f8f165078c8  decisions.csv
bf73c03f5f753652c7d0e62086dedbbcc6f6642de29b32976e814efc7860db74  mdl.xlsx
545655199557527fc2d41b938bfec173ec70bd3e00f6caff817d69db37c33e84  rail.xlsx
b6b1ea0ef6b4a4ed44132e13ae1727032dcddae02d2b174115b5272914d92125  risk.xlsx
42e68a3c5cd792534bf8184a57dad96c16b0950abb051d377ee7e507fb7757ea  schedule.csv
01fc38f085dc8218c0e006d8a27c8ad7fa157c964ffe4041a7599ebc54f6bf9e  tracker.xlsx
```

Raw files and DB files stay uncommitted (FILE_DROP_RUNBOOK standing rule);
run-generated mapping CSVs live under gitignored `pilot-scratch/import-ready/
tou-west-doe/`; committable capture is the evidence pack named below.

## What ships (the directed design, unchanged from the D-PEC-23 packet)

Optional-header §16 contract extensions + additive columns + register-view/UI
fit for MDL (package `area`/`package_type`/`package_name`), RAIL (`area`),
decisions (`open_date`/`area`/`source`), risks (category/type/treatment +
residual probability/impact pair), schedule (WBS `outline_level`/
`parent_activity_id`, `row_type`, `percent_complete`, `duration_days`,
`baseline_start`/`baseline_finish` + a new read-only Schedule register tab);
tracker renders the already-modeled `packageTypeApproved`. Existing headers,
behaviors, and templates remain valid; absent optional headers change no
behavior.

## Exact file fence (anything outside is out of scope)

Source:
- `projects/pec/core/src/types.ts` — field additions on `Package`,
  `WorkItem`, `IntakeItem`, `Decision`, `Risk`, `ScheduleActivity`; no new
  record type, no permission change, no new act family.
- `projects/pec/server/src/db.ts` — additive columns via DDL +
  `ensureColumn` migrations only; no table drop/rebuild, no trigger change.
- `projects/pec/server/src/import/index.ts` — optional-header handling in
  `importMdl`/`importRail`/`importDecisions`/`importRisks`/`importSchedule`;
  matching `exportRegister` column widening (§16 round-trip).
- `projects/pec/server/src/services/views.ts` — affected register views gain
  the new fields; new `scheduleRegisterView`.
- `projects/pec/server/src/api.ts` — exactly one new read-only route
  `GET /api/projects/:pid/schedule`.
- `projects/pec/web/src/pages/Deliverables.tsx`, `LogHome.tsx`,
  `Registers.tsx` (Decisions/Risks/Tracker tabs + new Schedule tab),
  `Packages.tsx`, `Admin.tsx` (export list entry) — rendering/filters only;
  no new mutation control anywhere.
- `projects/pec/server/test/**` — new/updated tests for the optional-header
  paths, migrations, views, and round-trip exports (synthetic fixtures only).
- `projects/pec/server/src/repo.ts` / `core/src/snapshot-index.ts` — ONLY if
  the type additions require serialization plumbing; no behavior change.

Coordination (not source):
- `IMPORT_TEMPLATES/{mdl,rail,decisions,risks,schedule}-template.csv` +
  `IMPORT_MAPPING.md` (new columns + §TOU-West-Doe mapping section);
- this packet; the D-PEC-23 packet; the pec register row; the loop receipt;
  the evidence pack `_DomainEngines/pec/PEC_2026-07-07_DPEC23-evidence-01/`.

Constraints carried whole: **zero new dependencies** (ADR-002/F-PEC-3); no
root-manifest change; no profile edit; no lifecycle/state-machine change;
no D-PEC-15 re-import-behavior change; no D-PEC-19 tracker edit path;
accept/apply/`force` remain human acts (K-DOMAIN-3).

**STOP clause (D-PEC-17 rider-8 pattern):** a DB-migration need beyond
additive columns, an out-of-fence file, or behavior beyond the directed
design → STOP and return to the owner; no in-run fence widening.

## Demo-instance acts (not repo writes; scratch/demo mutation basis)

A run-local script (uncommitted, under `pilot-scratch/`) creates on
`pec-demo.db`: the `TOU West Doe` project row (⚑ code `TWD`, ⚑ timezone
`America/Edmonton`), placeholder persons for workbook-verbatim
owner/authority names (`@placeholder.invalid`, no login — ROSTER precedent),
role grants, then — **only after the owner's step-4 import approval** — the
six §16 imports in dependency order (mdl → rail → decisions → risks →
schedule → tracker), report capture, and a backup. `seed`/`drill` are never
run against `pec-demo.db` (seed wipes its target).

## Rollback plan

Branch-first (`codex/pec-tou-west-doe-demo`); the PR is the unit of revert —
one `git revert` of the merge commit restores the prior source surface (new
columns are additive and inert unreferenced). Demo-instance rollback: the
pre-import backup taken by the run script restores `pec-demo.db`; the DB is
uncommitted either way.

## Verification plan (workplan step-4, at the tranche PR's final SHA)

pec `npm run typecheck && npm test && npm run build && npm run drill`
(including the new tests); repo self-check with no unexplained baseline
shift; full `tools/` pytest; coord-check on the committed range;
`git diff --check`; **adversarial scope check** — `git diff --name-only` on
the tranche commits ⊆ the fence above plus the enumerated coordination
surfaces; adversarial two-lens review (fact + governance) of the packets and
diff per session conventions; CI green; **owner merge is the gate** (no
pre-ruling in force; no self-merge).

## Evidence bar

`_DomainEngines/pec/PEC_2026-07-07_DPEC23-evidence-01/` (immutable, dated):
the presented step-3 import proposal (counts, mapping deltas, expected
rejects), the owner's approval verbatim, per-contract `ImportReport`
summaries at the count grain, refreshed register exports for the new project
where the API exposes them, and SHA256SUMS. Capture limits per the owner's
2026-07-05 basis (D-PEC-01/RV-11): count-level results + hashes; **no
verbatim real rows committed** unless the owner directs otherwise — this is
the same workbook family as the 26020 pilot (real project content).
