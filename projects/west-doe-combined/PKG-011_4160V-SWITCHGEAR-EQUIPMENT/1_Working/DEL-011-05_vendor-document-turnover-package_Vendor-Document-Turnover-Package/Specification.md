# Specification: Vendor Document Turnover Package

## Scope

This specification covers the Package Vendor's vendor-document turnover package for PKG-011, 4160V SWITCHGEAR EQUIPMENT. It includes the vendor document register, vendor document submittals, source-required vendor documentation where available, and turnover records, with EPC Integrator interface/integration review. Source: DELIVERABLE_REGISTER.csv row 52 and _CONTEXT.md.

Excluded or not established:

- Detailed package-specific vendor-document line-item requirements are not established by the current source material. Source: ARTIFACT_REGISTER.csv row 200.
- Individual vendor-document rows are not separate deliverables under the accepted Gate 5 basis. Source: PROJECT_DECOMP.md section 7.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-001 | The deliverable shall be maintained as one Vendor Document Turnover Package for PKG-011. | DELIVERABLE_REGISTER.csv row 52; PROJECT_DECOMP.md section 7 | Confirm one turnover package exists for DEL-011-05. |
| REQ-002 | The package shall include a vendor document register or explicitly record the register as TBD until the source-supported detailed document list is available. | DELIVERABLE_REGISTER.csv row 52; ARTIFACT_REGISTER.csv row 200 | Review Datasheet and turnover records for register status. |
| REQ-003 | Vendor document submittals and turnover records shall preserve the Package Vendor responsibility for vendor documentation and the EPC Integrator responsibility for interface/integration review. | PACKAGE_REGISTER.csv row 13; ARTIFACT_REGISTER.csv row 185 | Check responsibility assignment in the turnover package and review log references. |
| REQ-004 | The turnover package shall identify the 4160V switchgear package interfaces that may require EPC review: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row 13; INTERFACE_REGISTER.csv rows 43-48 | Confirm interface checklist or register cross-reference includes all six interface types. |
| REQ-005 | Where detailed source vendor-document requirements are unavailable, affected document titles, schemas, and acceptance criteria shall remain TBD and shall not be invented. | ARTIFACT_REGISTER.csv row 200; four-documents QA_CHECKS.md | Verify unsupported details are marked TBD or raised for human ruling. |

## Standards

| Standard or basis | Applicability |
|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Authoritative decomposition truth for package, deliverable, artifact, objective, and interface basis. |
| PROJECT_DECOMP.md section 7 | Governs accepted deliverable semantics for vendor-document turnover grouping. |
| 26020-Package_Requirements.docx | Listed as source basis in decomposition objectives and registers, but no detailed vendor-document requirements are present for PKG-011 in the accessible artifact row. Location for PKG-011 vendor document table: TBD. |
| Facility/project document control standard | TBD; no deliverable-specific source slice was accessible in _REFERENCES.md. |

## Verification

- Confirm the four-document kit and turnover package use consistent identity: DEL-011-05, PKG-011, 4160V SWITCHGEAR EQUIPMENT, Vendor Document Turnover Package.
- Confirm the turnover package does not promote individual vendor document rows into standalone deliverables.
- Confirm the vendor/EPC responsibility split is preserved.
- Confirm all six accepted interface types are represented as review context where applicable.
- Confirm detailed vendor-document requirements remain TBD unless a locally accessible source slice is added.

## Documentation

Required or anticipated records:

- Vendor document register, with detailed line items TBD until source-supported.
- Vendor document submittals.
- Source vendor document table rows as artifacts where available.
- Turnover records.
- EPC Integrator review/comment log reference where interface or integration review occurs.
- Human ruling record for the detailed vendor-document list gap.
