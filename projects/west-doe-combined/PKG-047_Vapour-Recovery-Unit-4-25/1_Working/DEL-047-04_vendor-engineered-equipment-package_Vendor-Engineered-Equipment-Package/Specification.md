# Specification — DEL-047-04 Vendor Engineered Equipment Package (VRU 4-25)

## Scope

### In Scope

This specification governs the Package Vendor production unit for the West Doe Deepcut (04-25) Vapour Recovery Unit, PKG-047. It covers:

- Vendor engineering and design of two (2) 100% capacity VRU compressor trains in lead-lag configuration for sour service. (Source: PACKAGE_REGISTER.csv PKG-047 summary; location in 26020-Package_Requirements.docx TBD.)
- Fabrication and supply of the physical equipment package developed from the EPC Scope of Work (DEL-047-01) and Package Datasheet (DEL-047-02). (Source: DELIVERABLE_REGISTER.csv DEL-047-04.)
- Vendor package design basis and datasheet set for the equipment. (Source: DELIVERABLE_REGISTER.csv DEL-047-04 anticipated artifacts.)
- All package mechanical, process, electrical, instrumentation, and structural elements internal to the package boundary, including: rotary vane compressors (Ro-Flo 17S/217M), 4,000 V VFD motor drivers, two-phase suction scrubbers (one per stage), air-cooled intercooler and aftercooler with warm-air recirculation louvers, capacity-control recycle valve, make-up/blanket gas regulator, package blowdown valves, dual mechanical pressurized barrier seal system with barrier-fluid alarm, manual sweet-gas purge connection, and package controls/PLC. (Source: DBM 4-25, VRU sections.)

### Out of Scope

- Facility-level integration into the West Doe Deepcut 04-25 plant — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration are owned by the EPC Integrator (Source: PACKAGE_REGISTER.csv PKG-047 responsibility text.)
- Construction and installation are part of DEL-047-03 Construction Work Package (Source: DELIVERABLE_REGISTER.csv).
- Vendor document register, submittals, and turnover records are DEL-047-05 (Source: DELIVERABLE_REGISTER.csv).
- EPC review and acceptance of the package is DEL-047-06 (Source: DELIVERABLE_REGISTER.csv).
- 03-25 VRU and 03-25 compressor station scope (Source: DBM 4-25 — 03-25 VRU listed separately with TBD parameters).

## Requirements

### Configuration

| ID | Requirement | Source |
|---|---|---|
| REQ-1 | Provide two (2) 100% capacity VRU trains in lead-lag arrangement; second normally in standby at design conditions. | DBM 4-25, VRU Configuration |
| REQ-2 | Both trains shall be housed (per the package scope summary, in one building). CONFLICT with DBM ("each VRU installed in an individual building"); see Guidance Conflict Table. | PACKAGE_REGISTER.csv; DBM 4-25 |
| REQ-3 | Each compressor shall be a Ro-Flo 17S/217M two-stage positive-displacement rotary vane unit. | DBM 4-25; PACKAGE_REGISTER.csv |
| REQ-4 | Each train shall be driven by a 4,000 V, 3-phase VFD motor at 200 hp (per package summary). ASSUMPTION pending resolution of 200 hp vs 300 hp conflict noted in DBM. | PACKAGE_REGISTER.csv; DBM 4-25 |
| REQ-5 | Capacity control shall use speed control plus an automated recycle valve from second-stage discharge to first-stage suction sized for 100% flow at minimum driver speed and lowest operating discharge pressure. | DBM 4-25 |
| REQ-6 | Driver speed range 310–760 rpm (TBC); inverter-duty driver turndown 3:1. | DBM 4-25 |
| REQ-7 | Mechanical seal shall be dual mechanical pressurized barrier seal with barrier-fluid alarm; primary seal vent routed to LP flare. | DBM 4-25 |

### Process Design

| ID | Requirement | Source |
|---|---|---|
| REQ-8 | Design suction pressure: 0.9 kPag (2 oz/in2) at VRU inlet flange. | DBM 4-25 |
| REQ-9 | Design discharge pressure: 483 kPag (70 psig). | DBM 4-25 |
| REQ-10 | Per-train design capacity: 1.5 MMSCFD / 42 e3m3/d (TBC). | DBM 4-25 |
| REQ-11 | Minimum MAWP: 1st-stage discharge 552 kPag; 2nd-stage discharge 1,034 kPag. Suction MAWPs TBC; design temperatures TBC. | DBM 4-25 |
| REQ-12 | Two-phase suction scrubber upstream of each compression stage; mist pad internals (no mesh/vane); sizing K-factor 0.25 max (Imperial) plus operating-pressure de-rating. | DBM 4-25 |
| REQ-13 | Suction scrubber inlet liquid density assumption ≥ 0.61 SG (to be reviewed). | DBM 4-25 |
| REQ-14 | Suction scrubber gas capacity shall consider off-design operation including low compression ratio, high package capacity, high suction pressure, and low discharge pressure during initial startup. | DBM 4-25 |
| REQ-15 | First-stage intercooler design shall account for hydrocarbon condensation (cooler discharge 48.9 °C < dewpoint 52.7 °C). | DBM 4-25 |
| REQ-16 | Coolers shall include manual warm-air recirculation louvers as the base design; automatic warm-air recirculation shall be considered. No bundle temperature control provision. | DBM 4-25 |
| REQ-17 | Sour service: design composition includes H2S 0.3557 mol%, mercaptans, disulphides, CS2; materials and seals shall be sour-service compatible. | DBM 4-25, VRU Inlet Composition |

### Controls, Safeguards, and Interfaces

| ID | Requirement | Source |
|---|---|---|
| REQ-18 | Implement inlet-pressure setpoint actions: 1 oz shutdown; 2 oz make-up fuel gas control and design suction; 2.5 oz shut down second VRU; 3 oz VRU control; 5 oz start second VRU; 8 oz open suction to flare; 16 oz thief hatch. | DBM 4-25, VRU inlet pressure table |
| REQ-19 | Make-up/blanket gas regulator at suction shall maintain minimum suction pressure at maximum turndown and shall be supplied from the LP fuel gas system. | DBM 4-25 |
| REQ-20 | Package blowdown valves shall route to the LP flare under compressor unit control-panel control. | DBM 4-25 |
| REQ-21 | Manual sweet-gas purge connection shall be provided at first-stage suction immediately downstream of the inlet manual isolation valve for maintenance isolation. | DBM 4-25 |
| REQ-22 | Glycol still vapours and stripping gas (after upstream water condensation), water/C5+ storage tank vapours, and BTEX-bearing stripping gas shall be recoverable through the package and discharged to stabilizer overheads compressor first-stage suction. Recovered liquids route to produced water tanks. | DBM 4-25, VRU Scrubbing/Cooling/Blowdown/Controls; Interfaces section |
| REQ-23 | Package shall accommodate the applicable interface types listed for PKG-047 (Process/Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas; Maintenance Access; Structural/Foundations/Supports). | PACKAGE_REGISTER.csv PKG-047 |

## Standards

The following are mentioned or implicit in available sources; clause-level requirements TBD pending access to the vendor RFQ and Package Requirements document.

| Standard / Code | Applicability | Location |
|---|---|---|
| Owner/EPC project specifications (ref. 26020 series) | All package engineering | location TBD (26020-Package_Requirements.docx, 26020-01-PT-RFQ-12-002_VRU_2_R0.docx not locally accessible) |
| Sour-service materials standards (e.g., NACE/ISO MR0175) | Wetted parts in H2S service | ASSUMPTION based on sour composition in DBM 4-25; location TBD |
| Canadian electrical and area-classification standards applicable to BC oil and gas facilities | 4,000 V motor and package electrical | ASSUMPTION (Canadian site, LSD 04-25-80-15W6); location TBD |
| Pressure equipment / piping codes governing 552 kPag / 1,034 kPag MAWP equipment in BC | Pressure boundary | ASSUMPTION; location TBD |

## Verification

| Verification | Method | Linked Requirements | Source |
|---|---|---|---|
| Capacity demonstration | Performance test at design suction 0.9 kPag, discharge 483 kPag, 1.5 MMSCFD per train (TBC) | REQ-8, REQ-9, REQ-10 | DBM 4-25 |
| Hydrostatic / pressure test of pressure-containing components | Per applicable pressure code; MAWP values per REQ-11 | REQ-11 | ASSUMPTION; standards location TBD |
| Recycle valve sizing demonstration | Functional test at minimum driver speed and lowest operating discharge pressure | REQ-5 | DBM 4-25 |
| Seal integrity | Barrier-fluid system functional test; alarm proving | REQ-7 | DBM 4-25 |
| Setpoint action logic | Functional test of inlet-pressure action setpoints against REQ-18 | REQ-18 | DBM 4-25 |
| Materials sour-service certification | Vendor MTRs and conformance to applicable sour-service standard | REQ-17 | ASSUMPTION; standard location TBD |
| Intercooler condensation handling | Verify scrubber capacity and drain provisions at condensing first-stage outlet | REQ-12, REQ-14, REQ-15 | DBM 4-25 |
| Driver/VFD turndown | Demonstrate 3:1 turndown on inverter duty over 310–760 rpm | REQ-6 | DBM 4-25 (speed range TBC) |
| Blowdown routing | Witness blowdown valve operation and verify LP flare routing | REQ-20 | DBM 4-25 |
| Interface conformance | Walk-down against PKG-047 applicable interface types | REQ-23 | PACKAGE_REGISTER.csv |

## Documentation

Required vendor-produced artifacts for this deliverable (the artifacts physically delivered or accompanying the equipment):

- Vendor engineered physical equipment package (the equipment itself). (Source: DELIVERABLE_REGISTER.csv DEL-047-04 anticipated artifacts.)
- Vendor package design basis and datasheet set. (Source: DELIVERABLE_REGISTER.csv DEL-047-04 anticipated artifacts.)

Vendor document submittals (drawings, calculations, test reports, manuals, certificates) are the subject of DEL-047-05 Vendor Document Turnover Package and are not produced as primary artifacts of this deliverable. EPC review/acceptance is DEL-047-06. (Source: DELIVERABLE_REGISTER.csv.)
