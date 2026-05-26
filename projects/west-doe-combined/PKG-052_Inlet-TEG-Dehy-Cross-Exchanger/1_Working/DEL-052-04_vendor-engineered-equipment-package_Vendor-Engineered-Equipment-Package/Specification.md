# Specification — DEL-052-04 Vendor Engineered Equipment Package (Inlet / TEG Dehy Cross Exchanger)

## Scope

This specification governs the Package Vendor production unit for the Inlet / TEG Dehy Cross Exchanger (tag E-5718-1) at the 4-25 (Deepcut) facility, including vendor engineering, design, fabrication/supply, and the physical equipment package developed from the EPC package Scope of Work (DEL-052-01) and Package Datasheet (DEL-052-02). [Source: `_CONTEXT.md` Scope; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2586.]

**Included:** vendor engineering deliverables, mechanical design, fabrication/supply of the shell-and-tube exchanger and integral package items, vendor design basis and datasheet set.

**Excluded:** EPC-side scope of work, EPC package datasheet, construction work package, vendor document turnover package, and EPC vendor package review/acceptance (held in sibling deliverables DEL-052-01, -02, -03, -05, -06 respectively).

## Requirements

### R-1 — Equipment configuration
The supplied unit shall be a single shell-and-tube heat exchanger (Quantity = 1), BEM type as described in the DBM source. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 601-602.]

### R-2 — Design pressure
Mechanical design pressure shall be not less than 9,756 kPag (1,415 psig) on both shell and tube sides unless the EPC Package Datasheet (DEL-052-02) authorizes side-specific values. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 603.]

### R-3 — Design temperature
Mechanical design temperature shall be not less than 66 deg C. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 604.]

### R-4 — Process service
The exchanger shall heat inlet separator overhead gas and cool a downstream warm process gas stream before that gas flows to the process-gas molecular-sieve inlet filter/coalescers. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 606.]

### R-5 — Warm-side stream identity (CONFLICT)
The warm-side stream identity is UNRESOLVED in the source basis (either dehydrated overhead gas from the TEG contactor or warm sweet gas leaving the amine sweetening unit). The vendor design shall be frozen against the warm-side identity issued in the EPC Package Datasheet (DEL-052-02). Until that ruling is issued, vendor engineering shall not commit material selections that depend on warm-side composition (e.g., H2S/CO2 partial pressure, water saturation). [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 606, 836; CONFLICT — see `Guidance.md`.]

### R-6 — Heat-integration intent
The exchanger shall preserve the heat-integration intent of reducing gas temperature entering the cryogenic plant and helping balance compression load between inlet and sales compressor services. Detailed duty, approach, and pressure drop targets are TBD from the EPC Package Datasheet. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 606; duty figures: location TBD.]

### R-7 — Code of construction
ASSUMPTION: The exchanger shall be designed, fabricated, inspected, and stamped to ASME BPVC Section VIII Division 1 as the governing pressure-vessel code, with TEMA Class R for petroleum/refinery service. Source-explicit code citation: location TBD; vendor shall confirm against EPC Package Datasheet and applicable Alberta jurisdictional requirements.

### R-8 — Materials of construction
TBD — to be selected by the vendor against the warm-side identity ruling (R-5), the sour-service severity called out in EPC Package Datasheet, and applicable NACE MR0175 / ISO 15156 requirements (ASSUMPTION; not explicitly cited in accessible source slice). Location TBD.

### R-9 — Interfaces
The package shall provide flanged process connections compatible with upstream inlet separator overhead piping and downstream warm-side piping, with rating, size, and orientation per the EPC Package Datasheet. TBD — sizes/ratings not in accessible source slice. The exchanger interfaces with gas treating, dehydration, molecular-sieve inlet filtration, cryogenic inlet temperature management, and compressor-load balance. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 836.]

### R-10 — Vendor design basis and datasheet set
The vendor shall produce a package design basis and vendor datasheet set covering thermal/hydraulic design, mechanical design, materials, NDE, testing, surface preparation, and shipping. [Source: `_CONTEXT.md` Anticipated Artifacts.]

## Standards

| Standard | Applicability | Source / status |
|---|---|---|
| ASME BPVC Section VIII Div 1 | Pressure-vessel design and stamping | ASSUMPTION; location TBD |
| TEMA (latest) Class R | Shell-and-tube mechanical standards | ASSUMPTION; location TBD |
| NACE MR0175 / ISO 15156 | Sour-service material qualification | ASSUMPTION; location TBD (depends on R-5 ruling and EPC Package Datasheet sour-gas declaration) |
| Provincial pressure-equipment regulations (Alberta ABSA) | Registration of pressure equipment | ASSUMPTION; location TBD |
| 26020-Package_Requirements.docx (heading 7) | Package requirements document referenced by decomposition row | location TBD — full text not extracted into accessible markdown |

## Verification

| Requirement | Verification |
|---|---|
| R-1, R-7 | Vendor mechanical design package review; ASME U-stamp data report |
| R-2, R-3 | Pressure-test record (hydrostatic) and stamped nameplate witnessed against design pressure/temperature |
| R-4, R-6 | Thermal/hydraulic design report including duty, approach, pressure drop reviewed against EPC Package Datasheet |
| R-5 | Documented warm-side ruling from DEL-052-02 incorporated in vendor datasheet revision history |
| R-8 | Material test reports (MTRs); NACE/ISO compliance certificates where applicable |
| R-9 | Dimensional and nozzle-orientation drawings reviewed against EPC P&ID and isometrics |
| R-10 | Vendor document register completeness check (handled by DEL-052-05) |

## Documentation

The vendor shall produce, at minimum:
- Vendor engineered physical equipment package (the supplied exchanger and integral package items).
- Vendor package design basis.
- Vendor datasheet set (thermal, mechanical, materials).
- Fabrication, NDE, and test records (to be turned over via DEL-052-05).
[Source: `_CONTEXT.md` Anticipated Artifacts.]
