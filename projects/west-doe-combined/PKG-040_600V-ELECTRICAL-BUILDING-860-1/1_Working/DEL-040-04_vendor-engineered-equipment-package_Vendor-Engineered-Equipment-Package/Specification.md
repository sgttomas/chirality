# Specification — DEL-040-04 Vendor Engineered Equipment Package (600V Electrical Building 860-1)

> Normative requirements for the Package Vendor production unit (engineering, design, fabrication/supply, physical equipment) for `PKG-040` (Building 860-1, 600V General Area / Tank Farm Electrical Building). Requirements derive from the accessible Deepcut DBM electrical source slices and the Gate 7 decomposition row. Inferred requirements are labelled `ASSUMPTION`; unsupported values are `TBD`.

## Scope

### Included

- Vendor engineering and design of the 600 V electrical building equipment package for `PKG-040` (Building 860-1, General Area / Tank Farm).
- Fabrication/supply of the physical equipment package: the prefabricated modular electrical building shell and the housed 600 V distribution and ancillary equipment (per DBM Electrical Buildings basis).
- Vendor package design basis and datasheet set supporting the equipment (ARTIFACT_REGISTER rows ART-409EB16E67, ART-A9C145C8F2).
- Integration review interfaces presented to the EPC Integrator for facility integration acceptance (`DEL-040-06`).

### Excluded

- Facility-level integration, tie-ins, constructability, and procurement/construction coordination — owned by the EPC Integrator per `PACKAGE_REGISTER` ownership statement for PKG-040.
- Civil/structural foundations and pile system beyond vendor-supplied building base steel and skid leveling provisions.
- Plant-wide grounding grid; vendor scope terminates at the building/equipment ground bus at specified connection points.
- Standby generator(s) where supplied as a separate package; vendor scope is limited to the 600 V MCC interface for transfer-switch terminations unless otherwise stated by `DEL-040-02`.
- Vendor document turnover package — that is `DEL-040-05`.
- Vendor package review and acceptance — that is `DEL-040-06`.
- Construction work package — that is `DEL-040-03`.

## Requirements

### REQ-040-04-001 — Low-voltage service basis

The 600 V equipment SHALL be engineered for 600 V, 3 phase, 3 wire, 60 Hz service, high-resistance grounded with a 5 A continuous neutral grounding resistor on each 600 V transformer secondary. (Source: DBM System Voltages, line 2937; Grounding, line 2985.)

### REQ-040-04-002 — Upstream feed configuration (ASSUMPTION shape; values TBD)

The 600 V bus SHALL be supplied radially through a 13.8 kV-to-600 V step-down transformer from the facility 13.8 kV switchgear. Transformer kVA, primary/secondary impedance, and feeder routing for Building 860-1 specifically: TBD pending `DEL-040-02 Package Datasheet`. (Source: DBM Power System lines 2919-2925.)

### REQ-040-04-003 — 600 V MCC composition and local control

The 600 V MCC(s) SHALL be traditional MCC construction with electronic motor overload relays. 600 V VFDs SHALL be built into the MCC lineup unless dedicated to large motors. A local control station (Hand-Off-Auto or On-Off as applicable) SHALL be provided adjacent to each driven motor and hard-wired to the MCC starter circuit by the field construction contractor. (Source: DBM Motor Control line 2959.)

### REQ-040-04-004 — 600 V MCC metering and ground-fault detection

The 600 V MCC SHALL include power metering and ground/resistor fault detection. Ground-fault protection on 600 V systems SHALL be alarm-only to maintain continuity of operations. (Source: DBM Grounding line 2985.)

### REQ-040-04-005 — 208/120 V distribution

A 600 V to 208/120 V, 3 phase, 4 wire, 60 Hz distribution transformer (or transformers) with solidly grounded neutral SHALL be provided where 208/120 V loads are served from this building. Each transformer SHALL feed its own 208/120 V distribution panelboard. (Source: DBM 208/120 V section line 2967.)

### REQ-040-04-006 — SCR heater-control panels

Where process-temperature controlled heaters are served from this building (including tank-area and freeze-protection heater loads where applicable to the General Area / Tank Farm), 600 V SCR heater-control panels SHALL be provided and supplied by feeder breakers in the 600 V MCC. (Source: DBM line 2969.)

### REQ-040-04-007 — UPS systems

Where required by detailed design, 120 V AC UPS systems (with battery banks and distribution panels) and 125 V DC UPS systems (with battery banks and distribution panels) SHALL be provided within the building. UPS larger than 10 kVA falls under low-voltage service distribution. UPS count, kVA, and battery autonomy: TBD pending `DEL-040-02`. (Source: DBM Electrical Buildings line 2973; System Voltages lines 2937-2939.)

### REQ-040-04-008 — Standby power interface

The 600 V MCC lineup SHALL accommodate a transfer-switch interface for TOU-typical low-voltage standby generator(s) supplying critical loads at the 600 V MCC level. Generator make/rating/transfer-switch configuration/load-shedding scheme: TBD per DBM. (Source: DBM Standby Power lines 2943-2945.)

### REQ-040-04-009 — Building shell, HVAC, and access

The prefabricated modular electrical building SHALL be sized for the housed equipment and SHALL be designed for indoor general-purpose-area installation. HVAC SHALL be sized as an n+1 system. Equipment doors SHALL be sized for, or include removable transom sections to allow, removal of the largest equipment. An outdoor GFI receptacle SHALL be provided for exterior maintenance. (Source: DBM Electrical Buildings lines 2971-2979.)

### REQ-040-04-010 — Cable entry and termination basis

The building SHALL be designed for bottom entry of incoming and outgoing power cables, with the building elevated to provide cable-tray space beneath. Internal wiring SHALL use TECK and ACIC cables; EMT conduit SHALL be used between adjacent equipment (e.g., control panels to contactor panels). Termination compartments SHALL accommodate ACWU cable (#1/0 AWG and larger, including 600 V transformer secondary to MCC) and copper TECK cable (low-voltage power smaller than #1/0 AWG). (Source: DBM Electrical Buildings line 2977; Cables lines 3010-3012.)

### REQ-040-04-011 — Grounding interface

Major electrical equipment in the building SHALL be directly connected to the facility ground grid at two points. Ground wells with bolted ground connections at test points SHALL be provided for the building. Above-grade grounding conductors SHALL be green insulated ground wires in PVC conduit where mechanical protection is required, with compression-type ground connections. (Source: DBM Grounding lines 2985-2989.)

### REQ-040-04-012 — Plant PLC and network interface

Plant PLC control panel(s) and network rack(s) housed in the building SHALL be integrated with the plant control architecture; power and control circuits at 13.8 kV / 4,160 V / 600 V SHALL be separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications. (Source: DBM Electrical Buildings line 2973.)

### REQ-040-04-013 — Codes and standards

The package SHALL be designed in accordance with the Canadian Electrical Code (CEC) for spacing, conductor sizing, transformer accessories, and installation provisions; and in accordance with the project electrical specifications and applicable industry standards for LV switchgear, MCCs, VFDs, and UPS. Specific clause-level code editions: location TBD pending extraction of `26020-Package_Requirements.docx`. (Source: DBM lines 2866, 2949, 2989; HRR-040-04-003.)

### REQ-040-04-014 — Interface obligations

The package SHALL provide engineered interfaces consistent with the PKG-040 PACKAGE_REGISTER applicable interface types: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Detailed interface clauses are governed by `DEL-040-02 Package Datasheet`. (Source: Gate 7 `INTERFACE_REGISTER.csv` 12 rows for PKG-040.)

### REQ-040-04-015 — Quantity allocation

Quantity allocation of the DBM Equipment List low-voltage switchgear, low-voltage MCC, and low-voltage induction-motor rows to PKG-040 SHALL be confirmed by the EPC Integrator via `DEL-040-02 Package Datasheet`. Quantities carried in this deliverable are TBD until confirmed. (HRR-040-04-002.)

### REQ-040-04-016 — Building served-area and feed designation

Whether Building 860-1 shares a footprint with the 4.16 kV General Area distribution called out in DBM Power System line 2925, and the specific 13.8 kV-to-600 V transformer feeding 860-1, SHALL be confirmed by the EPC Integrator. Carried as TBD pending `DEL-040-02`. (HRR-040-04-001.)

## Standards (governing — location TBD where not extracted)

- Project package requirements: `_Sources/26020-Package_Requirements.docx` — location TBD.
- Canadian Electrical Code (CEC), CSA C22.1-21 — referenced in DBM (line 2866); clause TBD.
- Applicable BC provincial and local electrical codes and regulations; Technical Safety BC and BCER authorities — DBM line 2866.
- API RP-505 — referenced in DBM for area classification (general project context, line 2907).
- IEEE / ANSI / NEMA series for LV switchgear, MCCs, VFDs, and UPS — ASSUMPTION: likely applicable; not explicitly cited in accessible sources.
- Project electrical specifications Table 12-1 (ELC-QAS-000001 through ELC-QAS-000018) — DBM lines 2872-2892; binding revision TBD.
- Gate 7 PROJECT_DECOMP snapshot — accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts.

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-040-04-001 | Vendor design basis review confirming 600 V / 3ph / 3w / 60 Hz HRG with 5 A continuous resistor. |
| REQ-040-04-002 | Confirmation that vendor sizing assumptions reflect accepted load-flow study outputs when issued, and align with `DEL-040-02` transformer designation. |
| REQ-040-04-003 | Inspection of MCC general arrangement, schematics, and local control station drawings. |
| REQ-040-04-004 | FAT confirmation of metering and ground/resistor fault detection; alarm-only configuration verified. |
| REQ-040-04-005 | Drawing review of 600 V → 208/120 V transformer secondary grounding and panelboard split. |
| REQ-040-04-006 | Drawing review of SCR heater-control panels and feeder-breaker assignments. |
| REQ-040-04-007 | Datasheet/drawing review of UPS systems against `DEL-040-02` requirements. |
| REQ-040-04-008 | Review of MCC transfer-switch interface provisions against standby-generator package. |
| REQ-040-04-009 | Building general arrangement and HVAC capacity check; door/transom sizing check; GFI receptacle present. |
| REQ-040-04-010 | Building base/elevation and cable-entry review; termination compartment review for ACWU/TECK cable accommodation. |
| REQ-040-04-011 | Inspection of grounding details, ground wells, conductor type/conduit, and connection method. |
| REQ-040-04-012 | Review of PLC/network rack interfaces and circuit separation arrangement. |
| REQ-040-04-013 | Vendor declaration of code compliance and listing/certification evidence. |
| REQ-040-04-014 | Interface verification against `DEL-040-02 Package Datasheet` interface matrix and `INTERFACE_REGISTER.csv`. |
| REQ-040-04-015 | EPC Integrator confirmation of equipment quantities via `DEL-040-02`. |
| REQ-040-04-016 | EPC Integrator confirmation of Building 860-1 served-area extent and transformer feed designation. |

Independent verification mechanisms (FAT witness, site acceptance test, integration acceptance) are governed by `DEL-040-06 EPC Vendor Package Review and Acceptance` (sibling deliverable).

## Documentation

The Package Vendor SHALL produce, at minimum:

- Vendor package design basis.
- Vendor equipment datasheet set (building, MCC, VFDs, UPS, transformers, panels, SCR panels, PLC/network panels).
- One-line and three-line diagrams for the package.
- Termination, grounding, and interface drawings.
- Protection, metering, and control schematics; PLC/network interface description.
- Building general arrangement, HVAC, lighting, and access drawings.
- Factory test plans, FAT procedures, and FAT records (records turned over via `DEL-040-05`).
- Installation, operation, and maintenance manuals.

Full vendor document register, submittal cadence, and turnover records are owned by `DEL-040-05 Vendor Document Turnover Package`.
