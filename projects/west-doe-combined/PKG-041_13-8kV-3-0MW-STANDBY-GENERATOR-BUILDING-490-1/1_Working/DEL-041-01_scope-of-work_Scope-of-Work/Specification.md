# Specification — DEL-041-01 Scope of Work (PKG-041, 490-1 Standby Generator Building)

## Scope

This Specification defines the EPC Integrator Scope of Work for PKG-041, the standby generator package referenced in the workbook as "13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1)" and identified in the design basis as Module 490-1 Emergency Generator Module. (Source: PACKAGE_REGISTER.csv row 43; DBM Module Assembly table.)

The current design basis for standby power has been revised. Per DBM "Standby Power", the centralized 13.8 kV emergency-generator concept has been replaced by TOU-typical low-voltage (480 V or 600 V class) standby generators connected at the LV MCC level with transfer switches serving 04-25 and 03-25 critical loads. The workbook package title (13.8 kV / 3.0 MW) is retained as the package identifier but does not, on the evidence in DBM-Deepcut, describe the current technical basis. The discrepancy is captured in `Guidance.md`, Conflict Table (CT-001) for human ruling.

In scope (EPC Integrator):
- Package scope of work documentation defining vendor-versus-EPC ownership split, package function, tagged equipment, and integration narrative. (PACKAGE_REGISTER.csv row 43)
- Facility-level integration of the vendor standby generator module 490-1 into 04-25 and 03-25 critical-load distribution.
- Interfaces enumerated in PACKAGE_REGISTER.csv row 43 (utility piping; drain/containment; electrical power; grounding/bonding; area/exterior lighting; I&C/control cabling; communications/network; building HVAC/services; fire & gas/safety systems; maintenance access; grading/site drainage/spill containment; structural/foundations/supports).
- Responsibility assignment record for vendor scope, EPC scope, and shared/coordination items.

Out of scope:
- Package engineering, package design, vendor documentation, and supply of the physical equipment package (owned by Package Vendor per PACKAGE_REGISTER.csv row 43).
- TBD: no package-specific exclusions stated in source materials (PACKAGE_REGISTER.csv row 43, Exclusions column).

## Requirements

| ReqID | Requirement | Source / Basis |
|---|---|---|
| R-041-01-01 | The Scope of Work shall name the package using its workbook identity ("13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1)") AND cross-reference its design-basis identity (Module 490-1 Emergency Generator Module). | PACKAGE_REGISTER.csv row 43; DBM Module Assembly table |
| R-041-01-02 | The Scope of Work shall list all tagged equipment associated with the package: AC-4910-1, EGD-4950-1, EG-4950-1, ACM-4910-1. | DBM Tagged Equipment table row 69 |
| R-041-01-03 | The Scope of Work shall describe the current standby-power basis: TOU-typical LV standby generator on LV MCC with transfer switch (480 V or 600 V class), serving 04-25 and 03-25 critical loads. | DBM "Emergency Power Generation Basis"; "Standby Power" |
| R-041-01-04 | The Scope of Work shall declare that the prior 13.8 kV centralized tie-in has been eliminated for this facility scope. | DBM "Emergency Power Generation Basis" table |
| R-041-01-05 | The Scope of Work shall identify open items: generator make/model/rating; LV switchgear and transfer switch configuration; fuel selection (NG or diesel); battery/charger sizing; diesel storage sizing if selected; sizing, count, transfer mode, paralleling, and load-shedding requirements. | DBM "Emergency Power Generation Basis"; Item table "Standby generator integration" |
| R-041-01-06 | The Scope of Work shall enumerate the EPC Integrator interface set: utility piping; drain/containment; electrical power; grounding/bonding; area/exterior lighting; I&C/control cabling; communications/network; building HVAC/services; fire & gas/safety systems; maintenance access; grading/site drainage/spill containment; structural/foundations/supports. | PACKAGE_REGISTER.csv row 43 |
| R-041-01-07 | The Scope of Work shall record the ownership split: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination. | PACKAGE_REGISTER.csv row 43 |
| R-041-01-08 | The Scope of Work shall describe the loads supported: heat medium, UPS, control systems, servers, freeze-protection electric heat tracing (during outage or turnaround). | DBM "Standby Power" |
| R-041-01-09 | The Scope of Work shall record the area classification (General Purpose) and the outdoor weather-protective vendor enclosure configuration with 1 m access walkway. | DBM "Emergency Power Generation Basis" table; section |
| R-041-01-10 | If natural gas is the selected fuel, the Scope of Work shall require fuel gas regulated to less than 66 psig before entering the generator enclosure. | DBM "Emergency Power Generation Basis" table |
| R-041-01-11 | The Scope of Work shall flag CT-001 (workbook 13.8 kV / 3.0 MW vs DBM LV basis) for human ruling. ASSUMPTION: DBM is more recent than the workbook title; this is not yet confirmed. | This document, Conflict Table |
| R-041-01-12 | Objective traceability: the Scope of Work shall reference the package's supported objectives (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010). ASSUMPTION (best-effort mapping via PACKAGE_HEURISTIC). | _CONTEXT.md; PACKAGE_REGISTER.csv row 43 |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| CEC (Canadian Electrical Code) | Transformer spacing and installation referenced in DBM electrical sections; applies to package integration where transformers or LV equipment are installed adjacent to the standby generator module. | DBM "Transformers" section; location TBD for clause-level requirements (not present in accessible slice) |
| TOU electrical / mechanical standards | DBM refers to "TOU-typical" generator package and "TOU standard confirmation" pending. Governing TOU standard set is not in the accessible reference set. | location TBD |
| TBD | Project electrical study basis, transfer switch / paralleling standards | location TBD |

## Verification

| ReqID | Verification approach |
|---|---|
| R-041-01-01..04 | Document review against PACKAGE_REGISTER.csv row 43 and DBM-Deepcut sections cited. |
| R-041-01-05 | Open-items list cross-checked against the DBM "Standby generator integration" row; gaps surfaced as TBD with named owner (MLE, EPC, electrical studies). |
| R-041-01-06..07 | Interface and responsibility tables in the Scope of Work compared element-by-element against the package register row 43 interface list and ownership split text. |
| R-041-01-08..10 | Cross-reference Scope of Work narrative to DBM "Standby Power" and "Emergency Power Generation Basis" tables. |
| R-041-01-11 | Conflict Table CT-001 visible in `Guidance.md`; ruling captured in `_MEMORY.md` when issued. |
| R-041-01-12 | Objective list cross-checked against OBJECTIVE_DELIVERABLE_MAP.csv (or PACKAGE_REGISTER.csv supported-objectives column) — ASSUMPTION flag retained until objective-deliverable mapping confirms at the deliverable-ID level. |

## Documentation

Anticipated artifacts (per `_CONTEXT.md` and DELIVERABLE_REGISTER.csv row 228):
- Package scope of work
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record
- Conflict Table entries for CT-001 (in `Guidance.md`) pending human ruling
