# Datasheet: Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-011-05_vendor-document-turnover-package |
| Deliverable name | Vendor Document Turnover Package |
| Parent package | PKG-011 - 4160V SWITCHGEAR EQUIPMENT |
| Workbook row | Workbook Packages row 13 |
| Discipline | Electrical |
| Type | Vendor Document Turnover |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Scope item | SOW-0012 |
| Supported objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package ownership model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: PACKAGE_REGISTER.csv row 13; ARTIFACT_REGISTER.csv row 185. |
| Vendor-document turnover scope | Single Package Vendor deliverable for the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review. Source: DELIVERABLE_REGISTER.csv row 52. |
| Anticipated artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. Source: _CONTEXT.md and DELIVERABLE_REGISTER.csv row 52. |
| Detailed vendor-document list | TBD. ARTIFACT_REGISTER.csv row 200 states detailed vendor-document requirements are not present in current source material for this package. |
| Source vendor-document evidence artifact | ART-A2FEBFE6DC - TBD vendor document register. Source: ARTIFACT_REGISTER.csv row 200. |

## Conditions

| Condition | Value |
|---|---|
| Decomposition authority | Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24. |
| Package basis | Workbook-defined vendor-owned Electrical package for 4160V SWITCHGEAR EQUIPMENT under WBS 02. Source: PACKAGE_REGISTER.csv row 13. |
| Declared upstream dependencies | None declared during PREPARATION. Source: _DEPENDENCIES.md. |
| Declared downstream dependencies | None declared during PREPARATION. Source: _DEPENDENCIES.md. |
| Interface context relevant to document review | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: PACKAGE_REGISTER.csv row 13 and INTERFACE_REGISTER.csv rows 43-48. |

## Construction

The turnover package is constructed as a controlled vendor-document package, not as separate deliverables for each source document row. The accepted Gate 5 basis states that vendor-document turnover is a single deliverable where needed, and Word-document vendor-document rows are artifacts under Vendor Document Turnover Package, not separate deliverables. Source: PROJECT_DECOMP.md section 7.

Minimum source-grounded components:

- Vendor document register identifying submitted, reviewed, revised, and final vendor documents. The exact register schema is TBD pending a source-supported vendor-document list.
- Vendor document submittals for the 4160V switchgear equipment package.
- Turnover records showing final document status and transmittal into EPC integration review.
- Cross-reference to the package interfaces listed in INTERFACE_REGISTER.csv rows 43-48 where the vendor documents affect integration review.

## References

- _CONTEXT.md for deliverable identity, scope, anticipated artifacts, and objective list.
- _DEPENDENCIES.md for declared dependency state.
- DELIVERABLE_REGISTER.csv row 52 for deliverable definition.
- PACKAGE_REGISTER.csv row 13 for package identity, responsibility split, and interface types.
- SCOPE_LEDGER.csv row 13 for scope item SOW-0012.
- ARTIFACT_REGISTER.csv row 200 for the vendor-document source gap.
- INTERFACE_REGISTER.csv rows 43-48 for package interface facts.
- PROJECT_DECOMP.md section 7 for accepted vendor-document grouping semantics.
