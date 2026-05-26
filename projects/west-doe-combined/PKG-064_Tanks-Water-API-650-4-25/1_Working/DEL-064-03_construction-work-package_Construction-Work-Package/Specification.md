# Specification — DEL-064-03 Construction Work Package

Normative requirements for the EPC Integrator Construction Work Package for PKG-064 "Tanks, Water (API 650) 4-25".

## Scope

### In scope
The Construction Work Package SHALL describe how PKG-064 is physically installed, built, inspected, turned over, and tied into the larger facility systems at the 04-25 facility (`_CONTEXT.md`; DBM-Deepcut SEC-01).

It SHALL cover:

- Receipt, off-loading, setting on foundations, mechanical hookup, instrument/electrical hookup, and tie-in of two (2) Process Water Storage Tanks (TK-5317-1, TK-5318-1) carrying SOW-0233 .. SOW-0236.
- Execution of all interface activities listed in INTERFACE_REGISTER.csv for PKG-064 (process piping; relief/flare/vent; drain/containment; grounding/bonding; area/exterior lighting; cathodic protection; I&C/control cabling; grading/site drainage/spill containment; structural/foundations/supports).
- Construction inspection, testing, and turnover evidence.

### Out of scope (covered by other PKG-064 deliverables or by other parties)
- Package engineering and design of the tanks themselves (Package Vendor — DEL-064-04).
- Vendor document register and submittals (DEL-064-05).
- EPC vendor package review and acceptance evidence (DEL-064-06).
- LACT units; off-site pipelines; acid gas disposal pipeline/well; pre-existing facility items not specifically modified — per DBM-Deepcut SEC-01 Scope Boundary (carried as facility-wide context, applicable to spill containment and discharge routing decisions only).

## Requirements

### R-064-03-01 — Equipment scope coverage
The Construction Work Package SHALL list every equipment tag carried by PKG-064 (TK-5317-1 and TK-5318-1) and assign a work-face activity set per tag. Source: DBM-Deepcut equipment/tag table row 102; SOW-0235.

### R-064-03-02 — Code / design basis traceability
The Construction Work Package SHALL identify each tank as a Modified API 650 atmospheric tank with design pressure 32 oz / 1.0 oz vacuum and SHALL require installation conditions consistent with that design basis. Source: SOW-0235.

### R-064-03-03 — Insulation and heating
Construction work-face plans SHALL include installation of external insulation and the freeze-protection heating system required for arctic/sub-arctic service (site temperature range -40 °C to 60 °C). Source: SOW-0235, SOW-0236.

### R-064-03-04 — Blanket gas connection
Construction work-face plans SHALL include the LP fuel-gas blanket connection at each tank. Source: SOW-0235.

### R-064-03-05 — EPC-managed interface execution
The Construction Work Package SHALL include an EPC-managed interface execution plan covering every interface row in INTERFACE_REGISTER.csv for PKG-064 (nine interface types, all flagged `RequiresEPCManagement = YES`). For each interface the package SHALL identify the boundary point, the responsible craft/discipline, the tie-in window, and the verification evidence.

### R-064-03-06 — Construction responsibility assignment
Per-activity construction responsibility SHALL follow the DBM-Deepcut SEC-01 "Construction Responsibility" table (Tourmaline Oil Corporation field construction scope for management, grading/piling/foundations, plant roads, off-loading, setting equipment, mechanical hookup, shipped-loose item installation, structural supports, home-run cable installation, electrical terminations, and area lighting). Tie-in interconnecting-piping responsibility SHALL be confirmed per tie-in. Source: DBM-Deepcut SEC-01.

### R-064-03-07 — "By others" scope explicitly carried
The Construction Work Package SHALL execute the items called "by others" in SOW-0236 for this package, specifically: foundations, mounting tanks at site, electrical/instrumentation, platforms, and staircases. Source: SOW-0236.

### R-064-03-08 — Spacing compliance at construction set-out
Tank placement SHALL be set out in accordance with the governing spacing criteria in DBM-Deepcut SEC-02 "Atmospheric Tank and General Plant Spacing", including (a) ≥ 2.35 m between atmospheric tanks (NFPA 30, Table 22.4.2.1), (b) ≥ 25 m between flare/separators and atmospheric produced-water tanks (OGAOM Sec. 9.6.15) where applicable to adjacent atmospheric water tankage, (c) ≥ 30.48 m between pressurized bullets and nearest atmospheric tank (API 2510). Final coordinates SHALL be reconciled to the project plot plan (status TBD per DBM-Deepcut SEC-02). Source: DBM-Deepcut SEC-02 spacing tables.

### R-064-03-09 — Turnover evidence
A construction interface and turnover checklist SHALL be produced as a Construction Work Package artifact (per `_CONTEXT.md` Anticipated Artifacts).

### R-064-03-10 — Workface plan
An installation and tie-in workface plan SHALL be produced as a Construction Work Package artifact (per `_CONTEXT.md` Anticipated Artifacts).

### R-064-03-11 — Permit and regulatory context
Construction execution SHALL respect the British Columbia Energy Regulator permit amendment and Section 12.4 site alteration permit context noted in DBM-Deepcut SEC-01 Permitting. Specific permit-clearance steps are TBD pending the regulatory section of the DBM (location TBD).

### R-064-03-12 — Acceptance handoff
The Construction Work Package SHALL produce evidence sufficient to support the downstream EPC Vendor Package Review and Acceptance deliverable (DEL-064-06). ASSUMPTION: downstream consumer is DEL-064-06 based on the PKG-064 deliverable register entry for DEL-064-06; not declared in `_DEPENDENCIES.md`.

## Standards

| Standard / Document | Applicability | Location |
|---|---|---|
| API 650 (modified) | Tank design basis — applies to construction acceptance of as-built dimensional and welded condition | Cited in SOW-0235; clause locations TBD |
| API 2000 | Tank venting (blanket-gas / PVRV basis used in DBM Produced Water tank table) — apply by analogy to atmospheric water tankage where vacuum/breathing protection is required; ASSUMPTION | DBM-Deepcut Produced Water Tank table |
| API 2510 | Spacing for pressurized bullets and nearest atmospheric tank | DBM-Deepcut SEC-02 |
| NFPA 30 | Atmospheric tank spacing | DBM-Deepcut SEC-02 (Tables 22.4.1.5, 22.4.2.1, 17.4.5 / 17.4.3) |
| OGAOM Sec. 9.6.15 | Flare-to-atmospheric-tank, road, and vegetation spacing | DBM-Deepcut SEC-02 |
| National Building Code of Canada 2020 (Dawson Creek IDF basis) | Climate-data basis for construction loadings | DBM-Deepcut SEC-02 §2.2 |
| British Columbia Energy Regulator permit + Section 12.4 site alteration permit | Permitting basis for facility construction | DBM-Deepcut SEC-01 Permitting |
| Project plot plan | Final equipment coordinates and layout verification | Status TBD per DBM-Deepcut SEC-02 |

Where the standard is cited at facility level but the clause-specific construction obligation is not present in accessible sources, the obligation is marked `location TBD` and SHALL be confirmed during detailed construction planning.

## Verification

| Requirement | Verification approach |
|---|---|
| R-064-03-01 | Equipment-tag-to-workface cross-check against DBM equipment/tag table (row 102) and PACKAGE_REGISTER (PKG-064). |
| R-064-03-02 | Field receipt inspection of vendor tank nameplate vs. SOW-0235 values (modified API 650; 32 oz design; 1.0 oz vacuum). |
| R-064-03-03 | Visual and continuity inspection of insulation and heat-trace circuits prior to commissioning; freeze-protection functional test. |
| R-064-03-04 | Pressure and leak check of LP fuel-gas blanket connection; PVRV setting confirmation (PVRV provision basis from DBM Produced Water tank narrative, applied by analogy; ASSUMPTION). |
| R-064-03-05 | Per-interface sign-off in the construction interface and turnover checklist for all nine PKG-064 interfaces. |
| R-064-03-06 | Construction responsibility-assignment register cross-checked against DBM-Deepcut SEC-01 Construction Responsibility table. |
| R-064-03-07 | Field walk-down confirming foundations, mounting, electrical/instrumentation, platforms, and staircases are installed. |
| R-064-03-08 | Set-out survey vs. plot plan and DBM SEC-02 spacing criteria; deviation log to engineering. |
| R-064-03-09 | Completion of construction interface and turnover checklist; package handover signature. |
| R-064-03-10 | Approval of installation and tie-in workface plan prior to mobilization. |
| R-064-03-11 | Document-control register references to applicable permit clearances (specific clearances TBD). |
| R-064-03-12 | Turnover dossier accepted by the EPC Integrator review process (DEL-064-06). |

## Documentation

Required Construction Work Package artifacts (from `_CONTEXT.md` "Anticipated Artifacts"):

- Construction work package (the bound document set itself)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
