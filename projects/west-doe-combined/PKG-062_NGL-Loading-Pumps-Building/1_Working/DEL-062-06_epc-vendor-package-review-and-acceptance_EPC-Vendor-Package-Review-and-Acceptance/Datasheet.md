# Datasheet — DEL-062-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-062-06_epc-vendor-package-review-and-acceptance | _CONTEXT.md |
| Name | EPC Vendor Package Review and Acceptance | _CONTEXT.md |
| ParentPackageID | PKG-062 | _CONTEXT.md |
| PackageName | NGL Loading Pumps Building | _CONTEXT.md; DBM-Deepcut 4-25_Deepcut_DBM.md line 2549 |
| LSD (Area) | 4-25 (Deepcut) | DBM-Deepcut 4-25_Deepcut_DBM.md line 2610 |
| Discipline | Mechanical | _CONTEXT.md |
| Type | EPC Vendor Package Acceptance | _CONTEXT.md |
| ResponsibleParty | EPC Integrator (lead), Package Vendor (input) | _CONTEXT.md |
| Workbook Row | Packages row 76 | _CONTEXT.md (location TBD — xlsx not parsed) |
| Source Heading | 26020-Package_Requirements.docx package heading 16 | _CONTEXT.md (location TBD — docx not parsed) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment count | 4 | DBM-Deepcut line 2549, 2610 |
| Equipment tags in package | P-9510-1, P-9520-1, P-9530-1, P-9540-1 | DBM-Deepcut line 2610 |
| Pump technology family | Rotary vane | DBM-Deepcut line 2610 ("Pumps (rotary vane)") |
| Service | NGL loading | DBM-Deepcut line 73, 2549 |
| Housing | Building (NGL Loading Pumps Building) | DBM-Deepcut line 2549 |
| Deliverable purpose | EPC integrator review and acceptance of the vendor-supplied package | _CONTEXT.md Scope |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating fluid | NGL (light hydrocarbon liquid product) | DBM-Deepcut line 73 (ASSUMPTION: confirmed package service is NGL loading) |
| Sparing philosophy | TBD (four pumps grouped under "NGL Loading Pumps") | location TBD — vendor datasheet not local |
| Design pressure / temperature / flow | TBD | location TBD — package datasheet (DEL-062-02) not consumed |
| Material class | TBD | location TBD |
| Driver type | TBD | location TBD |
| Seal plan | TBD | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | NGL Loading Pumps Building (pumps, baseplates, drivers, ancillaries within building battery limits) | DBM-Deepcut line 2549 (ASSUMPTION on detailed battery limits) |
| Acceptance artifact set | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | _CONTEXT.md Anticipated Artifacts |
| Upstream artifacts informing acceptance | EPC Scope of Work; Package Datasheet; Construction Work Package; Vendor Engineered Equipment Package; Vendor Document Turnover Package | _CONTEXT.md Scope (ASSUMPTION on detailed acceptance criteria — sibling deliverables not consumed) |

## Covered Scope Items

- SOW-0153
- SOW-0154
- SOW-0155
- SOW-0156

Source: _CONTEXT.md Covers Scope Items. Underlying SOW row text: location TBD (not extracted in this run).

## Supports Objectives

OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010. ASSUMPTION (best-effort, PACKAGE_HEURISTIC): associations sourced from _CONTEXT.md Supports Objectives; objective text not extracted in this run.

## References

- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md (package roster + line item, lines 2549, 2610; NGL service line 73)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx (package heading 16 — location TBD; docx not parsed locally)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx (Packages row 76 — location TBD; xlsx not parsed locally)
- _CONTEXT.md (deliverable identity, scope, supports/covers lists)
- _REFERENCES.md (decomposition snapshot pointers)
- GATE-07 PROJECT_DECOMP snapshot 2026-05-24 (deliverable register row for DEL-062-06)
