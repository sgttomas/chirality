# Specification — DEL-084-01 Scope of Work (PKG-084 Fuel Gas Skid 3-25)

Normative requirements for the EPC Integrator Scope of Work for the LP Fuel Gas Skid (`26020-02-PT-23-001`) at the 3-25 West Doe Compressor Station. Pass directive: P1_P2.

## Scope

### In Scope

- EPC Integrator definition of the full package scope for `PKG-084 Fuel Gas Skid 3-25`, including:
  - tagged equipment identity and package equipment list (Source: 26020-Package_Requirements.docx heading 37, Major Included Equipment),
  - package function and integration narrative into the 3-25 facility (Source: 26020-Package_Requirements.docx Basic Scope; `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas"),
  - source basis and boundaries (Source: 26020-Package_Requirements.docx Source Basis, Scope Notes / Open Items),
  - responsibility assignment record for EPC Integrator vs. Package Vendor vs. By Others (Source: 26020-Package_Requirements.docx Scope Notes / Open Items "By others"),
  - whole-facility integration narrative covering shared fuel-gas/instrument-air/electrical-power cross-facility utilities with 04-25 (Source: `3-25_Comp_and_Liquids_DBM.md` §Utilities, §"## Fuel Gas").
- Coverage of decomposition scope items SOW-0095, SOW-0096, SOW-0097, SOW-0098 (Source: OBJECTIVE_SCOPE_MAP.csv rows for PKG-084).

### Out of Scope (Excluded — "By others" per source)

- Shipping packages to site (Source: 26020-Package_Requirements.docx Scope Notes / Open Items).
- Installation of the package at site (Source: same).
- Tie-in piping at the skid boundary (Source: same).
- Electrical tie-in (the SCR control panels themselves are vendor-supplied at 600 V and located in the electrical building; field tie-in is by others) (Source: 26020-Package_Requirements.docx Scope Notes / Open Items + Major Included Equipment).
- Vendor engineering, fabrication, and document turnover content carried in sibling deliverables `DEL-084-04` and `DEL-084-05` (Source: DELIVERABLE_REGISTER.csv rows 327–328).
- Construction work package content carried in sibling deliverable `DEL-084-03` (Source: DELIVERABLE_REGISTER.csv row 326).

## Requirements

### R-SOW-084-1 — Equipment List

The Scope of Work shall list the tagged equipment for the package as exactly one skid-mounted LP Fuel Gas Package identified as `26020-02-PT-23-001 - Fuel Gas Skid`, comprising one LP fuel gas heater and one LP fuel gas scrubber, plus the mounting skid. (Source: 26020-Package_Requirements.docx heading 37, Basic Scope, Major Included Equipment.)

### R-SOW-084-2 — Process Function Statement

The Scope of Work shall state that the package serves the low-pressure fuel gas system for the West Doe Deep Cut Facility. (Source: 26020-Package_Requirements.docx Basic Scope.)

### R-SOW-084-3 — Capacity and Design Basis

The Scope of Work shall record the following package design basis as binding on vendor design:

- Design flow required: > 1.5 MMSCFD (42.5 e3m3/day) (Source: 26020-Package_Requirements.docx Scope Notes / Open Items).
- Heated outlet condition: gas heated to 95 °F (35 °C); final flow TBD (Source: same).
- Operating pressure: 150 psig (Source: same).
- Design pressure: 150 psig (Source: same).
- Design temperature: −40 °C to 35 °C (Source: same).
- Ambient temperature: −19 °C to 22.2 °C (Source: same).
- Heating value: 1040 BTU/SCF (Source: same).
- MAWP: TBD — to be set by vendor design within the design pressure/temperature envelope above (Source: same).

### R-SOW-084-4 — Heater Control

The fuel gas heater shall be controlled by an SCR control panel at 600 V located in the electrical building, and shall include a skin-temperature thermocouple override on the heater. (Source: 26020-Package_Requirements.docx Major Included Equipment, Scope Notes / Open Items.)

### R-SOW-084-5 — Scrubber Sizing

The LP fuel gas scrubber shall be sized using a K factor of 0.35 (imperial) maximum plus a de-ration factor for operating pressure; final sizing is by vendor design. (Source: 26020-Package_Requirements.docx Major Included Equipment.)

### R-SOW-084-6 — Boundary and Responsibility

The Scope of Work shall document that shipping, installation, tie-in piping, and electrical tie-in are by others (not included in the package). (Source: 26020-Package_Requirements.docx Scope Notes / Open Items "By others".)

### R-SOW-084-7 — Facility Integration Narrative

The Scope of Work shall include a whole-facility integration narrative that describes:

- the package's role as a 3-25 facility LP fuel-gas equipment item supplying the 3-25 Compressor Station and Liquids Hub (Source: `3-25_Comp_and_Liquids_DBM.md` §Utilities, §"## Fuel Gas");
- that fuel gas, instrument air, and electrical power are shared cross-facility utilities with the 04-25 Deep Cut Gas Plant, and that LP fuel-gas users include TEG stripping, caustic treating overhead dilution, maintenance purge, drive gas, and blanket gas (Source: same);
- the relationship between this skid and the facility-side LP fuel-gas scrubber `V-3210-2` and slop tank `TK-9130-2` (Source: same — relationship and tie-in details: `location TBD`; final integration to be confirmed by detail design);
- the unresolved emergency-buyback fuel-gas question (W242510 vs. Process_DBM_fixed) as an open item requiring human authority ruling before final issue (Source: same).

### R-SOW-084-8 — Physical Interface Applicability

The Scope of Work shall include the package physical interface applicability table from the source (interface source: `26020-Packages_Interfaces.3.xlsx`, row 60 — local export available as `26020-Packages_Interfaces_4_export.xlsx`; field-level export `location TBD`). Per-interface applicability shall match the source table reproduced in `Datasheet.md` §"Physical Interface Summary". (Source: 26020-Package_Requirements.docx Physical Interface Summary.)

### R-SOW-084-9 — Vendor Document Set Identification

The Scope of Work shall identify, by reference, the vendor engineering deliverables required of the Package Vendor as enumerated under "Vendor Engineering Deliverables" in source heading 37 (PRQ-009, DOC-008, QLT-006, QLT-003, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015, PRQ-016; MEC-001..MEC-025; PRO-004..PRO-028; PRO-014..PRO-015; etc., with the full list governed by the source). Full enumeration is the subject of `DEL-084-05_vendor-document-turnover-package`. (Source: 26020-Package_Requirements.docx Vendor Engineering Deliverables; DELIVERABLE_REGISTER.csv row 328.)

### R-SOW-084-10 — Coverage of Decomposition Scope Items

The Scope of Work shall close out SOW-0095 (package identity / workbook row 60), SOW-0096 (basic scope), SOW-0097 (major included equipment), and SOW-0098 (scope notes and open items) for PKG-084. (Source: OBJECTIVE_SCOPE_MAP.csv, PKG-084 rows.)

### R-SOW-084-11 — Open-Items Register

The Scope of Work shall carry an Open Items register that records, at minimum: heater capacity (TBD), final flow (TBD), MAWP (TBD), and the emergency-buyback fuel-gas question (CONFLICT — needs human ruling). (Source: 26020-Package_Requirements.docx Scope Notes / Open Items; `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas".)

## Standards

| Standard / Code | Applicability to this SOW | Source / Location |
|---|---|---|
| Pressure equipment registration (jurisdictional pressure-vessel registration) | Applies to package pressure equipment (scrubber); identified in source's Vendor Engineering Deliverables as `REG-022 Pressure Equipment Registration Package` | 26020-Package_Requirements.docx, Vendor Engineering Deliverables — `location TBD` for the governing code clause |
| Process safety / HAZOP / PSI | Required vendor deliverables `PRO-026 HAZOP / PHA Technical Input Package`, `PRO-027 Process Safety Information (PSI) Package` | 26020-Package_Requirements.docx, Vendor Engineering Deliverables — `location TBD` for governing standard |
| Relief / flare design | Required vendor deliverables `PRO-014 Relief and Flare Design Basis`, `PRO-015 PSV / Pressure Relief Sizing Calculations` | 26020-Package_Requirements.docx, Vendor Engineering Deliverables — `location TBD` for governing standard |
| ASSUMPTION: Canadian Electrical Code applies to 600 V SCR control panel and electrical building tie-in | likely applicable given Canadian project context | not stated in accessible sources — `location TBD` |

Other code/standard call-outs from the locally available source text were not found; clause-level requirements shall not be invented (per skill non-negotiables).

## Verification

| Requirement | Verification Approach | Source / Notes |
|---|---|---|
| R-SOW-084-1 (Equipment List) | Document review of the issued SOW against source heading 37 Basic Scope and Major Included Equipment | 26020-Package_Requirements.docx |
| R-SOW-084-2 (Process Function) | Document review against source Basic Scope | 26020-Package_Requirements.docx |
| R-SOW-084-3 (Design Basis) | Document review against source Scope Notes / Open Items values; vendor data sheets `MEC-003`, `PRO-010` to carry these values | 26020-Package_Requirements.docx |
| R-SOW-084-4 (Heater Control) | Vendor FAT and document review of `MEC-006` Package Equipment Specification and heater control documentation | 26020-Package_Requirements.docx, Vendor Engineering Deliverables |
| R-SOW-084-5 (Scrubber Sizing) | Vendor `MEC-014` Mechanical Calculation Package review against K = 0.35 + pressure de-ration | 26020-Package_Requirements.docx |
| R-SOW-084-6 (Boundary / By others) | Cross-check SOW responsibility matrix against source "By others" list | 26020-Package_Requirements.docx |
| R-SOW-084-7 (Facility Integration) | Review of SOW narrative against `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas" and §Utilities; record outstanding items in Open Items register | DBM source |
| R-SOW-084-8 (Interface Table) | Reconcile SOW interface table against `26020-Packages_Interfaces.3.xlsx` row 60 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` |
| R-SOW-084-9 (Vendor Document Set) | Cross-reference SOW vendor-document list to source Vendor Engineering Deliverables, with full enumeration handled in DEL-084-05 | 26020-Package_Requirements.docx |
| R-SOW-084-10 (Decomp Coverage) | Trace SOW sections to SOW-0095/96/97/98 via the issued SOW's traceability matrix | OBJECTIVE_SCOPE_MAP.csv |
| R-SOW-084-11 (Open Items) | Issued SOW contains an Open Items register with at least the listed entries; human ruling captured for emergency buyback | 26020-Package_Requirements.docx; DBM §Fuel Gas |

## Documentation (Anticipated Artifacts)

Per `_CONTEXT.md` Anticipated Artifacts and source Vendor Engineering Deliverables, the issued SOW shall produce/cite at minimum:

- Package scope of work narrative.
- Tagged equipment and package identity list (mirrors `Datasheet.md` Attributes).
- Package function and integration narrative.
- Responsibility assignment record (EPC Integrator / Package Vendor / By Others).
- Open Items register (per R-SOW-084-11).
- Reference to the Package Datasheet (`DEL-084-02`), Construction Work Package (`DEL-084-03`), and Vendor Document Turnover Package (`DEL-084-05`) as downstream/sibling deliverables. (Source: DELIVERABLE_REGISTER.csv rows 325–328.)
