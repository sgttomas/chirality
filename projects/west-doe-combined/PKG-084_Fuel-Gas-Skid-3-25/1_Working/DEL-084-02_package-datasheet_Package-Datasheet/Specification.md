# Specification — DEL-084-02 Package Datasheet (PKG-084 Fuel Gas Skid 3-25)

> Normative requirements for the Package Datasheet deliverable: what the EPC Integrator must capture, in what form, and how it will be verified before vendor handoff.

## Scope

### In scope

- Capture all source-supported package-level data required by a third-party vendor (or internal discipline package engineering team) to engineer, design, and supply the Low-Pressure Fuel Gas Package (skid-mounted LP fuel gas heater + LP fuel gas scrubber) as defined in `PACKAGE_REGISTER.csv` row PKG-084.
- Carry interface facts (per `_CONTEXT.md` "interface facts are intentionally carried here as evidence") at a package level for the interface types listed in `PACKAGE_REGISTER.csv` row PKG-084 (`Applicable interface types`).
- Reflect the source-of-truth design values from the accessible DBM source slices, with explicit `TBD` for values not present in those slices.

### Out of scope (explicitly)

- Vendor-side detailed engineering (cylinder/coil sizing, instrument loop diagrams, P&IDs) — handled under DEL-084-04 Vendor Engineered Equipment Package.
- EPC Scope of Work (DEL-084-01), Construction Work Package (DEL-084-03), Vendor Document Turnover (DEL-084-05), and EPC Vendor Package Review and Acceptance (DEL-084-06).
- Detailed clause-level standards extraction beyond what is locally accessible in source slices. Where standards/codes are cited but the clause text is not locally accessible, the requirement is marked `location TBD`.
- Whole-facility integration design (e.g., 03-25/04-25 facility split, shared-utility allocation) beyond what is necessary to define the package boundary.

Source for scope: `_CONTEXT.md` (Scope, Notes); `DELIVERABLE_REGISTER.csv` row DEL-084-02; `PACKAGE_REGISTER.csv` row PKG-084.

## Requirements

### R-DS-1 — Identification completeness (FACT)

The Package Datasheet shall populate, at minimum, the Identification block in `Datasheet.md` from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row PKG-084. Required fields: Deliverable ID, Package ID, Package Name, Workbook Row, Workbook Tag, Discipline, Type, Responsible Party, WBS, Source Basis.

Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-084.

### R-DS-2 — Equipment composition (FACT)

The datasheet shall enumerate the in-package equipment items as defined by `PACKAGE_REGISTER.csv` row PKG-084 description column: one (1) LP fuel gas heater and one (1) LP fuel gas scrubber.

Source: `PACKAGE_REGISTER.csv` row PKG-084 (description).

### R-DS-3 — LP fuel gas service basis (FACT)

The datasheet shall record service basis values that are directly traceable to source slices. Required attributes and source-bound values:

- Normal total LP fuel gas flow: 1.382 MMSCFD (39.13 e3m3/d) — `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463.
- Design LP fuel gas flow: > 1.5 MMSCFD (42.5 e3m3/d), exact value TBC — `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463.
- Fuel-gas source / pressure / MAWP table (Enbridge, Alliance) — `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L458-461.
- LP fuel gas user list — `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L456, L463; `DBM-Deepcut/4-25_Deepcut_DBM.md` L1830.

### R-DS-4 — LP fuel gas heater design basis (FACT)

The datasheet shall require the heater to be:

- electric resistance type, SCR-controlled;
- sized for maximum sales-compressor discharge pressure and winter ambient buyback gas conditions;
- equipped with skin-temperature thermocouple override and gas-outlet temperature control to prevent overheating under stagnant-gas conditions.

Heater duty (kW) shall be marked `TBD` in the datasheet until vendor sizing is performed.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872.

### R-DS-5 — LP fuel gas scrubber design basis (FACT)

The datasheet shall require the scrubber to be:

- located downstream of the LP fuel gas heater;
- sized using a maximum K factor of 0.35 Imperial with operating-pressure derating;
- sized for the fuel gas system design flow at design operating pressure;
- based on hydrocarbon liquid density at 150 psig and initial dewpoint;
- routed to TK-9130-1 / TK-9130-2 slop for condensed liquids.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463.

### R-DS-6 — Interface declaration (FACT)

The datasheet shall declare interface types per `PACKAGE_REGISTER.csv` row PKG-084 (`Applicable interface types`): Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

Tag-level interface IDs are out of scope; rolled-up interface tags from `INTERFACE_REGISTER.csv` may be referenced when applicable to package boundary definition.

### R-DS-7 — Pressure envelope (ASSUMPTION → TBD until ruled)

The datasheet shall record the package design pressure envelope as `TBD` and require that vendor design envelop the supply MAWP of 9,928 kPag (1,440 psig) per `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L458-461, unless upstream pressure-protection philosophy is documented and accepted. Final design pressure shall be confirmed during vendor engineering. ASSUMPTION until human ruling on pressure-protection scheme.

### R-DS-8 — Emergency buyback inclusion (NEEDS_HUMAN_RULING)

The datasheet shall NOT pre-judge the emergency buyback fuel gas scope. The conflict between W242510 (not required) and Process_DBM_fixed (included in 04-25 utility package) shall be carried as `NEEDS_HUMAN_RULING` in `Guidance.md` Conflict Table.

Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L465.

### R-DS-9 — Provenance discipline (FACT)

Every non-trivial value in `Datasheet.md` shall cite its source slice (file path + section / line reference) or be marked `TBD`. Inferences shall be labeled `ASSUMPTION`.

Source: governing skill `four-documents/SKILL.md` non-negotiable constraint "Source-anchored with explicit assumptions."

### R-DS-10 — Authority hierarchy (FACT)

When source materials and decomposition narrative disagree, source materials are authoritative; the discrepancy shall be recorded in the Conflict Table in `Guidance.md`.

Source: `four-documents/SKILL.md` "Authority hierarchy".

### R-DS-11 — No silent reconciliation (FACT)

Conflicting source values (e.g., V-3210-1 vs V-3210-2, emergency buyback inclusion) shall be surfaced in the Conflict Table, not silently chosen.

Source: `four-documents/SKILL.md` Step 5; `_CONTEXT.md` Notes.

## Standards

The following standards/codes are likely applicable based on package type and discipline. Where the clause text is not locally accessible, `location TBD` is recorded and no clause-level requirement is derived (per skill rules).

| Standard / Code | Applicable to | Notes |
|---|---|---|
| ASME Section VIII Div. 1 | LP fuel gas scrubber (pressure vessel) | ASSUMPTION; location TBD; standard not slice-read |
| ASME B31.3 | LP fuel gas process piping at skid limits | ASSUMPTION; location TBD |
| API 12J or API 14E (separator/gas-handling guidance) | LP fuel gas scrubber sizing context | ASSUMPTION; location TBD |
| NEMA MG 1 | Electrical equipment supporting heater controls (where applicable) | Cross-reference: NEMA MG 1 is cited at facility level for compressor motors in `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L533 — not directly applicable to the heater itself; ASSUMPTION |
| CSA / OGAOM | BC oil & gas facility siting (spacing for fired/heated equipment) | Cross-reference: OGAOM Sec. 9.6.15 cited in `DBM-Deepcut/4-25_Deepcut_DBM.md` L295-298 for fired heaters; package heater is electric, so siting requirement may not apply identically — ASSUMPTION; location TBD |
| Owner / EPC project specifications | Materials, painting, instrumentation, electrical area class | TBD; not in accessible source set |

Standards listed in `PACKAGE_REGISTER.csv` row PKG-084: the row carries `Applicable interface types` but does not enumerate code/standard rows. Any deeper standards basis shall be drawn from `26020-Package_Requirements.docx` heading 37 (not locally accessible — location TBD) and the project EPC specification suite.

## Verification

| Req ID | Verification Approach | Evidence | Owner |
|---|---|---|---|
| R-DS-1 | Cross-check `Datasheet.md` Identification block against `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row PKG-084 | Datasheet block + register row | EPC Integrator (this deliverable QA) |
| R-DS-2 | Cross-check equipment list against `PACKAGE_REGISTER.csv` description column | Datasheet Equipment List | EPC Integrator |
| R-DS-3 | Quote-match values to source-slice line numbers cited in Datasheet "Service / Process Attributes" | Datasheet Service block | EPC Integrator |
| R-DS-4 | Quote-match heater paragraph against `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 | Datasheet Heater block | EPC Integrator |
| R-DS-5 | Quote-match scrubber paragraph against `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874 and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 | Datasheet Scrubber block | EPC Integrator |
| R-DS-6 | Interface-type list parity check vs `PACKAGE_REGISTER.csv` PKG-084 | Datasheet Interface Matrix | EPC Integrator |
| R-DS-7 | Confirm design pressure carried as `TBD` and ASSUMPTION rationale present | Datasheet + Guidance | EPC Integrator + Owner ruling |
| R-DS-8 | Confirm Conflict Table CF-03 entry exists for emergency buyback ruling | `Guidance.md` Conflict Table | Owner ruling required |
| R-DS-9 | Audit every non-trivial value for source citation or `TBD` | Datasheet provenance | QA review (human) |
| R-DS-10 | Confirm any source-vs-decomposition disagreements appear in Conflict Table | Conflict Table | QA review (human) |
| R-DS-11 | Confirm no silent reconciliation of conflicts | Conflict Table coverage | QA review (human) |

## Documentation

The package datasheet rolls up the following anticipated artifacts per `DELIVERABLE_REGISTER.csv` row DEL-084-02:

- Package technical datasheet (this `Datasheet.md`)
- Vendor engineering handoff basis (this `Datasheet.md` + `Guidance.md`)
- Package interface requirements matrix (Datasheet "Interface Requirements Matrix"; tag-level detail deferred to EPC interface deliverables)
- Source-supported equipment and design criteria (this `Datasheet.md` Equipment + Service + Construction sections)

Final issued package datasheet shall be promoted to `2_Issued/` per the Chirality deliverable lifecycle. Vendor RFQ shall reference this datasheet as part of the package inquiry document set, alongside `26020-02-PT-RFQ-23-001_FG_Skid_1.docx`.

Source: `DELIVERABLE_REGISTER.csv` row DEL-084-02; `PACKAGE_REGISTER.csv` row PKG-084 (Word Source Basis).
