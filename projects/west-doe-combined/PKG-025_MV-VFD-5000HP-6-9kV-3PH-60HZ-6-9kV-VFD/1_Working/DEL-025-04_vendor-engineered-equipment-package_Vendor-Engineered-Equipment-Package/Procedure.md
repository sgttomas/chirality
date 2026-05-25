# Procedure — DEL-025-04 Vendor Engineered Equipment Package (PKG-025 MV VFD)

This Procedure describes the steps to **produce** the Vendor Engineered Equipment Package for the PKG-025 6.9 kV MV VFD, from upstream EPC inputs through vendor turnover. Steps to **operate** the VFD in service are governed by vendor commissioning and operating manuals (DEL-025-05) and are out of scope here.

## Prerequisites

- Accepted upstream snapshot: Gate 7 Final Published PROJECT_DECOMP snapshot (`_REFERENCES.md`).
- DEL-025-01 Scope of Work (EPC anchor) accepted (DELIVERABLE_REGISTER.csv DEL-025-01).
- DEL-025-02 Package Datasheet (EPC technical handoff) accepted, including resolved motor horsepower rating (closes CT-01 / HRR-025-04-001) and per-unit VFD allocation (closes CT-02 / HRR-025-04-002) (DELIVERABLE_REGISTER.csv DEL-025-02).
- DBM-Deepcut/4-25_Deepcut_DBM.md design basis accessible to vendor (`_REFERENCES.md`).
- Source clauses extracted from `26020-Package_Requirements.docx` and interface rows extracted from `26020-Packages_Interfaces_4_export.xlsx` (closes CT-03 / HRR-025-04-003) — currently TBD.
- Declared upstream dependencies: none (`_DEPENDENCIES.md`). Note: undeclared functional dependency on DEL-025-01 and DEL-025-02 is documented in Guidance and Specification rather than as a declared blocker.

## Steps

1. **Vendor receives and acknowledges EPC inputs.** Vendor confirms receipt of DEL-025-01 Scope of Work and DEL-025-02 Package Datasheet and logs any clarification requests against them.
2. **Vendor establishes package design basis.** Vendor documents its design basis grounded in the DBM-Deepcut design basis (voltage system, grounding, cable basis, area classification, Starting-VFD-with-synchronous-transfer architecture per DBM lines 893 and 2955) and the EPC Package Datasheet.
3. **Vendor performs package engineering.** Vendor produces single-line diagrams, control schematics, transfer-scheme logic, protection coordination basis, harmonic study (per resolved REQ-025-04-15 method), cable schedule, grounding interface diagram (referencing the 100 A NGR per DBM line 2985), and enclosure/building interface drawings.
4. **Vendor performs package design and fabrication readiness.** Vendor finalizes bill of materials, vendor-supplied subcomponents, factory test plan, and shipping/handling plan. Confirms removable transom/door provisions with the building vendor (DBM line 2979).
5. **Factory acceptance testing (FAT).** Vendor conducts FAT against REQ-025-04-01 through REQ-025-04-08, including starting profile and synchronous-transfer logic demonstration; EPC Integrator witnesses per its acceptance plan (DEL-025-06).
6. **Vendor produces vendor design basis document and datasheet set.** Vendor publishes the design basis and datasheet set as the deliverable's primary documentary artifacts (`_CONTEXT.md` anticipated artifacts).
7. **Vendor delivers physical equipment package.** Vendor ships the engineered physical equipment package to site per construction sequence.
8. **EPC integration review.** EPC Integrator confirms vendor-engineered package conforms to EPC Scope of Work and Package Datasheet and that interface obligations (Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports — PACKAGE_REGISTER.csv row PKG-025) are addressed.
9. **Vendor document turnover.** Vendor compiles submittals and turnover records into DEL-025-05 Vendor Document Turnover Package; EPC reviews and accepts under DEL-025-06.

## Verification

- All requirements REQ-025-04-01 through REQ-025-04-14 have evidence (drawing, test record, or submittal) recorded against them; REQ-025-04-15 and REQ-025-04-16 have explicit dispositions (closed by vendor proposal accepted by EPC, or carried as residual TBD with an owner).
- All open Conflict Table entries (CT-01, CT-02, CT-03) have a recorded human ruling before fabrication release; otherwise fabrication does not proceed.
- FAT report demonstrates Starting VFD function and synchronous-transfer logic against bus configuration consistent with MCC-8200 (no PFC capacitors on transfer bus).
- Cable schedule conforms to DBM Cable Specifications table for 6.9 kV (DBM line 3008) and for VFD-fed circuits (DBM line 3013).
- Area-classification compatibility verified for any Zone 2 motor (DBM line 2961).
- Building-fit / removal-envelope confirmed against electrical building door / transom provisions (DBM line 2979).

## Records

- Vendor package design basis document.
- Vendor package datasheet set.
- Vendor engineering drawing package (single line, schematics, transfer-scheme logic, cable schedule, grounding interface).
- Harmonic / power-quality study (when method per REQ-025-04-15 is established).
- Factory acceptance test report.
- Shipping records and field receipt confirmation.
- EPC integration review log (feeds DEL-025-06).
- Vendor document submittal index (feeds DEL-025-05).
- Human-ruling records closing CT-01, CT-02, CT-03 (or accepted carry-forward with owner).
