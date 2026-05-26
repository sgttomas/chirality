# Procedure — DEL-075-05 Vendor Document Turnover Package (PKG-075)

## Purpose

Operational steps to produce, submit, and turn over the vendor documentation set for the PKG-075 Cryogenic Unit ("Deepcut") package. This procedure addresses both production of the deliverable artifact (the document set) and the controlled submittal cycle that delivers it to the EPC Integrator for acceptance via `DEL-075-06` (ASSUMPTION on the receiving deliverable ID, by package-internal numbering convention).

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` (PREPARATION did not declare upstream edges for this deliverable). Practical upstream context: the EPC Scope of Work (`DEL-075-01`) and Package Datasheet (`DEL-075-02`) define what the Package Vendor is engineering; the engineered package (`DEL-075-04`) produces the physical basis the turnover records document.
- Accessible source set:
  - `_Sources/26020-Package_Requirements.docx` (Vendor Engineering Deliverables list, package heading 29 — Cryogenic Unit)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (facility design basis for the West Doe Deepcut expansion)
  - Gate 7 PROJECT_DECOMP snapshot (`PACKAGE_REGISTER.csv` row 52, `DELIVERABLE_REGISTER.csv` row 280)
- Vendor Document Control Procedure (`DOC-008`) and Vendor Document Index (`PRQ-009`) baselined before any document is submitted.
- EPC Integrator named reviewer assigned for `DEL-075-06`.

## Steps

### Step 1 — Baseline the Vendor Document Index
1. Instantiate `PRQ-009` for PKG-075 using `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" (package heading 29) as the template.
2. Mark each line APPLICABLE / N/A with a short rationale (see Guidance principle 2 and Specification R-4 through R-8).
3. Reflect the per-discipline applicability call in the Index revision baseline.

### Step 2 — Baseline the Document Control Procedure
1. Issue `DOC-008` describing document numbering, revisioning convention, transmittal mechanics, submittal milestones, and review-cycle handling.
2. Reflect the named milestones (e.g., preliminary, certified-for-construction, as-built) consistent with the package PO.

### Step 3 — Produce Core vendor documents
1. Produce and submit `QLT-006` Supplier Quality Plan, `QLT-003` ITP, `PRQ-013` Logistics / Shipping Plan, `PRQ-015` SPIR, and supporting quality documents as design and manufacturing milestones permit.
2. Track each submittal on the Vendor Document Index (Step 1).

### Step 4 — Produce discipline engineering documents
1. Process / Mechanical Equipment / Pressure / Piping: produce `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-024`, `MEC-025` plus PV/PIP set (specific IDs per source template; clause location TBD).
2. Relief / Flare / Vent / Drain / Containment: produce relief device data, package contribution to flare loads, drain/containment basis. Carry flare/incinerator-related deliverables as PRELIMINARY pending flare stack vendor reconciliation (HRR-075-05-001).
3. Electrical: produce `ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`.
4. I&C: produce `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009` and remaining INS line items per source.
5. Civil / Structural: produce foundation, support, and structural-steel documents for vendor-supplied skids/structures.
6. Fire & Gas / HVAC: produce F&G device data and HVAC documents for any vendor-supplied enclosure (mark N/A with rationale if facility-supplied).
7. Each document cites its governing standards (see Specification R-13). Where standards are not yet known (per HRR-075-05-002), mark `location TBD`.

### Step 5 — Execute and document FAT
1. Execute the FAT per `MEC-021` and `ELE-029`.
2. Issue `MEC-022` Equipment FAT / Performance Test Report and `ELE-030` Electrical Test Records / Energization Package.
3. Issue `QLT-020` Inspection Release Certificate prior to shipment.
4. Issue `QLT-013` Material Test Reports / Certificates as they are accumulated through fabrication — non-negotiable for pressure-boundary materials in sour and/or cryogenic service.
5. Compile `QLT-021` Manufacturing Record Book / Vendor Data Book.

### Step 6 — Ship and turn over
1. Execute the Logistics / Shipping Plan (`PRQ-013`).
2. Issue final turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation.
3. Issue as-built process, mechanical, piping, electrical, and I&C drawings as final revisions.
4. Submit the final Vendor Document Index (`PRQ-009`) reflecting all closed transmittals.
5. Hand off to EPC Integrator for `DEL-075-06` review.

### Step 7 — Close-out
1. Address EPC Integrator review comments raised in `DEL-075-06`.
2. Re-issue revisions and update the Index.
3. Reconcile relief/flare deliverables against the flare stack vendor's accepted design (HRR-075-05-001) and upgrade from PRELIMINARY where reconciled.
4. Confirm all lines on the Index are either CLOSED or N/A with rationale.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Index completeness | Compare `PRQ-009` against `_Sources/26020-Package_Requirements.docx` Core vendor documents list and applicable discipline lines for heading 29 (Cryogenic Unit). | Reviewed `PRQ-009` revision |
| Document Control Procedure in place | Confirm `DOC-008` issued before any document submittal. | `DOC-008` rev baseline |
| Quality records present | Confirm `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021` issued. | Document register entries |
| Logistics / spares present | Confirm `PRQ-013`, `PRQ-015` issued. | Document register entries |
| FAT/SAT records present | Confirm `MEC-021`/`MEC-022` and `ELE-029`/`ELE-030` issued. | Signed FAT/SAT records |
| Material traceability | MTRs/Certificates for all pressure-boundary items in sour/cryogenic service. | `QLT-013` records |
| Standards traceability | Each engineered document cites governing standards (or marks `location TBD` per HRR-075-05-002). | Document QA review |
| Relief/flare reconciliation | Relief and flare deliverables reconciled against flare stack vendor's accepted design (HRR-075-05-001). | Reconciliation transmittal |
| Acceptance | EPC Integrator acceptance via `DEL-075-06`. | `DEL-075-06` acceptance evidence |
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
- Electrical Test Records / Energization Package `ELE-030`
- Transmittal log and review-cycle disposition records
- Relief / flare reconciliation transmittal (vs. flare stack vendor design)
