# Datasheet: DEL-080-03 — Construction Work Package (Inlet Compressors)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-080-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-080` (Inlet Compressors) |
| WBS | 02 (Mechanical) |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| DeliverableNarrative | Mandatory EPC Integrator deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. (Source: DELIVERABLE_REGISTER.csv row 362) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment basis | Two identical parallel sour-inlet-gas reciprocating compressor packages (2 x 50%, no installed spare) | SCOPE_LEDGER.csv SOW-0120, SOW-0122; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §inlet compression |
| Equipment make/model basis | Two Ariel KBZ/6 separable reciprocating compressor packages, two-stage with intercooling and aftercooling | SCOPE_LEDGER.csv SOW-0121 |
| Equipment tags | KM-2150, KM-2250 (compressor motor tags) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §prime movers / §electrical |
| Modularization | Modular self-framing buildings; shop-assembled; disassembled into three pieces for transport and field installation | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §inlet compression |
| Drive basis | 4,000 V, three-phase, 60 Hz electric motor, 3,878 kW / 5,200 hp each, with starting VFD (SCA-001 VE #34) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §electrical/§prime movers |
| Materials | NACE-compliant materials and seals required (sour service) | SCOPE_LEDGER.csv SOW-0122 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour inlet gas (approx. 0.296 mol% H2S per compressor composition table) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §inlet compressor process basis |
| Per-unit flow | Approximately 40 MMSCFD | SCOPE_LEDGER.csv SOW-0122; DBM §inlet compression |
| Combined flow | Approximately 80 MMSCFD | SCOPE_LEDGER.csv SOW-0122 |
| Suction pressure (basis) | Approximately 1275 kPag | SCOPE_LEDGER.csv SOW-0122 |
| Discharge pressure (basis) | Approximately 6550 kPag | SCOPE_LEDGER.csv SOW-0122 |
| Installation environment | Self-framing modular buildings on prepared foundations | DBM §inlet compression; ASSUMPTION: site civil/foundation specifics TBD pending site plan |
| Field environment (temperature, snow, wind, seismic) | location TBD | Workbook Packages row 66; 26020-Package_Requirements.docx package heading 33 |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction scope items (this deliverable participates in) | SOW-0119; SOW-0120; SOW-0121; SOW-0122 | DELIVERABLE_REGISTER.csv row 362 |
| Required physical interfaces (facility integration) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER.csv rows 512-524; PACKAGE_REGISTER.csv row 66 |
| Construction artifacts (anticipated) | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row 362 |
| Companion EPC anchors | DEL-080-01 Scope of Work; DEL-080-02 Package Datasheet | DELIVERABLE_REGISTER.csv rows 360-361 |
| Companion vendor scope (informs construction interface) | DEL-080-04 Vendor Engineered Equipment Package; DEL-080-05 Vendor Document Turnover Package; DEL-080-06 EPC Vendor Package Review and Acceptance | DELIVERABLE_REGISTER.csv rows 363-365 |
| Foundation/structural loads | TBD (depends on vendor package weights and dynamic loads from DEL-080-04) |
| Lift plans, rigging studies | TBD (depends on module split and site access) |
| Required permits and authorizations | TBD (jurisdictional permits not stated in accessible sources) |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row 362)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row 66, PKG-080)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (rows 120-123)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` (rows 512-524)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (inlet compression / prime movers / electrical sections)
- Decomposition narrative: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md` (lines 118, 124, 127)
- Workbook Packages row 66; 26020-Package_Requirements.docx package heading 33 (binary source; located at `_Sources/26020-Package_Requirements.docx`; clause-level text not directly extracted in this run — `location TBD` at clause level)
