# Guidance: DEL-021-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-021` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 6.9kV SWITCHGEAR EQUIPMENT package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "6.9kV SWITCHGEAR EQUIPMENT" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (bus arrangement, breaker selection, relay configuration, cubicle layout) with the Package Vendor; keep facility-level integration (feeders, grounding tie-in, control-power source, communications backbone, building/foundation interface) with the EPC Integrator.
- Use `TBD` for bus current, short-circuit withstand, breaker ratings, arc-resistance class, relay schemes/settings, lineup quantity/configuration, control-power feeder origin, and physical building/room assignment until a source-supported package-specific basis is available.
- Use the DBM electrical basis only at the level it supports: facility MV service voltage and grounding regime, MV cable construction, UPS-fed control-power topology, 6.9 kV MCC communications pattern (as a reference for switchgear comms expectations), grounding/bonding philosophy, and maintenance-access constraints on cable tray/conduit.

## Considerations

The DBM electrical design basis confirms that 6.9 kV is one of three facility medium-voltage levels (13.8 kV, 6.9 kV, 4.160 kV) and that 6.9 kV serves AC inverter-drive motors rated 5,500 hp and above. The 6.9 kV system is sourced from the plant 13.8 kV switchgear via step-down transformers feeding the 820-1 6.9kV Inlet/Sales Compressor Electrical Building. Each 6.9 kV transformer is grounded by a 100 A, 10 s neutral grounding resistor operating as a tripping system. These facility facts frame the upstream conditions PKG-021 switchgear must accommodate.

The workbook row and Gate 7 registers support the existence and interface profile of the package, including the six interface facts. They do not provide bus or breaker ratings, lineup count, relay schemes, or cubicle configuration. The package-specific Word requirements source did not produce a PKG-021 match during this run; therefore, vendor-facing datasheet content should remain conservative until the missing detailed requirements are resolved.

Note that PKG-036 ("6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)") is a distinct package representing a different 6.9 kV switchgear scope housed in a different electrical building. PKG-021 should not absorb scope, equipment counts, or interface facts that belong to PKG-036. The DBM equipment list line "Medium Voltage Switchgear — quantity 1" cannot be unambiguously allocated to PKG-021 vs. PKG-036 from accessible source slices, and is captured as a human ruling item.

Grounding and bonding are explicit interface topics for PKG-021. The DBM source contains facility grounding basis, including two-point grounding for major electrical equipment and tripping-system NGR on each 6.9 kV transformer. The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing or connection details.

Communications and I&C / control cabling are also explicit interface facts. The DBM describes the 6.9 kV MCC as having Ethernet communications to the plant PLC central control panel for data acquisition; an equivalent communications/data-acquisition expectation for switchgear protective relays and metering is a reasonable EPC integration requirement and is carried as such, not as a vendor design directive.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The datasheet should require electrical routing and physical placement to preserve maintenance access (front withdrawal, rear access where applicable), but detailed clearances remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Bus, breaker, and short-circuit ratings | Mark `TBD` pending package-specific source confirmation. | DBM defines the service voltage and grounding regime but does not state package-specific electrical ratings for PKG-021. |
| Lineup count / cubicle configuration | Treat as `TBD`. | No accessible source slice defines the number of incomers, feeders, ties, or auxiliary cubicles for PKG-021. |
| Installation location | Identify the 820-1 6.9kV Inlet/Sales Compressor Electrical Building as `ASSUMPTION` (possible context), not confirmed. | DBM lists electrical buildings and identifies 820-1 by name and voltage, but does not explicitly assign PKG-021 to it. |
| MV switchgear product standards | List as `ASSUMPTION: likely applicable`. | DBM cites CEC and project electrical specifications; specific MV switchgear product standards/editions are not enumerated in accessible source. |
| Quantity allocation between PKG-021 and PKG-036 | Do not allocate the DBM "Medium Voltage Switchgear, quantity 1" line to PKG-021 without confirmation. | Two distinct packages share the 6.9 kV switchgear category; allocation is not source-supported. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 23 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Bus continuous current: TBD. No package-specific source slice available."
- Not acceptable without new source: "Bus rated 2000 A, breakers rated 40 kA interrupting." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-021-02-001 | The DBM electrical equipment list identifies "Medium Voltage Switchgear — quantity 1", but accessible source does not allocate this between PKG-021 (6.9kV SWITCHGEAR EQUIPMENT) and PKG-036 (6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical equipment list | Gate 7 `PACKAGE_REGISTER.csv` rows `PKG-021` and `PKG-036`; `DELIVERABLE_REGISTER.csv` | Datasheet Attributes; Specification Requirements | Do not allocate quantity to PKG-021 from this DBM line; record PKG-021 lineup count/configuration as `TBD` and resolve when source-supported. | TBD |
| HRR-021-02-002 | Installation location of PKG-021. The DBM lists the 820-1 6.9kV Inlet/Sales Compressor Electrical Building and describes electrical buildings as housing MV switchgear, but does not assign PKG-021 explicitly to a building/room. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list and facility electrical system narrative | Workbook Packages row 23; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-021` | Datasheet Construction; Procedure prerequisites | Carry the 820-1 association as `ASSUMPTION` context only; keep PKG-021 physical-location assignment `TBD` until human-confirmed. | TBD |
| HRR-021-02-003 | MV switchgear product standards (IEEE/IEC/CSA series) are not enumerated in accessible source for PKG-021; DBM only cites CEC and project electrical specifications generally. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical narrative | Project electrical specifications (location TBD) | Specification Standards | List MV switchgear product standards as `ASSUMPTION: likely applicable` and require source-supported confirmation before treating as binding. | TBD |
