# Datasheet: DEL-061-03 — Construction Work Package (NGL Booster and Transfer Pumps Building)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-061-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-061` (NGL Booster and Transfer Pumps Building) |
| ParentWorkbookID | 61 |
| WBS | 01 (Mechanical) |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| DeliverableNarrative | Mandatory EPC Integrator deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. (Source: DELIVERABLE_REGISTER.csv row for DEL-061-03) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment basis | Two LPG booster pumps arranged in parallel for transfer from LPG storage to the LACT unit where booster pressure may be required | SCOPE_LEDGER.csv SOW-0150; 26020-Package_Requirements.docx package heading 17 (Basic scope) |
| Equipment tags | P-9570-1, P-9580-1 (LPG booster pumps) | DBM-Deepcut/4-25_Deepcut_DBM.md row 2609 (NGL Booster and Transfer Pumps Building) |
| Equipment type | Vertical multistage can-type pumps, API 610 | SCOPE_LEDGER.csv SOW-0151; DBM-Deepcut/4-25_Deepcut_DBM.md row 2609 |
| Seal plan | API 610 seal plan 13/52 | SCOPE_LEDGER.csv SOW-0151 |
| Drive basis | 575 V / 3 phase / 60 Hz motors | SCOPE_LEDGER.csv SOW-0151 |
| Sparing philosophy | 2 x 100% (200% installed); no installed spare beyond the parallel pair | DBM-Deepcut/4-25_Deepcut_DBM.md row 2338 (C3/C4 LPG LACT Booster Pump 2 x 100%); ASSUMPTION: the PKG-061 "booster" pump pair corresponds to the C3/C4 LPG LACT Booster Pump entry in the DBM sparing table |
| Skid scope (vendor) | Structural skid, package piping, instrumentation, electrical, HVAC / enclosure, CRN/TSBC as applicable, and commissioning support | SCOPE_LEDGER.csv SOW-0151 |
| Modularization | Shop-assembled vendor module: "950-1 LPG Booster and Transfer Pump Module" (inventory label) | DBM-Deepcut/4-25_Deepcut_DBM.md row 2818 |
| Materials (sour/LPG service specifics) | TBD — not stated for PKG-061 in accessible source slices (NACE-class requirements appear elsewhere in DBM but are not asserted for this package). |
| Inclusions outside vendor scope | DCS integration, foundations, and electrical supply to MCC are by others | SCOPE_LEDGER.csv SOW-0152 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | LPG transfer from LPG storage to the LACT unit (where booster pressure may be required) | SCOPE_LEDGER.csv SOW-0150 |
| Per-pump flow basis | 145 m3/h each at 150% capacity | SCOPE_LEDGER.csv SOW-0152 |
| Booster differential pressure | 25 psid / 172 kPad | SCOPE_LEDGER.csv SOW-0152 |
| Total Dynamic Head (TDH) | TBD (open item in source) | SCOPE_LEDGER.csv SOW-0152 ("TBD TDH") |
| Installation environment | Vendor-supplied building/enclosure on EPC-supplied foundation | SCOPE_LEDGER.csv SOW-0151 (HVAC/enclosure); SOW-0152 (foundations by others); ASSUMPTION: pump-building boundary follows standard package skid + building delivery pattern |
| Field environment (temperature, snow, wind, seismic) | location TBD | Workbook Packages row 75; 26020-Package_Requirements.docx package heading 17 (binary source not extracted at clause level in this run) |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction scope items (this deliverable participates in) | SOW-0149; SOW-0150; SOW-0151; SOW-0152 | DELIVERABLE_REGISTER.csv row for DEL-061-03 |
| Required physical interfaces (facility integration) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row for PKG-061 (Applicable interface types) |
| Construction artifacts (anticipated) | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row for DEL-061-03; `_CONTEXT.md` Anticipated Artifacts |
| Companion EPC anchors | DEL-061-01 Scope of Work; DEL-061-02 Package Datasheet | DELIVERABLE_REGISTER.csv rows for DEL-061-01/02 |
| Companion vendor scope (informs construction interface) | DEL-061-04 Vendor Engineered Equipment Package; DEL-061-05 Vendor Document Turnover Package; DEL-061-06 EPC Vendor Package Review and Acceptance | DELIVERABLE_REGISTER.csv rows for DEL-061-04/05/06 |
| Foundation / structural loads | TBD (depends on vendor package weights and dynamic loads from DEL-061-04) |
| Lift plans, rigging studies | TBD (depends on module split and site access) |
| Required permits and authorizations | TBD (jurisdictional permits not stated in accessible sources) |
| EHT and freeze protection | TBD at construction level; EHT is a listed package interface (PACKAGE_REGISTER.csv row for PKG-061) |
| Hazardous area classification at building boundary | TBD (LPG service implies classified area but source clause not extracted in this run; `location TBD` in 26020-Package_Requirements.docx package heading 17) |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row for DEL-061-03)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row for PKG-061)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (SOW-0149, SOW-0150, SOW-0151, SOW-0152)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` (PKG-061 rows)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (NGL Booster and Transfer Pumps Building rows 2548, 2609, 2818; sparing tables row 2338-2339; transfer pump narrative rows 1673-1679 used only as informing context)
- Decomposition narrative: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
- Workbook Packages row 75; 26020-Package_Requirements.docx package heading 17 (binary source located at `_Sources/26020-Package_Requirements.docx`; clause-level text not directly extracted in this run — `location TBD` at clause level)
- Word source basis: `Bid Docs/Budgetary/26020-01-PT-18-004-LPG-Booster.pdf` (not locally extracted; `location TBD`)
