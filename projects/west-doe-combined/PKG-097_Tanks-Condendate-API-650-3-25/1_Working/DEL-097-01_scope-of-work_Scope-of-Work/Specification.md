# Specification — DEL-097-01 Scope of Work

Normative scope-of-work specification for `PKG-097` "Tanks, Condendate (API 650) 3-25", authored by the EPC Integrator for issue to the Package Vendor and for downstream facility integration use.

## Scope

### In scope (this deliverable)

This Scope-of-Work deliverable shall define, in normative terms, the EPC-issued package scope for `PKG-097`. It shall include:

- The tagged equipment and package identity for the four (4) 3,800 bbl Condensate Product Storage Tanks. (Source: `PACKAGE_REGISTER.csv` row 88; `SCOPE_LEDGER.csv` `SOW-0202`, `SOW-0203`.)
- The process function statement: C5+ Condensate Product Storage in the 03-25 Liquids Hub. (Source: `PACKAGE_REGISTER.csv` row 88; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling.)
- The package operating and design conditions, capacity, governing codes, and required per-tank fittings. (Source: `SCOPE_LEDGER.csv` `SOW-0203`, `SOW-0204`.)
- The package-level interface inventory and EPC/Vendor responsibility split. (Source: `INTERFACE_REGISTER.csv` `PKG-097` rows; `PACKAGE_REGISTER.csv` row 88 Responsibility model.)
- Whole-facility integration narrative situating this package within the 03-25 Liquids Hub. (Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Facility Overview and Condensate Storage and Product Handling.)
- Carry-through of declared `SOW-0201` through `SOW-0204` scope-ledger items and supports-objective set.

### Out of scope (excluded from the package — "By Others")

- Foundations and at-site mounting of the tanks. (`SCOPE_LEDGER.csv` `SOW-0204`.)
- Electrical and instrumentation supply, including site cabling. (`SCOPE_LEDGER.csv` `SOW-0204`.)
- Platforms, staircases, and other tank-external access steel. (`SCOPE_LEDGER.csv` `SOW-0204`.)
- LACT and offsite pipeline scope and design; the 03-25 facility responsibility ends at the defined tie-in flange. (Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Facility Overview / Liquids Hub.)
- Vendor-internal engineering and equipment supply (assigned to the Package Vendor — see Responsibility, not excluded from `PKG-097` but excluded from EPC Integrator authoring scope).

## Requirements

REQ-097-01-01 — Package identity. The Scope of Work shall state that `PKG-097` carries the workbook-defined vendor-responsible Mechanical package "Tanks, Condendate (API 650) 3-25" under WBS 03, with workbook tracking number 26020-03-19-006. (Source: `SCOPE_LEDGER.csv` `SOW-0201`; `PACKAGE_REGISTER.csv` row 88.)

REQ-097-01-02 — Basic equipment count and size. The Scope of Work shall require supply of four (4) 3,800 bbl Condensate Product Storage Tanks. (Source: `SCOPE_LEDGER.csv` `SOW-0202`, `SOW-0203`; `26020-Package_Requirements.docx` heading 49 Basic scope.)

REQ-097-01-03 — Governing tank standard. Tanks shall be designed and fabricated to **modified API 650**. (Source: `SCOPE_LEDGER.csv` `SOW-0203`.)

REQ-097-01-04 — Blanket-gas system standard. The blanket-gas system shall conform to **API 2000**. (Source: `SCOPE_LEDGER.csv` `SOW-0203`.)

REQ-097-01-05 — Atmospheric, non-insulated configuration. Tanks shall be non-insulated atmospheric tanks. A recycle to maintain temperature during winter may be required. (Source: `SCOPE_LEDGER.csv` `SOW-0203`.) — Cross-check: the same DBM elsewhere classifies the produced-water tanks as "API-650 Modified atmospheric tanks, externally insulated and heated" (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`); that classification applies to produced-water service and is *not* extended to condensate product tanks by the package source. The PKG-097 non-insulated requirement governs. See Conflict Table CT-097-01-A in `Guidance.md`.

REQ-097-01-06 — Internal coating. Internal floors, walls, and roofs of each tank shall be coated with Devchem 253. (Source: `SCOPE_LEDGER.csv` `SOW-0203`.)

REQ-097-01-07 — Per-tank pressure protection. Each tank shall be furnished with:
- a Pressure-Vacuum Relief Valve (PVRV) for vacuum and modulating pressure relief, and
- an Emergency Pressure Relief Valve (EPRV) sized for the single worst-case relief event.
(Source: `SCOPE_LEDGER.csv` `SOW-0203`.)

REQ-097-01-08 — Per-tank vapour and blanket connections. Each tank shall include a VRU header connection and a blanket-gas connection. (Source: `SCOPE_LEDGER.csv` `SOW-0203`.) Additional per-tank fittings beyond those enumerated are `TBD` pending full `26020-Package_Requirements.docx` heading 49 text.

REQ-097-01-09 — Fill control. Each tank shall be configured for a maximum 90 % shutdown fill limit. (Source: `SCOPE_LEDGER.csv` `SOW-0203`.)

REQ-097-01-10 — Fill rate / nozzle sizing. Tank nozzles shall be sized so plant design capacity can fill a single tank. (Source: `SCOPE_LEDGER.csv` `SOW-0203`.)

REQ-097-01-11 — Operating envelope. Operating pressure: atmospheric (ambient). Operating temperature: 0 °C minimum to 40 °C maximum. (Source: `SCOPE_LEDGER.csv` `SOW-0204`.)

REQ-097-01-12 — Design envelope. Design pressure: 32 oz test pressure. Design temperature: -40 °C minimum to 60 °C maximum. (Source: `SCOPE_LEDGER.csv` `SOW-0204`.)

REQ-097-01-13 — Capacity. Capacity / design throughput: 94,940 kg/h; 3,187 Am3/d (Preliminary Design conditions). (Source: `SCOPE_LEDGER.csv` `SOW-0204`.)

REQ-097-01-14 — Battery limits exclusions. Foundations, at-site mounting, electrical / instrumentation, platforms, and staircases are "By Others" and not within Package Vendor supply. (Source: `SCOPE_LEDGER.csv` `SOW-0204`.)

REQ-097-01-15 — Responsibility model. The Scope of Work shall state that Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: `PACKAGE_REGISTER.csv` row 88.)

REQ-097-01-16 — Interface coverage. The Scope of Work shall enumerate the nine package-level interfaces declared in `INTERFACE_REGISTER.csv` for `PKG-097` (Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports). Detailed interface facts are documented in `DEL-097-02_package-datasheet` per the decomposition note.

REQ-097-01-17 — Carry-through of decomposition scope items. The Scope of Work shall reference (not restate) `SOW-0201` through `SOW-0204` and shall state which deliverable artifacts within `PKG-097` consume each item. (Source: `SCOPE_LEDGER.csv`; `_CONTEXT.md` Covers Scope Items.)

REQ-097-01-18 — Objective alignment. The Scope of Work shall acknowledge the supports-objective set `OBJ-002`..`OBJ-010` (ASSUMPTION: package-grouping heuristic per `_CONTEXT.md`). (Source: `_CONTEXT.md`; `OBJECTIVE_REGISTER.csv`.)

## Standards

| Standard | Applicability | Status |
|---|---|---|
| API 650 (modified) | Tank design and fabrication | Active; modification points sourced from `SCOPE_LEDGER.csv` `SOW-0203`. Clause-level location in API 650 text: location TBD (standard not in `_REFERENCES.md`). |
| API 2000 | Tank venting / blanket-gas system | Active; sourced from `SCOPE_LEDGER.csv` `SOW-0203`. Clause-level location: location TBD. |
| Devchem 253 product datasheet | Internal coating product specification | Active product name only; vendor datasheet location TBD. |
| `26020-Package_Requirements.docx` heading 49 | Package-requirement clauses (project-internal) | Authoritative source; binary file not slice-extracted beyond the workbook-extracted ledger rows — additional clause text: location TBD. |
| 03-25 facility DBM (`3-25_Comp_and_Liquids_DBM.md`) | Whole-facility integration basis | Active; cited for service, site basis, and facility integration only. |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-097-01-01 to REQ-097-01-02 | Document review of issued Scope of Work against `PACKAGE_REGISTER.csv` row 88 and `SCOPE_LEDGER.csv` `SOW-0201`/`SOW-0202`. |
| REQ-097-01-03, REQ-097-01-04 | Cite the standard names verbatim in the Scope of Work; check by review against `SCOPE_LEDGER.csv` `SOW-0203`. |
| REQ-097-01-05 to REQ-097-01-10 | Line-by-line cross-check of Scope-of-Work clauses against `SCOPE_LEDGER.csv` `SOW-0203`. |
| REQ-097-01-11 to REQ-097-01-13 | Line-by-line cross-check against `SCOPE_LEDGER.csv` `SOW-0204`. |
| REQ-097-01-14 | Review "By Others" list against `SCOPE_LEDGER.csv` `SOW-0204`. |
| REQ-097-01-15 | Responsibility statement compared verbatim with `PACKAGE_REGISTER.csv` row 88 Responsibility model column. |
| REQ-097-01-16 | Interface table in the Scope of Work compared with the 9 `PKG-097` rows in `INTERFACE_REGISTER.csv`. |
| REQ-097-01-17 | Scope-item traceability table in the Scope of Work shall reference `SOW-0201`..`SOW-0204`. |
| REQ-097-01-18 | Supports-objective list checked against `_CONTEXT.md` (and flagged as ASSUMPTION). |

## Documentation

Anticipated artifacts (carried from `_CONTEXT.md` / `DELIVERABLE_REGISTER.csv` row 492):

- Package scope of work (the primary issued document)
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

Provenance handling: every clause in the issued Scope of Work shall carry a citation to (a) `PACKAGE_REGISTER.csv` row 88, (b) one of `SOW-0201`..`SOW-0204`, (c) `26020-Package_Requirements.docx` heading 49, or (d) `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` for facility-integration narrative. Unsourced statements are `TBD`.
