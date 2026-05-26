# Procedure — DEL-089-02 Package Datasheet

> Operational procedure to (a) produce the Package Datasheet artifact for the Pig Receivers (Inlet) 3-25 package, and (b) use it as the basis for the downstream vendor-engineering handoff. Steps reference Specification REQ-* and Guidance CFT-* identifiers.

## Purpose

`FACT` Produce a vendor-ready Package Datasheet for `PKG-089` that is source-grounded, interface-complete, and traceable to SOW-0157..0160 and the 3-25 DBM. The completed datasheet is the binding input to `DEL-089-04` (Vendor Engineered Equipment Package).

## Prerequisites

| Item | Source / Reference |
|---|---|
| Accepted `DEL-089-01_scope-of-work` (or its draft equivalent) | `_DEPENDENCIES.md` declares no upstream edges yet; `ASSUMPTION` — `DEL-089-01` is a peer that should be referenced when issued |
| Access to `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | This deliverable's `_REFERENCES.md` (Shared Source Root) |
| Access to `_Decomposition/.../GATE-07_Final_Published_2026-05-24/` registers (SCOPE_LEDGER, INTERFACE_REGISTER, DELIVERABLE_REGISTER, OBJECTIVE_REGISTER) | `_REFERENCES.md` |
| Access to `_Sources/26020-Package_Requirements.docx` (package heading 42) — currently `location TBD` in markdown form | `_REFERENCES.md`; CFT-04 |
| Pending human rulings on CFT-01, CFT-02, CFT-03, CFT-04 | `Guidance.md` Conflict Table |

## Steps

### Step 1 — Confirm Identification

Populate Datasheet §Identification from `_CONTEXT.md`. Verify Package ID, Workbook row, and Source Document Anchor against `DELIVERABLE_REGISTER.csv` row for `DEL-089-02`.

### Step 2 — Lift Source-Grounded Attributes

For each row of SOW-0158, SOW-0159, SOW-0160, write a corresponding Datasheet §Attributes row with the source ID. Where the source is silent, mark `TBD`. Do not invent values.

### Step 3 — Resolve Pressure and Temperature Envelopes (REQ-4, REQ-5)

Copy operating and design pressures, MAOP, MAWP, and ambient envelopes directly from SOW-0160 to Datasheet §Process Conditions and Specification §REQ-4 / §REQ-5. Cross-check against DBM §Inlet Pipeline Interface and Pigging (635 psig basis). Open CFT-03 if shutdown-pressure clarity is missing.

### Step 4 — Capture Sour-Service Basis (REQ-5.4, REQ-6.2)

Record the package H2S statement (0.1 mol%) from SOW-0159 and the DBM raw-gas H2S basis (0.3 mol% design / 2.0 mol% license). Raise CFT-02 in Guidance. Until ruled, design materials to the more restrictive license value as an `ASSUMPTION` documented in Specification §REQ-5.4.

### Step 5 — Enumerate Interfaces (REQ-7)

Pull the 10 PKG-089 rows from `INTERFACE_REGISTER.csv` into Datasheet §Interfaces and Specification §REQ-7. For each interface, document the directional responsibility and any By-Others scope (cross-check against SOW-0160).

### Step 6 — Capture Boundaries and By-Others Scope (REQ-8)

Write Datasheet §Boundaries from DBM §Inlet Pipeline Interface and Pigging (plant inlet boundary is the first aboveground flange within the lease boundary). Write the By-Others list verbatim from SOW-0160.

### Step 7 — Raise the Conflict Table

In `Guidance.md`, list each detected source disagreement with explicit Source A / Source B pointers, the impacted sections in this deliverable, and a `PROPOSAL` authority. Leave `Human ruling` as `TBD`.

### Step 8 — Verification Pre-Issue

Apply the Specification §Verification table checks against the draft Datasheet. Confirm:
- Every Datasheet attribute either cites a source or carries `TBD` / `ASSUMPTION`.
- Every Specification REQ-* line maps to a verification approach.
- Every interface row has a register ID.
- Every CFT row identifies impacted sections that exist in the current artifacts.

### Step 9 — Vendor Handoff (Downstream Use)

When issued, the Package Datasheet becomes the technical anchor for:
- `DEL-089-04` Vendor Engineered Equipment Package (engineering, design, fabrication/supply).
- `DEL-089-05` Vendor Document Turnover Package (submittal register).
- `DEL-089-06` EPC Vendor Package Review and Acceptance (integration review against this Datasheet and the Construction Work Package `DEL-089-03`).

Hand the deliverable to the Package Vendor with the Conflict Table open and call out the open CFT rulings as RFI items.

## Verification

| Verification Check | Mapped Requirement | Method |
|---|---|---|
| All §Attributes have a source or `TBD`/`ASSUMPTION` label | REQ-1..REQ-5 | Self-audit pre-issue |
| 10 PKG-089 interfaces present | REQ-7.1..REQ-7.10 | Diff against `INTERFACE_REGISTER.csv` filtered by `PKG-089` |
| Pressure envelope numerically consistent across Datasheet and Specification | REQ-4 | Cross-document numeric check (Pass 2) |
| H2S basis flagged as conflict | REQ-5.4, REQ-6.2 | CFT-02 present in `Guidance.md` |
| Receiver count flagged as conflict | REQ-1.1 | CFT-01 present in `Guidance.md` |
| By-Others list matches SOW-0160 verbatim | REQ-8, §Boundaries | Source comparison |
| Anticipated artifacts (per `_CONTEXT.md`) present in Specification §Documentation | REQ-9 | Self-audit |

## Records

The following records shall be produced and retained as evidence of completion:
- Issued `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` at `INITIALIZED` and onward states.
- `_run_records/TASK_RUN_*.md` for each four-documents pass.
- Open-CFT log (mirrored in `Guidance.md` Conflict Table). Closure of each CFT requires a human ruling row populated and the impacted artifact sections updated.
- Interface-control documents for REQ-7.1..REQ-7.10 (separate vendor/EPC artifacts), with each one back-referencing the corresponding `IFC-*` register ID.
- Vendor design-review minutes and the final issued Package Datasheet acceptance signature, captured under `DEL-089-06`.
