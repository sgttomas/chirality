# Datasheet: DEL-091-06 — EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-091-06_epc-vendor-package-review-and-acceptance |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | PKG-091 |
| PackageName | Tank Farm Pump Building 3-25 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| DeliverableArtifactClass | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package served | Tank Farm Pump Building, 03-25 Liquids Hub tank farm pump systems | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Liquids Hub equipment basis) |
| Pumps in scope (representative) | Condensate booster pumps P-9211-2 / P-9221-2 (2 x 100%); three condensate loading pumps; produced-water transfer pumps (2 x 100%); sour condensate recycle; condensate skim; product recycle; sales condensate booster | `3-25_Comp_and_Liquids_DBM.md` lines 40, 412-414, 526, 575-583 |
| Driver type | Electric motor driven (loading pumps; VRU drivers electric; ASSUMPTION other pump building drivers electric pending vendor confirmation) | `3-25_Comp_and_Liquids_DBM.md` line 526; ASSUMPTION |
| Booster pump duty | 165 m3/h at 35 m TDH per pump | `3-25_Comp_and_Liquids_DBM.md` line 413 |
| Loading pump arrangement | One loading pump per truck-loading station (three stations) | `3-25_Comp_and_Liquids_DBM.md` lines 414, 526, 654 |
| LACT interface | Facility-side tie-in only; LACT equipment is third-party NRM scope | `3-25_Comp_and_Liquids_DBM.md` lines 54, 417 |
| Covered SOW items | SOW-0185, SOW-0186, SOW-0187, SOW-0188 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | OBJ-002 through OBJ-010 | `_CONTEXT.md` (PACKAGE_HEURISTIC, ASSUMPTION) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | `3-25_Comp_and_Liquids_DBM.md` line 85 |
| Site elevation | 673 m AMSL | `3-25_Comp_and_Liquids_DBM.md` line 686 |
| Design ambient temperature | -40 deg C to +35 deg C | `3-25_Comp_and_Liquids_DBM.md` line 686 |
| Sour service classification | Sour (sour gas / sour produced water present in adjacent systems) | `3-25_Comp_and_Liquids_DBM.md` (sec scope) |
| Acceptance criteria documentation set | EPC Scope of Work (DEL-091-01), Package Datasheet (DEL-091-02), Construction Work Package (DEL-091-03) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Construction

| Item | Value | Source |
|---|---|---|
| Building type | Pump building enclosure (modular / self-framing assumed consistent with package modularization convention) | ASSUMPTION based on `3-25_Comp_and_Liquids_DBM.md` line 294 modularization convention; package-level details TBD pending `26020-Package_Requirements.docx` heading 44 |
| Vendor production unit | DEL-091-04 Vendor Engineered Equipment Package | `DELIVERABLE_REGISTER.csv` |
| Vendor turnover unit | DEL-091-05 Vendor Document Turnover Package | `DELIVERABLE_REGISTER.csv` |
| Acceptance evidence artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Inspection/test scope detail | TBD — to be drawn from vendor's `DEL-091-05` register and source `26020-Package_Requirements.docx` heading 44 (location TBD) | TBD |

## References

- `_REFERENCES.md` (deliverable-local)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` (package heading 44; not locally accessible as text — location TBD)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` (workbook Packages row 84; not locally accessible as text — location TBD)
- Gate 7 PROJECT_DECOMP snapshot deliverable / package / objective registers
- Sibling deliverables: DEL-091-01, DEL-091-02, DEL-091-03 (EPC anchors); DEL-091-04, DEL-091-05 (vendor inputs)
