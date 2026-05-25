# Guidance — DEL-034-04 Vendor Engineered Equipment Package (600V Electrical Building 820-2)

> Directional guidance for the Package Vendor and EPC Integrator on producing and accepting the engineered 600 V electrical building package for `PKG-034` (Building 820-2), anchored by the EPC Scope of Work (`DEL-034-01`) and Package Datasheet (`DEL-034-02`).

## Purpose

`DEL-034-04` is the Package Vendor's production unit: engineering, design, fabrication/supply, and physical equipment for PKG-034. It translates the EPC-owned scope and datasheet into a buildable, testable, code-compliant 600 V electrical building integrating the 600 V MCC, 600 V VFDs, 208/120 V distribution, UPS systems, PLC/network panels, HVAC, grounding, and bottom-entry cable provisions per the DBM electrical chapter.

## Principles

- **EPC Datasheet is the authoritative interface contract.** The Package Vendor does not redefine system voltage, grounding, MCC architecture, UPS scope, or interface boundary. Those are set by `DEL-034-02` and the DBM electrical chapter. Vendor design choices fill the engineered-detail space below those constraints, not above them.
- **Source over convention.** Where the DBM electrical chapter is explicit (600 V/3ph/3w/60Hz HRG 5 A; integrated VFDs in MCC; alarm-only ground-fault on 600 V; bottom-entry cabling; n+1 HVAC), the vendor SHALL match it. Convention or vendor-standard alternatives that conflict with the DBM require a documented deviation accepted by the EPC Integrator.
- **TBD over invention.** Where sizing inputs (load flow, short-circuit, arc-flash) and the Building 820-2 designator/served-area are not yet issued, the vendor design basis SHALL state assumed values as `ASSUMPTION` with a placeholder pending study/datasheet issuance, not as accepted facts.
- **Integration discipline.** Bottom-entry cabling, n+1 HVAC, ground-grid tie-ins at two points, PLC/network interfaces, and exterior maintenance provisions are facility constraints that flow into building dimensions, terminations, accessory selections, and door/transom design.

## Considerations

- **Building 820-2 not in the DBM buildings list.** The accessible DBM Deepcut buildings list (lines 2811-2816) enumerates 820-1 as the 6.9 kV Inlet/Sales Compressor Electrical Building and lists 840-1, 850-1, 860-1 as 600 V buildings, but does not enumerate "820-2". This deliverable assumes 820-2 is an additional 600 V electrical building introduced after the DBM buildings list was authored. Confirmation belongs to `DEL-034-02`.
- **600 V VFDs in the MCC lineup.** DBM is explicit that standalone 600 V VFDs are not allowed unless dedicated to large motors. Vendor should propose any standalone-VFD cases with justification.
- **HRG with alarm-only ground fault.** Continuity of operations is the design driver. Protection coordination must reflect alarm-only ground-fault on 600 V; trip on second ground or other engineered conditions belongs in the protection design, not implicit defaults.
- **Standby power at the MCC level.** The DBM standby basis is LV standby generators connected at the 600 V MCC with transfer switches, replacing the prior centralized 13.8 kV concept. Vendor design must accommodate the transfer-switch interface even if the generator itself is supplied under a separate package.
- **Bottom-entry and elevated building.** Building elevation on piles to provide MCC incoming cable-tray space underneath is a structural prerequisite that affects vendor base steel, door/access elevations, and outdoor lighting/GFI provisions.
- **UPS coverage.** Both 120 V AC and 125 V DC UPS systems may be housed; coverage of control system, selected emergency lighting, MV breaker control, and MV protective relays is set in the DBM electrical voltage table. Specific loads served from 820-2 must come from `DEL-034-02`.
- **Code edition.** CEC is referenced generically in the DBM; the binding edition and any provincial amendments are project-spec items not extracted in the accessible markdown source set — see Conflict Table.
- **Comp_and_Liquids facility (03-25).** Comp_and_Liquids DBM line 740 states 03-25 is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. Whether PKG-034 (820-2) serves 04-25 or 03-25 loads is not stated in accessible sources; HRR-034-04-001 covers this gap.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Standalone vs. MCC-integrated 600 V VFDs | DBM default is integrated; standalone requires dedicated-large-motor justification. Vendor should not propose standalone except as a documented deviation. |
| UPS sizing strategy | Centralized larger UPS vs. multiple smaller UPS per load class. Not specified in accessible sources; decision belongs to `DEL-034-02` based on critical-load list. |
| Building shell material/insulation | Not specified in accessible sources beyond "prefabricated modular". Trade-off between vendor-standard packages and EPC standardization. |
| Arc-flash mitigation on 600 V (zone-selective interlocking, light/arc detection, remote racking) | Not required by accessible sources, but a common mitigation responding to the DBM-listed arc-flash study. |
| HVAC redundancy beyond n+1 | DBM requires n+1; further redundancy is a cost/availability trade-off not addressed by accessible sources. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-034-04-001 | Building "820-2" is not enumerated in the DBM buildings list (which names 820-1 6.9 kV Inlet/Sales Compressor Electrical Building and 600 V buildings 840-1, 850-1, 860-1). Served area, location, and elevation for 820-2 are not stated in accessible sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Buildings table (lines 2811-2816) | Gate 7 `PACKAGE_REGISTER` row for PKG-034 (states 820-2 by name, source Workbook row 36) | Datasheet Identification/Attributes; Specification REQ-034-04-016; Procedure prerequisites | Carry 820-2 designator from Gate 7 register; mark served area, location, and feed transformer as TBD pending `DEL-034-02`. | TBD |
| HRR-034-04-002 | DBM Equipment List rows for low-voltage switchgear (2), low-voltage MCCs (1), and low-voltage induction motors (2) are not explicitly allocated to PKG-034 vs other 600 V buildings (PKG-033 840-1, PKG-035 850-1, PKG-040 860-1). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Equipment List (lines 2877-2882) | Gate 7 `PACKAGE_REGISTER` for PKG-034 (does not state quantities) | Datasheet Attributes; Specification REQ-034-04-015 | Hold quantities as TBD in this deliverable; defer authoritative allocation to `DEL-034-02 Package Datasheet`. | TBD |
| HRR-034-04-003 | Code/standard editions (CEC edition; IEEE/ANSI/NEMA references for LV switchgear/MCC/VFD/UPS) not present in accessible source slices but assumed applicable. | DBM lines 2951, 2989 (cite CEC generically) | `_Sources/26020-Package_Requirements.docx` (not extracted) | Specification Standards; REQ-034-04-013 | Mark binding code editions as `location TBD` in vendor design basis pending extraction of `26020-Package_Requirements.docx`. | TBD |
| HRR-034-04-004 | Sibling `DEL-034-01 Scope of Work` and `DEL-034-02 Package Datasheet` four-document sets are not yet drafted; this Vendor production unit would normally consume them. | This deliverable folder; no cross-links yet | Sibling DEL-034-01/02 folders | Specification REQ-034-04-002, -014, -015; all interface clauses | Defer engineered-detail commitments until `DEL-034-01` and `DEL-034-02` are drafted; flag as a sequencing dependency for `dependency-extract`. | TBD |

## Examples (from accessible sources)

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings section (line 2973): "Electrical buildings shall be prefabricated, modular buildings located in general purpose areas. They shall house, as required by detailed design, 13.8 kV main switchgear, medium-voltage motor control centers, medium-voltage reduced-voltage soft starters, medium-voltage VFDs, 600 V MCCs, 120 V AC UPS systems with battery banks and distribution panels, 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, and network racks." This is the principal source slice framing the building's expected internal scope.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Motor Control section (line 2959): "The 600 V MCCs shall be traditional MCCs complete with electronic motor overload relays.... 600 V VFDs shall be provided as part of the 600 V MCC lineup. Standalone 600 V VFDs are not allowed unless dedicated to large motors." Defines the MCC/VFD architecture basis.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding section (line 2985): "Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor. The 600 V MCCs shall include power metering and ground/resistor fault detection. Ground-fault protection on 600 V systems shall be alarm-only to maintain continuity of operations." Anchors the HRG/alarm-only basis.
