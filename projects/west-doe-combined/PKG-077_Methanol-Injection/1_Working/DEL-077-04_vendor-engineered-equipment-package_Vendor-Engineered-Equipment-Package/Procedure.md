# Procedure — DEL-077-04 Vendor Engineered Equipment Package

This procedure describes how to **produce** the Vendor Engineered Equipment Package deliverable (vendor design basis, datasheet set, and physical equipment package) for PKG-077 Methanol Injection. Steps marked `TBD` require source-slice extraction or human ruling.

## Prerequisites

1. **EPC anchors available.** The EPC Scope of Work (DEL-077-01) and EPC Package Datasheet (DEL-077-02) must be issued and accessible to the Package Vendor. [Source: `DELIVERABLE_REGISTER.csv` rows 396, 397, 399 Notes]
2. **Responsibility boundary acknowledged.** Package Vendor and EPC Integrator have a written understanding of the ownership split per `PACKAGE_REGISTER.csv` row 72.
3. **Declared dependencies.** None declared upstream or downstream in `_DEPENDENCIES.md` as of PREPARATION; rely on the EPC anchors above. [Source: `_DEPENDENCIES.md`]
4. **Reference set.** Decomposition registers (Gate 7 snapshot) and `_CONTEXT.md` per `_REFERENCES.md`. Deliverable-local source slices from the underlying workbook / DBM / package requirements doc are not yet extracted; extract before producing source-grounded technical content. [Source: `_REFERENCES.md` Missing / Deferred References]
5. **Gate 6 disposition reconciled** (Conflict C-077-04-001 in `Guidance.md`) — `TBD`.

## Steps

### S1 — Consume EPC Anchors
Read DEL-077-01 (Scope of Work) and DEL-077-02 (Package Datasheet) in full. Extract: package function, tagged equipment list, battery-limit definitions, interface requirements matrix, and any explicit technical criteria. [Source: `ARTIFACT_REGISTER.csv` rows 4267-4277+]

### S2 — Establish Vendor Package Design Basis
Author the vendor package design basis covering: process service and conditions, equipment selection rationale, material selection, area/electrical classification approach, safety/relief approach, and standards/codes applied. Process conditions: `TBD` pending S1 extraction.

### S3 — Develop Vendor Datasheet Set
Produce per-equipment datasheets covering all major equipment in the package (vessels, pumps/injection skids, instrumentation, piping specialties, electrical equipment as applicable). Major equipment inventory: `TBD` until DEL-077-01 tagged equipment list is extracted.

### S4 — Address All Declared Interface Types
For each of the 13 declared PKG-077 interface types (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports), define the vendor side of the boundary (terminations, ratings, set-points, support points) consistent with DEL-077-02 interface requirements matrix. [Source: `PACKAGE_REGISTER.csv` row 72; `INTERFACE_REGISTER.csv` rows 574-586]

### S5 — Engineer & Design the Physical Package
Perform package engineering (process, mechanical, electrical, I&C, structural as applicable) and produce design outputs (P&ID, GA, isometrics, electrical one-lines, instrument lists, etc.). Specific design output set: `TBD` (governed by EPC Package Datasheet expectations).

### S6 — Fabricate / Supply the Physical Equipment Package
Execute fabrication and/or procurement of the physical package per the vendor design output set. [Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row 399]

### S7 — Factory Verification
Perform vendor in-shop inspections and factory acceptance testing of the physical package prior to shipment. FAT protocol: `TBD` (ASSUMPTION: vendor-standard FAT plus any EPC-witnessed items per DEL-077-06).

### S8 — Package Hand-Off to EPC Integrator
Deliver the physical equipment package and the vendor package design basis and datasheet set to the EPC Integrator for vendor package review and acceptance under DEL-077-06. Vendor document register, submittals, and turnover records are handled in DEL-077-05. [Source: `DELIVERABLE_REGISTER.csv` rows 400, 401]

### S9 — Support EPC Review and Acceptance
Respond to EPC Integrator review comments raised under DEL-077-06 until acceptance is granted. [Source: `DELIVERABLE_REGISTER.csv` row 401]

## Verification

| Step | Verification |
|---|---|
| S1 | Traceability index from EPC anchors to vendor design basis is complete |
| S2 | Design basis covers all process / mechanical / electrical / I&C / structural domains relevant to the package (gap review) |
| S3 | Datasheet set covers all tagged major equipment items from DEL-077-01 with no omissions |
| S4 | Interface matrix walkthrough confirms vendor-side definition for all 13 declared PKG-077 interface types |
| S5 | Design output set complete per DEL-077-02 expectations (TBD list) |
| S6 | Vendor QA records show fabricated/procured equipment conforms to design outputs |
| S7 | FAT records signed off (witness scope TBD) |
| S8 | Hand-off package signed receipt from EPC Integrator |
| S9 | DEL-077-06 acceptance log shows closure of vendor comments |

## Records

The following evidence/documents result from this procedure:

- Vendor package design basis (document)
- Vendor datasheet set (document set)
- Vendor design outputs (P&ID, GA, isometrics, electrical one-lines, instrument list, etc. — exact set TBD)
- Vendor QA / fabrication / supply records
- FAT records
- Physical equipment package (the artifact itself)
- Hand-off transmittal to EPC Integrator (carried in DEL-077-05)
- EPC review/acceptance evidence (carried in DEL-077-06)

[Source for record set: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` rows 399, 400, 401]
