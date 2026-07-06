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
