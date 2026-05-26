# Datasheet — DEL-063-04 Vendor Engineered Equipment Package (Tanks, DSO API 650)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-063-04_vendor-engineered-equipment-package | _CONTEXT.md |
| Deliverable Name | Vendor Engineered Equipment Package | _CONTEXT.md |
| Parent Package | PKG-063 — Tanks, DSO (API 650) | _CONTEXT.md |
| Discipline | Mechanical | _CONTEXT.md |
| Type | Vendor Package Production Unit | _CONTEXT.md |
| Responsible Party | Package Vendor with EPC Integrator integration review | _CONTEXT.md |
| Equipment Tag(s) | TK-6770-1 | DBM-Deepcut/4-25_Deepcut_DBM.md L2626 |
| Service | DSO (Disulphide Oil) Storage Tank | DBM-Deepcut/4-25_Deepcut_DBM.md L1564 |
| Facility | 4-25 (Deepcut) NGL Mercaptan Treating Unit area | DBM-Deepcut/4-25_Deepcut_DBM.md L2626 |
| Quantity | 1 | DBM-Deepcut/4-25_Deepcut_DBM.md L2558, L2626 |
| Governing Code | API 650 (per package title) | _CONTEXT.md / PROJECT_DECOMP package name |

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Nominal capacity | 400 bbl | DBM-Deepcut L1530 ("Disulphide oil storage: 1 x 400 bbl tank"), L528 |
| Tank type | Atmospheric, vertical (API 650 family) | DBM-Deepcut L1564; tank orientation not explicitly stated — ASSUMPTION: vertical per API 650 convention |
| Heating | Heated | DBM-Deepcut L1564 |
| Insulation | Insulated | DBM-Deepcut L1564 |
| Blanket gas | Low-pressure fuel gas blanket | DBM-Deepcut L1564 |
| Vapour route | Off-gas to incinerator header (with backflash protection) | DBM-Deepcut L1564, L1570 |
| Flame arrestor | Required on incinerator-header connection | DBM-Deepcut L1564 |
| Truck-out connection | Required (truck-out capable) | DBM-Deepcut L1564 |
| Design specific gravity | 1.75 (TBC) | DBM-Deepcut L1564 — vendor to confirm |
| Materials of construction | TBD — must be compatible with DSO service (DSO-compatible alloy); aluminum prohibited in caustic building, no constraint stated explicitly for DSO tank materials | DBM-Deepcut L1566 (aluminum prohibition is caustic-building scope) |
| Heating medium | TBD | location TBD |
| Design pressure / vacuum rating | TBD | location TBD |
| Design temperature | TBD | location TBD |
| Roof type | TBD | location TBD |
| Foundation | TBD | location TBD |
| Containment / dyke | TBD | location TBD |
| Instrumentation (level, temperature, pressure) | TBD; LEL/H2S/fire detection placement is per facility hazards survey | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md L838 |
| Nozzle schedule | TBD | location TBD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Stored fluid | Disulphide oil (DSO), by-product of NGL non-regenerative caustic treating | DBM-Deepcut L528 |
| Disposition | Truck-out for disposal; alternate mixing into C5+ product subject to detailed-engineering review | DBM-Deepcut L528, L1564 |
| Adjacent vapour service | Connected to incinerator header (shared with spent caustic tank) | DBM-Deepcut L1564, L1570 |
| Indoor / outdoor | TBD — caustic-containing equipment is indoors; DSO tank location not explicitly stated | DBM-Deepcut L1552 (caustic equipment indoor) — ASSUMPTION: DSO tank treated similarly to other Mercaptan Treating Unit storage |
| Climate / freeze protection | Heated and insulated (per attributes); detailed protection scheme TBD | DBM-Deepcut L1564 |

## Construction

| Item | Value | Source |
|---|---|---|
| Governing fabrication code | API 650 (per package classification) | _CONTEXT.md / PROJECT_DECOMP |
| Code addenda / edition | TBD | location TBD |
| Modified-API-650 indicator | The DBM applies "Modified API 650" to condensate tanks (L1646); applicability to DSO tank not stated — TBD |
| Shop vs field erection | TBD | location TBD |
| Welding / NDE | Per API 650 default unless package datasheet specifies otherwise — TBD |
| Coatings | TBD | location TBD |
| Insulation system | Required (heated, insulated); thickness/material TBD | DBM-Deepcut L1564 |
| Cladding | TBD; stainless-steel cladding mandated in caustic-exposure areas (L1566); DSO applicability TBD |
| Vendor data deliverables | Per DEL-063-05 Vendor Document Turnover Package | _CONTEXT.md (sibling deliverable) |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — lines 528, 1530, 1552, 1564, 1566, 1570, 1646, 2558, 2626
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — line 838
- `26020-Package_Requirements.docx` package heading 18 — location TBD (binary source not directly readable in this run)
- PROJECT_DECOMP Gate-07 snapshot deliverable register row for DEL-063-04
