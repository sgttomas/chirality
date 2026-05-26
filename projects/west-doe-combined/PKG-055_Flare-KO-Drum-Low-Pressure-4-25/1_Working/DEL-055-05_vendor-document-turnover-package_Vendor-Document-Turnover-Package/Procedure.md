# Procedure — DEL-055-05 Vendor Document Turnover Package (PKG-055)

## Purpose

Operational steps to produce, submit, and turn over the vendor documentation set for the PKG-055 LP Flare KO Drum package (one LP flare KO drum V-3900-1 and one transfer pump P-3900-1, shop-built as Module 390-1). This procedure addresses both production of the deliverable artifact (the document set) and the controlled submittal cycle that delivers it to the EPC Integrator for acceptance via `DEL-055-06`.

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` (PREPARATION did not declare upstream edges for this deliverable). Practical upstream context: the EPC Scope of Work (`DEL-055-01`) and Package Datasheet (`DEL-055-02`) define what the Package Vendor is engineering; the engineered package (`DEL-055-04`) produces the physical basis the turnover records document.
- Accessible source set:
  - `_Sources/26020-Package_Requirements.docx` (Vendor Engineering Deliverables list, package heading 10 — binary; specific clauses are TBD pending text extraction)
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 57 — binary)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (LP flare KO drum equipment, header sizing, modularization)
  - Gate 7 PROJECT_DECOMP snapshot (`DELIVERABLE_REGISTER.csv` DEL-055-05 row)
- Vendor Document Control Procedure (`DOC-008`) and Vendor Document Index (`PRQ-009`) baselined before any document is submitted.
- EPC Integrator named reviewer assigned for `DEL-055-06`.
- ASME Authorized Inspector (AI) engaged for the pressure-vessel ITP hold points (ASSUMPTION; standard for ASME-stamped vessels).

## Steps

### Step 1 — Baseline the Vendor Document Index
1. Instantiate `PRQ-009` for PKG-055 using `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" (package heading 10) as the template.
2. Organize the Index either by equipment tag (V-3900-1, P-3900-1) or by module (Module 390-1) consistent with the module-level-vs-per-equipment decision recorded in `DOC-008`.
3. Mark each line APPLICABLE / N/A with a short rationale (see Guidance principle 2 and Specification R-4 through R-7).
4. Reflect the per-discipline applicability call in the Index revision baseline.

### Step 2 — Baseline the Document Control Procedure
1. Issue `DOC-008` describing document numbering, revisioning convention, transmittal mechanics, submittal milestones, and review-cycle handling.
2. Reflect the named milestones (e.g., preliminary, certified-for-construction, as-built) consistent with the package PO.
3. Reflect the module-level-vs-per-equipment documentation decision (see Guidance "Trade-offs").
4. Explicitly document the vendor-scope boundary at the package skirt/skid edge (see Conflict HRR-055-05-004).

### Step 3 — Produce Core vendor documents
1. Produce and submit `QLT-006` Supplier Quality Plan, `QLT-003` Inspection and Test Plan with explicit ASME hold/witness points for the pressure vessel, `PRQ-013` Logistics / Shipping Plan, `PRQ-015` SPIR, and supporting quality documents as design and manufacturing milestones permit.
2. Track each submittal on the Vendor Document Index (Step 1).

### Step 4 — Produce discipline engineering documents
1. Mechanical — pressure vessel (V-3900-1): vessel design report (ASME BPVC Section VIII calculations); nozzle schedule; weld map and NDE plan; general arrangement; foundation/saddle loads; lifting and transport drawings; IOM manual.
2. Mechanical — rotating equipment (P-3900-1): pump data sheet; performance curve; mechanical seal arrangement; bearing/lubrication data; coupling/baseplate drawings; foundation loads; alignment and grout instructions; IOM manual.
3. Electrical: pump-motor data sheet; area-classification certificate; grounding/bonding terminations at the skid edge.
4. I&C: instrument schedules and data sheets (level, pressure, temperature, level-trip); control schematics; alarm/trip schedules; junction-box drawings.
5. Process / piping interfaces: vendor scope-of-supply piping drawings with termination points and ratings; relief/flare/vent nozzle data (consistent with the 508 mm / 20 in LP header per DBM line 2029); drain/containment terminations.
6. Structural: skid/saddle structural calculations; anchor-bolt drawings; foundation interface drawings.
7. Each document cites its governing standards (see Specification R-12). Where standards are not yet known (per HRR-055-05-002), mark `location TBD`.

### Step 5 — Execute and document FAT and quality records
1. Execute pressure-vessel hydrostatic test per ASME and record on the Manufacturer's Data Report (U-1A as applicable). Issue ASME nameplate rubbing or photograph.
2. Issue NDE records (radiography, dye penetrant, magnetic particle as applicable) per the ITP (`QLT-003`).
3. Execute pump performance/witness test per the applicable API code and issue `MEC-022` equivalent Equipment FAT / Performance Test Report for P-3900-1.
4. Execute Module 390-1 integrated FAT (ASSUMPTION; consistent with shop-built modularization basis) and issue the corresponding FAT report.
5. Issue `QLT-013` Material Test Reports / Certificates as they are accumulated through fabrication (vessel plate MTRs, pump casing MTRs, weld consumable certificates).
6. Issue `QLT-020` Inspection Release Certificate prior to shipment for the module.
7. Compile `QLT-021` Manufacturing Record Book / Vendor Data Book per equipment item or per module (per `DOC-008` decision).

### Step 6 — Ship and turn over
1. Execute the Logistics / Shipping Plan (`PRQ-013`) for Module 390-1 (pressure vessel and pump skid integrated); record lift, transport, and field-storage requirements.
2. Issue final turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation, each containing the ASME Data Report for the pressure vessel.
3. Issue as-built drawings as final revisions.
4. Submit the final Vendor Document Index (`PRQ-009`) reflecting all closed transmittals.
5. Hand off to EPC Integrator for `DEL-055-06` review.

### Step 7 — Close-out
1. Address EPC Integrator review comments raised in `DEL-055-06`.
2. Re-issue revisions and update the Index.
3. Confirm all lines on the Index are either CLOSED or N/A with rationale.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Index completeness | Compare `PRQ-009` against `_Sources/26020-Package_Requirements.docx` Core vendor documents list and applicable discipline lines (per HRR-055-05-001, re-validate once docx slice is accessible). | Reviewed `PRQ-009` revision |
| Per-tag / per-module coverage | Index covers both equipment tags (V-3900-1, P-3900-1) and the integrated Module 390-1. | Reviewed `PRQ-009` revision |
| Document Control Procedure in place | Confirm `DOC-008` issued before any document submittal. | `DOC-008` rev baseline |
| Quality records present | Confirm `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021` issued. | Document register entries |
| ASME pressure-vessel records | Confirm ASME Manufacturer's Data Report (U-1A) and hydrostatic test certificate issued for V-3900-1. | Signed Data Report and hydrostatic certificate |
| Pump performance records | Confirm `MEC-022` equivalent issued for P-3900-1. | Signed performance test report |
| Module FAT records | Confirm Module 390-1 integrated FAT report issued. | Signed module FAT report |
| Logistics / spares present | Confirm `PRQ-013`, `PRQ-015` issued. | Document register entries |
| Standards traceability | Each engineered document cites governing standards (or marks `location TBD` per HRR-055-05-002). | Document QA review |
| Interface coverage | Each interface type applicable to the package has at least one vendor document addressing it. | Reviewed `PRQ-009` revision with interface annotation |
| Acceptance | EPC Integrator acceptance via `DEL-055-06`. | `DEL-055-06` acceptance evidence |
| Status hygiene | All Index lines CLOSED or marked N/A with rationale. | Final `PRQ-009` rev |

## Records

- Vendor Document Index `PRQ-009` — final revision
- Vendor Document Control Procedure `DOC-008` — final revision
- Supplier Quality Plan `QLT-006`
- Inspection and Test Plan `QLT-003` (with ASME hold/witness points)
- Material Test Reports / Certificates `QLT-013` (vessel plate, pump casing, weld consumables)
- Inspection Release Certificate `QLT-020`
- Manufacturing Record Book / Vendor Data Book `QLT-021`
- ASME Manufacturer's Data Report (U-1A) for V-3900-1
- Hydrostatic Test Certificate for V-3900-1
- NDE Records (radiography, dye penetrant, magnetic particle) per ITP
- Pump Performance / FAT Report for P-3900-1 (`MEC-022` equivalent)
- Module 390-1 Integrated FAT Report
- Logistics / Shipping Plan `PRQ-013`
- SPIR `PRQ-015`
- Vendor Data Book / Final Supplier Documentation `PRQ-016`
- Mechanical Final Documentation `MEC-023`
- As-built drawings (general arrangement, foundation/saddle interface, piping termination details)
- Transmittal log and review-cycle disposition records
