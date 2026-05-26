# Specification — DEL-077-01_scope-of-work (PKG-077 Methanol Injection)

## Scope

### In scope
- Author the mandatory EPC Integrator Scope of Work for PKG-077 Methanol Injection covering the full package scope, including tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-077-01_scope-of-work`.
- Carry the workbook-defined vendor-responsible Mechanical package 'Methanol Injection' as a distinct flat project package for WBS 01. Source: `SCOPE_LEDGER.csv` row `SOW-0143`.
- Document the responsibility split between Package Vendor (engineering/design/equipment) and EPC Integrator (facility-level integration). Source: `PACKAGE_REGISTER.csv` row `PKG-077`.

### Out of scope
- Package engineering, package design, vendor documentation, and the physical equipment package — owned by the Package Vendor, not by the EPC Integrator authoring this Scope of Work. Source: `PACKAGE_REGISTER.csv` row `PKG-077`.
- Other deliverables under PKG-077 (datasheet, CWP, vendor-engineered equipment package, vendor document turnover, EPC vendor package review/acceptance) are tracked separately and referenced as siblings under SOW-0143. Source: `SCOPE_LEDGER.csv` row `SOW-0143`.
- Package-specific exclusions: TBD — no package-specific exclusions stated in source materials (`PACKAGE_REGISTER.csv` Exclusions field).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-077-01-01 | The Scope of Work SHALL identify the package by name (Methanol Injection), workbook ID (77), workbook row (72), CoA tracking number (26020-01-29-002), WBS (01), and discipline (Mechanical). | `PACKAGE_REGISTER.csv` row `PKG-077` |
| REQ-077-01-02 | The Scope of Work SHALL state the package function as a vendor-owned Mechanical package providing methanol injection within the 04-25 Deepcut facility scope. | `PACKAGE_REGISTER.csv` row `PKG-077`; `OBJ-001` |
| REQ-077-01-03 | The Scope of Work SHALL list tagged major equipment supplied as part of the vendor package. | `ARTIFACT_REGISTER.csv` row ART-F30A41723D; specific tag list location TBD (workbook row 72 detailed text not in registers) |
| REQ-077-01-04 | The Scope of Work SHALL record the responsibility assignment: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-077` ResponsibilityNote; `OBJ-004` |
| REQ-077-01-05 | The Scope of Work SHALL enumerate the applicable interface types between the package and the facility (13 types). | `INTERFACE_REGISTER.csv` rows for PKG-077 |
| REQ-077-01-06 | The Scope of Work SHALL state the package boundary and exclusions; ASSUMPTION: where no package-specific exclusions are sourced, state explicitly that none are declared in source materials (TBD entry retained). | `PACKAGE_REGISTER.csv` row `PKG-077` |
| REQ-077-01-07 | The Scope of Work SHALL provide a whole-facility integration narrative describing how Methanol Injection integrates with the process facility. | `ARTIFACT_REGISTER.csv` row ART-7A3F23A6BA |
| REQ-077-01-08 | The Scope of Work SHALL trace its supported objectives to OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010. | `DELIVERABLE_REGISTER.csv` row `DEL-077-01_scope-of-work` |
| REQ-077-01-09 | The Scope of Work SHALL cite its scope-ledger anchor `SOW-0143` and Gate 6 disposition that Methanol Injection scope is included with the Cryogenic Unit package scope. | `SCOPE_LEDGER.csv` row `SOW-0143`; `PACKAGE_REGISTER.csv` row `PKG-077` Notes |

## Standards

| Standard / Authority | Applicability | Source |
|---|---|---|
| Project workbook (`26020-Package_Requirements.docx`; `26020-Packages_Interfaces_4_export.xlsx`) | Authoritative source for package definition (row 72) | `_Sources` listing; `PACKAGE_REGISTER.csv` SourceRef |
| PROJECT_DECOMP Gate-07 snapshot registers | Authoritative basis for deliverable identity, scope ledger, interfaces, objectives | `_REFERENCES.md`; snapshot manifest |
| Industry codes for sour-gas methanol injection (e.g., NACE MR0175 / ISO 15156) | ASSUMPTION: likely applicable to sour-service Methanol Injection equipment — not cited in available source slices | location TBD |

## Verification

| Requirement | Verification Approach | Source |
|---|---|---|
| REQ-077-01-01 | Field-by-field check against `PACKAGE_REGISTER.csv` row `PKG-077`. | self |
| REQ-077-01-02 | Function statement reviewed against PACKAGE_REGISTER `Function` and `Description` fields. | self |
| REQ-077-01-03 | Tagged equipment list reviewed against the workbook row 72 detailed major-equipment text (source-reread required; currently TBD). | `ARTIFACT_REGISTER.csv` ART-F30A41723D |
| REQ-077-01-04 | Responsibility wording verbatim/equivalent to `PACKAGE_REGISTER.csv` ResponsibilityNote. | self |
| REQ-077-01-05 | Cross-check interface list count and type names against the 13 IFC-* rows for PKG-077. | `INTERFACE_REGISTER.csv` |
| REQ-077-01-06 | Confirm boundary statement and explicit handling of TBD exclusions. | self |
| REQ-077-01-07 | Narrative cites whole-facility integration touchpoints (interface types and Gate 6 cryogenic-unit grouping). | self |
| REQ-077-01-08 | Each objective ID maps to a statement in `OBJECTIVE_REGISTER.csv`. | `OBJECTIVE_REGISTER.csv` |
| REQ-077-01-09 | SOW-0143 statement cited verbatim or paraphrased; Gate 6 disposition cited from PACKAGE_REGISTER Notes. | `SCOPE_LEDGER.csv`; `PACKAGE_REGISTER.csv` |

## Documentation

Required artifacts to be produced under this deliverable (per `ARTIFACT_REGISTER.csv`):

- Package scope of work (ART-319578C39E)
- Tagged equipment and package identity list (ART-F30A41723D)
- Package function and whole-facility integration narrative (ART-7A3F23A6BA)
- Package responsibility assignment record (ART-1230D957BE)
