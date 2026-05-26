# Specification: DEL-076-01 — Scope of Work (Lube Oil Supply)

Pass: P1 (initial draft); Pass 2 consistency sweep applied.

## Scope

### In Scope (EPC Integrator-authored Scope of Work for PKG-076)

The EPC Integrator shall produce a Scope of Work that defines, for the Lube Oil Supply package (PKG-076), all of the following [Source: `DELIVERABLE_REGISTER.csv` row 384; `_CONTEXT.md`]:

1. Full package scope statement covering supply of two (2) lube oil transfer pumps for the West Doe Deepcut facility Storage Tank Area, serving all compressor packages on site [`SCOPE_LEDGER.csv` SOW-0136].
2. Tagged equipment and package identity list:
   - P-9240-1 Cylinder Lube Oil Transfer Pump
   - P-9250-1 Crankcase Lube Oil Transfer Pump
   - Horizontal split storage tank (cylinder + crankcase oils)
   [`SCOPE_LEDGER.csv` SOW-0137].
3. Package function and integration narrative explaining how the package supplies cylinder and crank-case lube oil from heated bulk storage to compressor frame day tanks across the facility [`SCOPE_LEDGER.csv` SOW-0136, SOW-0137; `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis].
4. Responsibility assignment record: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration [`PACKAGE_REGISTER.csv` row 70; `ARTIFACT_REGISTER.csv` ART-369E16AA74].
5. Source basis citations (workbook row 70; `26020-Package_Requirements.docx` package heading 30) [`DELIVERABLE_REGISTER.csv` row 384].
6. Whole-facility integration narrative covering the declared interface types listed in the Datasheet.

### Out of Scope

- Package engineering, design, vendor documentation, and physical equipment supply (these are covered by `DEL-076-04_vendor-engineered-equipment-package`) [`DELIVERABLE_REGISTER.csv` row 387].
- Package datasheet content (carried in `DEL-076-02_package-datasheet`) [`DELIVERABLE_REGISTER.csv` row 385].
- Construction work package execution detail (carried in `DEL-076-03_construction-work-package`) [`DELIVERABLE_REGISTER.csv` row 386].
- Vendor document register and turnover (carried in `DEL-076-05_vendor-document-turnover-package`) [`DELIVERABLE_REGISTER.csv` row 388].
- EPC vendor package review/acceptance evidence (carried in `DEL-076-06_epc-vendor-package-review-and-acceptance`) [`DELIVERABLE_REGISTER.csv` row 389].
- Shipping to site, installation on piles, tie-in piping, electrical connections, and mounting platform/stairs (explicitly "by others" in source SoW) [`SCOPE_LEDGER.csv` SOW-0138].

## Requirements

### R-01 — Package Identity Statement (Mandatory)

The Scope of Work shall identify the package as PKG-076 Lube Oil Supply, workbook row 70, WBS 01, Mechanical discipline, CoA tracking number 26020-01-29-001, vendor package title 26020-01-PT-29-001 [Source: `PACKAGE_REGISTER.csv` row 70].

### R-02 — Tagged Equipment Identification (Mandatory)

The Scope of Work shall list the tagged equipment P-9240-1 (Cylinder Lube Oil Transfer Pump) and P-9250-1 (Crankcase Lube Oil Transfer Pump), plus the horizontal split storage tank carrying both cylinder and crankcase oils [Source: `SCOPE_LEDGER.csv` SOW-0137; `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis].

### R-03 — Service Classification (Mandatory)

The Scope of Work shall declare the package as sweet and sour service [Source: `SCOPE_LEDGER.csv` SOW-0137].

### R-04 — Driver Statement (Mandatory)

The Scope of Work shall declare pumps as electric-motor driven and shall record the "no Toshiba motors" driver constraint [Source: `SCOPE_LEDGER.csv` SOW-0137, SOW-0138].

### R-05 — Operating and Design Conditions (Mandatory)

The Scope of Work shall record the source-stated operating and design conditions:
- Operating pressure: low / atmospheric (lube oil transfer pump service)
- Operating temperature: ambient to heated tank temperature
- Design pressure: low / atmospheric
- Design temperature: ambient to heated tank temperature
[Source: `SCOPE_LEDGER.csv` SOW-0138]. Heated-tank set point: `TBD`.

### R-06 — Battery-Limit ("By Others") Statement (Mandatory)

The Scope of Work shall enumerate the explicit by-others items as exclusions from vendor scope: shipping to site, installation on piles, tie-in piping, electrical connections, and mounting platform/stairs [Source: `SCOPE_LEDGER.csv` SOW-0138].

### R-07 — Responsibility Split (Mandatory)

The Scope of Work shall record the Package Vendor / EPC Integrator responsibility split exactly as carried in the workbook row 70 [Source: `PACKAGE_REGISTER.csv` row 70].

### R-08 — Interface Disclosure (Mandatory)

The Scope of Work shall list all eight declared interface types (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports) and reference the Package Datasheet (`DEL-076-02`) as the carrier of the interface requirements matrix [Source: `INTERFACE_REGISTER.csv` rows 557-564; `PACKAGE_REGISTER.csv` row 70; `ARTIFACT_REGISTER.csv` rows 4040+ confirming interface evidence is carried in DEL-076-02].

### R-09 — Bulk Storage Volume Statement (Mandatory)

The Scope of Work shall record bulk lube-oil storage as a 400 bbl heated cylinder-oil tank and a 200 bbl heated crank-case oil tank, located in the storage tank area, with a horizontal split tank arrangement carrying both fluids [Source: `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis; `SCOPE_LEDGER.csv` SOW-0137]. ASSUMPTION: the "400/200 bbl" DBM values and the "horizontal split tank" workbook description describe the same physical storage system; if vendor configuration replaces split-tank with two tanks, the SoW shall be revised.

### R-10 — Scope Item Coverage (Mandatory)

The Scope of Work shall demonstrably cover scope items SOW-0135, SOW-0136, SOW-0137, SOW-0138 [Source: `DELIVERABLE_REGISTER.csv` row 384; `SCOPE_LEDGER.csv` rows 136-139].

### R-11 — Objective Linkage (Informational)

The Scope of Work shall record support for OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 [Source: `DELIVERABLE_REGISTER.csv` row 384; `OBJECTIVE_REGISTER.csv`]. ASSUMPTION: this association is the package-heuristic mapping; deliverable-level objective specificity is not asserted in source.

### R-12 — Source Citation Discipline (Mandatory)

Every non-trivial statement in the SoW shall cite either the workbook row, the package requirements document heading, the DBM section, or another locally accessible source. Inferred items shall be labeled `ASSUMPTION`. Missing data shall be marked `TBD` and not invented.

## Standards

| Standard / Document | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx package heading 30 | Source basis for package scope statements | `_Sources/26020-Package_Requirements.docx` (binary; text-extracted slice TBD) |
| Bid Docs/Budgetary/26020-01-PT-RFQ-29-001-Lube oil supply.docx | Vendor RFQ basis cited in `PACKAGE_REGISTER.csv` row 70 | location TBD — not present in accessible workspace |
| 4-25_Deepcut_DBM.md (Lube Oil Storage and Pump Basis) | Storage volumes, tank design specific gravities, pump tag identifiers | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Project hazardous-material list | Lube-oil storage classification | location TBD — referenced in DBM (Compressor and Liquids Emergency Power, Lube Oil, and Analyzers section: "list was not available in the current workspace") |
| Sour-service codes/standards (NACE MR0175 / ISO 15156 class) | Sweet/sour service equipment classification | TBD — not explicitly stated in accessible source slices |

## Verification

| Requirement | Verification Method | Acceptance Evidence |
|---|---|---|
| R-01 Package identity | Document review | Identity block present, matches PACKAGE_REGISTER.csv row 70 |
| R-02 Tagged equipment | Document review | P-9240-1 and P-9250-1 named; storage tank described |
| R-03 Service classification | Document review | "Sweet and sour service" statement present |
| R-04 Driver statement | Document review | Electric drive and "no Toshiba motors" present |
| R-05 Conditions | Document review | Operating + design conditions present; TBDs flagged |
| R-06 By-others list | Document review | All five by-others items enumerated |
| R-07 Responsibility split | Document review | Vendor vs EPC responsibilities present verbatim or paraphrased without scope change |
| R-08 Interfaces | Document review against `INTERFACE_REGISTER.csv` | All eight interface types listed; DEL-076-02 referenced |
| R-09 Storage volumes | Document review | 400 bbl cylinder + 200 bbl crankcase + split-tank arrangement present |
| R-10 Scope-item coverage | Traceability check | SOW-0135..SOW-0138 covered with section pointers |
| R-11 Objective linkage | Document review | OBJ-001/004/005/006/007/008/009/010 listed; package-heuristic basis disclosed |
| R-12 Source citations | Source audit | Every non-trivial claim carries a source pointer or is marked TBD/ASSUMPTION |

## Documentation

The Scope of Work deliverable artifact set, per `ARTIFACT_REGISTER.csv` rows 4033-4037:

| Artifact ID | Artifact |
|---|---|
| ART-853208E9E8 | Package scope of work |
| ART-558D879D67 | Tagged equipment and package identity list |
| ART-8DAFE7D39E | Package function and whole-facility integration narrative |
| ART-369E16AA74 | Package responsibility assignment record |
| ART-EA90D18DCF | Detailed mechanical package scope extraction evidence |
