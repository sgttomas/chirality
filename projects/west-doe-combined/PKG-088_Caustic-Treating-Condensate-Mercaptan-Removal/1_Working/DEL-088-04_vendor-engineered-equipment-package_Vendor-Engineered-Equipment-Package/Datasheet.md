# Datasheet — DEL-088-04 Vendor Engineered Equipment Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-088-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-088` Caustic Treating (Condensate Mercaptan Removal) | `_CONTEXT.md`; DELIVERABLE_REGISTER row 267 |
| Workbook Row | Workbook Packages row 50 | `_CONTEXT.md`; DELIVERABLE_REGISTER row 267 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Anchoring Deliverables | DEL-088-01 EPC Scope of Work; DEL-088-02 Package Datasheet | `_CONTEXT.md` Notes; DELIVERABLE_REGISTER rows 264, 265 |
| Covers Scope Items | SOW-0055, SOW-0056, SOW-0057, SOW-0058 | `_CONTEXT.md`; SCOPE_LEDGER rows 56–59 |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION: package-grouping heuristic per skill) |

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Package function | Non-regenerable caustic treating of C5+ condensate for mercaptan removal | SCOPE_LEDGER SOW-0056; DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Treating technology | Non-regenerative caustic mercaptan treating (Merichem or equivalent) | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Treating capacity | 20,000 bbl/d C5+ condensate (≈ 3,180 m³/d) | DBM-Comp_and_Liquids §Condensate Mercaptan Treating; SOW-0057 |
| Caustic regeneration | Not included in current basis | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Caustic basis | 50 wt% NaOH in H2O; SG 1.75 TBC | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Treated-product C1-C3 RSH target | Below 175 ppmw S | SCOPE_LEDGER SOW-0058 |
| Treated-product total sulphur target | Below 0.5 wt% | SCOPE_LEDGER SOW-0058 |
| Volatile mercaptan waiver | Possible; requires confirmation | SCOPE_LEDGER SOW-0058 |
| Indoor/outdoor | All caustic treating equipment indoor | SCOPE_LEDGER SOW-0058 |
| Material restriction | No aluminum permitted in the caustic building | SCOPE_LEDGER SOW-0058; DBM-Comp_and_Liquids §Condensate Mercaptan Treating |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Feed | C5+ stabilized condensate from 03-25 Liquids Hub | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Extractable compounds | H2S, CO2, methyl/ethyl/propyl/butyl mercaptans | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Expected DSO entrainment | 30 ppmw S | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Design DSO entrainment | 50 ppmw S, TBC vendor | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Consumables | Fresh caustic and make-up water (continuous) | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Waste streams | Spent caustic, DSO | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Caustic tank type | Atmospheric 32 oz tanks with LP fuel-gas blanket, heating, insulation | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Spent caustic tank venting | Flame arrestor to incinerator header; truck-out support; no VRU connection on fresh caustic | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Operating temperature/pressure | TBD (location TBD; not stated in accessible sources) | TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Major included equipment | Caustic contactor/treating equipment, pumps, indoor caustic-area equipment, instrumentation, piping, controls, and related package systems for 20,000 BPD C5+ condensate treating | SCOPE_LEDGER SOW-0057 |
| Package internals | Caustic C5+ contactor, pre-heater, caustic outlet filter, water wash | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Tankage included with package | DSO, spent-caustic, fresh-caustic, fresh-water tanks | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| External interfaces | Incinerator overhead, dilution gas, enrichment gas | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Caustic building constraints | Indoor; aluminum not permitted; tank coating/material details TBC | SOW-0058; DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Skid/footprint | TBD | TBD (not in accessible source slices) |
| Design code/standards | TBD; ASSUMPTION: applicable Canadian provincial and CSA standards for caustic service; specific codes location TBD | ASSUMPTION |

## References

- `_CONTEXT.md` — deliverable identity, scope, anchoring deliverables.
- `_REFERENCES.md` — authoritative decomposition basis.
- SCOPE_LEDGER.csv rows 56–59 — SOW-0055 to SOW-0058 (PKG-088 scope items).
- DELIVERABLE_REGISTER.csv row 267 — DEL-088-04 entry.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Condensate Mercaptan Treating" (lines 387–402).
- `_Sources/26020-Package_Requirements.docx` package heading 41 — referenced but binary; location TBD.
