# Specification — DEL-087-06 EPC Vendor Package Review and Acceptance

> Normative document. States the requirements that the assembled review-and-acceptance evidence set must satisfy for the PKG-087 Incinerator vendor package, and how each requirement is verified.

## Scope

### Includes
- EPC Integrator's review of the Package Vendor's engineered equipment package (DEL-087-04) and vendor document turnover package (DEL-087-05) against:
  - DEL-087-01 EPC Scope of Work (SOW-0111..SOW-0114),
  - DEL-087-02 Package Datasheet,
  - DEL-087-03 Construction Work Package.
- Compilation of the vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence (per `_CONTEXT.md` Anticipated Artifacts).
- Acceptance disposition records (accept / accept with conditions / reject) with traceable justification.

### Excludes
- Authoring of the EPC SOW, Package Datasheet, or CWP themselves (those are DEL-087-01/02/03).
- Vendor's internal engineering, fabrication, and supply (covered by DEL-087-04).
- Vendor document register authoring (covered by DEL-087-05).
- Operations, maintenance, and post-handover lifecycle activities.

## Requirements

> Requirements are organized as **R-AC-#**. Each requirement maps to a verification approach in the Verification matrix and to a step in `Procedure.md`. Acceptance-criteria values that depend on the unread workbook row 64 / 26020 heading 40 slices are marked **TBD (location TBD)**.

| ID | Requirement | Authority |
|---|---|---|
| R-AC-01 | The acceptance evidence set SHALL include a vendor document review log enumerating every required vendor submittal, its current revision, EPC review code, comment-resolution status, and date of disposition. | _CONTEXT.md Anticipated Artifacts; DELIVERABLE_REGISTER.csv row 353 |
| R-AC-02 | The acceptance evidence set SHALL include a package acceptance checklist whose line items derive from the DEL-087-01 SOW (SOW-0111..SOW-0114), DEL-087-02 Datasheet, and DEL-087-03 CWP. Each line item SHALL carry a pass / fail / conditional disposition with traceable evidence references. | _CONTEXT.md Scope; DELIVERABLE_REGISTER.csv row 353 |
| R-AC-03 | The acceptance evidence set SHALL include test and inspection evidence covering, at minimum, vendor FAT, SAT (where applicable), NDE records, pressure-test records, performance-test records, and nameplate verification. Specific test scopes and acceptance thresholds: **TBD (location TBD — 26020-Package_Requirements.docx heading 40)**. | ASSUMPTION (industry-standard EPC package acceptance practice); requires source confirmation |
| R-AC-04 | The acceptance evidence set SHALL include turnover evidence: mechanical completion certificate(s), A/B punchlists, preservation records, training records (if scope), and system handover certificate. | _CONTEXT.md Anticipated Artifacts |
| R-AC-05 | Every non-conformance or concession SHALL be logged, dispositioned by engineering, and closed (or carried forward as a documented deviation) before package acceptance is granted. | ASSUMPTION (EPC quality practice) |
| R-AC-06 | Interface acceptance SHALL confirm the package satisfies all interfaces enumerated in the DEL-087-02 Package Datasheet interface matrix and in 26020-Packages_Interfaces_4_export.xlsx row 64. Specific interface points: **TBD (location TBD)**. | _REFERENCES.md (workbook row 64); DELIVERABLE_REGISTER.csv row 353 |
| R-AC-07 | The incinerator package SHALL be verified to meet flare/incinerator spacing of at least 25 m (82 ft) from the nearest plant equipment and 25 m (82 ft) from any fired heater, and the thermal-radiation boundary SHALL comply with applicable regulatory requirements. | DBM-Deepcut `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines ~280, ~296, ~316 (OGAOM Sec. 9.6.15) — applicability to PKG-087 is ASSUMPTION pending source confirmation |
| R-AC-08 | The acceptance review SHALL confirm presence and integrity of the upstream knock-out drum and flame arrestor backflash protection on the spent caustic and DSO off-gas headers feeding the incinerator. | DBM-Deepcut `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines ~1562, ~1564, ~1568-1570 — applicability ASSUMPTION |
| R-AC-09 | Open-at-acceptance design parameters (supplemental fuel gas rate, incinerator flow basis, dilution/enrichment gas rate, 03-25/04-25 operational responsibility) SHALL be resolved or explicitly carried as TBC deviations with a defined closure path before acceptance is granted. | DBM-Deepcut `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines ~1572, ~1812, ~1890 |
| R-AC-10 | A single acceptance disposition (Accepted / Accepted with Conditions / Rejected) SHALL be recorded for the package, signed by the EPC Integrator authority, with cross-references to each underlying evidence record. | ASSUMPTION (K-AUTH-1 — only humans author binding acceptance) |
| R-AC-11 | Acceptance evidence SHALL be retained per the project document-control basis, and shall be re-issuable on audit. Retention period: **TBD (location TBD)**. | TBD |
| R-AC-12 | Objectives `OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` are package-grouped to this deliverable; objective-specific acceptance criteria: **TBD (location TBD — objective text not extracted to deliverable scope)**. | OBJECTIVE_DELIVERABLE_MAP.csv (package-heuristic); ASSUMPTION |

## Standards

| Standard / Document | Use | Local availability |
|---|---|---|
| 26020-Package_Requirements.docx heading 40 | Defines package-specific scope, acceptance criteria, vendor document requirements | Present as binary; **text slice TBD** |
| 26020-Packages_Interfaces_4_export.xlsx row 64 | Defines package interfaces and counterparty disciplines | Present as binary; **text slice TBD** |
| DBM-Deepcut design basis (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) | Site spacing, incinerator interface, design-basis open items | Accessible (markdown) |
| OGAOM Sec. 9.6.15 | Spacing criteria (cited via DBM-Deepcut) | Cited only; primary text **location TBD** |
| Applicable provincial/federal emissions regulations | Thermal-radiation and air-emissions boundary compliance | **location TBD** |
| Project document-control procedure | Evidence retention and reissue | **location TBD** |

## Verification

| Requirement | Verification approach | Evidence record |
|---|---|---|
| R-AC-01 | Document review of vendor submittal register against required-document list | Vendor document review log |
| R-AC-02 | Line-by-line traceback of checklist items to SOW/Datasheet/CWP source rows | Package acceptance checklist |
| R-AC-03 | Witness/review of FAT, SAT, NDE, pressure test, performance test; nameplate inspection | Test/inspection evidence dossier |
| R-AC-04 | Walk-down and document review at mechanical completion | Turnover evidence dossier |
| R-AC-05 | Audit of NCR/concession log against acceptance disposition | NCR log |
| R-AC-06 | Interface matrix cross-check against workbook row 64 (TBD) | Acceptance checklist (interface section) |
| R-AC-07 | Site survey / plot-plan check against 25 m criteria; thermal-radiation calculation review | Acceptance checklist (siting section) |
| R-AC-08 | Visual inspection and P&ID/datasheet conformance check of KO drum and flame arrestors | Inspection record |
| R-AC-09 | Review of TBC/deviation log with closure plan dates | NCR/deviation log |
| R-AC-10 | Human-signed acceptance disposition record | Acceptance disposition document |
| R-AC-11 | Audit of document-control system retention metadata | Document-control audit record |
| R-AC-12 | Mapping of acceptance disposition items to OBJ-002/004/005-010 (TBD) | Objective traceability appendix |

## Documentation

Artifacts to be produced under this deliverable (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist (mapped to SOW-0111..SOW-0114 and Package Datasheet attributes)
- Test/inspection evidence dossier (or pointers to vendor-held dossier)
- Turnover evidence dossier
- Non-conformance / deviation log
- Acceptance disposition record (human-signed)
- Objective traceability appendix (R-AC-12)
