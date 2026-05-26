# Specification — DEL-050-02 Package Datasheet (Stabilizer Overheads Compressors)

## Scope

### In Scope

This specification governs the EPC Integrator-authored Package Datasheet for PKG-050 Stabilizer Overheads Compressors. It covers:

- The technical data package required for third-party vendor or discipline package engineering and design (from `_CONTEXT.md`).
- Package identity, function, configuration, equipment, performance, operating and design conditions, and the package interface requirements matrix (per `_CONTEXT.md` anticipated artifacts and `ARTIFACT_REGISTER.csv` rows ART-6803A1BA12, ART-3E88938FCE, ART-E77A969E05, ART-15F17CEA07 and interface-fact rows).
- The package interface inventory carried as datasheet evidence (`_CONTEXT.md` notes: "interface facts are intentionally carried here as evidence rather than standalone deliverables").

### Out of Scope

- Vendor-internal engineering, design choices, and fabrication (owned by Package Vendor per `PACKAGE_REGISTER.csv` row PKG-050 responsibility text and `DELIVERABLE_REGISTER.csv` DEL-050-04).
- Items explicitly carried by others: shipping of packages to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs (SOW-0176 — `26020-Package_Requirements.docx` heading 5, Scope notes and open items).
- Construction work-face plan (handled by DEL-050-03).
- Vendor document turnover (DEL-050-05) and EPC vendor package acceptance (DEL-050-06).

## Requirements

Numbering: `REQ-DS-<n>`. Source citation in parentheses. `ASSUMPTION:` flags inferences.

### Identification & Provenance

- **REQ-DS-01.** The Package Datasheet SHALL identify the package by PackageID (`PKG-050`), Workbook row (81), WBS (01), Package Name ("Stabilizer Overheads Compressors"), Discipline (Mechanical), and CoA tracking number (`26020-01-PT-12-005`). (`PACKAGE_REGISTER.csv` row PKG-050)
- **REQ-DS-02.** The Package Datasheet SHALL cite the EPC Scope of Work (DEL-050-01) and the Workbook/Package_Requirements source rows as its provenance. (`PACKAGE_REGISTER.csv` SourceBasis)

### Package Configuration

- **REQ-DS-10.** The package SHALL consist of two (2) identical induction motor-driven separable reciprocating compressor packages, each designed for 100% capacity. (SOW-0174)
- **REQ-DS-11.** Each compressor package SHALL be an Ariel KBC/6 four-stage separable reciprocating compressor. (SOW-0175)
- **REQ-DS-12.** Process function: the package SHALL compress and recycle multiple streams from 50 psig to 1100 psig, with final discharge routed to the amine inlet filter coalescer or recycled back to the first stage. (SOW-0174)

### Driver / Motor

- **REQ-DS-20.** The driver SHALL be an 8-pole electric induction motor rated 2700 HP @ 891 RPM with speed control, 4000 V / 3 PH / 60 Hz. (SOW-0175; SOW-0176)
- **REQ-DS-21.** Motor enclosure SHALL be quoted as TEFC; final enclosure designation is TBD per source. (SOW-0176)
- **REQ-DS-22.** Cooling fans SHALL be non-spark, bidirectional. (SOW-0176)
- **REQ-DS-23.** Motors SHALL be tested/labelled to NEMA MG 1. (SOW-0176)
- **REQ-DS-24.** Toshiba motors SHALL NOT be supplied. (SOW-0175; SOW-0176)
- **REQ-DS-25.** An automated recycle valve SHALL be provided. (SOW-0175)

### Capacity & Turndown

- **REQ-DS-30.** Design capacity per stage SHALL be: Stage 1 = 2.5 MMSCFD; Stage 2 = 5 MMSCFD; Stage 3 = 17 MMSCFD; Stage 4 = 17 MMSCFD. (SOW-0176)
- **REQ-DS-31.** Turndown ratio SHALL be 3:1. (SOW-0176)

### Operating & Design Conditions

- **REQ-DS-40.** Per-stage operating pressures SHALL meet the values tabulated in Datasheet > Operating Conditions. (SOW-0176)
- **REQ-DS-41.** Cooler discharge temperatures (Stage 1 = 65.56 C, Stage 2 = 87.78 C) SHALL be achieved by the air-cooler intercoolers; Stage 3 and Stage 4 cooler discharge temperatures are `TBD` (source text truncated as "3rd."). (SOW-0176)
- **REQ-DS-42.** Design temperatures SHALL be 149 C at each stage suction and 177 C at each stage discharge. (SOW-0176)
- **REQ-DS-43.** MAWP SHALL be at minimum 1723 kPag at the 1st-stage suction, and at minimum 9101 kPag at 177 C for the final-stage discharge. Other MAWP values are TBC per source. (SOW-0176)

### Auxiliaries / Included Equipment

- **REQ-DS-50.** A forced-air intercooler (air cooler) SHALL be provided after each stage of compression, mounted on a common frame (Ap-661 modified), with a warm-air recirculation plenum heater and non-sparking, bidirectional cooling. (SOW-0175)
- **REQ-DS-51.** First-stage scrubber SHALL be two-phase c/w cyclonic element; size and capacity by Vendor. (SOW-0175)
- **REQ-DS-52.** Second-, third-, and fourth-stage scrubbers SHALL be two-phase c/w demister; size and capacity by Vendor. (SOW-0175)
- **REQ-DS-53.** A packing vent/drain separation pot SHALL be supplied (two-phase; DP 101 kPag; size and capacity by Vendor). (SOW-0175)
- **REQ-DS-54.** A vacuum pump SHALL be supplied (size and capacity by Vendor). (SOW-0175)
- **REQ-DS-55.** A seal-pot waste-oil transfer pump SHALL be supplied (size and capacity by Vendor). (SOW-0175)

### Interface Requirements (Battery Limits)

- **REQ-DS-60.** The Package Datasheet SHALL carry the interface inventory listed in `INTERFACE_REGISTER.csv` for PKG-050 (13 interface types from Process Piping through Structural / Foundations / Supports) as the interface requirements matrix. (`INTERFACE_REGISTER.csv` PKG-050 rows; `_CONTEXT.md` note)
- **REQ-DS-61.** Tie-in points, sizes, ratings, elevations, and side-of-line responsibility for each listed interface are `TBD`; the EPC Integrator SHALL populate these prior to vendor handoff. (No source slice available in this run.)

### Exclusions Carried By Others

- **REQ-DS-70.** The following SHALL be excluded from the Package Vendor scope (carried by others): shipping packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs. (SOW-0176)

## Standards

Locally cited / inferred standards. `location TBD` indicates the source asserted the standard but the relevant clause text was not opened.

| Standard | Topic | Source / Notes |
|---|---|---|
| NEMA MG 1 | Motor testing/labelling | SOW-0176 (cited); clause-level `location TBD` |
| ASME (BPVC / B31.3) | Pressure vessels, process piping | ASSUMPTION: likely applicable given pressure envelope and MAWP values; not explicitly cited in accessible source slices |
| API 618 | Reciprocating compressors for petroleum, chemical and gas industry services | ASSUMPTION: likely applicable for separable reciprocating compressor packages; not cited in accessible source slices |
| API 11P / ISO 13631 | Packaged reciprocating compressors | ASSUMPTION: possibly applicable; not cited in accessible source slices |
| CSA / NEC area classification | Electrical area classification | `TBD` — not stated in accessible source slices |

## Verification

| Requirement(s) | Verification Approach |
|---|---|
| REQ-DS-01, REQ-DS-02 | Document review against `PACKAGE_REGISTER.csv` row PKG-050 and DEL-050-01 |
| REQ-DS-10 – REQ-DS-12 | Design review against `26020-Package_Requirements.docx` heading 5 — Basic scope |
| REQ-DS-20 – REQ-DS-25 | Motor datasheet review; NEMA MG 1 test report; supplier confirmation Toshiba excluded |
| REQ-DS-30 – REQ-DS-31 | Vendor performance curves; turndown demonstration |
| REQ-DS-40 – REQ-DS-43 | Process datasheet check; vessel/piping design pressure/temperature stamping |
| REQ-DS-50 – REQ-DS-55 | Vendor equipment list and detail datasheets |
| REQ-DS-60 – REQ-DS-61 | Interface requirements matrix completeness review against `INTERFACE_REGISTER.csv` PKG-050 rows |
| REQ-DS-70 | Vendor scope split confirmation; cross-check with DEL-050-03 Construction Work Package |

## Documentation

Anticipated artifacts produced/aggregated by this deliverable (from `_CONTEXT.md` and `ARTIFACT_REGISTER.csv` DEL-050-02 rows):

- Package technical datasheet (ART-6803A1BA12)
- Vendor engineering handoff basis (ART-3E88938FCE)
- Package interface requirements matrix (ART-E77A969E05)
- Major included equipment evidence (ART-15F17CEA07)
- Interface fact evidence rows ART-E909E5E3DD through ART-E601A41014 (13 interface types) (`ARTIFACT_REGISTER.csv`)
