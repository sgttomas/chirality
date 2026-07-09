# §16 Import Templates + Workbook Mapping (pilot project 26020)

> **Epistemic status: agent-prepared coordination artifact at owner direction
> (2026-07-05: "Create the templates you need that take the best of what I've
> provided and adds what else you need."), not authority.** The §16 import
> contracts in `server/src/import/index.ts` govern the columns; the owner's
> workbooks govern the content. Clerical defaults below are flagged ⚑ for
> owner ratification. Example rows in the `*-template.csv` files are fiction.

## The six templates (tracker added 2026-07-06 under the D-PEC-13 O-A ruling)

Each `*-template.csv` header row is the exact §16 contract (identical to the
register export headers, so export→edit→re-import round-trips). Required
columns per contract (header-level; ✱ = also required per row):

| Contract | Required columns |
|---|---|
| `mdl` | doc_no✱, title✱, package✱, discipline, owner, current_rev✱, state✱, due_date |
| `rail` | item_id✱, statement✱, type✱, log✱, owner✱, need_by✱, status✱, raised_by✱, raised_date✱ |
| `decisions` | decision_id✱, title✱, statement✱, authority✱, need_by, status✱ |
| `risks` | risk_id✱, title✱, cause, consequence, owner, status✱ |
| `schedule` | activity_id✱, description✱, start✱, finish✱ |
| `tracker` | package✱ (the key, amended 2026-07-06), package_name✱, tracking_no, discipline, area, stage_* (12, header-required) |

Accepted vocabularies (import normalizes case/spaces/hyphens):

- MDL `state`: `in_work, in_check, check_accepted, ready_for_approval,
  approved, issued, returned_with_comments, superseded` (aliases `IFR/IFA/IFC`
  → issued).
- RAIL `type`: `action, coordination, risk_treatment, rework, other, task,
  hold, interface` (hold rows also need `hold_cause`: `information, decision,
  approval, resource, client_input, interface, vendor_data, other`).
- RAIL `log`: `package, internal, client`. RAIL `status`: `open, in_work,
  in_progress/started, closed/complete/completed/done, cancelled`.
- decisions `status`: `identified, in_progress, pending, decided, superseded`;
  `decided` rows require an `outcome` from `select, approve, reject, defer,
  conditionally_accept, confirm_basis, waive, supersede`.
- risks `status`: `open, mitigating/treating, closed`; probability/impact 1–5.
- Dates are `YYYY-MM-DD`. `owner`/`authority`/`raised_by` match a registered
  person by exact name or email; unmatched `owner`/`authority` rejects the row.

## Workbook → template mapping applied (2026-07-05 run)

### MDL (`Master Deliverables List` sheet, header row 2, 457 rows → 457 mapped)

| §16 column | Source | Note |
|---|---|---|
| doc_no | Deliverable ID | unique in workbook — idempotency key |
| title | Deliverable Description | |
| package | Package ID | import auto-creates packages by code |
| discipline | Discipline | |
| owner | — | ⚑ no owner column in workbook; left blank (optional for MDL) |
| current_rev | — | ⚑ workbook tracks no rev; defaulted `A` on every row |
| state | Working Status | ⚑ `Not Set` → `in_work` (only value present) |
| due_date | Next Target Date | empty in workbook |
| milestone | Next Approval Gate | empty in workbook |
| remarks | Package Name + Area # + Package Type + Priority + Hold Type | preserves the workbook columns §16 has no slot for |
| deliverable_type | Document Type | |

### RAIL (`RAIL` sheet, header row 7, 332 rows → 272 mapped + 60 routed)

| §16 column | Source | Note |
|---|---|---|
| item_id | Item # | unique — idempotency key |
| statement | ITEM DESCRIPTION | |
| type | ITEM TYPE | `Action`→action; ⚑ `Information`→other (tagged in notes); **`Decision` rows (60) excluded here — they are the decisions log** (see below) |
| log | — | ⚑ constant `package` (the workbook is the packages RAIL) |
| owner | RESPONSIBLE PARTY | verbatim — see the roster gap below |
| need_by | CURRENT else ORIGINAL TARGET COMPLETION DATE | 71 rows blank → those reject (row-required) |
| status | STATUS | `New`→open; ⚑ `On Hold`→open + `[source status: On Hold]` note (RAIL has no on-hold work-item state; §16 holds are their own type); `Information`→open |
| raised_by | RESPONSIBLE PARTY (fallback `unspecified`) | workbook has no raiser column; import falls back to the importing session |
| raised_date | ASSIGNED DATE | blank rows reject (row-required) |
| notes | UPDATES | |

### decisions (`Sheet1`, 62 rows → 62 mapped; RAIL `Decision` rows are the same population)

| §16 column | Source | Note |
|---|---|---|
| decision_id | ID # | verbatim — idempotency key |
| title | Action (fallback Source) | |
| statement | Decision (fallback Action) | |
| authority | Responsible | verbatim — see the roster gap below |
| need_by | Due Date | Excel serials converted to ISO |
| status | Status | `Decision`→decided; ⚑ `Cancelled`→superseded |
| outcome | — | ⚑ decided rows defaulted `select` (workbook records no outcome vocabulary) |
| rationale | Category + Source + Area + Comments | preserves unslotted columns |
| decided_date | Date Closed | serials → ISO |

### risks (`Risk Log` sheet — placeholder/scaffold only, not yet populated per owner)

No risks import has succeeded yet because the owner-provided workbook held only
the scaffold sheet. This mapping is a placeholder crosswalk for when the risk
log is populated:
`RISK ID`→risk_id, `RISK TITLE`→title, `RISK DESCRIPTION`→cause (put the
impact side in consequence), `PROB`→probability, `IMP`→impact, `PROPOSED
MITIGATION`→mitigation, `CATEGORY`/`TYPE`/`RISK LEVEL`/`RISK TREATMENT` have
no §16 slot — carry in title prefix or mitigation text as needed.

### schedule (`schedule.csv` extractor output, evidence-04: 127 rows → 127 mapped)

The owner replaced the PDF with `pilot-scratch/input/schedule.csv`; evidence-04
proved the CSV extractor path. Mapping applied:

| §16 column | Source | Note |
|---|---|---|
| activity_id | `id` | `SCH-{id}` idempotency key |
| description | `task_name` | Adds `[Summary]` / `[Milestone]` tags where the extractor flags them |
| start | `start` | ISO date passthrough |
| finish | `finish` | ISO date passthrough |

Evidence: `_DomainEngines/pec/PEC_2026-07-05_DPEC01-pilot-evidence-04/MANIFEST.md`
records 127/127 accepted and `activity_id←SCH-{id}`,
`description←task_name`, ISO start/finish passthrough.

## The person roster — RULED (owner, 2026-07-05: "Create placeholders")

`ROSTER_PLACEHOLDERS.csv` beside this file holds the 44 placeholder persons
(workbook strings verbatim as names; `@placeholder.invalid` emails; no login).
Replace a placeholder with the real person in-app (or update + re-import) as
the pilot roster firms up. `None` is deliberately NOT a placeholder — decision
rows with authority `None` stay rejected until a real authority is assigned.

Owner ruling on the ⚑ clerical defaults (2026-07-05): "Proceed with this
as-is unless you recommend changes now (do it!)" — defaults above stand, and
two recommended changes were applied at the same ruling:

- RAIL `raised_date` now defaults to the import date when ASSIGNED DATE is
  blank (tagged `[raised_date defaulted to import date]` in notes) — 199 rows.
- RAIL `package` now carries the workbook AREA (e.g. `26020-01 - Deep Cut`)
  so unanchored intake rows keep their area as the anchor suggestion.

## Known import-seam behaviors (observed 2026-07-05, evidence-03)

- **RAIL re-import is not idempotent for unanchored rows**: rows that land as
  intake are NOT matched by `item_id` on re-import and would duplicate. Only
  re-import rows that were rejected (or that match an existing
  work-item/hold/interface ref). Candidate harness/tool improvement — logged
  in the evidence-03 manifest.
- Person-creation from the roster CSV must use a real CSV parser: the quoted
  `"PC, DC, SCM"` name breaks naive comma-splitting (this bit the first
  roster application; fixed in-place in the scratch DB).

## §tracker — workbook → template mapping (added 2026-07-06, D-PEC-13 O-A)

Owner ruling of record (verbatim, both sentences): "Proceed with 1. Rule
D-PEC-13 as follows. Use the tracker.xlsx provided as your template and
proceed accordingly." (recorded in
`../_DECISIONS/D-PEC-13_package_tracker_import_contract.md`). Capture grain:
manifests/hashes only (the ruling's item-4 default) — this section carries
header names, shape patterns, and counts; no verbatim workbook content. Source
file: `pilot-scratch/input/tracker.xlsx`, sheet `Package Summary`, SHA-256
`01fc38f085dc8218c0e006d8a27c8ad7fa157c964ffe4041a7599ebc54f6bf9e`, 65 data
rows.

Agent-side mapping at CSV-authoring time (xlsx never enters the server —
ADR-002):

| §16 column | Workbook column | Note |
|---|---|---|
| tracking_no | CoA Tracking Number | plain data field, shape `26020-NN-PT-NN-NNN`; kept verbatim, non-unique, never a conflict source (owner amendment 2026-07-06: "Keep the CoA number but don't key on that.") |
| package_name | Package Name | |
| discipline | Discipline | |
| area | Area | |
| package_type_approved | Approved Package Type (per TOU)? | trimmed; mixed `No`/type-string semantics carried verbatim ⚑ |
| package_type_proposed | Proposed Package Type for TOU | trimmed |
| line_items | Line Items | newline → `; ` join |
| vendors_engaged | Vendor(s) Engaged | newline → `; ` join; `-` → blank ⚑ |
| vendor_awarded | Vendor Awarded | empty in workbook today |
| expected_delivery_date | Expected Delivery Date | empty today; `YYYY-MM-DD` when populated |
| cost_estimate_cad | Cost Estimate $CAD (2026) | empty today |
| comments | Comments | 12/65; carries prose dates today ⚑ |
| stage_* (12) | Budgetary Datasheet … Databook | vocabulary normalized (`Not Started`→`not_started`, `In Progress`→`in_progress`, `Complete`→`complete`, `Issued`→`issued`, `Not Applicable`→`not_applicable`) |
| package | — (derived) | **the idempotency key** (owner amendment 2026-07-06: "match the tracker entries with the PKG-#### numbers we're using"): unique tracker-name → MDL Package ID → `package.code` resolution at authoring time (54/65 unique today); row-required and must resolve to an existing `package` record — unresolved rows reject as owner-side data gaps until mapped (11/65 today, residual gap below) |
| — | Package # | 0/65 populated; unmapped until the owner populates it ⚑ |

Tracker rows are import-owned (no in-app edit path in this scope; re-import
always refreshes); rows with no resolvable `package` anchor still create
`package_tracker` records with a null link (NO intake fallback — ruled
divergence from RAIL, D-PEC-13). Stated-but-unresolvable `package` anchors
reject the row.

Refresh conventions (shipped behavior, test-pinned): optional columns refresh
only when their header is present in the file — a narrower re-import retains
existing values rather than silently wiping them (the schedule contract's §16
no-silent-wipe reading, generalized); header-required columns always refresh.
Duplicate-vs-validation precedence (on the package key per the 2026-07-06
amendment): rows are validated before the duplicate-in-file check, so an
invalid duplicate row reports as a reject (not a conflict), and if the FIRST
occurrence of a key is invalid the next valid occurrence wins the key — every
row is reported either way, nothing silent.

## Residual workbook data gaps (owner/pilot-team side)

- 17 RAIL rows with no target-completion date (+1 with a `1900-11-27` junk
  date) — reject until dated.
- 8 decision rows with authority `None` + 2 with blank authority + 2 with
  blank status — reject until assigned.
- Risk log unpopulated; schedule.csv extractor mapping is proven by
  evidence-04.
- Tracker workbook (2026-07-06, updated under the same-day key amendment):
  11/65 rows have a Package Name resolving to no `package` record — they
  reject as data gaps until the owner maps them (or adds the MDL rows); the
  duplicated CoA value on sheet rows 16/54 is no longer an import blocker
  (both rows key on their distinct packages) but remains a workbook oddity
  the owner may fix; `Package #` column 0/65 populated (unmapped until
  populated).

## §D-PEC-23 — optional-column extensions (2026-07-07, directed by owner steer)

The five non-tracker contracts gained OPTIONAL columns; absent headers change
no behavior, and a file without them never wipes previously imported values
(§16: update only when the header is present). Import validation and the
mirrored register exports are in `server/src/import/index.ts`; tests in
`server/test/import-dpec23.test.ts`.

| Contract | New optional columns | Lands on |
|---|---|---|
| `mdl` | `package_name`, `area`, `package_type` | the auto-created `package` record (refreshed once per run under the import-ownership guard) |
| `rail` | `area` | `work_item.area` / `intake_item.area` |
| `decisions` | `open_date` (YYYY-MM-DD), `area`, `source` | `decision` columns of the same names |
| `risks` | `category`, `risk_type`, `treatment`, `residual_probability` (1–5), `residual_impact` (1–5) | `risk` columns of the same names |
| `schedule` | `row_type` (`task\|summary\|milestone`), `outline_level` (int), `parent_activity_id`, `percent_complete` (0–100), `duration_days`, `baseline_start`, `baseline_finish` | `schedule_activity` columns; rendered by the read-only Schedule register tab (`GET /api/projects/:pid/schedule`) |

## §TOU-West-Doe — workbook → template mapping (2026-07-07 run)

Same workbook family as the 26020 pilot (the six files at
`pilot-scratch/input/`, SHA-256 pinned in
`../TRANCHE_2026-07-07_D-PEC-23_tou_west_doe_demo.md`), mapped for the new
demo project **TOU West Doe** with the D-PEC-23 optional columns now carried
first-class instead of folded into composites:

- **MDL** (457 → 457): as the 2026-07-05 run, except `Package Name` →
  `package_name`, `Area #` → `area`, `Package Type` → `package_type` (no
  longer packed into `remarks`; remarks keeps only Priority/Hold Type when
  populated). `current_rev=A` fill and `Not Set → in_work` unchanged (ruled).
- **RAIL** (332 → 272 mapped + 60 `Decision` rows routed to decisions.csv):
  as the 2026-07-05 run, plus `AREA` → `area` (also still copied to
  `package` as the ruled anchor-suggestion fill). 18 expected rejects: 17
  blank need-by + 1 literal `Ongoing` (passed through verbatim, never
  invented). `raised_date` fill tagged in-row.
- **decisions** (62 → 62): as the 2026-07-05 run, plus `Open Date` →
  `open_date`, `Area` → `area`, `Source` → `source` (rationale keeps only
  Comments). Excel serial dates converted (e.g. 46086 → 2026-03-05).
  `decision_id` kept verbatim (`1`…`62`, the ruled convention). 10 expected
  rejects (8 authority `None`, 2 blank rows) — `None` is deliberately NOT a
  placeholder.
- **risks**: scaffold still unpopulated — nothing to import; the crosswalk
  for when populated now includes `CATEGORY` → `category`, `TYPE` →
  `risk_type`, `RISK TREATMENT` → `treatment`, `PROB2`/`IMP3` →
  `residual_probability`/`residual_impact`.
- **schedule** (127 → 127): `id` → `SCH-{id}`, ISO date columns, plus
  `row_type`/`outline_level`/`parent_id → parent_activity_id (SCH-{id})`/
  `percent_complete`/`duration_days`/`baseline_*_date_iso` → the new columns.
  Description no longer tagged `[Summary]`/`[Milestone]` (row_type is
  first-class).
- **tracker** (65 → 54 resolvable + 11 package-key data gaps): unchanged
  §tracker mapping; `package` resolved from Package Name → MDL Package ID.

Import-ready CSVs + per-run mapping report:
`pilot-scratch/import-ready/tou-west-doe/` (gitignored, per the standing
capture rules).

## §contract-v2 — MDL/RAIL v2 from the owner's revised TWD templates (2026-07-09, D-PEC-41 O-A)

The revised templates (owner-provided 2026-07-09; structure of record in
`../_DECISIONS/D-PEC-41_mdl_rail_contract_v2.md`) have no `doc_no`/`item_id`.
Both v2 shapes ride the SAME contract ids (`mdl`, `rail`); the importer
detects the shape from the header set. v1 files keep working unchanged.
Owner fidelity direction (Receipt 75, verbatim in the packet): every provided
column and sheet is captured losslessly; display stays selective — unmapped
columns land verbatim in the record's `source_payload`, non-tabular workbook
sheets land verbatim in the proposal's `source_extras`.

| Contract | v2 detection | Required | Optional (mapped) |
|---|---|---|---|
| `mdl` | no `doc_no`, has `package` + `deliverable_type` | package✱, deliverable_type✱ | area, project_phase, discipline, package_type, package_name, deliverable_id, target_completeness, working_status, percent_complete |
| `rail` | no `item_id`, has `package` + `issue_no` | package✱, issue_no✱ | discipline, area, phase, coa_tracking_number, package_type, package_name, issue_type, statement, updates, responsible_party, status, priority, assigned_date, original_target_date, current_target_date, actual_completion_date |

Recorded mapping rules (v2):

- **MDL identity**: a populated `deliverable_id` wins; otherwise `doc_no` is
  derived deterministically as
  `<package>-<slug(deliverable_type)>[-<slug(package_name)>]` — a pure
  per-row function of provided content (never file-structure-dependent), the
  name segment present whenever `package_name` is (the template legitimately
  repeats package + type across items distinguished only by name). Identical
  duplicate rows: first processed, later rows reported as conflicts.
  Re-imports are idempotent for unchanged content; a changed distinguishing
  name is a new identity (the stale record stays visible — never silently
  deleted).
- **MDL attested fields**: `percent_complete` (0–100 integer; non-numeric
  markers such as `Next Phase` are captured verbatim and excluded from
  rollups; out-of-range numerics are row rejections), `working_status`,
  `target_completeness`, `project_phase` are PE-attested import fields —
  never in-app editable, never derived in-app (reconciliation 1). No revision
  is created (the v2 template carries no revision facts).
- **MDL title**: derived for display as `<deliverable_type> — <package_name>`
  (recorded rule; the template has no title column).
- **RAIL identity**: `<package>#<issue_no>`. Package placeholder rows (no
  issue_type and no statement) refresh package attributes only and create no
  issue record (factual-or-absent); they are counted as `packageRows` in the
  import report.
- **RAIL records**: every issue row is a package-anchored work item; the
  verbatim issue type is attested on `source_issue_type` (`Action` maps to
  kind `action`, all other types to `other` — the reporting vocabulary reads
  the attested type). `responsible_party` is a discipline/function captured
  verbatim; `owner_id` resolves only on an exact person match, else the
  importing PE holds custody. `current_target_date` maps to `need_by`;
  verbatim status/phase/updates/CoA/dates ride `source_payload`.
- **Caught review signals** (returned in dry-run/apply reports, persisted on
  the proposal; never coerced, never schema-blocked): `mdl-on-hold` /
  `rail-on-hold` (MDL↔RAIL consistency seeds), `phase-cancelled` (RAIL phase
  says Cancelled, status does not), `percent-marker`, `working-status-vocab`
  / `issue-type-vocab` (value outside the template Lists vocabulary).
- **Identity adoption**: when the PE later populates `Deliverable ID` for a
  row previously imported under a derived identity, the existing record
  adopts the provided id (no register duplication); the migration honors the
  import-ownership guard.
- **Round-trip**: registers `mdl-v2` and `rail-v2` export the v2 columns
  plus any captured verbatim payload columns (full-fidelity parity; attested
  markers round-trip as provided). Source-faithful columns emit ONLY
  verbatim-provided values — never app state tokens, the need-by fallback, or
  app-generated closure timestamps. `deliverable_id` exports the record
  identity (provided or derived), so feeding an export back re-imports
  against the same identity.
- **Fix-forward pins (adversarial review 2026-07-09)**: multiline cell values
  survive the workbook→CSV→mapping path intact (quote-aware record
  splitting); MDL `area`/`package_name`/`package_type` are dual-captured
  (package record first-row-wins AND per-row verbatim payload); RAIL
  placeholder rows may leave `Issue #` blank; reopening a completed RAIL
  issue clears its stale closure timestamp; v2 shape detection also requires
  the absence of v1's other key column (`current_rev`/`raised_by`) so a
  malformed v1 file fails loudly as v1.
- **Non-tabular sheets** (Rules of Credit, Data Dictionary, Lists, RAIL
  metadata block): the proposal API accepts a JSON body `{ csv, extras }`;
  `extras` is stored verbatim on the proposal (`source_extras`, size-capped
  like the CSV). The XLSX lane (D-PEC-42) populates it.
