# Specification — DEL-091-02 Package Datasheet (Tank Farm Pump Building 3-25)

## Scope

This specification defines the EPC Integrator's requirements for the Package Datasheet deliverable of PKG-091 Tank Farm Pump Building 3-25. The Package Datasheet is the technical handoff document carrying package data required for third-party vendor or discipline package engineering and design (DELIVERABLE_REGISTER.csv DEL-091-02).

In scope:
- Tagged equipment inventory (P-9295-2; P-9290/9293-2; P-9215/9216-2; P-9210/9220-2; P-9200-2; P-9230-2; P-9211/9221-2; P-9240-2) — source: SOW-0187.
- Process function, configuration, and boundary "by others" — source: SOW-0186, SOW-0188.
- Package interface requirements matrix across all fifteen applicable interface types — source: INTERFACE_REGISTER.csv PKG-091 rows.
- Equipment design criteria and capacity/throughput — source: SOW-0187, SOW-0188.

Excludes:
- Vendor package engineering, design, and fabrication itself (DEL-091-04 — Package Vendor scope).
- Vendor document register and turnover (DEL-091-05).
- Construction work packaging and tie-in workface plans (DEL-091-03).
- Vendor package review and acceptance evidence (DEL-091-06).
- Per PACKAGE_REGISTER.csv exclusions cell: "TBD; no package-specific exclusions stated in source materials."

## Requirements

| ReqID | Requirement | Source / Basis | Label |
|---|---|---|---|
| R-1 | The datasheet shall identify the package as PKG-091 / Workbook row 84 / WBS 03 with tag prefix 26020-03-18-001. | PACKAGE_REGISTER.csv | FACT |
| R-2 | The datasheet shall list each tagged pump with tag, type, seal plan (where applicable), and rated power as stated in SOW-0187. | SCOPE_LEDGER SOW-0187 | FACT |
| R-3 | The datasheet shall record design throughput/capacity values verbatim from SOW-0188, including the source-stated "TBC" placeholders, without invented substitutions. | SCOPE_LEDGER SOW-0188 | FACT |
| R-4 | The datasheet shall state the package electrical supply basis: 575 V / 3 Ph / 60 Hz motors, fed from 600 V MCC, with DOL or VFD starting and local H-O-A or On-Off control. | SCOPE_LEDGER SOW-0188 | FACT |
| R-5 | Motors shall be sized for inlet stabilizer composition density at −40 °C start-up condition. | SCOPE_LEDGER SOW-0188 | FACT |
| R-6 | "By others" boundaries (DCS integration, foundations, electrical supply to MCC) shall be carried as explicit exclusions of the vendor-supplied package. | SCOPE_LEDGER SOW-0188 | FACT |
| R-7 | The datasheet shall enumerate all fifteen interface types listed in INTERFACE_REGISTER for PKG-091 with their InterfaceIDs, marking each as applicable. | INTERFACE_REGISTER.csv | FACT |
| R-8 | Seal plans for vertical inline centrifugal pumps shall be API-682 Plan 14/52 as specified in SOW-0187. | SCOPE_LEDGER SOW-0187 | FACT |
| R-9 | The datasheet shall identify EPC Integrator as the deliverable's responsible party and clearly delineate Package Vendor vs EPC Integrator responsibilities per PACKAGE_REGISTER.csv responsibility-mode narrative. | PACKAGE_REGISTER.csv | FACT |
| R-10 | The datasheet shall be source-grounded; values not explicitly present in the workbook row 84 / Word heading 44 / DBM source slices shall be carried as TBD. | _REFERENCES.md; SKILL authority hierarchy | FACT |
| R-11 | The datasheet shall cite the upstream snapshot GATE-07 Final Published 2026-05-24 as authoritative decomposition basis. | _REFERENCES.md | FACT |
| R-12 | Operating and design conditions beyond throughput and electrical supply remain TBC per source language; the datasheet shall not synthesize unstated values. | SCOPE_LEDGER SOW-0188 | FACT |

## Standards

| Standard | Application | Location |
|---|---|---|
| API-682 | Mechanical seal plan for vertical inline centrifugal pumps (Plan 14/52 for sour and condensate booster/feed services). | Cited in SOW-0187; clause-level text not locally accessible — location TBD. ASSUMPTION: governing edition follows project-wide convention (TBD). |
| CSA C22.1 / NEC (electrical code) | 575 V / 3 Ph / 60 Hz motor wiring and MCC interconnect at site. | ASSUMPTION based on project geography (Canadian DOE project context); not explicit in source slices — location TBD. |
| NFPA-class fire & gas standards | Interface IFC-9D2C05504D Fire & Gas / Safety Systems. | TBD — no clause-level source carried in snapshot. |

## Verification

| ReqID | Verification Approach | Records |
|---|---|---|
| R-1 .. R-2 | Cross-check datasheet identity and equipment list against PACKAGE_REGISTER row PKG-091 and SCOPE_LEDGER SOW-0185/SOW-0187. | Review checklist; signed completion sheet. |
| R-3 .. R-5 | Tabular comparison of datasheet capacity/electrical entries against SCOPE_LEDGER SOW-0188 with `TBC` items flagged. | Review log. |
| R-6 | Boundary review against SOW-0188 "By others" line. | Boundary checklist. |
| R-7 | Interface count and labels reconciled with INTERFACE_REGISTER.csv (15 rows, each `Applies=YES`). | Interface matrix QA report. |
| R-8 | Vendor seal plan declarations reconciled against API-682 Plan 14/52 statement. | Vendor data review record. |
| R-9 | Responsibility narrative cross-checked against PACKAGE_REGISTER responsibility-mode cell. | Review log. |
| R-10 .. R-12 | QA grep for non-`TBD` non-cited substantive values; conflict table review. | QA report attached to deliverable run record. |

## Documentation

The Package Datasheet deliverable produces the following anticipated artifacts (per _CONTEXT.md):

- Package technical datasheet (`Datasheet.md` is the deliverable-local production document of record for this folder; native vendor datasheet forms TBD downstream).
- Vendor engineering handoff basis (carried in `Datasheet.md` and `Guidance.md`).
- Package interface requirements matrix (carried in `Datasheet.md`).
- Source-supported equipment and design criteria (carried in `Datasheet.md`).
