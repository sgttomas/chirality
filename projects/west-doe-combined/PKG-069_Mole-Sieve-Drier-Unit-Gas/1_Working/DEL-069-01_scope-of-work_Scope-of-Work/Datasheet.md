# Datasheet — DEL-069-01 Scope of Work (PKG-069 Mole Sieve Drier Unit (Gas))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-069-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-069` — Mole Sieve Drier Unit (Gas) | `PACKAGE_REGISTER.csv` row (WorkbookRow=73) |
| Workbook Row | 73 | `PACKAGE_REGISTER.csv` (WorkbookRow=73) |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-22-002 | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE (workbook-defined vendor-responsible Mechanical package) | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (basic scope) | Provide final dehydration of process gas upstream of cryogenic recovery via three molecular-sieve adsorber driers, with associated inlet filter/coalescers, dust filtration, and regeneration support. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (Mole Sieve narrative, line ~1243); `PACKAGE_REGISTER.csv` PKG-069 ScopeSummary |
| Major Tagged Equipment (per DBM equipment inventory) | `AC-6180-1`, `K-6190-1`, `K-6195-1`, `F-5910-1`, `F-5920-1`, `F-6151-1`, `F-6155-1`, `E-6170-1`, `V-6160-1`, `V-6130-1`, `V-6140-1`, `V-6150-1`, `V-6185-1` | `DBM-Deepcut/4-25_Deepcut_DBM.md` equipment table (line ~2607, row 56 "Mole Sieve Drier Unit (Gas)") |
| Configuration | Two driers in adsorption (downflow) while the third is in standby, regeneration, or cooling; two 100% inlet filter/coalescers upstream; molecular-sieve dust filtration and mercury recovery unit downstream prior to cryogenic unit. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1243, line ~1263); spares table (line ~2362–2364) |
| Sparing Philosophy (Gas Mole Sieve) | Inlet Filter Coalescer 2 × 100% (200% installed); Mole Sieve Driers 3 × 50% (100% installed). | `DBM-Deepcut/4-25_Deepcut_DBM.md` spares table (line ~2362–2364) |
| Regeneration Heat Supply | Mole sieve regeneration gas heating is removed from the unified heat medium loop and is served by a separate direct-fired heater. | `DBM-Deepcut/4-25_Deepcut_DBM.md` heat medium narrative (line ~1947) |
| Moisture Analysis | Two moisture analyzers for the process gas molecular sieve; dry-gas analyzer manifolded from the common line and from each of three driers. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~2134) |
| Package Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). | `PACKAGE_REGISTER.csv` PKG-069 ResponsibilityModel |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Final dehydration of sour/wet process gas upstream of cryogenic recovery; downstream of TEG dehydration. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1243) |
| Operating regime | Continuous adsorption with cyclic regeneration (two beds adsorbing while one is in standby/regeneration/cooling). | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1243, ~1263) |
| Design pressures / temperatures | TBD (not in locally accessible source slices for the gas mole-sieve drier vessels; resides in `26020-Package_Requirements.docx` package heading for row 73 and detailed DBM clauses — location TBD). | `PACKAGE_REGISTER.csv` SourceRefRaw |
| Sizing / Capacity | TBD; bed sizing, cycle time, and regeneration heater duty not in locally accessible source slices. | location TBD |
| Materials of construction | TBD | location TBD |
| Isolation basis | Multiple parallel packages are generally isolated on a unit basis so an entire unit can be removed from service for maintenance while remaining units continue to operate (applies to mole sieve inlet coalescer/filter service among other examples). | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~2408) |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | Mechanical equipment package supplied by Package Vendor; integrated into facility by EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Applicable interface types (package boundary integration) | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-069 rows (IFC-8863228D03, IFC-DB1A71F6DF, IFC-9479DAC2A5, IFC-1D3E18B0BE, IFC-BA6F4E6AB5, IFC-8AEB17AA5C, IFC-F72C2E190F, IFC-14518427AC, IFC-DA19470A67, IFC-C2918ADF74, IFC-0F979B5E62, IFC-0B1DEDEC2D); `PACKAGE_REGISTER.csv` InterfaceTypes |
| Regeneration interfaces (external utilities) | Tie-in to separate direct-fired regeneration gas heater (heat medium loop is NOT a regeneration source for the gas mole sieve). | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1947) |
| Downstream connection | Dried gas to molecular-sieve dust filtration → mercury recovery unit → MRU dust filter → UltraTEF cryogenic unit. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1243) |
| Heat tracing / insulation | TBD at package level; outdoor piping/header heat-tracing requirements for the gas mole sieve are not in locally accessible source slices. | location TBD |

## Scope Items Covered

| Scope Item | Statement |
|---|---|
| `SOW-0144` | Carry the workbook-defined vendor-responsible Mechanical package 'Mole Sieve Drier Unit (Gas)' as a distinct flat project package for WBS 01; the Package Vendor owns engineering/design/equipment and the EPC Integrator owns facility integration. |

Source: `SCOPE_LEDGER.csv` SOW-0144 (impacted deliverables: DEL-069-01 through DEL-069-06).

## Objectives Supported

| Objective | Source |
|---|---|
| `OBJ-001` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-003` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-004` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-005` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-006` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-007` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-008` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-009` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| `OBJ-010` | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |

Objective association mode: `PACKAGE_HEURISTIC` per brief; `_CONTEXT.md` lists these objectives explicitly for this deliverable, so the association is explicit at the deliverable-ID level rather than heuristic-only.

## Gate-6 Disposition Note

`PACKAGE_REGISTER.csv` includes the Gate 6 disposition: "Gas Mole Sieve scope is included with the Cryogenic Unit package scope; NGL Mole Sieve remains a distinct package." This deliverable carries `PKG-069` as a discrete workbook package per Workbook row 73; downstream integration with the cryogenic unit package is an EPC-Integrator integration concern and is flagged in the Guidance Conflict Table as `CONF-069-01-01`. Source: `PACKAGE_REGISTER.csv` PKG-069 NotesRaw.

## References

- `_CONTEXT.md`; `_REFERENCES.md`; `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 snapshot: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Source basis (per `PACKAGE_REGISTER.csv` SourceRefRaw): Workbook Packages row 73; `26020-Package_Requirements.docx` package row 73 heading; `DBM-Deepcut/4-25_Deepcut_DBM.md` (mole sieve narrative ~line 1243, equipment inventory row 56 ~line 2607, sparing table ~line 2362, regeneration heat narrative ~line 1947, moisture analyzer narrative ~line 2134, isolation philosophy ~line 2408). Deliverable-specific source slices were NOT copied into the deliverable folder during PREPARATION; clause-level extraction beyond the cited DBM slices is marked `location TBD` above.
