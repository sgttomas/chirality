# Package Datasheet Specification — Storage Bullets (PKG-059)

> Normative requirements that the Package Datasheet (`DEL-059-02`) shall satisfy. Requirements are drawn from the GATE-07 PROJECT_DECOMP snapshot (`SCOPE_LEDGER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`) and the DBM-Deepcut source slices listed in `_REFERENCES.md`.

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for the Storage Bullets package (`PKG-059`), which comprises two unstable condensate storage bullets and sixteen LPG product storage bullets supplied as a single vendor-engineered package.

### In scope

- Package identity, RFQ tag, scope items, and supported objectives.
- Major equipment attributes extracted from `26020-Package_Requirements.docx` package heading 14 (via SCOPE_LEDGER): count, dimensions, nominal volume, fill, design pressure/temperature, full vacuum, mounting, and access.
- Operating service for each bullet group (unstable C5 condensate vs LPG product) and downstream disposition.
- API 2510 spacing constraints carried in the Deepcut DBM that govern bullet plot-plan layout.
- Interface boundary between the Package Vendor scope and the EPC Integrator scope, expressed as the interface requirements matrix on the Datasheet.

### Out of scope

- Detailed mechanical design calculations (vessel wall thickness, PSV sizing, nozzle reinforcement). These remain with the package vendor.
- Construction Work Package content (covered by `DEL-059-03`).
- Vendor document submittals and turnover (covered by `DEL-059-05`).
- Vendor package review/acceptance (covered by `DEL-059-06`).
- Foundations, DCS integration, and electrical MCC supply (declared "by others" per SCOPE_LEDGER SOW-0184; carried by EPC discipline packages).

## Requirements

| ID | Requirement | Source / Note |
|---|---|---|
| REQ-DS-01 | The datasheet shall identify the package using the canonical decomposition IDs `PKG-059` and `DEL-059-02_package-datasheet`. | `_CONTEXT.md`; GATE-07 register |
| REQ-DS-02 | The datasheet shall identify the source RFQ tag `26020-01-PT-RFQ-17-007` (Pressure Vessels — Storage Bullets). | PACKAGE_REGISTER.csv (Source Basis) |
| REQ-DS-03 | The datasheet shall declare the package responsibility split: Package Vendor owns engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and tie-ins. | PACKAGE_REGISTER.csv |
| REQ-DS-04 | The datasheet shall list the two unstable condensate storage bullets and sixteen LPG product storage bullets and shall state their function (C5 condensate before transfer pumps; LPG product from depropanizer before transfer to off-site liquids hub). | SCOPE_LEDGER SOW-0182, SOW-0184 |
| REQ-DS-05 | The datasheet shall record bullet major dimensions exactly as in source: 3658 mm ID x 42494 mm S/S; nominal volume 454 m3 / 120,000 US gal; maximum fill 84%. | SCOPE_LEDGER SOW-0183 |
| REQ-DS-06 | The datasheet shall record bullet design conditions exactly as in source: design pressure 1724 kPag, design temperature 66 C, full vacuum (external). | SCOPE_LEDGER SOW-0183 |
| REQ-DS-07 | The datasheet shall record mounting and access exactly as in source: outdoor saddle mounting with stairs and platforms. | SCOPE_LEDGER SOW-0183 |
| REQ-DS-08 | The datasheet shall record vapour-equalization and blanket-gas constraints: LPG vapour equalization piping must avoid pockets; butane storage requires blanket gas. | SCOPE_LEDGER SOW-0184 |
| REQ-DS-09 | The datasheet shall record the explicit "by others" exclusions for foundations, DCS integration, and electrical MCC supply. | SCOPE_LEDGER SOW-0184 |
| REQ-DS-10 | The datasheet shall record the API 2510 pressurized-bullet spacing constraints from the Deepcut DBM (max 6 per cluster; inter-cluster 15.24 m; 38.1 m to property line; 30.48 m to flare; etc.). | DBM-Deepcut lines 245-259, 265-267, 284, 299 |
| REQ-DS-11 | The datasheet shall carry an Interface Requirements Matrix covering the ten interface types declared for PKG-059 (Process Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports). | INTERFACE_REGISTER.csv (10 PKG-059 rows); `_CONTEXT.md` Notes (interfaces carried as evidence here) |
| REQ-DS-12 | The datasheet shall mark all values not present in accessible source material as `TBD` (e.g., MOC, MAWP, nozzle schedule, internals, EHT specifics, per-bullet LPG service mix, RFQ-document parameters not yet parsed). | Skill rule: no invented values |
| REQ-DS-13 | The datasheet shall cite source for each non-trivial value (SourcePath + SectionRef or `location TBD`). Inferred items shall be labeled `ASSUMPTION`. | Skill source-grounding rule |
| REQ-DS-14 | The datasheet shall align with the package scope items covered by `DEL-059-02` (`SOW-0181`, `SOW-0182`, `SOW-0183`, `SOW-0184`). | `_CONTEXT.md`; SCOPE_LEDGER |
| REQ-DS-15 | The datasheet shall record the deliverable's supported objectives (`OBJ-001`, `OBJ-003`, `OBJ-004`..`OBJ-010`) per PACKAGE_HEURISTIC association (ASSUMPTION pending objective-to-deliverable confirmation). | `_CONTEXT.md`; skill default mode |
| REQ-DS-16 | The datasheet shall surface, but not silently reconcile, any discrepancy between source descriptions of bullet service (e.g., "LPG product" in SCOPE_LEDGER vs "NGL storage bullets" in DBM-Deepcut after depropanizer retirement). | Skill `CONFLICT:` rule; see CONF-01 in `Guidance.md` |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| API 2510 (Design and Construction of LPG Installations) | Pressurized bullet spacing, layout, and cluster limits (carried into DBM-Deepcut spacing table) | DBM-Deepcut lines 245-259, 265-267, 284, 299; full standard text location TBD |
| ASME BPVC Section VIII, Division 1 | Pressure-vessel design code for the bullets | ASSUMPTION (industry standard for LPG/condensate pressure-vessel bullets); not explicit in available source slice; full standard text location TBD |
| BC Boiler and Pressure Vessel Safety Regulation / CRN registration | Provincial pressure-vessel registration (British Columbia jurisdiction) | ASSUMPTION (project located in BC per facility context); not explicit in available source slice; location TBD |
| NFPA 30 (Flammable and Combustible Liquids Code) | Atmospheric tank spacing referenced alongside bullet spacing | DBM-Deepcut line 268 (Table 22.4.2.1); applies to adjacent atmospheric tanks rather than bullets directly; location TBD |
| OGAOM Sec. 9.6.15 (BC Oil and Gas Activity Operations Manual) | Flare/KO drum vegetation spacing — context for adjacent flare module | DBM-Deepcut line 287; location TBD |
| BCER Oil and Gas Processing Facility Regulation, Appendix 1, Schedule 1 | Thermal-radiation flux limits at flare boundaries — informs distance between bullets and flare | DBM-Deepcut lines 285-286; location TBD |
| `26020-Package_Requirements.docx` package heading 14 | EPC package requirements applicable to PKG-059 (the SCOPE_LEDGER source-of-record for bullet attributes) | Native .docx not parsed in this pass; SCOPE_LEDGER carries the extracted text |
| `26020-01-PT-RFQ-17-007` Pressure Vessels — Storage Bullets | Vendor RFQ specifying detailed bullet datasheet parameters | Not locally accessible in this pass; `location TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-DS-01 / REQ-DS-02 / REQ-DS-14 / REQ-DS-15 | Cross-check IDs and tags against GATE-07 registers and `_CONTEXT.md` during datasheet review. |
| REQ-DS-03 | Confirm responsibility split language matches PACKAGE_REGISTER row exactly. |
| REQ-DS-04 / REQ-DS-05 / REQ-DS-06 / REQ-DS-07 / REQ-DS-08 / REQ-DS-09 | Cross-reference numeric and textual values against SCOPE_LEDGER SOW-0182..SOW-0184 entries character-for-character. |
| REQ-DS-10 | Confirm spacing values match DBM-Deepcut Pressurized Bullet Spacing table (lines 245-259) and adjacent tables. |
| REQ-DS-11 | Confirm Interface Requirements Matrix on the Datasheet includes every interface row in INTERFACE_REGISTER for PKG-059. |
| REQ-DS-12 / REQ-DS-13 | Datasheet review confirms every value either has a citation, is labeled ASSUMPTION, or is labeled TBD. |
| REQ-DS-16 | Confirm conflict between SCOPE_LEDGER LPG/condensate service and DBM-Deepcut NGL bullet basis is captured in the Conflict Table in `Guidance.md`. |

## Documentation

The Package Datasheet deliverable shall include the following artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Package technical datasheet (`Datasheet.md`).
- Vendor engineering handoff basis (captured in `Datasheet.md` Attributes/Conditions/Construction and in `Guidance.md` Considerations/Trade-offs).
- Package interface requirements matrix (carried in `Datasheet.md` Interface Requirements Matrix section, with detailed EPC/Vendor split rows; vendor-document parsing of `26020-Packages_Interfaces_4_export.xlsx` remains TBD).
- Source-supported equipment and design criteria (captured in `Datasheet.md` Attributes/Conditions with citations to SCOPE_LEDGER and DBM-Deepcut).
- This Specification (`Specification.md`), Guidance (`Guidance.md`), and Procedure (`Procedure.md`).
