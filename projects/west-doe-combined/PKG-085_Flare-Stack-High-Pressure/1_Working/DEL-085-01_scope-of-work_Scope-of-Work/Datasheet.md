# Datasheet — DEL-085-01 Scope of Work (PKG-085 Flare Stack (High Pressure))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-085-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | PKG-085 | `_CONTEXT.md`; PACKAGE_REGISTER row 58 |
| Package Name | Flare Stack (High Pressure) | PACKAGE_REGISTER row 58 |
| Workbook Tracking Number | 26020-02-25-001 | PACKAGE_REGISTER row 58 |
| Discipline | Mechanical | PACKAGE_REGISTER row 58 |
| WBS | 02 | PACKAGE_REGISTER row 58 |
| Type | EPC Scope of Work | DELIVERABLE_REGISTER row 312 |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER row 312 |
| Vendor-Owned (Reference) | TRUE — Reference/interface package | PACKAGE_REGISTER row 58 |
| Covers Scope Items | SOW-0087; SOW-0088; SOW-0089; SOW-0090 | `_CONTEXT.md`; SCOPE_LEDGER rows 88-91 |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | DELIVERABLE_REGISTER row 312 (ASSUMPTION — PACKAGE_HEURISTIC mapping) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Reference/interface package for the common HP/Cryo flare stack serving HP and cryogenic flare systems | PACKAGE_REGISTER row 58; SCOPE_LEDGER SOW-0088 |
| Major Included Equipment | HP flare stack FL-4120-1 and related downstream shared flare-stack interface content | SCOPE_LEDGER SOW-0089 |
| Stack Geometry — HP/Cryo | Sonic HP/Cryo flare stack, 660 mm OD x 60,957 mm tall | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Active Flare Basis (lines ~497-499) |
| HP Relief Header Size | 508 mm (20 in.) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Active Flare Basis (line ~499) |
| HP Knockout Drums Served | V-4100-2 (compressor area); V-4150-2 (tank farm) — manifold to HP flare | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~497) |
| KO Drum Transfer Pumps (HP) | P-4100-2 and P-4150-2 — truck-out or transfer to slop | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~497) |
| HP Loads Routed to Stack (representative) | Pig receiver vents; stabilizer flash/feed relief and blowdown; stabilizer tower relief and blowdown; SOC blowdown; MPFF; TEG contactor automated blowdown | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~354); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (lines ~585, 704, 813, 838-842) |
| Cross-Facility Status | Shared between 03-25 and 04-25; treated as interface/reference package | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~56); SCOPE_LEDGER SOW-0090 |
| Cost-Scope Treatment | Explicitly excluded from 3-25 costing scope; 4-25 shared asset (subject to boundary ruling) | SCOPE_LEDGER SOW-0090 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour hydrocarbon HP and cryogenic flare relief and blowdown | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines ~56, 497-499) |
| Operating Mode | Continuous availability for relief, planned blowdown, and emergency blowdown | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines ~497-501) |
| Staggered Blowdown Required | Yes — to limit maximum relief | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~501) |
| Detailed Blowdown Sequencing Source | W242510-PRC-REP-000003-001 Plant Shutdown and Blowdown Philosophy (external; not locally accessible) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~501) |
| Site Location | TBD (location TBD — not in accessible sources) | `TBD` |
| Design Pressure / Temperature (stack) | TBD — not stated in accessible source slices | `TBD` |
| Pilot, Ignition, Purge Provisions | TBD — not stated in accessible source slices for HP stack | `TBD` |
| Codes / Standards | TBD — governing standards (e.g., API 521, API 537) not enumerated in accessible source slices | `TBD` |

## Construction

| Item | Value | Source |
|---|---|---|
| Equipment Tag (HP stack) | FL-4120-1 | SCOPE_LEDGER SOW-0089 |
| Configuration | Self-supported sonic stack (configuration label per PACKAGE_REGISTER row 58 cross-reference to budgetary go-by document `24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf` — go-by only, not authoritative) | PACKAGE_REGISTER row 58 (ASSUMPTION on configuration; only the budgetary go-by names a self-supported dual stack arrangement) |
| OD | 660 mm | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~499) |
| Height | 60,957 mm | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~499) |
| Materials of Construction | TBD — not stated in accessible source slices | `TBD` |
| Foundation / Civil | TBD — civil/structural integration deferred to interface scope | `TBD`; PACKAGE_REGISTER row 58 lists Structural/Foundations/Supports interface type |
| Vendor Documentation Requirements | Detailed list per 26020-Package_Requirements.docx package heading 38 (source-binary; location TBD for clause-level rendering) | DELIVERABLE_REGISTER row 312 source field |

## References

- `_REFERENCES.md` (deliverable-local)
- `_CONTEXT.md` (deliverable-local)
- PACKAGE_REGISTER.csv row 58 — accepted GATE-07 snapshot
- DELIVERABLE_REGISTER.csv row 312 — accepted GATE-07 snapshot
- SCOPE_LEDGER.csv rows 88-91 (SOW-0087 through SOW-0090) — accepted GATE-07 snapshot
- OBJECTIVE_REGISTER.csv rows for OBJ-002, OBJ-004 through OBJ-010 — accepted GATE-07 snapshot
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Facility Overview, Active Flare Basis (lines ~56, 497-501, 548)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — flare-served service descriptions (lines ~585, 704, 813, 838-842)
- `_Sources/26020-Package_Requirements.docx` package heading 38 — binary; clause-level location TBD (no local markdown rendering identified)
- Budgetary go-by (non-authoritative): `Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf` — referenced by PACKAGE_REGISTER row 58 as go-by only
