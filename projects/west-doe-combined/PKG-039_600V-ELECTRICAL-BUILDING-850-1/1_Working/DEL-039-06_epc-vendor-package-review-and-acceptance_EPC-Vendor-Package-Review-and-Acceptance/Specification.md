# Specification: DEL-039-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC-Integrator review of, and acceptance evidence for, the Package Vendor production unit and turnover documentation associated with package `PKG-039 — 600V ELECTRICAL BUILDING (850-1)` (Sales/Overheads compressor 600 V electrical building per the facility electrical distribution narrative).

**Covered:**
- Review of the vendor engineered equipment package (`DEL-039-04`) against the EPC Scope of Work (`DEL-039-01`), Package Datasheet (`DEL-039-02`), and Construction Work Package (`DEL-039-03`).
- Review of the vendor document turnover package (`DEL-039-05`) for completeness, source-required content, and interface fidelity.
- Production of the vendor document review log, package acceptance checklist, factory/shop test and inspection evidence record, and turnover evidence record.

**Excluded:**
- Authoring of vendor engineering, drawings, vendor datasheets, or vendor test reports (Package Vendor responsibility under `DEL-039-04`/`DEL-039-05`).
- Binding acceptance / sign-off (human authority only; agent outputs are proposals).
- Authoring of the EPC Scope of Work, Package Datasheet, or Construction Work Package (separate deliverables `DEL-039-01`..`DEL-039-03`).
- Cathodic protection engineering and supply (excluded from the facility design scope per the electrical design basis; supports owner interface only).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-039-06-01 | The EPC Integrator shall review the vendor engineered equipment package (`DEL-039-04`) against the three anchor EPC documents (`DEL-039-01` Scope of Work, `DEL-039-02` Package Datasheet, `DEL-039-03` Construction Work Package) and shall record each review comment and disposition in the Vendor document review and comment log (`ART-3910447327`). | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-039-01`..`DEL-039-06`; `ARTIFACT_REGISTER.csv` row `ART-3910447327` |
| REQ-039-06-02 | The EPC Integrator shall produce a package acceptance and turnover checklist (`ART-AA4BFB86C9`) covering each interface row for `PKG-039` in `INTERFACE_REGISTER.csv` and confirming consistency with the EPC Package Datasheet interface matrix. | `ARTIFACT_REGISTER.csv` row `ART-AA4BFB86C9`; `INTERFACE_REGISTER.csv` rows for `PKG-039` |
| REQ-039-06-03 | The EPC Integrator shall record factory/shop test and inspection evidence (`ART-0156F0196A`) for the prefabricated, shop-fabricated 600 V electrical building before facility installation; specific test types, witness points, and acceptance thresholds shall be drawn from the vendor inspection and test plan (ITP). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" and equipment-list row 2815; `ARTIFACT_REGISTER.csv` row `ART-0156F0196A` |
| REQ-039-06-04 | The acceptance record shall demonstrate that vendor design and installation evidence complies with CSA C22.1-21 Canadian Electrical Code, applicable BC provincial and local electrical codes, and the requirements of the Tourmaline-designated electrical inspection authority. Standards-body applicability includes CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical compliance paragraph (line 2866) |
| REQ-039-06-05 | The acceptance record for the Electrical Power interface (`IFC-C1DF6B8DD9`) shall demonstrate alignment with the facility radial distribution from the 13.8 kV main switchgear through step-down transformers to the 600 V electrical building. | `INTERFACE_REGISTER.csv` `IFC-C1DF6B8DD9`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Power Distribution" |
| REQ-039-06-06 | The acceptance record for the Grounding / Bonding interface (`IFC-9653B84E14`) shall demonstrate that major electrical equipment is connected to the ground grid at two points and that a ground well is provided at the electrical building per the design basis. | `INTERFACE_REGISTER.csv` `IFC-9653B84E14`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Grounding and Bonding" |
| REQ-039-06-07 | The acceptance record for the Structural / Foundations / Supports interface (`IFC-E3D0A5A836`) shall demonstrate that the building is elevated and installed on piles with bottom entry for incoming and outgoing cables. | `INTERFACE_REGISTER.csv` `IFC-E3D0A5A836`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" |
| REQ-039-06-08 | The acceptance record for the Building HVAC / Services interface (`IFC-D8A8F7FEBC`) shall demonstrate that climate control is sized as an n + 1 system so the cooling system can tolerate failure or maintenance of one HVAC unit without affecting building heating and cooling. | `INTERFACE_REGISTER.csv` `IFC-D8A8F7FEBC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" |
| REQ-039-06-09 | The acceptance record for the Maintenance Access interface (`IFC-D971A17948`) shall demonstrate that equipment doors are sized for, or include removable transom sections to allow, removal of the largest equipment, and that cable tray routing does not interfere with maintenance access. | `INTERFACE_REGISTER.csv` `IFC-D971A17948`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings", "Cable Tray and Conduit" |
| REQ-039-06-10 | The acceptance record for the I&C / Control Cabling, Communications / Network, and Area / Exterior Lighting interfaces (`IFC-3F18DB0D3A`, `IFC-B95212AB85`, `IFC-4BC9BD20C1`) shall demonstrate that vendor-supplied cabling and lighting match the facility cable/raceway basis (ACIC instrumentation, armored tray-rated communications, LED lighting suitable for area classification). | `INTERFACE_REGISTER.csv` rows; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Cable, Wire, and Raceways", "Lighting and Receptacles" |
| REQ-039-06-11 | The vendor document turnover package (`DEL-039-05`) shall be reviewed for completeness against the EPC Scope of Work, Package Datasheet, and Construction Work Package; gaps shall be recorded in the review log and tracked to closure before acceptance. | `DELIVERABLE_REGISTER.csv` rows `DEL-039-05`, `DEL-039-06` |
| REQ-039-06-12 | Binding acceptance shall be authored by a human (EPC Integrator authorized reviewer). Agent-produced drafts of the review log, checklist, and turnover evidence are proposals; they MUST NOT be treated as binding acceptance. | K-AUTH-1 (CONTRACT) |
| REQ-039-06-13 | ASSUMPTION: The acceptance scope covers Vendor Document Turnover (`DEL-039-05`) under the same review/acceptance authority as the Vendor Engineered Equipment Package (`DEL-039-04`), because `_CONTEXT.md` names "vendor document review log" among the anticipated artifacts. To be confirmed by human ruling. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-039-06` |

## Standards

| Standard / authority | Applicability | Location |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Electrical design, installation, testing, inspection. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2866 |
| Applicable BC provincial and local electrical codes and regulations | Provincial/local electrical compliance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2866 |
| Tourmaline-designated electrical inspection authority requirements | Field inspection acceptance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2866 |
| CSA, API, IEEE, ISA, NEMA | Standards bodies applicable to electrical materials, equipment, instrumentation, and panels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2866 |
| WorkSafeBC, Technical Safety BC, BCER | Regulatory bodies for worker safety, equipment safety, and BC Energy Regulator oversight. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2866 |
| NEMA VE2 | Cable tray support detail where shop drawings do not include a support detail. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Cable Tray and Conduit" |
| Vendor inspection and test plan (ITP) | Specific FAT/SAT test types, witness points, and acceptance thresholds; `location TBD` until vendor ITP is received. | Source gap (vendor-supplied) |

## Verification

| Req ID(s) | Verification approach |
|---|---|
| REQ-039-06-01, REQ-039-06-11 | Documentation review against `DEL-039-01`/`DEL-039-02`/`DEL-039-03` anchors; closeout of each review-log comment with vendor disposition. |
| REQ-039-06-02, REQ-039-06-05..REQ-039-06-10 | Interface-by-interface checklist walk-through using `INTERFACE_REGISTER.csv` rows for `PKG-039` and the Package Datasheet interface matrix. |
| REQ-039-06-03 | Witness, document, or signoff of factory/shop test and inspection results; record evidence in `ART-0156F0196A`. |
| REQ-039-06-04 | Compliance evidence package (code-compliance statements, inspection authority acceptance, third-party certifications). |
| REQ-039-06-12 | Authorized human signature on the acceptance checklist (`ART-AA4BFB86C9`); agent submissions remain in proposal state. |

## Documentation

- Vendor document review and comment log (`ART-3910447327`).
- Vendor package acceptance and turnover checklist (`ART-AA4BFB86C9`).
- Factory/shop test and inspection evidence record (`ART-0156F0196A`).
- Turnover evidence record (form / index `TBD` pending vendor turnover documentation).
- Conflict Table entries (in `Guidance.md`) for any unresolved review findings requiring human ruling.
