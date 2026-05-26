# Datasheet: DEL-085-06 — EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-085-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | `PKG-085` | `_CONTEXT.md` |
| Package | Flare Stack (High Pressure) | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Covered SOW items | SOW-0087, SOW-0088, SOW-0089, SOW-0090 | `_CONTEXT.md` |
| Supported Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION: package-heuristic association) |

## Attributes (Subject Equipment under Review)

The deliverable reviews and accepts the EPC-integrated vendor package for the High Pressure flare stack serving facility 03-25 and shared with 04-25 (HP/Cryo and LP dual stack).

| Attribute | Value | Source |
|---|---|---|
| Service | HP/Cryo + LP dual flare stack; HP relief disposal for facility 03-25 and 04-25 (shared interface) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Flare and Blowdown (L497) |
| Configuration | Dual stack: HP/Cryo and LP risers | DBM L497, L548 |
| HP/Cryo stack outside diameter | 660 mm OD | DBM L499 |
| HP/Cryo stack height | 60,957 mm | DBM L499 |
| Burner type | Sonic (HP/Cryo) | DBM L499 |
| LP stack OD | TBD | DBM L499 (explicit TBD in source) |
| HP relief header size | 508 mm (20 in) | DBM L499 |
| LP relief header size | 508 mm (20 in) | DBM L499 |
| HP KO drums upstream | V-4100-2 (compressor area), V-4150-2 (tank farm); manifold to HP flare | DBM L497 |
| HP KO transfer pumps | P-4100-2, P-4150-2 (one per drum, 1x100%); truck-out or transfer to slop | DBM L497, L550 (pump count) |
| LP KO drum | V-3900-2 with pump P-3900-2 to slop | DBM L499 |
| LP services routed to LP flare | TEG regeneration, VRU, compressor seal-pot | DBM L499 |
| Service split (HP vs LP allocation between 03-25/04-25) | TBD (open interface) | DBM L56 |
| Final flare relief and blowdown loads | TBD (require final flare studies) | DBM L548, L555 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Design ambient temperature range | -40 °C to +35 °C | DBM L96 |
| Site exposure governance | -40 °C minimum ambient governs exposed equipment, package buildings, panels, instrumentation, field devices, unless a stricter package/process basis applies | DBM L145 |
| Snow/wind/seismic loading | Applies to flare/stack elements; values per geotechnical and site criteria | DBM L700 |
| Emissions tabulation status | Adequate for DBM scoping; not permit-final | DBM L555 |

## Construction (Acceptance-Scope Artifacts under Control of this Deliverable)

| Item | Value | Source |
|---|---|---|
| Vendor document review log | Required artifact | `_CONTEXT.md` (Anticipated Artifacts) |
| Package acceptance checklist | Required artifact | `_CONTEXT.md` |
| Test/inspection evidence | Required artifact | `_CONTEXT.md` |
| Turnover evidence | Required artifact | `_CONTEXT.md` |
| Foundation/anchorage acceptance | Required for flare/stack elements per source | DBM L700 |
| Cross-facility interface acceptance with 04-25 | Required (shared HP/LP allocation) | DBM L56 |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- Source: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Flare and Blowdown; Site Basis; Foundations; Emissions)
- Source (not locally text-accessible): `_Sources/26020-Package_Requirements.docx` package heading 38 — **location TBD** (binary; relevant slice not extracted)
- Source (not locally text-accessible): `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 58 — **location TBD** (binary; relevant slice not extracted)
- Decomposition: GATE-07 Final Published 2026-05-24 PROJECT_DECOMP snapshot
