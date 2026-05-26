# Specification — DEL-042-02 Package Datasheet (PKG-042 Control Room Building)

> Normative document. Requirements derived from accessible source slices; inferred items labeled ASSUMPTION; unavailable values marked TBD.

## Scope

This specification governs the data content of the Package Datasheet for the Control Room Building (PKG-042). It covers technical handoff content required by third-party vendors or by discipline design teams to engineer, design, fabricate, and integrate the Control Room Building.

**Includes:** package identification, building functional role, hosted controls/IT equipment, building envelope, electrical scope, site spacing, interface requirements matrix, applicable standards.

**Excludes:** the EPC Scope of Work (DEL-042-01), the Construction Work Package (DEL-042-03), and the Vendor Engineered Equipment Package (DEL-042-04). Detailed mechanical/HVAC/F&G design content is referenced by interface but not duplicated.

## Requirements

### R-1 Identification (Mandatory)
The Package Datasheet shall identify the package by `PackageID = PKG-042`, name `Control Room Building`, and reference the Scope of Work (`SOW-0043`). [Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 235]

### R-2 Functional Role (Mandatory)
The datasheet shall state that the Control Room Building serves as the central operations control room providing the environment for operations personnel to monitor and control the facility. [Source: DBM-Deepcut §3119]

### R-3 Hosted Controls Equipment (Mandatory)
The datasheet shall list, at minimum: operator workstations (initial design basis: three workstation sets), engineering workstations, primary controls servers (two fault-tolerant physical hosts), and core network switches located in the control room. [Source: DBM-Deepcut §3141, §3165, §3184]

### R-4 Operator Workstation Configuration (Mandatory)
Each operator workstation shall include four monitors in a 2x2 arrangement, monitors ≥ 24 inches at 1920x1080 minimum (unless HMI requires otherwise). [Source: DBM-Deepcut §3184]

### R-5 Server Redundancy (Mandatory)
Primary controls hosts shall be located in the control room; the secondary host shall be located in the motor control center / low-voltage MCC room. [Source: DBM-Deepcut §3165; DBM-Comp_and_Liquids §796]

### R-6 Packaged Equipment Monitoring Interface (Mandatory)
The datasheet shall state that process monitoring from packaged equipment shall be available at the central control room. [Source: DBM-Deepcut §3121]

### R-7 Alarm Beacon Interface (Mandatory)
The datasheet shall include the requirement for beacon groups on the control room exterior as part of the facility alarm strategy. [Source: DBM-Deepcut §3262, §3293]

### R-8 Wiring Method (Mandatory)
The datasheet shall specify wiring methods consistent with the DBM: EMT permitted in control rooms as non-process locations; rigid conduit where building is fabricated and erected in assembly shop prior to shipment; minimum conduit size 21 mm (3/4 in); compliance with CEC and area classification. [Source: DBM-Deepcut §3025]

### R-9 Spacing Constraints (Mandatory)
The datasheet shall record minimum spacing constraints:
- 15.24 m (50 ft) from pressurized bullets and process buildings (API 2510). [Source: DBM-Deepcut §254]
- 25 m (82 ft) from fired heater to control room or electrical buildings (OGAOM §9.6.15). [Source: DBM-Deepcut §298]

### R-10 Foundation Basis (Mandatory)
The datasheet shall require the control room foundation design to be based on the final geotechnical report with equipment-specific foundation/anchorage checks and the project snow/wind/seismic, frost, vibration, and settlement criteria. [Source: DBM-Comp_and_Liquids §700]

### R-11 Building Coordination (Mandatory)
The datasheet shall state coordination items: area classification, ventilation, heating, emergency egress, F&G detection, ESD pushbutton placement, RIO panel locations, power distribution, maintenance access. [Source: DBM-Comp_and_Liquids §704]

### R-12 Construction Mode (ASSUMPTION → Mandatory pending ruling)
The datasheet shall indicate fabrication mode "Shop" per the package list designation 800-1 Office/Control Building "Shop", with field activities limited to install on site or modify if existing. [Source: DBM-Deepcut §2810, §2759]

### R-13 Interface Requirements Matrix (Mandatory)
The datasheet shall contain an Interface Requirements Matrix enumerating each external interface (controls network, electrical power, HVAC, F&G, telecom/security, civil/structural) with counterpart, requirement, and source. Unknown values may be `TBD` but the row shall be present.

### R-14 Discipline / Responsibility (Mandatory)
The datasheet shall identify Discipline = Electrical (with multi-discipline interfaces) and ResponsibleParty = EPC Integrator. [Source: `_CONTEXT.md`; multi-discipline scope ASSUMPTION based on building scope coordination items.]

### R-15 Provenance (Mandatory)
Every non-trivial value in the datasheet shall cite a source (SourcePath + SectionRef) or be marked `location TBD`. Inferred items shall be labeled `ASSUMPTION`.

### R-16 Stable Schema (Mandatory)
The datasheet shall preserve the default section schema: Identification, Attributes, Conditions, Construction, References. Additional sections (e.g., Interface Requirements Matrix) are permitted and required where listed above.

## Standards

| Standard | Use | Location |
|---|---|---|
| API 2510 | LPG spacing | DBM-Deepcut §254; primary text TBD |
| OGAOM §9.6.15 | Fired heater spacing | DBM-Deepcut §298; primary text TBD |
| Canadian Electrical Code (CEC) | Building wiring and area classification | DBM-Deepcut §3025; primary text TBD |
| 26020-Package_Requirements.docx | EPC package requirements | Local file present; not text-readable in this environment; location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1, R-14 | Document review against `_CONTEXT.md` and decomposition register. |
| R-2, R-6 | Document review against DBM-Deepcut §3119, §3121. |
| R-3, R-4, R-5 | Document review against DBM-Deepcut §3141, §3165, §3184 and DBM-Comp_and_Liquids §796. |
| R-7 | Cross-check against facility alarm strategy in DBM-Deepcut §3262, §3293. |
| R-8 | Wiring method review against DBM-Deepcut §3025; CEC clause review when source accessible. |
| R-9 | Plot plan / spacing study review; API 2510 and OGAOM clause check when sources accessible. |
| R-10, R-11 | Geotechnical report review; building coordination matrix review. |
| R-12 | Confirm against package list 800-1 designation. |
| R-13 | Datasheet content review; presence and completeness of matrix rows. |
| R-15, R-16 | Document QA against `four-documents/QA_CHECKS.md`. |

## Documentation

The datasheet anticipates the following artifacts (per `_CONTEXT.md`):

- Package technical datasheet (this deliverable)
- Vendor engineering handoff basis
- Package interface requirements matrix (embedded in datasheet)
- Source-supported equipment and design criteria
