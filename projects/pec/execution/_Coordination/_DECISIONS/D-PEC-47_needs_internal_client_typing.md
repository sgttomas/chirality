# D-PEC-47 - PROPOSAL: Needs internal-client typing

**Status:** AWAITING_RULING
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-47
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-39/41/43 precedent.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes the R2 "Needs internal/client typing" row of the
> reporting-product standing plan. Source execution remains prohibited unless
> and until the owner rules this packet.

## Why this row exists

The owner's discipline status report separates Needs into internal vs client
needs. The current discipline view and standard reports already show needs,
but they explicitly say the split is absent because no ruled typing exists.
D-PEC-41 landed RAIL v2 source facts and full-fidelity capture, but the live
TWD RAIL workbook does not provide an explicit internal/client classification
column; therefore this tranche must keep unknown values honest until the PE,
agent, or a future source column supplies the type.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The findings record the owner requirement: "Needs will be triaged into 'internal' and 'client'." | `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md` §4.4 |
| The standing plan's R2 row calls for typed requester-side triage on needs-shaped records, feeding the discipline view's Needs split and aging. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (R2 row) |
| Current standard reports mark `client/internal needs split` absent because needs typing is not implemented. | `projects/pec/server/src/reports/standard.ts` |
| Current discipline detail reports open needs and needs aging, with detail saying internal-vs-client typing is absent until its ruled tranche. | `projects/pec/server/src/services/views.ts`; `projects/pec/execution/_Coordination/REPORT_BASIS.md` |
| Work items and holds have no internal/client needs field today. RAIL v2 records do carry `responsibleParty`, `sourceIssueType`, and full-fidelity `sourcePayload`. | `projects/pec/core/src/types.ts`; `projects/pec/server/src/db.ts` |
| The live TWD RAIL workbook header set includes Package/Issue/Discipline/CoA/Issue Type/Responsible Party/Status/Priority/date fields, but no explicit internal/client classification column. | `projects/pec/pilot-scratch/input/2026-07-07-RAIL_Packages(1).xlsx` (headers inspected only) |

## Decision to rule

Whether to authorize one source tranche implementing needs typing:

1. **Model:** add a nullable, import/triage-owned needs audience field with
   values `internal` / `client` / absent. Absent is a first-class honest
   state, not a hidden default.
2. **Source mapping:** if a future uploaded source provides an explicit
   internal/client column, the import lane maps it. The current TWD RAIL
   workbook does not, so existing rows remain absent unless triaged.
3. **Triage path:** PE/agent triage may set or correct the audience on
   needs-shaped intake/work-item/hold records, with history. The agent may
   propose or summarize classifications; final setting follows the ruled
   RBAC/triage boundary and never edits computed status.
4. **Read/report surfacing:** discipline detail and standard reports split
   Needs into Internal / Client / Unclassified buckets. Aging remains
   drill-backed and visibility-filtered. Report drafts may say "unclassified"
   rather than invent a side.
5. **Exports and round-trip:** any contract/export that carries needs typing
   round-trips the explicit value; absent stays blank/absent.
6. **Tests:** import explicit values, reject invalid values with basis,
   preserve absent, triage update/history, discipline split, report absent
   removal once typed values exist, and visibility redaction.

**Not in scope:** inferring client/internal from free text, party names,
discipline, issue type, log, or package; bulk editable task-management
surfaces; new dependencies; `.docx` generation; interfaces contract work.

## Fence (exact; STOP outside it)

O-A may touch only:

- `projects/pec/core/src/**` (additive type)
- `projects/pec/server/src/**` (schema/import/triage/read/report surfacing)
- `projects/pec/server/test/**`
- `projects/pec/web/src/**` (read-only display of the split if the
  implementation elects to show it on the existing discipline/report surfaces)
- `projects/pec/agent-sidecar/**` (bounded triage/proposal language only)
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`

No tracked DB files; no new runtime dependency; no direct import apply; no
board/bulk-mutate/task-management UI.

## Options

- **O-A (recommended):** implement nullable needs audience with explicit
  import/triage ownership and read/report split.
- **O-B:** report-only "Unclassified" bucket, no model/triage change yet.
- **O-C:** documentation-only convention pending a revised source column.
- **O-D:** defer.

## Verification plan (workplan step-4 bar)

PEC belt-and-braces; source tests listed above; visual pass if `web/**` is
touched; scope containment subset of the ruled fence; self-check / coord-check
/ `git diff --check`; adversarial review that no classification is inferred
from weak evidence and unclassified rows remain visible.

## Rollback

Single revert of the tranche commit(s). Additive nullable fields revert by
ordinary rollback; history entries remain append-only if triage actions occur
before rollback.

## Human ruling

**OPEN - decision is the owner's (K-AUTH-1).** Rule O-A / O-B / O-C / O-D.
