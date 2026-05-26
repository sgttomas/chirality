# Procedure — Vendor Engineered Equipment Package (DEL-087-04)

> Operational steps to produce, supply, and ready-for-acceptance the Package Vendor production unit for PKG-087 Incinerator. Steps describe how the Package Vendor executes the deliverable; EPC Integrator review and acceptance is procedurally distinct (DEL-087-06).

## Purpose

Define the sequence by which the Package Vendor turns the EPC Scope of Work (DEL-087-01) and EPC Package Datasheet (DEL-087-02) into an engineered, designed, fabricated, and supplied incinerator equipment package — together with the vendor design basis and datasheet set — and presents it for EPC integration review. [`_CONTEXT.md`; `PACKAGE_REGISTER.csv` Description; `DELIVERABLE_REGISTER.csv` DEL-087-01, DEL-087-02, DEL-087-06]

## Prerequisites

| Prerequisite | Status | Source |
|---|---|---|
| EPC Scope of Work (DEL-087-01) issued | Required before package engineering kickoff | `DELIVERABLE_REGISTER.csv` DEL-087-01 |
| EPC Package Datasheet (DEL-087-02) issued | Required before package design freeze | `DELIVERABLE_REGISTER.csv` DEL-087-02 |
| Shared-interface allocation between 03-25 and 04-25 confirmed by EPC Integrator | Open interface item; required before capacity freeze | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 547 |
| Inlet stream composition and design conditions from upstream caustic-treating package | Required before vendor process design freeze | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 389, 400, 402 |
| Vendor document list per `26020-Package_Requirements.docx` package heading 40 | Required before vendor documentation kickoff; locally accessible slice (510-521) contains Basic Scope and Major Included Equipment; the vendor-document table within the same source remains location TBD | `_REFERENCES.md`; `26020-Package_Requirements.docx` package heading 40 |
| Self-framing incinerator building erection at site | Confirmed as in-scope per source | `26020-Package_Requirements.docx` package heading 40 (slice 510-515) |
| Facility ambient design basis (-40 deg C) | Confirmed | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696 |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |

## Steps

### Step 1 — Receive and confirm package inputs

1.1 Receive EPC Scope of Work (DEL-087-01), EPC Package Datasheet (DEL-087-02), interface schedule (built from `INTERFACE_REGISTER.csv` PKG-087 rows), and the vendor document list (from `26020-Package_Requirements.docx` heading 40 — location TBD).
1.2 Reconcile the Datasheet's inlet streams and capacity against the DBM-stated incinerator service (spent-caustic vapours, caustic-treating overhead/dilution/enrichment gas, and the 03-25/04-25 shared-interface allocation). [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 400, 402, 547]
1.3 Log open inputs (Conflicts CONF-01/CONF-02/CONF-03 in `Guidance.md`) and request EPC ruling before proceeding past process design.

### Step 2 — Package process engineering

2.1 Develop heat and material balances for incinerator inlets (spent-caustic vapours + caustic-treating overhead/dilution/enrichment + shared-interface contributors) covering normal and design conditions, including the 214 SCFM TBC caustic-oxidation demand. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 477]
2.2 Define combustion control philosophy, draft control (blower), and stack discharge configuration (low pressure flare stack).
2.3 Issue package P&IDs and PFDs.

### Step 3 — Package mechanical and material engineering

3.1 Specify the knockout drum (ASME VIII vessel — ASSUMPTION; confirm against source standards list), transfer pump, blower, and low-pressure flare stack.
3.2 Apply caustic-service material constraints: no aluminum in caustic-wetted service or caustic building; confirm coating/cladding strategy for caustic-touching components. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402]
3.3 Apply caustic drain rating (300# ANSI minimum) and address embrittlement; coordinate with the EPC for the final position on caustic drain heat tracing. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 493]
3.4 Engineer winterisation/freeze-protection consistent with -40 deg C site ambient. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696]

### Step 4 — Package electrical, controls, instrumentation

4.1 Define electrical terminal points and power demand per `INTERFACE_REGISTER.csv` IFC-D8FC238CE8 (Electrical Power); grounding/bonding per IFC-FD13F602FB.
4.2 Provide package controls signals, alarms, shutdowns, and cause-and-effect input to the EPC controls topology under OBJ-006. [`OBJECTIVE_REGISTER.csv` OBJ-006]
4.3 Provide layout to support EPC fire & gas detection coverage (LEL, H2S, methyl mercaptan, fire detectors); detector placement is an EPC responsibility informed by vendor layout. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 838]

### Step 5 — Civil / structural interface

5.1 Produce equipment loads, anchor patterns, lift points, access requirements, and shipping splits sufficient for the EPC Integrator to design foundations, supports, and maintenance access (interfaces IFC-23A65D01E5 Structural / Foundations / Supports; IFC-A18F15D335 Maintenance Access). [`INTERFACE_REGISTER.csv` (PKG-087 rows)]
5.2 Confirm building/HVAC interface (IFC-588E647FEE) and area/exterior lighting (IFC-1892D97798) handoff points.

### Step 6 — Interface schedule, design review, and design freeze

6.1 Issue a vendor interface schedule mirroring the GATE-07 interface register row-for-row. [`INTERFACE_REGISTER.csv` (PKG-087 rows)]
6.2 Hold design reviews with the EPC Integrator; resolve open items including CONF-01, CONF-02, CONF-03 from `Guidance.md`.
6.3 Freeze the package design.

### Step 7 — Fabrication, FAT, and supply

7.1 Fabricate / procure equipment.
7.2 Execute Factory Acceptance Testing per the EPC Datasheet and vendor inspection plan (specifics TBD pending source vendor document list).
7.3 Package, ship, and supply equipment to site under the EPC Integrator construction work package (DEL-087-03).

### Step 8 — Vendor documentation set

8.1 Produce the vendor design basis and datasheet set (an anticipated artifact of this deliverable). [`_CONTEXT.md` Anticipated Artifacts]
8.2 Issue the vendor documentation set required by `26020-Package_Requirements.docx` heading 40 (full list TBD; location TBD); submit to the EPC Integrator and to DEL-087-05 for register and turnover handling. [`DELIVERABLE_REGISTER.csv` DEL-087-05]

### Step 9 — Handoff for EPC review and acceptance

9.1 Present the engineered package, vendor documentation, and supplied equipment to the EPC Integrator for review and acceptance (DEL-087-06). [`DELIVERABLE_REGISTER.csv` DEL-087-06]
9.2 Address review findings; close out vendor open items (operability, maintainability, sparing, isolation, winterization, commissioning support per OBJ-010). [`OBJECTIVE_REGISTER.csv` OBJ-010]

## Verification

| Step | Verification |
|---|---|
| 1 | Documented inputs log; open-input ruling memo from EPC Integrator. |
| 2 | Heat & material balance review; P&ID/PFD issue stamp. |
| 3 | Material test reports; mill certificates; coating reports; winterisation design memo. |
| 4 | Electrical single-line and cause-and-effect issued; controls integration test record. |
| 5 | Equipment load schedule and anchor drawings stamped; access study. |
| 6 | Vendor interface schedule reviewed against `INTERFACE_REGISTER.csv` PKG-087 rows; conflict ruling memos closed; design-freeze record. |
| 7 | FAT report; shipping release; receipt acceptance at site. |
| 8 | Vendor document register status report (consumed by DEL-087-05). |
| 9 | EPC Vendor Package Review and Acceptance evidence (DEL-087-06). |

## Records

The following records SHALL result from execution of this procedure:

- Vendor design basis document. [`_CONTEXT.md` Anticipated Artifacts]
- Vendor package datasheet set. [`_CONTEXT.md` Anticipated Artifacts]
- Heat & material balance, P&IDs, PFDs.
- Equipment datasheets, instrument index, electrical single-line at package boundary, cause-and-effect matrix.
- General arrangement, lifting, and shipping drawings.
- Material test reports, mill certificates, coating reports.
- Factory Acceptance Test records.
- Shipping and receipt acceptance records.
- Operating and maintenance manuals; spare parts list.
- Vendor document register entries (input to DEL-087-05).
- EPC Vendor Package Review and Acceptance evidence (input to DEL-087-06).
- Open-item closure records under OBJ-010. [`OBJECTIVE_REGISTER.csv` OBJ-010]

Full record list is governed by `26020-Package_Requirements.docx` vendor document tables (location TBD).
