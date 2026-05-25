# Package Datasheet: 10KVA AC UNINTERRUPTIBLE POWER SUPPLY

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-012-02_package-datasheet | _CONTEXT.md; DELIVERABLE_REGISTER.csv row for DEL-012-02 |
| Deliverable name | Package Datasheet | _CONTEXT.md; DELIVERABLE_REGISTER.csv row for DEL-012-02 |
| Parent package | PKG-012 | _CONTEXT.md; PACKAGE_REGISTER.csv row for PKG-012 |
| Package name | 10KVA AC UNINTERRUPTIBLE POWER SUPPLY | PACKAGE_REGISTER.csv row for PKG-012 |
| Workbook ID / row | 12 / 14 | PACKAGE_REGISTER.csv row for PKG-012 |
| WBS | 02 | PACKAGE_REGISTER.csv row for PKG-012 |
| CoA tracking number | 26020-02-30-003 | PACKAGE_REGISTER.csv row for PKG-012 |
| Discipline | Electrical | _CONTEXT.md; PACKAGE_REGISTER.csv row for PKG-012 |
| Responsible party for this datasheet | EPC Integrator | _CONTEXT.md; DELIVERABLE_REGISTER.csv row for DEL-012-02 |
| Package delivery responsibility | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration. | PACKAGE_REGISTER.csv row for PKG-012 |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package role | Vendor-owned Electrical package under WBS 02. | PACKAGE_REGISTER.csv row for PKG-012 |
| Datasheet purpose | EPC Integrator technical handoff containing package data required for third-party vendor or discipline package engineering and design. | DELIVERABLE_REGISTER.csv row for DEL-012-02 |
| Anticipated artifacts | Package technical datasheet; vendor engineering handoff basis; package interface requirements matrix; source-supported equipment and design criteria. | _CONTEXT.md; DELIVERABLE_REGISTER.csv row for DEL-012-02 |
| Source scope item | SOW-0013. | SCOPE_LEDGER.csv row for SOW-0013 |
| Nominal UPS capacity | 10 kVA appears in package name; detailed rating basis TBD pending source slice. | PACKAGE_REGISTER.csv row for PKG-012; Workbook Packages row 14 location TBD |
| AC input voltage / phase / frequency | TBD. | No source-supported value in Gate 7 package row |
| AC output voltage / phase / frequency | TBD. | No source-supported value in Gate 7 package row |
| Battery autonomy / backup duration | TBD. | No source-supported value in Gate 7 package row |
| Battery type | TBD. | No source-supported value in Gate 7 package row |
| Bypass / maintenance bypass requirements | TBD. | No source-supported value in Gate 7 package row |
| Enclosure / installation location | TBD. | No source-supported value in Gate 7 package row |
| Environmental design conditions | TBD. | No source-supported value in Gate 7 package row |

## Conditions

| Condition | Datasheet entry | Source |
|---|---|---|
| Scope boundary | Carry the workbook-defined vendor-responsible Electrical package as a distinct flat project package for WBS 02. | SCOPE_LEDGER.csv row for SOW-0013 |
| EPC / vendor boundary | Package Vendor owns engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv row for PKG-012; PROJECT_DECOMP.md Intake Summary |
| Exclusions | TBD; no package-specific exclusions stated in source materials. | PACKAGE_REGISTER.csv row for PKG-012 |
| Declared upstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |
| Declared downstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |

## Construction

| Interface / construction datum | Required datasheet treatment | Source |
|---|---|---|
| Electrical Power | Include as package interface fact and identify vendor/EPC boundary details as TBD until source-supported values are available. | INTERFACE_REGISTER.csv IFC-AA089340E0; ARTIFACT_REGISTER.csv ART-846E14C8E7 |
| Grounding / Bonding | Include as package interface fact and identify grounding/bonding responsibility split as TBD until source-supported values are available. | INTERFACE_REGISTER.csv IFC-2F50872E45; ARTIFACT_REGISTER.csv ART-DA6652060F |
| Maintenance Access | Include as package interface fact and reserve space/access requirements as TBD until source-supported values are available. | INTERFACE_REGISTER.csv IFC-52E7E27E87; ARTIFACT_REGISTER.csv ART-D3BD4B5406 |
| Structural / Foundations / Supports | Include as package interface fact and identify support/foundation loads, anchorage, and layout data as TBD until vendor or source-supported values are available. | INTERFACE_REGISTER.csv IFC-1D40B1F072; ARTIFACT_REGISTER.csv ART-D5709F2B4B |

## References

- _CONTEXT.md for deliverable identity and anticipated artifacts.
- _DEPENDENCIES.md for declared dependency state.
- Gate 7 PROJECT_DECOMP snapshot, especially PROJECT_DECOMP.md, PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, SCOPE_LEDGER.csv, OBJECTIVE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.
- Workbook Packages row 14 is the underlying source reference cited by Gate 7. The row itself was not reinterpreted in this Phase 2.2 run per instruction; values not present in Gate 7 remain TBD.
