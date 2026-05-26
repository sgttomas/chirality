# Procedure — DEL-068-04 Vendor Engineered Equipment Package (TEG Dehydration Unit)

## Purpose

This procedure describes the steps to **produce** the Vendor Engineered Equipment Package deliverable: from receipt of the EPC handoff documents through vendor engineering, fabrication, and supply, to readiness for EPC integration review and acceptance. (Interpretation rule per skill: "produce" path selected because the deliverable is itself the vendor's engineered package and the physical equipment supply.)

## Prerequisites

### Upstream inputs required before vendor engineering begins
- DEL-068-01 EPC Scope of Work — final issued (state per `_DEPENDENCIES.md` — not declared at PREPARATION; ASSUMPTION based on register narrative).
- DEL-068-02 EPC Package Datasheet — final issued (ASSUMPTION; same basis).
- DEL-068-03 Construction Work Package — at least interim, sufficient to define installation interface envelope (ASSUMPTION).
- Accepted DBM source basis: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 and Utility Integration Basis.
- Accepted SCA-002 supersession state for compressor discharge pressure (800 psig).

### Required references
- `_REFERENCES.md` (this deliverable)
- `_CONTEXT.md` (this deliverable)
- PKG-068 / 0_References folder (currently `_Archive` only; ASSUMPTION: EPC will populate)
- 26020-Package_Requirements.docx package heading 23 (binary; location TBD locally)

### Open items to resolve before fabrication release
- Conflict Table entries C-068-04-01 through C-068-04-05 in `Guidance.md`.
- Maximum gas flow rating (TBC in source).

## Steps

### Step 1 — Vendor mobilization and design basis confirmation
1.1 Receive EPC SOW (DEL-068-01) and Package Datasheet (DEL-068-02).
1.2 Confirm scope coverage against SOW items SOW-0237, SOW-0238, SOW-0239, SOW-0240.
1.3 Read SEC-05 of `3-25_Comp_and_Liquids_DBM.md` and the Utility Integration Basis to establish the binding process and utility envelope.
1.4 Issue Vendor Design Basis Document; flag deviations from EPC documents as formal deviation requests.

### Step 2 — Process and equipment engineering
2.1 Size the contactor: structured packing, at least three theoretical stages, Fs not more than 3.0, inlet/outlet demisters, against the inlet pressure/temperature/flow table in `Datasheet.md`. Demonstrate the 4 lb H2O/MMSCF outlet specification.
2.2 Size the regeneration train (still column, stripping column, reflux condenser, reboiler, surge drum, regen cooler, regen overhead scrubber, regen overhead pumps) to deliver lean TEG quality consistent with the contactor design and 2:1 regen turndown.
2.3 Size the flash drum and confirm flash gas pressure-regulation envelope to 04-25 SOC first-stage suction.
2.4 Size rich TEG filtration: full-flow 5 micron solids filter plus 20 percent slipstream carbon/particle filter.
2.5 Size the surge drum for 30 minutes retention at 50 psig.
2.6 Select TEG pumps (2 x 100 percent, rotary gear or positive-displacement, single mechanical seals).
2.7 Design the inlet filter coalescer (1 x 100 percent, manual bypass and isolation, manual blowdown at coalescer, automated blowdown downstream of contactor).
2.8 Design the makeup system (atmospheric tank, fuel-gas blanketed, heated/insulated, not connected to VRU; makeup pump).
2.9 Materials selection consistent with sour-service basis (0.296 mol% H2S compressor composition); document standards applied (ASSUMPTION pending vendor confirmation per Spec R-068-04-16).

### Step 3 — Mechanical, piping, electrical, and instrumentation engineering
3.1 Issue equipment datasheets and mechanical drawings for each item in the `Datasheet.md` Construction table.
3.2 Issue package P&IDs, GA drawings, and isometrics.
3.3 Define the automated contactor blowdown to HP flare and regeneration overhead routing consistent with LP flare basis (LP KO drum V-3900-2).
3.4 Define LP fuel-gas tie-in to TEG stripping/reboiler firing per facility utility basis.
3.5 Define control narrative: contactor pressure/level/temperature control; flash drum level and pressure control; regeneration temperature control; TEG quality monitoring.

### Step 4 — Vendor design review and EPC interface
4.1 Internal vendor design review (HAZOP-ready package).
4.2 Submit package design dossier to EPC Integrator for integration review (per `_CONTEXT.md` ResponsibleParty statement).
4.3 Resolve integration comments; freeze design for fabrication.

### Step 5 — Fabrication and supply
5.1 Issue purchase orders for long-lead equipment (columns, exchangers, pumps).
5.2 Execute Inspection and Test Plan (ITP) at fabrication shops with vendor and EPC witness points as agreed.
5.3 Module assembly and shop testing per vendor standards.
5.4 Performance test or functional test as agreed (e.g., regeneration train hot test, instrument loop checks).

### Step 6 — Documentation and turnover preparation
6.1 Compile vendor turnover dossier (datasheets, drawings, materials certificates, test records, O&M manuals, spare parts list). Handoff to DEL-068-05 for register management.
6.2 Prepare for EPC Vendor Package Review and Acceptance (DEL-068-06).

### Step 7 — Shipment
7.1 Pack and ship the package per agreed transport plan to project site.
7.2 Provide site technical advisor support for installation, commissioning, and start-up as contracted (interface with DEL-068-03 Construction Work Package).

## Verification

| Check | Verifier | Evidence |
|---|---|---|
| Contactor sized per R-068-04-01, 03, 04, 06 | Vendor process lead; EPC reviewer | Process calculations; contactor datasheet |
| 4 lb H2O/MMSCF performance | Vendor performance test | Witnessed test record; performance guarantee letter |
| Filtration architecture per R-068-04-10 | Vendor; EPC | Filtration datasheets; P&ID |
| Surge drum retention per R-068-04-11 | Vendor; EPC | Surge drum datasheet and calculation |
| TEG pumps per R-068-04-12 | Vendor; EPC | Pump datasheets and seal selection rationale |
| Makeup tank per R-068-04-13 | Vendor; EPC | Tank datasheet; utility tie-in P&ID |
| Sour-service materials per R-068-04-16 | Vendor QA; EPC | Materials report; mill test reports; PMI records |
| Relief and blowdown per R-068-04-07, 15 | Vendor; EPC; HAZOP | Relief calculations; flare interface P&ID |
| Integration review per R-068-04-17 | EPC Integrator | EPC integration review record (consumed by DEL-068-06) |
| All deviations logged | Vendor; EPC | Deviation register |

## Records

- Vendor Design Basis Document
- Equipment datasheets and mechanical drawings (per item in `Datasheet.md`)
- P&IDs, GA drawings, isometrics, control narrative
- Materials selection report and mill test reports
- Inspection and Test Plan and executed test records
- Performance test record (TEG outlet water content)
- Deviation register
- Shipment and transport documentation
- Turnover dossier (routed to DEL-068-05)
- EPC integration review record (input to DEL-068-06)
