# Guidance — DEL-098-01 Scope of Work

> Directional guidance for drafting the EPC Integrator Scope of Work for PKG-098.

## Purpose

The Scope of Work is the mandatory Gate-5 EPC anchor deliverable that bounds the PKG-098 package: it names the tagged equipment, states package function, cites source basis, draws boundaries between package-vendor and EPC/by-others scope, and provides the whole-facility integration narrative needed by downstream EPC, vendor, construction, and acceptance deliverables (DEL-098-02 through DEL-098-06). [Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row `DEL-098-01_scope-of-work`]

## Principles

1. **Source-first.** Every scope statement must trace to `26020-Package_Requirements.docx` §`26020-03-PT-19-007 - Tanks, Sour Water` or to the 3-25 DBM (`3-25_Comp_and_Liquids_DBM.md`). Decomposition prose contextualizes; it does not author requirements.
2. **Preserve source language for tagged equipment, code, and design envelope.** Tags (TK-9010 through TK-9050 series), "modified API 650", Devchem 253 coating, Kennilworth-type HCL skim, 32 oz test pressure, and -40/60 °C design envelope are quoted from source.
3. **Surface, do not paper over, source-stated TBDs.** Capacity (Appendix A), Item-2 operating temperature, driver, material of construction, and Interface Coordination Notes are all "TBD" in the source — carry them as TBD in the Scope of Work.
4. **Boundary discipline.** "By others" exclusions (foundations, on-site mounting, E&I, platforms, staircases) are explicit in the source; restate them prominently.
5. **Responsibility assignment is a register, not a narrative.** Use a structured table aligned to the Physical Interface Summary applicability matrix.
6. **Conflict avoidance over conflict resolution.** Where source and DBM disagree on counts/labels, surface in the Conflict Table for human ruling rather than silently choosing.

## Considerations

- The Physical Interface Summary in the package source enumerates 18 interface types with Yes/No applicability and an interface-source identifier `26020-Packages_Interfaces.3.xlsx`. That workbook is not in `_Sources/` locally; cell-level evidence (beyond "column M (row 93)" cited for Area/Exterior Lighting) is not accessible.
- The DBM identifies sour-service requirements at the facility level for pressure vessels and references Devchem 253 coating for produced-water tanks; this corroborates the package source.
- The DBM notes the produced-water tank design SG is 1.25 TBC while the pump fluid SG basis is 1.18 — to be closed in detailed design. This is downstream of the Scope of Work but should be referenced under R-11 integration narrative.
- The Vendor Engineering Deliverables list in the source is extensive (≈ 60 deliverable IDs across MEC/PRO/PIP/CIV/ELE/PLN/INS/CTL/STR/QLT/PRQ/DOC families). The Scope of Work should reference the source table rather than restating it inline, with a pointer that DEL-098-05 (Vendor Document Turnover) governs the live register.

## Trade-offs

- **Verbatim quotation vs. integrator narrative.** Verbatim preserves traceability; narrative aids EPC integration readability. Recommendation: verbatim for equipment lists, codes, conditions, and exclusions; narrative for facility integration and responsibility framing.
- **Single Scope of Work vs. split with Package Datasheet.** Decomposition splits scope/identity (this deliverable) from technical interface evidence (DEL-098-02). Avoid duplicating interface tables — reference DEL-098-02 instead.
- **Treat Items 1/2/3 as one tank set vs. three sub-packages.** Source enumerates three Items but states common technical basis. Recommendation: one Scope of Work with three identification rows, common requirements section, and per-item exceptions (Item-2 temperature).

## Examples

The following text snippet illustrates source-faithful Scope of Work phrasing for tagged equipment (drawn from Package Requirements §`26020-03-PT-19-007` Major Included Equipment):

> "PKG-098 comprises seven (7) × 3,800 bbl atmospheric storage tanks designed and fabricated to modified API 650, with Devchem 253 internal coating (floor, walls, roof), external insulation with electric heating, and one (1) Kennilworth-type HCL float skim system per tank. The package is enumerated as Item 1 — three (3) Sour Produced Water Storage Tanks (TK-9030-2, TK-9040-2, TK-9050-2); Item 2 — two (2) Sour Inlet Produced Water Storage Tanks (TK-9010-2, TK-9020-2); and Item 3 — two (2) Produced Water Storage Tanks (TK-9010-1, TK-9020-1)."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-098-01-01 | Basic Scope lists only Item 1 (3 sour tanks) as the package "Basic Scope," while Major Included Equipment enumerates Items 1–3 (7 tanks total). | `26020-Package_Requirements.docx` §`26020-03-PT-19-007` Basic Scope | `26020-Package_Requirements.docx` §`26020-03-PT-19-007` Major Included Equipment | Datasheet (Identification, Attributes); Specification R-1, R-3, R-4 | Treat "Major Included Equipment" as the governing scope set; treat "Basic Scope" line as a labelling of the headline subset; surface as PROPOSAL | TBD |
| CFT-098-01-02 | Item 3 tag labels (TK-9010-1, TK-9020-1) are called "Produced Water Storage Tanks" in source; DBM §"produced-water system" classifies the seven tanks as "five sour produced-water tanks and two sweet produced-water tanks." Mapping of Item-3 tanks to "sweet" vs. "sour produced-water" is not explicit. | `26020-Package_Requirements.docx` §`26020-03-PT-19-007` Major Included Equipment | `3-25_Comp_and_Liquids_DBM.md` §"produced-water system" | Datasheet (Attributes — Item 3 process function); Specification R-1, R-11 | Treat Item 3 (TK-9010-1, TK-9020-1) as the "two sweet produced-water tanks" pending tank-register confirmation; PROPOSAL only | TBD |
| CFT-098-01-03 | Item 2 operating temperature is "TBD" in source but Items 1 and 3 are 10 °C; no DBM value resolves Item 2 specifically. | `26020-Package_Requirements.docx` §`26020-03-PT-19-007` Scope Notes / Open Items | (no resolving source) | Datasheet (Conditions); Specification R-4 | Carry as TBD; do not infer | TBD |
| CFT-098-01-04 | Produced-water tank design SG is "1.25 TBC" while pump fluid SG basis is 1.18; DBM flags the discrepancy as one to close in detailed design. | `3-25_Comp_and_Liquids_DBM.md` §"produced-water system" (1.25 TBC) | `3-25_Comp_and_Liquids_DBM.md` §"produced-water system" (1.18 pump basis) | Datasheet (Conditions footnote); Specification R-11 integration narrative | Reference but do not resolve in Scope of Work; defer to DEL-098-02 / detailed design | TBD |
| CFT-098-01-05 | Driver and material of construction are not stated in accessible source slices; "Driver: TBD" appears explicitly. | `26020-Package_Requirements.docx` §`26020-03-PT-19-007` Scope Notes / Open Items | (no resolving source) | Datasheet (Construction — material; Conditions — driver); Specification (Standards row on sour-service) | Carry as TBD; flag for resolution in DEL-098-02 | TBD |
| CFT-098-01-06 | Interface Coordination Notes in source = "TBD."; responsibility assignment between EPC and Package Vendor is therefore unsupported by accessible source. | `26020-Package_Requirements.docx` §`26020-03-PT-19-007` Interface Coordination Notes | (no resolving source) | Specification R-10 (responsibility assignment record) | Carry the responsibility table with TBD assignments per "Yes" interface; resolve via DEL-098-02 / DEL-098-06 | TBD |
| CFT-098-01-07 | Source Basis RFQ document (`26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx`) and `26020-Packages_Interfaces.3.xlsx` are cited but not present in `_Sources/`; Appendix A (capacity) not accessible. | Package Requirements §`26020-03-PT-19-007` Location/Status and Physical Interface Summary | (file absent in `_Sources/`) | Datasheet (Conditions — capacity); Specification R-5, R-6 | Carry as location TBD; do not invent capacities | TBD |
