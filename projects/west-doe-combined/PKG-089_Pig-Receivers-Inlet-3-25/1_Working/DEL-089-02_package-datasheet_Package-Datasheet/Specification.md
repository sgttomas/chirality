# Specification — DEL-089-02 Package Datasheet

> Normative requirements that the Package Vendor and EPC Integrator must satisfy to produce a vendor-engineered Pig Receivers (Inlet) 3-25 package consistent with the package source basis. Each requirement is anchored to a source. Inferences are labelled `ASSUMPTION`; unresolved items are `TBD`. Cross-source conflicts impacting requirement direction are flagged and resolved via the Conflict Table in `Guidance.md`.

## Scope

### In Scope

`FACT` (SOW-0157, SOW-0158, SOW-0159):
- Vendor engineering, design, and supply of two (2) Pig Receiver assemblies (610 mm / 24 in OD) for the 03-25 plant inlet, each on a dedicated structural-steel, non-enclosed skid (subject to CFT-01 ruling — see Guidance Conflict Table).
- Inlet ESDVs (full-port, piggable, with position transmitters), skid isolation/ESDV valves, sweet-gas purge provision, HP flare vent connection.
- Vendor package design basis, datasheet set, and vendor documentation supporting the EPC Integrator's facility-integration review.

### Out of Scope (By Others per SOW-0160)

- Interconnecting piping between the package and facility process systems.
- DCS integration (signal wiring/configuration to facility DCS).
- Foundations.
- Electrical supply to the MCC.
- Plant inlet pipeline upstream of the first aboveground flange (Doe field pipeline contractor).

## Requirements

### REQ-1 — Receiver Configuration

`FACT` Source: SOW-0158, SOW-0159
- REQ-1.1: Two pig receivers shall be supplied, tagged `PR-1010-2` and `PR-1020-2`. *(Open: CFT-01 — DBM states "single combined three-phase pig receiver". Authority `PROPOSAL`: SOW-0158/0159.)*
- REQ-1.2: Each receiver shall have an outside diameter of 610 mm (24 in).
- REQ-1.3: Each receiver shall be mounted on a dedicated structural-steel, non-enclosed skid.
- REQ-1.4: Barrel length, internal diameter, and pig-handling volume are `TBD` (DBM "Pig receiver size is TBD") and shall be specified by the Package Vendor based on pipeline pig size, sphere/cup pig type, and operator preference.

### REQ-2 — Isolation and Safety Valves

`FACT` Source: SOW-0159; DBM §Inlet Pipeline Interface and Pigging
- REQ-2.1: An ESDV shall be installed upstream of each receiver.
- REQ-2.2: The inlet ESDV shall be full-port, piggable, and shall include position transmitters.
- REQ-2.3: All skid-mounted block valves shall be either manual isolation valves or ESDVs per the package P&ID (P&IDs `TBD` until Package Vendor scope).
- REQ-2.4: Delivery-point ESDV shutdown pressure is `TBC` (DBM). Inlet-separator ESDV shutdown pressure is 635 psig (DBM); the receiver skid shall not impose a more restrictive shutdown pressure without EPC ruling.

### REQ-3 — Purge and Vent

`FACT` Source: SOW-0159; DBM
- REQ-3.1: A sweet-gas purge connection shall be provided downstream of a manual isolation valve to purge the receiver barrel of sour gas prior to opening for pig retrieval.
- REQ-3.2: A vent line shall be routed to the facility HP flare system. Sizing/relief basis to be coordinated with the HP flare interface (IFC-8FDDF0DF74).

### REQ-4 — Process Conditions and Pressure Envelope

`FACT` Source: SOW-0160
- REQ-4.1: Design throughput shall be 80 MMSCFD at the package level. (`ASSUMPTION`: 40 MMSCFD per receiver, mirroring the two-train inlet-separator basis in DBM §Inlet Separation.)
- REQ-4.2: Normal operating pressure range: 125–200 psig.
- REQ-4.3: MAOP: 572 psig.
- REQ-4.4: Design pressures: 125 psig (low); 200 psig (normal high); MAWP 635 psig.
- REQ-4.5: Normal flowrate per receiver: `TBC` (operator/pipeline-side input required).

### REQ-5 — Ambient and Service Conditions

`FACT` Source: SOW-0160; DBM
- REQ-5.1: Ambient design temperature: −40 °C minimum to +35 °C maximum.
- REQ-5.2: Historical ambient envelope: −19 °C min to +22.2 °C max.
- REQ-5.3: Service classification: sour gas (variable composition per DBM); package shall be designed for sour service.
- REQ-5.4: Sour-service H2S basis applied to materials selection: SOW-0159 states 0.1 mol%; DBM raw-gas design states 0.3 mol% with 2.0 mol% license value. Governing value is `TBD` pending CFT-02 ruling. Until ruled, **Package Vendor shall design to the most restrictive (DBM license 2.0 mol%) for materials selection** as `ASSUMPTION` to avoid downstream rework.

### REQ-6 — Codes and Standards

`ASSUMPTION` (not explicitly enumerated for this package in the accessible source slices; package heading 42 in `26020-Package_Requirements.docx` may enumerate further — `location TBD`):
- REQ-6.1: Pressure boundary design shall comply with ASME B31.3 (Process Piping) and ASME BPVC Section VIII for pressure vessels, as applicable to receiver geometry.
- REQ-6.2: Sour-service materials shall comply with NACE MR0175 / ISO 15156 based on governing H2S partial pressure (subject to CFT-02 ruling).
- REQ-6.3: Welding, NDE, PWHT shall meet the project Welding Specification (`TBD`, EPC Integrator to issue).
- REQ-6.4: All standards above are `ASSUMPTION` until confirmed against the package requirements document slice or the EPC project specifications.

### REQ-7 — Interfaces

`FACT` Source: INTERFACE_REGISTER (10 PKG-089 rows). Each interface below shall have a documented interface deliverable between the Package Vendor and EPC Integrator. Each row is also a Mechanical-package interface marked YES in the workbook.

| Req | Interface | Register ID | Direction / Note |
|---|---|---|---|
| REQ-7.1 | Process Piping (inlet pipeline tie-in, outlet to inlet separator) | IFC-1AA715D034 | By Others; flange ratings/types `TBD` |
| REQ-7.2 | Relief / Flare / Vent (HP flare) | IFC-8FDDF0DF74 | Package supplies tail-pipe; common flare header by EPC |
| REQ-7.3 | Drain / Containment | IFC-9289961CBA | Closed/open drain routing `TBD` |
| REQ-7.4 | Electrical Power (to MCC) | IFC-2BEB4D0C0C | By Others to MCC; loads & cable schedule from Vendor |
| REQ-7.5 | EHT | IFC-9EA22696F8 | Heat-trace strategy `TBD`; tied to ambient envelope and dewpoint |
| REQ-7.6 | I&C / Control Cabling | IFC-6646B13FC8 | DCS integration by Others; junction-box and tag list by Vendor |
| REQ-7.7 | Maintenance Access | IFC-73B5712650 | Pig retrieval, valve maintenance access; clearances `TBD` |
| REQ-7.8 | Grading / Site Drainage / Spill Containment | IFC-E553602F11 | Civil scope; spill containment for sour-condensate carry-over |
| REQ-7.9 | Structural / Foundations / Supports | IFC-7BEBBC1154 | Foundations by Others; skid anchor and load schedule from Vendor |
| REQ-7.10 | Pipeline / Pigging | IFC-C734FF9F3E | Pig type/size & launch frequency `TBC`; pipeline-side coordination |

### REQ-8 — Boundaries

`FACT` Source: DBM §Inlet Pipeline Interface and Pigging; SOW-0160
- REQ-8.1: The plant inlet boundary is the first aboveground flange within the lease boundary. The pig receiver inlet pipeline tie-in flange is the scope-transfer flange.
- REQ-8.2: The receiver outlet boundary is the connection to facility process piping that conveys gas to inlet separators V-1600-2 / V-1700-2; sizing of this segment is by Others (REQ-7.1).

### REQ-9 — Documentation Submittals

`ASSUMPTION` (typical vendor document set; specific list to be governed by `DEL-089-05_vendor-document-turnover-package`):
- Mechanical package datasheet(s) per receiver and ESDV.
- P&IDs at vendor-package level.
- General Arrangement and skid layout drawings.
- Stress, lifting, anchor-load, and skid structural calculations.
- Materials test reports / MTRs for pressure-containing components.
- Hydrotest and NDE reports.
- IOM (installation, operation, maintenance) manual.
- O&M spares list and recommended commissioning spares.

## Standards

| Standard | Applicability | Status |
|---|---|---|
| ASME B31.3 — Process Piping | Process piping on receiver skids | `ASSUMPTION` — typical; confirm against package source slice |
| ASME BPVC Section VIII Div. 1 | Pressure receiver vessels | `ASSUMPTION` — typical; confirm geometry treatment |
| NACE MR0175 / ISO 15156 | Sour-service materials | `ASSUMPTION` — applicability triggered by sour service; partial pressure basis subject to CFT-02 |
| CSA Z662 (Oil & Gas Pipeline Systems) | Plant inlet boundary segments crossing pipeline scope | `ASSUMPTION` — typical for BC pipeline facilities; `location TBD` in source |
| Provincial regulator (BCER) requirements | Sour-service operating permit | `ASSUMPTION` — applicability; clause-level `TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-1, REQ-3, REQ-7 | Design review (P&ID, GA, skid drawing) against this Specification and the Package Datasheet |
| REQ-2, REQ-3.2 | FAT / function test of ESDVs, position transmitters, purge and vent isolation |
| REQ-4 (pressure envelope) | Hydrostatic test at 1.5 × MAWP per ASME; pressure-test certificate |
| REQ-5.3, REQ-5.4 | Material certifications (MTRs); NACE compliance certification |
| REQ-6 | Code-compliance package (ASME stamping, B31.3 weld records, NDE reports) |
| REQ-7 (interfaces) | Interface-control documents signed by Vendor and EPC Integrator |
| REQ-8 | Walkdown at site against P&ID / GA at construction handoff |
| REQ-9 | Document Submittal Register reviewed under `DEL-089-05` |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):
- Package technical datasheet (this deliverable, with the vendor-completed equipment datasheets attached).
- Vendor engineering handoff basis.
- Package interface requirements matrix (REQ-7 table is the seed).
- Source-supported equipment and design-criteria summary.
