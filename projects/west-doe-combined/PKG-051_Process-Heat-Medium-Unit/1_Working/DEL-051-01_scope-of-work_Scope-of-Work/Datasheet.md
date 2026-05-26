# Datasheet: DEL-051-01_scope-of-work — Scope of Work

> Descriptive datasheet for the EPC Integrator Scope of Work for PKG-051 Process Heat Medium Unit. Values cite Workbook Packages row 79 (SOW-0165..0168) and DBM-Deepcut `4-25_Deepcut_DBM.md` `## Heat Medium Basis` (lines 1945-2002) as locally accessible source slices. Items not present in those slices are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-051-01_scope-of-work` | `_CONTEXT.md` Identity |
| Deliverable Name | Scope of Work | `_CONTEXT.md` Identity |
| Parent Package | `PKG-051` Process Heat Medium Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row |
| Workbook Tracking Number | `26020-01-15-001` | `PACKAGE_REGISTER.csv` row PKG-051 |
| Workbook Row | 79 (WBS 01) | `PACKAGE_REGISTER.csv` row PKG-051 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` (responsibility model) |
| Covers Scope Items | SOW-0165, SOW-0166, SOW-0167, SOW-0168 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; ASSUMPTION (package-grouping heuristic per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |

## Attributes (Package Subject)

| Attribute | Value | Source |
|---|---|---|
| Package function | Closed-loop hot oil / heat medium system supplying heat to multiple process users in the facility. | SOW-0166 (Basic scope) |
| Architecture per workbook scope | Pump Module (expansion tank + 3 pumps) and Medium Heater Module (one medium heater, one heater blower, one air intake pre-heater) with hot/cold loop and hot/cold mixing for optimum supply temperature. | SOW-0166 (Basic scope); SOW-0167 (Major equipment) |
| Architecture per Deepcut DBM | Single unified heat medium loop at 220 °C (428 °F); pre-existing cold/hot loop segregation, separate hot expansion tank, and separate hot pumps are retired; mole sieve regeneration gas heating removed from the loop. | `4-25_Deepcut_DBM.md` `## Heat Medium Basis` (lines 1945-1947) |
| Heat medium fluid | Brenntag Petrotherm (DBM); Petro-Canada Petrotherm (Workbook). Both reference Petrotherm. Vendor confirmation of fluid rating to maximum bulk temperature required during detailed engineering. | `4-25_Deepcut_DBM.md` line 1951; SOW-0167 |
| Maximum normal operating temperature | 428 °F (220 °C) | `4-25_Deepcut_DBM.md` line 1957 |
| Maximum bulk fluid temperature | 599 °F (315 °C) per DBM; 500 °F (260 °C) per Workbook SOW-0167 | `4-25_Deepcut_DBM.md` line 1958; SOW-0167. CONFLICT — see Guidance Conflict Table. |
| Assumed start-up temperature | 68 °F (20 °C) | `4-25_Deepcut_DBM.md` line 1956; SOW-0167 (consistent) |
| Total required loop duty (post-VE basis) | ~21,913 kW (~74.8 MM BTU/h) at winter design | `4-25_Deepcut_DBM.md` lines 1976 (duty table total) |
| Heater design duty basis | 1.25 × winter steady-state design duty (sparing 1 × 125 % pending review of multi-heater options) | `4-25_Deepcut_DBM.md` line 1998 |
| Heater type | API-560 natural-draft cabin-style direct-fired thermal-fluid heater | `4-25_Deepcut_DBM.md` line 1998 |
| Heater burner turndown | 4:1 typical with burner management for additional turndown | `4-25_Deepcut_DBM.md` line 1998 |
| Circulation pumps | Single-stage vertical inline; cold-start at 15 °C (DBM); 3 × 66 % per Workbook; consolidated sparing TBC. | `4-25_Deepcut_DBM.md` line 1996; SOW-0167 |
| Expansion tank | Horizontal; size/capacity by vendor; expansion volume at 274 °C to fill max 85 %. | SOW-0167 |
| Pop tank | ~600 bbl, normally empty, level switch for empty validation; sour tube-rupture venting to pop tank to be reviewed. | `4-25_Deepcut_DBM.md` line 2002 |

## Conditions (Design and Operating)

| Parameter | Value | Source |
|---|---|---|
| Heat medium components design pressure | ≥ 350 psig (2413 kPag) | `4-25_Deepcut_DBM.md` line 1983; SOW-0167; SOW-0168 |
| Pump discharge operating pressure (estimated) | ~100 psig (695 kPag), assuming 75 psid pump differential, TBC | `4-25_Deepcut_DBM.md` line 1983; SOW-0167 |
| Expansion tank operating pressure | 125–240 kPag (18–35 psig) per Workbook (depends on NPSHR) | SOW-0167. Note: SOW-0168 states 695 kPag (100 psig); CONFLICT — see Guidance Conflict Table. |
| Expansion tank operating temperature | 20 °C to 260 °C | SOW-0168 |
| Heat medium pump design temperature | 274 °C | SOW-0167; SOW-0168 |
| Total heat medium supply (approximate) | 151.6 m³/day | SOW-0168 |
| Single-loop circulation rates | TBD pending detailed engineering simulation | `4-25_Deepcut_DBM.md` line 1961 |
| Minimum circulation basis | ~85 % of design flow for fired-heater operation, TBC | `4-25_Deepcut_DBM.md` line 1961 |
| Heater pressure drop | ~25 psid (172 kPad) assumed | `4-25_Deepcut_DBM.md` line 2000 |
| Heater area classification | General Purpose | `4-25_Deepcut_DBM.md` line 2000 |
| Pour point | TBC | `4-25_Deepcut_DBM.md` line 1955 |
| Maximum tubeskin / film temperature | TBC | `4-25_Deepcut_DBM.md` line 1959 |

## Construction (Scope Boundaries and Exclusions)

| Item | Value | Source |
|---|---|---|
| Included — Pump Module | Expansion tank + 3 vertical inline circulation pumps. | SOW-0166; SOW-0167 |
| Included — Medium Heater Module | One medium heater (direct-fired thermal-fluid heater), one heater blower, one air intake pre-heater. | SOW-0166 |
| Included (DBM-aligned) — Pop tank | Heat medium heater PSV discharge tank (~600 bbl) is part of the heat medium system scope. | `4-25_Deepcut_DBM.md` line 2002. ASSUMPTION (DBM-aligned): inclusion in vendor package boundary vs. EPC scope to be confirmed. |
| By Others (EPC Integrator or other) | Interconnecting piping; DCS integration; foundations; mounting buildings at site; electrical supply from MCC; platforms, stairs, etc. | SOW-0168 (Scope notes and open items) |
| Package vendor responsibility | Package engineering, package design, vendor documentation, physical equipment package. | `PACKAGE_REGISTER.csv` row PKG-051 (responsibility model); OBJ-004 |
| EPC Integrator responsibility | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration. | `PACKAGE_REGISTER.csv` row PKG-051 (responsibility model) |
| Applicable interface types | Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. | `PACKAGE_REGISTER.csv` row PKG-051 (applicable interface types) |
| Source-stated exclusions | None package-specific stated in source materials. | `PACKAGE_REGISTER.csv` row PKG-051 (exclusions column) |

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — authoritative basis pointers
- Workbook Packages row 79 — captured via `PACKAGE_REGISTER.csv` row `PKG-051` in `GATE-07_Final_Published_2026-05-24/`
- `26020-Package_Requirements.docx` package heading 6 — captured via `SCOPE_LEDGER.csv` rows SOW-0165, SOW-0166, SOW-0167, SOW-0168
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` `## Heat Medium Basis` (lines 1945-2002), `## Utilities and Support Systems Basis` heat medium entries (line 1832), and Energy Balance heat-medium rows (lines 1884, 2242-2243, 2264, 2293, 2357-2359, 2435)
- `OBJECTIVE_REGISTER.csv` — OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010
- `SCOPE_LEDGER.csv` — SOW-0165, SOW-0166, SOW-0167, SOW-0168
- `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` — binary; not directly readable in this run; location TBD for clause-level rereads
