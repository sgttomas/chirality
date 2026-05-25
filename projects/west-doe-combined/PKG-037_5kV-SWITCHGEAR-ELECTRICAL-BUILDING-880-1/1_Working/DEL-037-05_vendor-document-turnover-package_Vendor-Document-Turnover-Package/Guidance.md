# Guidance: DEL-037-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists to assemble and turn over the vendor-produced documentation for `PKG-037`, the 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) package, in a controlled, register-tracked form that supports EPC Integrator interface/integration review and downstream EPC acceptance (`DEL-037-06`). It should let operations, construction, and EPC integration verify that the vendor has produced and delivered the documents needed to design, fabricate, ship, install, commission, operate, and maintain the package.

## Principles

- Preserve source spelling and identity. The package name is carried as "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)" because that is the workbook and Gate 7 register spelling, including the building identifier "(880-1)."
- Treat workbook interface `X` facts as evidence for what the vendor documentation must address; do not promote interfaces to separate deliverables.
- Keep vendor-owned documentation production with the Package Vendor and EPC interface/integration review with the EPC Integrator; do not absorb the EPC acceptance scope owned by `DEL-037-06`.
- Preserve the source-supported core vendor-document entries (`PRQ-009` Vendor Document Index and `DOC-008` Vendor Document Control Procedure), and use `TBD` for package-specific schema, hold/issue codes, submittal stages, and turnover acceptance criteria until source-supported.
- Treat individual vendor-document rows from source as artifacts/evidence, not as separate deliverables, consistent with `_CONTEXT.md` notes.

## Considerations

The Comp & Liquids DBM source establishes vendor document registers as a required package deliverable for mechanical/equipment packages alongside datasheets, cause-and-effect inputs, utility load summaries, relief/load data, tie-in lists, operating envelopes, sparing, materials/coating basis, maintenance access, and shipped-loose item lists (line 617). That basis supports requiring a vendor document register here even though no PKG-037-specific register schema is published in the accessible source set.

The Deepcut DBM electrical section describes electrical buildings as prefabricated modular buildings that may house 13.8 kV main switchgear, MV MCCs/RVSSs/VFDs, 600 V MCCs, 120 V AC and 125 V DC UPS systems, distribution transformers and panelboards, contactor panels, plant PLC control panels, and network racks. The "5 kV" naming aligns with the project MV cable insulation class (5 kV insulation, 100 percent, for 4.160 kV cables) rather than with a 5 kV bus voltage in isolation; the package basis must be confirmed by vendor documentation and detailed design.

Workbook row 39 lists twelve applicable interfaces, including Electrical Power, Grounding / Bonding, I&C / Control Cabling, Building HVAC / Services, Structural / Foundations / Supports, and Maintenance Access. Vendor documentation must address each interface where vendor scope crosses it. The Package Requirements source provides generic core vendor-document entries, but the absence of a detailed package-specific document index means the deliverable must enumerate package-specific `TBD` content rather than invent codes or stages.

The artifact register confirms the source-set gap explicitly via `ART-8E3FB7B466` ("TBD vendor document register" — Vendor Documentation Gap Evidence). This is the authoritative basis for marking the register schema and acceptance criteria as `TBD` until a package-specific source is added.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Vendor document register schema | Require `PRQ-009` Vendor Document Index and `DOC-008` Vendor Document Control Procedure as core vendor-document entries; mark detailed columns (number, title, code, revision, status, transmittal) as `TBD` pending vendor or project source. | `_Sources/26020-Package_Requirements.docx` supports the core entries; `ART-8E3FB7B466` flags package-specific vendor-document requirements as a source gap. |
| Submittal stages and hold/issue codes | List as `TBD` and require vendor or EPC procedure to define. | No accessible source defines stages or hold codes for this package. |
| 5 kV interpretation | Treat "5kV" as the project MV insulation-class naming alignment for 4.16 kV equipment until vendor documentation confirms the building's bus voltage and class. | DBM MV cable table supports 5 kV insulation class for 4.16 kV MV cables; building 880-1 bus voltage is not stated in the accessible source set. |
| Building 880-1 identity | Carry "(880-1)" as the workbook-spelled building identifier; do not invent floor plans, dimensions, or location. | Workbook row 39 spelling is the only accessible identity reference. |
| EPC acceptance scope | Keep out of this deliverable; route to `DEL-037-06`. | `DELIVERABLE_REGISTER.csv` separates the EPC acceptance deliverable from vendor turnover. |
| Standards | List CEC, project MV cable/insulation basis, project electrical specifications, and area classification as governing with detailed locations `TBD`. | DBM references these bases but specific clauses/specifications are not accessible. |

## Examples

- Acceptable register entry: "Vendor document register row: document number `TBD`; title `TBD`; revision `TBD`; transmittal `TBD`. Source basis: `ART-8E3FB7B466` (Vendor Documentation Gap Evidence)."
- Acceptable interface treatment: "Vendor grounding interface drawings and bonding details shall be included in the register and submittal set. Source: `INTERFACE_REGISTER.csv` row `IFC-E26DA604FB`."
- Not acceptable without new source: "Submittal stage 1 (for-review) shall be due 4 weeks ARO and stage 3 (as-built) shall be due 60 days after mechanical completion." The accessible source set does not establish these stages or durations for this package.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-037-05-001 | Package title states "5kV SWITCHGEAR" but the accessible source set does not state the building 880-1 bus voltage or switchgear class; only the project MV cable insulation class (5 kV for 4.16 kV cables) is source-supported. | Workbook Packages row 39; `PACKAGE_REGISTER.csv` row `PKG-037` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table (line 3009); electrical buildings paragraph | Datasheet Attributes/Construction; Specification Standards; Guidance Trade-offs | Treat "5kV" as project MV insulation-class naming alignment until vendor documentation or detailed electrical design confirms bus voltage; do not invent switchgear class. | TBD |
| HRR-037-05-002 | DBM and Package Requirements sources support vendor document register/index/control-procedure existence, but no PKG-037-specific document index, hold/issue code list, submittal-stage schedule, or turnover acceptance criteria are present in the accessible source set. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverables paragraph (line 617); `_Sources/26020-Package_Requirements.docx`, Core vendor documents table | `ARTIFACT_REGISTER.csv` row `ART-8E3FB7B466` (Vendor Documentation Gap Evidence) | Datasheet Construction; Specification Requirements; Procedure Steps | Require `PRQ-009` Vendor Document Index, `DOC-008` Vendor Document Control Procedure, submittals, and turnover records; keep detailed schema and acceptance content `TBD` until a package-specific source is accepted. | TBD |
