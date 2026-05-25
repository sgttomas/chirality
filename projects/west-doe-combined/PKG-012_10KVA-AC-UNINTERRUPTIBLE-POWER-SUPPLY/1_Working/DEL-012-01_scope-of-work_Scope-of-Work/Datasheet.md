# Datasheet: DEL-012-01_scope-of-work — Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-012-01_scope-of-work` |
| Deliverable name | Scope of Work |
| Parent package | `PKG-012` |
| Package name | 10KVA AC UNINTERRUPTIBLE POWER SUPPLY |
| Workbook ID / row | 12 / row 14 |
| WBS | 02 |
| CoA tracking number | 26020-02-30-003 |
| Discipline | Electrical |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Source scope item | `SOW-0013` |
| Accepted upstream snapshot | Gate 7 final published PROJECT_DECOMP snapshot, 2026-05-24 |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package role | Workbook-defined vendor-owned Electrical package under WBS 02. |
| Package function | TBD; the source slice names the package as a 10KVA AC uninterruptible power supply but does not define load, runtime, topology, battery type, distribution arrangement, or protected circuits. |
| EPC scope-of-work role | Mandatory EPC Integrator deliverable for package scope, tagged equipment, package identity, source basis, boundaries, and whole-facility integration narrative. |
| Vendor / EPC responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. |
| Tagged equipment | TBD; no tag number is present in Workbook Packages row 14 or the Gate 7 row excerpts for this deliverable. |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. |

## Conditions

| Condition | Source-grounded value |
|---|---|
| Electrical power interface | Required interface fact marked `X` in Workbook Packages row 14. |
| Grounding / bonding interface | Required interface fact marked `X` in Workbook Packages row 14. |
| Maintenance access interface | Required interface fact marked `X` in Workbook Packages row 14. |
| Structural / foundations / supports interface | Required interface fact marked `X` in Workbook Packages row 14. |
| Facility / area context | WBS 02; objective mapping associates this package with the 03-25 compressor station and liquids hub package set as best-effort decomposition context. |
| Detailed design criteria | TBD; no deliverable-specific voltage input/output, load, runtime, enclosure, environmental, testing, or documentation criteria were available in the local source slice. |

## Construction

| Item | Source-grounded value |
|---|---|
| Scope-of-work author | EPC Integrator. |
| Package execution owner | Package Vendor for engineering, design, vendor documentation, and physical equipment package. |
| Integration owner | EPC Integrator for integration into the functional process facility. |
| Required scope boundaries | Electrical power, grounding/bonding, maintenance access, and structural/foundation/support interfaces must be identified and coordinated. |
| Exclusions | TBD; no package-specific exclusions are stated in available source materials. |
| Downstream deliverables supported | Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover Package, and EPC Vendor Package Review and Acceptance for `PKG-012`. |

## References

- `_CONTEXT.md` for deliverable identity, scope, anticipated artifacts, and accepted snapshot pointer.
- `_REFERENCES.md` for the accepted source and decomposition references.
- `_DEPENDENCIES.md` for declared dependency state.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row for `DEL-012-01_scope-of-work`.
- Gate 7 `PACKAGE_REGISTER.csv`, row for `PKG-012`.
- Gate 7 `SCOPE_LEDGER.csv`, row `SOW-0013`.
- Gate 7 `ARTIFACT_REGISTER.csv`, rows for `DEL-012-01_scope-of-work`.
- Gate 7 `INTERFACE_REGISTER.csv`, rows for `PKG-012`.
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, rows mapping `DEL-012-01_scope-of-work` to `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, and `OBJ-010`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 14.
