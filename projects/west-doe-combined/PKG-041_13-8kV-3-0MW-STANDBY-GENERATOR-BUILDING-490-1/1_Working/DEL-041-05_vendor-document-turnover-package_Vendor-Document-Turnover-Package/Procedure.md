# Procedure — DEL-041-05 Vendor Document Turnover Package (PKG-041)

## Purpose

Operational steps to produce, submit, and turn over the vendor documentation set for the PKG-041 13.8kV, 3.0MW Standby Generator Building (490-1) package. This procedure addresses both production of the deliverable artifact (the document set) and the controlled submittal cycle that delivers it to the EPC Integrator for acceptance via `DEL-041-06`.

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` (PREPARATION did not declare upstream edges for this deliverable). Practical upstream context: the EPC Scope of Work (`DEL-041-01`) and Package Datasheet (`DEL-041-02`) define what the Package Vendor is engineering; the engineered package (`DEL-041-04`) produces the physical basis the turnover records document.
- Accessible source set:
  - `_Sources/26020-Package_Requirements.docx` (Vendor Engineering Deliverables list)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (emergency-power and 490-1 module basis; lines 2076–2083, 2787, 2943, 3086)
  - Gate 7 PROJECT_DECOMP snapshot (`PACKAGE_REGISTER.csv` row 43, `DELIVERABLE_REGISTER.csv` row 232)
- Vendor Document Control Procedure (`DOC-008`) and Vendor Document Index (`PRQ-009`) baselined before any document is submitted.
- EPC Integrator named reviewer assigned for `DEL-041-06`.
- Rating-basis reconciliation (HRR-041-05-001) acknowledged: vendor documentation will report as-engineered ratings; package title remains nominal until EPC Integrator confirms.

## Steps

### Step 1 — Baseline the Vendor Document Index
1. Instantiate `PRQ-009` for PKG-041 using `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" as the template.
2. Mark each line APPLICABLE / N/A with a short rationale (see Guidance principle 2 and Specification R-4 through R-6).
3. Annotate the Index header with the rating-basis source (per HRR-041-05-001) and the standby-power architecture status (per HRR-041-05-004).
4. Reflect the per-discipline applicability call in the Index revision baseline.

### Step 2 — Baseline the Document Control Procedure
1. Issue `DOC-008` describing document numbering, revisioning convention, transmittal mechanics, submittal milestones, and review-cycle handling.
2. Reflect the named milestones (e.g., preliminary, certified-for-construction, as-built) consistent with the package PO.
3. Note any cold-climate / outdoor-enclosure-specific document expectations (heating, fuel, battery/charger sizing, lift provisions) per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2076.

### Step 3 — Produce Core vendor documents
1. Produce and submit `QLT-006` Supplier Quality Plan, `QLT-003` ITP, `PRQ-013` Logistics / Shipping Plan, `PRQ-015` SPIR, and supporting quality documents as design and manufacturing milestones permit.
2. Track each submittal on the Vendor Document Index (Step 1).

### Step 4 — Produce discipline engineering documents
1. Electrical: produce `ELE-002`, `ELE-003`, `ELE-012`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, plus `ELE-011` if package-internal motor starting studies are warranted; `ELE-017` for integral lighting.
2. I&C: produce `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009` and remaining INS line items per source applicable to genset controls/monitoring/trip interfaces.
3. Mechanical (packaged equipment and enclosure): produce `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-024`, `MEC-025`.
4. Structural (enclosure/skid/anchoring): produce the applicable structural document subset per `DEL-041-06` confirmation.
5. HVAC / building services / fire & gas interface: produce ventilation, heating, lighting, and F&G interface documents as integral to the module.
6. Each document cites its governing standards (see Specification R-11). Where standards are not yet known (per HRR-041-05-002), mark `location TBD`.
7. Each engineered document reports as-engineered generator rating, terminal voltage, and connection scheme (per HRR-041-05-001, R-13).

### Step 5 — Execute and document FAT
1. Execute the FAT per `ELE-029` and `MEC-021` procedures.
2. Issue `ELE-030` Electrical Test Records / Energization Package and `MEC-022` Equipment FAT / Performance Test Report.
3. Issue `QLT-020` Inspection Release Certificate prior to shipment.
4. Issue `QLT-013` Material Test Reports / Certificates as they are accumulated through fabrication.
5. Compile `QLT-021` Manufacturing Record Book / Vendor Data Book.

### Step 6 — Ship and turn over
1. Execute the Logistics / Shipping Plan (`PRQ-013`); the shipping plan addresses the shop-fabricated module form factor (per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2787).
2. Issue final turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation.
3. Issue as-built electrical, I&C, mechanical, and structural drawings as final revisions.
4. Submit the final Vendor Document Index (`PRQ-009`) reflecting all closed transmittals.
5. Hand off to EPC Integrator for `DEL-041-06` review.

### Step 7 — Close-out
1. Address EPC Integrator review comments raised in `DEL-041-06`, including rating-basis reconciliation (HRR-041-05-001) and standards list confirmation (HRR-041-05-002).
2. Re-issue revisions and update the Index.
3. Confirm all lines on the Index are either CLOSED or N/A with rationale.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Index completeness | Compare `PRQ-009` against `_Sources/26020-Package_Requirements.docx` Core vendor documents list and applicable discipline lines. | Reviewed `PRQ-009` revision |
| Document Control Procedure in place | Confirm `DOC-008` issued before any document submittal. | `DOC-008` rev baseline |
| Quality records present | Confirm `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021` issued. | Document register entries |
| Logistics / spares present | Confirm `PRQ-013`, `PRQ-015` issued. | Document register entries |
| FAT/SAT records present | Confirm `ELE-029` / `ELE-030` and `MEC-021`/`MEC-022` issued. | Signed FAT/SAT records |
| Standards traceability | Each engineered document cites governing standards (or marks `location TBD` per HRR-041-05-002). | Document QA review |
| Rating-basis annotation | Vendor Document Index carries the as-engineered rating annotation and the package-title-source note (HRR-041-05-001). | Final `PRQ-009` header |
| Acceptance | EPC Integrator acceptance via `DEL-041-06`. | `DEL-041-06` acceptance evidence |
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
- Electrical Test Records / Energization Package `ELE-030`
- Mechanical FAT / Performance Test Report `MEC-022`
- As-built electrical, I&C, mechanical, and structural drawings
- Transmittal log and review-cycle disposition records
