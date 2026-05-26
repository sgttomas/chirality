# Specification — DEL-085-03 Construction Work Package (Flare Stack, High Pressure)

## Scope

This Construction Work Package (CWP) governs the EPC Integrator scope for the
physical installation, tie-in, inspection, turnover, and facility-integration
of `PKG-085` (Flare Stack, High Pressure) — specifically the self-supported
dual flare stack serving HP/Cryo and LP services, shared between the 03-25
compressor/liquids facility and the 04-25 gas plant
(Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56,
497-499, 548).

### Included
- Foundation works, anchorage, and erection of the dual flare stack
  (Source: `3-25_Comp_and_Liquids_DBM.md` line 700).
- Installation of HP and LP relief header tie-ins (each DN 500 / 20 in) from
  the upstream KO drums (V-4100-2, V-4150-2, V-3900-2) to the flare riser
  flanges (Source: `3-25_Comp_and_Liquids_DBM.md` lines 497, 499).
- Installation of KO drum transfer-pump piping interfaces
  (P-4100-2, P-4150-2, P-3900-2) where they belong to facility integration
  rather than the vendor skid (Source: lines 497, 499, 583-584).
- Installation of facility interfaces listed for PKG-085: Utility Piping;
  Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding;
  I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/
  Supports (Source: `PACKAGE_REGISTER.csv` PKG-085 "Applicable interface types").
- Construction inspection, pre-commissioning hand-over, and turnover packaging
  per `DELIVERABLE_REGISTER.csv` DEL-085-03 anticipated artifacts.

### Excluded
- Package engineering, package design, vendor documentation, and the physical
  equipment package itself — these are Package Vendor scope under DEL-085-04
  (Source: `PACKAGE_REGISTER.csv` PKG-085 "Discipline Responsibility Note";
  `DELIVERABLE_REGISTER.csv` DEL-085-04).
- Vendor document turnover content (DEL-085-05).
- EPC vendor review and acceptance evidence (DEL-085-06).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| CWP-085-03-R-001 | Construction shall install the self-supported dual flare stack with HP/Cryo riser 660 mm OD x 60,957 mm tall to within tolerances defined by vendor engineering. | `3-25_Comp_and_Liquids_DBM.md` line 499; tolerance values TBD (vendor). |
| CWP-085-03-R-002 | HP relief header tie-ins shall be made up at DN 500 / 20 in nominal size and routed from HP KO drums V-4100-2 and V-4150-2 manifolded to the HP flare. | `3-25_Comp_and_Liquids_DBM.md` lines 497, 499. |
| CWP-085-03-R-003 | LP relief header tie-in shall be made up at DN 500 / 20 in nominal size and routed from LP KO drum V-3900-2 to the LP flare. | `3-25_Comp_and_Liquids_DBM.md` line 499. |
| CWP-085-03-R-004 | Foundation, anchorage, and structural support for the flare stack shall be installed to the final geotechnical and structural design basis (snow/wind/seismic/frost/vibration/settlement). | `3-25_Comp_and_Liquids_DBM.md` line 700. Final basis: `location TBD`. |
| CWP-085-03-R-005 | All eight PKG-085 interface types (utility piping, relief/flare/vent, drain/containment, electrical power, grounding/bonding, I&C/control cabling, fire & gas/safety, structural/foundations/supports) shall be installed and inspected against the EPC Scope of Work and Package Datasheet. | `PACKAGE_REGISTER.csv` PKG-085. |
| CWP-085-03-R-006 | Grounding/bonding of the flare stack and associated piping shall be installed and verified prior to first hydrocarbon introduction. | ASSUMPTION (industry standard for flare systems); specific code clause `location TBD`. |
| CWP-085-03-R-007 | Fire & Gas detection (LEL, H2S, methyl mercaptan, fire) at the flare/vent interfaces shall be installed per the project F&G layout. | `3-25_Comp_and_Liquids_DBM.md` line 838. Detector quantity, tag list, set points: TBD (per source). |
| CWP-085-03-R-008 | The shared 03-25 / 04-25 service-split and ownership at the dual stack shall be installed per the resolved interface allocation. | `3-25_Comp_and_Liquids_DBM.md` lines 56, 548. Resolution: TBD — see Guidance Conflict Table. |
| CWP-085-03-R-009 | Construction shall produce: (a) construction work package, (b) installation and tie-in workface plan, (c) construction interface and turnover checklist. | `DELIVERABLE_REGISTER.csv` DEL-085-03 "Anticipated Artifacts". |

## Standards

| Standard | Applicability | Status |
|---|---|---|
| Vendor engineering specification (24292-02-PT-ENR-25-201, Self-Supported Dual Flare Stack R1) | Defines vendor-supplied flare stack design basis; CWP installation tolerances follow vendor design. | Referenced; `location TBD` (slice not locally accessible). |
| 26020-Package_Requirements.docx, package heading 38 | Defines package requirements for Flare Stack (High Pressure). | Referenced; `location TBD` (slice not locally accessible). |
| API STD 537 (Flare details), API STD 521 (Pressure-relieving and depressuring), CSA Z662 (where pipeline-jurisdictional tie-ins apply), local AHJ structural and electrical codes. | TBD — likely applicable based on discipline; not explicitly cited in accessible sources. | ASSUMPTION. |

## Verification

| Requirement | Verification Method |
|---|---|
| CWP-085-03-R-001 | Survey + dimensional check vs vendor drawings; erection record. |
| CWP-085-03-R-002, R-003 | Piping isometric walkdown; weld map; NDE per project NDE plan (plan: TBD). |
| CWP-085-03-R-004 | Foundation inspection records (rebar, concrete strength, anchor bolt grout); structural sign-off. |
| CWP-085-03-R-005 | Interface checklist (one row per interface type) signed at turnover. |
| CWP-085-03-R-006 | Grounding continuity test record. |
| CWP-085-03-R-007 | F&G loop checks and pre-commissioning detector functional tests. |
| CWP-085-03-R-008 | Interface ownership confirmation memo signed by 03-25 and 04-25 operators (TBD). |
| CWP-085-03-R-009 | Document register completeness check at turnover. |

## Documentation

Required turnover artifacts (matching `DELIVERABLE_REGISTER.csv` DEL-085-03):
- Construction work package (this document set plus subordinate work packs)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Inspection/NDE records (TBD — project NDE plan governs)
- Grounding/bonding test records
- F&G pre-commissioning functional test records
- Punch list and turnover acceptance record (to feed DEL-085-06)
