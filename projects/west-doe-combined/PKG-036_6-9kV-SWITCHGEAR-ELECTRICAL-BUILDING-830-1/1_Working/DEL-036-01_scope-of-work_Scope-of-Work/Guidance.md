# Guidance: DEL-036-01_scope-of-work

## Purpose

This deliverable is the mandatory Gate 5 EPC Integrator Scope of Work for the workbook-defined Electrical package `PKG-036` "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)". It anchors the package identity, function, source basis, boundary, responsibility split, and whole-facility integration narrative used by every downstream PKG-036 deliverable.

## Principles

- **Workbook is the decomposition basis.** Package identity (name, workbook row, CoA number, WBS, discipline, interface set, supported objectives) is taken from Workbook Packages row 38 as carried into the Gate 7 final-published registers. Do not silently substitute alternative identity from DBM prose.
- **Source slices are authoritative for technical content.** Where the workbook defines what the package IS, accessible DBM source slices define how the facility behaves around it (voltages, distribution architecture, grounding, MCC/VFD basis, electrical-building HVAC, cable/conduit, hazardous-area context). Do not invent values not supported by source slices.
- **Responsibility split is binding.** EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Package Vendor owns engineering, design, vendor documentation, and the physical equipment package. The Scope of Work shall not blur this split.
- **Surface conflicts, do not reconcile them silently.** Where workbook identity and DBM equipment-list prose disagree (see Conflict Table), the Scope of Work carries the workbook identity and surfaces the discrepancy for human ruling.

## Considerations

- The package function is medium-voltage distribution at 6.9 kV per the workbook name and per the DBM voltage/service table, which describes the 6.9 kV service as supporting facility process AC inverter-drive motors rated 5,500 hp and above. The 6.9 kV MCC supports starting VFDs for the KM-2150/2250 Inlet/Sales Gas Compressor motors and provides an Ethernet port to the plant PLC central control panel.
- The DBM electrical-buildings list does not contain a row identifying tag `830-1` as a 6.9 kV switchgear building; it lists `830-1` as the 4.16 kV Acid Gas / Overheads Compressor Electrical Building and lists `820-1` as the 6.9 kV Inlet / Sales Compressor Electrical Building. This is a real source discrepancy that the Scope of Work must surface.
- The applicable interface set is large (12 IFC IDs in `INTERFACE_REGISTER.csv`). The Scope of Work enumerates the interfaces and points to the Datasheet for interface requirements detail; it does not duplicate the package interface requirements matrix.
- No deliverable-specific source slices were copied during PREPARATION. `26020-Package_Requirements.docx` exists in `_Sources/` but was not parsed as an accessible source slice in this run; any package-specific clause it may contain is `TBD` until the document is parsed.

## Trade-offs

- **Carry workbook identity vs. defer to DBM tag-to-function mapping.** Carrying workbook identity preserves the decomposition basis and Gate 7 register integrity; deferring to DBM would imply re-decomposition. The Scope of Work therefore carries the workbook identity and flags the source mismatch.
- **Narrative completeness vs. source fidelity.** Where source slices do not exist for package-specific equipment, the Scope of Work prefers `TBD` over inferred narrative.

## Examples

- Building tag and function appear together in source row "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building" and "820-1 6.9kV Inlet / Sales Compressor Electrical Building" from the DBM electrical-buildings list. The Scope of Work uses these source excerpts as evidence of the conflict, not as a basis to overwrite the workbook identity.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-036-01-001 | Building tag-to-function mismatch. Workbook Packages row 38 names `PKG-036` as "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)". The DBM electrical-buildings list maps `830-1` to "4.16kV Acid Gas / Overheads Compressor Electrical Building" and maps the 6.9 kV building to tag `820-1` ("6.9kV Inlet / Sales Compressor Electrical Building"). | `_Decomposition/.../PACKAGE_REGISTER.csv` row `PKG-036`; Workbook Packages row 38 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings list (rows for 820-1 and 830-1) | `Datasheet.md` Identification / Attributes; `Specification.md` R-036-01-03, R-036-01-04; `Procedure.md` prerequisites | PROPOSAL: Carry the workbook identity (name, tag, IFC set) for PKG-036 (Gate 7 decomposition basis). Capture the DBM mismatch as a human-ruling item; do not overwrite the workbook tag or function during this Scope of Work pass. | TBD |
| CT-036-01-002 | Source slice gap for package-specific equipment. The workbook identifies the package, but no accessible source slice itemizes the breakers, MCC line-ups, transformers, protective relays, and building location coordinates assigned to PKG-036. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical sections (general) | `_Sources/26020-Package_Requirements.docx` (presence only; not parsed) | `Datasheet.md` Attributes / Construction; `Specification.md` R-036-01-10 | PROPOSAL: Keep package-specific equipment and location items as `TBD` until `26020-Package_Requirements.docx` is parsed or a vendor datasheet is received. | TBD |
