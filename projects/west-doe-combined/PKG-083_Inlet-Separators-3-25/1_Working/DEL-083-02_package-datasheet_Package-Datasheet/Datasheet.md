# Datasheet — DEL-083-02 Package Datasheet (PKG-083 Inlet Separators 3-25)

Status: INITIALIZED (P1_P2 draft). Source-grounded per accessible references; unresolved values marked TBD; inferences labeled ASSUMPTION.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-083-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | PKG-083 Inlet Separators 3-25 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Workbook Row | 67 | PACKAGE_REGISTER.csv |
| WBS | 02 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv |
| Equipment Tag (representative) | 26020-02-PT-17-003 — Inlet Separators | PACKAGE_REGISTER.csv |
| Responsible Party | EPC Integrator (this datasheet); Package Vendor (equipment package engineering) | PACKAGE_REGISTER.csv |
| Source Basis Documents | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-04 "Inlet Separation"; Workbook Packages row 67; 26020-Package_Requirements.docx heading 36 (binary, location TBD); 26020-02-PT-RFQ-17-003 RFQ doc (binary, location TBD) | PACKAGE_REGISTER.csv |

## Attributes

### Package Definition

| Attribute | Value | Source |
|---|---|---|
| Package function | Supply two (2) identical horizontal three-phase separators receiving raw inlet gas from upstream pipeline pig receiver; separate into sour natural gas (vapour), sour raw condensate (light liquid), sour water (heavy liquid). | PACKAGE_REGISTER.csv `Package Description` |
| Equipment count | 2 separator packages (V-1600-2 and V-1700-2) | DBM SEC-04 "Inlet Separation" |
| Capacity basis | 2 x 50% of facility capacity; no installed spare beyond the two units | DBM SEC-04 |
| Service | Sour (process fluid contains H2S; H2S mol% TBD at separator-stream level — adjacent compressor inlet basis cites approx. 0.296 mol% H2S in DBM SEC-05 only) | DBM SEC-04/SEC-05 |

### Per-Separator Process Design Basis

Values copied verbatim from DBM-Comp_and_Liquids SEC-04 "Inlet Separation" table.

| Parameter | Value | Source |
|---|---:|---|
| Gas flow | 40 MMSCFD | DBM SEC-04 |
| Condensate flow | 556 m3/d (3,494 bbl/d) | DBM SEC-04 |
| Produced-water flow | 1,800 m3/d (11,322 bbl/d) | DBM SEC-04 |
| Diameter | 2,743 mm (9 ft) | DBM SEC-04 |
| Straight-side length | 12,191 mm (40 ft) | DBM SEC-04 |
| Pressure class | ANSI 600# | DBM SEC-04 |
| Design pressure | 4,963 kPag | DBM SEC-04 |
| Slug handling | ~38 m3 | DBM SEC-04 |
| Internal coating | Devchem 253 | DBM SEC-04 |

### Operating Conditions

| Parameter | Value | Source |
|---|---:|---|
| Low operating pressure (inlet) | 125 psig | DBM SEC-04 |
| Design operating pressure (inlet) | 200 psig | DBM SEC-04 |
| Maximum operating pressure (inlet) | 572 psig | DBM SEC-04 |
| Normal high operating pressure | TBC | DBM SEC-04 |
| Inlet design temperature | 8.3 deg C (CONFLICT — downstream excerpts disagree; reconcile in detailed design — see Guidance Conflict Table) | DBM SEC-04 |
| ESDV shutdown pressure (inlet separator) | 635 psig | DBM SEC-04 "Inlet Pipeline / Pigging" |

## Conditions (Service / Environment)

| Item | Value | Source |
|---|---|---|
| Fluid phases handled | Sour gas, sour raw condensate, sour water (three-phase) | DBM SEC-04; PACKAGE_REGISTER.csv |
| Methanol presence | Infrequent; expected to drain at inlet separator boot; downstream methanol disposition TBD | DBM SEC-03 "Produced water and waste streams" line 218 |
| Drive-gas recycle | Recycle from downstream of inlet compressor aftercoolers returns to the separators; drive-gas pressure set above 04-25 stabilizer flash-feed separator pressure | DBM SEC-04 "Flow Distribution and Controls" |
| Site / location | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15W6, north of Dawson Creek, BC; elevation 673 m | DBM SEC-02 |
| Area classification | TBD (not stated in DBM source slice) | — |
| Climatic / winterization design | Instrumentation and one end of each package enclosed in a heated self-framing building; exact building extent TBD | DBM SEC-04 |

## Construction

| Item | Value | Source |
|---|---|---|
| Orientation | Horizontal | DBM SEC-04; PACKAGE_REGISTER.csv |
| Internals | Manually adjustable weir; vertical/horizontal high-performance mesh/vane mist eliminators; de-sanding provisions | DBM SEC-04 |
| Internal coating | Devchem 253 | DBM SEC-04 |
| Piping coating | Not coated under current separator basis | DBM SEC-04 |
| Inlet pressure-control valves | At least two parallel inlet pressure-control valves per package; balanced globe hardened trim; dP limit ≤ 5 psid | DBM SEC-04 "Flow Distribution and Controls" |
| Produced-water level-control valves | At least two parallel per package | DBM SEC-04 |
| Building enclosure | Instrumentation and one end of each package enclosed in heated self-framing building; extent TBD | DBM SEC-04 |
| Skid materials of construction | TBD (not stated in source slice) | — |
| Code stamps / pressure-vessel code | TBD (not stated in DBM; expected ASME Section VIII via 26020-Package_Requirements.docx heading 36 — ASSUMPTION; verify in source doc) | — |

## Package Interfaces (carried as datasheet evidence per Gate-5 convention)

Each interface row is taken from INTERFACE_REGISTER.csv for PKG-083.

| Interface ID | Interface Type | Applicable | Source |
|---|---|---|---|
| IFC-0A3F3DB464 | Process Piping | YES | INTERFACE_REGISTER.csv |
| IFC-1087C6F97F | Utility Piping | YES | INTERFACE_REGISTER.csv |
| IFC-FA3B8A5DBC | Relief / Flare / Vent | YES | INTERFACE_REGISTER.csv |
| IFC-15DD5D35D2 | Drain / Containment | YES | INTERFACE_REGISTER.csv |
| IFC-5BF640DD30 | EHT (Electric Heat Trace) | YES | INTERFACE_REGISTER.csv |
| IFC-4C3DDE8C75 | Grounding / Bonding | YES | INTERFACE_REGISTER.csv |
| IFC-2CB7E6CE97 | Area / Exterior Lighting | YES | INTERFACE_REGISTER.csv |
| IFC-338890FE9F | I&C / Control Cabling | YES | INTERFACE_REGISTER.csv |
| IFC-6DAB319A6E | Fire & Gas / Safety Systems | YES | INTERFACE_REGISTER.csv |
| IFC-CB6BFFFFDD | Maintenance Access | YES | INTERFACE_REGISTER.csv |
| IFC-9D554F8422 | Structural / Foundations / Supports | YES | INTERFACE_REGISTER.csv |

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts.
- `_REFERENCES.md` — authoritative decomposition and source-root pointers.
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (locally accessible) — SEC-02 Site, SEC-03 Process Overview, SEC-04 Inlet, Separation, and Sour-Gas Export, SEC-05 Inlet Compression.
- PACKAGE_REGISTER.csv (Gate-07 snapshot) — PKG-083 row.
- DELIVERABLE_REGISTER.csv (Gate-07 snapshot) — DEL-083-02 row.
- INTERFACE_REGISTER.csv (Gate-07 snapshot) — PKG-083 interface set.
- 26020-Package_Requirements.docx heading 36 — referenced by source basis; binary not text-accessible (location TBD for clause-level extraction).
- 26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx — referenced by source basis; binary not text-accessible (location TBD).
