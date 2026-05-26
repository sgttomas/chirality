# Procedure — DEL-099-03 Construction Work Package (PKG-099)

> Operational procedure for producing the Construction Work Package artifact set (Construction Work Package narrative, Installation and Tie-in Workface Plan, Construction Interface and Turnover Checklist) for PKG-099 (truck product loading stations for sweet stabilized condensate at the 03-25 Liquids Hub). This procedure describes how to **produce** the deliverable; site-execution procedures are downstream of this artifact set and follow the resulting workface plan.

## Prerequisites

Authoritative inputs:

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- PKG-099 row from `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`.
- DEL-099-03 row from the same snapshot's `DELIVERABLE_REGISTER.csv`.
- 03-25 DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) — Site Basis; SEC-06 Liquids Hub (Condensate Storage and Product Handling; Vapour Recovery); SEC-08 Prime Movers; SEC-10 Miscellaneous Facilities; SEC-11 Plant Layout/Civil; SEC-12 Electrical; SEC-13 F&G references.
- 26020-Package_Requirements.docx package heading 51 (binary; resolve when text-accessible).
- 26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx (binary RFQ; resolve when text-accessible).
- Project piping specification and project measurement / custody-transfer specification (location TBD).
- API RP 2003 (static-bonding industry practice; location TBD; applicability ASSUMPTION).

Coordinating inputs (when produced):

- DEL-099-01 Scope of Work (EPC Scope of Work for PKG-099).
- DEL-099-02 Package Datasheet (technical handoff basis and interface requirements matrix).
- DEL-099-04 Vendor Engineered Equipment Package (vendor design basis once issued).
- DEL-099-06 EPC Vendor Package Review and Acceptance (downstream consumer of turnover evidence).

No upstream/downstream dependency edges are declared in `_DEPENDENCIES.md` at this writing; coordinate informally with DEL-099-01, DEL-099-02, and DEL-099-04 authors. (TBD: formal dependency declaration.)

## Steps

1. **Confirm package identity and resolve the station-count conflict.**
   - Re-read the PKG-099 PACKAGE_REGISTER row and the DBM Condensate Storage and Product Handling / Miscellaneous Facilities sections.
   - Record the station-count conflict (PACKAGE_REGISTER: 2 stations 2x2; DBM: 3 stations) in the `Guidance.md` Conflict Table (C-099-03-01) and treat as TBD pending vendor equipment list / RFQ read.
   - Confirm process service: sweet stabilized C5+ condensate, loaded to atmospheric trucks via dedicated loading pumps at 103 m3/h per station, 345 kPad differential.

2. **Establish construction site basis.**
   - Capture site location (LSD 03-25-80-15 W6M), elevation (673 m), and -40 deg C governing minimum ambient from the DBM Site Basis.
   - Record cold-climate constructability drivers (winterization, heat tracing, cold-weather concrete, winter road operation, snow/wind/seismic) as basis statements.

3. **Resolve loading system design basis.**
   - Pull loading-station capacity (103 m3/h, 345 kPad) and per-station loading-pump basis from the DBM (SEC-06; SEC-08).
   - Identify upstream connection (condensate booster pumps P-9211-2 / P-9221-2 or direct from product condensate tanks per final P&IDs) and vapour-return interface (TBD per Conflict C-099-03-03).
   - Cross-check vendor datasheet (when issued) against DEL-099-02 Package Datasheet. Mark `TBD` if not yet issued.

4. **Draft Construction Work Package narrative.**
   - Sequence: site prep -> foundations / truck-loading slab -> structural supports / canopy -> mechanical equipment set (loading skids, metering, pumps) -> piping erection -> electrical and I&C rough-in -> F&G installation -> hydrotest / leak test -> metering proving -> tie-ins (process, vapour return, drain/containment, electrical, F&G) -> commissioning support -> mechanical completion -> turnover.
   - For each phase, identify EPC scope, vendor scope, and the EPC/vendor interface boundary; cite PACKAGE_REGISTER row for the boundary statement.
   - Add hold points: foundation pre-pour inspection; slab pre-pour inspection; pre-piping-erection readiness; pre-hydrotest readiness; metering proving witness; pre-F&G live; pre-first-product-load static-bonding verification.

5. **Build Installation and Tie-in Workface Plan.**
   - Enumerate workface packages per station (civil/slab, mechanical/piping, electrical/instrumentation, metering, F&G, commissioning) and assign crew, schedule window, and weather constraints. Total station count carried as TBD per Conflict C-099-03-01.
   - For each station, list one row per declared interface type from PKG-099 (eleven rows × N stations); identify drawing reference (TBD where drawings not yet issued) and acceptance criteria reference (package heading 51, RFQ, project specs — clause `location TBD`).
   - Include shared facility tie-ins (electrical feed from 04-25 cross-facility system; vapour return to VRU header per resolved process basis).

6. **Build Construction Interface and Turnover Checklist.**
   - Columns: Interface ID; Interface Type; Station Tag; Description; Acceptance Criteria Reference; Required Records; EPC Sign-off; Vendor Sign-off; Date Closed.
   - Pre-populate with the eleven interface tie-in items per station plus station-level acceptance items: hydrotest/leak test, metering proving, pump performance/commissioning, vapour-return tie-in verification, spill containment walkdown, CP (if applicable) and grounding/bonding test, static-bonding verification (per loading position), F&G commissioning, heat-tracing commissioning.
   - Add mechanical-completion and turnover gates referencing DEL-099-06 (EPC Vendor Package Review and Acceptance).

7. **Cross-check requirements traceability.**
   - For each R-099-03-* requirement in `Specification.md`, confirm a corresponding verification step exists in this Procedure and an evidence column exists on the checklist.
   - Ensure all eleven interface types are represented on the checklist for each station.

8. **Mark unresolved items.**
   - Any clause-level reference still pointing to `location TBD` (e.g., package requirements heading 51, RFQ 26020-03-PT-RFQ-23-001, project piping/measurement specs, API RP 2003) is recorded as `TBD` in the deliverable Conflict Table and surfaced for human ruling.
   - Station count remains TBD per Conflict C-099-03-01 until the vendor equipment list or RFQ is text-accessible. Do not pick a default count.
   - Vapour-return routing remains TBD per Conflict C-099-03-03.
   - Do not invent clause numbers or device counts.

9. **Issue for review.**
   - Tag the artifact set for EPC Integrator review; coordinate with DEL-099-01, DEL-099-02, and DEL-099-04 owners for terminology and station-count alignment before downstream consumption by DEL-099-04 / DEL-099-06.

## Verification

- All three artifacts (Construction Work Package narrative, Workface Plan, Turnover Checklist) exist and are internally consistent.
- Every R-099-03-* requirement in `Specification.md` has a corresponding entry on the Turnover Checklist or in the Workface Plan.
- All eleven declared PKG-099 interface types appear on the checklist for each station.
- Cold-climate site basis (-40 deg C) appears explicitly in the narrative.
- Station-count conflict (C-099-03-01) is surfaced and not silently resolved.
- All `TBD` items are either resolvable from accessible sources or surfaced in `Guidance.md` Conflict Table.

## Records

The procedure (this document) is satisfied by producing the following records inside the deliverable folder when site execution actually occurs (downstream of this drafting deliverable):

- Construction Work Package narrative document
- Installation and Tie-in Workface Plan document
- Construction Interface and Turnover Checklist document
- Hydrostatic / leak test reports (per station)
- Metering proving and calibration records (per station)
- Pump performance / motor commissioning records
- F&G installation and integration records
- CP (if applicable) and grounding/bonding test records
- Static-bonding verification records (per loading position)
- Foundation and slab inspection / pour records
- Heat-tracing commissioning records
- Tie-in punch list closure records
- EPC and Vendor sign-off records for each checklist row
- As-built mark-ups

At the time of this draft, the deliverable folder contains the four-document kit only; site-execution records (hydrotest, proving, F&G commissioning, etc.) are produced during downstream execution. (TBD: site-execution evidence not yet produced.)
