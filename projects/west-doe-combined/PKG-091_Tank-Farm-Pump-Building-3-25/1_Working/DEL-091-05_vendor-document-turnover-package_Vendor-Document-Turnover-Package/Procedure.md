# Procedure — DEL-091-05 Vendor Document Turnover Package

**Interpretation.** This procedure describes how to **produce** the Vendor Document Turnover Package deliverable (compile the register, manage submittals, and execute final turnover to the EPC Integrator). Steps for **using/operating** the documents at facility level are out of scope here (covered downstream).

## Purpose

Produce a complete, controlled vendor document set for PKG-091 Tank Farm Pump Building 3-25, submit it through the agreed control flow, and turn it over to the EPC Integrator with evidence sufficient to support package acceptance (DEL-091-06) and downstream operations/maintenance.

## Prerequisites

- Accepted PROJECT_DECOMP snapshot: GATE-07_Final_Published_2026-05-24. (Source: `_REFERENCES.md`.)
- Approved package scope: SOW-0185 through SOW-0188. (Source: GATE-07 SCOPE_LEDGER.)
- Vendor Document Index (PRQ-009) and Vendor Document Control Procedure (DOC-008) issued and accepted by EPC Integrator before substantive document submittals begin. (Source: ART-0C24267CA9; ART-A0D4D9C668.)
- Vendor's Supplier Quality Plan (QLT-006) and Inspection and Test Plan (QLT-003) in place before fabrication-evidence documents are generated. (Source: ART-11985AF946; ART-172F5C1FA0.)
- Declared upstream dependencies: none declared during PREPARATION (Source: `_DEPENDENCIES.md`). Substantive content dependence on DEL-091-04 (vendor-engineered-equipment-package) and DEL-091-02 (package datasheet) is **ASSUMPTION** — not declared in `_DEPENDENCIES.md`.

## Steps

1. **Initialize the document register.**
   1.1 Establish the Vendor Document Index (PRQ-009) listing every document required by the source vendor-documentation table (26020-Package_Requirements.docx package heading 44; location TBD).
   1.2 Bind each register row to a document number under the Vendor Document Control Procedure (DOC-008).
   1.3 Confirm category coverage: Core vendor documents; Core package engineering; Rotating equipment/pumps; and any additional source-table categories. (Source: GATE-07 ARTIFACT_REGISTER DEL-091-05 rows.)

2. **Produce and submit Core vendor documents.**
   2.1 Issue Supplier Quality Plan (QLT-006), ITP (QLT-003), Vendor Document Control Procedure (DOC-008), and Logistics/Shipping Plan (PRQ-013) early in the vendor workflow.
   2.2 Maintain MTRs/Certificates (QLT-013) as fabrication progresses.
   2.3 Issue SPIR (PRQ-015) once equipment configuration is firm.

3. **Produce and submit Core package engineering documents.**
   3.1 Submit Mechanical Design Basis (MEC-001), Mechanical Equipment List (MEC-002), Equipment Data Sheets (MEC-003), Package Equipment Specifications (MEC-006), and the Mechanical Calculation Package (MEC-014).
   3.2 Submit Equipment GA Drawing (MEC-016), Installation/Setting Drawings (MEC-017), and Lifting/Handling Study (MEC-018).
   3.3 Ensure data sheets and specs reflect SOW-0187 equipment list, seal plans (API-682 Plan 14/52 where applicable), and 575 V/3 Ph/60 Hz drive data. (Source: SOW-0187; SOW-0188.)

4. **Produce and submit Rotating equipment / pumps documents.**
   4.1 Submit Rotating Equipment Specifications (MEC-004), Pump Data Sheets (MEC-007), and Mechanical Seal / Lube Oil Specification (MEC-019).
   4.2 Cover all pump tags in SOW-0187 (P-9295-2; P-9290/9293-2; P-9215/9216-2; P-9210/9220-2; P-9200-2; P-9230-2; P-9211/9221-2; P-9240-2). (Source: SOW-0187.)

5. **Submit additional source-table categories.**
   5.1 For each additional `Vendor Documentation Category Evidence` row under DEL-091-05 in the ARTIFACT_REGISTER, supply the associated documents per the source table.
   5.2 Per-category required/optional designation: **TBD** (location TBD — DOCX heading 44 not locally readable as text in this run).

6. **Execute FAT and capture FAT evidence.**
   6.1 Issue Equipment FAT / Performance Test Procedure (MEC-021) prior to test.
   6.2 Conduct FAT per the agreed ITP and Procedure.
   6.3 Issue Equipment FAT / Performance Test Report (MEC-022) and obtain EPC Integrator review.

7. **Assemble pre-shipment records.**
   7.1 Compile Manufacturing Record Book / Vendor Data Book (QLT-021) with MTRs, ITP records, NDE records, and inspection releases.
   7.2 Issue Inspection Release Certificate (QLT-020) once ITP hold/witness points are signed off.

8. **Assemble turnover documentation.**
   8.1 Compile the Final Vendor Data Book / Final Supplier Documentation (PRQ-016).
   8.2 Compile the Mechanical Vendor Data Book / Final Documentation (MEC-023).
   8.3 Issue the Mechanical Equipment IOM Manual (MEC-025).
   8.4 Include Mechanical Spares / Special Tools Requirements (MEC-024).

9. **Transmit to EPC Integrator and support interface/integration review.**
   9.1 Transmit the complete vendor document set per the Vendor Document Control Procedure.
   9.2 Support EPC Integrator review under DEL-091-06 (EPC Vendor Package Review and Acceptance). (Source: GATE-07 DELIVERABLE_REGISTER row for DEL-091-05; DEC-006.)
   9.3 Close out review comments and reissue documents as required.

10. **Final turnover.**
    10.1 Hand over the final document set (binder + electronic) to the EPC Integrator.
    10.2 Record turnover in the Vendor Document Index final-status column.
    10.3 Update OBJ-010 closure evidence as appropriate.

## Verification

| Step | Verification |
|---|---|
| 1 | Vendor Document Index issued and accepted by EPC Integrator; every category from the source table represented. |
| 2 | All Core vendor documents present in the register at the required revision. |
| 3 | All Core package engineering documents present; data-sheet values cross-check against SOW-0187/0188. |
| 4 | All listed pump tags from SOW-0187 covered by data sheets and seal/lube specs. |
| 5 | Additional category coverage confirmed against source table (after reread). **TBD until reread.** |
| 6 | FAT Procedure approved before test; FAT Report accepted by EPC. |
| 7 | Inspection Release Certificate signed; MRB complete prior to shipment. |
| 8 | Final Vendor Data Book and IOM Manual issued; spares/special tools list complete. |
| 9 | EPC Integrator review record exists under DEL-091-06 referencing DEL-091-05 submittals. |
| 10 | Turnover acknowledged; OBJ-010 closure evidence updated. |

## Records

- Vendor Document Index (PRQ-009) — controlling register.
- Vendor Document Control Procedure (DOC-008).
- ITP records and MTRs (QLT-003; QLT-013).
- FAT Procedure and Report (MEC-021; MEC-022).
- Manufacturing Record Book / Vendor Data Book (QLT-021).
- Inspection Release Certificate (QLT-020).
- Final Vendor Data Book (PRQ-016); Mechanical Final Documentation (MEC-023); IOM Manual (MEC-025); Spares/Special Tools (MEC-024).
- EPC Integrator interface/integration review record (under DEL-091-06).
