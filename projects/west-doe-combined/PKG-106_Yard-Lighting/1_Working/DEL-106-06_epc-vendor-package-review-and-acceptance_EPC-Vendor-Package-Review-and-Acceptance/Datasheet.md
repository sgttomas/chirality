# Datasheet — EPC Vendor Package Review and Acceptance (DEL-106-06)

> Descriptive document. Identification and observable attributes of the EPC Integrator review/acceptance evidence package for the PKG-106 Yard Lighting vendor scope.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-106-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-106` |
| PackageName | Yard Lighting |
| Discipline | Electrical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | SOW-0011 |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC; sourced from `_CONTEXT.md` Supports Objectives) |
| Source Reference | Workbook Packages row 12; 26020-Package_Requirements.docx package heading TBD (location TBD) |

## Attributes

Attributes describe the EPC Integrator review/acceptance evidence package against the vendor-supplied Yard Lighting scope (area/exterior lighting for the West Doe facility).

| Attribute | Value | Source |
|---|---|---|
| Package subject | Yard Lighting — area/exterior LED lighting for the West Doe facility yard (process areas, roads, walkways, pad edges) | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row PKG-106; DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" section (lines 3027-3035) |
| Discipline interfaces present (per workbook row 12) | Electrical Power; Grounding/Bonding; Area/Exterior Lighting | `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` row 12 |
| Fixture technology basis | LED (all lighting), to minimize electrical demand and maintenance | DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" (line 3027) |
| Voltage basis (general purpose lighting) | 120/208 V, fed from nearest power distribution centre | DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" (line 3027) |
| Area-classification suitability | Fixtures shall be suitable for the area classification in which they are installed | DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" (line 3027) |
| Process area / outdoor fixture type | LED fixtures (process area and outdoor lighting) | DBM `4-25_Deepcut_DBM.md` (line 3031) |
| Emergency lighting | LED with battery backup; at least two emergency fixtures per building (where buildings within yard scope) | DBM `4-25_Deepcut_DBM.md` (line 3031) |
| Light-pollution control | LED, selective minimization of exterior lighting to working areas, downward illumination (downcast floodlights), prohibition of horizontally aimed floodlights, photocell or switch control, lighting mast poles located away from pad edge where masts are required | DBM `4-25_Deepcut_DBM.md` (line 3035) |
| Site low-temperature basis | -40 deg C minimum ambient governs exposed equipment, panels, and field devices | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-04 (line 145); DBM `4-25_Deepcut_DBM.md` (cross-reference, location TBD) |
| Lighting as construction-scope item | Area lighting is field-construction scope at the Tourmaline facility; aligned with EPC integrator/EPC vendor split for this package | DBM `4-25_Deepcut_DBM.md` (line 120); DBM `3-25_Comp_and_Liquids_DBM.md` (lines 38, 75) |
| Review lead | EPC Integrator | `_CONTEXT.md` ResponsibleParty |
| Reviewed inputs | Vendor Engineered Equipment Package (DEL-106-04); Vendor Document Turnover Package (DEL-106-05) | DELIVERABLE_REGISTER.csv PKG-106 rows |
| Acceptance baseline | EPC Scope of Work (DEL-106-01); Package Datasheet (DEL-106-02); Construction Work Package (DEL-106-03) | DELIVERABLE_REGISTER.csv PKG-106 rows |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating environment | Outdoor yard; mix of process and non-process areas with varying hazardous-area classifications | DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" (lines 3027, 3031) |
| Ambient temperature envelope | -40 deg C to +35 deg C design envelope governs exposed luminaires, drivers, controls, and field wiring | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-04 (line 145) |
| Area classification | Luminaires must be selected per the area classification of the installed location (hazardous vs non-hazardous; class/division/zone TBD) | DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" (line 3027) |
| Electrical code basis | Canadian Electrical Code (conduit, wiring methods, area-classification compliance) | DBM `4-25_Deepcut_DBM.md` "Cable, Conduit and Lighting" prose (line preceding "Lighting and Receptacles" section; CEC reference) |
| Light-pollution regulatory basis | Regulatory light-pollution requirements (jurisdictional, TBD which regulation) | DBM `4-25_Deepcut_DBM.md` (line 3035) |
| Switching/control basis | Photocell or switch control; interior switches at the door (where buildings within yard scope) | DBM `4-25_Deepcut_DBM.md` (lines 3027, 3035) |
| Acceptance signing authority | Human approver (K-AUTH-1); agent does not certify | Chirality `docs/CONTRACT.md` K-AUTH-1 |

## Construction

The "construction" of this deliverable is an evidence package, not a physical object. It is constituted by the following anticipated artifacts (from `_CONTEXT.md` Anticipated Artifacts):

| Artifact | Description | Form |
|---|---|---|
| Vendor document review log | Per-document review status, comments, and dispositions against vendor submittals delivered under DEL-106-05 | Log (table/CSV or Markdown) |
| Package acceptance checklist | Item-by-item acceptance against EPC SOW (DEL-106-01), Package Datasheet (DEL-106-02), and CWP (DEL-106-03) | Checklist |
| Test/inspection evidence | Records of FAT, SAT, factory photometric tests, area-classification certification, grounding/bonding continuity tests, illumination/uniformity field measurements, energization checks, photocell/control verification, as applicable | Records (vendor + EPC witness) |
| Turnover evidence | Mechanical Completion, Pre-Commissioning, Commissioning/Operational Acceptance records for the yard lighting system | Turnover certificates and supporting records |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable folder)
- Decomposition: GATE-07_Final_Published_2026-05-24 — `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- DBM: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — "Lighting and Receptacles" (lines 3027, 3031, 3035); area lighting as field-construction scope (line 120); cable/conduit/CEC prose preceding the lighting section
- DBM: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — facility lighting in civil/infrastructure scope (line 38); construction-scope area lighting (line 75); -40 deg C ambient basis SEC-04 (line 145)
- Workbook: `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` row 12 (interfaces: Electrical Power, Grounding/Bonding, Area/Exterior Lighting)
- `_Sources/26020-Package_Requirements.docx` package heading for PKG-106 — not text-accessible during this run; content TBD (location TBD)
- Sibling PKG-106 deliverables: DEL-106-01 (SOW), DEL-106-02 (Datasheet), DEL-106-03 (CWP), DEL-106-04 (Vendor Eng. Package), DEL-106-05 (Vendor Document Turnover)
