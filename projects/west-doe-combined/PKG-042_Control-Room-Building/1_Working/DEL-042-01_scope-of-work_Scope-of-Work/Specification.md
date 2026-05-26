# Specification: DEL-042-01_scope-of-work — Scope of Work (PKG-042)

Normative requirements for the EPC Integrator-authored Scope of Work for vendor-owned Electrical package PKG-042 "Control Room Building".

## Scope

### In Scope
- Statement of the package scope of work for PKG-042 as a distinct flat project package under WBS 03 (Workbook row 44). [SCOPE_LEDGER.csv `SOW-0043`]
- Declaration of package function and whole-facility integration narrative for the Control Room Building. [ART-B33959740B]
- Tagged-equipment and package-identity record (package name, workbook ID, CoA tracking number 26020-03-39-010, WBS, and detailed major-equipment text where source-supported). [ART-09426CDD36]
- Package responsibility assignment record per the responsibility model below. [ART-93D323D241]
- Identification of the EPC integration boundary by interface type for PKG-042. [INTERFACE_REGISTER.csv rows for PKG-042]
- Source basis citation back to Workbook row 44 and any explicitly relevant DBM section. [`PACKAGE_REGISTER.csv` SourceReference]

### Out of Scope
- Package engineering, package design, vendor documentation, and physical equipment supply (these are owned by the Package Vendor and are produced through DEL-042-04 and DEL-042-05). [`PACKAGE_REGISTER.csv` ResponsibilityModel]
- Technical handoff data for vendor engineering (the Package Datasheet DEL-042-02 carries this). [`DELIVERABLE_REGISTER.csv` row `DEL-042-02_package-datasheet`]
- Installation, tie-in workface plan, and turnover (the Construction Work Package DEL-042-03 carries this). [`DELIVERABLE_REGISTER.csv` row `DEL-042-03_construction-work-package`]
- Vendor package review and acceptance evidence (DEL-042-06). [`DELIVERABLE_REGISTER.csv` row `DEL-042-06_epc-vendor-package-review-and-acceptance`]
- Package-specific exclusions: TBD — no exclusions stated in workbook row 44. [`PACKAGE_REGISTER.csv` Exclusions]

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-042-01-01 | The Scope of Work SHALL identify the package as PKG-042 "Control Room Building", Workbook row 44, CoA tracking number 26020-03-39-010, WBS 03, discipline Electrical. | `PACKAGE_REGISTER.csv` (FACT) |
| REQ-042-01-02 | The Scope of Work SHALL state the package function and a whole-facility integration narrative explaining how the Control Room Building integrates into the process facility. | ART-B33959740B (FACT) |
| REQ-042-01-03 | The Scope of Work SHALL assign Package Vendor responsibility for package engineering, package design, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` ResponsibilityModel; ART-93D323D241 (FACT) |
| REQ-042-01-04 | The Scope of Work SHALL assign EPC Integrator responsibility for integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` ResponsibilityModel; ART-93D323D241 (FACT) |
| REQ-042-01-05 | The Scope of Work SHALL identify, by interface type, the EPC integration boundaries flagged in the interface register for PKG-042: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv`; `PACKAGE_REGISTER.csv` applicable interface types (FACT) |
| REQ-042-01-06 | The Scope of Work SHALL list the tagged equipment and package identity items source-supported by Workbook row 44; items not directly supported by an accessible source SHALL be marked `TBD`. | ART-09426CDD36 (FACT); skill source-grounding rule |
| REQ-042-01-07 | The Scope of Work SHALL cite Workbook Packages row 44 as the authoritative source for the package scope, and SHALL cite the relevant DBM section when that section is locally accessible. | `PACKAGE_REGISTER.csv` SourceReference (FACT) |
| REQ-042-01-08 | The Scope of Work SHALL be consistent with `SCOPE_LEDGER.csv` row `SOW-0043` and SHALL NOT modify scope items established at decomposition. | `SCOPE_LEDGER.csv` (FACT) |
| REQ-042-01-09 | The Scope of Work SHOULD enumerate the package-specific exclusions where stated in source; if none are stated, it SHALL record "no package-specific exclusions stated in source". | `PACKAGE_REGISTER.csv` Exclusions (FACT) |
| REQ-042-01-10 | The Scope of Work SHALL identify the supported objectives carried by PKG-042 (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010) as directionally relevant context, recorded as ASSUMPTION per the PACKAGE_HEURISTIC association mode until human-confirmed. | `OBJECTIVE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv` (ASSUMPTION) |

## Standards

| Standard / Source | Use | Location |
|---|---|---|
| Workbook Packages (26020-Packages_Interfaces_4_export.xlsx), row 44 | Authoritative package definition (name, WBS, tracking number, discipline, function, responsibility model, interface flags) | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` (FACT; source file present; row 44 slice extraction TBD) |
| 26020-Package_Requirements.docx | Vendor-document and package requirements basis | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` (FACT — present; section relevance to PKG-042 Scope of Work TBD) |
| DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | Design Basis Memorandum referenced by PKG-042 row | `_Sources/DBM-Comp_and_Liquids/` (FACT — present; specific section for Control Room Building TBD; ASSUMPTION on direct relevance to the Control Room Building scope) |
| GATE-07 Final Published PROJECT_DECOMP | Authoritative decomposition basis (registers, scope ledger, interfaces, artifacts, objectives) | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (FACT) |

## Verification

| ReqID | Verification Method |
|---|---|
| REQ-042-01-01 | Inspection: identification block matches PACKAGE_REGISTER.csv row PKG-042 exactly. |
| REQ-042-01-02 | Review by EPC Integrator: function and integration narrative present and consistent with package function. |
| REQ-042-01-03 / REQ-042-01-04 | Inspection: responsibility assignment record exactly mirrors PACKAGE_REGISTER.csv ResponsibilityModel. |
| REQ-042-01-05 | Cross-reference: every PKG-042 interface row with `RequiresInterface=YES` is enumerated in the Scope of Work by interface type. |
| REQ-042-01-06 | Inspection: every tagged-equipment claim has a cited source slice or is marked `TBD`. |
| REQ-042-01-07 | Inspection: source citation for Workbook row 44 and (where applicable) DBM section is present. |
| REQ-042-01-08 | Cross-reference against `SCOPE_LEDGER.csv` `SOW-0043`. |
| REQ-042-01-09 | Inspection: exclusions section present with either enumerated exclusions or the "no package-specific exclusions stated in source" statement. |
| REQ-042-01-10 | Inspection: supported-objectives list matches `DELIVERABLE_REGISTER.csv` SupportsObjectives column for this deliverable, labeled ASSUMPTION. |

## Documentation (Anticipated Artifacts)

Per `ARTIFACT_REGISTER.csv` for `DEL-042-01_scope-of-work`:

| ArtifactID | Artifact |
|---|---|
| ART-5CE60C498E | Package scope of work (EPC Scope of Work) |
| ART-09426CDD36 | Tagged equipment and package identity list |
| ART-B33959740B | Package function and whole-facility integration narrative |
| ART-93D323D241 | Package responsibility assignment record |
