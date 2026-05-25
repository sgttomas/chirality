# Specification — DEL-015-01 Scope of Work (PKG-015)

> Normative requirements for the EPC Integrator Scope of Work artifact for PKG-015 Transformer TXP-8300-1.
> This document specifies what the SoW artifact must contain, not the transformer design itself (which is vendor scope).

## 1. Scope

### 1.1 In scope
This Specification governs the content, structure, and acceptance criteria of the EPC Integrator's Scope of Work document for PKG-015 — the 12/15 MVA, 13.8 kV / 4,160 / 2,400 V step-down distribution transformer package designated TXP-8300-1. The Scope of Work must define:

- Package identity and tagged equipment (Source: PACKAGE_REGISTER.csv, Workbook row 17).
- Package function within the 03-25 facility electrical architecture (Source: DBM L738–L750).
- Source basis pointer (Source: DBM L740–L750; PACKAGE_REGISTER.csv).
- Vendor / EPC Integrator scope boundaries (Source: PACKAGE_REGISTER.csv `Vendor_EPC_Boundary`).
- Whole-facility integration narrative across the seven applicable interface types (Source: PACKAGE_REGISTER.csv `Interface_Types`).

### 1.2 Out of scope
- Vendor package engineering, vendor datasheets, vendor design calculations (Package Vendor scope per PACKAGE_REGISTER.csv).
- Construction execution detail (covered by DEL-015-03 Construction Work Package).
- Vendor document register and submittals (covered by DEL-015-05).
- Review/acceptance evidence (covered by DEL-015-06).

## 2. Requirements

| ID | Requirement | Source / Verification |
|---|---|---|
| REQ-015-01-01 | The Scope of Work shall identify the package by ID (`PKG-015`), tag (`TXP-8300-1`), WBS (`02 / 26020-02-30-006`), and discipline (Electrical). | PACKAGE_REGISTER.csv; verify by inspection. |
| REQ-015-01-02 | The Scope of Work shall state the package function: step-down distribution from the facility 13.8 kV bus to 4,160 V (and 2,400 V) services serving the 03-25 facility. | DBM L744; Package name. ASSUMPTION: 2,400 V service basis to be confirmed against detailed electrical drawings. |
| REQ-015-01-03 | The Scope of Work shall name the upstream source of supply: sub-feed from the 04-25 13.8 kV Main Switchgear Electrical Building. | DBM L740. |
| REQ-015-01-04 | The Scope of Work shall list tagged equipment within the package boundary (transformer TXP-8300-1; package-bundled auxiliaries TBD per vendor). | Vendor scope; mark vendor-defined items `TBD`. |
| REQ-015-01-05 | The Scope of Work shall declare the vendor/EPC boundary verbatim from PACKAGE_REGISTER.csv: Vendor owns package engineering, design, documentation, and physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination. | PACKAGE_REGISTER.csv `Vendor_EPC_Boundary`. |
| REQ-015-01-06 | The Scope of Work shall identify the seven applicable interface types (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports) and describe the EPC integration responsibility for each. | PACKAGE_REGISTER.csv `Interface_Types`. |
| REQ-015-01-07 | The Scope of Work shall cite governing area classification: Class I, Zone 2, Gas Groups IIA/IIB as the general facility basis (transformer-specific classification may differ when sited in general-purpose areas — confirm during detailed engineering). | DBM L722. |
| REQ-015-01-08 | The Scope of Work shall cite that the package shall comply with CEC spacing and installation requirements applicable to MV transformers, with secondary containment review per DBM general policy. | DBM L2949 (general DBM transformer policy carried across facilities); confirm 03-25 specific application during detailed engineering. |
| REQ-015-01-09 | The Scope of Work shall assert the responsibility assignment: EPC Integrator leads facility integration; Package Vendor provides the equipment and vendor documentation. | PACKAGE_REGISTER.csv; DELIVERABLE_REGISTER.csv DEL-015-01 (Responsible Party). |
| REQ-015-01-10 | The Scope of Work shall reference (not duplicate) the Package Datasheet (DEL-015-02), Construction Work Package (DEL-015-03), Vendor Document Turnover Package (DEL-015-05), and EPC Vendor Package Review and Acceptance (DEL-015-06). | DELIVERABLE_REGISTER.csv PKG-015 rows. |
| REQ-015-01-11 | All quantitative values and detailed technical parameters not supported by the accessible source set shall be marked `TBD` or `ASSUMPTION` in the Scope of Work; the Scope of Work shall not invent vendor design data. | Skill rule (source-anchored); PROJECT_DECOMP authority hierarchy. |

## 3. Standards and Governing Documents

| Standard / Document | Application | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | MV transformer installation, spacing, grounding | DBM L2949 (general); `location TBD` (clause-level) |
| API RP 505 | Area classification basis for hazardous areas | DBM L722; `location TBD` (clause-level) |
| Project electrical specifications | Cable tray, conduit, grounding, bonding | DBM L768; `location TBD` (project specs not in source set) |
| 26020-02-30-006 (Package Specification series) | Package-level requirements | PACKAGE_REGISTER.csv `Spec_Number`; full text not in accessible source set — `location TBD` |
| Workbook Packages row 17 | Decomposition source row | `_Sources` workbook export — row 17 |

## 4. Verification

| REQ | Verification Method |
|---|---|
| REQ-015-01-01 | Document inspection vs. PACKAGE_REGISTER.csv. |
| REQ-015-01-02..03 | Cross-check against DBM Section "Incoming Power and Transformers". |
| REQ-015-01-04 | Inspection; vendor handoff confirms package boundary. |
| REQ-015-01-05..06 | Verbatim/structured comparison against PACKAGE_REGISTER.csv columns. |
| REQ-015-01-07..08 | DBM clause cross-reference; detailed-engineering confirmation. |
| REQ-015-01-09 | Inspection vs. DELIVERABLE_REGISTER.csv `Responsible Party`. |
| REQ-015-01-10 | Hyperlink/file-path check across DEL-015-02/03/05/06. |
| REQ-015-01-11 | Reviewer audit: any unsourced quantitative claim is a defect. |

## 5. Documentation

The SoW deliverable shall produce, as anticipated artifacts:

- Package scope of work (this artifact)
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

(Source: DELIVERABLE_REGISTER.csv `Anticipated Artifacts` for DEL-015-01.)
