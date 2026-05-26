# Datasheet — DEL-070-06 EPC Vendor Package Review and Acceptance

> Deliverable type: EPC Vendor Package Acceptance (descriptive datasheet of the acceptance object and its evidentiary attributes). The "object" here is the EPC Integrator's acceptance instrument for the PKG-070 Mole Sieve Drier Unit (NGL) vendor package — not the vendor equipment itself, which is described in DEL-070-04.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-070-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| Parent Package ID | `PKG-070` | `_CONTEXT.md` |
| Package Name | Mole Sieve Drier Unit (NGL) | `_CONTEXT.md` |
| Workbook Row | Packages row 74 | `_CONTEXT.md` Source Reference |
| Source Heading | `26020-Package_Requirements.docx` package heading 24 | `_CONTEXT.md` Source Reference; **location TBD** (DOCX not locally extracted) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Acceptance Object | EPC Integrator package-acceptance record for PKG-070 vendor package | ASSUMPTION (deliverable-type convention; DOCX heading 24 not accessible) |
| Covered Scope Items | `SOW-0145`, `SOW-0146`, `SOW-0147`, `SOW-0148` | `_CONTEXT.md` |
| Supported Objectives | `OBJ-001`, `OBJ-003`–`OBJ-010` | `_CONTEXT.md` (PACKAGE_HEURISTIC — ASSUMPTION) |

## Attributes (acceptance instrument)

| Attribute | Value | Source |
|---|---|---|
| Acceptance scope | Vendor document review, integration acceptance, and handoff readiness against the EPC Scope of Work (DEL-070-01), Package Datasheet (DEL-070-02), and Construction Work Package (DEL-070-03) | `_CONTEXT.md` Scope |
| Subject vendor package | Mole sieve drier unit for NGL service (PKG-070) | `_CONTEXT.md`; DBM-Deepcut §"NGL molecular sieve dehydration" (line 73) |
| Acceptance evidence classes | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Acceptance lead | EPC Integrator | `_CONTEXT.md`; deliverable register row for `DEL-070-06` |
| Vendor input role | Package Vendor (clarifications, RFI responses, ITP/QA records, turnover documents from DEL-070-05) | `_CONTEXT.md` ResponsibleParty |
| Acceptance authority | Human EPC Integrator authorized signatory (binding approval) | ASSUMPTION (K-AUTH-1; not stated in DBM) |
| Upstream inputs | DEL-070-01 SOW; DEL-070-02 Package Datasheet; DEL-070-03 CWP; DEL-070-04 Vendor Engineered Equipment Package; DEL-070-05 Vendor Document Turnover Package | Sibling deliverable IDs in PKG-070 working folder; ASSUMPTION on review-pipeline ordering |

## Conditions (review and acceptance context)

| Condition | Value | Source |
|---|---|---|
| Subject-package service | Process gas / NGL molecular sieve dehydration (final dehydration upstream of cryogenic recovery) | DBM-Deepcut §"Molecular-Sieve Dehydration and Mercury Removal Basis" (line 1239); §Process Description line 1243 |
| Subject-package critical performance | Outlet water content expected <0.1 ppmv H2O; dewpoint <-90 degC; cryogenic limit dewpoint <-75 degC | DBM-Deepcut §Molecular-Sieve Design Values (line 1254–1255) |
| Subject-package adsorbent constraint | 3A molecular sieve mandatory; 4A/5A not permitted | DBM-Deepcut line 1269 |
| Subject-package BAHX protection | New-bed bring-online gas temperature must not exceed 66 degC | DBM-Deepcut line 1257 |
| Acceptance environment | Facility 04-25 West Doe Deepcut expansion; mole sieve module adjacent to cryogenic modules | DBM-Deepcut line 1249; line 1134 |
| Permitting context | BC Energy Regulator amendment granted for 300 MMSCFD train (subject to Section 12.4 site-alteration permit; waste discharge permit amendment required) | DBM-Deepcut line 131 |

## Construction / composition (acceptance package contents)

The acceptance package is a composite artifact set produced during EPC integration review.

| Component | Content | Source |
|---|---|---|
| Vendor document review log | Per-document log against DEL-070-05 turnover package: document ID, revision received, reviewer, comments, disposition (Accept / Accept w/ Comments / Revise & Resubmit / Reject), close-out reference | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on log columns |
| Package acceptance checklist | Itemized check of vendor package against SOW (DEL-070-01), Package Datasheet (DEL-070-02), and CWP (DEL-070-03) clauses; SOW-0145 through SOW-0148 line items | `_CONTEXT.md` Covers Scope Items; scope-item content **TBD** (SOW deliverable not yet drafted) |
| Test / inspection evidence | Vendor FAT records, ITP signoffs, NDE reports, hydrostatic / pressure-test certificates, instrumentation calibration records; field SAT records as applicable | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on standard EPC integration practice |
| Turnover evidence | Receipt of DEL-070-05 turnover package; verification that operating manuals, spare parts lists, recommended-spares interchange records, and as-built marked-up drawings are present and complete | `_CONTEXT.md` Anticipated Artifacts; sibling DEL-070-05 |
| Acceptance disposition record | Final EPC Integrator acceptance signature(s), date, conditional-acceptance items, residual open items, and reference to issue/closeout tracker | ASSUMPTION (K-AUTH-1 binding-approval convention) |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Molecular-Sieve Dehydration and Mercury Removal Basis" (lines 1239–1291); §"NGL Treating and Dehydration" reference at line 73
- Gate 7 PROJECT_DECOMP snapshot deliverable register and objective-deliverable map (cited in `_REFERENCES.md`)
- `26020-Package_Requirements.docx` package heading 24 — **location TBD** (binary DOCX; not extracted locally)
- Sibling deliverables in PKG-070 1_Working: DEL-070-01, -02, -03, -04, -05 (upstream evidence sources)
