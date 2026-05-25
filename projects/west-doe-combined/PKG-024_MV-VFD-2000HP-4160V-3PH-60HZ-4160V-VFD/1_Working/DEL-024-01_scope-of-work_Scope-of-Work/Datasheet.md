# Datasheet: DEL-024-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-024-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-024 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |
| Package name | MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD | Gate 7 `PACKAGE_REGISTER.csv` row PKG-024; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 26 |
| Workbook ID / row | ID 24 / row 26 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-024; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 26 |
| WBS | 01 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |
| Tracking number | 26020-01-30-015 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |
| Discipline | Electrical | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis; DEC-001 |
| Scope item | SOW-0025 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0025 |
| Supports objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` Supports Objectives; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-024-01_scope-of-work |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts; Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-024-01_scope-of-work |
| Package-level major equipment text | TBD; no detailed major-equipment text is exposed in the accessible workbook row or Gate 7 package row beyond the package name `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`. | Workbook Packages row 26; Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |
| Tagged equipment | TBD; no equipment tag number is exposed in the accessible workbook row or Gate 7 package row for PKG-024. | Workbook Packages row 26; Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Package interfaces (source-supported) | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 26; Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-024 |
| Facility MV VFD context | The facility electrical basis lists medium-voltage VFDs among equipment that may be housed in prefabricated, modular electrical buildings, alongside MV switchgear, MV MCCs, MV reduced-voltage soft starters, 600 V MCCs, and UPS systems. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings section, line 2973 |
| Facility 4.16 kV MCC context | The 4.16 kV MCC provides mechanically latched fused contactors with motor protection relays and an Ethernet port to the plant PLC; VFD and soft-starter requirements for 4.16 kV motors are TBD in the facility basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Motor Control and Motor Specifications, lines 2957 and 3088 |
| Facility motor-class context | Larger motors on this facility shall be 4,000 V or 13.2 kV; motors 100 hp and larger shall be fed from soft starters or VFDs as required by the process. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Motor Control and Motor Specifications, lines 2961-2963 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 |
| Driven motor identity, tag, service, manufacturer, and topology (input cell count, output filter, bypass, harmonic mitigation, cooling, enclosure, environmental rating, weights, dimensions, support loads) | TBD; not present in accessible source slices for this deliverable. | Workbook Packages row 26; Gate 7 PKG-024 rows; DBM-Deepcut electrical sections |
| Driven equipment identification (2,000 hp, 4,160 V, 3-phase, 60 Hz load) | ASSUMPTION: package title indicates a 2,000 hp, 4,160 V, 3-phase, 60 Hz medium-voltage VFD with a 4,160 V output. The specific driven motor tag and process service are TBD; no accessible source slice ties the package to a named driven motor or driven process service. | Workbook Packages row 26; Gate 7 `PACKAGE_REGISTER.csv` row PKG-024; DBM-Deepcut motor-control sections |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package design, vendor documentation production, or physical equipment supply to the EPC Integrator. |
| Electrical Power | Identify the package as a medium-voltage electrical power interface; require coordination with facility 4.16 kV distribution and MV switchgear/MCC basis. Detailed feeder, protection, and metering values are TBD pending vendor data. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring EPC review and construction coordination consistent with the facility grounding basis (driven-pile electrodes, equipment double-grounding, separate ground conductors for transformers and motors larger than 100 hp). |
| I&C / Control Cabling | Carry I&C / control cabling as an interface; coordinate VFD control, run/start/stop, speed reference, and status signal routing with the plant PLC central control panel. Specific signal lists, communication protocols, and control architecture are TBD. |
| Communications / Network | Carry communications / network as an interface; coordinate any VFD network port (e.g., Ethernet to plant PLC) consistent with the facility's MV MCC/PLC integration basis. Specific protocol and addressing are TBD. |
| Maintenance Access | Carry maintenance access as an interface requiring layout and handoff coordination; equipment doors, removal paths, and clearances are TBD pending vendor envelope. |
| Structural / Foundations / Supports | Carry structural/support requirements as interface scope; package-specific loads, anchor pattern, and foundation requirements are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-024-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- `_REFERENCES.md`, decomposition basis and shared source root.
- Gate 7 `PROJECT_DECOMP.md`, mandatory EPC anchor deliverable basis and DEC-001.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-024.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0025.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-024-01_scope-of-work.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-024 rows (six interface categories).
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-024-01 rows.
- Gate 7 `ARTIFACT_REGISTER.csv`, DEL-024-01 rows.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 26 (referenced via Gate 7 registers; no local slice was extracted during PREPARATION).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Motor Control and Motor Specifications (lines 2953-2963) and Electrical Buildings (line 2973).
