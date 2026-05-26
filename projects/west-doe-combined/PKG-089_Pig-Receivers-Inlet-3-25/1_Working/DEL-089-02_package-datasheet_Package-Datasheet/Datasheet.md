# Datasheet — DEL-089-02 Package Datasheet

> Descriptive technical datasheet for the **Pig Receivers (Inlet) 3-25** package (PKG-089). Authority: source-grounded from `26020-Package_Requirements.docx` package heading 42 (SOW-0157..SOW-0160) and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. Inferences are labelled `ASSUMPTION`; unknown values are `TBD`. Inter-source conflicts are listed in `Guidance.md` Conflict Table.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-089-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | `PKG-089` | `_CONTEXT.md` |
| Package Name | Pig Receivers (Inlet) 3-25 | `_CONTEXT.md`; SOW-0157 |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub | DBM-Comp_and_Liquids §Facility Overview |
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC; elevation 673 m AMSL | DBM-Comp_and_Liquids §Site and Climate |
| Discipline | Mechanical | `_CONTEXT.md`; INTERFACE_REGISTER PKG-089 rows |
| Responsible Party | EPC Integrator (this datasheet); Package Vendor (engineering/design/equipment for the equipment package) | `_CONTEXT.md`; SOW-0157 |
| Workbook Reference | Packages row 77 | `_CONTEXT.md` |
| Source Document Anchor | `26020-Package_Requirements.docx` package heading 42 (location TBD inside docx) | `_CONTEXT.md` |
| Equipment Tags | `PR-1010-2`, `PR-1020-2` (per SOW-0159 "(PR-1010/1020-2)") | SOW-0159 |

## Attributes

### Function

`FACT` The pig receivers form the plant inlet boundary of the 03-25 facility. Plant inlet pipeline gas enters the facility through the pig receivers, then flows to the inlet separators (V-1600-2 / V-1700-2). Source: SOW-0158 (Basic scope, Process function); DBM-Comp_and_Liquids §Inlet Pipeline Interface and Pigging.

### Quantity, Size, and Skid Configuration

| Attribute | Value | Source / Note |
|---|---|---|
| Number of receivers | 2 (SOW-0158, SOW-0159) | CONFLICT — see `Guidance.md` Conflict Table (CFT-01): DBM §Inlet Pipeline Interface and Pigging states "A single combined three-phase pig receiver is provided." Authority `PROPOSAL`: SOW-0158/0159 (package-level basis). |
| Tagging | `PR-1010-2`, `PR-1020-2` | SOW-0159 |
| Pig receiver OD | 610 mm (24 in) | SOW-0158; SOW-0159 |
| Skid arrangement | Dedicated structural steel, non-enclosed skid, one per receiver | SOW-0158; SOW-0159; DBM §Inlet Pipeline Interface and Pigging |
| Phase service | Three-phase (per DBM "combined three-phase pig receiver") | `ASSUMPTION` for PR-1010/1020-2 if two receivers are confirmed; phase split between two receivers `TBD` |
| Pig receiver size (length, barrel ID, nominal volume) | `TBD` — DBM §Inlet Pipeline Interface and Pigging states "Pig receiver size is TBD" | DBM |

### Process Conditions

| Parameter | Value | Source |
|---|---|---|
| Design throughput (package) | 80 MMSCFD | SOW-0160 |
| Per-receiver design throughput | 40 MMSCFD `ASSUMPTION` (two-receiver assumption per SOW-0158; aligns with two-train 40 MMSCFD inlet separator basis in DBM §Inlet Separation) | SOW-0158; DBM |
| Normal operating pressure | 125 psig to 200 psig | SOW-0160 |
| MAOP | 572 psig | SOW-0160 |
| Design pressure (low) | 125 psig | SOW-0160 |
| Design pressure (normal high) | 200 psig | SOW-0160 |
| MAWP (design code) | 635 psig (consistent with inlet-separator ESDV shutdown pressure of 635 psig per DBM §Inlet Pipeline Interface and Pigging) | SOW-0160; DBM |
| Normal flowrate per receiver | `TBC` | SOW-0160 |
| Ambient temperature (historical) | −19 °C min, +22.2 °C max | SOW-0160 |
| Ambient design temperature | −40 °C min, +35 °C max | SOW-0160 |

### Service and Materials

| Parameter | Value | Source |
|---|---|---|
| Service | Sour gas (Doe field inlet wellstream); three-phase fluids may be present | SOW-0159; DBM §Inlet Pipeline Interface and Pigging |
| Sour-service H2S basis (package) | 0.1 mol% (SOW-0159 "Sour service: Design is 0.1 mol%") | CONFLICT — see `Guidance.md` Conflict Table (CFT-02): DBM §Raw Gas and Water Design Conditions gives raw-gas design H2S of 0.3 mol% with license value 2.0 mol%. |
| CO2 (low/startup) | 0.002 mol%; design, high, license `TBC` | DBM §Raw Gas and Water Design Conditions |
| Materials (pressure boundary) | `TBD` — driven by NACE MR0175/ISO 15156 sour-service classification using governing H2S/CO2 once CFT-02 is ruled | `ASSUMPTION`: NACE applies given sour-service designation |

### Appurtenances and Built-in Provisions

| Item | Provision | Source |
|---|---|---|
| Inlet ESDV (upstream of receiver) | Full-port, piggable, with position transmitters | SOW-0159; DBM |
| Skid isolation valves | All skid-mounted isolation or ESDV | SOW-0159 |
| Sweet-gas purge | Provided downstream of manual isolation valve, for sour-gas purge of receiver barrel prior to opening for pig retrieval | SOW-0159; DBM |
| Vent | Routed to HP flare system | SOW-0159; DBM ("HP flare vent provisions") |
| Pig retrieval handling | Quick-opening closure, kicker line, indication of pig presence | `ASSUMPTION` — standard pig-receiver appurtenances; not enumerated in source. `TBD` for confirmation by Package Vendor |
| Delivery-point ESDV shutdown pressure | `TBC` | DBM §Inlet Pipeline Interface and Pigging |

### Boundaries and By-Others Scope

`FACT` Items explicitly excluded from this package (per SOW-0160 "By others"):
- Interconnecting piping
- DCS integration
- Foundations
- Electrical supply to MCC

Plant inlet boundary: first aboveground flange within the lease boundary; Doe field pipeline contractor transfers scope at that flange to facility fabricator/construction contractor (DBM §Inlet Pipeline Interface and Pigging).

### Interfaces (Mechanical Package Interfaces — Workbook Row 77)

| Interface | Discipline / Type | Source |
|---|---|---|
| Process Piping | Process Piping | INTERFACE_REGISTER IFC-1AA715D034 |
| Relief / Flare / Vent (HP flare) | Relief/Flare/Vent | IFC-8FDDF0DF74 |
| Drain / Containment | Drain/Containment | IFC-9289961CBA |
| Electrical Power | Electrical | IFC-2BEB4D0C0C |
| EHT (Electrical Heat Trace) | Electrical | IFC-9EA22696F8 |
| I&C / Control Cabling | I&C | IFC-6646B13FC8 |
| Maintenance Access | Mechanical | IFC-73B5712650 |
| Grading / Site Drainage / Spill Containment | Civil | IFC-E553602F11 |
| Structural / Foundations / Supports | Structural | IFC-7BEBBC1154 |
| Pipeline / Pigging | Pipeline / Pigging | IFC-C734FF9F3E |

## Conditions

| Condition | Basis |
|---|---|
| Sour service | SOW-0159; DBM §Raw Gas (sour and variable) — H2S basis subject to CFT-02 |
| Ambient design envelope | −40 °C / +35 °C (SOW-0160) |
| Pressure envelope | 125–200 psig normal; 635 psig MAWP (SOW-0160) |
| Frac-flowback and pigging slug handling | DBM §Inlet Separation — slugs processed downstream over ~6 hours by 04-25 stabilization; operator manages pigging/flowback to avoid overloading downstream capacity |
| Winterization, EHT | `TBD` — driven by IFC-9EA22696F8 (EHT) and ambient envelope; package-level details `TBD` until Package Vendor scope |

## Construction

| Item | Basis |
|---|---|
| Skid type | Structural-steel, non-enclosed (SOW-0158, SOW-0159; DBM) |
| Foundations | By others (SOW-0160) — interface IFC-7BEBBC1154 |
| Interconnecting piping | By others (SOW-0160) — interface IFC-1AA715D034 |
| Electrical supply to MCC | By others (SOW-0160) — interface IFC-2BEB4D0C0C |
| DCS integration | By others (SOW-0160) — interface IFC-6646B13FC8 |
| Maintenance access | EPC Integrator interface IFC-73B5712650 |
| Spill containment / grading | EPC Integrator interface IFC-E553602F11 |

## References

Authoritative sources used to populate this datasheet:

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — §Facility Overview; §Scope Inclusions; §Inlet Pipeline Interface and Pigging; §Inlet Separation; §Raw Gas and Water Design Conditions
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` — SOW-0157, SOW-0158, SOW-0159, SOW-0160
- `_Decomposition/.../INTERFACE_REGISTER.csv` — PKG-089 rows (10 interfaces)
- `_Decomposition/.../DELIVERABLE_REGISTER.csv` — DEL-089-02 row
- `_Decomposition/.../OBJECTIVE_REGISTER.csv` — OBJ-002 through OBJ-010 (linked via SOW-0157..0160)
- Inaccessible (not converted to local markdown; `location TBD` for clause-level citations): `_Sources/26020-Package_Requirements.docx` (package heading 42) and `_Sources/26020-Packages_Interfaces_4_export.xlsx` — content is reflected via the extracted SCOPE_LEDGER and INTERFACE_REGISTER rows that cite these sources.
