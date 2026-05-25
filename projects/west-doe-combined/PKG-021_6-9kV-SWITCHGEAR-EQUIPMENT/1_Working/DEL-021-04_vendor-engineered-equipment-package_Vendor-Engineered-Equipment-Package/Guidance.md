# Guidance — DEL-021-04 Vendor Engineered Equipment Package (6.9 kV Switchgear Equipment)

> Directional guidance for the Package Vendor and EPC Integrator on producing and accepting the engineered 6.9 kV switchgear equipment package, anchored by the EPC Scope of Work (`DEL-021-01`) and Package Datasheet (`DEL-021-02`).

## Purpose

`DEL-021-04` is the Package Vendor's production unit: engineering, design, fabrication/supply, and physical equipment for PKG-021. It exists to translate the EPC-owned scope and datasheet into a buildable, testable, code-compliant 6.9 kV switchgear lineup that integrates cleanly with the 13.8 kV upstream switchgear, the 6.9 kV `MCC-8200`, the starting VFDs for `KM-2150`/`KM-2250`, and the plant PLC.

## Principles

- **EPC Datasheet is the authoritative interface contract.** The Package Vendor does not redefine system voltage, grounding, bus sizing, or interface scope. Those are set by `DEL-021-02` and the DBM electrical chapter. Vendor design choices fill the engineered-detail space below those constraints, not above them.
- **Source over convention.** Where the DBM electrical chapter is explicit (system voltages, grounding, MCC type, PFCC prohibition on the synchronous-transfer bus), the vendor SHALL match it. Convention or vendor-standard alternatives that conflict with the DBM require a documented deviation accepted by the EPC Integrator.
- **TBD over invention.** Where sizing inputs (load flow, short-circuit, arc-flash) are not yet issued, the vendor design basis SHALL state the assumed values as `ASSUMPTION` with a placeholder pending study issuance, not as accepted facts.
- **Integration discipline.** Bottom-entry cabling, n+1 HVAC, ground-grid tie-ins, and PLC Ethernet interface are facility constraints that flow into vendor equipment dimensions, terminations, and accessory selections.

## Considerations

- **Synchronous-transfer bus.** `MCC-8200` is called out as a synchronous-transfer bus; switchgear protection settings, breaker close timing, and any source-paralleling logic upstream require explicit coordination with the MCC vendor and the plant control philosophy.
- **VFD interactions.** Starting VFDs for `KM-2150`/`KM-2250` impose harmonic and inrush considerations on the upstream bus; vendor should clarify whether harmonic mitigation is in scope or excluded.
- **Grounding tripping system.** The 100 A / 10 s neutral grounding resistor operating as a tripping system means a single ground fault is expected to trip rather than alarm. Protection coordination must reflect this — not a sustained-fault basis.
- **Cable system.** Three-conductor copper TECK cable rated 8 kV with 100 percent insulation (shielded) drives termination compartment design (gland plate, lug pads, stress-cone provisions).
- **Studies not yet issued.** Relay coordination, arc-flash, and load-flow studies are listed in the DBM as required project studies; vendor proposal should make explicit which study outputs the design depends on and how revisions will be re-baselined.
- **Code edition.** CEC is referenced generically in the DBM; the binding edition and any provincial amendments are project-spec items not extracted in the accessible markdown source set — see Conflict Table.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Metal-clad vs. metal-enclosed construction | Not specified in accessible sources. Metal-clad offers compartmentation and maintainability typical for 6.9 kV utility/industrial; metal-enclosed may be acceptable in some scopes. Decision should be made in `DEL-021-02` rather than left to vendor default. |
| Vacuum vs. SF6 breakers | Not specified in accessible sources. Both meet typical MV duty; selection driven by EPC standardization, environmental policy, and maintainability. |
| Arc-flash mitigation (zone-selective interlocking, light/arc-detection, remote racking) | Not required by accessible sources but a common modern mitigation for the published arc-flash study requirement. |
| Harmonic filtering for VFD starts | Not in DBM; trade-off between vendor scope creep and integration cleanliness. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-021-04-01 | DBM equipment list shows "Medium Voltage Switchgear (1)" but does not allocate to PKG-021 vs. other MV packages (PKG-020 13.8 kV, PKG-022 5 kV). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~2880 | Gate 7 `PACKAGE_REGISTER` for PKG-021 (does not state quantity) | Datasheet Attributes, Specification REQ-021-04-011 | Treat quantity as TBD and defer to `DEL-021-02 Package Datasheet`. | TBD |
| CONF-021-04-02 | Code-edition specifics (CEC edition, IEEE C37 references) not present in accessible source slices but assumed applicable. | DBM Area Classification / Transformers sections (cite CEC generically) | `_Sources/26020-Package_Requirements.docx` (not extracted) | Specification Standards | Mark binding code editions as `location TBD` in vendor design basis pending extraction of `26020-Package_Requirements.docx`. | TBD |
| CONF-021-04-03 | Sibling `DEL-021-02` Package Datasheet not yet drafted; this Vendor package would normally consume it. | This deliverable folder has no `Datasheet.md` cross-link yet | `DEL-021-02_package-datasheet_Package-Datasheet` folder has only metadata, no production docs | Specification REQ-021-04-010, all interface clauses | Defer engineered-detail commitments until `DEL-021-02` is drafted; flag as a sequencing dependency. | TBD |

## Examples (from accessible sources)

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Motor Control section: "The 6.9 kV motor control center shall provide mechanically latched fused contactors with motor protection relays and an Ethernet communication port for connection to the plant PLC central control panel for data acquisition. Starting VFDs shall be provided for the KM-2150/2250 Inlet/Sales Gas Compressor motors. Power-factor-correction capacitor banks shall not be installed on the MCC-8200 synchronous-transfer bus." This is the principal source slice constraining vendor MCC/VFD interface and PFCC scope.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding and Bonding section: "Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system." Defines the tripping-system basis for protection coordination.
