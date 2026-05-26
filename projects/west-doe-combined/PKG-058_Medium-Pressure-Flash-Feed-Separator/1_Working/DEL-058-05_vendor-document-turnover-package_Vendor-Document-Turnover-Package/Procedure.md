# Procedure — DEL-058-05 Vendor Document Turnover Package (PKG-058)

## Purpose

Operational steps to produce, submit, and turn over the vendor documentation set for the PKG-058 Medium Pressure Flash Feed Separator (MPFF) package. This procedure addresses both production of the deliverable artifact (the document set) and the controlled submittal cycle that delivers it to the EPC Integrator for acceptance via `DEL-058-06`.

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`. Practical upstream context: the EPC Scope of Work (`DEL-058-01`) and Package Datasheet (`DEL-058-02`) define what the Package Vendor is engineering; the engineered package (`DEL-058-04`) produces the physical basis the turnover records document.
- Accessible source set:
  - `_Sources/26020-Package_Requirements.docx` (Vendor Engineering Deliverables list and MPFF package heading 13)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF process basis: lines 658, 668, 672, 674)
  - Gate 7 PROJECT_DECOMP snapshot (DELIVERABLE_REGISTER and PACKAGE_REGISTER)
- Vendor Document Control Procedure (`DOC-008`) and Vendor Document Index (`PRQ-009`) baselined before any document is submitted.
- EPC Integrator named reviewer assigned for `DEL-058-06`.
- Conflict Table entries HRR-058-05-001 through HRR-058-05-005 surfaced to the integrator for ruling or carried as ASSUMPTION until resolved.

## Steps

### Step 1 — Baseline the Vendor Document Index
1. Instantiate `PRQ-009` for PKG-058 using `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" as the template.
2. Mark each line APPLICABLE / N/A with a short rationale (see Guidance principle 2 and Specification R-4 through R-7).
3. Reflect the per-discipline applicability call (Mechanical lead, with pressure-equipment, I&C, electrical-for-enclosure, piping, structural, civil interface) in the Index revision baseline.
4. Capture train-count disposition (per HRR-058-05-001).

### Step 2 — Baseline the Document Control Procedure
1. Issue `DOC-008` describing document numbering, revisioning, transmittal mechanics, submittal milestones, and review-cycle handling.
2. Reflect the named milestones (preliminary, certified-for-construction, as-built) consistent with the package PO.

### Step 3 — Produce Core vendor documents
1. Produce and submit `QLT-006` Supplier Quality Plan, `QLT-003` ITP (with hydrotest, NDE, mechanical FAT hold/witness points), `PRQ-013` Logistics / Shipping Plan, `PRQ-015` SPIR, and supporting quality documents as design and manufacturing milestones permit.
2. Track each submittal on the Vendor Document Index (Step 1).

### Step 4 — Produce discipline engineering documents
1. Mechanical / pressure equipment: produce `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-024`, `MEC-025`, plus the pressure-vessel package (vessel datasheet, design calculations, NDE reports, hydrotest record, manufacturer's data report or jurisdictional registration evidence per Specification R-4 and HRR-058-05-002).
2. I&C: produce `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009` and remaining INS line items per source, covering level/pressure control, overhead PCV to SOC, automated blowdown valve, and methanol-injection tie-ins.
3. Electrical / enclosure: produce `ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-017` (lighting if integral), `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`.
4. Piping / structural / civil interface: produce skid-edge piping isometrics, line lists, supports drawings, structural calculations, anchor-bolt details, civil loadings package.
5. Each document cites its governing standards (see Specification R-13). Where standards are not yet known (HRR-058-05-002), mark `location TBD`.

### Step 5 — Execute and document FAT
1. Execute the mechanical FAT per `MEC-021` procedure (vessel hydrotest, internals install verification, instrument hookup verification, blowdown valve cycling).
2. Issue `MEC-022` Equipment FAT / Performance Test Report.
3. Issue applicable electrical FAT/energization records for the enclosure (`ELE-029`/`ELE-030`) if integral electrical scope warrants.
4. Issue `QLT-020` Inspection Release Certificate prior to shipment.
5. Issue `QLT-013` Material Test Reports / Certificates as accumulated through fabrication.
6. Compile `QLT-021` Manufacturing Record Book / Vendor Data Book.

### Step 6 — Ship and turn over
1. Execute the Logistics / Shipping Plan (`PRQ-013`).
2. Issue final turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation.
3. Issue as-built mechanical, piping, I&C, and electrical drawings as final revisions.
4. Submit the final Vendor Document Index (`PRQ-009`) reflecting all closed transmittals.
5. Hand off to EPC Integrator for `DEL-058-06` review.

### Step 7 — Close-out
1. Address EPC Integrator review comments raised in `DEL-058-06`.
2. Re-issue revisions and update the Index.
3. Confirm all lines on the Index are either CLOSED or N/A with rationale.
4. Surface any remaining Conflict Table entries to the EPC Integrator for ruling.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Index completeness | Compare `PRQ-009` against `_Sources/26020-Package_Requirements.docx` Core vendor documents list and applicable discipline lines. | Reviewed `PRQ-009` revision |
| Document Control Procedure in place | Confirm `DOC-008` issued before any document submittal. | `DOC-008` rev baseline |
| Pressure-vessel certification | Confirm vessel design calculations, NDE reports, hydrotest record, MDR or jurisdictional registration delivered. | Pressure-vessel package contents |
| Quality records present | Confirm `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021` issued. | Document register entries |
| Logistics / spares present | Confirm `PRQ-013`, `PRQ-015` issued. | Document register entries |
| FAT records present | Confirm `MEC-021`/`MEC-022` (and `ELE-029`/`ELE-030` if applicable) issued. | Signed FAT records |
| Process-basis traceability | Cross-read vendor documents against DBM lines 668, 672, 674; record any deviation. | Cross-reference register |
| Standards traceability | Each engineered document cites governing standards (or marks `location TBD` per HRR-058-05-002). | Document QA review |
| Acceptance | EPC Integrator acceptance via `DEL-058-06`. | `DEL-058-06` acceptance evidence |
| Status hygiene | All Index lines CLOSED or marked N/A with rationale. | Final `PRQ-009` rev |

## Records

- Vendor Document Index `PRQ-009` — final revision
- Vendor Document Control Procedure `DOC-008` — final revision
- Supplier Quality Plan `QLT-006`
- Inspection and Test Plan `QLT-003`
- Material Test Reports / Certificates `QLT-013`
- Inspection Release Certificate `QLT-020`
- Manufacturing Record Book / Vendor Data Book `QLT-021`
- Logistics / Shipping Plan `PRQ-013`
- SPIR `PRQ-015`
- Vendor Data Book / Final Supplier Documentation `PRQ-016`
- Mechanical Final Documentation `MEC-023`
- Mechanical FAT / Performance Test Report `MEC-022`
- Pressure-vessel manufacturer's data report or jurisdictional registration evidence
- Hydrotest record, NDE reports, design calculations
- Skid-edge piping isometrics; structural drawings and calculations; civil loadings package
- As-built drawing set (mechanical, piping, I&C, electrical)
- Transmittal log and review-cycle disposition records
