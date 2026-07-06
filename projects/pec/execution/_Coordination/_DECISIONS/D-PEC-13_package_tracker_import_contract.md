# D-PEC-13 - Package Tracker import contract + proposal-shaped agent path

**Status:** RULED (O-A, 2026-07-06 — see Human ruling).
**Date prepared:** 2026-07-06
**Decision ID:** D-PEC-13
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is
the owner's (K-AUTH-1; D-GOV-04). This packet is prepared for the owner's read
at the gate — it is NOT covered by any pre-ruled selection: the Receipt 32
item-4 conditional standing pre-ruling named D-PEC-13 among the eligible rows
but expired by its own quoted terms ("this session only; expires at session
end or 24 hours after this direction, whichever comes first"); this packet is
prepared in a later session.

**Register note (the D-PEC-14 register-row convention):** the register-row
flip NOT_PREPARED → AWAITING_RULING rides the PR that carries this packet (the
main loop flips the row); the on-ruling flip is AWAITING_RULING → RULED.

> **Epistemic status: agent-prepared decision packet, not authority.** Every
> claim about the owner's Package Tracker workbook below is grounded in a
> read-only analysis of the owner-dropped file
> `projects/pec/pilot-scratch/input/tracker.xlsx` performed 2026-07-06
> (openpyxl, data-only); every claim about the shipped import mechanism cites
> the source file and line. Clerical mapping defaults are flagged ⚑ for owner
> ratification, the `IMPORT_MAPPING.md` convention.
>
> **Capture grain of this packet:** tracker.xlsx is a materially new data
> source — it is NOT among the owner-enumerated D-PEC-01 input files
> (`_DomainEngines/pec/PEC_2026-07-05_DPEC01-execution-basis/OWNER_INPUTS.md`
> enumerates the mdl/rail/decisions/risks workbooks and the schedule export —
> `schedule.pdf` in the basis; the live CSV arrived later per its delta
> record), and
> the pilot-scratch gitignore rule carries the owner ruling "manifests/hashes
> only" (`projects/pec/.gitignore:9-11`). This packet therefore commits **no
> verbatim tracker content**: only header names, shape patterns, counts,
> distributions, row coordinates, and the file hash — the evidence-manifest
> grain. A ruling line letting the owner set tracker capture limits going
> forward is requested in "Decision to rule" item 4.

Structure precedent: the design-gate shape of `D-PEC-16_builtin_agent_ui.md`
(adopt design → runtime/tranche structure made explicit in the options), the
verbatim-quote and named-obligation conventions of
`D-PEC-10_agent_intake_triage.md`, the tranche-authorization shape of
`D-PEC-08_upload_agent_source_tranche_authorization.md` (implementation
authorization is its own act, with the exact fence, tests, and
rollback/verification plan pinned) and the folded-tranche detail of
`D-PEC-17_builtin_agent_ui_source_tranche.md`, and the semantics baseline of
`D-PEC-12_l3_import_proposal_semantics.md`. Mapping-table and ⚑-flag
conventions follow `../IMPORT_TEMPLATES/IMPORT_MAPPING.md`.

## Why this row exists

This row was opened at Receipt 30 by the D-PEC-10 O-A ruling: obligation WF-5
(the Package Tracker has a proposal-shaped agent path) was **parked by
construction — no §16 contract exists** (verified then at
`server/src/import/index.ts` and re-verified now: the contract switch carries
exactly `mdl, rail, decisions, risks, schedule`,
`server/src/import/index.ts:493-502`).

The owner workflow intent of record (2026-07-05, in-session, Ryan Tufts,
verbatim — quoted per the D-PEC-10 direction item 1, which forbids
paraphrase):

> So for now I'm planning to use it myself, on my local machine. I will be using the RAIL,
> Master Deliverables List, Risk Log, Schedule, and Package Tracker, to update the status by
> having the agent intake and triage the information therein to the correct database
> assignments. The interface will also allow the human to make targeted changes within the
> current screen and what it shows. But the agent is the primary means of making updates. As
> for how I get the information into those documents, it occurs from weekly updates and work
> I do within my team. That's the intended workflow, which was more than how I probably
> initially described it.

The Package Tracker is the fifth named document of that intent and the only
one with no contract. The owner's preparation direction for this row
(2026-07-05, D-PEC-10 direction item 2(a), verbatim):

> (a) each of the five named source documents has a proposal-shaped agent path — note the
> Package Tracker has NO §16 import contract today, so it gets its own register row rather
> than an awkward MDL mapping;

And the ruled priority governing shape (D-PEC-12 owner amendment, 2026-07-05,
verbatim): "The agent should have full agency, don't try to use semantics as a
replacement for proper governance harnesses (more than just semantics) so
focus on making a useful agent for now."

**The concrete basis is a live-tree delta first observed and recorded by this
loop after Receipt 35:** the owner dropped
`projects/pec/pilot-scratch/input/tracker.xlsx` into the pilot-scratch input
directory (file timestamps: created 2026-07-05 23:49, last modified
2026-07-05 23:52 — the file itself predates the commit times of Receipts
31–35; it enters this loop's record here). Observed file facts: 39,508
bytes, SHA-256
`01fc38f085dc8218c0e006d8a27c8ad7fa157c964ffe4041a7599ebc54f6bf9e`; the file
is inside the gitignored `pilot-scratch/` tree (`projects/pec/.gitignore:11`),
so it is owner-local, never committed. Reading it is lawful under the D-T0-20
O-B ruling — owner-dropped weekly files are enumeration item (iv)
(`_DomainEngines/_DECISIONS/D-T0-20_pec_harness_agent_residency.md`, ruling
verbatim: "I rule O-B, the enumerated OPEN surface exactly as listed (i)–(iv),
under the agent person's RBAC, is_admin=0").

## Decision to rule

Whether to adopt, as the sixth §16 import contract and its agent path:

1. the **`tracker` contract** defined below (columns, vocabulary, target
   record family, idempotency/update semantics, anchor semantics), grounded in
   the observed structure of the owner's tracker.xlsx;
2. the **pathway**: proposal-shaped, through the shipped import-proposal seam,
   exactly like the other five contracts (D-PEC-12 semantics; no new operation
   family);
3. the **implementation structure**: whether the source tranche that ships the
   contract rides this row's ruling as an explicit authorization (O-A) or is
   its own successor row (O-B). This packet authorizes **no implementation by
   itself** — under O-A the *ruling* is the authorization act, with the fence,
   tests, verification plan, and rollback plan pinned below; under O-B that
   act stays separate (D-PEC-08 / D-PEC-16→D-PEC-17 precedent); and
4. **capture limits for tracker.xlsx** (requested owner line): tracker.xlsx is
   a materially new data source outside the D-PEC-01 owner enumeration; the
   ruling may state its capture limits going forward (what, if anything,
   beyond manifests/hashes/counts/shape patterns may be committed or shown in
   evidence). Absent an owner statement, the strictest standing reading
   governs: the gitignore ruling's "manifests/hashes only" grain — which is
   the grain this packet itself uses.

## The shipped mechanical harness (verified facts)

| Fact | Source |
|---|---|
| Exactly five §16 contracts exist: `mdl`, `rail`, `decisions`, `risks`, `schedule`; unknown contract names are refused. | `server/src/import/index.ts:493-502` |
| The proposal seam (propose / list / get / refresh / accept / reject / apply; hash+version-bound acceptance; transaction-atomic apply; 409 `STALE_PROPOSAL` staleness refusal) is contract-generic **below a five-contract allowlist gate**: `const CONTRACTS = ['mdl', 'rail', 'decisions', 'risks', 'schedule'] as const` at `server/src/services/proposals.ts:22`, and `createProposal` refuses any other contract name (`badRequest('unknown import contract: …')`) **before** dispatching into the generic `importContract` layer — a `?contract=tracker` proposal would 400 today. A sixth contract therefore needs a one-line CONTRACTS extension (the refusal-message text follows the array) in addition to the `importContract` case. | `server/src/api.ts:339-368`; `server/src/services/proposals.ts:22,88-90`; D-PEC-08 (PR #82) |
| Idempotency pattern of record: an external key column is stored verbatim as the record ref/key; re-import matches it and updates in place; a record edited in-app since its last import is a conflict unless `force=true` (human-only). | `server/src/import/index.ts:61-67,107-121,196-211,341-355,406-421` |
| Schedule precedent for import-owned records: "schedule rows are import-owned (no in-app edit path); re-import always refreshes" — no conflict guard needed where no in-app edit path exists. | `server/src/import/index.ts:477-481` |
| Anchor precedent (schedule): an optional stated `package` mapping column must resolve to an existing `package.code` or the row rejects — "silently dropping it would be a silent drop of data (§16)". | `server/src/import/index.ts:454-460` |
| The `package` record is thin: `code`, `name`, `leadId`, `description`, `milestone` (+version). It has **no slots** for procurement stages, vendors, package type, line items, or area. Packages auto-created by MDL import carry `code = name = <MDL Package ID>`. | `core/src/types.ts:134-143`; `server/src/db.ts:71-81`; `server/src/import/index.ts:98-105` |
| Exports mirror imports for round-trip (§16); the register-export switch is where a `tracker` export case would live, and the export HTTP route is already register-generic (`GET /api/projects/:pid/export/:register` → `exportRegister`) — no route change needed for export. | `server/src/import/index.ts:504-689`; `server/src/api.ts:324-326` |
| The repo layer needs **no registration for a new table** (checked explicitly at the verification lens's request): `repo.insert`/`get`/`list` take table names directly (`server/src/repo.ts:118-135`); the `TABLE` map's only consumer **in the repo layer** is a reverse lookup with an identity fallback (`repo.ts:159`); the service-layer consumers of `TABLE` (decision/hold/plan record-type→table lookups in `services/{decisions,holds,plan}.ts`) never target `package_tracker` in this contract's scope. The snapshot builder enumerates tables explicitly (`repo.ts:275-291`), so this contract's export/view read the table directly via `repo.list` and stay out of the snapshot (design pinned in the fence). `core/src/snapshot-index.ts` memoizes hold/work-item structural lookups only — untouched. | `server/src/repo.ts:24-33,118-135,159,275-291`; `core/src/snapshot-index.ts:1-17` |
| Register views are JSON routes in `api.ts` backed by `server/src/services/views.ts`, fetched by `web/src/pages/Registers.tsx` (e.g. `GET /api/projects/:pid/risks` → `views.riskRegisterView`). The Admin page's contract dropdowns are a module-level five-entry `CONTRACTS` list feeding both the proposal select and the direct-import select, plus an `EXPORTS` list. | `server/src/api.ts:249-273`; `web/src/pages/Registers.tsx:17-45`; `web/src/pages/Admin.tsx:107,224-230,271,344-355` |
| Agent RBAC: `import.propose` covers admin/pm/coordinator/document_controller; `import.accept` (accept/apply) is admin-only; the agent person is provisioned `is_admin=0` (D-PEC-10 WF-8; D-T0-20 O-B). | `core/src/permissions.ts:225` (import.propose), `core/src/permissions.ts:229-231` (import.accept); D-PEC-10 riders |

## Observed structure of tracker.xlsx (read-only analysis, 2026-07-06)

Reported at the evidence-manifest grain (header names, shape patterns, counts,
distributions, row coordinates; no verbatim cell content — see the capture
note above; the file is identified by the SHA-256 in "Why this row exists").

One sheet: `Package Summary`. Header row 1; used range A1:Y149; **65 data
rows** (rows 2–66; rows 67–149 are fully empty formatting rows; no row has
data without a tracking number). All populated cells are strings (no date or
numeric cells anywhere). Column inventory, verbatim, in sheet order:

```
CoA Tracking Number | Package # | Discipline | Package Name |
Approved Package Type (per TOU)? | Proposed Package Type for TOU |
Line Items | Area | Cost Estimate $CAD (2026) | Comments |
Vendor(s) Engaged | Vendor Awarded | Expected Delivery Date |
Budgetary Datasheet | Cost Estimate | Package Datasheet | Package | RFQ |
Review | Vendor Bids | Clarifications | Evaluation | Eng. Req. | PO | Databook
```

Population and shapes (of 65 rows):

- **`CoA Tracking Number`** — 65/65, all matching the shape pattern
  `26020-NN-PT-NN-NNN`. **The natural idempotency key** — but observed 64
  distinct values: one tracking-number value appears twice, on sheet rows 16
  and 54, which are two different packages (different names, line items, and
  vendors) — a workbook data defect the contract must surface, never absorb
  (see duplicate handling below).
- **`Package #`** — 0/65 populated. It cannot serve as key or link today. ⚑
- **`Discipline`** — 65/65: Mechanical (55), Electrical (10).
- **`Package Name`** — 65/65, free text (equipment/unit package names).
- **`Approved Package Type (per TOU)?`** — 65/65, mixed semantics: either the
  literal `No` or an upper-case equipment-type string; some values carry
  trailing newlines. Carried verbatim (trimmed). ⚑
- **`Proposed Package Type for TOU`** — 65/65, an upper-case equipment-type
  vocabulary (short type strings).
- **`Line Items`** — 65/65, free text, frequently multi-line
  (newline-separated equipment items).
- **`Area`** — 65/65: three area labels of the form `N-NN (<name>)` — the
  same three project areas the committed `IMPORT_TEMPLATES/IMPORT_MAPPING.md`
  already carries for the MDL/RAIL basis; distribution 41 / 12 / 12.
- **`Cost Estimate $CAD (2026)`**, **`Vendor Awarded`**,
  **`Expected Delivery Date`** — 0/65 populated (scaffolded, not yet used).
- **`Comments`** — 12/65, free text; today it carries expected-delivery
  information as short prose (month-and-day phrases) rather than the date
  column. ⚑
- **`Vendor(s) Engaged`** — 55/65, newline-separated lists of one to three
  vendor names; the literal `-` used as an explicit "none" marker.
- **The 12 stage columns** (`Budgetary Datasheet` → `Databook`) — 65/65 each,
  a procurement-stage pipeline with observed vocabulary
  `Not Started`, `In Progress`, `Complete`, `Issued`, `Not Applicable`:
  Budgetary Datasheet {Issued 42, Not Applicable 23}; Cost Estimate
  {Complete 60, In Progress 5}; Package Datasheet {Not Started 62,
  Not Applicable 3}; the remaining nine stages are `Not Started` on all 65
  rows (early-lifecycle tracker).

**Relationship to existing records (measured):** the app's `package` records
were auto-created by the MDL import keyed on the MDL workbook's `Package ID`
(shape `26020-PKG-NNN`, 142 distinct) — a **different keyspace** from the CoA
tracking numbers, so the tracker key can never collide with or match an
existing `package.code`. Cross-workbook name comparison: 54/65 tracker
`Package Name` values match exactly one MDL `Package ID` by exact
case-insensitive name; 0 are ambiguous; 11 match nothing (predominantly the
Electrical-discipline building rows plus a few Mechanical ones). Name
resolution is therefore an **agent-side mapping step at CSV-authoring time**
(workbook-to-workbook), not a server-side lookup — in the DB the MDL-created
packages carry `name = code`, so a server-side name match would find nothing
(`server/src/import/index.ts:102`).

**Can this support a §16 contract as-is?** Yes, with one stated defect: the
key column exists, is well-formed, and is unique except for the one duplicated
value above. No silent scope trim is needed; the duplicate is handled by
contract semantics (below) and reported to the owner as a residual workbook
data gap (the `IMPORT_MAPPING.md` "Residual workbook data gaps" pattern).

## The proposed `tracker` contract (§16 style)

**What it is NOT (the own-row demand honored):** not an MDL mapping. The
tracker's rows are procurement packages with a 12-stage pipeline; the
`package` record has no slots for any of it, and `deliverable` rows are the
wrong grain. Folding stages into `package.description` or MDL `remarks` would
be exactly the "awkward MDL mapping" the owner's direction item 2(a) forbade.

**Risk class: `engine_checkable` by construction** (the D-PEC-12 §2 class the
five ruled contracts carry): every validation is deterministic — required
columns, closed stage vocabulary, `YYYY-MM-DD` date check, key uniqueness,
anchor resolution — and the dry-run is the live contract itself executed in a
rolled-back savepoint (`server/src/services/proposals.ts:76-84`), never a
reimplementation.

**Target record family: a new first-class `package_tracker` record** — one row
per tracked procurement package, import-owned (schedule precedent):

- `trackingNo` (unique per project — the idempotency key, stored verbatim),
  `packageName`, `discipline`, `area`, `packageTypeApproved`,
  `packageTypeProposed`, `lineItems`, `vendorsEngaged`, `vendorAwarded`,
  `expectedDeliveryDate` (date, nullable), `costEstimateCad` (nullable),
  `comments`, twelve stage fields (below), `packageId` (nullable FK →
  `package` — an enrichment link, not a requirement), `version`.
- Stage fields: `stageBudgetaryDatasheet`, `stageCostEstimate`,
  `stagePackageDatasheet`, `stagePackage`, `stageRfq`, `stageReview`,
  `stageVendorBids`, `stageClarifications`, `stageEvaluation`, `stageEngReq`,
  `stagePo`, `stageDatabook` — shared vocabulary `not_started`, `in_progress`,
  `complete`, `issued`, `not_applicable` (import normalizes case/spaces, the
  `normState` convention); blank stored null; an unrecognized stage value
  rejects the row (never silently coerced).

**CSV contract columns** (snake_case; the contract is CSV like the other five —
xlsx never enters the server, see Constraints):

| Column | Required | Notes |
|---|---|---|
| `tracking_no` | header✱ + row✱ | idempotency key, stored verbatim |
| `package_name` | header✱ + row✱ | |
| `discipline`, `area` | header✱ | row-optional |
| `stage_budgetary_datasheet` … `stage_databook` (12) | header✱ | row-optional; vocabulary above |
| `package_type_approved`, `package_type_proposed`, `line_items`, `vendors_engaged`, `vendor_awarded`, `comments` | optional | free text |
| `expected_delivery_date` | optional | `YYYY-MM-DD` or reject |
| `cost_estimate_cad` | optional | |
| `package` | optional | a stated `package.code` anchor **must resolve** or the row rejects (schedule precedent, `import/index.ts:454-460`) |

**Idempotency / update semantics:** re-import matches on `tracking_no` and
updates in place — `package_tracker` rows are **import-owned with no in-app
edit path in this scope** (the schedule precedent verbatim: "re-import always
refreshes"), so weekly v2 drops update rather than duplicate, and no
conflict-guard interplay arises. ⚑ If the owner later wants targeted in-app
tracker edits ("targeted changes within the current screen"), that adds an
edit act + the `lastChangeIsImport` conflict guard; per the residual-row
convention this trim is not left silent — the O-A/O-B mechanism **opens a
named register row** (tracker in-app edit path, NOT_PREPARED) on ruling.

**Within-file duplicate keys:** the first occurrence of a `tracking_no` wins;
every subsequent occurrence in the same file lands in the report as a
**conflict** (`duplicate tracking_no in file`), never applied, never silent.
The observed duplicate (sheet rows 16/54) will surface on the first real run
exactly this way; owner-side fix recommended (residual data gap).

**Anchor / intake-fallback semantics (deliberate divergence from RAIL, with
rationale):** rows that cannot be anchored to a `package` record do **NOT**
land as intake items. RAIL's intake fallback exists because unanchorable RAIL
rows are action-like statements that need triage; tracker rows are self-keyed
**register rows** — the `package_tracker` record itself is created regardless,
with `packageId` null when no anchor is stated. Burying a register row in the
triage queue would misfile it. Unlinked rows are visible in the register view
and countable in the report; `intakeCreated` stays 0 for this contract by
construction. Anchoring is enrichment: the agent's mapping resolves tracker
`Package Name` → MDL `Package ID` → `package.code` where the match is unique
(observed 54/65 today) and leaves `package` blank otherwise (11/65). ⚑

**Export round-trip:** a `tracker` register export mirroring the import
columns exactly (§16 round-trip), added to the `exportRegister` switch; the
HTTP route is already generic (`api.ts:324-326`).

## Workbook → template mapping (the observed 2026-07-05 tracker.xlsx)

Agent-side mapping at CSV-authoring time (sheet `Package Summary`, header
row 1, 65 data rows → 65 mapped):

| §16 column | Source | Note |
|---|---|---|
| tracking_no | CoA Tracking Number | key; 64 distinct / 65 rows — the duplicate surfaces as a conflict |
| package_name | Package Name | |
| discipline | Discipline | |
| area | Area | |
| package_type_approved | Approved Package Type (per TOU)? | trimmed; mixed `No`/type-string semantics carried verbatim ⚑ |
| package_type_proposed | Proposed Package Type for TOU | trimmed |
| line_items | Line Items | newline → `; ` join |
| vendors_engaged | Vendor(s) Engaged | newline → `; ` join; `-` → blank ⚑ |
| vendor_awarded | Vendor Awarded | empty in workbook today |
| expected_delivery_date | Expected Delivery Date | empty today; must be `YYYY-MM-DD` when populated |
| cost_estimate_cad | Cost Estimate $CAD (2026) | empty today |
| comments | Comments | 12/65; carries prose dates today ⚑ |
| stage_* (12) | Budgetary Datasheet … Databook | vocabulary normalized (`Not Started`→`not_started`, etc.) |
| package | — (derived) | unique-name resolution via the MDL workbook, 54/65; blank otherwise ⚑ |
| — | Package # | 0/65 populated; unmapped until the owner populates it ⚑ |

On ruling (O-A or O-B), a `tracker-template.csv` and this mapping table land
in `../IMPORT_TEMPLATES/` (IMPORT_MAPPING §tracker), the same convention as
the other five.

## The agent path (pathway half of the decision)

Identical in shape to the five ruled contracts — no new operation family, no
new authority:

- The agent (own person record, `is_admin=0`, `coordinator` role — the
  D-PEC-10 WF-8 actor basis) reads the owner-dropped tracker file (D-T0-20 O-B
  item (iv)), authors the CSV mapping, files
  `POST /api/projects/:pid/import-proposals?contract=tracker`, runs/refreshes
  the dry-run, authors the governance mirror artifact, and may withdraw its
  own proposals (D-PEC-12 §3 as amended — full agency inside the mechanical
  harnesses).
- Accept (hash+version echo), apply, `force`, and reject-any remain human
  screen acts per shipped RBAC (`import.accept` admin-only) — unchanged by
  this row.

**Sixth-contract L3 scope, resolved by this row.** The tier-0 decision line is
quoted verbatim
(`_DomainEngines/_DECISIONS/D-T0-18_pec_l3_operation_proposal_advance.md`):

> Whether to advance PEC's ruled staging destination from L2 to L3 —
> `integration_level: OPERATION_PROPOSAL` in the schema's vocabulary — scoped
> initially to the §16 import-contract family through the `import_proposal`
> seam, with semantics fixed by the companion pec-local packet `D-PEC-12`.

A reading exists on which extending the contract enumeration requires a fresh
tier-0 ruling, because D-T0-18 "fixed" semantics by delegating to D-PEC-12,
whose §2 enumerates five contracts "and nothing else." That reading is
disposed of on two grounds, both the owner's own acts:

1. **The full-agency amendment demoted the enumeration to convention.** The
   D-PEC-12 ruling's recorded interpretation (the amendment text governs)
   states: "Sections 1, 2, 4, 5, and 6 of the proposed semantics stand as
   working conventions, not as new authority constraints" — the binding gates
   are the mechanical harnesses. §2's five-contract list is therefore a
   convention whose extension needs an own row, not a tier-0 authority
   boundary. D-T0-18's own scope words — "the §16 import-contract family" —
   name the family, not a closed five-member list.
2. **The owner designated this pec-local row as the venue.** The D-PEC-10 O-A
   ruling adopted WF-5 with its discharge path verbatim: "PARKED by
   construction → new register row opened on ruling (contract design; carries
   its own L3-scope question — the ruled scope is imports per D-T0-18 O-A, and
   D-PEC-12 §2 states it as 'The five §16 import contracts … and nothing else.
   Any other operation family needs its own row.')" — and the register row the
   owner's ruling opened reads: Carries the sixth-contract L3-scope question
   (D-PEC-12 §2: "Any other operation family needs its own row."). The
   question was routed here, by ruling.

Conclusion: a sixth *contract* stays inside the ruled **imports** operation
family — no new operation family opens, no `integration_level` change is
claimed — and this packet is the own row that extends the pec-local
enumeration from five to six. The D-PEC-12 packet is not reopened or edited
(residual-row convention); the extension is recorded here and, on ruling, in
the profile note (see the profile fence-note below).

## Implementation (what shipping the contract requires — NOT authorized by this packet itself)

A source tranche under `projects/pec/{server,core,web}/**` — the F-PEC-1 fence
is absolute and only an explicitly ruled tranche opens it. Under O-A the
ruling of this row is that act, bounded by this fence; under O-B this section
is carried into the successor row's packet. **The tranche packet authored
under either option may not widen this fence** — any needed widening comes
back to the owner as its own row.

**Tranche fence (exact file list; anything outside it is out of scope):**

- `projects/pec/core/src/types.ts` (+ `core/src/index.ts` re-export if the
  export list is explicit): `PackageTracker` interface; `'package_tracker'`
  added to the record-type enumeration (`types.ts:12-23`). The
  `ProjectSnapshot` interface is **not** touched: the export and the register
  view read the table directly via the table-name-generic `repo.list`
  (design pinned — verified facts row above). `core/src/snapshot-index.ts` is
  **not** touched (it memoizes hold/work-item structural lookups only).
  `server/src/repo.ts` is **not** touched (insert/get/list are
  table-name-generic; no registration needed — checked, see the verified
  facts). No permission change, no new act family (import-owned record; the
  import path runs under the existing `import.propose`/`import.accept` acts).
- `projects/pec/server/src/db.ts`: additive `package_tracker` table
  (`UNIQUE(project_id, tracking_no)`).
- `projects/pec/server/src/import/index.ts`: `importTracker` (validation,
  duplicate-in-file conflict, stated-anchor-must-resolve, always-refresh
  update); `tracker` case in `importContract`; `tracker` case in
  `exportRegister` (round-trip, direct table read).
- `projects/pec/server/src/services/proposals.ts`: the one-line `CONTRACTS`
  allowlist extension (`proposals.ts:22`; the refusal-message text follows the
  array) — without it every `?contract=tracker` proposal is refused 400
  before dispatch.
- `projects/pec/server/src/services/views.ts`: `trackerRegisterView` (JSON
  register view, the `riskRegisterView` pattern).
- `projects/pec/server/src/api.ts`: exactly one new read-only route,
  `GET /api/projects/:pid/tracker` → `views.trackerRegisterView` (authed,
  project visibility — the `api.ts:249-273` register-route pattern). The
  proposal routes and the export route need **no** change (both dispatch
  generically once the allowlist and switch cases above exist).
- `projects/pec/web/src/pages/Registers.tsx`: a Tracker tab fetching the new
  route (read-only table; no mutation controls — the register stays
  import-owned).
- `projects/pec/web/src/pages/Admin.tsx`: the module-level five-entry
  `CONTRACTS` dropdown list (`Admin.tsx:224-230`, feeding both the proposal
  select and the direct-import select) gains the `tracker` entry; the
  `EXPORTS` list (`Admin.tsx:344-355`) gains `tracker`.
- `projects/pec/server/test/import-tracker.test.ts` (+ a proposal-path test
  pinning `contract=tracker`, including the allowlist acceptance): synthetic
  fixtures only; v1+v2 idempotency, duplicate-key conflict, vocabulary
  rejection, anchor resolution/rejection, round-trip export.
- Coordination (not source): `tracker-template.csv` + IMPORT_MAPPING §tracker.
- **Zero new dependencies** (ADR-002 / F-PEC-3); no root-manifest change; no
  lifecycle/state-machine addition (stage values are plain fields, not
  lifecycle states — no I-5 gate interaction).

**Profile fence-note (stated loudly for the owner — the D-PEC-17
opening-of-record pattern):** the sixth-contract note belongs in the ADOPTED
`_DomainEngines/profiles/pec.yaml` (the `deterministic_tools` `import.csv`
entry, `pec.yaml:117-121`, currently enumerating five contracts). F-PEC-4's
literal allowlist ("tier-0 writes only under `_DomainEngines/pec/**` and
`_DomainEngines/proposals/pec/**`") does not include `profiles/pec.yaml`, and
prior edits to that file rode explicitly opened mechanisms — tier-0 rulings
D-T0-16 (location), D-T0-12 (Gate-2 adoption), D-T0-18, and D-T0-19/20, plus
one DRAFT-era open-issue annotation riding the pec-local D-PEC-01 basis.
**Ruling O-A (or the O-B successor ruling) is therefore
asked to open exactly this one edit:** the `import.csv` note line gains the
sixth contract (and nothing else in the file changes), with the profile
validator re-run merge-gating in the same PR and the opening recorded in the
receipt as an opening of record. If the owner prefers the strict routing
instead, the alternative is a tier-0 pointer/residual row carrying the same
one-line edit — state the choice in the ruling.

**Verification plan (workplan step-4 checks, at the tranche PR's final SHA):**

- pec belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill` — all green, including the new import-tracker and
  proposal-path tests.
- Repo self-check with no unexplained baseline shift; full `tools/` pytest.
- coord-check on the committed range; `git diff --check`.
- **Adversarial scope check:** `git diff --name-only` on the tranche commits
  is a subset of the pinned fence above plus exactly these coordination
  surfaces: the `TRANCHE_` packet, this packet's ruling-section update, the
  register-row flip, `IMPORT_TEMPLATES/{tracker-template.csv,IMPORT_MAPPING.md}`,
  the receipt, the evidence snapshot dir + proposals mirror, and — only if
  the ruling opens it — the one profile-note row + its validation report.
  Any excess file fails the tranche.
- Profile validator re-run (merge-gating) if the profile-note edit rides.
- CI green on the PR; owner merge is the gate (see the self-merge rider in
  the mechanism).

**Rollback plan (D-PEC-08 grade):** branch-first
(`codex/pec-dpec13-tracker`); the PR is the unit of revert — one
`git revert` of the merge commit restores the prior surface. The
`package_tracker` table is additive and inert when unreferenced (no existing
code path reads it; no migration of existing data; drill/backup surface
unchanged — the SQLite backup copies the whole DB file regardless of table
set). The allowlist, view, route, and dropdown entries revert with the same
commit; no data written under the contract survives on a scratch basis
(scratch DBs are deleted after capture).

**Evidence convention (tranche verification bar):** immutable
`PEC_<date>_DPEC13-evidence-01/` per the L3-evidence convention — **synthetic**
tracker CSV (v1 + edited v2) through the live proposal seam on a fresh scratch
DB: propose → dry-run → accept → apply; v2 update-in-place counts; one
duplicate-key conflict exercised; one stated-anchor rejection exercised; an
**export-and-compare round-trip step** (export the `tracker` register and
compare against the applied v2 — the D-PEC-12 §5 convention); the
**governance mirror artifact** authored per agent-initiated proposal under
`_DomainEngines/proposals/pec/` citing the `IPR-` ref and source SHA-256
(D-PEC-12 §1 — mirror only, confers no authority); demo-cast admin
accept/apply disclosed per act with `force: false` (never true); manifest
with SHA-256s; scratch DB deleted after capture. The **real** tracker.xlsx
run on the pilot-scratch instance is then lawful (D-T0-20 O-B item (iv)
visibility; owner-clarified scratch/demo mutation basis) but its captured
artifacts follow the capture limits of Decision-to-rule item 4: count-level
results in the receipt, no verbatim real rows committed to the repo.

**WF-5 discharge condition:** the governing bar is D-PEC-10 direction item 3
(owner, verbatim): "Code landing alone does not discharge the intent; the
rehearsed instance does." WF-5 therefore discharges only when (a) the
`tracker` contract is shipped under a ruled tranche AND (b) a live
proposal-path evidence run (v1 + edited v2, idempotent update-in-place) is
captured. (The unruled sibling row D-PEC-14 proposes the same shape of bar
for WF-3/WF-4 — cited as a shape pointer only, not authority.) Design
adoption alone (O-B before its tranche rules) leaves WF-5 parked, stated
plainly in the register.

## Constraints (bind any ruled option)

- **F-PEC-1..4 unchanged.** This packet writes nothing under
  `projects/pec/{server,core,web,tools,fixtures}/**` and authorizes nothing by
  itself; only a ruled tranche (O-A's ruling, or O-B's successor row) opens
  source scope, bounded by the exact fence above; the profile-note edit is
  opened only by the explicit fence-note mechanism above, or not at all.
- **ADR-002 zero-dep server intact:** no xlsx parser or any other dependency
  enters pec. The contract is CSV; xlsx→CSV mapping is performed agent-side at
  proposal-authoring time (exactly how the 2026-07-05 workbook runs were
  done), from the owner-dropped file the agent may lawfully read.
- **Mutation basis unchanged:** scratch/demo only (the pilot-scratch instance
  is within it per the D-T0-20 ruling's clarity sentence); agent operation
  against the owner's real/non-scratch DB remains its own future row.
- **Accept, apply, and `force` are human acts** per shipped RBAC; no agent run
  ever sets `force=true`; demo-cast accept/apply in evidence is disclosed per
  act (Receipt 34/35 convention).
- **D-T0-20 O-B visibility bounds:** agent reads exactly the enumerated
  surface — here items (ii) proposal records/reports and (iv) owner-dropped
  weekly files — under the agent person's RBAC, `is_admin=0`; everything
  unenumerated stays CLOSED; egress only to the owner-configured provider.
  Visibility is distinct from **capture**: what may be committed from
  tracker.xlsx is governed by Decision-to-rule item 4.
- **No record-state invention** (F-PEC-2); no pilot-readiness, go-live, or
  issuance claim; imported stage values are plain imported fields, not
  lifecycle assertions.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | **Adopt the `tracker` contract + agent path as specified, AND authorize the implementation tranche in the same ruling** (exact fence + tests + verification plan + rollback plan pinned above; the ruling is the explicit F-PEC-1-opening act — and, if the owner so states, the explicit opener of the one profile-note row — D-PEC-08 mechanism with the tranche detail folded per the D-PEC-17 precedent). | One owner gate covers design and implementation; a `TRANCHE_<date>_D-PEC-13_tracker_contract_v1.md` packet is authored before any source change and may not widen the fence; WF-5 becomes dischargeable this cycle (contract + live evidence); the weekly five-document workflow reaches its last missing contract. |
| O-B | **Adopt the contract + agent path design only; the source tranche is its own successor row** (opened NOT_PREPARED on ruling, next-free ID — the D-PEC-16 → D-PEC-17 two-gate precedent). | Design of record now; implementation waits for a second gate with packaging facts in front of the owner; WF-5 stays parked pending that row, stated in the register. |
| O-C | **Defer.** | The row stays open; the Package Tracker half of the ruled weekly workflow remains without a path; WF-5 stays parked; the owner-dropped tracker.xlsx has no in-app destination. |

## Recommendation (non-binding)

**O-A.** Reasons: (1) the contract is fully specified against observed data —
the key column exists and is well-formed, every mapping decision above is
grounded in the actual file, and the one data defect (the duplicated tracking
number) is handled by contract semantics rather than blocking; (2) the
implementation is small, additive, and fully pinned — one table, one import
function, one export case, one view + route, a one-line proposal-allowlist
extension (the seam is generic below that allowlist, so this is the only seam
change), two dropdown entries, zero dependencies, no permission or lifecycle
change — so a second design gate between this ruling and that tranche would
gate nothing the fence above does not already pin; (3) the ruled priority is
a useful agent on the owner's weekly cycle, and this is the last of the five
named documents without a path. O-B is the sound choice if the owner wants
the two-act separation D-PEC-16/17 used, or wants to fix the workbook
duplicate and populate the workbook's `Package #` column before committing to
the key semantics.

## On ruling (mechanism)

- **O-A:** record the ruling verbatim here; flip the register row
  AWAITING_RULING → RULED. Author
  `../TRANCHE_2026-07-XX_D-PEC-13_tracker_contract_v1.md` pinning this
  packet's fence (no widening) before any source change; execute
  branch-first; land `tracker-template.csv` + IMPORT_MAPPING §tracker with
  the tranche PR, and the one profile-note row + validator re-run only if the
  ruling opens it (profile fence-note above); run the full verification plan
  at the final SHA; capture `PEC_<date>_DPEC13-evidence-01/` per the evidence
  convention (round-trip compare + governance mirror included); report the
  duplicated tracking-number defect (sheet rows 16/54) to the owner as a
  residual workbook data gap; **open the residual register row** "tracker
  in-app edit path" (NOT_PREPARED) per the residual-row convention; record
  WF-5 as DISCHARGED in the receipt only when both discharge conditions hold;
  append the receipt; STOP at owner merge — unless a standing owner
  authorization in force at execution time covers self-merge, in which case
  that authorization is **quoted verbatim in the receipt that relies on it**
  (the Receipt-32 self-quoting pattern) and its full check set is green.
- **O-B:** flip the row RULED (design adopted, verbatim ruling recorded); open
  the successor source-tranche row NOT_PREPARED (next-free D-PEC ID) carrying
  the §Implementation fence unwidened, and the residual "tracker in-app edit
  path" row alongside it; the duplicated tracking-number defect (sheet rows
  16/54) is reported to the owner as a residual workbook data gap the same
  way as under O-A; no source change under this row; WF-5 remains
  PARKED (register-visible) pending the successor ruling.
- **O-C:** the row records the deferral verbatim; no execution; the decision
  slate returns whenever the owner reopens it.
- Under any option the owner may add the Decision-to-rule item-4
  capture-limits line for tracker.xlsx; absent it, the manifests/hashes-only
  grain governs.
- Any owner amendment is recorded verbatim and governs over this packet's
  prose (the D-PEC-12 convention).

## Human ruling

**Ruling (owner, Ryan Tufts, 2026-07-06, in-session, verbatim):**

> Proceed with 1. Rule D-PEC-13 as follows. Use the tracker.xlsx provided as
> your template and proceed accordingly.

— where "1." is this packet as presented first on the session decision slate,
with recommendation O-A.

**Recorded interpretation (the ruling text governs on any disagreement):**
the recommended option **O-A** is affirmed — the `tracker` contract and agent
path are adopted with the owner-provided tracker.xlsx as the template basis
(exactly this packet's workbook → template mapping), and the implementation
tranche is authorized in the same ruling, bounded by the pinned fence. Two
in-packet defaults stand because the ruling does not state otherwise:

1. **Profile fence-note:** the ruling does not open the one profile-note edit
   (the fence-note required the choice to be stated in the ruling), so
   `_DomainEngines/profiles/pec.yaml` is NOT touched by this tranche; the
   one-line sixth-contract note remains pending its own explicit opener
   (owner ruling line or tier-0 pointer/residual row) and is recorded as a
   parked residual in the receipt.
2. **Capture limits (Decision-to-rule item 4):** no capture-limits line was
   stated, so the strictest standing reading governs — manifests/hashes-only
   grain for all tracker.xlsx-derived captures (committed evidence uses
   synthetic fixtures; the real-run capture is count-level + hashes).

**Ruling SHA:** received with `main` at `c4e00afbb` (immediately after the
owner-directed PR #93/#94 merges).

**Status change:** AWAITING_RULING → RULED (register row flipped in the same
commit).

**Owner amendment (2026-07-06, in-session, Ryan Tufts, verbatim — governs
over this packet's prose per the amendment clause in "On ruling
(mechanism)" above):**

> You should match the tracker entries with the PKG-#### numbers we're using.
> Keep the CoA number but don't key on that.

**Recorded interpretation of the amendment:** the idempotency key of the
`tracker` contract changes from `tracking_no` (the CoA number) to the
project's package identifiers (`package.code`, the MDL-created
`26020-PKG-NNN` universe) — i.e. the `package` column becomes the
row-required key and must resolve to an existing `package` record
(anchor-must-resolve, already ruled); one tracker row per package
(`UNIQUE(project_id, package_id)`); re-import matches on the package and
updates in place. `tracking_no` is retained verbatim as a plain data field —
optional, non-unique, never a conflict source. Direct consequences, stated
for the record: (1) the duplicated CoA value (workbook rows 16/54) stops
being an import defect — both rows key on their distinct packages and both
land; (2) workbook rows whose Package Name resolves to no `package` record
(11/65 observed) reject as owner-side data gaps until mapped (§16
never-silently-drop) — listed count-level in evidence; (3) within-file
duplicate semantics move to the package key (first valid occurrence wins;
later ones report as conflicts). Executed as an amendment revision inside
the same ruled tranche fence, evidenced by
`PEC_2026-07-06_DPEC13-evidence-02/`; evidence-01 remains the honest record
of the pre-amendment run.
