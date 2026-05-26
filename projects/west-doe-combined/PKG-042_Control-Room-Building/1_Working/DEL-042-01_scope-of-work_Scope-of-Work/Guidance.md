# Guidance: DEL-042-01_scope-of-work — Scope of Work (PKG-042)

Directional guidance for drafting the EPC Integrator Scope of Work for PKG-042 "Control Room Building".

## Purpose

The Scope of Work is the Gate 5 EPC anchor deliverable for PKG-042. It frames the package as a vendor-owned Electrical package within the larger process facility and establishes the EPC Integrator's bounded responsibility for integration. It is the document that downstream deliverables (Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover Package, EPC Vendor Package Review and Acceptance) align against. [`DELIVERABLE_REGISTER.csv` row notes; `_CONTEXT.md`]

## Principles

1. **Workbook row 44 is authoritative.** The package name, WBS, CoA tracking number, discipline, function statement, responsibility model, and applicable interface types come from Workbook row 44 and are mirrored — not reinterpreted — in the Scope of Work. [`PACKAGE_REGISTER.csv`]
2. **Vendor-EPC split is preserved.** Package engineering, package design, vendor documentation, and the physical equipment package are Package Vendor responsibilities. Integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration are EPC Integrator responsibilities. The Scope of Work must not silently transfer vendor design work to the EPC Integrator. [OBJ-004; `PACKAGE_REGISTER.csv` ResponsibilityModel]
3. **Scope of Work names the integration boundary; Datasheet carries the interface facts.** Interface types are enumerated here; specific battery limits, tie-in points, and load values belong on DEL-042-02 (Package Datasheet). [ART-CC3360DFD7; ART-31BDD93887 series]
4. **Tagged equipment is source-anchored.** If Workbook row 44 carries detailed major-equipment text, it appears here verbatim or summarized with citation. If it does not, the field is `TBD`, not invented. [skill source-grounding rule]
5. **Exclusions are explicit.** If the workbook states no package-specific exclusions, the Scope of Work says so explicitly; this protects downstream readers from assuming silence means "anything goes". [`PACKAGE_REGISTER.csv` Exclusions]

## Considerations

- **Electrical discipline as a building-package outlier.** PKG-042 is a "Control Room Building", classified under WBS 03 with discipline Electrical. The Control Room Building is in practice a multi-discipline integration point (electrical, controls, communications, fire & gas, HVAC, civil/structural foundations). The wide interface list on PKG-042 reflects this. The Scope of Work should describe the building as an electrical/controls building with structural and utility tie-ins, not as a pure electrical equipment skid. [PROPOSAL — based on interface-type spread; `INTERFACE_REGISTER.csv`]
- **Objectives this package carries.** PKG-042 is associated (via the PACKAGE_HEURISTIC mapping) with OBJ-002 (3-25 facility scope), OBJ-004 (vendor/EPC package execution model), OBJ-005 (electrical infrastructure), OBJ-006 (controls/instrumentation/comms/F&G integration), OBJ-007 (utilities and ancillary), OBJ-008 (civil/structural/site), OBJ-009 (safety, sour-service, regulatory), and OBJ-010 (operability, vendor-documentation, turnover). These are recorded as ASSUMPTION until human-confirmed but should inform what the integration narrative chooses to make explicit. [`OBJECTIVE_REGISTER.csv`]
- **Source-slice availability.** The accessible source set at drafting time is the GATE-07 PROJECT_DECOMP snapshot plus `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `_Sources/26020-Package_Requirements.docx`, and the DBM-Comp_and_Liquids and DBM-Deepcut folders. Specific Workbook row 44 cells and specific DBM sections for the Control Room Building have not been read in this pass; further enrichment passes should resolve them. [_REFERENCES.md; this run record]
- **Coordination with DEL-042-02.** The interface-type list here should match exactly the per-interface evidence rows in DEL-042-02's Package Datasheet (ART-31BDD93887 et seq.). A mismatch indicates that one of the two documents is out of step with `INTERFACE_REGISTER.csv`.

## Trade-offs

- **Brevity vs. integration narrative depth.** The Scope of Work is a scope statement, not a design document. Trade off completeness against duplication of content that properly lives on the Package Datasheet or Construction Work Package.
- **Source fidelity vs. readability.** Verbatim quoting of workbook cells preserves fidelity but produces stilted text. Prefer faithful paraphrase with citation, falling back to verbatim quotation when the original wording is normative.
- **Naming the discipline narrowly vs. honoring the workbook.** The workbook says "Electrical"; reality is multi-discipline. The Scope of Work should keep the workbook discipline classification and explain the multi-discipline integration in the integration narrative rather than re-classifying the package.

## Examples

- **Identification block:** Render exactly the seven fields from PACKAGE_REGISTER.csv (PackageID, Workbook Package ID, Workbook Row, WBS, Tracking Number, Discipline, Name).
- **Responsibility paragraph (verbatim-faithful):** "The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration." [`PACKAGE_REGISTER.csv` ResponsibilityModel]
- **Interface enumeration:** A bulleted list of the eleven interface types flagged for PKG-042, each pointing to its `IFC-*` ID, with the note that battery-limit details live on DEL-042-02.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-042-01-01 | Discipline classification "Electrical" vs. de facto multi-discipline integration scope (HVAC, structural, F&G, comms). | `PACKAGE_REGISTER.csv` Discipline=Electrical | `INTERFACE_REGISTER.csv` PKG-042 interface-type spread (11 interfaces incl. HVAC, structural, F&G) | Datasheet Identification; Spec REQ-042-01-05; Guidance integration narrative | Keep workbook discipline = Electrical; explain multi-discipline reality in narrative; do not reclassify | TBD |
| CONF-042-01-02 | "Applicable interface types" on PACKAGE_REGISTER lists 11 types; `INTERFACE_REGISTER.csv` rows enumerated for PKG-042 in the source slice opened during this pass show 10 IFC-* rows (Structural / Foundations / Supports listed on PACKAGE_REGISTER but its IFC row was not surfaced in the grep slice). | `PACKAGE_REGISTER.csv` ApplicableInterfaceTypes | `INTERFACE_REGISTER.csv` PKG-042 rows | Datasheet Interface Conditions; Spec REQ-042-01-05 | Treat PACKAGE_REGISTER list as authoritative for interface-type enumeration; re-open `INTERFACE_REGISTER.csv` in Pass 3 to confirm all eleven IFC-* IDs exist | TBD |
| CONF-042-01-03 | Source basis cites "DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md" for PKG-042, but the Control Room Building is not obviously a 3-25 compressor/liquids subject; relevance is unverified in this pass. | `PACKAGE_REGISTER.csv` SourceReference | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md content (not opened in this pass) | Datasheet References; Spec Standards table | Carry citation as ASSUMPTION until DBM slice is opened and confirmed | TBD |
