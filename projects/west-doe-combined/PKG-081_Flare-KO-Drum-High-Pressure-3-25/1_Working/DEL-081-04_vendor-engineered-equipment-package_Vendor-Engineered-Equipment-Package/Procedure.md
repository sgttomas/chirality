# Procedure: DEL-081-04 — Vendor Engineered Equipment Package (Flare KO Drum, High Pressure, 3-25)

> Operational procedure for the Package Vendor producing this deliverable, with EPC Integrator coordination touchpoints. This procedure covers producing the vendor-engineered HP flare KO drum package; downstream installation and operation are covered by the Construction Work Package (DEL-081-03) and facility operating procedures.

## Purpose

Define the sequence by which the Package Vendor turns the EPC-issued Scope of Work and Package Datasheet (with applicable DBM source slices) into the engineered, fabricated, supplied physical HP flare KO drum package ready for site installation and EPC review/acceptance.

## Prerequisites

### Upstream artifacts required
- DEL-081-01 — EPC Scope of Work for PKG-081 (**TBD** at the time of this procedure draft).
- DEL-081-02 — EPC Package Datasheet for PKG-081 (**TBD** at the time of this procedure draft).
- Locally accessible DBM source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, sections "Flare and Blowdown", "Sparing Philosophy", and isolation/sour-service guidance.
- Package Requirements source: `_Sources/26020-Package_Requirements.docx` package heading 34 (text not extracted in this run; **location TBD** at clause level).

### Vendor-side prerequisites
- Vendor engineering team mobilized with appropriate disciplines (mechanical/vessel, rotating, instrumentation, electrical, structural, materials).
- Confirmed equipment tag assignment (V-4100-2 or V-4150-2) — **NEEDS_HUMAN_RULING.**
- Access to project design specifications referenced by the EPC Package Datasheet (materials, instrumentation, painting, electrical area classification).

### EPC-side prerequisites
- EPC Integrator point of contact identified for integration review.
- Final (or current best) flare study allocation for the assigned KO drum (**TBD** pending W242510-PRC-REP-000003-001 availability).
- Tie-in interface drawings (HP relief header, HP flare header, slop transfer routing, electrical/instrument terminations).

## Steps

### Step 1 — Initiation and design basis confirmation
1. Receive EPC Scope of Work and EPC Package Datasheet for PKG-081.
2. Confirm equipment tag (V-4100-2 or V-4150-2) and location (compressor area or tank farm). `[SourcePath: DBM; SectionRef: Flare and Blowdown]`
3. Issue a vendor design basis memorandum capturing inherited design pressure/temperature, relief case, header sizes, sour-service classification, sparing basis, codes/standards, and any ASSUMPTION items pending EPC clarification. **TBD** values explicitly listed.

### Step 2 — Process and sizing engineering
1. Size the KO drum for the assigned relief case under the staggered-blowdown assumption stated in the DBM. `[SourcePath: DBM; SectionRef: Flare and Blowdown]`
2. Select internals (mist eliminator vs gravity-only) per Package Datasheet preference; document trade-off rationale.
3. Size and select the transfer pump (1 x 100 percent per KO drum) for truck-out or transfer-to-slop service. `[SourcePath: DBM; SectionRef: SEC-09 Sparing Philosophy + Flare and Blowdown]`

### Step 3 — Mechanical, materials, and code design
1. Perform vessel design per the governing pressure-vessel code (per Package Datasheet; ASME BPVC Section VIII or equivalent — **ASSUMPTION**).
2. Select materials of construction per the project materials specification, with sour-service compliance where applicable. `[SourcePath: DBM; SectionRef: Isolation philosophy (line ~607)]`
3. Specify weld procedures, NDE level, and post-weld heat treatment per code and materials specification.

### Step 4 — Instrumentation, electrical, and controls design
1. Specify level, pressure, and temperature instrumentation with safe failure modes (avoid liquid carryover to flare).
2. Specify electrical terminations and area-classification compliance.
3. Produce I/O list, loop diagrams, and SIL/safety-function documentation as required.

### Step 5 — Layout, structural, and integration design
1. Produce general arrangement drawings, P&ID, and isometrics for package-internal piping.
2. Define battery-limit nozzles consistent with HP relief / HP flare header sizing (current source basis 508 mm / 20 inch). `[SourcePath: DBM; SectionRef: Flare and Blowdown]`
3. Provide structural/skid design (if skid-mounted) or anchor/foundation interface (if site-erected).
4. Provide vent, drain, and isolation provisions per project isolation philosophy. `[SourcePath: DBM; SectionRef: Isolation philosophy (line ~607)]`

### Step 6 — Integration review with EPC Integrator
1. Submit design documentation package for EPC Integrator integration review.
2. Resolve interface punch items.
3. Reissue affected documents.

### Step 7 — Procurement, fabrication, and FAT
1. Procure long-lead items (vessel material, pump).
2. Fabricate per approved drawings; perform code-required NDE and inspection.
3. Perform pressure test and code certification.
4. Conduct Factory Acceptance Test for instrumentation/controls (and pump performance test).
5. Apply preservation, painting/coating, and prepare for shipment.

### Step 8 — Documentation handover
1. Compile vendor package design basis, datasheets, calculations, drawings, MTRs, code certificates, FAT records, O&M manuals, and spare parts list.
2. Transmit to EPC Integrator as the engineering package supporting downstream DEL-081-05 (Vendor Document Turnover Package) and DEL-081-06 (EPC Vendor Package Review and Acceptance).

## Verification

| Check | How verified |
|---|---|
| Equipment tag identity confirmed | EPC Package Datasheet revision and vendor design basis memorandum |
| Relief sizing aligns with assigned flare-study case | Vendor sizing calculation reviewed against the assigned relief case |
| Vessel design code-compliant | Stamped vessel certification; design report |
| Materials suit sour-service classification | MTRs and (where applicable) NACE compliance certificates |
| Transfer pump performance | Vendor witnessed performance test report |
| Battery-limit nozzles match header design | Nozzle schedule cross-checked against tie-in drawings |
| Instrumentation correctness | I/O list reconciled with EPC instrument index; loop checks |
| Documentation completeness | Turnover index reconciled with EPC requirements |
| Integration acceptance | EPC Integrator integration review sign-off (precondition for DEL-081-06) |

## Records

The following records shall result from this procedure and be retained in the vendor package documentation set:

- Vendor design basis memorandum (with TBD/ASSUMPTION register at issue)
- Vessel design calculations and code data report
- Vessel pressure test certificate; material test reports (MTRs)
- Pump sizing/selection calculation; pump performance test report
- General arrangement drawings, P&ID, isometrics (as-built)
- I/O list, loop diagrams, FAT records
- Painting/coating and preservation records
- Spare parts list
- Shipment documentation (packing list, transport notes)
- Vendor O&M manual
- Integration review minutes and disposition of EPC comments
