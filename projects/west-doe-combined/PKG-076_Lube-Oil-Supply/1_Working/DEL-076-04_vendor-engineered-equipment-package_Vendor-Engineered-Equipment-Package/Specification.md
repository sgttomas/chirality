# Specification — Vendor Engineered Equipment Package (DEL-076-04)

> Normative requirements for the Package Vendor's engineering, design, fabrication/supply, and physical delivery of the PKG-076 Lube Oil Supply utility package, derived from the EPC package Scope of Work (DEL-076-01), the EPC Package Datasheet (DEL-076-02), and the locally accessible Design Basis Memorandum (DBM-Deepcut SEC-08 and SEC-05). Source-anchored values cite the DBM; values from `26020-Package_Requirements.docx` heading 30 are marked `location TBD`.

## Scope

### In scope
- Detailed engineering and design of the Lube Oil Supply utility package serving the 04-25 Deep Cut Gas Plant compressor frames.
- Fabrication, supply, modularization, shop assembly, and shipping of:
  - Heated compressor-cylinder lube oil storage tank (400 bbl basis) located in the storage tank area;
  - Heated compressor-crank-case lube oil storage tank (200 bbl basis) located in the storage tank area;
  - Cylinder lube oil transfer pump P-9240-1 (basis: one pump filling compressor frame day tanks as needed);
  - Crank-case lube oil transfer pump P-9250-1 (basis: one pump filling compressor frame day tanks as needed);
  - Associated heating provisions (tank heating, heat tracing), instrumentation, controls, and tie-in to the compressor frame day-tank distribution.
- Package design basis documentation, datasheets, and vendor turnover documents required to support the EPC integration review (DEL-076-06) and the Vendor Document Turnover Package (DEL-076-05).

### Out of scope
- Compressor frame day tanks (within compressor package vendor scope — DBM SEC-05 L828; analogous SEC-05 L928, L967 references "electric circulating lube oil heater" within compressor frame scope).
- Compressor manufacturer-specified cylinder oil and crank-case oil selection (TBC by compressor manufacturers per DBM SEC-08 L2072).
- Long-distance distribution piping between the storage tank area and compressor packages — interface scope **TBD** against EPC site standards and `26020-Package_Requirements.docx` h.30.
- Plant utilities upstream of the package tie-in flanges (electrical supply, heat-medium supply if used, instrument air).
- Used / waste lube oil collection and disposal infrastructure (TBD per DBM SEC-08 L2072 "additional storage requirements remain TBD").

## Requirements

### R-1 Service performance
| ID | Requirement | Source |
|---|---|---|
| R-1.1 | Package shall provide heated bulk storage and on-demand transfer of compressor cylinder lube oil and compressor crank-case lube oil to compressor frame day tanks. | DBM SEC-08 L1835, L2059–L2071 |
| R-1.2 | Tank heating shall maintain stored lube oil at a pumpable temperature suitable for transfer to compressor frame day tanks across the site ambient envelope (−40 °C to +35 °C). Specific service temperature **TBD**. | DBM SEC-02 L198; SEC-08 L1835, L2059 |
| R-1.3 | Pumps shall transfer oil "as needed" (intermittent fill duty); design shall accommodate the day-tank refill cycle of the served compressor frames. | DBM SEC-08 L2068, L2070 |
| R-1.4 | Multi-grade cylinder oil capability: package design shall not preclude future introduction of a second cylinder-oil grade (sulphur/H2S/rich-gas-driven differentiation per L2072). Whether the initial build supports a single grade or multiple grades is **TBD** pending compressor-manufacturer rulings. | DBM SEC-08 L2072 |

### R-2 Equipment configuration
| ID | Requirement | Source |
|---|---|---|
| R-2.1 | One (1) compressor cylinder lube oil storage tank, 400 bbl nominal, heated, located in the facility storage tank area. Tank design specific gravity 1.00 (TBC). | DBM SEC-08 L2065, L2067 |
| R-2.2 | One (1) compressor crank-case lube oil storage tank, 200 bbl nominal, heated, located in the facility storage tank area. Tank design specific gravity 1.00 (TBC). | DBM SEC-08 L2066, L2069 |
| R-2.3 | One (1) cylinder lube oil transfer pump, tag P-9240-1, sized to fill compressor frame day tanks as needed. | DBM SEC-08 L2068; SEC-16 L2602 |
| R-2.4 | One (1) crank-case lube oil transfer pump, tag P-9250-1, sized to fill compressor frame day tanks as needed. | DBM SEC-08 L2070; SEC-16 L2602 |
| R-2.5 | Pump type, drive, materials, mechanical seal arrangement, and capacity — **TBD** (vendor selection). Vendor shall propose pump sparing based on availability analysis; the DBM line-item basis is one pump per service. | ASSUMPTION; DBM SEC-08 L2068, L2070 |
| R-2.6 | Tanks shall be provided with heating (electric trace, jacket, or coil — method **TBD**), insulation, level indication/transmitter, high-/low-level alarms, vent, fill, drain, and sample connections. Specific configuration per vendor standard; tank tag identifiers **TBD** (not stated in DBM). | ASSUMPTION; DBM SEC-08 L2059 |
| R-2.7 | Filtration, strainers, and check valves at each pump suction and discharge per vendor standard for clean heated-oil transfer service. | ASSUMPTION (not stated in DBM) |

### R-3 Mechanical / site / environmental
| ID | Requirement | Source |
|---|---|---|
| R-3.1 | Equipment shall be suitable for site design ambient envelope −40 °C to +35 °C, including winterization, heat tracing, insulation, package buildings or enclosures, and instrumentation rated for the envelope. | DBM SEC-02 L198 |
| R-3.2 | Layout shall respect minimum spacing criteria for atmospheric storage tanks, pumps, and electrical equipment areas. | DBM SEC-02 §2.5 (L241–L308) |
| R-3.3 | Secondary containment shall be provided in accordance with site civil/environmental standards for heated hydrocarbon liquid storage; sizing basis **TBD**. | ASSUMPTION; DBM SEC-08 (not explicit) |
| R-3.4 | Area classification basis: lube oil storage and transfer is not a process hydrocarbon stream and is expected to default to General Purpose, subject to confirmation against any local sources of ignition (heaters) — **TBD**. | ASSUMPTION |

### R-4 Interfaces (tie-points the vendor must design to)
| ID | Interface | Source |
|---|---|---|
| R-4.1 | Outbound: cylinder lube oil supply pipe to compressor frame day tanks across the SOC inlet/sales compressor area, stabilizer overheads compressor area, sales gas booster compressor area, and acid gas compressor area. Routing and pipe-spec interface **TBD** against EPC layout. | DBM SEC-08 L1835; SEC-05 L828 |
| R-4.2 | Outbound: crank-case lube oil supply pipe to compressor frame day tanks across the same compressor areas. | DBM SEC-08 L1835; SEC-05 L828 |
| R-4.3 | Inbound: bulk cylinder oil and crank-case oil receiving (truck offload) at storage tank area — connection design and offload pump (if any) **TBD**. | ASSUMPTION; DBM SEC-08 L2072 (storage and transfer concept) |
| R-4.4 | Electrical: LV power to transfer pumps, tank heaters/trace, and instrumentation per facility electrical distribution. | DBM SEC-12 (Electrical Basis); detailed interface **TBD** |
| R-4.5 | Controls: integration into DCS for tank levels, pump start/stop, and high-level/low-level alarms. | DBM SEC-13 (Controls System Basis) — **location TBD** for lube-oil scope |
| R-4.6 | Civil: secondary containment, foundation, and bunding within the storage tank area. | DBM SEC-02 General Layout Basis; SEC-11 (Civil Basis) — **location TBD** for lube-oil scope |

## Standards

| Standard | Application | Location |
|---|---|---|
| API 650 | Welded atmospheric storage tanks (typical for bulk heated lube oil storage at this size) | ASSUMPTION based on DBM use of API 650 for other atmospheric tanks (e.g., SEC-16 packages list "Tanks, Caustic (API 650)" L2556, "Tanks, Condensate (API 650)" L2557); explicit API selection for lube oil tanks **location TBD** against `26020-Package_Requirements.docx` h.30 |
| ASME B&PV Section VIII | Any pressure-containing equipment if pump discharge vessels or filter housings are pressure-rated | ASSUMPTION; **location TBD** |
| BC CRN registration | Pressure equipment registration in British Columbia (only applicable items) | ASSUMPTION based on facility location (04-25 BC); `location TBD` |
| NEMA MG-1 | Electric motor compliance for transfer pump drivers (analogous to compressor-motor basis) | DBM SEC-05 L828 (analogous for compressor motors); `location TBD` for lube-oil pump motors |
| Vendor/EPC site standards | Heat tracing, winterization, electrical area classification, secondary containment | `location TBD` against `26020-Package_Requirements.docx` h.30 |

## Verification

| Requirement(s) | Verification approach |
|---|---|
| R-1.1, R-1.2, R-1.3, R-1.4 | Vendor design narrative and HMB; commissioning fill/transfer trial; service-temperature confirmation against compressor-vendor required supply conditions. |
| R-2.1 – R-2.7 | Equipment datasheet review against requirement table; vendor mechanical drawings; FAT/ITP for tanks and pumps; shop hydrotest records where applicable. |
| R-3.1 – R-3.4 | Mechanical/material spec review; cold-climate review; layout/spacing review; civil/secondary-containment review with EPC Integrator. |
| R-4.1 – R-4.6 | Interface tie-point review against EPC Package Datasheet (DEL-076-02); P&ID and layout alignment with compressor packages, electrical distribution, controls, and civil. |

## Documentation (Required Vendor Documents)

Per `_CONTEXT.md` anticipated artifacts and the Vendor Document Turnover Package scope (DEL-076-05), the vendor package shall deliver:

- Vendor package design basis and datasheet set (per major equipment item in R-2)
- Mechanical equipment drawings and module/skid general arrangements
- P&IDs covering the package boundary
- Electrical and instrumentation drawings and lists
- Cause-and-effect / safeguarding documentation for tank level controls and pump permissives
- FAT records, hydrotest reports, NDE records (as applicable)
- Operations & maintenance manuals (including oil-grade compatibility and changeout procedures)
- Spare parts and consumables lists
- Turnover documentation per DEL-076-05

`location TBD` — specific vendor document index against `26020-Package_Requirements.docx` h.30.
