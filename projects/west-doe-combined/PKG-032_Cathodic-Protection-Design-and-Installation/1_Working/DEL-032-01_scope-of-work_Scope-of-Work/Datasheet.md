# Datasheet: DEL-032-01_scope-of-work — Scope of Work

Descriptive identity and attribute record for the EPC Integrator Scope of Work covering PKG-032 Cathodic Protection Design and Installation.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-032-01_scope-of-work` | `_CONTEXT.md` |
| Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-032` | `_CONTEXT.md` |
| ParentWorkbookID | 32 | `_CONTEXT.md` |
| PackageName | Cathodic Protection Design and Installation | `_CONTEXT.md`; PACKAGE_REGISTER row PKG-032 |
| Package Tag | 26020-03-30-023 | PACKAGE_REGISTER row PKG-032 |
| WBS | 03 | PACKAGE_REGISTER row PKG-032 |
| Discipline | Electrical | `_CONTEXT.md`; PACKAGE_REGISTER row PKG-032 |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0033` | `_CONTEXT.md` |
| Supports Objectives | `OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-009; OBJ-010` | `_CONTEXT.md` (ASSUMPTION: package-grouping heuristic) |

## Attributes

| Attribute | Value | Notes |
|---|---|---|
| Package ownership | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package | PACKAGE_REGISTER row PKG-032 |
| Integration ownership | EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER row PKG-032 |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network | PACKAGE_REGISTER row PKG-032 |
| Facility-design treatment of CP | Cathodic protection engineering and supply is excluded from the facility design scope; facility design supports owner cathodic-protection interfaces | DBM-Deepcut `4-25_Deepcut_DBM.md`, SEC-12 §Cathodic Protection (line 3073-3075) |
| CP scope status in DBM TBD table | Engineering and supply excluded from facility design; owner interface requirements remain to be coordinated | DBM-Deepcut `4-25_Deepcut_DBM.md`, SEC-12 Assumptions/TBDs table (line 3092) |
| Electrical scope inclusion of CP | Cathodic protection listed within electrical-design support scope at facility level | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` line 718, line 770 |

## Conditions

| Condition | Value | Notes |
|---|---|---|
| Tagged equipment list | TBD | Not enumerated in accessible sources; vendor package datasheet pending |
| CP system type (impressed-current vs. sacrificial anode) | TBD | Not specified in accessible sources |
| Protected structures / inventory | TBD | Not enumerated; depends on owner CP basis and final facility layout |
| Design current density / driving voltage | TBD | Not specified in accessible sources |
| AC interference mitigation requirements | TBD | Not specified; coordination with electrical grounding scope expected |
| Power supply rating to rectifier(s) | TBD | Not specified in accessible sources |

## Construction

| Item | Value | Notes |
|---|---|---|
| Construction responsibility | EPC Integrator (facility integration); Package Vendor (package equipment) | PACKAGE_REGISTER row PKG-032 |
| Tie-in points | TBD | Interface points to facility grounding and electrical power TBD |
| Site location within facility | TBD | Not specified in accessible sources |
| Commissioning party | TBD; ASSUMPTION: jointly between owner/vendor and EPC Integrator | Not explicit in accessible sources |

## References

- `_CONTEXT.md` (deliverable identity)
- `_REFERENCES.md` (authoritative basis pointers)
- DELIVERABLE_REGISTER.csv row `DEL-032-01_scope-of-work` (GATE-07_Final_Published_2026-05-24)
- PACKAGE_REGISTER.csv row `PKG-032` (GATE-07_Final_Published_2026-05-24)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 §Cathodic Protection (line 3073-3075) and Assumptions/TBDs table (line 3092)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` electrical-design scope statements (line 718, 770)
- Workbook Packages row 34 (cited via decomposition; not directly opened in this run — `location TBD` for clause text)
