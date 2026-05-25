# Datasheet: Vendor Engineered Equipment Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-012-04_vendor-engineered-equipment-package` |
| Deliverable Name | Vendor Engineered Equipment Package |
| Parent Package | `PKG-012` |
| Package Name | 10KVA AC UNINTERRUPTIBLE POWER SUPPLY |
| Workbook Row | 14 |
| WBS | 02 |
| Tracking Number | 26020-02-30-003 |
| Discipline | Electrical |
| Deliverable Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Scope Item | `SOW-0013` |
| Source Basis | Gate 7 `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment/service | 10KVA AC uninterruptible power supply | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`; `SCOPE_LEDGER.csv`, row `SOW-0013` |
| Vendor scope model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |
| EPC scope model | EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |
| Deliverable scope | Vendor engineering, design, fabrication/supply, and physical equipment package developed from the EPC package Scope of Work and Package Datasheet | Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-012-04_vendor-engineered-equipment-package` |
| Anticipated artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set | Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-012-04_vendor-engineered-equipment-package`; `ARTIFACT_REGISTER.csv`, rows `ART-F3CC1D5672` and `ART-7A2DEBA163` |
| Applicable interface types | Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |
| Supported objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, `OBJ-010` | Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-012-04_vendor-engineered-equipment-package` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Execution boundary | Vendor package production unit; EPC integration review remains separate from vendor design ownership | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`; `DELIVERABLE_REGISTER.csv`, row `DEL-012-04_vendor-engineered-equipment-package` |
| Facility integration basis | Whole-facility integration by EPC Integrator; vendor package must preserve electrical power, grounding/bonding, maintenance access, and support/foundation interfaces for EPC review | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |
| Detailed UPS ratings beyond package name | TBD | Not provided in accessible Gate 7 source slices for this deliverable |
| Vendor standards, certifications, inspection criteria, and test protocols | TBD | No deliverable-specific vendor source slice copied during PREPARATION |

## Construction

| Construction / Supply Element | Value | Source |
|---|---|---|
| Physical equipment package | Vendor engineered physical equipment package | Gate 7 `ARTIFACT_REGISTER.csv`, row `ART-F3CC1D5672` |
| Vendor design evidence | Vendor package design basis and datasheet set | Gate 7 `ARTIFACT_REGISTER.csv`, row `ART-7A2DEBA163` |
| Fabrication/supply content | TBD; physical equipment package is in scope, but detailed bill of materials, enclosure, battery, charger, bypass, distribution, and accessory details are not available in the accepted local source slices | Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-012-04_vendor-engineered-equipment-package`; unavailable detailed source slice |
| Installation supports and access interfaces | Must be coordinated with Structural / Foundations / Supports and Maintenance Access interface types; detailed loads, footprints, and access envelopes are TBD | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |

## References

- `_CONTEXT.md` for deliverable identity and local scope.
- `_REFERENCES.md` for accepted decomposition basis and available source pointers.
- Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-012-04_vendor-engineered-equipment-package`.
- Gate 7 `SCOPE_LEDGER.csv`, row `SOW-0013`.
- Gate 7 `ARTIFACT_REGISTER.csv`, rows `ART-F3CC1D5672` and `ART-7A2DEBA163`.
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-012-04_vendor-engineered-equipment-package`.
- Gate 7 `PROJECT_DECOMP.md`, section 5, objective rows `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, and `OBJ-010`.

