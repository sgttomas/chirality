# Specification — DEL-094-01 Scope of Work, PKG-094 Tanks, Caustic (API 650) 3-25

> Normative specification of what this EPC Integrator Scope of Work deliverable must contain. Requirements grounded in locally accessible source slices; inferences labeled `ASSUMPTION`; missing items marked `TBD`.

## Scope

### In scope
The Scope of Work deliverable (this production unit) shall define, for PKG-094 "Tanks, Caustic (API 650) 3-25", the EPC Integrator's package-level scope statement, including:

- Package identity and boundaries.
- Tagged equipment list, with package function and integration narrative.
- Source-grounded basic scope (per SOW-0193..SOW-0196).
- Responsibility assignment between EPC Integrator and Package Vendor.
- Whole-facility integration narrative tying the caustic-tank package into the 03-25 Liquids Hub caustic mercaptan treating system.
- Explicit "by others" exclusions per source.

Source: `SCOPE_LEDGER.csv` SOW-0193..0196; `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.

### Out of scope (for this Scope of Work deliverable)
- Detailed vendor engineering, design calculations, or fabrication drawings (carried in DEL-094-04 Vendor Engineered Equipment Package).
- Vendor document register and turnover (DEL-094-05).
- Construction work package, installation/tie-in workface plans (DEL-094-03).
- EPC vendor package review and acceptance (DEL-094-06).
- Detailed Package Datasheet (DEL-094-02).

Source: `DELIVERABLE_REGISTER.csv` rows DEL-094-02..06.

### Excluded from PKG-094 physical scope (by others)
- Foundations and tank mounting at site.
- Electrical and instrumentation.
- Platforms and staircases.

Source: `SCOPE_LEDGER.csv` SOW-0196.

## Requirements

### R1 — Package identity
R1.1 The SoW shall identify PKG-094 as "Tanks, Caustic (API 650) 3-25", parent workbook ID 94, package row 86, discipline Mechanical, WBS 03.
- Source: `DELIVERABLE_REGISTER.csv`; `OBJECTIVE_PACKAGE_MAP.csv`.

R1.2 The SoW shall reference the authoritative source basis: Workbook Packages row 86 and 26020-Package_Requirements.docx package heading 46.
- Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.

### R2 — Tagged equipment
R2.1 The SoW shall list at minimum the tagged spent caustic storage tank TK-6930-2 (1 ea, 400 bbl nominal, modified API 650, atmospheric 32 oz / 1.0 oz vacuum, heater minimum 32.2 °C / 90 °F, vendor-designed heater).
- Source: `SCOPE_LEDGER.csv` SOW-0195.

R2.2 The SoW shall list the fresh caustic tank (1 ea) with function "store and supply fresh caustic solution to the caustic treatment unit". Tag and capacity per Package Datasheet; `ASSUMPTION`: same 400 bbl nominal basis as Item 2 in SOW-0196.
- Source: `SCOPE_LEDGER.csv` SOW-0194/0196; DBM 3-25.

### R3 — Basic scope statement
R3.1 The SoW shall reproduce the source-defined Basic Scope:
> "Supply One (1) spent caustic tank, and one (1) fresh caustic tank. Process function: Fresh Caustic Tank: To store and supply fresh caustic solution to the caustic treatment unit; Spent Caustic Tank: To receive and safely store spent caustic from the pressurized caustic drain drum."
- Source: `SCOPE_LEDGER.csv` SOW-0194 (26020-Package_Requirements.docx package heading 46; Basic scope).

### R4 — Design conditions
R4.1 The SoW shall carry the source-stated design conditions: atmospheric service, minimum ambient design temperature, design pressure 32 oz / 1.0 oz vacuum (Item 1: 400 bbl; Item 2: 400 bbl). Flow rate per item is `TBD`; capacity/throughput is `TBC`.
- Source: `SCOPE_LEDGER.csv` SOW-0195/0196.

R4.2 The SoW shall reflect the facility site basis: minimum ambient -40 °C per the 03-25 DBM, governing exposed equipment metallurgy and winterization.
- Source: DBM 3-25 (Site basis section).

R4.3 The SoW shall carry the caustic-solution basis (50 wt% NaOH/H2O, SG 1.75 TBC), aluminum prohibition in the caustic building, and the LP fuel-gas blanket / heating / insulation requirement.
- Source: DBM 3-25 (Caustic Mercaptan Treating section).

### R5 — Integration / interfaces
R5.1 The SoW shall describe whole-facility integration into the 03-25 Liquids Hub non-regenerative caustic mercaptan treating system (per DBM 3-25), including:
- Fresh-caustic supply path to the caustic treatment unit.
- Spent-caustic receipt path from the pressurized caustic drain drum.
- Spent-caustic vent path to incinerator header via flame arrestor.
- Spent-caustic truck-out provision.
- Fresh-caustic VRU non-connection requirement.
- Source: DBM 3-25.

R5.2 The SoW shall enumerate the package interfaces declared in `INTERFACE_REGISTER.csv` for PKG-094:
- Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports.
- Source: `INTERFACE_REGISTER.csv`.

### R6 — Responsibility assignment
R6.1 The SoW shall assign:
- Package Vendor: engineering, design, fabrication/supply, and physical equipment package (per DEL-094-04 framing).
- EPC Integrator: package SoW authorship, Package Datasheet (DEL-094-02), Construction Work Package (DEL-094-03), vendor package review and acceptance (DEL-094-06), and whole-facility integration.
- Source: `DELIVERABLE_REGISTER.csv`.

R6.2 The SoW shall explicitly carry "by others" items per SOW-0196 (foundations, mounting, electrical/instrumentation, platforms, staircase).
- Source: `SCOPE_LEDGER.csv` SOW-0196.

### R7 — Scope-item traceability
R7.1 The SoW shall trace each scope statement back to SOW-0193, SOW-0194, SOW-0195, or SOW-0196 as appropriate.
- Source: `SCOPE_LEDGER.csv`; `_CONTEXT.md`.

### R8 — Objective coverage
R8.1 The SoW shall acknowledge that PKG-094 supports OBJ-002..OBJ-010 per the objective-to-package map (PACKAGE_HEURISTIC association labeled `ASSUMPTION` until human-confirmed at deliverable-ID level).
- Source: `OBJECTIVE_PACKAGE_MAP.csv`; `_CONTEXT.md`.

### R9 — Open items
R9.1 The SoW shall carry forward all source-declared open items:
- Capacity/design throughput: TBC.
- Flow rate per item: TBD.
- Caustic SG 1.75: TBC.
- Caustic tank material/coating: TBC.
- Produced-water tank SG discrepancy (1.18 vs 1.25) noted in DBM — not directly within PKG-094 caustic scope; record as cross-package note only.
- Source: `SCOPE_LEDGER.csv` SOW-0196; DBM 3-25.

## Standards

| Standard | Applicability | Local Access |
|---|---|---|
| API 650 (Modified) | Atmospheric storage tank design and fabrication for caustic tanks | location TBD (standard text not in local sources) |
| API 650 Modified — facility-wide produced-water tank basis (context) | Referenced in DBM for 03-25 facility tanks generally | DBM 3-25 |
| CSA / Provincial pressure equipment codes for BC | ASSUMPTION: applicable to facility based on BC site; clause-level requirements TBD | location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1.x identity fields | Document review against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` |
| R2.x tagged equipment list | Document review against `SCOPE_LEDGER.csv` SOW-0195 and Package Datasheet (DEL-094-02) |
| R3.1 basic scope text | Verbatim/structural review against SOW-0194 source slice |
| R4.x design conditions | Document review against SOW-0195/0196 and DBM 3-25 |
| R5.x integration narrative | Document review against DBM 3-25 and `INTERFACE_REGISTER.csv` |
| R6.x responsibility assignment | Document review against `DELIVERABLE_REGISTER.csv` rows DEL-094-01..06 |
| R7.1 SOW traceability | Cross-reference matrix in the SoW deliverable |
| R8.1 objective coverage | Map check against `OBJECTIVE_PACKAGE_MAP.csv`; human ruling required to upgrade ASSUMPTION |
| R9.1 open items | Open-items log within the SoW deliverable |

## Documentation

The SoW deliverable artifacts (per `_CONTEXT.md` Anticipated Artifacts) shall include:
- Package scope of work narrative.
- Tagged equipment and package identity list.
- Package function and integration narrative.
- Responsibility assignment record (EPC Integrator vs Package Vendor and "by others").
- Open items / TBD register tied to SOW-0193..0196.
