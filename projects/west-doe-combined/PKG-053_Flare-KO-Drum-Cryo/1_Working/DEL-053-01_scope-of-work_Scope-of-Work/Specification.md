# Specification: DEL-053-01_scope-of-work — Scope of Work

## Scope

This deliverable specifies the EPC scope-of-work content for `PKG-053 — Flare KO Drum (Cryo)`, a Mechanical WBS 01 vendor-engineered equipment package at the West Doe Deepcut (04-25) facility. It covers the package identity, source basis, boundaries, applicable interfaces, package function, whole-facility integration narrative, and responsibility split between the Package Vendor (engineering, design, vendor documentation, physical equipment) and the EPC Integrator (facility integration).

Included scope:

- Carry SOW-0067 through SOW-0070: the workbook-defined Mechanical package "Flare KO Drum (Cryo)" as a distinct flat project package for WBS 01 with CoA tracking number `26020-01-17-001` (`PACKAGE_REGISTER.csv`, PKG-053; `SCOPE_LEDGER.csv`, SOW-0067).
- Document the basic package scope: cryogenic flare KO drum plus electric immersion heater supplied as a single equipment package (`SCOPE_LEDGER.csv`, SOW-0068; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems).
- Identify the major included equipment by tag: V-4110-1 (cryogenic flare KO drum) and H-4112-1 (electric immersion heater) (`SCOPE_LEDGER.csv`, SOW-0069; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems and Tagged Equipment table).
- Record service basis: drum serves cryogenic-unit reliefs and molecular-sieve-dehydrated systems with PSVs relieving below -45.5 deg C; non-sour per the brief (`SCOPE_LEDGER.csv`, SOW-0070; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems).
- Document the applicable interface types from the Gate 7 register: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports (`INTERFACE_REGISTER.csv`, PKG-053).
- Align the integration narrative with the 04-25 Deepcut DBM flare-systems and spacing basis (`4-25_Deepcut_DBM.md`, SEC-02; SEC-09).
- Identify missing package-specific design values as `TBD` and route them to DEL-053-02 (Package Datasheet) and detailed engineering rather than deriving them here.

Excluded or deferred scope:

- Package-specific exclusions are `TBD`; no source-specific exclusions are stated for PKG-053 (`PACKAGE_REGISTER.csv`, PKG-053).
- Drum sizing, MAWP, MDMT, nozzle schedule, materials of construction, heater electrical rating and control philosophy, instrumentation specification, structural/foundation loads, and tie-in coordinates are `TBD` until the Package Datasheet and detailed engineering are issued.
- HP flare KO drum (V-4100-1) and LP flare KO drum (V-3900-1) are separate workbook packages and are not in this scope (`4-25_Deepcut_DBM.md`, SEC-09 Flare Systems).
- Common HP/cryo flare stack supply is not in this package; PKG-053 terminates where the cryogenic flare header combines with the HP flare header downstream of the KO drums (`4-25_Deepcut_DBM.md`, SEC-09 Flare Systems).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-053-01 | The scope of work shall identify `PKG-053 — Flare KO Drum (Cryo)` as a Mechanical package under WBS 01 with CoA tracking number `26020-01-17-001`. | `PACKAGE_REGISTER.csv`, PKG-053 |
| REQ-053-02 | The scope of work shall identify SOW-0067, SOW-0068, SOW-0069, and SOW-0070 as the covered scope items and retain the package as a distinct flat project package. | `SCOPE_LEDGER.csv`, SOW-0067 through SOW-0070 |
| REQ-053-03 | The scope of work shall include the mandatory EPC scope-of-work artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | `DELIVERABLE_REGISTER.csv`, DEL-053-01_scope-of-work |
| REQ-053-04 | The scope of work shall identify the major included equipment as V-4110-1 (cryogenic flare KO drum) and H-4112-1 (electric immersion heater) supplied as a single equipment package. | `SCOPE_LEDGER.csv`, SOW-0068; SOW-0069; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| REQ-053-05 | The scope of work shall define the cryogenic flare service as serving cryogenic-unit reliefs and molecular-sieve-dehydrated systems whose PSVs relieve below -45.5 deg C. | `SCOPE_LEDGER.csv`, SOW-0070; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| REQ-053-06 | The scope of work shall declare service as non-sour per the brief and require source-basis re-confirmation during detailed engineering. | `SCOPE_LEDGER.csv`, SOW-0070 |
| REQ-053-07 | The scope of work shall include the nine declared interface types from `INTERFACE_REGISTER.csv` for PKG-053: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv`, PKG-053 |
| REQ-053-08 | The scope of work shall locate the cryogenic flare header tie-in upstream of V-4110-1 with the cryogenic relief header sized at 610 mm (24 in). | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| REQ-053-09 | The scope of work shall identify the downstream battery limit where the cryogenic flare header combines with the HP flare header downstream of both KO drums before the common HP/cryo stack. | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| REQ-053-10 | The scope of work shall reflect that the cryogenic flare KO drum and its inlet header are not heat traced because water is not expected; streams have passed through molecular sieve dehydration and contain less than 0.1 ppm H2O. | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems; Drains table - Cryogenic drain row |
| REQ-053-11 | The scope of work shall require the cryogenic drain header at the KO drum to be a segregated drain header with minimum 300# ANSI design-pressure basis. | `4-25_Deepcut_DBM.md`, SEC-09 Drains; Cryogenic drain row |
| REQ-053-12 | The scope of work shall apply the 10 m (32 ft) spacing requirement between flare tanks (including KO drums) and vegetation or other fire hazards. | `4-25_Deepcut_DBM.md`, SEC-02 Flare and Incinerator Spacing; OGAOM Sec. 9.6.15 |
| REQ-053-13 | The scope of work shall split responsibility so that the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package, and the EPC Integrator owns integration into the facility, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv`, PKG-053 |
| REQ-053-14 | The scope of work shall mark drum sizing, MAWP, MDMT, material grades, nozzle schedule, immersion heater rating and control philosophy, instrumentation, structural loads, and tie-in coordinates as `TBD` at this deliverable and route them to DEL-053-02 Package Datasheet and detailed engineering. | `DELIVERABLE_REGISTER.csv`, DEL-053-02_package-datasheet; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems (relief volumes TBD) |
| REQ-053-15 | ASSUMPTION: The scope of work shall identify the package as supporting the West Doe Deepcut 04-25 expansion based on the Tagged Equipment table assignment of V-4110-1/H-4112-1 to 4-25 (Deepcut). | `4-25_Deepcut_DBM.md`, Tagged Equipment table row 11 |

## Standards

| Standard or governing content | Status | Source |
|---|---|---|
| OGAOM Sec. 9.6.15 (flare spacing) | Applicable to flare KO drum spacing to vegetation/fire hazards; relied upon by DBM basis | `4-25_Deepcut_DBM.md`, SEC-02 Flare and Incinerator Spacing |
| 300# ANSI design-pressure basis for cryogenic drain header | Required for segregated cryogenic drain header at the KO drum | `4-25_Deepcut_DBM.md`, SEC-09 Drains; Cryogenic drain row |
| Pressure vessel code (ASME BPVC or equivalent) | Applicable to cryogenic KO drum design; specific code, edition, and registration class are TBD at this deliverable and to be confirmed in DEL-053-02 and Vendor Document Turnover | `DELIVERABLE_REGISTER.csv`, DEL-053-05_vendor-document-turnover-package (Pressure Equipment Registration Package); location TBD |
| Aspen Flare System Analyzer modelling basis | Preliminary header sizing relied on Aspen FSA models; relief volumes TBD pending detailed engineering | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| Electrical area classification, EHT, grounding/bonding, and I&C standards | Required for immersion heater and instrumentation tie-ins; specific clause references are TBD | `INTERFACE_REGISTER.csv`, PKG-053; location TBD |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-053-01 through REQ-053-03 | Check scope-of-work identity, deliverable contents, and CoA tracking number against the Gate 7 registers and workbook row 53. |
| REQ-053-04, REQ-053-05 | Check tagged equipment list and service description against `4-25_Deepcut_DBM.md` SEC-09 Flare Systems and the Tagged Equipment table. |
| REQ-053-06 | Re-confirm non-sour basis against the consolidated 04-25 service classification during detailed engineering and update if a sour-service case is identified. |
| REQ-053-07 | Cross-check the nine declared interface types against `INTERFACE_REGISTER.csv`, PKG-053. |
| REQ-053-08, REQ-053-09 | Check header sizing and battery-limit description against `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems narrative and flare materials table. |
| REQ-053-10, REQ-053-11 | Check heat-tracing exclusion and drain-class basis against the SEC-09 Drains table (Cryogenic drain row). |
| REQ-053-12 | Confirm spacing assumptions against the project plot plan when issued and re-check against OGAOM Sec. 9.6.15. |
| REQ-053-13 | Compare responsibility narrative against `PACKAGE_REGISTER.csv` for PKG-053 and against the project responsibility matrix when issued. |
| REQ-053-14 | Confirm that all design-value `TBD` items are carried into DEL-053-02 Package Datasheet and are not silently dropped. |
| REQ-053-15 | Re-confirm facility/unit assignment from the issued P&IDs and the latest tagged equipment list. |

## Documentation

The scope-of-work package shall produce or reference:

- Package scope of work narrative.
- Tagged equipment and package identity list (V-4110-1; H-4112-1; package ID PKG-053; CoA `26020-01-17-001`).
- Package function and integration narrative.
- Responsibility assignment record (Package Vendor vs EPC Integrator split).
- Interface summary covering the nine declared interface types for PKG-053.
- Source basis list and `TBD` / open-item list routed to DEL-053-02 Package Datasheet and downstream vendor and construction packages.
