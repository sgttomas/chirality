# Guidance: DEL-014-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-014` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the lighting and exhaust-fan low-voltage contactor panels package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables. All seven applicable interfaces shall appear.
- Keep vendor-owned design work (contactor selection, panel internals, schedule generation) with the Package Vendor and facility-level integration (building coordination, source distribution panel assignment, control-system tie-in, area-classification interlock) with the EPC Integrator.
- Use `TBD` for panel quantity, contactor ratings, circuit schedules, feeder sizing, in-building location, and per-building assignment until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: 208/120 V supply, contactor-panel housing in electrical buildings, lighting/exhaust-fan loads, raceway methods, grounding, and forced-ventilation interlock.

## Considerations

The DBM electrical design basis confirms the 208/120 V, 3 phase, 4 wire, 60 Hz, solidly grounded "Lighting and utility services" supply that energizes the contactor panels, and explicitly lists "208/120 V contactor panels" among the equipment housed in prefabricated modular electrical buildings. The 208/120 V system is fed from 600 V to 208/120 V distribution transformers with dedicated 208/120 V distribution panelboards.

The DBM lists the loads served by the 208/120 V system as lighting and utility receptacles, building exhaust fans, building heater blower fans, electric heat tracing, and packaged equipment requiring 208/120 V power. The lighting subset includes 120/208 V LED general-purpose lighting fed from the nearest power distribution centre, MCC-room flat-panel LED fixtures, process-area and outdoor LED fixtures, post lighting for the overall area, and battery-backed exit/emergency lighting per building code.

The exhaust-fan subset is safety-relevant: where forced-ventilation modules or buildings rely on ventilation to maintain area classification, exhaust-fan control and monitoring must include an interlock initiated in the plant control system. The control I/O for exhaust-fan and heater control may be hosted at Remote Distribution Centre (RDC) Remote I/O nodes (Allen-Bradley Flex5000). This places the contactor panels squarely in the I&C/Control Cabling and Communications/Network interface scope as well as Area/Exterior Lighting and Electrical Power.

Building integration imposes additional facility-level constraints: prefabricated, pile-supported, elevated buildings with bottom cable entry, n + 1 HVAC, EMT permitted between adjacent panels (including from control panels to contactor panels), and equipment door sizing for largest-equipment removal. Cable tray and conduit routing shall not interfere with maintenance access.

The package-specific Word requirements source (`26020-Package_Requirements.docx`) did not produce a PKG-014 match during this run, so vendor-facing datasheet content should remain conservative for panel count, ratings, circuit assignments, and per-building location until those source slices are resolved.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Panel quantity / per-building assignment | Mark `TBD` pending package-specific source confirmation. | DBM confirms that 208/120 V contactor panels are housed in electrical buildings "as required by detailed design," but does not enumerate quantity or per-building assignment for PKG-014. |
| Contactor ratings / circuit schedules | Mark `TBD`. | No accessible source slice defines contactor sizing, circuit counts, or per-circuit load lists for PKG-014. |
| Split between "lighting" and "exhaust-fan" contactor panels | Treat as a vendor/detailed-design distinction; keep both subsets represented in load lists but do not invent a specific physical-panel split for PKG-014. | The package name implies a split, but no source slice confirms how many discrete panel assemblies serve each subset. |
| Standards | List CEC, area classification, project electrical specifications, and building code (exit/emergency lighting) as governing bases with clause locations TBD. | DBM references these bases, but detailed clauses/specification documents are not present in the deliverable folder. |
| Forced-ventilation interlock scope | Carry the interlock as a hard requirement wherever exhaust-fan loads are served. | DBM states the interlock is required for safe operation of electrical equipment in ventilation-dependent classified areas. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 16 and `INTERFACE_REGISTER.csv`."
- Acceptable source-grounded entry: "Upstream supply: 208/120 V, 3 phase, 4 wire, 60 Hz, solidly grounded distribution panelboards fed from 600 V to 208/120 V distribution transformers (DBM '208/120 V Systems and SCR Heater Controls')."
- Acceptable source-gap entry: "Panel quantity and per-building assignment: TBD. No package-specific source slice available."
- Not acceptable without new source: "Package consists of N lighting contactor panels rated X A and M exhaust-fan contactor panels rated Y A in Building B." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-014-02-001 | Package name combines "CONTACTOR PANELS - LIGHTING" and "EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE", implying a discrete split of physical-panel assemblies, but no accessible source slice confirms how many discrete panel assemblies serve lighting vs. exhaust-fan loads or how they are assigned per building. | Workbook Packages row 16; `PACKAGE_REGISTER.csv` row `PKG-014` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Electrical Buildings" and "208/120 V Systems" | Datasheet Attributes / Construction; Specification Requirements; Procedure Steps | Treat both subsets (lighting; exhaust-fan / heater-fan) as functional load groupings under one package, and keep physical-panel split as a vendor/detailed-design decision. | TBD |
| HRR-014-02-002 | The package title says "LOW VOLTAGE" but DBM defines "Low-voltage services" as 600 V (3 phase, 3 wire, HRG), whereas the loads served by contactor panels (lighting, receptacles, exhaust fans, heater blower fans) are explicitly the 208/120 V "Lighting and utility services" system. | Workbook Packages row 16 (package title) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Voltage Levels and Services"; "208/120 V Systems and SCR Heater Controls" | Datasheet Identification / Attributes; Specification Scope / Requirements | Interpret "LOW VOLTAGE" in the package title as "below medium voltage" (i.e., the 208/120 V utility system), consistent with the contactor-panel loads. Record any contactor-panel feeders at 600 V (if applicable to coil or distribution side) as TBD pending vendor data. | TBD |
| HRR-014-02-003 | DBM places exhaust-fan and heater control I/O at RDC Remote I/O nodes (Allen-Bradley Flex5000), but does not confirm whether PKG-014 contactor panels host their own integral control logic or are slaved to RDC Remote I/O. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 804 (Remote I/O may support exhaust fan/heater controls) | DBM "208/120 V Systems"; absence of integral-PLC source slice for contactor panels | Datasheet Attributes (Exhaust-fan / heater control I/O); Specification REQ-014-02-008 | Treat exhaust-fan and heater control I/O as hosted at RDC Remote I/O nodes by default and carry "integral panel control logic" as TBD pending vendor data. | TBD |
