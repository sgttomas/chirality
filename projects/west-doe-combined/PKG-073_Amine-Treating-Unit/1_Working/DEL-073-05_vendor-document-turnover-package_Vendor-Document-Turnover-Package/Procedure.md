# Procedure — DEL-073-05 Vendor Document Turnover Package (PKG-073)

## Purpose

Operational steps to produce, submit, and turn over the vendor documentation set for the PKG-073 Amine Treating Unit package. This procedure addresses both production of the deliverable artifact (the document set) and the controlled submittal cycle that delivers it to the EPC Integrator for acceptance via `DEL-073-06`.

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` (PREPARATION did not declare upstream edges for this deliverable). Practical upstream context: the EPC Scope of Work (`DEL-073-01`) and Package Datasheet (`DEL-073-02`) define what the Package Vendor is engineering; the engineered package (`DEL-073-04`) produces the physical basis the turnover records document.
- Accessible source set:
  - `_Sources/26020-Package_Requirements.docx` — heading 27 "26020-01-PT-27-001 - Amine Treating Unit" (Vendor Engineering Deliverables list, Basic Scope, Physical Interface Summary)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (facility design basis, site ambient and MDEA function context)
  - Gate 7 PROJECT_DECOMP snapshot (`PACKAGE_REGISTER.csv` row 49, `DELIVERABLE_REGISTER.csv` row 262)
- Inaccessible but referenced: `Bid Docs/Budgetary/26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx` (not present under `_Sources/`; see HRR-073-05-003).
- Vendor Document Control Procedure (`DOC-008`) and Vendor Document Index (`PRQ-009`) baselined before any document is submitted.
- EPC Integrator named reviewer assigned for `DEL-073-06`.
- Package PO defines submittal cadence and native-file format requirements (HRR-073-05-002) prior to vendor mobilization.

## Steps

### Step 1 — Baseline the Vendor Document Index
1. Instantiate `PRQ-009` for PKG-073 using `_Sources/26020-Package_Requirements.docx` heading 27 "Vendor Engineering Deliverables" as the template.
2. Populate the index with the document classes enumerated in source heading 27 (see Datasheet "Construction" section for the full enumeration).
3. For each line, record APPLICABLE / N/A with a brief rationale (see Guidance principle 2 and Specification R-4 through R-12).

### Step 2 — Baseline the Document Control Procedure
1. Issue `DOC-008` describing document numbering, revisioning convention, transmittal mechanics, submittal milestones, and review-cycle handling.
2. Reflect named milestones (preliminary, certified-for-construction, as-built) consistent with the package PO (HRR-073-05-002).
3. Reflect pressure-equipment registration sequencing under `REG-022` (jurisdiction TBD).

### Step 3 — Produce Core vendor documents and process design baseline
1. Produce and submit `QLT-006` Supplier Quality Plan, `QLT-003` ITP, `PRQ-013` Logistics / Shipping Plan, `PRQ-015` SPIR.
2. Issue process baseline: `PRO-004` PFD, `PRO-005` Heat and Material Balance, `PRO-007` Process Description / Operating Philosophy, `PRO-008` P&IDs, `PRO-010` Major Equipment Process Data Sheets, `PRO-011` Utility Summary, `PRO-012` Line Sizing, `PRO-020` Process Control Philosophy.
3. Issue relief/flare/vent design baseline: `PRO-014` Relief and Flare Design Basis, `PRO-015` PSV / Pressure Relief Sizing, `PRO-016` Relief Valve Data Sheets, `PRO-017` Flare Load Summary, `PRO-018` Blowdown / Depressurization Study. Coordinate with facility-level relief/flare basis (interface obligation).
4. Track each submittal on the Vendor Document Index.

### Step 4 — Produce mechanical and pressure-equipment documents
1. Mechanical core: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-014`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-024`, `MEC-025`.
2. Static pressure equipment: `MEC-005`, `MEC-009`, and `REG-022` Pressure Equipment Registration Package (jurisdiction-specific; sequence per `DOC-008`).
3. Each document cites its governing standards (see Specification R-14). Where standards are not yet known (per HRR-073-05-001), mark `location TBD`.
4. Address sour-service materials, welding, inspection, and PWHT requirements (Guidance principle 6) explicitly in `MEC-005`, `MEC-009`, and applicable ITP entries.

### Step 5 — Produce piping, drainage, electrical, I&C, F&G, structural documents
1. Piping interfaces: `PIP-003`, `PIP-004`, `PIP-006`, `PIP-007`, `PIP-008`, `PIP-009`, `PIP-017`, `PIP-018`, `PIP-024`, `PIP-025`.
2. Drainage/containment: `PRO-023`, `CIV-014`.
3. Electrical / lighting / EHT / grounding: `ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-017`, `ELE-018`, `PIP-020`, `PIP-021`, `ELE-012`, `ELE-019`. (Note: `ELE-011` Motor Starting Study not in source; add only if detailed design surfaces motors warranting it per HRR-073-05-005.)
4. I&C: `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, `INS-010`, `INS-011`, `INS-016`, `INS-017`, `INS-018`, `INS-025`, `CTL-003`, `CTL-005`, `CTL-006`, `CTL-026`.
5. Fire and gas / technical safety: `TSF-002`, `TSF-003`, `TSF-004`, `TSF-009`, `TSF-011`, `TSF-013`, `TSF-028`.
6. Structural: `STR-001`, `STR-002`, `STR-004`, `STR-005`, `STR-006`, `STR-011`, `STR-012`, `STR-013`, `STR-014`, `STR-020`.

### Step 6 — Issue process safety and HAZOP inputs
1. Issue `PRO-026` HAZOP / PHA Technical Input Package and `PRO-027` Process Safety Information (PSI) Package before HAZOP review milestones.
2. Issue `PRO-025` Operating Guidelines / Startup-Shutdown Narrative.
3. Reflect HAZOP closure actions in revised `PRO-008` P&IDs and applicable `CTL-005` Cause-and-Effect Matrix.

### Step 7 — Execute and document FAT
1. Execute the FAT per `MEC-021` (mechanical) and `ELE-029` (electrical).
2. Issue `MEC-022` Equipment FAT / Performance Test Report and `ELE-030` Electrical Test Records / Energization Package.
3. Issue `QLT-020` Inspection Release Certificate prior to shipment.
4. Issue `QLT-013` Material Test Reports / Certificates as they are accumulated through fabrication.
5. Compile `QLT-021` Manufacturing Record Book / Vendor Data Book.

### Step 8 — Ship and turn over
1. Execute the Logistics / Shipping Plan (`PRQ-013`).
2. Issue final turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation.
3. Issue as-built drawings: `PIP-028` Piping As-Built, `INS-029` Instrument As-Built, `PRO-028` Process As-Built PFD/P&ID Package.
4. Submit the final Vendor Document Index (`PRQ-009`) reflecting all closed transmittals.
5. Hand off to EPC Integrator for `DEL-073-06` review.

### Step 9 — Close-out
1. Address EPC Integrator review comments raised in `DEL-073-06`.
2. Re-issue revisions and update the Index.
3. Confirm all lines on the Index are either CLOSED or N/A with rationale.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Index completeness | Compare `PRQ-009` against `_Sources/26020-Package_Requirements.docx` heading 27 Core vendor documents list and applicable discipline lines. | Reviewed `PRQ-009` revision |
| Document Control Procedure in place | Confirm `DOC-008` issued before any document submittal. | `DOC-008` rev baseline |
| Quality records present | Confirm `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021` issued. | Document register entries |
| Logistics / spares present | Confirm `PRQ-013`, `PRQ-015` issued. | Document register entries |
| Process baseline present | Confirm `PRO-004`, `PRO-005`, `PRO-007`, `PRO-008`, `PRO-010`, `PRO-011`, `PRO-012`, `PRO-020`, `PRO-025` issued. | Document register entries |
| Relief/flare/blowdown reconciled | Confirm `PRO-014`, `PRO-015`, `PRO-016`, `PRO-017`, `PRO-018` issued and reconciled with facility-level relief/flare basis. | Interface review record |
| Pressure equipment registration | Confirm `REG-022` issued for the applicable jurisdiction; pressure vessel data sheets `MEC-009` complete. | `REG-022` package; regulator correspondence |
| FAT/SAT records present | Confirm `MEC-021`/`MEC-022` and `ELE-029`/`ELE-030` issued. | Signed FAT/SAT records |
| HAZOP/PSI present | Confirm `PRO-026`, `PRO-027` issued and HAZOP closure actions reflected in revised P&IDs and C&E. | HAZOP closure log |
| As-builts present | Confirm `PIP-028`, `INS-029`, `PRO-028` issued. | As-built drawing register |
| Standards traceability | Each engineered document cites governing standards (or marks `location TBD` per HRR-073-05-001). | Document QA review |
| Acceptance | EPC Integrator acceptance via `DEL-073-06`. | `DEL-073-06` acceptance evidence |
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
- Pressure Equipment Registration Package `REG-022`
- Process Safety Information (PSI) Package `PRO-027`
- HAZOP / PHA Technical Input Package `PRO-026`
- As-built `PIP-028`, `INS-029`, `PRO-028`
- Transmittal log and review-cycle disposition records
