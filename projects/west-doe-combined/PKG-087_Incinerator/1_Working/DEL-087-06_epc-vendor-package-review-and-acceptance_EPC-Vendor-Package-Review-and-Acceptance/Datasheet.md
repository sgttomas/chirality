# Datasheet — DEL-087-06 EPC Vendor Package Review and Acceptance

> Descriptive document. Identifies the deliverable, its attributes, applicable conditions, and constituent records used by the EPC Integrator to review and accept the PKG-087 Incinerator vendor package.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-087-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-087` |
| PackageName | Incinerator |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | `SOW-0111`, `SOW-0112`, `SOW-0113`, `SOW-0114` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-heuristic association from PROJECT_DECOMP Objective-Deliverable Map, package-grouped) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator review and acceptance evidence package for the Incinerator vendor scope | DELIVERABLE_REGISTER.csv row 353 (GATE-07 snapshot) |
| Acceptance subject | Vendor package developed under DEL-087-04 (Vendor Engineered Equipment Package) and DEL-087-05 (Vendor Document Turnover Package) | DELIVERABLE_REGISTER.csv rows 351-352 (GATE-07 snapshot) — ASSUMPTION linkage |
| Acceptance reference docs (EPC side) | DEL-087-01 EPC Scope of Work, DEL-087-02 Package Datasheet, DEL-087-03 Construction Work Package | _CONTEXT.md Scope; DELIVERABLE_REGISTER.csv rows 348-350 |
| Constituent records | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | _CONTEXT.md Anticipated Artifacts; DELIVERABLE_REGISTER.csv row 353 |
| Equipment identity | Incinerator package (mercaptan treating service incinerator, fed by spent caustic and DSO off-gas, with upstream knock-out drum) | DBM-Deepcut sec "Incinerator Interface" (location: 4-25_Deepcut_DBM.md line ~1568) — applicability to PKG-087 is ASSUMPTION pending docx/xlsx slice confirmation |
| Package boundary attributes | TBD | location TBD (26020-Package_Requirements.docx, package heading 40) |
| Interface points (mechanical/process/electrical/I&C/civil) | TBD | location TBD (26020-Packages_Interfaces_4_export.xlsx row 64) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / facility | West Doe Deepcut expansion at facility 04-25; incinerator physically at 03-25 facility servicing the 04-25 NGL mercaptan treating system | DBM-Deepcut 4-25_Deepcut_DBM.md line ~1568-1570 (ASSUMPTION: PKG-087 = this incinerator) |
| Vapour feed sources | Spent caustic storage tank off-gas, DSO storage tank off-gas | DBM-Deepcut 4-25_Deepcut_DBM.md lines ~1562-1570 |
| Backflash protection on feed tanks | Flame arrestor required on tank-to-incinerator header | DBM-Deepcut 4-25_Deepcut_DBM.md lines ~1562, ~1564 |
| Supplemental fuel gas rate | TBC | DBM-Deepcut 4-25_Deepcut_DBM.md line ~1572 |
| Incinerator flow basis | TBC | DBM-Deepcut 4-25_Deepcut_DBM.md line ~1572 |
| Shared-facility (03-25/04-25) operational responsibility | TBC | DBM-Deepcut 4-25_Deepcut_DBM.md line ~1572, ~1812 |
| Dilution/enrichment gas | TBC | DBM-Deepcut 4-25_Deepcut_DBM.md line ~1890 |
| Spacing — flare/incinerator to nearest plant equipment | 25 m (82 ft) | DBM-Deepcut 4-25_Deepcut_DBM.md line ~280 (OGAOM Sec. 9.6.15) |
| Spacing — fired heater to flare/incinerator | 25 m (82 ft) | DBM-Deepcut 4-25_Deepcut_DBM.md line ~296 (OGAOM Sec. 9.6.15) |
| Thermal radiation boundary compliance | Required | DBM-Deepcut 4-25_Deepcut_DBM.md line ~316 |
| Emission basis (annual quantities) | TBD — current non-regenerative-caustic emissions basis remains to be confirmed | DBM-Deepcut 4-25_Deepcut_DBM.md lines ~2173, ~2186, ~2244-2246 |

## Construction (record types collected for acceptance)

| Record class | Contents | Owner |
|---|---|---|
| Vendor document review log | Per-document submittal IDs, revision, EPC review status (A/B/C or equivalent), comment resolution status | EPC Integrator |
| Package acceptance checklist | EPC-mapped acceptance criteria derived from SOW, Datasheet, and CWP; pass/fail/conditional entries | EPC Integrator |
| Test/inspection evidence | Vendor FAT, SAT, NDE, hydrotest, performance test reports; PWHT/heat-treatment records; nameplate verification | Package Vendor (executed); EPC Integrator (witness/review) |
| Turnover evidence | Mechanical completion certificates, punchlist (A/B), preservation records, training records, system handover certificate | EPC Integrator |
| Non-conformance / deviation log | NCRs, concessions, engineering dispositions referenced back to vendor submittals | EPC Integrator |
| Final data book / dossier index | TBD structure; cross-references all of the above | Package Vendor compiles; EPC Integrator accepts |

Specific equipment counts, tag numbers, datasheet attributes, and acceptance thresholds: **TBD** (location TBD — 26020-Package_Requirements.docx heading 40 and 26020-Packages_Interfaces_4_export.xlsx row 64).

## References

- `_REFERENCES.md` (this deliverable)
- `_CONTEXT.md` (this deliverable)
- Decomposition basis: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 353 (DEL-087-06)
- Decomposition basis: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-087-06
- DBM-Deepcut: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — sections "Flare and Incinerator Spacing" and "Incinerator Interface"
- 26020-Package_Requirements.docx (binary, heading 40) — **location TBD as text slice**
- 26020-Packages_Interfaces_4_export.xlsx (binary, row 64) — **location TBD as text slice**
