# Datasheet — DEL-065-06 EPC Vendor Package Review and Acceptance

EpistemicStatus: DRAFT (Pass 1/Pass 2 — source-grounded with explicit TBDs)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-065-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` Identity |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-065` (Tanks, Caustic API 650, 4-25) | `_CONTEXT.md` Identity |
| WorkbookID | 65 (Packages row 87) | `_CONTEXT.md` Source Reference |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| DeliverableType | EPC Vendor Package Acceptance | `_CONTEXT.md` Identity |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` Identity |
| Decomposition row | DELIVERABLE_REGISTER.csv row 491 (GATE-07 Final Published 2026-05-24) | `_REFERENCES.md` |

## Attributes (Package Under Acceptance)

| Attribute | Value | Source |
|---|---|---|
| Package subject | Caustic storage tanks for the NGL non-regenerative caustic (mercaptan) treating unit | DBM-Deepcut `4-25_Deepcut_DBM.md` §"NGL Mercaptan Treating" and §"Disulphide Oil, Spent Caustic, and Waste Amine" |
| Tank specification basis | API 650 (per package title "Tanks, Caustic (API 650) 4-25") | PACKAGE_REGISTER.csv / package name; ASSUMPTION: clause-level API 650 requirements not yet excerpted (location TBD) |
| Fresh caustic storage tank | 1 x 400 bbl, atmospheric, heated, insulated, truck-in capable, fuel-gas blanketed, not connected to VRU header | DBM-Deepcut line 1528, 1562 |
| Spent caustic storage tank | 1 x 400 bbl, atmospheric, heated, insulated, truck-out capable, incinerator-header connected, flame-arrestor protected, low-pressure fuel-gas blanketed | DBM-Deepcut line 1529, 1562 |
| Fresh caustic concentration | 50 wt% NaOH | DBM-Deepcut line 1526 |
| Fresh caustic tank design specific gravity | 1.75 (TBC) | DBM-Deepcut line 1562 |
| Indoor installation | All caustic treating equipment installed indoors; caustic-containing equipment segregated to Mercaptan Treating Unit building or immediately adjacent area | DBM-Deepcut line 1552 |
| Material constraints | No aluminum in caustic building; insulation cladding/straps in caustic exposure areas SS; caustic storage tanks must use polymer or other caustic-compatible materials | DBM-Deepcut line 1566 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service fluid (fresh) | 50 wt% NaOH caustic solution | DBM-Deepcut line 1526 |
| Service fluid (spent) | Used caustic from NGL mercaptan-treating contactor and pressurized caustic drain drum | DBM-Deepcut lines 1554, 1560, 1562 |
| Off-gas routing (spent) | Vapours to incinerator (located at 3-25, services 4-25); KO drum upstream of incinerator | DBM-Deepcut lines 1570 |
| Freezing/crystallization risk | Yes — heated and insulated tanks; indoor installation | DBM-Deepcut lines 1552, 1562 |
| Safety provisions | Building safety showers (quantity and locations TBD; activation must provide discrete control-room alert) | DBM-Deepcut line 1552 |

## Construction / Acceptance Attributes (Scope of This Deliverable)

| Acceptance artifact | Status / Source |
|---|---|
| Vendor document review log | Anticipated artifact per `_CONTEXT.md`; content TBD |
| Package acceptance checklist | Anticipated artifact per `_CONTEXT.md`; checklist content TBD pending vendor package and EPC SOW/Datasheet/CWP |
| Test / inspection evidence | Anticipated artifact per `_CONTEXT.md`; specific tests TBD |
| Turnover evidence | Anticipated artifact per `_CONTEXT.md`; format TBD |
| Acceptance basis documents | EPC Scope of Work (DEL-065-01), Package Datasheet (DEL-065-02), Construction Work Package (DEL-065-03) | `_CONTEXT.md` Scope |
| Vendor inputs | Vendor Engineered Equipment Package (DEL-065-04); Vendor Document Turnover Package (DEL-065-05) | DELIVERABLE_REGISTER.csv rows 489, 490 |

## Scope Items Covered

- `SOW-0197`, `SOW-0198`, `SOW-0199`, `SOW-0200` (`_CONTEXT.md`)

## Objectives Supported

- `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic per OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC)

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- GATE-07 Final Published PROJECT_DECOMP snapshot (deliverable register row 491)
- `26020-Package_Requirements.docx` package heading 20 — location TBD (binary file, slice not extracted)
- API 650 — location TBD (not locally accessible)
