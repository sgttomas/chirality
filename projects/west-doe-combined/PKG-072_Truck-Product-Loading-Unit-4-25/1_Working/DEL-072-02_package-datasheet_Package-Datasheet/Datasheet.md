# Datasheet: DEL-072-02 Package Datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-072-02_package-datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet` |
| Parent package | PKG-072 - Truck Product Loading Unit 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-072` |
| Workbook ID / row | 72 / row 99 | `PACKAGE_REGISTER.csv` row `PKG-072` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-072` |
| CoA tracking number | 26020-01-23-001 | `PACKAGE_REGISTER.csv` row `PKG-072` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-072` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet` |
| Covered scope items | SOW-0245; SOW-0246; SOW-0247; SOW-0248 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` rows `SOW-0245`..`SOW-0248` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope statement | Carry the workbook-defined vendor-responsible Mechanical package "Truck Product Loading Unit 4-25" as a distinct flat project package for WBS 01; the Package Vendor owns engineering/design/equipment and the EPC Integrator owns facility integration. | `SCOPE_LEDGER.csv` row `SOW-0245` |
| Datasheet purpose | Integrator-authored technical handoff data required for third-party package engineering and design. | `ARTIFACT_REGISTER.csv` artifact `ART-1E30749941` |
| Vendor / discipline handoff basis | Technical basis, battery limits, design expectations, and source-supported requirements to be handed to the package delivery entity. | `ARTIFACT_REGISTER.csv` artifact `ART-6F113CE055` |
| Interface requirements matrix | Workbook interface facts are carried as datasheet evidence for third-party engineering/design handoff. | `ARTIFACT_REGISTER.csv` artifact `ART-170CD144CD` |
| Major included equipment (per source row) | ASSUMPTION (CONFLICT): A skid for the system to be mounted on; a fuel gas heater capacity TBD with SCR (600V) control and skin-temperature override; a fuel gas scrubber sized using a k factor of 0.35 (imperial) maximum plus de-ration factor. Source row text describes fuel-gas equipment, which conflicts with the package name "Truck Product Loading Unit 4-25"; see Guidance Conflict Table HRR-072-02-001. | `ARTIFACT_REGISTER.csv` artifact `ART-92126744C5`; `SCOPE_LEDGER.csv` row `SOW-0247`; 26020-Package_Requirements.docx package heading 26 |
| Interface fact | Process Piping | `INTERFACE_REGISTER.csv` row `IFC-7DA48FE453`; `ARTIFACT_REGISTER.csv` artifact `ART-443319758F` |
| Interface fact | Drain / Containment | `INTERFACE_REGISTER.csv` row `IFC-54A006CB40`; `ARTIFACT_REGISTER.csv` artifact `ART-D9CF09E777` |
| Interface fact | Electrical Power | `INTERFACE_REGISTER.csv` row `IFC-56B91F1F2C`; `ARTIFACT_REGISTER.csv` artifact `ART-8A0FFB57FB` |
| Interface fact | Grounding / Bonding | `INTERFACE_REGISTER.csv` row `IFC-D2B00B4765`; `ARTIFACT_REGISTER.csv` artifact `ART-DE562D23BF` |
| Interface fact | Area / Exterior Lighting | `INTERFACE_REGISTER.csv` row `IFC-7ACEBA3962`; `ARTIFACT_REGISTER.csv` artifact `ART-9F06DBE170` |
| Interface fact | I&C / Control Cabling | `INTERFACE_REGISTER.csv` row `IFC-CC2FFD98C5`; `ARTIFACT_REGISTER.csv` artifact `ART-352E6EE5FF` |
| Interface fact | Building HVAC / Services | `INTERFACE_REGISTER.csv` row `IFC-AC31864294`; `ARTIFACT_REGISTER.csv` artifact `ART-A0DD2CBD97` |
| Interface fact | Fire & Gas / Safety Systems | `INTERFACE_REGISTER.csv` row `IFC-FC828A3F07`; `ARTIFACT_REGISTER.csv` artifact `ART-2227A8EDAD` |
| Interface fact | Grading / Site Drainage / Spill Containment | `INTERFACE_REGISTER.csv` row `IFC-4591BAA704`; `ARTIFACT_REGISTER.csv` artifact `ART-90CF023A4A` |
| Interface fact | Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` row `IFC-8DD643386F`; `ARTIFACT_REGISTER.csv` artifact `ART-EE48A43E43` |
| Interface fact | Product Loading | `INTERFACE_REGISTER.csv` row `IFC-E3B7B98B0B`; `ARTIFACT_REGISTER.csv` artifact `ART-2BAC93EBC4` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating pressure | 150 psig | `SCOPE_LEDGER.csv` row `SOW-0248`; 26020-Package_Requirements.docx package heading 26 (Scope Notes / Open Items) |
| Design pressure | 150 psig | `SCOPE_LEDGER.csv` row `SOW-0248` |
| MAWP | TBD | `SCOPE_LEDGER.csv` row `SOW-0248` |
| Ambient temperature range | -19 C to 22.2 C | `SCOPE_LEDGER.csv` row `SOW-0248` |
| Design temperature range | -40 C to 35 C | `SCOPE_LEDGER.csv` row `SOW-0248` |
| Design flow (per source row) | ASSUMPTION (CONFLICT): > 8.4 MMSCFD (237.5 e3m3/day), gas heated to 95 F (35 C); final flow TBD. Throughput is stated in source text describing a fuel-gas skid and may not apply to a truck loading station; see Guidance HRR-072-02-001. | `SCOPE_LEDGER.csv` row `SOW-0248` |
| Driver / electrical control | SCR heater control panels at 600V, located in electrical building | `SCOPE_LEDGER.csv` row `SOW-0248` |
| Objective context | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 are mapped to this deliverable. | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-072-02_package-datasheet` |
| Facility context | 04-25 Deepcut sour-gas processing facility (Mechanical, WBS 01). | `OBJECTIVE_REGISTER.csv` row `OBJ-001`; `PACKAGE_REGISTER.csv` row `PKG-072` |
| Commercial / boundary context | Truck loading is a named commercial-stream boundary; product accountability and metering are within preserved decomposition objectives. | `OBJECTIVE_REGISTER.csv` row `OBJ-003` |
| Declared upstream dependencies | None declared. | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared. | `_DEPENDENCIES.md` |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction-facing companion deliverable | DEL-072-03_construction-work-package | `DELIVERABLE_REGISTER.csv` row `DEL-072-03_construction-work-package` |
| Vendor production unit companion deliverable | DEL-072-04_vendor-engineered-equipment-package | `DELIVERABLE_REGISTER.csv` row `DEL-072-04_vendor-engineered-equipment-package` |
| Construction handoff relevance | Installation, tie-in piping, electrical tie-in, and on-site assembly are by others (i.e., handled outside the vendor package scope) per source notes; carried to the construction work package. | `SCOPE_LEDGER.csv` row `SOW-0248`; `DELIVERABLE_REGISTER.csv` row `DEL-072-03_construction-work-package` |
| Major equipment construction criteria | TBD - detailed mechanical, structural, and process design values for the truck loading station (pump count, meter sizing, loading-arm configuration, vapor recovery routing, grounding-stud locations, secondary containment sizing) are not stated in the Gate 7 accepted snapshot at clause level; source row text describes fuel-gas equipment that conflicts with the package name (see Guidance HRR-072-02-001). | `PACKAGE_REGISTER.csv` row `PKG-072`; 26020-Package_Requirements.docx package heading 26 |
| Codes and standards | TBD at clause level. DBM-Deepcut/4-25_Deepcut_DBM.md references API 2510 for distance between pressurized bullets and truck loading station, and Deepcut DBM Section on grounding requires facility-installed ground studs connected to the facility main ground grid for truck-out connections. | `_REFERENCES.md`; DBM-Deepcut/4-25_Deepcut_DBM.md (truck loading references) |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 final published `PROJECT_DECOMP.md`
- Gate 7 final published `PACKAGE_REGISTER.csv` row `PKG-072`
- Gate 7 final published `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet`
- Gate 7 final published `ARTIFACT_REGISTER.csv` rows scoped to `DEL-072-02_package-datasheet`
- Gate 7 final published `INTERFACE_REGISTER.csv` rows scoped to `PKG-072`
- Gate 7 final published `OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`
- Gate 7 final published `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-072-02_package-datasheet`
- Gate 7 final published `SCOPE_LEDGER.csv` rows `SOW-0245`, `SOW-0246`, `SOW-0247`, `SOW-0248`
- 26020-Package_Requirements.docx package heading 26 (source row)
- DBM-Deepcut/4-25_Deepcut_DBM.md (truck loading and grounding references)
