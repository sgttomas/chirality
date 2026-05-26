# Procedure: DEL-102-03 — Construction Work Package (PKG-102)

This procedure covers two interpretations: (a) producing the CWP document set, and (b) using the CWP to execute construction at the workface. Both are required.

## Purpose

Produce, issue, and execute the Construction Work Package for PKG-102 Monolithic Concrete Foundations, ending in a documented turnover to commissioning.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` present and current.
- Accepted GATE-07 PROJECT_DECOMP snapshot (2026-05-24) available.
- Issued-for-Construction structural drawings (CAN/CSA A23.3) for the foundations within PKG-102. Source: DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2674).
- Geotechnical report values needed for the affected foundations are no longer TBD. Source: DBM-Deepcut/4-25_Deepcut_DBM.md §"Geotechnical and Topographical Assumptions" (lines ~2685-2696).
- Concrete materials, mix designs, and placement plans aligned to CSA A23.1/A23.2. Source: DBM-Deepcut/4-25_Deepcut_DBM.md (line ~2677).
- Declared upstream dependencies: none declared in PREPARATION (`_DEPENDENCIES.md`); the CWP author should run `TASK + dependency-extract` if foundation-specific upstream packages must be formally declared.
- Interface counterparts identified for both declared interface types. Source: INTERFACE_REGISTER.csv rows `IFC-1EDEDC0453`, `IFC-8283744B5B`.

## Steps

### Part A — Produce the CWP document set

1. Confirm scope boundary by listing the specific monolithic foundations included in PKG-102 (foundation ID, served equipment/structure, location). If detailed structural engineering has not yet produced this list, record as TBD and gate further production on that list.
2. Assemble ART-009507D767 (Construction work package): identification, scope, applicable codes (NBCC; CAN/CSA A23.3; CSA A23.1/A23.2; Canadian Foundation Engineering Manual), and reference to the geotechnical report. Source: DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis".
3. Produce ART-E8798F2006 (Installation and tie-in workface plan): sequencing, formwork, rebar placement, embeds and anchor bolt sets, pour windows, curing plan, and tie-in moves at each declared interface. Source: `_CONTEXT.md` Anticipated Artifacts; INTERFACE_REGISTER.csv.
4. Produce ART-66649A8AE4 (Construction interface and turnover checklist) covering: pre-pour readiness, pour records, post-pour inspections, interface walkdowns at the two declared interface types, and turnover sign-offs. Source: ARTIFACT_REGISTER.csv `ART-66649A8AE4`.
5. Issue the CWP for construction with appropriate review and approval signatures (human authorization required; agents may propose). Source: governance — K-AUTH-1.

### Part B — Execute construction using the CWP

6. Verify prerequisites at each pour:
   - IFC drawings current for the foundation being poured.
   - Geotechnical values used in design are no longer TBD for this foundation.
   - Mix design ticket matches the specified strength/exposure class. Source: DBM-Deepcut/4-25_Deepcut_DBM.md (line ~2677).
   - Ambient conditions within CSA A23.1 limits (cold/hot-weather provisions invoked as required — location TBD for project-specific addendum).
7. Place reinforcement, embeds, and anchor bolts; perform pre-pour inspection and document the hold-point release.
8. Pour and consolidate concrete per CSA A23.1; capture pour record (mix ticket, ambient conditions, cylinders cast).
9. Cure and protect per CSA A23.1; document curing duration and method.
10. Perform post-pour inspection: dimensional, anchor bolt as-built locations, surface tolerances. Document non-conformances and route through the project NCR process.
11. At each declared interface (`IFC-1EDEDC0453` Grading/Site Drainage/Spill Containment; `IFC-8283744B5B` Structural/Foundations/Supports), perform an interface walkdown with the counterpart package representative and record sign-off.
12. Verify top-of-foundation elevations and adjacent pad slopes against the design (1.5% nominal; 1.0% allowed at top-of-pile-cap critical areas). Source: DBM-Deepcut/4-25_Deepcut_DBM.md §"Site Grading and Surface Water Management" (line ~2710).
13. Assemble turnover dossier: pour records, cylinder test reports (per CSA A23.2), as-built survey, NCRs/dispositions, interface sign-offs.
14. Execute commissioning turnover using ART-66649A8AE4; obtain human sign-off; archive the dossier.

## Verification

| Check | How verified |
|---|---|
| IFC drawings current at each pour | Drawing log entry in pour record |
| Geotechnical inputs not TBD for poured foundation | Reference to dated geotechnical report section in pour record |
| Concrete meets specified strength | Cylinder test results per CSA A23.2 |
| Anchor bolt as-built within tolerance | Post-pour survey vs. IFC tolerance |
| Interface compatibility (both types) | Signed interface walkdown record |
| Turnover complete | Signed ART-66649A8AE4 checklist |
| Pad slope at top-of-foundation acceptable | As-built survey shows 1.5% (or documented 1.0% exception) |

## Records

- Issued-for-Construction CWP (ART-009507D767), workface plan (ART-E8798F2006), turnover checklist (ART-66649A8AE4).
- Pour records, mix tickets, cylinder test certificates (CSA A23.2).
- Pre-pour and post-pour inspection records, NCRs and dispositions.
- Interface walkdown sign-offs at `IFC-1EDEDC0453` and `IFC-8283744B5B`.
- As-built survey of foundation tops and adjacent grades.
- Final turnover dossier archived in the package record set (location TBD — project records management convention not in accessible sources).
