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

### risks (`Risk Log` sheet — scaffold only, not yet populated per owner)

Workbook scaffold → template crosswalk for when the log is populated:
`RISK ID`→risk_id, `RISK TITLE`→title, `RISK DESCRIPTION`→cause (put the
impact side in consequence), `PROB`→probability, `IMP`→impact, `PROPOSED
MITIGATION`→mitigation, `CATEGORY`/`TYPE`/`RISK LEVEL`/`RISK TREATMENT` have
no §16 slot — carry in title prefix or mitigation text as needed.

### schedule (`schedule.pdf` — not importable; contract is CSV/XER-derived)

Populate `schedule-template.csv` from the schedule tool's CSV/XER export (the
RAIL references `26020-FEED-Activities-Plan…xlsx`, which looks like the
natural source).

## ⚑ The one blocking gap: the person roster

§16 rejects any RAIL `owner` or decisions `authority` that is not a registered
person (exact name or email). The workbooks use first names, disciplines, and
companies — 39 distinct RAIL values (`Adam`, `Alex / Chris`, `Process`,
`CSA`…) and 9 decisions values (`Millenia`, `Tourmaline`, `Piping`,
`None`…). Until the pilot roster exists (people registered + a mapping from
these strings), those rows land as row-level rejects in the import report —
by design. Owner options: supply a roster mapping, or rule that discipline/
company placeholder persons may be created.
