# Specification — Construction Work Package (DEL-059-03)

> Normative requirements for the PKG-059 Storage Bullets EPC Construction Work Package. The CWP describes how the package will be installed, built, inspected, turned over, and tied into the larger 04-25 facility. Requirements are sourced from the GATE-07 accepted decomposition snapshot and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. The cited `26020-Package_Requirements.docx` package heading 14 is referenced by the decomposition but is not available as locally readable text; clause-level requirements from that document are marked `location TBD`.

## Scope

### In Scope

- All physical installation work to receive, set, align, and tie in 16 x 120,000 USG NGL storage bullets at 04-25 (Deepcut), consistent with the current DBM basis (DBM-Deepcut lines 448, 492, 1629).
- Civil scope local to the bullet field: foundations, grading per slope basis, berm or surface-control feature, drainage continuity to facility drainage / spill containment (DBM-Deepcut line 2722).
- Piping tie-ins from the package boundary to facility systems: NGL inlet from upstream treating/dehydration; NGL outlet to product/booster pumps and the LACT to NRM NEBC Connector (DBM-Deepcut lines 73, 492, 1408).
- Relief and flare tie-ins for pressurized bullets to the applicable flare header per detailed design (relief routing TBD; location TBD).
- Drainage and containment tie-ins consistent with NGL storage area grading and containment basis (DBM-Deepcut line 2722).
- Electrical, grounding, EHT-where-applicable, area lighting, I&C / control cabling, fire & gas / safety system tie-ins for the bullet field, including beacon group near the NGL Storage Area (DBM-Deepcut line 3262; remaining E&I scope TBD pending `26020-Package_Requirements.docx` heading 14).
- Construction-phase inspections, line walk-downs, pre-commissioning leak / pressure / dryness / purge work for new piping at the package boundary.
- Construction interface and turnover checklist; mechanical completion turnover record set.

### Out of Scope

- Bullet vendor engineering, design, fabrication, and the physical bullet equipment package itself (responsibility of the Package Vendor; tracked separately under `DEL-059-04` Vendor Engineered Equipment Package and `DEL-059-05` Vendor Document Turnover Package).
- Adjacent atmospheric storage tank construction (4 x 3,800 bbl condensate product tanks at 04-25; DBM-Deepcut line 1639 — separate package).
- Detailed bullet design parameters not yet developed in the product-storage basis (DBM-Deepcut line 1629 / 1814 — open design-development item; consumed when issued by the vendor package).

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| CWP-001 | The Construction Work Package shall enable installation of 16 x 120,000 USG NGL storage bullets at 04-25 (Deepcut). | DBM-Deepcut lines 448, 492, 1629 | Layout drawing review against DBM; ITP signoff. |
| CWP-002 | The bullet field layout shall meet API 2510 spacing as listed in DBM-Deepcut lines 245-266, 284, 299 (cluster size <=6; cluster-to-cluster 15.24 m; bullet-to-property-line 38.1 m; bullet-to-flare 30.48 m; bullet-to-fired-heater 15.24 m; bullet-to-process-vessel 15.24 m; bullet-to-control-building 15.24 m; bullet-to-non-control-building 30.48 m; bullet-to-truck-loading-station 15.24 m; bullet-to-nearest-atmospheric-tank 30.48 m; bullet-to-nearest-spill-containment 3.05 m; bullet-to-related-pump-skid 3.05 m; bullet-to-unrelated-rotating-equipment 15.24 m). | DBM-Deepcut lines 245-266, 284, 299 (API 2510) | Layout dimensional review; spacing verification walk-down. |
| CWP-003 | Site grading under and around the NGL storage bullets shall provide a berm, elevation decline, or other surface-control feature to contain accidental leaks/spills and redirect NGL away from the pipe rack and process areas (slope potentially southbound). | DBM-Deepcut line 2722 | Civil drawing review; as-built grading survey. |
| CWP-004 | Construction shall provide the tie-ins required for product run-down to the NRM NEBC Connector via LACT. | DBM-Deepcut line 492 | Line walk-down; system test against P&ID. |
| CWP-005 | Construction shall provide the tie-ins required to upstream NGL treating/dehydration and to the NGL product pumps / NGL product booster pumps / NGL loading. | DBM-Deepcut lines 73, 1408 | Line walk-down; interface checklist (see CWP-013). |
| CWP-006 | Pressurized vessel relief routing for the bullets shall connect to the facility flare system per detailed design. Header selection and sizing are determined by relief load analysis (location TBD pending detailed design and `26020-Package_Requirements.docx` heading 14). | DBM-Deepcut lines 245-299 (bullet-to-flare spacing implies tie-in scope); location TBD | Relief routing P&ID review; flare load model record. |
| CWP-007 | A facility alarm beacon group shall be installed near the NGL Storage Area as part of construction scope or interface coordination. | DBM-Deepcut line 3262 | Installation verification; beacon group commissioning record. |
| CWP-008 | Inspection scope shall include hydrotest / pressure test of new tie-in piping, NDE of welds to facility ITP, and verification of vessel code stamps and vendor-furnished test records at receipt. | ASSUMPTION (standard EPC ITP); `26020-Package_Requirements.docx` heading 14 expected to govern — location TBD | Signed ITP records; hydrotest certificates; NDE reports. |
| CWP-009 | Pre-commissioning shall include line flushing, leak testing, dryness verification, and inert purge of NGL-service lines prior to introduction of hydrocarbons. | ASSUMPTION (standard EPC pre-commissioning practice) — location TBD | Pre-commissioning checklists; purge certificates. |
| CWP-010 | Mechanical completion turnover shall produce a documented turnover package consisting of, at minimum: signed ITP records, weld maps and NDE results, hydrotest certificates, vessel code documentation, vendor document handoff (per `DEL-059-05`), red-line as-builts, and the construction interface / turnover checklist (DEL-059-03 anticipated artifact). | `_CONTEXT.md` Anticipated Artifacts; GATE-07 deliverable register | Turnover dossier review; acceptance per `DEL-059-06`. |
| CWP-011 | The CWP shall identify and resolve installation interfaces for all PKG-059 interface types declared in the GATE-07 `PACKAGE_REGISTER.csv` row PKG-059: Process Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | GATE-07 `PACKAGE_REGISTER.csv` row PKG-059 | Interface checklist signoff; per-interface walk-down. |
| CWP-012 | Construction sequencing shall maintain the physical and inspection independence of the package bullets from the adjacent atmospheric storage tank area (produced water / condensate tanks; DBM-Deepcut lines 1639, 3262). | DBM-Deepcut lines 1639, 3262 | Sequencing plan review; interface beacon-group installation record. |
| CWP-013 | The CWP shall produce an Installation and Tie-in Workface Plan and a Construction Interface and Turnover Checklist as required anticipated artifacts. | `_CONTEXT.md` Anticipated Artifacts | Artifact presence and completeness review. |
| CWP-014 | Detailed bullet design parameters required to finalize foundation, support, EHT/insulation, and tie-in geometry shall be obtained from the vendor package (DEL-059-04) before the affected construction work face is released. | DBM-Deepcut lines 1629, 1814 (design-development items) | Vendor data approval record prior to work-face release. |
| CWP-015 | Cathodic protection scope at the bullet field shall be defined by the detailed design (location TBD). | location TBD | CP design package review when issued. |

ASSUMPTION: CWP-008, CWP-009, CWP-010 reflect standard EPC inspection and turnover practice in the absence of a locally readable `26020-Package_Requirements.docx` package heading 14. Clause-level citations are deferred (location TBD) and should be reconciled when the package requirements document is locally accessible.

## Standards

| Standard | Application | Source / Note |
|---|---|---|
| API 2510 (LPG installations) | Pressurized bullet spacing in the bullet field | DBM-Deepcut lines 245-266, 284, 299. The LPG terminology is retained as a spacing-code descriptor under API 2510; it does not redefine current NGL product-handling scope (DBM-Deepcut note adjacent to spacing tables). |
| API 2510 Table 1 | Bullet-to-property-line distance (38.1 m / 125 ft) | DBM-Deepcut line 259 |
| Vessel pressure code (ASME BPVC Section VIII or equivalent jurisdictional code) | Bullet design and code-stamp verification | ASSUMPTION (standard for pressurized storage bullets); location TBD |
| NFPA 30 / API 2510 spacing for adjacent atmospheric tanks | Interface to adjacent condensate / produced water tank area | DBM-Deepcut spacing tables (atmospheric-tank rows); location TBD for governing standard at that interface |
| Facility ITP and weld / NDE program | Construction inspection of tie-in piping | location TBD — `26020-Package_Requirements.docx` heading 14 expected to govern |
| Project HSE / construction standards | Construction execution and safety | location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| CWP-001, CWP-002 | Drawing review and dimensional walk-down against DBM spacing table |
| CWP-003 | Civil drawing review and post-grading topographical survey |
| CWP-004, CWP-005, CWP-006, CWP-011 | Per-interface line walk-down and signed Interface and Turnover Checklist |
| CWP-007, CWP-012 | Installation verification and beacon-group commissioning record |
| CWP-008 | Signed ITP, hydrotest certificates, NDE reports, vessel code documentation |
| CWP-009 | Pre-commissioning checklists, purge certificates |
| CWP-010 | Turnover dossier acceptance under `DEL-059-06` review and acceptance |
| CWP-013 | Document presence and completeness review |
| CWP-014 | Recorded vendor data approvals against work-face release register |
| CWP-015 | CP design package review when issued |

## Documentation

Required documentation (from `_CONTEXT.md` Anticipated Artifacts):

- Construction Work Package (this deliverable's primary artifact)
- Installation and Tie-in Workface Plan
- Construction Interface and Turnover Checklist

Additional construction-execution evidence (per CWP-008..CWP-010):

- Signed ITPs, hydrotest and NDE records, vessel code records, pre-commissioning records
- As-built red-line drawings
- Vendor document handoff record (interfacing with `DEL-059-05` Vendor Document Turnover Package)

ASSUMPTION: The exact dossier structure should align with `26020-Package_Requirements.docx` package heading 14 once that document is locally accessible (location TBD).
