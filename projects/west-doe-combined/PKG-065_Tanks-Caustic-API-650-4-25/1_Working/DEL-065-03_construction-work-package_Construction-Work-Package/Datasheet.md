# Datasheet: DEL-065-03 — Construction Work Package (PKG-065 Tanks, Caustic (API 650) 4-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-065-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-065 |
| PackageName | Tanks, Caustic (API 650) 4-25 |
| Facility | 04-25 Deep Cut Gas Plant |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Covers SOW | SOW-0197; SOW-0198; SOW-0199; SOW-0200 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC mapping from DELIVERABLE_REGISTER row 488) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope | Atmospheric storage tanks supporting the 04-25 NGL non-regenerative caustic mercaptan treating system | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Disulphide Oil, Spent Caustic, and Waste Amine" (lines 526-534) |
| In-scope tanks | DSO storage tank (1 x 400 bbl) and spent caustic storage tank (1 x 400 bbl); ASSUMPTION: fresh-caustic/process-water/H2O2 tank inclusion at 04-25 is TBC pending tank register | 4-25 DBM lines 528, 530; ASSUMPTION |
| Tank code basis | API-650 (Modified) atmospheric tank; 16 oz test pressure | 4-25 DBM lines 518-519 |
| Maximum fill | 90% of tank volume; thermal expansion review required | 4-25 DBM line 519 |
| Service media | Spent caustic (NaOH-based); disulphide oil (DSO) | 4-25 DBM lines 528, 530 |
| Disposition | Truck-out for off-site disposal; alternate DSO blend into C5+ product under review | 4-25 DBM lines 528-530 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site minimum ambient | -40 deg C governs exposed equipment | 3-25 DBM line 145 (cross-cutting site basis) |
| Tank external treatment | Externally insulated and heated (basis from sibling produced-water tank treatment at 04-25; ASSUMPTION applies to caustic tank service) | 4-25 DBM line 524 (sibling reference); ASSUMPTION |
| Vent / pressure-relief | At least one PVRV per tank; EPRV sizing reviewed in detailed engineering (sibling basis from produced-water tanks) | 4-25 DBM line 524; ASSUMPTION extension to caustic tanks |
| Caustic material constraint | Aluminum shall not be used in caustic service buildings; coating/material details TBC | 3-25 DBM line 402 (analogous 03-25 caustic basis); ASSUMPTION extension |

## Construction

| Item | Value | Source |
|---|---|---|
| Tank construction standard | API-650 Modified, field-erected atmospheric tank | 4-25 DBM line 518 |
| Foundation | Engineered concrete ringwall/slab (TBD — not in accessible source slice) | TBD |
| Internal coating | TBD for caustic service; produced-water tanks use Devchem 253 — applicability to caustic service not asserted in source | TBD |
| External insulation/heat trace | Insulated and heated; circuit detail TBD | 4-25 DBM line 524 (sibling); ASSUMPTION |
| Erection sequence | TBD (not in accessible source slice) | TBD |
| Hydrotest / NDE | Per API-650 erection requirements; site-specific test plan TBD | API-650 (location TBD) |
| Tie-in interfaces | NGL caustic treating package inlet/outlet, truck-out loading station, drain header (300# ANSI minimum) | 3-25 DBM lines 493, 400 (analogous); ASSUMPTION |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (authoritative facility basis for 04-25)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (analogous caustic-service basis at 03-25; used only where 04-25 source is silent and labelled ASSUMPTION)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 488
- API-650 Welded Tanks for Oil Storage — location TBD (not in locally accessible source set)
- API 2510, NFPA 30, OGAOM Sec. 9.6.15 — spacing references (4-25 DBM lines 258-297) inform site layout but not construction details
