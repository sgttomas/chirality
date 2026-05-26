# Specification: DEL-048-01 — Scope of Work, PKG-048 Inlet / Sales Compressors

## Scope

### In Scope (EPC Integrator Scope of Work for PKG-048)

The EPC Integrator shall deliver a complete Scope of Work record for PKG-048 — Inlet / Sales Compressors — covering five (5) parallel multi-service reciprocating compressor packages at the 04-25 West Doe Deep Cut Gas Plant expansion. The Scope of Work shall include:

1. Tagged equipment and package identity list (per Datasheet).
2. Package function and integration narrative (per Guidance and this Specification).
3. Source basis citations (Workbook Packages row 65; 26020-Package_Requirements.docx package heading 3; DBM-Deepcut SEC-05).
4. Process and facility boundaries (this Specification, Section "Process Boundaries").
5. Whole-facility integration narrative (interfaces listed in Section "Interfaces and Tie-Ins").
6. Responsibility assignment record (this Specification, Section "Responsibility Assignment").

Source: _CONTEXT.md (Anticipated Artifacts; Scope); DELIVERABLE_REGISTER.csv (DEL-048-01 row).

### Out of Scope

- Package engineering, package design, vendor documentation, and physical equipment supply — owned by the Package Vendor (Source: PACKAGE_REGISTER.csv Responsibility).
- Cryogenic recovery, amine sweetening, TEG dehydration, sales gas booster compression (PKG-049), acid gas injection compression — addressed in separate packages (Source: DBM-Deepcut SEC-04, SEC-05; PACKAGE_REGISTER.csv).
- Disposal-well interface — external scope (Source: DBM-Deepcut SEC-05 Acid Gas Disposal Well Interface).
- Specific package exclusions — no package-specific exclusions are stated in source materials (TBD pending RFQ confirmation). Source: PACKAGE_REGISTER.csv ("TBD; no package-specific exclusions stated in source materials").

## Requirements

### R-1 — Package Configuration

The package vendor shall supply five (5) inlet/sales gas multi-service reciprocating compressor packages, each providing one sour inlet gas compression stage and two sweet sales gas compression stages on a common compressor frame.
Source: PACKAGE_REGISTER.csv Scope; DBM-Deepcut SEC-05 Compression Configuration.

### R-2 — Per-Package Sizing

Each compressor shall be sized for 120% of its proportional share (5 x 20% nominal configuration with per-unit oversize).
Source: PACKAGE_REGISTER.csv Scope ("Each compressor shall be sized for 120%"); DBM-Deepcut SEC-05 Compression Configuration ("Five x 20%; no installed spare package").

### R-3 — Inlet Service Design Conditions

The inlet service shall meet:
- Per-package capacity: 62.4 MMSCFD supported basis (60 MMSCFD appears in some detailed tables — TBC).
- Suction pressure: 4,309 kPag (625 psig) service basis; 385 psig at compressor cylinder inlet.
- Discharge pressure: 7,791 kPag (1,130 psig) service basis.
- Operating inlet temperature: 27.3 deg C winter / 35.7 deg C summer; J-T mode TBD.
- Minimum MAWP: 9,032 kPag (initial estimate, suction and discharge).
Source: DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions" table.

### R-4 — Sales Service Design Conditions

The sales service shall meet:
- Per-package capacity: 57.6 MMSCFD.
- Suction pressure: 440 psig service basis (430 psig normal in detailed pressure table).
- Discharge pressure: 10,343 kPag (1,500 psig) current supported basis; 1,700 psig second-stage detailed estimate TBC.
- Suction temperature: 43.3 deg C first stage; 71.1 deg C second stage.
- Minimum MAWP: 9,032 kPag lower sales stages; 13,100 kPag third-stage discharge.
Source: DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions" table.

### R-5 — Compressor Frame and Driver

- Compressor frame: Ariel KBC/6 preliminary, to be confirmed; legacy conflicting frame reference unresolved — model selection is TBD pending human ruling.
- Driver: 6,700 hp, 3-phase electric induction motor (conflict against 7,000 hp legacy value — TBD).
- Motor start method: per DBM-Deepcut SEC-05, Starting VFD with synchronous transfer to normal-service bus after full speed. Workbook scope row 65 states "DOL driver with a soft-start." CONFLICT — see Guidance Conflict Table CT-1.
Source: PACKAGE_REGISTER.csv Scope; DBM-Deepcut SEC-05 Inlet/Sales Compressor Basis.

### R-6 — Suction Pressure Control

The inlet-service suction pressure control valve shall allow 5 psid differential pressure, be an ET-type control valve, and fail closed. No modulating suction pressure control valve is included on the sales service; sales-service suction pressure is regulated by the upstream J-T valve and expander, with package loading regulated through the inlet-service suction pressure control valve.
Source: DBM-Deepcut SEC-05.

### R-7 — Suction Scrubbers

Two-phase suction scrubbers shall be provided upstream of each compression stage. Sales-service scrubber necessity shall be evaluated during detailed engineering due to low dewpoint of the inlet gas. Sizing shall use K factor not greater than 0.5 Imperial with operating-pressure de-rating; assumed inlet liquid density 0.61 SG. Horizontal and vertical vane-style demisters are acceptable.
Source: DBM-Deepcut SEC-05.

### R-8 — Air Cooler

Each package shall include a common air-cooler frame for both compression services with the following cooler outlet basis: 1st stage inlet 35.0 deg C winter / 43.3 deg C summer; 2nd stage sales 71.1 deg C (both seasons); 3rd stage sales 35.0 deg C winter / 43.3 deg C summer. Simulated gas-section pressure drop: 69.0 kPad (1st and 3rd), 34.5 kPad (2nd). Design pressure drops TBD. Automated pneumatic louver control required.
Source: DBM-Deepcut SEC-05 cooler basis table.

### R-9 — Blowdown and Recycle

- Inlet-service blowdown valve fails open; sales-service blowdown valve fails closed.
- Dedicated recycle control valves per service, sized for 100% capacity at minimum pipeline operating pressure and high suction pressure.
- Inlet-service recycle valve fail position currently stated fail open — TBD.
- Sales-service recycle valve fail position currently stated fail closed — TBD.
- Single full-port manual isolation valve on the outlet of each recycle control valve.
Source: DBM-Deepcut SEC-05.

### R-10 — Start, Purge, Drains, and Lube

- Designed to start from equalization pressure in both services; if equalization exceeds MAWP, alternate is to depressure back into respective inlet headers.
- Isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, and shutdown sequences automated.
- Electric circulating lube oil heater on each frame for quick start.
- Manual sweet gas purge from fuel gas on sour inlet system for maintenance sweeping.
- Packing drains and vents collected to common seal pot; seal-pot vapour to VRU suction header; liquids by local truck-out.
- Sweet-service distance pieces require sweep purge to prevent sour gas backflow from the shared packing drain/vent recovery system.
Source: DBM-Deepcut SEC-05.

### R-11 — Clearance Pockets

Automated continuously variable or automated fixed-volume clearance pockets shall be evaluated during detailed engineering against standard manual variable volume clearance pockets. Final selection TBD.
Source: DBM-Deepcut SEC-05.

### R-12 — Sparing

No installed spare package and no spare package-level equipment or instrumentation.
Source: DBM-Deepcut SEC-05 design table; Compression Configuration table.

### R-13 — Interfaces and Tie-Ins (EPC Integrator Scope)

Applicable interface types — the EPC Integrator scope shall cover integration of:
Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
Source: PACKAGE_REGISTER.csv (Applicable interface types).

### R-14 — Process Boundaries

| Boundary | Description |
|---|---|
| Inlet service suction | Sour gas from inlet/TEG heat exchanger, combined with West Doe sour gas from 03-25 Compressor Station |
| Inlet service discharge | To downstream amine sweetening |
| Sales service suction | Sweet sales gas from turbo expander compressor aftercooler (440 psig, 110 deg F) |
| Sales service discharge | To Sales Gas Booster Compressor suction (PKG-049) |

Source: DBM-Deepcut SEC-05.

## Standards

- API 11P (or equivalent) for reciprocating compressor packaging — ASSUMPTION: applicable industry convention; location TBD (not explicitly stated for PKG-048 in accessed source slices; sales gas booster DBM section cites API-11P for vane-demister sizing).
- NEMA MG 1 for electric motor testing/labeling — ASSUMPTION applicable; explicitly cited for sales gas booster motor in DBM-Deepcut SEC-05 and for 03-25 inlet compressor motor in DBM-Comp_and_Liquids SEC-05; location TBD for PKG-048.
- IEC / CSA area classification, fire/gas codes, provincial pressure-equipment codes (Alberta/BC) — TBD: not explicitly extracted in accessed slices.
- Project specifications and standards as listed in 26020-Package_Requirements.docx (heading 3) — location TBD; not read as text in this run.

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 Configuration | Vendor data sheet review; PFD/P&ID review against DBM-Deepcut SEC-05. |
| R-2 Sizing | Compressor performance run verification at 120% case. |
| R-3 Inlet service conditions | Performance test or simulation at stated suction/discharge; cylinder selection review. |
| R-4 Sales service conditions | Two-stage performance run; second-stage discharge resolved against 1,500 psig vs 1,700 psig — see Guidance CT-2. |
| R-5 Frame and driver | Vendor frame selection ruling; motor data sheet; conflict resolution recorded (CT-3, CT-1). |
| R-6 Suction pressure control | Valve data sheet review; functional test of fail position. |
| R-7 Suction scrubbers | Sizing calculation review; K-factor and density assumptions verified. |
| R-8 Air cooler | Thermal performance test at winter/summer outlet temperatures; pressure drop measured vs design TBD-to-be-set. |
| R-9 Blowdown/recycle | Valve data sheet and fail-position confirmation; recycle capacity verification (CT-4). |
| R-10 Start/purge/drains/lube | FAT functional checks; seal-pot routing inspection. |
| R-11 Clearance pockets | Detailed-engineering selection memo; vendor confirmation. |
| R-12 Sparing | EPC verification that no spare items are in BOM. |
| R-13 Interfaces | EPC integration drawings (P&ID, electrical SLDs, area classification, structural). |
| R-14 Boundaries | Boundary verification on the integrated process flow diagram. |

## Documentation

Required artifacts for this deliverable (per _CONTEXT.md Anticipated Artifacts and DELIVERABLE_REGISTER.csv):
- Package scope of work (this Specification and Guidance set).
- Tagged equipment and package identity list (Datasheet "Identification" and "Attributes").
- Package function and integration narrative (Guidance, Sections "Purpose" and "Principles").
- Responsibility assignment record (this Specification, Section "Responsibility Assignment").

## Responsibility Assignment

| Activity | Owner | Source |
|---|---|---|
| Package engineering and design | Package Vendor | PACKAGE_REGISTER.csv Responsibility |
| Vendor documentation | Package Vendor | PACKAGE_REGISTER.csv Responsibility |
| Physical equipment supply | Package Vendor | PACKAGE_REGISTER.csv Responsibility |
| Facility integration (interfaces, tie-ins, constructability) | EPC Integrator | PACKAGE_REGISTER.csv Responsibility |
| Procurement and construction coordination | EPC Integrator | PACKAGE_REGISTER.csv Responsibility |
| Facility-level commissioning | EPC Integrator | ASSUMPTION (consistent with EPC Integrator scope; not explicit in accessed slices) |
| Acceptance of conflicting basis items (frame, hp rating, start method) | Owner / Project decision authority | TBD (no authority designated in accessed source slices) |
