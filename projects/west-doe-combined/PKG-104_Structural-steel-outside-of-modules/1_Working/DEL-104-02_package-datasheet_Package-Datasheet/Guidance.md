# Guidance — PKG-104 Package Datasheet (Structural Steel — Outside of Modules)

> Directional commentary for the people producing and consuming this Package Datasheet. Rationale is grounded in the accessible DBM source slices and the decomposition. Where rationale would require source material not yet in the accessible set, items are marked `TBD` rather than invented.

## Purpose

The Package Datasheet exists because PKG-104 is a Gate 5 EPC anchor deliverable: the EPC Integrator owes a third-party structural-steel vendor (or discipline subcontractor) a single, source-grounded technical handoff that is sufficient to start engineering the outside-of-module structural steel. The datasheet is intentionally narrow — package data only — and is read alongside the Scope of Work (DEL-104-01), the Construction Work Package (DEL-104-03), and the discipline production package (DEL-104-04). Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` PKG-104 rows.

## Principles

- **Outside-of-module is the defining boundary.** PKG-104's identity is that it covers steel *not* internal to the shop-fabricated process/utility modules listed in the DBM module table. Where ambiguity arises (e.g., interface steel between a shop module and a field-erected pipe rack), document the boundary explicitly in the datasheet. Source: `DBM-Deepcut` module table (lines ~2766-2818).
- **CSA-based design throughout.** All steel design, materials, and welding are CSA-based (S16, G40.20/G40.21, W59), under the NBCC umbrella. Do not introduce ASTM or AISC equivalents into the datasheet unless an accessible source slice supports the substitution. Source: `DBM-Deepcut` §"Governing Civil and Structural Basis"; §"Codes and Standards".
- **Cold-climate metallurgy.** -40 deg C is the design minimum ambient. Carry that condition through to material toughness requirements (CVN where applicable) — but do not write a specific CVN value into the datasheet without an accessible source slice. Source: `DBM-Comp_and_Liquids` line ~145.
- **Foundation interface is owned by Civil.** PKG-104 steel sits on driven-steel-pile foundations defined in the Civil/Foundations basis. The datasheet should state the interface clearly and refer foundation parameters out — not absorb them. Source: `DBM-Deepcut` §"Piles and Foundations".
- **Cable-tray modules on pipe racks are part of PKG-104 by convention.** The DBM explicitly places cable trays on dedicated structural modules at the top of pipe racks, with walkways and ≥30% future growth. Treat these as a defined sub-scope of PKG-104 unless the project later reassigns them. Source: `DBM-Deepcut` line ~3023.

## Considerations

- **Workbook Packages row 105** is the canonical source for the package definition but is presently in a binary (`.docx`) form that this run did not parse. Drafters of subsequent revisions should resolve a parsed source slice from `_Sources/26020-Package_Requirements.docx` and cite specific clauses rather than relying on the decomposition row alone. Source: `_REFERENCES.md`.
- **Interface matrix is interface-register-driven.** `26020-Packages_Interfaces_4_export.xlsx` is the upstream interface register; until a parsed slice is available, the interface matrix entries are `TBD` rather than invented. Source: `_REFERENCES.md`.
- **Objective association (`OBJ-001`, `OBJ-008`) is heuristic.** Per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`, objectives are inherited from the package-grouping mapping and recorded as ASSUMPTION. Do not promote them to hard requirements without explicit human confirmation. Source: `_CONTEXT.md`; SKILL §Step 1.3.
- **Module table is an inventory list, not a scope list.** The DBM module table labels are civil/building inventory labels; process scope and product terminology are governed by the applicable process sections. Use the table to identify what is *out* of PKG-104 (the modules themselves), not as a directory of PKG-104 steel locations. Source: `DBM-Deepcut` line ~2764.
- **Geotechnical TBDs propagate.** Bearing capacity, LPILE curves, dynamic-design criteria, and pile design parameters remain TBD pending the geotechnical report; the datasheet should carry these as TBDs rather than placeholder numbers. Source: `DBM-Deepcut` §"Geotechnical and Topographical Assumptions".

## Trade-offs

- **Detail vs. timing.** The package datasheet is a Gate 5 anchor; pushing it to wait for every interface and every geotechnical value to close would delay the entire EPC handoff. Prefer issuing the datasheet with explicit `TBD` markers and a clear interface matrix shell, rather than waiting. Rationale: `_CONTEXT.md` notes the deliverable is "Mandatory Gate 5 EPC anchor deliverable; interface facts are intentionally carried here as evidence rather than standalone deliverables."
- **Single datasheet vs. per-structure datasheet.** A single package-level datasheet keeps the EPC handoff coherent; per-structure datasheets (e.g., one per pipe rack) belong in the discipline production package (DEL-104-04), not here. ASSUMPTION based on the four-deliverable PKG-104 breakdown in `DELIVERABLE_REGISTER.csv`.

## Examples

- *(Worked example deferred.)* No accessible source slice in the current `_REFERENCES.md` set provides a worked structural-steel sizing or take-off example for PKG-104. Mark **TBD**; do not invent.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-104-02-01 | Objective association for DEL-104-02 (`OBJ-001`, `OBJ-008`) — `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` assert these objectives directly, but per SKILL Step 1.3 the package-grouping heuristic should record them as ASSUMPTION unless explicitly confirmed. | `_CONTEXT.md` "Supports Objectives" | SKILL §Step 1.3; `OBJECTIVE_DELIVERABLE_MAP.csv` (mapping granularity TBD) | Datasheet §Identification; Specification §Scope | Carry as ASSUMPTION until human confirms the objective map is deliverable-ID-level rather than package-grouped. | TBD |
| CONF-104-02-02 | Supported-equipment list and interface matrix entries are required by `_CONTEXT.md` "Anticipated Artifacts" but the necessary source slices (`26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx`) are present in `_Sources/` only as binary files and were not parsed in this run. | `_CONTEXT.md` Anticipated Artifacts | `_REFERENCES.md` Missing/Deferred References | Datasheet §Attributes; Specification §R-8 / §Documentation | Parse the two binary sources or copy parsed slices into the deliverable folder and re-run `four-documents` Pass 3, or accept current `TBD` markers. | TBD |
| CONF-104-02-03 | Package boundary statement ("outside of modules") is asserted by the package name but no accessible source slice defines the explicit module-vs-non-module steel boundary at the interface (e.g., where a field-erected pipe rack abuts a shop module). | Package name `PKG-104` (PACKAGE_REGISTER.csv) | DBM module table (`DBM-Deepcut` lines ~2766-2818) — labels modules but does not define the steel interface boundary | Datasheet §Attributes (package boundary); Specification §Scope (in/out) | Carry boundary as ASSUMPTION; request human-confirmed boundary rule (typically: structural steel that ships with a module is module scope; steel installed in the field between/around modules is PKG-104). | TBD |
