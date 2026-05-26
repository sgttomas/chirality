# Procedure: DEL-048-04 — Vendor Engineered Equipment Package

> Operational procedure for *producing* the vendor-engineered equipment package deliverable. The procedure describes the workflow by which the Package Vendor develops the engineered package from upstream SOW and Package Datasheet, and surfaces it for EPC Integrator review and turnover. Procedural specifics that depend on unextracted source slices are marked TBD.

## Purpose

Define the steps by which the Package Vendor produces, verifies, and releases the engineered Inlet / Sales Compressors equipment package described in `Specification.md`, in a form ready for vendor documentation turnover (DEL-048-05) and EPC Integrator review and acceptance (DEL-048-06). [`_CONTEXT.md`; PACKAGE_REGISTER PKG-048]

## Prerequisites

- **Upstream inputs (PROPOSAL — see Guidance Conflict CONF-002):** DEL-048-01 Scope of Work and DEL-048-02 Package Datasheet are available and at an `INITIALIZED` (or higher) maturity. [`_CONTEXT.md` Scope role text]
- **Reference materials available:** `26020-Package_Requirements.docx` package heading 3; `Bid Docs/Budgetary/RFQ/Bid Docs/26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md` accessible to the Package Vendor in source form. [`_REFERENCES.md`; PACKAGE_REGISTER PKG-048]
- **Decomposition snapshot in force:** GATE-07 Final Published (2026-05-24) PROJECT_DECOMP snapshot. [`_REFERENCES.md`]
- **Specification requirements:** REQ-1 through REQ-9 in `Specification.md` reviewed and understood.

## Steps

### Step 1 — Lock the package basis
1. Confirm the EPC package SOW (DEL-048-01) and Package Datasheet (DEL-048-02) are the basis-of-design inputs.
2. Reconcile any gaps between the SOW/Datasheet and the source extracts referenced here (SOW-0115..0118; PKG-048).
3. Record the locked basis in the vendor design basis document.

### Step 2 — Resolve TBD source slices
1. Extract from `26020-Package_Requirements.docx` and the RFQ the clauses governing: materials of construction, area classification, process gas composition, ambient/site design conditions, noise/vibration limits, applicable code list (e.g., API 618 confirmation), and any vendor data requirements list. [REQ-9]
2. Update vendor datasheets and design basis accordingly. Surface remaining gaps to the EPC Integrator.

### Step 3 — Compressor train engineering
1. Configure 5 × Ariel KBC/6, 3-stage reciprocating compressors, sized for 120%, with inlet service single-stage and sales service double-stage. [REQ-1]
2. Select drivers per REQ-2 (8-pole, 6600 V/3PH/60Hz, 891 RPM, 5,220 kW / 7,000 HP design rating bounding per Guidance CONF-001; TEFC or WPII; NEMA MG 1; KBZ frame WEG preferred).
3. Produce compressor and motor performance datasheets and performance curves covering REQ-3 operating/design conditions.

### Step 4 — Suction scrubbers
1. Size two-phase suction scrubbers upstream of each stage with vertical flow vane-style demisters per REQ-4 (K <= 0.5 Imperial with pressure de-ration; liquid SG = 0.61).
2. Produce vessel mechanical datasheets and demister sizing calculations.

### Step 5 — Process cooling
1. Design one common air cooler frame per package serving both services, per REQ-5.
2. Implement automated louver control via pneumatic temperature control on each process bundle.
3. Produce cooler datasheet and control narrative.

### Step 6 — Interface design
1. For each of the 13 PKG-048 applicable interface types (REQ-6), produce a section in the vendor interface compliance matrix indicating: package-side termination point, design assumption about EPC side, and any vendor-side coordination items.
2. Confirm by-others items (REQ-8) are not duplicated in vendor scope and are designed *for* at the interface.

### Step 7 — Vendor documentation set
1. Assemble the vendor design basis document.
2. Assemble the vendor datasheet set (mechanical, electrical, controls).
3. Assemble the vendor interface compliance matrix.
4. Assemble FAT plan and acceptance criteria.

### Step 8 — Fabrication and FAT
1. Fabricate the physical equipment package per the engineered design.
2. Execute factory acceptance tests per the FAT plan; capture performance, motor, scrubber, and cooler control results.
3. Resolve FAT punch items prior to release for turnover.

### Step 9 — Release for turnover
1. Compile the vendor turnover documentation (handled in DEL-048-05) referencing the artifacts produced here.
2. Notify the EPC Integrator that the package is ready for review and acceptance (handled in DEL-048-06).

## Verification

| Check | Pass criterion |
|---|---|
| Configuration check | 5 × Ariel KBC/6 units configured per REQ-1; inlet single-stage and sales double-stage verified in datasheets. |
| Sizing check | Each compressor verified sized for 120% per REQ-1. |
| Driver check | Motor datasheet and nameplate satisfy REQ-2; NEMA MG 1 compliance documented. |
| Pressure/capacity check | Performance curves and mechanical run test demonstrate REQ-3 values for both services. |
| Scrubber check | Demister sizing calculation shows K <= 0.5 Imperial (with pressure de-ration) and 0.61 SG basis per REQ-4. |
| Cooler check | Single common air cooler frame with bundle-level pneumatic louver control verified per REQ-5. |
| Interface compliance | Interface compliance matrix completed for all 13 interface types per REQ-6. |
| Documentation completeness | Vendor design basis and datasheet set delivered per REQ-7 and `_CONTEXT.md` Anticipated Artifacts. |
| Scope demarcation | Vendor scope-of-supply list aligns with REQ-8 by-others list. |
| TBD closure | Items flagged TBD (materials, area classification, gas composition, ambient/site, noise/vibration) resolved and recorded, or escalated to the EPC Integrator. |

## Records

- Vendor design basis document
- Vendor datasheet set (compressor, motor, scrubber, cooler, controls)
- Demister sizing calculation
- Cooler control narrative
- Interface compliance matrix
- FAT plan, FAT records, punch list closure
- Vendor scope-of-supply list (reconciled against SOW-0118 by-others items)
- Release-for-turnover notification (handoff record to DEL-048-05 / DEL-048-06)
