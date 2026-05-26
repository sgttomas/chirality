# Datasheet: DEL-071-04 Vendor Engineered Equipment Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-071-04_vendor-engineered-equipment-package |
| Deliverable name | Vendor Engineered Equipment Package |
| Parent package | PKG-071 |
| Package name | Fuel Gas Skid 4-25 |
| Workbook ID / row | 71 / row 61 |
| WBS | 01 |
| CoA / tag number | 26020-01-23-001 (package); equipment tag 26020-01-PT-23-001 — Fuel Gas Skid |
| Discipline | Mechanical |
| Deliverable type | Vendor Package Production Unit |
| Responsible party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| Source basis | Workbook Packages row 61; 26020-Package_Requirements.docx package heading 25; Gate 7 PROJECT_DECOMP snapshot |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Skid-mounted Low-Pressure Fuel Gas package serving the low-pressure fuel gas system for the West Doe Deep Cut Facility | Gate 7 `PACKAGE_REGISTER.csv`, PKG-071; `SCOPE_LEDGER.csv`, SOW-0100 |
| Package responsibility model | Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) | Gate 7 `PACKAGE_REGISTER.csv`, PKG-071 |
| Anchor inputs for vendor work | EPC Scope of Work (DEL-071-01) and EPC Package Datasheet (DEL-071-02) | `_CONTEXT.md`, Scope; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-071-01 / DEL-071-02 |
| Major included equipment | (1) Skid for the system to be mounted on; (1) low-pressure fuel gas heater — capacity TBD; (1) low-pressure fuel gas scrubber — vendor-designed | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101 |
| Heater control basis | Heater controlled by SCR (600 V); SCR heater control panels located in electrical building; heater shall include skin-temperature thermocouple override control | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101; SOW-0102 |
| Scrubber sizing basis | k factor of 0.35 (imperial) maximum plus de-ration factor for operating pressure; vendor to design | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101 |
| Source-supported interface types (vendor must support these tie-ins) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | Gate 7 `INTERFACE_REGISTER.csv`, PKG-071 (12 declared interfaces) |
| Package-specific exclusions | TBD; no package-specific exclusions stated in accessible source materials beyond the by-others items listed under Construction | Gate 7 `PACKAGE_REGISTER.csv`, PKG-071 |

## Conditions

| Condition | Value / basis | Source |
|---|---|---|
| Design Flow Required | > 8.4 MMSCFD (237.5 e3m3/day); final flow TBD | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| Outlet gas temperature | Gas heated to 95 F (35 C) | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| Operating Pressure | 150 psig | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| Ambient Temperature | -19 C to 22.2 C | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| Design Pressure | 150 psig | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| Design Temperature | -40 C to 35 C | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| MAWP | TBD | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| Heating value | TBD (not stated for 4-25 in accessible source); ASSUMPTION: comparable to companion package 3-25 basis (1040 BTU/SCF) unless EPC Package Datasheet states otherwise | Gate 7 `SCOPE_LEDGER.csv`, SOW-0098 (companion 3-25); to be confirmed against DEL-071-02 |
| Facility process role | Low-pressure fuel gas serves blanket, purge, sweep/drive, stripping, and supplemental fuel duties across inlet separation, MPFF, stabilizers, amine treating, TEG dehydration, VRU make-up, caustic and DSO tank blanketing, and incinerator supplemental fuel | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, fuel-gas usage descriptions |

## Construction

| Construction item | Current basis | Source |
|---|---|---|
| Vendor scope | Engineering, design, fabrication / supply, and the physical equipment package developed from the EPC Scope of Work and Package Datasheet | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-071-04; `_CONTEXT.md`, Scope |
| By-others (excluded from vendor scope) | Shipping packages to site, installation, tie-in piping, electrical tie-in, etc. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 |
| Anticipated artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set | `_CONTEXT.md`, Anticipated Artifacts; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-071-04 |
| Vendor documentation handoff | Vendor document register, submittals, and source-required vendor documentation are produced under DEL-071-05 (Vendor Document Turnover Package) | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-071-05 |
| Integration acceptance | EPC Integrator review and acceptance occurs under DEL-071-06 (EPC Vendor Package Review and Acceptance) | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-071-06 |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, PKG-071 row
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, DEL-071-04 row (and DEL-071-01, -02, -05, -06 for upstream/downstream)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`, SOW-0099 through SOW-0102
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`, PKG-071 rows (12 interface types)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, fuel-gas service descriptions
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx`, package heading 25 (binary; location TBD until converted)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 61 (binary; location TBD until converted)
