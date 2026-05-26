# Procedure — DEL-081-05 Vendor Document Turnover Package (PKG-081)

## Purpose

Operational steps to produce, submit, and turn over the vendor documentation set for the PKG-081 HP Flare KO Drum package (two HP flare KO drums and two transfer pumps). This procedure addresses both production of the deliverable artifact (the document set) and the controlled submittal cycle that delivers it to the EPC Integrator for acceptance via `DEL-081-06`.

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` (PREPARATION did not declare upstream edges for this deliverable). Practical upstream context: the EPC Scope of Work (`DEL-081-01`) and Package Datasheet (`DEL-081-02`) define what the Package Vendor is engineering; the engineered package (`DEL-081-04`) produces the physical basis the turnover records document.
- Accessible source set:
  - `_Sources/26020-Package_Requirements.docx` (Vendor Engineering Deliverables list, package heading 34 — binary; specific clauses are TBD pending text extraction)
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 54 — binary)
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (HP KO drum equipment count, sizing context, and transfer-pump configuration)
  - Gate 7 PROJECT_DECOMP snapshot (`PACKAGE_REGISTER.csv` row 54, `DELIVERABLE_REGISTER.csv` DEL-081-05 row)
- Vendor Document Control Procedure (`DOC-008`) and Vendor Document Index (`PRQ-009`) baselined before any document is submitted.
- EPC Integrator named reviewer assigned for `DEL-081-06`.
- ASME Authorized Inspector (AI) engaged for the pressure-vessel ITP hold points (ASSUMPTION; standard for ASME-stamped vessels).

## Steps

### Step 1 — Baseline the Vendor Document Index
1. Instantiate `PRQ-009` for PKG-081 using `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" (package heading 34) as the template.
2. Add a per-tag column or per-tag duplication for the four equipment items (V-4100-2, V-4150-2, P-4100-2, P-4150-2) consistent with the per-tag-vs-consolidated decision recorded in `DOC-008`.
3. Mark each line APPLICABLE / N/A with a short rationale (see Guidance principle 2 and Specification R-4 through R-7).
4. Reflect the per-discipline applicability call in the Index revision baseline.

### Step 2 — Baseline the Document Control Procedure
1. Issue `DOC-008` describing document numbering, revisioning convention, transmittal mechanics, submittal milestones, and review-cycle handling.
2. Reflect the named milestones (e.g., preliminary, certified-for-construction, as-built) consistent with the package PO.
3. Reflect the per-tag-vs-consolidated documentation decision (see Guidance "Trade-offs").

### Step 3 — Produce Core vendor documents
1. Produce and submit `QLT-006` Supplier Quality Plan, `QLT-003` Inspection and Test Plan with explicit ASME hold/witness points for the pressure vessels, `PRQ-013` Logistics / Shipping Plan, `PRQ-015` SPIR, and supporting quality documents as design and manufacturing milestones permit.
2. Track each submittal on the Vendor Document Index (Step 1).

### Step 4 — Produce discipline engineering documents
1. Mechanical — pressure vessel (V-4100-2 and V-4150-2): vessel design report (ASME BPVC Section VIII calculations); nozzle schedule; weld map and NDE plan; general arrangement; foundation/saddle loads; lifting and transport drawings; IOM manual.
2. Mechanical — rotating equipment (P-4100-2 and P-4150-2): pump data sheets; performance curves; mechanical seal arrangement; bearing/lubrication data; coupling/baseplate drawings; foundation loads; alignment and grout instructions; IOM manual.
3. Electrical: pump-motor data sheets; area-classification certificates; grounding/bonding terminations at the skid edge.
4. I&C: instrument schedules and data sheets (level, pressure, temperature, level-trip); control schematics; alarm/trip schedules; junction-box drawings.
5. Process / piping interfaces: vendor scope-of-supply piping drawings with termination points and ratings; relief/flare/vent nozzle data; drain/containment terminations.
6. Structural: skid/saddle structural calculations; anchor-bolt drawings; foundation interface drawings.
7. Each document cites its governing standards (see Specification R-12). Where standards are not yet known (per HRR-081-05-002), mark `location TBD`.

### Step 5 — Execute and document FAT and quality records
1. Execute pressure-vessel hydrostatic test per ASME and record on the Manufacturer's Data Report (U-1A or U-2A as applicable). Issue ASME nameplate rubbing or photograph.
2. Issue NDE records (radiography, dye penetrant, magnetic particle as applicable) per the ITP (`QLT-003`).
3. Execute pump performance/witness test per the applicable API code and issue `MEC-022` equivalent Equipment FAT / Performance Test Report for each pump.
4. Issue `QLT-013` Material Test Reports / Certificates as they are accumulated through fabrication (vessel plate MTRs, pump casing MTRs, weld consumable certificates).
5. Issue `QLT-020` Inspection Release Certificate prior to shipment for each equipment item.
6. Compile `QLT-021` Manufacturing Record Book / Vendor Data Book per equipment item or per train (per `DOC-008` decision).

### Step 6 — Ship and turn over
1. Execute the Logistics / Shipping Plan (`PRQ-013`) for the pressure vessels and pump skids; record lift, transport, and field-storage requirements.
2. Issue final turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation, each containing the ASME Data Reports for the pressure vessels.
3. Issue as-built drawings as final revisions.
4. Submit the final Vendor Document Index (`PRQ-009`) reflecting all closed transmittals.
5. Hand off to EPC Integrator for `DEL-081-06` review.

### Step 7 — Close-out
1. Address EPC Integrator review comments raised in `DEL-081-06`.
2. Re-issue revisions and update the Index.
3. Confirm all lines on the Index are either CLOSED or N/A with rationale.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Index completeness | Compare `PRQ-009` against `_Sources/26020-Package_Requirements.docx` Core vendor documents list and applicable discipline lines (per HRR-081-05-001, re-validate once docx slice is accessible). | Reviewed `PRQ-009` revision |
| Per-tag coverage | Index covers all four equipment tags (V-4100-2, V-4150-2, P-4100-2, P-4150-2). | Reviewed `PRQ-009` revision |
| Document Control Procedure in place | Confirm `DOC-008` issued before any document submittal. | `DOC-008` rev baseline |
| Quality records present | Confirm `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021` issued. | Document register entries |
| ASME pressure-vessel records | Confirm ASME Manufacturer's Data Reports (U-1A/U-2A) and hydrostatic test certificates issued for V-4100-2 and V-4150-2. | Signed Data Reports and hydrostatic certificates |
| Pump performance records | Confirm `MEC-022` equivalent issued for P-4100-2 and P-4150-2. | Signed performance test reports |
| Logistics / spares present | Confirm `PRQ-013`, `PRQ-015` issued. | Document register entries |
| Standards traceability | Each engineered document cites governing standards (or marks `location TBD` per HRR-081-05-002). | Document QA review |
| Interface coverage | Each interface type listed on `PACKAGE_REGISTER.csv` row 54 has at least one vendor document addressing it. | Reviewed `PRQ-009` revision with interface annotation |
| Acceptance | EPC Integrator acceptance via `DEL-081-06`. | `DEL-081-06` acceptance evidence |
| Status hygiene | All Index lines CLOSED or marked N/A with rationale. | Final `PRQ-009` rev |

## Records

- Vendor Document Index `PRQ-009` — final revision
- Vendor Document Control Procedure `DOC-008` — final revision
- Supplier Quality Plan `QLT-006`
- Inspection and Test Plan `QLT-003` (with ASME hold/witness points)
- Material Test Reports / Certificates `QLT-013` (vessel plate, pump casing, weld consumables)
- Inspection Release Certificate `QLT-020` (per equipment item)
- Manufacturing Record Book / Vendor Data Book `QLT-021`
- ASME Manufacturer's Data Reports (U-1A or U-2A) for V-4100-2 and V-4150-2
- Hydrostatic Test Certificates for V-4100-2 and V-4150-2
- NDE Records (radiography, dye penetrant, magnetic particle) per ITP
- Pump Performance / FAT Reports for P-4100-2 and P-4150-2 (`MEC-022` equivalent)
- Logistics / Shipping Plan `PRQ-013`
- SPIR `PRQ-015`
- Vendor Data Book / Final Supplier Documentation `PRQ-016`
- Mechanical Final Documentation `MEC-023`
- As-built drawings (general arrangement, foundation/saddle interface, piping termination details)
- Transmittal log and review-cycle disposition records
