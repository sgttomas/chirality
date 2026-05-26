# Specification — DEL-088-03 Construction Work Package

> Normative requirements for the EPC Construction Work Package for PKG-088 Caustic Treating (Condensate Mercaptan Removal). Requirements are grounded in the project DBM and the deliverable register; clause-level requirements from `26020-Package_Requirements.docx` heading 41 are recorded as `location TBD` until that source slice is extracted.

## Scope

### Inclusions
- The Construction Work Package shall describe how PKG-088 will be physically installed, built, inspected, turned over, and tied into the larger 03-25 facility systems. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-088-03_construction-work-package`.)
- The package shall address all interface types declared for PKG-088: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. (Source: `PACKAGE_REGISTER.csv` row PKG-088 "Interface Types".)
- The package shall cover construction execution activities within the EPC Integrator scope: construction management; grading; piling; foundations; field buildings; offloading and setting of the caustic treating package and ancillaries; mechanical hookups; installation of shipped-loose instruments and valves; pipe supports; ISBL/OSBL interconnecting piping; home-run cabling and terminations; area lighting; fencing; fire & gas/security systems; control room and maintenance interfaces; drain/vent tie-ins. (Source: `3-25_Comp_and_Liquids_DBM.md` "Construction Scope Summary"; line 619 coordination.)

### Exclusions
- Package engineering, package design, vendor documentation, and the physical equipment package itself are the Package Vendor's scope (DEL-088-04, DEL-088-05); this Construction Work Package shall not redefine them. (Source: `PACKAGE_REGISTER.csv` row PKG-088 "Boundaries".)
- Third-party LACT package equipment, upstream/product pipelines outside facility tie-ins, and sales condensate LACT equipment are excluded except for facility-side power/tie-in interfaces. (Source: `3-25_Comp_and_Liquids_DBM.md` Scope Exclusions; lines 54, 69, 70.)

## Requirements

### R1 — Construction-Execution Coverage
The package shall produce a construction work package, an installation and tie-in workface plan, and a construction interface and turnover checklist. (Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` Anticipated Artifacts column.)

### R2 — Interface Tie-In Discipline
For each interface type listed in PKG-088, the package shall identify field tie-in locations, mechanical/electrical/I&C scope handoff points, and the responsible discipline for execution. (Source: `PACKAGE_REGISTER.csv` row PKG-088; `3-25_Comp_and_Liquids_DBM.md` "Mechanical Packages" line 617 — "field tie-in lists" required as a package deliverable input.)

### R3 — Caustic Building Material Restriction
Aluminum shall not be used in the caustic building. The construction work package shall flag this restriction in material handling, supports, ladders, platforms, and shipped-loose items installed in or interfacing with the caustic building. (Source: `3-25_Comp_and_Liquids_DBM.md` "Condensate Mercaptan Treating".)

### R4 — Caustic Drain System
Minimum drain-header rating shall be 300# ANSI for caustic drain service. Caustic drain maximum design temperature is 121 deg C / 250 deg F (TBC); minimum drain-tank temperature is 80 deg F. Heat tracing at 37.8 deg C / 100 deg F with redundant circuits is under consideration. Caustic drain material selection requires detailed review due to embrittlement concerns. (Source: `3-25_Comp_and_Liquids_DBM.md` "Drains".)

### R5 — Caustic Tank Construction Provisions
Fresh and spent caustic tanks are atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation; the construction work package shall include the installation, blanket-gas connection, heat tracing, insulation, and venting (spent tank to incinerator header via flame arrestor) tasks for these tanks. Fresh caustic shall not be connected to the VRU. (Source: `3-25_Comp_and_Liquids_DBM.md`.)

### R6 — Utility Tie-Ins
Instrument air is supplied from 04-25 (no local 03-25 IA compressor under SCA-006); the construction work package shall plan IA distribution and tie-ins consistent with that cross-facility supply (including the 214 SCFM TBC caustic oxidation demand). LP fuel-gas distribution shall serve caustic treating overhead dilution per the DBM. (Source: `3-25_Comp_and_Liquids_DBM.md` "Instrument Air"; "Utilities"; line 463.)

### R7 — Modularization and Field Installation
Where the vendor equipment package is delivered as modular units, the construction work package shall include offloading, setting, and field installation sequencing. The split between shop assembly and field installation shall be confirmed against the selected Package Vendor scope. (Source: `3-25_Comp_and_Liquids_DBM.md` lines 294, 661; ASSUMPTION: package-level modularization for PKG-088 specifically is TBD until vendor selection.)

### R8 — Turnover and Construction Register Alignment
The final construction work package register entry and supporting documents shall be aligned with the project plot plan, equipment list, and construction work package register before issue for construction. (Source: `3-25_Comp_and_Liquids_DBM.md` line 661.)

### R9 — Hazard Recognition for Construction Operations
Methyl mercaptan toxicity and odour hazards shall be recognized for purge, analyzer maintenance, and construction-phase commissioning operations involving caustic treating streams; a formal hazard review is required before finalizing purge and analyzer maintenance practices. (Source: `3-25_Comp_and_Liquids_DBM.md` "Fuel-Gas Sulphur and Purge Hazard Basis".)

### R10 — Geotechnical Confirmation Hook
Foundation selection, pile design, settlement criteria, frost protection, site preparation, and structural support requirements for the caustic treating package shall be confirmed against the final geotechnical report. (Source: `3-25_Comp_and_Liquids_DBM.md` line 141.)

### R11 — Source-Document Clause Reconciliation (TBD)
Construction-execution clauses identified in `26020-Package_Requirements.docx` package heading 41 shall be reconciled into this specification before issue for construction. `location TBD` — source slice not extracted in this run.

## Standards

| Standard / Basis | Application | Status |
|---|---|---|
| ANSI 300# flange/header rating | Caustic drain header | Source-grounded (`3-25_Comp_and_Liquids_DBM.md` "Drains") |
| Project DBM (Comp_and_Liquids 3-25) | Process, utility, civil, and construction scope basis | Source-grounded |
| `26020-Package_Requirements.docx` heading 41 | Package-specific EPC requirements | Cited; `location TBD` |
| HAZOP / hazard review | Pressure segregation and purge/analyzer practices | Required (per DBM); deliverable specifies hook |
| Local construction codes, electrical code, and area classification standards | Site execution | ASSUMPTION (typical EPC); specific code revisions `TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Document completeness check against `_CONTEXT.md` Anticipated Artifacts list |
| R2 | Interface-by-interface traceability table mapping each PKG-088 interface type to a tie-in scope entry |
| R3 | Material take-off review for items entering caustic building; checklist line item |
| R4 | Drain isolation/material spec review; HAZOP confirmation of pressure segregation |
| R5 | Tank installation work pack inspection record; blanket-gas leak check; insulation/heat-trace commissioning record |
| R6 | Utility tie-in punch list; IA distribution loop check; LP fuel-gas leak check |
| R7 | Module offloading and setting inspection records; field-installation hookup completion record |
| R8 | Construction work package register cross-check against plot plan and equipment list before IFC |
| R9 | Hazard review meeting minutes; purge/analyzer maintenance procedure approval |
| R10 | Geotechnical report reference recorded against foundation/pile design release |
| R11 | Source-clause reconciliation log closing out `location TBD` items |

## Documentation

The deliverable shall produce, at minimum:

- Construction work package document set (per R1).
- Installation and tie-in workface plan (per R1, R2).
- Construction interface and turnover checklist (per R1, R8).
- Field tie-in list (per R2; aligned with the package deliverable inputs cited in `3-25_Comp_and_Liquids_DBM.md` line 617).
- Material/coating handling notes for caustic-building exclusions (per R3).
- Hazard review record for purge and analyzer operations (per R9).
