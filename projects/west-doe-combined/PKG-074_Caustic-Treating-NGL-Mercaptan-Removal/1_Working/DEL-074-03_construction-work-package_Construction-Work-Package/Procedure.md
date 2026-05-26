# Procedure — Construction Work Package (DEL-074-03)

> Operational procedure to **produce** the Construction Work Package artifact for PKG-074 (Caustic Treating — NGL Mercaptan Removal). The execution of the construction work itself is governed by the issued CWP and subordinate workface packages — not by this Procedure. This Procedure operationalizes `Specification.md` requirements R-CWP-1 through R-CWP-12.

## Purpose

Produce, review, and issue the Construction Work Package, the installation and tie-in workface plan, and the construction interface and turnover checklist for PKG-074, in a way that satisfies the requirements in `Specification.md` and respects the constraints in `Guidance.md`.

## Prerequisites

| Prerequisite | Source | Status |
|---|---|---|
| `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for `DEL-074-03` | This deliverable folder | Present |
| Accepted decomposition snapshot `GATE-07_Final_Published_2026-05-24` | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/` | Present |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-07 NGL mercaptan treating slices) | `_Sources/` | Present |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (winter / 03-25 incinerator co-location context) | `_Sources/` | Present |
| `26020-Package_Requirements.docx` package heading 28 (cited by decomposition) | `_Sources/` | Present as binary `.docx`; relevant slices not directly read in this run — `location TBD` until extracted |
| `DEL-074-02_package-datasheet` (technical datasheet content) | Sibling deliverable | TBD — peer deliverable not yet drafted |
| `DEL-074-04_vendor-engineered-equipment-package` (vendor engineered equipment package) | Sibling deliverable | TBD — vendor selection open per DBM |
| Process licensor selection | DBM § "Current-Scope NGL Mercaptan Treating" | TBD |
| HAZOP / SIL outputs (for ESD / F&G coverage) | Safety studies | TBD |

If `DEL-074-02` and `DEL-074-04` are not yet available, the CWP can be drafted at the equipment-basis level using DBM SEC-07 directly, with explicit `TBD` markers on data normally pulled from the datasheet and vendor package.

## Steps

### Step 1 — Read and pin authoritative inputs
1. Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
2. Open the `GATE-07_Final_Published_2026-05-24` `DELIVERABLE_REGISTER.csv` row 272 entry for `DEL-074-03` to confirm scope items, supported objectives, and source-reference row.
3. Read DBM SEC-07 "Current-Scope NGL Mercaptan Treating", "NGL Mercaptan Treating Equipment and Utilities", and "Incinerator Interface" sections in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
4. Extract the equipment list, design conditions, material constraints, tie-in inventory, and open `TBD` items.

Verification: a pinned, dated source reference list exists inside the working folder (see `Datasheet.md` "References" section).

### Step 2 — Assemble equipment and tie-in inventory
1. Build the equipment list per R-CWP-3 and `Datasheet.md`.
2. Build the tie-in inventory per R-CWP-5 and R-CWP-6. For each tie-in, record: source unit / package, destination unit / package, service, design conditions (pressure, temperature, fluid, blanket-gas isolation as applicable), tag (TBD where not yet assigned), and acceptance owner.

Verification: every tie-in identified in DBM SEC-07 § "Current-Scope NGL Mercaptan Treating" and § "Incinerator Interface" appears in the tie-in inventory.

### Step 3 — Draft the CWP narrative
1. Write the governing CWP narrative covering: package identity, construction scope, equipment list, building and materials constraints (R-CWP-4), cross-facility interface to the 03-25 incinerator (R-CWP-6), winter execution provisions (R-CWP-9), and inspection/testing approach (R-CWP-11).
2. Explicitly carry open items into a CWP "open items / TBD" section: process licensor selection, caustic concentration confirmation, MTU floor material, caustic tank material, safety-shower count and location, F&G/ESD detector lists, supplemental fuel-gas rate, shared-facility operational responsibility split with 03-25.

### Step 4 — Draft the installation and tie-in workface plan
1. Decompose the construction work into workface packages with prerequisite logic per R-CWP-8 (illustrative anchor sequence in `Datasheet.md` § "Construction Sequence Anchors").
2. Define each workface package by: scope, prerequisite logic, expected craft mix and crew size (TBD until EPC execution plan is finalized), winter / cold-weather provisions (R-CWP-9), and required inspections and tests.
3. Verify against R-CWP-8 that prerequisite logic enforces: MTU building enclosure before caustic equipment installation; tank foundations and erection before vapour tie-in; hydrotest before chemical introduction.

### Step 5 — Draft the construction interface and turnover checklist
1. For every tie-in from Step 2, generate a checklist row with construction completion, mechanical completion, and pre-commissioning sign-off lines (R-CWP-7).
2. Add safety-critical rows: safety-shower activation and control-room-alert verification; no-aluminum material verification at receipt and at install; SS cladding/strap verification in caustic exposure areas; F&G / ESD loop-check status; HAZOP / SIL action closure status.
3. Add documentation-handoff rows for `DEL-074-05_vendor-document-turnover-package` and `DEL-074-06_epc-vendor-package-review-and-acceptance`.

### Step 6 — Cross-reference QA
1. Cross-check equipment list, tie-in inventory, workface plan, and turnover checklist for consistent terminology, tag conventions, and values (see `Specification.md` Verification table).
2. Confirm that every `Specification.md` R-CWP-* requirement maps to at least one section of the CWP artifact set.
3. Confirm that all `TBD` items in `Datasheet.md` and `Specification.md` are mirrored in the CWP open-items register.

### Step 7 — Issue and register
1. Issue the CWP at the appropriate construction-issue revision in accordance with EPC document control (specific control standard `TBD`).
2. Register the CWP, workface plan, and turnover checklist in the project document register and link from `_REFERENCES.md` (update outside the four-document scope; not modified in this skill run).
3. Notify downstream consumers (`DEL-074-04`, `DEL-074-05`, `DEL-074-06`) of issue and any open items affecting their scope.

## Verification

| Step | Verification |
|---|---|
| 1 | Authoritative sources read and pinned (References section in `Datasheet.md`) |
| 2 | Tie-in inventory matches DBM SEC-07 enumerations |
| 3 | CWP narrative covers R-CWP-1, -2, -3, -4, -6, -9, -10, -11 |
| 4 | Workface plan satisfies R-CWP-8 prerequisite logic |
| 5 | Checklist satisfies R-CWP-7 and includes safety-critical rows |
| 6 | Specification ↔ CWP mapping complete; TBDs mirrored |
| 7 | CWP issued and registered; consumers notified |

## Records

The following records evidence successful execution of this Procedure:

- Issued Construction Work Package narrative (revision-controlled).
- Issued installation and tie-in workface plan (revision-controlled).
- Issued construction interface and turnover checklist (revision-controlled).
- Inspection and Test Plan (ITP) [ASSUMPTION — standard CWP companion].
- Open-items / TBD register associated with the CWP.
- Distribution / acknowledgement log to downstream EPC and vendor consumers.

Records retention and storage location are governed by EPC document control and are `TBD` in the available source set.
