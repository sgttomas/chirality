# Datasheet — DEL-083-03 Construction Work Package (PKG-083 Inlet Separators 3-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-083-03_construction-work-package |
| Deliverable Name | Construction Work Package |
| Parent Package | PKG-083 — Inlet Separators 3-25 (WBS 02; Tag 26020-02-17-003) |
| Discipline | Mechanical |
| Deliverable Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Covers Scope Items | SOW-0123, SOW-0124, SOW-0125, SOW-0126 |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION — package-grouping heuristic; sourced from `_CONTEXT.md`) |

## Attributes — Package Being Installed

| Attribute | Value | Source |
|---|---|---|
| Package scope | Two (2) identical horizontal three-phase separators (V-1600-2, V-1700-2) | PACKAGE_REGISTER.csv row PKG-083; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-04 |
| Process function | Separates raw inlet gas into sour natural gas (vapour), sour raw condensate (light liquid), and sour water (heavy liquid) | PACKAGE_REGISTER.csv row PKG-083 |
| Capacity basis | 2 x 50% of facility capacity | DBM-Comp_and_Liquids §SEC-04 Inlet Separation |
| Per-separator gas flow | 40 MMSCFD | DBM-Comp_and_Liquids §SEC-04 (table) |
| Per-separator condensate flow | 556 m3/d (3,494 bbl/d) | DBM-Comp_and_Liquids §SEC-04 (table) |
| Per-separator produced-water flow | 1,800 m3/d (11,322 bbl/d) | DBM-Comp_and_Liquids §SEC-04 (table) |
| Vessel diameter | 2,743 mm (9 ft) | DBM-Comp_and_Liquids §SEC-04 (table) |
| Vessel straight-side length | 12,191 mm (40 ft) | DBM-Comp_and_Liquids §SEC-04 (table) |
| Pressure class | 600# | DBM-Comp_and_Liquids §SEC-04 (table) |
| Design pressure | 4,963 kPag | DBM-Comp_and_Liquids §SEC-04 (table) |
| Slug handling | ~38 m3 per separator | DBM-Comp_and_Liquids §SEC-04 (table) |
| Internal coating | Devchem 253 | DBM-Comp_and_Liquids §SEC-04 (table); §SEC-06 |
| Building | Instrumentation and one end of each package enclosed in a heated self-framing building; exact extent TBD | DBM-Comp_and_Liquids §SEC-04 |

## Conditions — Installation Site

| Condition | Value | Source |
|---|---|---|
| Site | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15W6, north of Dawson Creek, BC | DBM-Comp_and_Liquids §Site Description |
| Site elevation | 673 m AMSL | DBM-Comp_and_Liquids §Site Description |
| Inlet design temperature (process) | 8.3 deg C (note: detailed design shall reconcile inlet temperature basis) | DBM-Comp_and_Liquids §SEC-04 |
| Service | Sour gas, sour condensate, sour produced water | DBM-Comp_and_Liquids §SEC-04 |
| Ambient/seasonal envelope | TBD (not stated in accessed source slice) | location TBD |

## Construction — Interfaces Owned by EPC Integrator at PKG-083

Per PACKAGE_REGISTER.csv row PKG-083, the EPC Integrator owns integration into the functional process facility including the following interface types for this package:

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- EHT (electric heat tracing)
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

Notably absent from the PKG-083 interface list (compared with other mechanical packages): Electrical Power and Building HVAC / Services. TBD whether power feed and building services are scoped elsewhere or are inside the vendor package boundary.

## Construction — Adjacent Tie-in Conditions

| Tie-in | Source-stated condition |
|---|---|
| Inlet ESDV shutdown pressure | 635 psig at the inlet separator ESDV (DBM §Pig Receiver / ESDV) |
| Inlet pipeline interface | Single Doe field inlet pipeline via pig receiver/isolation upstream (DBM §SEC-04 inlet receipt) |
| Drive-gas recycle | Returns to the separators from downstream of inlet compressor aftercoolers (DBM §Flow Distribution and Controls) |
| Inlet pressure-control valves | At least two parallel per package; balanced globe hardened trim; dP limit <=5 psid (DBM §Flow Distribution and Controls) |
| Produced-water level-control valves | At least two parallel per package (DBM §Flow Distribution and Controls) |
| Methanol drain | Methanol expected to drain at the inlet separator boot; downstream methanol disposition TBD (DBM §SEC-03 narrative line 218) |

## Construction Work Package Artifact Set (anticipated)

Per `_CONTEXT.md` anticipated artifacts:

- Construction work package
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## References

- `_CONTEXT.md` (deliverable identity, scope, objectives)
- `_REFERENCES.md` (authoritative basis pointers)
- `_DEPENDENCIES.md` (no declared upstream/downstream during PREPARATION)
- PACKAGE_REGISTER.csv (GATE-07_Final_Published_2026-05-24) row PKG-083
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot) row DEL-083-03_construction-work-package
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (SEC-03 Facility Inlet, SEC-04 Inlet Separation)
- 26020-Package_Requirements.docx package heading 36 — referenced but binary not parsed in this run; clause-level text not extracted (location TBD)
- Bid Docs/Budgetary/26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx — referenced by package register; binary not parsed in this run (location TBD)
