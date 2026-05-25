# Guidance: DEL-024-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis and the DBM Construction Responsibility basis for `PKG-024` into a source-supported installation, tie-in, inspection, and turnover plan for the MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD package. It is the EPC Integrator's mandatory Gate 5 anchor document for how the package becomes physically integrated into the West Doe Deepcut expansion facility.

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat the six workbook interface `X` facts as the authoritative interface profile for construction planning.
- Keep vendor-owned package engineering with the Package Vendor, facility integration with the EPC Integrator, and field execution with Tourmaline per the DBM Construction Responsibility section.
- Use `TBD` for installation location, driven-motor identity, tie-in coordinates, foundation details, cable schedules, and detailed turnover checklist content until source-supported package-specific data is available.
- Use the DBM only at the level it supports: facility-wide construction scope, MV VFD housing context (electrical buildings), grounding/bonding basis, cable tray/conduit routing, and area-classification marking for VFD-fed motors.

## Considerations

The DBM Construction Responsibility section provides a strong, enumerated list of Tourmaline field-scope activities (grading and foundations, setting modules and equipment, mechanical hookup, shipped-loose installation, miscellaneous structural supports, home-run cables, electrical terminations, area lighting, and demolition where required). The Construction Work Package for `PKG-024` should map each applicable item against the package's physical scope rather than re-deriving construction scope from first principles.

The DBM electrical section notes that "VFD and soft-starter requirements for 4.16 kV motors are TBD" at the DBM level. Construction planning therefore cannot assume specific starting-method behaviors, harmonic-filter inclusions, or transformer configurations; these must come from vendor data at detailed engineering. The DBM also notes that MV VFDs may be housed in prefabricated electrical buildings; the installation location is not assigned.

Tie-ins are explicitly handled as external interface responsibility markers in the DBM, with per-tie-in responsibility to be confirmed. The Construction Work Package should make this explicit for the MV feeder tie-in, the I&C/control cabling tie-in to the plant PLC, the network tie-in, and the grounding tie-in to the facility ground grid.

The driven motor is not unambiguously identified in the accessible source set. DBM Section paragraphs mention 4.16 kV motors (e.g., the Ariel KBC/6 inlet/sales compressor frame uses a Starting VFD at 6,700 hp basis, which is materially different from this package's 2000 HP basis) and other 4 kV applications, but no source slice anchors the PKG-024 2000 HP driven motor to a specific service. Construction planning should treat motor identity as `TBD` and not pre-commit to a service-specific tie-in or maintenance-access envelope.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Installation location | Mark `TBD`; do not pre-commit to a specific electrical building. | DBM says MV VFDs may be housed in prefabricated electrical buildings but does not locate PKG-024. |
| Driven motor identity | Mark `TBD`; do not infer 2000 HP service. | Workbook name states ratings but no source slice maps this VFD to a specific motor service. |
| Tie-in responsibility | Carry each tie-in as a row with responsibility `TBD` or assigned, per the DBM external-interface basis. | DBM Construction Responsibility treats ISBL/OSBL tie-ins as items requiring per-tie-in confirmation. |
| Turnover checklist content | Provide structural section headings only; mark detailed line items as `TBD` pending vendor data. | The package-specific Word requirements source did not produce a PKG-024 match during this run. |
| Area-classification marking | Require if Zone 2; otherwise treat as not applicable. | DBM area-classification rule applies to VFD-fed motors in Zone 2 areas; the motor's area is `TBD`. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations `TBD`. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable construction-scope entry: "Setting of the VFD module/skid on foundations is Tourmaline field construction scope. Source: DBM Construction Responsibility section."
- Acceptable tie-in entry: "MV feeder tie-in to the VFD input: responsibility `TBD`; joint planning required (DBM external-interface marker)."
- Acceptable source-gap entry: "Installation location: `TBD`. No package-specific source slice assigns PKG-024 to a building or area."
- Not acceptable without new source: "VFD is installed in the main electrical building, room 200, on the south wall." The accessible source set does not establish this value.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-024-03-001 | The 2000 HP, 4.16 kV driven-motor service is not identified in the accessible source set; DBM mentions 4.16 kV motor starting as `TBD` and references unrelated MV motor services (e.g., 6,700 hp Ariel inlet/sales compressor with Starting VFD). | Workbook Packages row 26 (package name lists 2000 HP, 4160 V) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph and inlet/sales compressor paragraphs | Datasheet Construction; Specification Requirements; Procedure Steps | Treat driven-motor identity as `TBD` until vendor data or process/electrical study assigns it; do not pre-commit construction details that depend on motor identity. | TBD |
| HRR-024-03-002 | No package-specific requirements document slice was found for PKG-024 in `26020-Package_Requirements.docx`; detailed construction turnover checklist content cannot be source-anchored. | `_Sources/26020-Package_Requirements.docx` (no PKG-024 match observed) | `_CONTEXT.md` Anticipated Artifacts (lists turnover checklist as required artifact) | Specification Requirements (REQ-024-03-009); Procedure Steps | Provide checklist structural skeleton only; mark detailed line items `TBD` and obtain vendor-supplied content at detailed engineering. | TBD |
| HRR-024-03-003 | Installation location for the MV VFD is not assigned by the accessible source set; DBM electrical-buildings paragraph lists MV VFDs as possible occupants but does not locate PKG-024. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph | Workbook Packages row 26; `PACKAGE_REGISTER.csv` row `PKG-024` | Datasheet Construction; Specification Requirements; Procedure Steps | Keep installation location `TBD`; allow detailed design / plot plan to assign building, room, or outdoor location. | TBD |
