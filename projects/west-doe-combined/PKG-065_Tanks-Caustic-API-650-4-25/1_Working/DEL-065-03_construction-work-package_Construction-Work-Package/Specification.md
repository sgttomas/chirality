# Specification: DEL-065-03 — Construction Work Package (PKG-065)

## Scope

This Construction Work Package (CWP) defines how the PKG-065 Tanks, Caustic (API 650) production unit at the 04-25 Deep Cut Gas Plant shall be physically installed, built, inspected, turned over, and tied into adjacent facility systems. The package covers the caustic-service atmospheric tanks supporting the 04-25 NGL non-regenerative caustic mercaptan treating system, namely the DSO storage tank and spent caustic storage tank identified in the 4-25 DBM, and any additional caustic-service tanks confirmed by the tank register (TBD).

Excluded: process package mechanical equipment outside of tankage; pipeline interfaces beyond facility tie-in flanges; vendor-supplied skid-internal piping (DEL-065-04 vendor scope).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| R-01 | Tanks shall be constructed to API-650 Modified atmospheric tank requirements with 16 oz test pressure. | 4-25 DBM line 518 |
| R-02 | Maximum normal fill shall not exceed 90% of tank volume; thermal expansion review shall be completed. | 4-25 DBM line 519 |
| R-03 | Each tank shall have at least one PVRV; EPRV sizing shall be reviewed during detailed engineering. (ASSUMPTION applied from sibling tank requirement.) | 4-25 DBM line 524; ASSUMPTION |
| R-04 | Tanks shall be externally insulated and heated. (ASSUMPTION applied from sibling tank requirement; circuit basis TBC.) | 4-25 DBM line 524; ASSUMPTION |
| R-05 | Aluminum shall not be used in caustic service materials, fittings, or building components. | 3-25 DBM line 402; ASSUMPTION extension to 04-25 |
| R-06 | Caustic drain interface shall be 300# ANSI minimum at the spent-caustic tank flange. | 3-25 DBM line 493 (analogous); ASSUMPTION |
| R-07 | Spent caustic and DSO tanks shall provide truck-out loading capability. | 4-25 DBM lines 528-532 |
| R-08 | Spent caustic tank vent path shall route to incinerator header via flame arrestor where applicable. | 3-25 DBM line 402 (analogous); ASSUMPTION |
| R-09 | Tank spacing shall comply with API 2510, NFPA 30 Table 22.4.2.1, and OGAOM Sec. 9.6.15 as applicable to atmospheric tank service. | 4-25 DBM lines 268-270, 282-287 |
| R-10 | Internal coating for caustic service is TBD; selection shall be confirmed prior to coating procurement. | TBD |
| R-11 | Hydrotest, NDE, and erection inspection shall be performed per API-650 Section on testing (location TBD). | API-650 location TBD |
| R-12 | Construction tie-in to the NGL caustic treating package shall be coordinated with DEL-065-04 (Vendor Engineered Equipment Package) and the package scope-of-work boundary. | Decomposition (DELIVERABLE_REGISTER row 488 context) |

## Standards

| Standard | Use | Locally accessible? |
|---|---|---|
| API-650 Welded Tanks for Oil Storage (Modified) | Construction, inspection, testing | No (location TBD) |
| API 2510 | Spacing for pressurized bullets vs. atmospheric tanks | Cited in 4-25 DBM (excerpt only) |
| NFPA 30 Table 22.4.2.1 | Atmospheric tank spacing | Cited in 4-25 DBM (excerpt only) |
| OGAOM Sec. 9.6.15 | Flare/heater/road spacing | Cited in 4-25 DBM (excerpt only) |

## Verification

| Requirement | Verification Method |
|---|---|
| R-01, R-02 | Review of fabricator API-650 design package; witness hydrotest |
| R-03, R-04 | Mechanical completion checklist; PVRV factory certs; trace circuit commissioning |
| R-05, R-10 | Material/coating receiving inspection; vendor MTR review |
| R-06, R-07, R-08 | Walkdown of drain, truck-out, and vent piping against P&IDs (P&IDs TBD) |
| R-09 | Layout audit against site plot (plot plan TBD) |
| R-11 | Hydrotest record; NDE report package |
| R-12 | Interface checklist signed with DEL-065-04 vendor at mechanical completion |

## Documentation

Required artifacts at turnover (from `_CONTEXT.md` Anticipated Artifacts and CWP convention):

- Construction work package document (this CWP and supporting work plans)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Hydrotest and NDE record set (TBD detail)
- Mechanical completion certificate per tank
- Punch list and clearance record
- Red-line as-built markups for handoff to DEL-065-06 (EPC Vendor Package Review and Acceptance, ASSUMPTION analog to DEL-088-06)
