# Specification — DEL-093-02 Package Datasheet (Tanks, Water (API 650) 3-25)

## Scope

This Package Datasheet specifies the technical handoff content for `PKG-093` (Tanks, Water (API 650) 3-25). Per `PACKAGE_REGISTER.csv` row PKG-093, the authoritative package scope is **two 3,800 bbl Sweet Produced Water Storage Tanks (TK-9060-2, TK-9070-2)** at the 03-25 Liquids Hub, with sweet produced water / process water as the design service.

**In scope:**
- Equipment identity (TK-9060-2, TK-9070-2) and quantity (2 x 3,800 bbl).
- Tank design code (API 650 Modified) and construction features (external insulation, external heating, internal coating Devchem 253).
- Design conditions: design SG, ambient temperature, atmospheric pressure class, sweet-service classification.
- Package interfaces enumerated in `PACKAGE_REGISTER.csv` row PKG-093: Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports.

**Out of scope (for this deliverable, carried elsewhere):**
- Sour produced-water tanks (5 of 7 in the DBM family) — not part of PKG-093.
- Condensate tanks (eleven 3,800 bbl tanks) — not part of PKG-093.
- Detailed vendor mechanical drawings (vendor scope, `DEL-093-04`).
- Construction installation methodology (`DEL-093-03`).
- Vendor document turnover (`DEL-093-05`).

## Requirements

| Req-ID | Statement | Authority | Notes |
|---|---|---|---|
| REQ-093-02-001 | The package shall comprise two 3,800 bbl atmospheric storage tanks, identified as TK-9060-2 and TK-9070-2, in sweet produced-water / process-water service. | `PACKAGE_REGISTER.csv` row PKG-093 (Process Mechanical Scope, Process function) | Mandatory equipment identity. |
| REQ-093-02-002 | Tanks shall be designed and fabricated to API 650 Modified for atmospheric service. | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) | "Modified" clause text location TBD in `26020-Package_Requirements.docx` heading 45. |
| REQ-093-02-003 | Each tank shall be externally insulated and externally heated for -40 deg C ambient service. | `3-25_Comp_and_Liquids_DBM.md` §SEC-02 (line 145), §SEC-06 (line 421) | Heat-tracing detail TBD. |
| REQ-093-02-004 | Internal coating shall be Devchem 253 (or accepted equivalent — equivalence criteria TBD). | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) | DBM specifies Devchem 253 for produced-water tank family. |
| REQ-093-02-005 | Produced-water tank design SG shall be 1.25 (TBC in source). Pump-side SG of 1.18 shall be reconciled during detailed design. | `3-25_Comp_and_Liquids_DBM.md` §SEC-04 (line 176), §SEC-06 (line 421) | OPEN discrepancy. |
| REQ-093-02-006 | The package shall provide vapour collection ties to the facility VRU system (2 x 200 hp electric-drive packages, 2 x 100%). | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 436); `PACKAGE_REGISTER.csv` (Relief/Flare/Vent) | Under SCA-002, VRU discharges to 04-25 SOC. |
| REQ-093-02-007 | The package shall provide interface to the facility H2O2 treatment package (1 x, 3,840 m3/d TBC), where treated sweet water is allocated to or returned from this storage. | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 427) | Treatment-package boundary clause-level reference TBD. |
| REQ-093-02-008 | The package shall accept tank outflow through the facility 2 x 100% produced-water transfer pumps to pipeline or truck-out. | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 429, 432) | Pipeline downstream of facility riser by others. |
| REQ-093-02-009 | Each tank shall include a vacuum-truck connection (DBM ASSUMPTION basis 2.75 m3/min per tank). | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 430) | DBM labels this "assumed". |
| REQ-093-02-010 | Tank construction shall comply with the sour-service materials and welding rules of the governing package basis where applicable to produced-water service. | location TBD — `26020-Package_Requirements.docx` heading 45 | Clause text not locally accessible. Note PKG-093 service label is "Sweet" but H2S contingency review TBD. |
| REQ-093-02-011 | The package shall provide tie-in provisions for cathodic protection, grounding/bonding, area lighting, I&C/control cabling, drain/containment, and structural foundations/supports per the EPC interface basis. | `PACKAGE_REGISTER.csv` row PKG-093 (Applicable interface types) | Mandatory interface set. |
| REQ-093-02-012 | The package shall comply with the spill-containment, site drainage, and grading provisions defined by the facility civil basis at the tank bunds and surroundings. | `PACKAGE_REGISTER.csv` row PKG-093 (Grading/Site Drainage/Spill Containment) | Containment volumes TBD from civil basis. |

## Standards

| Standard | Applies To | Location |
|---|---|---|
| API 650 (Modified) | Tank design, materials, fabrication, testing | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421); modifications clause location TBD |
| Owner package requirements | All package interfaces, documentation, materials, welding | `26020-Package_Requirements.docx` heading 45 — clause-level location TBD |
| NACE / sour-service standards | Materials selection contingency (sweet-service designated but produced water is the duty) | location TBD; applicability ASSUMPTION pending owner clause review |
| BC water resource and discharge regulation | Produced-water handling at the facility level (context, not equipment design) | `3-25_Comp_and_Liquids_DBM.md` §SEC-12 (line 876) |

## Verification

| Req-ID | Verification Approach |
|---|---|
| REQ-093-02-001 | Equipment list / tag-number audit; vendor datasheet review (`DEL-093-04`). |
| REQ-093-02-002 | Vendor compliance matrix to API 650 Modified; nameplate/MTR review. |
| REQ-093-02-003 | Insulation and heat-tracing design review; cold-climate compliance check. |
| REQ-093-02-004 | Coating spec review; coating application QA records. |
| REQ-093-02-005 | Hydraulic and structural calculation review reconciling tank and pump SG bases. |
| REQ-093-02-006 | VRU suction interface line-list / P&ID review. |
| REQ-093-02-007 | Treatment-package P&ID and interface schedule review. |
| REQ-093-02-008 | Pump performance test; tie-in flange and class verification. |
| REQ-093-02-009 | Tank nozzle schedule audit. |
| REQ-093-02-010 | Materials selection diagram and MTR audit per governing sour/sweet-service basis. |
| REQ-093-02-011 | Interface punch-list against `PACKAGE_REGISTER.csv` applicable interface types; tie-in walkdown. |
| REQ-093-02-012 | Civil/structural review of bunds, drainage, and containment volumes. |

## Documentation

Anticipated outputs supported by this Package Datasheet (per `_CONTEXT.md`):
- Package technical datasheet (this deliverable's primary artifact).
- Vendor engineering handoff basis (input to `DEL-093-04`).
- Package interface requirements matrix (carried within this deliverable as the Interfaces section in `Datasheet.md`).
- Source-supported equipment and design criteria record.
