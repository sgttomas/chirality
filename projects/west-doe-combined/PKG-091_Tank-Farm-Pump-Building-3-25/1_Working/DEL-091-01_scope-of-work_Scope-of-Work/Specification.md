# Specification — DEL-091-01 Scope of Work (PKG-091 Tank Farm Pump Building 3-25)

> Normative scope-of-work specification for the EPC Integrator Scope of Work
> deliverable for the Tank Farm Pump Building 3-25 package (PKG-091). Requirements
> are derived from the GATE-07 PROJECT_DECOMP snapshot
> (`SCOPE_LEDGER.csv` rows SOW-0185…SOW-0188, `PACKAGE_REGISTER.csv` row PKG-091,
> `INTERFACE_REGISTER.csv` PKG-091 rows). Source material referenced by the
> decomposition (`26020-Package_Requirements.docx` heading 44; Packages workbook
> row 84) is not locally accessible as text slices; requirements that would
> require those slices are marked `TBD` or `ASSUMPTION` and not invented.

## Scope

### In scope (this Scope of Work shall cover)

- Identification of the PKG-091 Tank Farm Pump Building 3-25 package as a
  distinct, vendor-responsible Mechanical package (Workbook row 84, WBS 03)
  carried into the project as a flat package per SCOPE_LEDGER SOW-0185.
- Statement of the package process function as the tank-farm pump building,
  containing water-transfer pumps, sour- and sweet-condensate pumps, and a
  building drain pump per SCOPE_LEDGER SOW-0186.
- Tagged equipment list for the included pumps as enumerated in SCOPE_LEDGER
  SOW-0187 (tags `P-9200-2`, `P-9210-2`, `P-9211-2`, `P-9215-2`, `P-9216-2`,
  `P-9220-2`, `P-9221-2`, `P-9230-2`, `P-9240-2`, `P-9290-2`, `P-9293-2`,
  `P-9295-2`).
- Source basis statement (Workbook Packages row 84; 26020-Package_Requirements.docx
  heading 44).
- Battery-limit / boundary definition between Package Vendor and EPC Integrator
  responsibilities per `PACKAGE_REGISTER.csv` ResponsibilityModel and SCOPE_LEDGER
  SOW-0185.
- Whole-facility integration narrative covering the 15 applicable interface
  types listed in `INTERFACE_REGISTER.csv` for PKG-091.
- Responsibility assignment record referencing the EPC Integrator (this
  deliverable) and the Package Vendor (DEL-091-04, DEL-091-05).
- Cross-references to the sibling Gate-5 deliverables: DEL-091-02 Package
  Datasheet, DEL-091-03 Construction Work Package, DEL-091-04 Vendor
  Engineered Equipment Package, DEL-091-05 Vendor Document Turnover Package,
  DEL-091-06 EPC Vendor Package Review and Acceptance.

### Out of scope (this deliverable shall not include)

- Detailed per-tag pump datasheets (delegated to DEL-091-02 Package Datasheet).
- Construction installation, tie-in workface, inspection, and turnover content
  (DEL-091-03 Construction Work Package).
- Vendor engineering, design, fabrication, and the physical equipment package
  (DEL-091-04 Vendor Engineered Equipment Package).
- Vendor document register, submittals, and turnover records (DEL-091-05
  Vendor Document Turnover Package).
- DCS integration, foundations, and electrical supply to the MCC — explicitly
  "by others" per SCOPE_LEDGER SOW-0188.

## Requirements

### R1 — Package identification

R1.1 The Scope of Work shall identify the package as `PKG-091 Tank Farm Pump
Building 3-25`, WBS 03, Discipline Mechanical, Workbook row 84, Word source
heading 44 (`PACKAGE_REGISTER.csv`; SCOPE_LEDGER SOW-0185).

R1.2 The Scope of Work shall identify the Package Vendor tracking number
`26020-03-18-001` and the Word source tracking title
`26020-03-PT-18-002 — Tank Farm Pumps` (`PACKAGE_REGISTER.csv`).

### R2 — Process function and basic scope

R2.1 The Scope of Work shall state the package process function: house all
pumps for the Tank Farm 3-25 with water-transfer pumps in parallel feeding the
produced-water pipeline through a bag filter; sour-condensate booster pumps
feeding the condensate-sweetening feed pumps; and the additional condensate
and drain services per SCOPE_LEDGER SOW-0186.

R2.2 The Scope of Work shall enumerate the basic-scope pump types and counts
as stated in SCOPE_LEDGER SOW-0186 (1 building drain pump (pneumatic diaphragm);
2 water transfer pumps (radial centrifugal); 2 sour-condensate pumps (vertical
inline centrifugal); 2 condensate-sweetening feed pumps (vertical inline
centrifugal); plus the recycle, skim, and booster pumps enumerated in SOW-0187).

### R3 — Tagged equipment list

R3.1 The Scope of Work shall present a tagged equipment list naming each pump
tag with type, drive, rated point (where stated), and seal plan (where stated)
per SCOPE_LEDGER SOW-0187. Values not stated in the source slice shall be
recorded as `TBC` or `TBD` and not invented.

R3.2 ASSUMPTION: per-tag datasheets are produced by DEL-091-02 Package
Datasheet. This Scope of Work shall reference DEL-091-02 for per-tag detail
rather than duplicate it.

### R4 — Drivers and electrical interface

R4.1 The Scope of Work shall state that all pumps are driven by 575 V / 3 Ph /
60 Hz motors with starting method DOL or VFD, local H-O-A or On-Off switch
control, and fed from a 600 V MCC (SCOPE_LEDGER SOW-0188).

R4.2 The Scope of Work shall state that motors are sized for inlet stabilizer
composition density at -40 °C start-up condition (SCOPE_LEDGER SOW-0188).

### R5 — Boundary and responsibility split

R5.1 The Scope of Work shall state the responsibility split: Package Vendor
owns package engineering, package design, vendor documentation, and the
physical equipment package; EPC Integrator owns integration into the functional
process facility, including interfaces, tie-ins, constructability, procurement/
construction coordination, and facility-level integration
(`PACKAGE_REGISTER.csv` ResponsibilityModel; SCOPE_LEDGER SOW-0185).

R5.2 The Scope of Work shall explicitly identify the "by others" exclusions:
DCS integration, foundations, and electrical supply to the MCC (SCOPE_LEDGER
SOW-0188).

### R6 — Whole-facility integration narrative

R6.1 The Scope of Work shall include a whole-facility integration narrative
covering each of the 15 applicable interface types recorded for PKG-091 in
`INTERFACE_REGISTER.csv`: Process Piping; Utility Piping; Relief / Flare /
Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area /
Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC /
Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site
Drainage / Spill Containment; Structural / Foundations / Supports.

R6.2 For each applicable interface type, the narrative shall identify the
EPC-owned tie-in/integration scope at the package battery limit. Interface
type-specific tie-in detail beyond the GATE-07 register rows is `TBD` and shall
be developed against the EPC engineering deliverables for those disciplines.

### R7 — Open items carried forward

R7.1 The Scope of Work shall carry forward as `TBC`/`TBD` the items the
source explicitly leaves open: operating specs; design conditions; rated
points for the Sour Condensate Booster Pump, Sweet Condensate Feed Pump,
Condensate Booster Pump, and Condensate Loading; inlet basket strainer size
for P-9240-2 (SCOPE_LEDGER SOW-0187, SOW-0188).

R7.2 The Scope of Work shall mark `TBD` any item that is not stated in the
accessible source slices (e.g., sour-service / NACE applicability, site
ambient design conditions, package-specific materials). Inferences shall be
labeled `ASSUMPTION`.

### R8 — Objectives traceability

R8.1 The Scope of Work shall trace the package to objectives OBJ-002 through
OBJ-010 per `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC mapping;
ASSUMPTION until confirmed by the human owner).

## Standards

| Standard | Use | Source / Location |
|---|---|---|
| API-682 (mechanical seals) | Cited as the seal-plan basis (Plan 14/52) for vertical-inline centrifugal pumps in the package | SCOPE_LEDGER SOW-0187; clause location TBD (API-682 text not locally accessible) |
| NACE (sour-service materials) | TBD — applicability to sour-condensate services not stated in accessible source slices; standard location TBD | TBD |
| Project process mechanical package requirements (`26020-Package_Requirements.docx` heading 44) | Word-source basis cited by GATE-07; not locally accessible as text | location TBD |
| Project packages workbook (`26020-Packages_Interfaces_4_export.xlsx` row 84) | Workbook-source basis cited by GATE-07; not locally accessible as text | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| R1 (identification) | Inspection — Scope of Work contains the stated identifiers and source references; cross-checked against `PACKAGE_REGISTER.csv` PKG-091. |
| R2 (function/basic scope) | Inspection — narrative matches SCOPE_LEDGER SOW-0186 wording without invention; bag-filter and parallel water-transfer arrangement explicitly stated. |
| R3 (tagged equipment) | Inspection — pump tags, types, ratings, and seal plans match SOW-0187; missing values marked `TBC`/`TBD`. |
| R4 (drivers) | Inspection — voltage / phase / frequency, starting method, MCC source, and -40 °C sizing basis match SOW-0188. |
| R5 (boundary/responsibility) | Inspection — responsibility split matches `PACKAGE_REGISTER.csv` ResponsibilityModel; "by others" list matches SOW-0188. |
| R6 (interface narrative) | Inspection — the 15 interface types are each present in the narrative and traceable to `INTERFACE_REGISTER.csv` PKG-091 rows. |
| R7 (open items) | Inspection — explicit `TBC`/`TBD` markings present for all source-stated open items. |
| R8 (objectives traceability) | Cross-reference — objectives OBJ-002…OBJ-010 are listed and labeled as `PACKAGE_HEURISTIC` ASSUMPTION. |
| R3.2, R5.1, R5.2 (cross-deliverable handoffs) | Cross-reference — sibling deliverables DEL-091-02 through DEL-091-06 are named in the Scope of Work and their roles are not duplicated. |

## Documentation

The following artifacts result from this deliverable (per `_CONTEXT.md`
"Anticipated Artifacts"):

- Package scope of work (this deliverable's narrative Scope of Work document).
- Tagged equipment and package identity list (table per R3).
- Package function and integration narrative (per R2 and R6).
- Responsibility assignment record (per R5).
