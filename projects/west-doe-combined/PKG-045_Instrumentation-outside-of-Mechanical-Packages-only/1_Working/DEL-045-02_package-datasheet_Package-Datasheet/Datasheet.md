# Datasheet — DEL-045-02 Package Datasheet (PKG-045 Instrumentation, WBS 03)

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-045-02_package-datasheet | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-045-02 |
| Parent package | PKG-045 — Instrumentation (outside of Mechanical Packages only) | `PACKAGE_REGISTER.csv` row PKG-045 |
| Workbook row | 47 (Packages) | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| WBS | 03 (03-25 Compressor Station and Liquids Hub) | `PACKAGE_REGISTER.csv` row PKG-045 |
| Discipline | Instrumentation | `PACKAGE_REGISTER.csv` row PKG-045 |
| Deliverable type | EPC Package Datasheet | `DELIVERABLE_REGISTER.csv` row DEL-045-02 |
| Responsible party | EPC Integrator | `DELIVERABLE_REGISTER.csv` row DEL-045-02 |
| Covers scope item | SOW-0046 | `DELIVERABLE_REGISTER.csv` row DEL-045-02 |
| Supports objectives | OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 (ASSUMPTION: package-grouping heuristic per `_CONTEXT.md`) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Source authority | Workbook Packages row 47; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | `PACKAGE_REGISTER.csv` row PKG-045 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package title | Instrumentation (outside of Mechanical Packages only) | `PACKAGE_REGISTER.csv` PKG-045 |
| Workbook UID(s) | 26020-01-32-002 | `PACKAGE_REGISTER.csv` PKG-045 |
| Operating site | 03-25 Compressor Station and Liquids Hub (West Doe complex) | DBM 3-25_Comp_and_Liquids_DBM.md SEC-14, SEC-13 |
| Package philosophy | Plug-n-play package philosophy; instrumentation field supports, power, and communications included in each package scope as appropriate (Gate 6 disposition) | `INTERFACE_REGISTER.csv` PKG-045 (interface notes) |
| Approved detector manufacturer basis | MSA / General Monitors | DBM SEC-14 "Detector Manufacturer" |
| BPCS / RIO platform | Allen-Bradley ControlLogix BPCS with Flex5000 Remote I/O over PRP | DBM SEC-14 ESD table |
| ESD pushbutton wiring basis | Wired to nearest Remote I/O control panel where practical | DBM SEC-14 ESD table |
| ESD pushbutton location basis | Outside all building exterior doors | DBM SEC-14 |
| Visual alarm association | Red beacon for Fire Detection, LEL Detection, ESD activation | DBM SEC-14 "Audible and Visual Alarms" |
| Audible alarm basis | Horn tone selection differentiating fire, LEL, H2S, ESD trip; final mapping detailed-design | DBM SEC-14 |
| Detector scope (in-scope hazards) | Fire, LEL, H2S, methyl mercaptan | DBM SEC-14 |
| Detector placement drivers | Process hazards, building layouts, ventilation, equipment spacing, truck loading, tankage, caustic/DSO systems, VRU, flare/vent interfaces, compressor buildings, TEG package, operator access | DBM SEC-14 |
| Instrument air supply basis | Supplied from 04-25 (no local 03-25 compressor); SCA-006 in effect | DBM SEC-13 "Instrument Air"; SEC-14 utility narrative |
| Instrument air demand (03-25) | 393 SCFM TBC; combined 03-25/04-25 demand 1,113 SCFM TBC | DBM SEC-13 "Instrument Air Interface" |
| Ambient design minimum | -40 deg C (governs exposed instrumentation, panels, field devices) | DBM SEC-04 "Site Basis" (line 145) |
| Cable separation basis | 13.8 kV / 4,160 V / 600 V power separated from control and instrument circuits by distance, shielding, or routing | DBM SEC-13 |
| Field-device tag list / set-points / voting | TBD pending detailed design and safety studies | DBM SEC-14 |
| Cause-and-effect matrix / SIL ratings | TBD by HAZOP and SIL assessment | DBM SEC-14 |
| Enclosure classifications | TBD by detailed design | DBM SEC-14 |
| Building list / building-by-building ESD placement | TBD until final building list and layout frozen | DBM SEC-14 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service split for shared HP/Cryo and LP dual flare stack and incinerator | Open interface item; allocation between 03-25 and 04-25 not fully resolved | DBM SEC-04 (line 56) |
| Remaining 03-25 instrument demand | 100 SCFM TBC | DBM SEC-13 instrument-air table (line 478) |
| Heated package buildings | Instrumentation and one end of each package in heated self-framing building; exact building extent TBD | DBM SEC-12 (line 260) |
| Safety device routing | Safety devices (fire, LEL, H2S, ESD) wired to nearby Remote I/O to reduce field wiring | DBM SEC-14 |
| Reset, bypass, permissive logic | TBD; to be defined in cause-and-effect matrix and shutdown philosophy | DBM SEC-14 |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction scope element (instrumentation hookups) | Installation of shipped-loose instruments and valves, home-run cabling, terminations | DBM SEC-05 (line 75) |
| Coordination requirements | Coordinate package buildings, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, drain/vent tie-ins with civil, electrical, controls, and instrumentation sections | DBM SEC-08 (line 619) |
| Electrical & controls interface coordination | SEC-07 (Electrical) and SEC-13 (Controls) | DBM SEC-13 (line 774) |

## Physical Interfaces (carried as datasheet evidence per Gate 6 disposition)

Per `INTERFACE_REGISTER.csv` PKG-045 and `ARTIFACT_REGISTER.csv` for DEL-045-02, the following package-level interfaces are recorded as datasheet evidence:

| Interface ID | Type | Present | Source |
|---|---|---|---|
| IFC-33F8A9F366 | Process Piping | YES | `INTERFACE_REGISTER.csv` row PKG-045 |
| IFC-AE76B11E50 | Utility Piping | YES | `INTERFACE_REGISTER.csv` row PKG-045 |
| IFC-2D030CA850 | Electrical Power | YES | `INTERFACE_REGISTER.csv` row PKG-045 |
| IFC-210F46B073 | I&C / Control Cabling | YES | `INTERFACE_REGISTER.csv` row PKG-045 |
| IFC-9DAC4D3C4D | Communications / Network | YES | `INTERFACE_REGISTER.csv` row PKG-045 |

Vendor model selection, environmental ratings, certification details, range, mounting, and accessories: TBD (detailed-design items per DBM SEC-14).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- GATE-07 snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- DBM source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-04, SEC-05, SEC-08, SEC-12, SEC-13, SEC-14)
- Workbook Packages row 47 (location TBD; not locally accessible as a parsed slice)
