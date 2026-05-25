# Datasheet: DEL-014-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-014-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-014 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 |
| Package name | CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE | Gate 7 `PACKAGE_REGISTER.csv` row PKG-014; workbook Packages row 16 |
| Workbook ID / row | ID 14 / row 16 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 |
| WBS | 02 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 |
| Tracking number | 26020-02-30-005 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 |
| Discipline | Electrical | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-014-01_scope-of-work |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md`; `_CONTEXT.md` Notes |
| Scope item | SOW-0015 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0015 |
| Supports objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 (package-grouped, ASSUMPTION best-effort mapping) | `_CONTEXT.md` Supports Objectives; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-014-01_scope-of-work |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-014-01_scope-of-work |
| Tagged equipment | TBD; no equipment tag numbers exposed in the accessible workbook row or Gate 7 package row. | Workbook Packages row 16; Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility low-voltage service context | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5A continuous resistor; serves motors 3/4 hp through 250 hp, DOL starting, lighting transformers, building heaters, and UPS larger than 10 kVA. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Power Distribution table, Low-voltage service row. |
| Facility lighting and utility service context | 120/208 V, 3 phase, 4 wire, 60 Hz solid grounded; serves lighting, receptacles, heat trace, small motors, and UPS 10 kVA or smaller. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Power Distribution table, Lighting and utility row. |
| Building exhaust fan / heater control context | Remote I/O nodes may support building exhaust fan and heater controls; 208/120 V AC power serves building exhaust fans and building heater blower fans. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Remote I/O); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (208/120 V loads). |
| Contactor-panel housing context | Electrical buildings shall house 208/120 V contactor panels alongside MV/LV switchgear, MCCs, UPS systems, and PLC/network racks; EMT conduit shall be used between adjacent control panels and contactor panels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. |
| Package interfaces (Gate 7 flagged YES) | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 16; Gate 7 `INTERFACE_REGISTER.csv` PKG-014 rows. |
| Package-specific exclusions | TBD; no package-specific exclusions stated in accessible source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-014. |
| Design values for contactor-panel counts, ratings, lineup, enclosure, environmental class, load schedules, and lighting/exhaust-fan branch circuit details | TBD; not exposed in accessible source slices for this deliverable. | Workbook Packages row 16; Gate 7 PKG-014 rows; DBM electrical sections. |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package design or contactor-panel engineering to the EPC Integrator. |
| Electrical Power | Identify the package as a low-voltage electrical power interface and require coordination with facility 600 V LV and 120/208 V lighting/utility distribution basis. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring EPC review and construction coordination, consistent with the facility HRG LV grounding basis. |
| Area / Exterior Lighting | Carry area/exterior lighting as an interface for the contactor-panel lighting control scope; specific lighting branch assignments are TBD pending vendor data. |
| I&C / Control Cabling | Carry I&C / control cabling as an interface, including control wiring between Remote I/O / control panels and contactor panels. |
| Communications / Network | Carry communications/network as an interface for any contactor-panel monitoring or status reporting; specific protocol and node count TBD. |
| Maintenance Access | Carry maintenance access as an interface requiring layout, equipment door sizing, and handoff coordination. |
| Structural / Foundations / Supports | Carry structural/support requirements as interface scope; contactor-panel weights, mounting, and seismic loads TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-014-01 identity, scope, artifacts, objective context.
- `_REFERENCES.md`, decomposition and source pointers.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, package anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-014.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-014-01_scope-of-work.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0015.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-014 rows.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Power Distribution table and Remote I/O notes.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings, contactor-panel housing, and 208/120 V AC loads.
