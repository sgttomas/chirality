# Procedure — DEL-098-05 Vendor Document Turnover Package

This procedure describes how to **produce** the Vendor Document Turnover Package as a controlled deliverable for PKG-098 Tanks, Sour Water (API 650) 3-25. Operational use of the turnover documents (operate, maintain, retrieve) is downstream and is governed by the EPC Integrator's document control standard.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot for PKG-098 (referenced in `_REFERENCES.md`).
- Package Vendor identified and engaged for `26020-03-PT-19-007 - Tanks, Sour Water`.
- DEL-098-01 (Scope of Work) and DEL-098-02 (Package Datasheet) available for vendor handoff (declared upstream context; no `_DEPENDENCIES.md` hard upstream edges were declared during PREPARATION).
- `26020-Package_Requirements.docx` heading 50 (Vendor Engineering Deliverables table) available to the vendor.
- EPC Integrator document control standard and numbering convention available to the vendor. TBD: standard not in source slice.
- API 650 (vendor copy) and project specifications register.

## Steps

1. Establish the vendor document index.
   - The Package Vendor compiles the Vendor Document Index (PRQ-009) from the full ARTIFACT_REGISTER row set for DEL-098-05, organized by the source categories (Core vendor documents; Core package engineering; Storage tanks; Relief / flare / vent design; Process piping interfaces; Drainage / containment interfaces; Electrical / grounding; Cathodic protection; Instrumentation and controls; Structural / access; Civil grading / spill containment).
   - Each row carries: document number, title, revision, status, originator, date issued, transmittal reference.

2. Issue document control governance.
   - Vendor publishes the Vendor Document Control Procedure (DOC-008) covering numbering, revision, transmittal, hold/release status, and final-as-built handling.
   - EPC Integrator reviews and accepts before any technical document is issued for review.

3. Issue quality governance.
   - Supplier Quality Plan (QLT-006) and ITP (QLT-003) submitted and accepted before fabrication start.
   - Hold/witness/notify points recorded in the ITP align with REQ-04 and REQ-05.

4. Produce and submit Core package engineering documents.
   - MEC-001 Mechanical Design Basis includes Item No. 2 operating temperature proposal (CT-03 in `Guidance.md`).
   - MEC-002 Mechanical Equipment List confirms tank count and driver disposition (CT-02, CT-04).
   - MEC-003 Mechanical Equipment Data Sheets carry tank-by-tank data.
   - Package Equipment Specifications, Mechanical Calculation Package, Equipment GA, Installation/Setting Drawings, Lifting/Handling Study, FAT Procedure issued per the index.

5. Produce and submit Storage tank documents.
   - Static Equipment Specifications and Storage Tank Data Sheets reflect modified API 650 with a deviation register (CT-01).
   - Coating (Devchem 253), external insulation with electric heating, and Kennilworth HCL float skim system reflected on data sheets and IOM (REQ-10, REQ-11, REQ-12).

6. Produce and submit interface-side documents per interface category in INTERFACE_REGISTER for PKG-098.
   - Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.
   - Each interface uses the document set called out in `Datasheet.md` Construction section for that category.

7. Execute fabrication, FAT, and inspection.
   - Material certificates collected (QLT-013).
   - FAT performed per Equipment FAT / Performance Test Procedure; results captured in Equipment FAT / Performance Test Report.
   - Inspection Release Certificate (QLT-020) issued per tank.

8. Prepare and submit shipping documents.
   - Logistics / Shipping Plan (PRQ-013).
   - SPIR (PRQ-015).

9. Compile turnover records.
   - Manufacturing Record Book / Vendor Data Book (QLT-021) assembled per tank or per package per DOC-008.
   - Vendor Data Book / Mechanical Final Documentation and Vendor Data Book / Final Supplier Documentation (PRQ-016) assembled and transmitted as the final turnover record.
   - Mechanical Equipment IOM Manual and Mechanical Spares / Special Tools Requirements included in the final book.

10. EPC Integrator interface and integration review.
    - EPC Integrator reviews each submittal against DEL-098-02 (datasheet), DEL-098-01 (scope of work), DEL-098-06 (EPC vendor package review and acceptance).
    - Conflicts in `Guidance.md` Conflict Table are pursued to ruling; rulings recorded in DEL-098-06 and reflected in the vendor's revised submittals before turnover is accepted.

11. Issue final turnover.
    - Final Vendor Document Index (PRQ-009) reissued at "as-built / as-turned-over" status.
    - Vendor Data Book / Final Supplier Documentation (PRQ-016) issued.
    - EPC Integrator records acceptance.

## Verification

| Check | Method | Pass condition |
|---|---|---|
| Index completeness | Compare current PRQ-009 against the full ARTIFACT_REGISTER row set for DEL-098-05. | Every artifact present with current revision and status. |
| Document control compliance | Sample 10 percent of transmittals against DOC-008. | All sampled transmittals conform. |
| Pre-fabrication QA | QLT-006 and QLT-003 accepted before fabrication start. | Date of acceptance precedes fabrication start. |
| Material traceability | MTRs cross-checked against tank BOM and welded components. | Full traceability with no gaps. |
| Per-tank release | One QLT-020 per shipped tank. | Count matches shipment count. |
| FAT closure | FAT Report references FAT Procedure and ITP; any nonconformance dispositioned. | All nonconformances closed before turnover. |
| Interface set completeness | Each interface in INTERFACE_REGISTER for PKG-098 has at least one accepted document per category. | All categories covered. |
| Final turnover | PRQ-016 assembled and accepted; MRB included; SPIR included; IOM included. | Single consolidated turnover record. |
| Conflict Table closure | Each Conflict Table row in `Guidance.md` either ruled by human or carried as open item in DEL-098-06. | No silently dropped conflicts. |

## Records

The following artifacts constitute the records this procedure produces (per `_CONTEXT.md` Anticipated Artifacts and ARTIFACT_REGISTER for DEL-098-05):

- Vendor Document Index (PRQ-009), final revision.
- Vendor Document Control Procedure (DOC-008).
- Supplier Quality Plan (QLT-006); ITP (QLT-003); MTRs (QLT-013); Inspection Release Certificates (QLT-020); Manufacturing Record Book / Vendor Data Book (QLT-021).
- Logistics / Shipping Plan (PRQ-013); SPIR (PRQ-015); Vendor Data Book / Final Supplier Documentation (PRQ-016).
- Mechanical Design Basis (MEC-001); Mechanical Equipment List (MEC-002); Mechanical Equipment Data Sheets (MEC-003); plus the package engineering, storage tank, relief/flare/vent, process piping, drainage/containment, electrical/grounding, cathodic protection, instrumentation, structural/access, and civil grading interface documents enumerated in `Datasheet.md`.
- Equipment FAT / Performance Test Procedure and Report.
- Mechanical Equipment IOM Manual; Mechanical Spares / Special Tools Requirements.
- Conflict Table rulings (carried through DEL-098-06 acceptance record).

Storage location: package folder `1_Working/DEL-098-05_vendor-document-turnover-package_Vendor-Document-Turnover-Package` during production; promoted to `2_Checking` and `3_Issued` per the package lifecycle.
