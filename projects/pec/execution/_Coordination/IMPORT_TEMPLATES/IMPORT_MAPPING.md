# §16 Import Templates + Workbook Mapping (pilot project 26020)

> **Epistemic status: agent-prepared coordination artifact at owner direction
> (2026-07-05: "Create the templates you need that take the best of what I've
> provided and adds what else you need."), not authority.** The §16 import
> contracts in `server/src/import/index.ts` govern the columns; the owner's
> workbooks govern the content. Clerical defaults below are flagged ⚑ for
> owner ratification. Example rows in the `*-template.csv` files are fiction.

## The five templates

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

## Residual workbook data gaps (owner/pilot-team side)

- 17 RAIL rows with no target-completion date (+1 with a `1900-11-27` junk
  date) — reject until dated.
- 8 decision rows with authority `None` + 2 with blank authority + 2 with
  blank status — reject until assigned.
- Risk log unpopulated; schedule.csv extractor mapping is proven by
  evidence-04.
