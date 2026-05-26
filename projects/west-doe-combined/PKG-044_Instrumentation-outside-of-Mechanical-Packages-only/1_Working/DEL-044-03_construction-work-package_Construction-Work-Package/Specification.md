# Specification — DEL-044-03 Construction Work Package

## Scope

This specification governs the content of the Construction Work Package deliverable for PKG-044 "Instrumentation (outside of Mechanical Packages only)". The deliverable shall describe how the instrumentation package will be physically installed, built, inspected, turned over, and tied into the larger facility systems (DELIVERABLE_REGISTER.csv row 246).

**Included:** Construction-phase planning, installation methodology, tie-in execution, construction interface management, inspection, and turnover evidence for instrumentation scope outside of Mechanical Packages.

**Excluded:** Vendor-supplied mechanical package construction scope (covered in their respective PKGs); package-specific exclusions are TBD — no package-specific exclusions are stated in source materials (PACKAGE_REGISTER.csv row 46).

## Requirements

| Req ID | Requirement | Source / Label |
|---|---|---|
| REQ-044-03-01 | The Construction Work Package shall describe physical installation, build, inspection, turnover, and tie-in of the package to the larger facility systems. | DELIVERABLE_REGISTER.csv row 246 |
| REQ-044-03-02 | The deliverable shall include a construction work package narrative (artifact ART-98EDB38A63). | ARTIFACT_REGISTER.csv row 979 |
| REQ-044-03-03 | The deliverable shall include an installation and tie-in workface plan covering connections to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable (artifact ART-48F9265F2F). | ARTIFACT_REGISTER.csv row 980 |
| REQ-044-03-04 | The deliverable shall include a construction interface and turnover checklist covering construction-facing interface, tie-in, inspection, and turnover evidence (artifact ART-C05FF15A97). | ARTIFACT_REGISTER.csv row 981 |
| REQ-044-03-05 | The installation and tie-in workface plan shall address each declared package interface type: Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, and Communications / Network. | INTERFACE_REGISTER.csv rows 302-306; PACKAGE_REGISTER.csv row 46 |
| REQ-044-03-06 | Instrumentation field supports, power, and communications shall be carried as in-scope per the Gate 6 disposition: "instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy." | INTERFACE_REGISTER.csv rows 302-306 |
| REQ-044-03-07 | Responsibility assignment in the construction work package shall be source-grounded; no separate vendor-package ownership model shall be inferred without source support. | PACKAGE_REGISTER.csv row 46 |
| REQ-044-03-08 | The construction work package shall preserve traceability to SOW-0045 and to supported objectives OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-010. | DELIVERABLE_REGISTER.csv row 246; SCOPE_LEDGER.csv row 46 |
| REQ-044-03-09 | Construction methodology that requires design values, lift plans, weights, or equipment counts shall cite the underlying source slice (Workbook Packages row 46 or DBM section) or be marked TBD with location TBD. | ASSUMPTION (source-fidelity convention); no source slice currently in deliverable folder |
| REQ-044-03-10 | The construction work package shall support operability, maintainability, isolation, winterization, commissioning, and turnover handoff evidence required for facility handoff. | OBJECTIVE_REGISTER.csv row for OBJ-010 (ASSUMPTION: objective-to-deliverable mapping at package level per PACKAGE_HEURISTIC) |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| Workbook Packages row 46 (26020-Packages_Interfaces_4_export.xlsx) | Authoritative package definition, discipline, WBS, applicable interface types | location TBD (workbook row not extracted to deliverable folder) |
| DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | Design basis context for the 03-25 facility scope | location TBD (referenced by PACKAGE_REGISTER row 46) |
| DBM-Deepcut/4-25_Deepcut_DBM.md SEC-13/SEC-14 | Controls topology, instrumented protection basis — context for instrumentation construction tie-ins | location TBD (referenced by OBJ-006) |
| 26020-Package_Requirements.docx | Vendor document and package requirements basis for turnover evidence | location TBD (referenced by OBJ-010) |
| Construction-execution codes/standards (e.g., ABSA, CSA, ASME, applicable provincial regulations) | ASSUMPTION: likely applicable to oil-and-gas facility construction in Western Canada context. Clause-level requirements TBD pending source confirmation. | location TBD |

## Verification

| Req ID | Verification approach |
|---|---|
| REQ-044-03-01 | Document review confirms presence of installation, build, inspection, turnover, and tie-in narrative sections. |
| REQ-044-03-02 | Document review confirms presence of ART-98EDB38A63 construction work package narrative. |
| REQ-044-03-03 | Document review confirms workface plan covers tie-ins to process, utility, electrical, controls, civil, structural, and safety systems as applicable. |
| REQ-044-03-04 | Document review confirms construction interface and turnover checklist is present and addresses interface, tie-in, inspection, and turnover evidence. |
| REQ-044-03-05 | Trace matrix maps each interface row (IFC-A0182B4C75, IFC-9E42D79051, IFC-0DD8B45540, IFC-20C7248CDB, IFC-0664000480) to a workface-plan section. |
| REQ-044-03-06 | Workface plan and turnover checklist explicitly account for instrumentation field supports, power, and communications inclusion. |
| REQ-044-03-07 | Responsibility table cross-references PACKAGE_REGISTER row 46 ownership note. |
| REQ-044-03-08 | Traceability matrix shows SOW-0045 and listed objectives mapped to deliverable sections. |
| REQ-044-03-09 | Source-citation check: every numeric/design value carries a source reference or `TBD (location TBD)`. |
| REQ-044-03-10 | Turnover checklist covers commissioning/turnover and open-item closure evidence aligned to OBJ-010. |

## Documentation

The deliverable comprises the following anticipated artifacts (DELIVERABLE_REGISTER.csv row 246; ARTIFACT_REGISTER.csv rows 979-981):

- Construction work package (ART-98EDB38A63)
- Installation and tie-in workface plan (ART-48F9265F2F)
- Construction interface and turnover checklist (ART-C05FF15A97)

Supporting deliverable-local documents in this folder:

- `Datasheet.md`
- `Specification.md` (this document)
- `Guidance.md`
- `Procedure.md`
