# Specification: DEL-046-04 — Vendor Engineered Equipment Package (Acid Gas Compressors)

## Scope

### In Scope
- Package Vendor engineering, design, fabrication/supply, factory acceptance, and delivery of the physical Acid Gas Injection (AGI) compressor packages for PKG-046 (tag basis 26020-01-PT-12-001). (_CONTEXT.md; PACKAGE_REGISTER row PKG-046)
- Package process, mechanical, piping, instrumentation, electrical, structural, and HVAC engineering internal to the package skid/building boundary. (PACKAGE_REGISTER row PKG-046 "Applicable interface types" enumeration; ASSUMPTION that internal-to-package scope follows standard vendor package practice)
- Vendor package design basis and datasheet set including the package-vendor datasheet for each major component (compressor, driver, scrubbers, air coolers, recycle valves, blowdown valve, seal pot, lube/auxiliary systems). (_CONTEXT.md anticipated artifacts; ASSUMPTION on per-component datasheet scope)
- Acid gas compressor configuration per Acid Gas Composition Basis and MAWP/temperature schedule in Datasheet.md. (DBM-Deepcut SEC-05)
- Cascading scrubber liquid handling and stage-1 produced-water Hydra-Cell pump within the package boundary. (DBM-Deepcut SEC-05)
- Package-internal controls per §Controls and Protection Basis (DBM-Deepcut SEC-05): automated sequencing (isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, shutdown), recycle controls, blowdown control, air-cooler louver control and warm-air recirculation, seal-pot vapour recovery routing.
- Methanol injection provisions on the AGI compressor package (capacities TBC). (DBM-Deepcut Hydrate-Inhibition table)

### Excluded
- Facility-level integration (interfaces, tie-ins, constructability, procurement/construction coordination): EPC Integrator scope per PACKAGE_REGISTER row PKG-046.
- Acid gas disposal pipeline and well design (existing 02-25 disposal well/reservoir; pipeline/well design responsibility excluded unless explicitly modified by the DBM). (DBM-Deepcut §Acid Gas Disposal Well Interface; DBM-Deepcut §System Boundaries)
- Definition of disposal well pressure characteristics (provided by Tourmaline or its third party). (DBM-Deepcut §Acid Gas Disposal Well Interface)
- Acid gas injection pipeline sizing and hydraulics (3 in. NPS assumed by Tourmaline, final sizing reviewed during detailed engineering). (DBM-Deepcut)
- Package-specific exclusions beyond those captured here: TBD (PACKAGE_REGISTER row PKG-046 records "TBD; no package-specific exclusions stated in source materials").

## Requirements

### R-PKG-046-04-001 — Configuration
Two (2) x 100% acid gas compressor packages plus one (1) spare compressor shall be supplied. The possible three (3) x 50% alternative arrangement is not confirmed design basis. (DBM-Deepcut SEC-05 §Acid Gas Compressor Design Conditions; Conflict Table item C-1)

### R-PKG-046-04-002 — Compressor Type and Stages
Each compressor shall be a separable reciprocating machine of five (5) stages, Ariel KBT/6 detailed basis. The KBK/6 reference is conflicting (Conflict Table C-2). (DBM-Deepcut SEC-05)

### R-PKG-046-04-003 — Driver
Each compressor shall be driven by an 8-pole induction motor, 969 kW (1,300 hp) with approximately 10% excess power, operating at 900 rpm full speed on a VFD with minimum 3:1 inverter turndown. (DBM-Deepcut SEC-05)

### R-PKG-046-04-004 — Capacity Control
Capacity control shall be by driver speed control and recycle control. Adjustable volume pockets shall be excluded from the cylinders. (DBM-Deepcut SEC-05)

### R-PKG-046-04-005 — Acid Gas Composition Cases
The package shall be designed for the Design, Start-up, and High-CO2 composition cases tabulated in Datasheet.md (DBM-Deepcut SEC-05 §Acid Gas Composition Basis). Minimum methane content for design is 0.5 mol%; turndown cases may produce approximately 1.4 mol% C1. The Dry-out case is TBC.

### R-PKG-046-04-006 — Flow Basis
- Design total flow: 4.209 MMSCFD; design unit flow: 4.5 MMSCFD preliminary, target 1.10 capacity at design.
- Start-up total flow: 0.603 MMSCFD; start-up unit flow: 1.5 MMSCFD.
(DBM-Deepcut SEC-05)

### R-PKG-046-04-007 — Pressure Basis
- 1st-stage suction: 3.8 psig low; 7 psig normal/expander/J-T modes.
- 5th-stage discharge: 1,200 psig normal/expander/J-T modes; 1,500 psig design-discharge reference (unresolved — Conflict Table C-3).
(DBM-Deepcut SEC-05)

### R-PKG-046-04-008 — Per-Stage MAWP and Design Temperature
Each stage shall be designed at not less than the MAWP and not less than the design temperature in Datasheet.md "MAWP / Design Temperature" schedule. (DBM-Deepcut SEC-05)

### R-PKG-046-04-009 — Aftercoolers
A common forced-draft motor-driven air cooler shall be provided per stage discharge.
- Stages 1-4 cooler outlet: 110 deg F (43.33 deg C).
- Stage 5 cooler outlet: 150 deg F (65.56 deg C); to injection pipeline shall be controlled to 8.3 deg C above maximum ambient at all times.
Each bundle shall include actuated louver temperature control, automatic warm-air recirculation on low discharge temperature, and heat-medium heating for freeze protection. (DBM-Deepcut SEC-05 / §Controls and Protection Basis)

### R-PKG-046-04-010 — Suction Scrubbers
Two-phase suction scrubbers shall be provided upstream of each compression stage. Scrubber sizing shall consider off-design conditions including low compression ratio, high package capacity, and start-up cases with high suction and low discharge pressure (capacity range TBC). Inlet liquid SG = 1.00 assumed. Maximum K factor = 0.55 Imperial. Horizontal double-hook vane demisters are acceptable. All scrubbers shall include PID liquid-level control. Except for stage 1, scrubber liquids cascade to the prior-stage scrubber. Stage 1 scrubber liquid shall be pumped to the produced water tank by a 0.75 hp motor-driven Hydra-Cell pump. (DBM-Deepcut SEC-05)

### R-PKG-046-04-011 — Blowdown Valve
A single fail-open blowdown valve shall be provided on the final discharge downstream of the aftercooler. (DBM-Deepcut SEC-05 / §Controls and Protection Basis)

### R-PKG-046-04-012 — Recycle System
High-pressure recycle: final discharge to 4th-stage suction upstream of the 4th-stage suction scrubber. Low-pressure recycle: 4th-stage suction to 1st-stage suction upstream of the 1st-stage suction scrubber. Recycle valves shall be sized for 100% capacity at minimum driver speed, maximum suction pressure, and minimum injection pipeline pressure, and shall fail open. Manual isolation of recycle valves shall be excluded. (DBM-Deepcut SEC-05)

### R-PKG-046-04-013 — Sweet-Gas Purge
A manual sweet-gas purge connection shall be included at 1st-stage suction downstream of the inlet shutdown valve to remove H2S before maintenance. (DBM-Deepcut SEC-05)

### R-PKG-046-04-014 — Packing Drains/Vents
Packing drains and vents shall be collected to a common seal pot; seal-pot vapour shall route to the VRU suction header; liquids shall be removed by local truck-out connection. (DBM-Deepcut SEC-05)

### R-PKG-046-04-015 — Automated Sequencing
The package shall automate isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, and shutdown. Start-up from equalization pressure with 3:1 turndown VFD and cascading recycle; additional automated bypass is unlikely. (DBM-Deepcut SEC-05 / §Controls and Protection Basis)

### R-PKG-046-04-016 — Disposal Metering
The vendor package shall provide a high-pressure Coriolis mass meter downstream of compression and a continuous acid gas composition measurement for sulfur and CO2 balance reporting. (DBM-Deepcut SEC-05)

### R-PKG-046-04-017 — Lubrication
Lubrication oil injected into compressor valves and cylinders shall be a consumable injected into the disposal well; vendor shall declare consumption rates. (DBM-Deepcut §Acid Gas Disposal Well Interface; ASSUMPTION on declaration requirement)

### R-PKG-046-04-018 — Methanol Injection
The AGI compressor package shall include methanol injection provisions; design capacities TBC. (DBM-Deepcut Hydrate-Inhibition table)

### R-PKG-046-04-019 — Sour Service Materials
Materials of construction shall comply with sour service requirements per NACE MR0175 / ISO 15156 for the H2S composition basis. (ASSUMPTION: standard industry practice for the H2S levels in the composition basis; explicit standard reference not located in DBM source slice — location TBD)

### R-PKG-046-04-020 — Ambient Envelope
The package shall be designed for an ambient temperature range of -40 deg C to +35 deg C unless a package-specific basis is stricter. (DBM-Comp_and_Liquids site basis; applied here by ASSUMPTION as facility-wide envelope)

### R-PKG-046-04-021 — Applicable Interface Types (Package Boundary)
The vendor package shall provide and document interfaces to facility scope for: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. (PACKAGE_REGISTER row PKG-046 "InterfaceTypes")

## Standards

| Standard | Use | Location/Status |
|---|---|---|
| NACE MR0175 / ISO 15156 | Sour service materials | Edition/clause: location TBD (ASSUMPTION) |
| API 618 | Reciprocating compressors for petroleum/chemical/gas industry services | Applicability: ASSUMPTION (standard industry practice); not explicitly cited in DBM source slice — location TBD |
| API 11P / API 618 packaging | Packaging requirements | ASSUMPTION; location TBD |
| CSA Z662 | Oil & gas pipeline systems (interfacing piping classes) | ASSUMPTION; location TBD |
| Provincial/CSA electrical codes | Hazardous area classification | TBD |
| 26020-Package_Requirements.docx package heading 1 | Project package requirements (overarching) | Source present (binary) at _Sources; clause-level content TBD until text-readable extract is available |

## Verification

| Requirement | Verification approach | Records |
|---|---|---|
| R-...-001 Configuration | Vendor design submittal review; FAT count and tag list | Reviewed P&ID, equipment list |
| R-...-002 Type/Stages | Vendor proposal review; OEM model confirmation; pulsation study report | Confirmed model, study report |
| R-...-003 Driver | Motor and VFD datasheets; factory test certificate; performance curve | Datasheets, FAT certificate |
| R-...-004 Capacity Control | Control narrative review; FAT recycle test | Control narrative, FAT log |
| R-...-005 Composition cases | Process simulation/heat-and-material balance with all cases | HMB, performance curves |
| R-...-006 Flow basis | Performance test at design and start-up flow per FAT | FAT performance report |
| R-...-007 Pressure basis | Pressure test (hydrotest) per code; performance test | Hydrotest cert, FAT report |
| R-...-008 Per-stage MAWP/temp | Vendor U-1A or equivalent code data report per pressure vessel | Code data reports |
| R-...-009 Aftercoolers | Cooler thermal performance test; cold-weather operability simulation | Cooler test cert, control narrative |
| R-...-010 Scrubbers | Vendor scrubber sizing report; vessel datasheets; level control loop test | Sizing report, datasheets |
| R-...-011 Blowdown valve | Valve datasheet and fail-action stroke test | Datasheet, stroke test |
| R-...-012 Recycle | Valve sizing report; FAT recycle operation | Sizing report, FAT |
| R-...-013 Sweet-gas purge | Package P&ID review | P&ID |
| R-...-014 Seal pot | Seal pot datasheet; vent routing P&ID review | Datasheet, P&ID |
| R-...-015 Automated sequencing | Control narrative + FAT sequence demonstration | Control narrative, FAT script |
| R-...-016 Disposal metering | Meter datasheet; calibration certificate; analyzer datasheet | Meter cert, analyzer datasheet |
| R-...-017 Lubrication | Lube system datasheet; consumption rate declaration | Lube datasheet |
| R-...-018 Methanol injection | P&ID review; injection point capacity confirmation (TBC at detailed engineering) | P&ID, capacity calc |
| R-...-019 Sour service | Material test reports per NACE MR0175; PMI records | MTRs, PMI |
| R-...-020 Ambient envelope | Cold-temperature design review; winterization assessment | Design review record |
| R-...-021 Interfaces | Interface list reconciliation against facility interface register | Interface reconciliation report |

## Documentation

Required artifacts (anticipated; final list per EPC Integrator vendor documentation requirement):

- Vendor engineered physical equipment package (the package itself). (_CONTEXT.md)
- Vendor package design basis. (_CONTEXT.md)
- Vendor package datasheet set (compressor, driver, scrubbers, air coolers, recycle valves, blowdown, seal pot, lube/auxiliary, meter, analyzer). (ASSUMPTION on enumeration; _CONTEXT.md anticipates the set)
- P&IDs, equipment list, instrument index, cause-and-effect / control narrative.
- Pulsation/mechanical study (API 618 Design Approach Level: TBD).
- Hazardous area classification drawings (TBD).
- Inspection and Test Plan (ITP), FAT procedure and report.
- Vendor Document Turnover Package (handed to DEL-046-05; not produced under this deliverable).
- Conflict resolutions for items C-1 through C-3 in Guidance.md Conflict Table.
