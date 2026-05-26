# Specification — DEL-104-03 Construction Work Package

## Scope

**In scope.** This specification governs the EPC Integrator's Construction Work Package for `PKG-104` "Structural steel - outside of modules" (WBS 01, workbook row 105, CoA 26020-01-36-004). It defines how the package's structural steel scope located outside of modules — including connections, supports, and tie-ins to adjacent grading/foundation work — will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The Construction Work Package shall produce:

- a Construction Work Package document (`ART-9478B627E2`),
- an installation and tie-in workface plan (`ART-A0BC38D152`), and
- a construction interface and turnover checklist (`ART-8131641C3B`).

Sources: `ARTIFACT_REGISTER.csv` rows for DEL-104-03; `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-104-03 row.

**Out of scope.** Detailed structural member design, IFC drawings, fabrication shop drawings, and discipline production deliverables are produced by `DEL-104-04` (EPC/Structural Discipline Production Package) and other discipline deliverables. Package scope of work and tagged-equipment basis are in `DEL-104-01`. Package datasheet and vendor handoff data are in `DEL-104-02`. Process-side equipment within modules is covered by other packages.

## Requirements

Numbered requirements (REQ-104-03-NN). Each requirement is grounded in a source slice or labelled ASSUMPTION.

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-104-03-01 | Construction execution shall follow the project's Construction Responsibility model: Tourmaline Oil Corporation performs field construction including grading, piling and foundation work, setting modules/pipe racks/equipment on foundations, mechanical hookup of modules and interconnecting piping, and installation of miscellaneous structural supports. | `4-25_Deepcut_DBM.md` Construction Responsibility |
| REQ-104-03-02 | Structural steel furnished and erected under this package shall conform to CSA G40.20/G40.21 350W for W-flange and HSS sections, and 300W for channels, plates, and angles. | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| REQ-104-03-03 | Structural steel design and fabrication compliance shall be verified against CAN/CSA-S16, Design of Steel Structures (latest edition). | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| REQ-104-03-04 | Concrete used for foundation interfaces under this package (e.g., precast pile caps, bearing concrete) shall comply with CAN/CSA A23.3 (design) and CSA A23.1/A23.2 (materials, construction, testing). | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| REQ-104-03-05 | The Construction Work Package shall identify and plan the installation interface with grading/site drainage/spill containment (`IFC-CCDE4B56CA`) and with structural/foundations/supports (`IFC-ECDD4D3A15`) and shall coordinate workface sequencing across these interfaces. | `INTERFACE_REGISTER.csv` PKG-104 rows |
| REQ-104-03-06 | Foundation tie-in for outside-of-module structural steel shall default to driven steel piles consistent with the project's piles-and-foundations basis, unless detailed engineering documents an alternate support basis for a specific structure. | `4-25_Deepcut_DBM.md` Piles and Foundations |
| REQ-104-03-07 | Site grading adjacent to installed structural steel and supporting pipe-rack steel shall preserve the project grading basis: high equal-elevation ridges along main pipe racks, pad slopes from pipe racks at 1.5% per side (1.0% allowed where top-of-pile-cap dictates), and the project ditch/culvert slope minima. | `4-25_Deepcut_DBM.md` Site Grading and Surface Water Management |
| REQ-104-03-08 | The Construction Work Package shall plan ISBL/OSBL tie-in execution under joint Tourmaline/EPC planning; responsibility for each interconnecting-piping tie-in to ISBL/OSBL shall be confirmed before construction. | `4-25_Deepcut_DBM.md` Construction Responsibility |
| REQ-104-03-09 | The Construction Work Package shall preserve layout access for operations, maintenance, emergency response, modular installation/erection, and hazardous-area separation, and shall not foreclose future plot provisions. | `4-25_Deepcut_DBM.md` General Layout Basis; Minimum Spacing Criteria |
| REQ-104-03-10 | The Construction Work Package shall include a construction interface and turnover checklist that documents installation completion, interface verification, and handoff to commissioning consistent with `OBJ-010` (operability/maintainability/sparing/isolation/winterization/vendor-documentation/commissioning/turnover/controlled open-item closure). | `OBJECTIVE_REGISTER.csv` OBJ-010; `ARTIFACT_REGISTER.csv` `ART-8131641C3B` |
| REQ-104-03-11 | The Construction Work Package shall not finalize foundation, grading, or pile-design values until the project geotechnical report is issued; affected items remain TBD pending geotechnical confirmation. | `4-25_Deepcut_DBM.md` Geotechnical and Topographical Assumptions |
| REQ-104-03-12 | ASSUMPTION: An Inspection and Test Plan (ITP) keyed to CAN/CSA-S16 fabrication, erection tolerances, bolting, and welding shall be included or referenced in the Construction Work Package. No package-specific ITP requirement is stated in the accessible source slices; this is an EPC convention pending confirmation. | ASSUMPTION (no source) |

## Standards

| Standard / Code | Applicability | Source slice |
|---|---|---|
| National Building Code of Canada (latest edition) | Building loading and egress applicable to ancillary buildings/structures within or supporting the package | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis; Buildings and Miscellaneous Facilities |
| CAN/CSA-S16 | Steel structure design | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| CAN/CSA A23.3 | Concrete design | same |
| CSA A23.1 / A23.2 | Concrete materials, construction, testing | same |
| CSA G40.20 / G40.21 | Structural steel materials (350W W-flange/HSS; 300W channel/plate/angle) | same |
| Canadian Foundation Engineering Manual | Foundation engineering reference | same |
| Project-specific procedures (welding, bolting, NDE, surveying, lift planning) | Detailed construction execution | location TBD — not present in accessible source slices |
| `26020-Package_Requirements.docx` | Vendor/package documentation requirements (referenced by `OBJ-010`) | location TBD — file present in `_Sources` index but not opened as source slice in this run |

## Verification

| Requirement | Verification Method | Records |
|---|---|---|
| REQ-104-03-01 | Review against project Construction Responsibility matrix; signoff by EPC Integrator and Tourmaline field construction | Responsibility signoff record |
| REQ-104-03-02 | Mill test reports (MTRs) for each heat; material verification at receiving | MTR file; receiving inspection record |
| REQ-104-03-03 | Design package and fabrication review against CAN/CSA-S16; structural inspector signoff during erection | Design review record; erection inspection log |
| REQ-104-03-04 | Concrete mix submittals, cylinder break tests, batch tickets per CSA A23.1/A23.2 | Concrete test records |
| REQ-104-03-05 | Interface checklist closed out for `IFC-CCDE4B56CA` and `IFC-ECDD4D3A15` prior to turnover | Interface checklist |
| REQ-104-03-06 | Pile installation records (driving logs, set/PDA where applicable) and as-built pile coordinates | Pile installation log; as-built record |
| REQ-104-03-07 | Site survey verification of finished grades against grading plan | Grading as-built survey |
| REQ-104-03-08 | Tie-in responsibility confirmation log per ISBL/OSBL tie-in, signed by Tourmaline and EPC | Tie-in responsibility log |
| REQ-104-03-09 | Layout walk-down to confirm access envelopes preserved | Walk-down record |
| REQ-104-03-10 | Turnover checklist executed; open-item register reconciled | Turnover record; open-item register |
| REQ-104-03-11 | Geotechnical report received and reviewed; affected TBDs closed before construction of impacted items | Geotechnical review record |
| REQ-104-03-12 | ITP executed; hold/witness points recorded | ITP records (ASSUMPTION — pending confirmation that ITP is the binding mechanism) |

## Documentation

Required documentation deliverables for DEL-104-03:

- Construction Work Package document (`ART-9478B627E2`)
- Installation and tie-in workface plan (`ART-A0BC38D152`)
- Construction interface and turnover checklist (`ART-8131641C3B`)
- ITP / inspection records, MTRs, weld and NDE records, concrete test records, pile driving logs, grading and tie-in as-builts (TBD — specific document register not enumerated in accessible source slices; ASSUMPTION based on project conventions and OBJ-010 handoff evidence requirements)
