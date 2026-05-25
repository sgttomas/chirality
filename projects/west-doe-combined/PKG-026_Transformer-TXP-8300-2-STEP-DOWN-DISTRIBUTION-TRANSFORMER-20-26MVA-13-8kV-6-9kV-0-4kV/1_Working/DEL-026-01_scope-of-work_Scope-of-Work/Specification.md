# Specification — DEL-026-01 Scope of Work (PKG-026)

> Normative requirements for the EPC Integrator Scope of Work artifact for PKG-026 Transformer TXP-8300-2.
> This document specifies what the SoW artifact must contain, not the transformer design itself (which is vendor scope).

## 1. Scope

### 1.1 In scope
This Specification governs the content, structure, and acceptance criteria of the EPC Integrator's Scope of Work document for PKG-026 — the 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV step-down distribution transformer package designated TXP-8300-2. The Scope of Work must define:

- Package identity and tagged equipment (Source: PACKAGE_REGISTER.csv, Workbook row 28).
- Package function within the 03-25 facility electrical architecture (Source: DBM L728–L750 for general facility basis; package-specific load assignments are `TBD`).
- Source basis pointer (Source: PACKAGE_REGISTER.csv `Sources` column citing Workbook row 28 and 3-25 DBM).
- Vendor / EPC Integrator scope boundaries (Source: PACKAGE_REGISTER.csv `Vendor_EPC_Boundary`).
- Whole-facility integration narrative across the seven applicable interface types (Source: PACKAGE_REGISTER.csv `Interface_Types`).

### 1.2 Out of scope
- Vendor package engineering, vendor datasheets, vendor design calculations (Package Vendor scope per PACKAGE_REGISTER.csv).
- Construction execution detail (covered by DEL-026-03 Construction Work Package).
- Vendor document register and submittals (covered by DEL-026-05 Vendor Document Turnover Package).
- Review/acceptance evidence (covered by DEL-026-06 EPC Vendor Package Review and Acceptance).
- Package technical handoff datasheet content (covered by DEL-026-02 Package Datasheet).

## 2. Requirements

| ID | Requirement | Source / Verification |
|---|---|---|
| REQ-026-01-01 | The Scope of Work shall identify the package by ID (`PKG-026`), tag (`TXP-8300-2`), WBS (`02 / 26020-02-30-017`), and discipline (Electrical). | PACKAGE_REGISTER.csv; verify by inspection. |
| REQ-026-01-02 | The Scope of Work shall state the package function: step-down distribution from the facility 13.8 kV bus to 6.9 kV and 0.4 kV services serving 03-25 facility loads. ASSUMPTION: secondary load assignments to be confirmed against detailed electrical drawings. | Package name (Workbook row 28). Accessible DBM does not enumerate 6.9 kV or 0.4 kV service in 03-25 — see Guidance Conflict Table. |
| REQ-026-01-03 | The Scope of Work shall name the upstream source of supply at the facility level: 03-25 13.8 kV system, ultimately sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building per facility convention. | DBM L740 (general 03-25 incoming-power basis). |
| REQ-026-01-04 | The Scope of Work shall list tagged equipment within the package boundary (transformer TXP-8300-2; package-bundled auxiliaries `TBD` per vendor). | Vendor scope; mark vendor-defined items `TBD`. |
| REQ-026-01-05 | The Scope of Work shall declare the vendor/EPC boundary verbatim from PACKAGE_REGISTER.csv: Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv `Vendor_EPC_Boundary` for PKG-026. |
| REQ-026-01-06 | The Scope of Work shall identify the seven applicable interface types (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports) and describe the EPC integration responsibility for each. | PACKAGE_REGISTER.csv `Interface_Types` for PKG-026. |
| REQ-026-01-07 | The Scope of Work shall cite governing area classification: Class I, Zone 2, Gas Groups IIA/IIB as the general facility basis (transformer-specific classification may differ when sited in general-purpose areas — confirm during detailed engineering). | DBM L720–L726. |
| REQ-026-01-08 | The Scope of Work shall cite that the package shall comply with CEC spacing and installation requirements applicable to MV transformers, with secondary containment review per DBM general policy. | DBM general transformer policy (clause-level `location TBD`); confirm 03-25 application during detailed engineering. |
| REQ-026-01-09 | The Scope of Work shall assert the responsibility assignment: EPC Integrator leads facility integration; Package Vendor provides the equipment and vendor documentation. | PACKAGE_REGISTER.csv; DELIVERABLE_REGISTER.csv DEL-026-01 (Responsible Party). |
| REQ-026-01-10 | The Scope of Work shall reference (not duplicate) the Package Datasheet (DEL-026-02), Construction Work Package (DEL-026-03), Vendor Engineered Equipment Package (DEL-026-04), Vendor Document Turnover Package (DEL-026-05), and EPC Vendor Package Review and Acceptance (DEL-026-06). | DELIVERABLE_REGISTER.csv PKG-026 rows. |
| REQ-026-01-11 | All quantitative values and detailed technical parameters not supported by the accessible source set shall be marked `TBD` or `ASSUMPTION` in the Scope of Work; the Scope of Work shall not invent vendor design data. | Skill rule (source-anchored); PROJECT_DECOMP authority hierarchy. |
| REQ-026-01-12 | The Scope of Work shall surface the identity-vs-DBM verification gap (Workbook row 28 names a 20/26 MVA 13.8/6.9/0.4 kV transformer; the accessible 3-25 DBM describes only a 12 MVA 13.8/4.16 kV transformer) and defer reconciliation to the Package Datasheet (DEL-026-02) and detailed engineering. | DBM L744 vs. Workbook row 28; Guidance Conflict Table CFL-026-01-01. |

## 3. Standards and Governing Documents

| Standard / Document | Application | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | MV transformer installation, spacing, grounding | DBM general transformer policy; clause-level `location TBD` |
| API RP 505 | Area classification basis for hazardous areas | DBM L720–L726 (general policy); clause-level `location TBD` |
| Project electrical specifications | Cable tray, conduit, grounding, bonding | DBM L768 (general policy); project specs not in accessible source set — `location TBD` |
| 26020-02-30-017 (Package Specification series number) | Package-level requirements | PACKAGE_REGISTER.csv `Spec_Number` for PKG-026; full text not in accessible source set — `location TBD` |
| Workbook Packages row 28 | Decomposition source row | `_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 28 |
| 26020-Package_Requirements.docx | Package requirements source document | `_Sources/26020-Package_Requirements.docx`; binary not read in this run — `location TBD` |

## 4. Verification

| REQ | Verification Method |
|---|---|
| REQ-026-01-01 | Document inspection vs. PACKAGE_REGISTER.csv. |
| REQ-026-01-02 | Cross-check against DBM Section "Incoming Power and Transformers" and Conflict Table CFL-026-01-01 / CFL-026-01-02. |
| REQ-026-01-03 | Cross-reference DBM L740 (facility incoming-power basis). |
| REQ-026-01-04 | Inspection; vendor handoff confirms package boundary. |
| REQ-026-01-05..06 | Verbatim/structured comparison against PACKAGE_REGISTER.csv columns. |
| REQ-026-01-07..08 | DBM clause cross-reference; detailed-engineering confirmation. |
| REQ-026-01-09 | Inspection vs. DELIVERABLE_REGISTER.csv `Responsible Party`. |
| REQ-026-01-10 | Hyperlink/file-path check across DEL-026-02 through DEL-026-06. |
| REQ-026-01-11 | Reviewer audit: any unsourced quantitative claim is a defect. |
| REQ-026-01-12 | Inspection: Conflict Table CFL-026-01-01 cited and reconciliation deferred to DEL-026-02. |

## 5. Documentation

The SoW deliverable shall produce, as anticipated artifacts:

- Package scope of work (this artifact) — ART-F154B8A581
- Tagged equipment and package identity list — ART-AA91097B6C
- Package function and integration narrative — ART-CDB03DA424
- Responsibility assignment record — ART-CCD4B8B930

(Source: DELIVERABLE_REGISTER.csv and ARTIFACT_REGISTER.csv for DEL-026-01.)
