# Datasheet — DEL-083-01 Scope of Work (PKG-083 Inlet Separators 3-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-083-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package | PKG-083 Inlet Separators 3-25 | `_CONTEXT.md` |
| Workbook Package ID | 83 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |
| Source Reference | Workbook Packages row 67; 26020-Package_Requirements.docx package heading 36 | `_CONTEXT.md` |

## Attributes

### Tagged Equipment (Inlet Separation Package)

The package scope corresponds to the 03-25 West Doe Compressor Station inlet separation system as defined in the governed DBM (3-25_Comp_and_Liquids_DBM.md, SEC-04 "Inlet Separation").

| Tag | Item | Per-Unit Basis | Source |
|---|---|---|---|
| V-1600-2 | Horizontal three-phase inlet separator, train A | 50% facility capacity | DBM §SEC-04 "Inlet Separation" |
| V-1700-2 | Horizontal three-phase inlet separator, train B | 50% facility capacity | DBM §SEC-04 "Inlet Separation" |
| (TBD-tag) | Inlet pressure-control valves, parallel | At least two per package | DBM §SEC-04 "Flow Distribution and Controls" |
| (TBD-tag) | Produced-water level-control valves, parallel | At least two per package | DBM §SEC-04 "Flow Distribution and Controls" |
| (TBD-tag) | Heated self-framing separator building | One end of each package enclosed; exact extent TBD | DBM §SEC-04 "Inlet Separation" |

Note: Reciprocating inlet compressors (KM-2150, KM-2250), the pig receiver, the inlet ESDV, and downstream TEG dehydration are adjacent packages and are not within PKG-083 scope unless explicitly assigned by the package register. **ASSUMPTION:** package boundary draws at the inlet separator package skids; cross-package interface ownership confirmed by `_DEPENDENCIES.md` (currently none declared — see `_DEPENDENCIES.md`).

### Per-Separator Process Conditions

| Parameter | Value | Source |
|---|---|---|
| Gas flow | 40 MMSCFD | DBM §SEC-04 "Inlet Separation" |
| Condensate flow | 556 m3/d (3,494 bbl/d) | DBM §SEC-04 |
| Produced-water flow | 1,800 m3/d (11,322 bbl/d) | DBM §SEC-04 |
| Diameter | 2,743 mm (9 ft) | DBM §SEC-04 |
| Straight-side length | 12,191 mm (40 ft) | DBM §SEC-04 |
| Pressure class | ANSI 600# | DBM §SEC-04 |
| Design pressure | 4,963 kPag | DBM §SEC-04 |
| Slug handling | ~38 m3 | DBM §SEC-04 |
| Internal coating | Devchem 253 | DBM §SEC-04 |
| Low operating pressure | 125 psig | DBM §SEC-04 |
| Design operating pressure | 200 psig | DBM §SEC-04 |
| Maximum operating pressure | 572 psig | DBM §SEC-04 |
| Normal high operating pressure | TBC | DBM §SEC-04 |
| Inlet design temperature | 8.3 deg C (reconciliation TBC) | DBM §SEC-04, §SEC-03 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM §SEC-02 |
| Elevation | 673 m AMSL | DBM §SEC-02 |
| Barometric pressure | 93.3 kPa(a) | DBM §SEC-02 |
| Design ambient range | -40 deg C to +35 deg C | DBM §SEC-02 |
| Service | Sour gas, raw condensate, produced water (three-phase) | DBM §SEC-04 |
| H2S design | 0.3 mol% (license 2.0 mol%; high TBC) | DBM §SEC-03 |
| CO2 design | TBC; low/startup 0.002 mol% | DBM §SEC-03 |

## Construction

| Item | Basis | Source |
|---|---|---|
| Module form | Two identical packages, modularized for shop assembly; instrumentation and one end enclosed in heated self-framing building | DBM §SEC-04 |
| Internals | Devchem 253 coating; manually adjustable weir; vertical/horizontal high-performance mesh/vane mist eliminators; de-sanding provisions | DBM §SEC-04 |
| Piping coating | Not coated under current separator basis | DBM §SEC-04 |
| Building extent | TBD | DBM §SEC-04 |
| Vessel design | Per applicable pressure class, sour-service requirements, corrosion allowance, coating, manway access, internals removal, drainage, venting, inspection (per SEC-08 vessel general) | DBM §SEC-04, §SEC-08 (location TBD) |

## Package Function (Summary Attributes)

- Receive sour wellstream from the Doe field inlet pipeline downstream of pig receiver/isolation.
- Separate sour natural gas, raw condensate, and produced water; each train sized at 50% of facility capacity.
- Deliver separated sour gas to inlet compression (KM-2150 / KM-2250) at 125-165 psig first-stage suction (per DBM §SEC-05).
- Deliver raw condensate forward to 04-25 MPFS / stabilization routing (per DBM §SEC-01 "Facility Overview").
- Deliver produced water to liquids hub produced-water tanks and H2O2 treatment (per DBM §SEC-01).
- Provide methanol drain at separator boot when methanol appears (per DBM §SEC-04 "Slug and Flowback Basis" / methanol note).

## References

- `_CONTEXT.md` — deliverable identity, scope items, supported objectives
- `_REFERENCES.md` — accepted upstream decomposition snapshot and source root
- `_DEPENDENCIES.md` — declared upstream/downstream (none declared during PREPARATION)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — primary governed source (SEC-01, SEC-02, SEC-03, SEC-04, SEC-05, SEC-08 referenced)
- `_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md` — KTY-04-02 Inlet-Separator KA traceability (HBK-0050..0059 evidence chain)
- Decomposition: GATE-07 PROJECT_DECOMP snapshot — `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- Source materials cited in decomposition row but not locally extracted as deliverable-scoped slices: `26020-Package_Requirements.docx` package heading 36 (location TBD — DOCX not parsed in this pass); Workbook Packages row 67 (location TBD).

## Covers / Supports

- Covers scope items: SOW-0123, SOW-0124, SOW-0125, SOW-0126 (per `_CONTEXT.md`)
- Supports objectives: OBJ-002 through OBJ-010 (per `_CONTEXT.md`; **ASSUMPTION** under PACKAGE_HEURISTIC association mode)
