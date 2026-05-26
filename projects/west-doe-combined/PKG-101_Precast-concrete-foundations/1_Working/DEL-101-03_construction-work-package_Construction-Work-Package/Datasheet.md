# Datasheet — DEL-101-03 Construction Work Package (PKG-101 Precast Concrete Foundations)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-101-03_construction-work-package | `_CONTEXT.md` Identity |
| Name | Construction Work Package | `_CONTEXT.md` Identity |
| ParentPackageID | PKG-101 | `_CONTEXT.md` Identity |
| ParentWorkbookID | 101 | `_CONTEXT.md` Identity |
| PackageName | Precast concrete foundations | `_CONTEXT.md` Identity |
| Discipline | Structural | `_CONTEXT.md` Identity |
| Type | EPC Construction Work Package | `_CONTEXT.md` Identity |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` Identity |
| Decomposition Row | Workbook Packages row 102 | `_CONTEXT.md` Source Reference |
| Covers Scope Item | SOW-0257 | `_CONTEXT.md` Covers Scope Items |
| Supports Objectives | OBJ-001, OBJ-008, OBJ-010 | `_CONTEXT.md` Supports Objectives |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Anticipated artifact: Construction work package | ART-384DBDF766 — Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems | `ARTIFACT_REGISTER.csv` row for DEL-101-03 |
| Anticipated artifact: Installation and tie-in workface plan | ART-674B3EBE60 — Workface planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable | `ARTIFACT_REGISTER.csv` row for DEL-101-03 |
| Anticipated artifact: Construction interface and turnover checklist | ART-37A6123862 — Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package | `ARTIFACT_REGISTER.csv` row for DEL-101-03 |
| Workbook-declared interface (Grading / Site Drainage / Spill Containment) | IFC-26343B703C — declared YES for PKG-101 | `INTERFACE_REGISTER.csv` line 905 |
| Workbook-declared interface (Structural / Foundations / Supports) | IFC-BED3DE4194 — declared YES for PKG-101 | `INTERFACE_REGISTER.csv` line 906 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site ambient — design minimum temperature | -40 deg C governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies | DBM-Comp_and_Liquids §"Site basis" line 145; same basis is consistent with DBM-Deepcut SEC-11 |
| Geotechnical input | Foundation selection, pile design, settlement criteria, frost protection, site preparation, and structural support requirements shall be confirmed against the final geotechnical report; until accepted, geotechnical values are design placeholders, not closed construction criteria | DBM-Comp_and_Liquids §Civil/Structural line 141 |
| Building/structural codes | Buildings engineered for project-site snow, rain, wind, and seismic loading per National Building Code of Canada; egress per NBC | DBM-Deepcut SEC-11 §Buildings and Miscellaneous Facilities |
| Foundation engineering basis | Canadian Foundation Engineering Manual | DBM-Deepcut SEC-11 §Governing Codes table |
| Default support basis | Driven steel piles for buildings, equipment, towers, tanks, modules, pipe racks unless a more specific foundation basis applies or detailed engineering confirms otherwise | DBM-Deepcut SEC-11 §Piles and Foundations |

## Construction (named precast-concrete elements supported by sources)

| Element | Foundation Basis | Open Requirement | Source |
|---|---|---|---|
| Transformers | Generally supported on precast concrete bearing foundations | None identified | DBM-Deepcut SEC-11 §Piles and Foundations table |
| Compressors | Precast concrete block supported on driven steel piles, subject to dynamic analysis | Dynamic analysis results are TBD | DBM-Deepcut SEC-11 §Piles and Foundations table |
| Compressors — alternate concept | Propak verification of welding steel skid directly to piles (considered unlikely for this compressor size) | Verification is TBD | DBM-Deepcut SEC-11 §Piles and Foundations table |
| Compressor skid/foundation arrangement | Shall consider containment and management of on-skid oil leaks | Detailed arrangement TBD | DBM-Deepcut SEC-11 §Piles and Foundations table |

Per-tag inventories of precast foundations, drawings, embed details, anchor schedules, lift weights, rigging plans, and concrete mix design are **TBD** — not present in the locally accessible sources for PKG-101.

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `ARTIFACT_REGISTER.csv` — Gate 7 snapshot, rows ART-384DBDF766, ART-674B3EBE60, ART-37A6123862
- `INTERFACE_REGISTER.csv` — Gate 7 snapshot, lines 905-906 (PKG-101 interfaces)
- `DELIVERABLE_REGISTER.csv` — Gate 7 snapshot, row DEL-101-03_construction-work-package
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-11 Civil and Structural Basis (Piles and Foundations; Buildings; External Dependencies)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Construction Scope Summary; Civil/Foundations notes
- `_Sources/26020-Package_Requirements.docx` — referenced; location TBD (binary; specific clauses not extracted in this pass)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — referenced; location TBD (binary; row 102 not extracted in this pass)
