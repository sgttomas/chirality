# Specification — DEL-071-02 Package Datasheet (Fuel Gas Skid 4-25)

## Scope

This Specification defines the normative content the EPC Integrator must include in the Package Datasheet for `PKG-071` Fuel Gas Skid 4-25 to enable third-party vendor / discipline package engineering and design (DELIVERABLE_REGISTER.csv row 331; `_CONTEXT.md`).

In scope:
- Package identity, function, and responsibility split (PACKAGE_REGISTER.csv row 61).
- Major equipment basis and design/operating conditions extracted from `26020-Package_Requirements.docx` package heading 25 (SCOPE_LEDGER.csv `SOW-0099`..`SOW-0102`).
- Package-level interface requirements matrix (INTERFACE_REGISTER.csv `PKG-071` rows; ARTIFACT_REGISTER.csv `ART-E22110A1BA` plus per-interface fact artifacts).
- Vendor engineering handoff basis (ART-2C758E3018).

Excluded (carried in sibling deliverables or by others):
- Package scope-of-work narrative — `DEL-071-01_scope-of-work`.
- Construction installation/tie-in workface planning — `DEL-071-03_construction-work-package`.
- Vendor-side engineering, design, fabrication and physical equipment package — `DEL-071-04_vendor-engineered-equipment-package`.
- Vendor document register / submittals / turnover — `DEL-071-05_vendor-document-turnover-package`.
- EPC vendor-package review and acceptance evidence — `DEL-071-06_epc-vendor-package-review-and-acceptance`.
- Shipping to site, installation, tie-in piping, electrical tie-in — by others per `SOW-0102`.

## Requirements

### R-1 Identity and ownership block (FACT)
The datasheet MUST identify the package by `PKG-071`, workbook ID 71, workbook row 61, WBS 01, CoA tracking 26020-01-23-001, package name "Fuel Gas Skid 4-25", discipline Mechanical, and the responsibility split (Package Vendor: package engineering/design/vendor documentation/physical equipment; EPC Integrator: facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination). [PACKAGE_REGISTER.csv row 61]

### R-2 Package function statement (FACT)
The datasheet MUST state that the skid serves the low-pressure fuel gas system for the West Doe Deep Cut Facility and comprises one (1) skid-mounted low-pressure fuel gas package containing one low-pressure fuel gas heater and one low-pressure fuel gas scrubber. [SCOPE_LEDGER.csv `SOW-0100`; 26020-Package_Requirements.docx heading 25 Basic scope]

### R-3 Major equipment list (FACT)
The datasheet MUST list, at minimum: (a) a skid for the system to be mounted on; (b) a fuel gas heater with capacity TBD, controlled by SCR (600 V), including skin-temperature thermocouple override control; (c) a fuel gas scrubber sized using a k factor of 0.35 (imperial) maximum plus operating-pressure de-ration factor (vendor to design). [SCOPE_LEDGER.csv `SOW-0101`]

### R-4 Capacity and process duty (FACT, with TBDs preserved)
The datasheet MUST carry: Design flow required > 8.4 MMSCFD (237.5 e3m3/day); Gas heated to 95 F (35 C); Final flow TBD. [SCOPE_LEDGER.csv `SOW-0102`]

### R-5 Operating conditions (FACT)
The datasheet MUST carry: Operating Pressure 150 psig; Ambient Temperature -19 C to 22.2 C. [SCOPE_LEDGER.csv `SOW-0102`]

### R-6 Design conditions (FACT, with TBD preserved)
The datasheet MUST carry: Design Pressure 150 psig; Design Temperature -40 C to 35 C; MAWP TBD. [SCOPE_LEDGER.csv `SOW-0102`]

### R-7 Driver / electrical power for SCR (FACT)
The datasheet MUST state that SCR heater control panels are 600 V, located in the electrical building. [SCOPE_LEDGER.csv `SOW-0102`]

### R-8 By-others / out-of-vendor-scope list (FACT)
The datasheet MUST preserve the "by others" list: shipping packages to site, installation, tie-in piping, electrical tie-in, etc. [SCOPE_LEDGER.csv `SOW-0102`]

### R-9 Interface requirements matrix (FACT)
The datasheet MUST include a package interface requirements matrix that lists every applicable interface type recorded for `PKG-071` (12 interface types, all `Applicable=YES`): Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. Each row MUST be traceable to its `IFC-*` ID. [INTERFACE_REGISTER.csv rows 453-464; ARTIFACT_REGISTER.csv `ART-E22110A1BA` + ART-26878D11A8..ART-4CC76B3673]

### R-10 Vendor handoff basis (FACT)
The datasheet MUST present the technical basis, battery limits, design expectations, and source-supported requirements as a coherent vendor handoff package (ART-2C758E3018).

### R-11 TBD preservation (FACT)
The datasheet MUST NOT silently resolve TBDs. Heater capacity, final flow, MAWP, and package-specific exclusions remain TBD until the source-of-truth (or a human decision record) provides resolution.

### R-12 Provenance (FACT)
Every non-trivial datasheet value MUST cite its source by file + row (CSV) or by source-document section reference. Values supported only by inference MUST be labeled `ASSUMPTION:`.

## Standards

Source-cited governing references (locations as recorded; clause-level slices not read in this run):
- `26020-Package_Requirements.docx` package heading 25 — package basis (slice carried via SCOPE_LEDGER `SOW-0099`..`SOW-0102`).
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis; sections referenced through OBJECTIVE_REGISTER (`OBJ-005` SEC-12 Electrical; `OBJ-006` SEC-13, SEC-14; `OBJ-007` SEC-08; `OBJ-009` SEC-09, SEC-14, SEC-15; `OBJ-010` SEC-10) — location TBD at clause level.
- Sour-service / pressure-vessel / electrical-area-classification codes and standards — ASSUMPTION: applicable per `OBJ-009`; specific codes (e.g., ASME, CSA Z662, API) — location TBD in available local sources.

## Verification

| Requirement | Verification approach |
|---|---|
| R-1..R-3 (identity, function, equipment) | Datasheet content compared against PACKAGE_REGISTER.csv row 61 and SCOPE_LEDGER.csv `SOW-0099`..`SOW-0101`. |
| R-4..R-7 (conditions, driver) | Datasheet conditions cross-checked against SCOPE_LEDGER.csv `SOW-0102` line-by-line. |
| R-8 (by-others) | Presence of the "by others" list, verbatim from `SOW-0102`. |
| R-9 (interface matrix) | Row-count and `IFC-*` ID match against the 12 INTERFACE_REGISTER rows for `PKG-071`. |
| R-10 (handoff basis) | Reviewer confirms datasheet is self-sufficient for a vendor to scope engineering; gaps recorded as TBD, not assumed. |
| R-11 (TBD preservation) | Explicit grep for "TBD" against the open-item set (heater capacity, final flow, MAWP). |
| R-12 (provenance) | Every numeric value or normative clause traces back to a source citation. |

## Documentation

Artifacts that this deliverable produces or carries as evidence (ARTIFACT_REGISTER.csv `PKG-071` rows scoped to `DEL-071-02_package-datasheet`):
- `ART-CFC06E1B97` — Package technical datasheet (this `Datasheet.md`).
- `ART-2C758E3018` — Vendor engineering handoff basis.
- `ART-E22110A1BA` — Package interface requirements matrix.
- `ART-26878D11A8` .. `ART-4CC76B3673` — Per-interface-type fact records (12 rows; carried into the matrix).

This Specification itself is normative companion content for the four-document kit and is not itself a tagged ARTIFACT row.
