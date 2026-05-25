# Datasheet — DEL-018-05 Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-018-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-018-05` |
| Parent Package | `PKG-018` — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-018` |
| Workbook Row | 20 (Workbook Packages) | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Scope Item Covered | `SOW-0019` | `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (ASSUMPTION — package-grouping heuristic) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment tag | `26020-02-30-009` | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Package equipment description | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | `PACKAGE_REGISTER.csv` |
| WBS | `02` | `PACKAGE_REGISTER.csv` |
| Package ownership boundary | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration and interfaces. | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Applicable interface types | Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports | `PACKAGE_REGISTER.csv` |
| Source basis for vendor documentation requirements | "Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers." | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Mechanical packages organization paragraph) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Driven-equipment service basis (context for the VFD package) | Two electric-drive separable reciprocating inlet compressor packages, ~40 MMSCFD each, no installed spare. Each driven by a 4,000 V, 3φ, 60 Hz electric motor rated 3,878 kW / 5,200 hp, NEMA MG1, TEFC/WPII, Class F insulation/Class B rise, ~891 rpm 8-pole, continuous inverter duty, supplied with starting VFD under SCA-001 VE #34. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Electric Driver and Starting Basis; Electric-Drive Compression Basis) |
| Medium-voltage system basis | 4,160 V, 3-phase, 3-wire, 60 Hz LRG; serves process AC inverter-drive motors from 250 hp to 5,500 hp. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Medium-voltage service row) |
| Capacitor bank/harmonics constraint | SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present; harmonic and reactive-power mitigation by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Minimum ambient design driver | -40 °C governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (site basis paragraph) |
| Submittal package contents (per source) | Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating/design envelopes, sparing philosophy, materials/coating basis, maintenance access, shipped-loose item lists, vendor document register. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |

## Construction (Composition of the Turnover Package)

| Element | Description | Source |
|---|---|---|
| Vendor document register | Indexed register listing all vendor documents (drawings, datasheets, certifications, manuals, test reports) for `PKG-018`. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` |
| Vendor document submittals | Controlled submittals of each registered vendor document. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Source-required vendor documentation rows as evidence | Individual rows from the source vendor document table carried as artifacts where available (not as separate deliverables). | `DELIVERABLE_REGISTER.csv` (Notes column) |
| Turnover records | Records demonstrating turnover of the documentation set to the EPC Integrator. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Specific document classes (typical for an MV VFD package) | TBD — locally accessible source slices do not enumerate the vendor document classes for this specific MV VFD package; the package-requirements workbook (`26020-Package_Requirements.docx`) is referenced but no package-row match for `PKG-018` was located in PREPARATION. | `_REFERENCES.md` (Missing/Deferred); `_Sources/.../3-25_Comp_and_Liquids_DBM.md` (silent on per-package vendor doc list) |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- `_DEPENDENCIES.md` (this deliverable)
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (row `DEL-018-05`)
  - `PACKAGE_REGISTER.csv` (row `PKG-018`)
  - `ARTIFACT_REGISTER.csv`
  - `INTERFACE_REGISTER.csv`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Electric Driver and Starting Basis; Electric-Drive Compression Basis; MV service; mechanical-packages organization paragraph)
- `_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md` (compressor-driver evidence rows)
- Workbook Packages row 20 (cited authority; not directly read in this run)
- `PKG-018/26020-Package_Requirements.docx` (referenced authority; no per-package vendor-document slice located during PREPARATION — `location TBD`)
