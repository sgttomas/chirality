# Procedure — DEL-082-05 Vendor Document Turnover Package

This procedure covers both production of the vendor document turnover package and operation of the document control workflow through to EPC acceptance.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in this deliverable folder.
- Access to source slice: `_Sources/26020-Package_Requirements.docx` section `26020-02-PT-17-002 - Flare KO Drum (Low Pressure)` (package heading 35).
- EPC anchor deliverables for the package available for cross-reference:
  - `DEL-082-01` Scope of Work
  - `DEL-082-02` Package Datasheet
  - `DEL-082-03` Construction Work Package
- Vendor selected and contracted for `DEL-082-04 Vendor Engineered Equipment Package` (the engineering/supply scope this documentation set documents).
- Project document control numbering and transmittal procedures available — **location TBD** (not in locally accessible source).

## Steps

### Step 1 — Initialize Vendor Document Index (PRQ-009)

1. Create the Vendor Document Index from the source-enumerated list in `Datasheet.md` (Construction section).
2. Preserve the source grouping (Core vendor documents; Core package engineering; Rotating equipment / pumps; Static pressure equipment; Relief / flare / vent design; Process piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Instrumentation and controls interfaces; Structural, foundations, supports, access).
3. For each row, assign: document ID, document name, revision, planned issue date, status, vendor responsible engineer, EPC reviewer.
4. Mark rows where vendor's equivalent document title differs from source title; provide the mapping.

### Step 2 — Apply Document Control Procedure (DOC-008)

1. Adopt or submit the Vendor Document Control Procedure governing: numbering, revision codes (e.g., IFR/IFA/IFC/AFC), transmittal cover sheets, review turnaround SLAs, comment dispositions, and re-issue triggers.
2. Confirm alignment with project document control standard (TBD source).

### Step 3 — Submit engineering documents in design-phase tranches

1. Tranche A (design basis): MEC-001, MEC-002, PRO-008 (P&ID issue-for-review), PRO-014 Relief and Flare Design Basis, STR-001 Structural Design Basis.
2. Tranche B (data sheets and calcs): MEC-003, MEC-009 (Pressure Vessel Data Sheet for `V-3900-2`), MEC-007 (Pump Data Sheet for `P-3900-2`), PRO-013 NPSH, PRO-015 PSV sizing, PRO-016 Relief valve data, PRO-017 Flare load summary, PRO-018 Blowdown study, MEC-014 Mechanical Calculations, STR-004/005 Structural and Foundation Calculations.
3. Tranche C (drawings and interfaces): MEC-016 GA, MEC-017 Installation, PIP-003/004/006/007/008/009, INS-002/003/005/006/008/009/010/011, CTL-003/005/006/026, ELE-002/003/014/015/016/020/027/028, STR-002/006/011/012/013.
4. Tranche D (quality and pre-fab): QLT-006 Supplier Quality Plan, QLT-003 ITP, REG-022 Pressure Equipment Registration package submission.

### Step 4 — EPC interface/integration review

1. EPC Integrator reviews each transmittal against `DEL-082-01` SOW, `DEL-082-02` Package Datasheet, and `DEL-082-03` Construction Work Package.
2. Verify boundary at KO drum outlet flange is reflected on P&IDs and tie-in list; reject submittals that show LP flare stack scope inside the package boundary.
3. Verify all "Yes" interface types from the source Physical Interface Summary have at least one supporting submitted document.
4. Log review comments and dispositions in the review log that feeds `DEL-082-06`.

### Step 5 — Fabrication, inspection, and test execution

1. Execute ITP (`QLT-003`) with witness/hold points per Supplier Quality Plan.
2. Collect Material Test Reports/Certificates (`QLT-013`) as material is received and used.
3. Execute equipment FAT/performance test per `MEC-021`; produce `MEC-022` FAT Report.
4. Execute electrical FAT/SAT per `ELE-029`; produce `ELE-030` test records.
5. Issue Inspection Release Certificate (`QLT-020`) authorizing shipment.

### Step 6 — Shipment and site delivery

1. Execute Logistics / Shipping Plan (`PRQ-013`).
2. Issue lifting/handling documents per `MEC-018` and `STR-014` to receiving site.
3. Transmit shipping documents and lift plan to construction.

### Step 7 — Resolve open items

1. Close out the blowdown valve TBD identified in source Scope Notes by issuing revised `INS-017` (On-Off / Shutdown Valve Data Sheet) and/or `INS-016` / `PIP-018`; record resolution in `MEMORY.md`.
2. Close out any other `TBD` rows in the Vendor Document Index before final turnover.

### Step 8 — Final turnover

1. Compile Manufacturing Record Book / Vendor Data Book (`QLT-021`).
2. Compile Mechanical Final Documentation (`MEC-023`) and overall Final Vendor Data Book (`PRQ-016`).
3. Submit SPIR (`PRQ-015`), Spares / Special Tools (`MEC-024`), and IOM (`MEC-025`).
4. Submit as-builts: `PIP-028`, `INS-029`.
5. EPC accepts the turnover package, generating evidence for `DEL-082-06`.

## Verification

| Check | Pass Criterion |
|---|---|
| Vendor Document Index completeness | Every source-enumerated row present, with revision and status |
| Boundary check | KO drum outlet flange shown as package boundary on `PRO-008` P&IDs and `PIP-004` Tie-In List |
| Interface coverage | Each source "Yes" interface type has at least one supporting document submitted |
| Pressure equipment registration | `REG-022` accepted by jurisdiction prior to vessel turnover |
| FAT/SAT acceptance | `MEC-022`, `ELE-030` accepted by EPC reviewer |
| Open-item closure | No `TBD` rows remain in the Vendor Document Index at turnover |
| Turnover books complete | `QLT-021`, `MEC-023`, `PRQ-016` complete and accepted |

## Records

- `PRQ-009` Vendor Document Index (controlled register, all revisions retained)
- All transmittals and EPC review comments/dispositions
- `QLT-013` Material Test Reports / Certificates
- `QLT-020` Inspection Release Certificate
- `QLT-021` Manufacturing Record Book / Vendor Data Book
- `MEC-022` FAT Report; `ELE-030` Electrical Test Records
- `REG-022` Pressure Equipment Registration evidence
- `PRQ-013` Logistics / Shipping Plan execution records
- `PRQ-015` SPIR; `PRQ-016` Final Vendor Data Book
- `PIP-028`, `INS-029` As-Built Drawings
- `MEC-025` IOM Manual
- EPC review log entries (feed `DEL-082-06`)
- Updates to deliverable-local `MEMORY.md` capturing resolved TBDs and human rulings
