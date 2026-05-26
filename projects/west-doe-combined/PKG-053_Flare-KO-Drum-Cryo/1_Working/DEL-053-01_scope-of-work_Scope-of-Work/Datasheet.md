# Datasheet: DEL-053-01_scope-of-work — Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-053-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-053 — Flare KO Drum (Cryo) |
| Workbook basis | Workbook Packages row 53 |
| WBS | 01 |
| CoA tracking number | 26020-01-17-001 |
| Discipline | Mechanical |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Scope items covered | SOW-0067; SOW-0068; SOW-0069; SOW-0070 |
| Supported objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package role | Workbook-defined Mechanical package carried as a distinct flat project package for WBS 01 | `SCOPE_LEDGER.csv`, SOW-0067 |
| Basic scope | Supply the cryogenic flare knock-out drum and associated electric immersion heater as a single equipment package | `SCOPE_LEDGER.csv`, SOW-0068; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| Major included equipment | Cryogenic flare KO drum V-4110-1 and electric immersion heater H-4112-1 | `SCOPE_LEDGER.csv`, SOW-0069; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems; Tagged Equipment table row 11 |
| Service description | Drum serves cryogenic-unit reliefs and molecular-sieve-dehydrated systems relieving below -45.5 deg C; service treated as non-sour in the brief | `SCOPE_LEDGER.csv`, SOW-0070; `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv`, PKG-053; `INTERFACE_REGISTER.csv`, PKG-053 |
| Responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | `PACKAGE_REGISTER.csv`, PKG-053 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv`, PKG-053 |
| Facility | West Doe Deepcut expansion at facility 04-25 | `4-25_Deepcut_DBM.md`, SEC-01 |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Flare system role | Equipment in cryogenic service and systems containing molecular-sieve-dehydrated gas with PSVs relieving below -45.5 deg C connect to the cryogenic flare system | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| Cryogenic relief header | 610 mm (24 in) relief header feeding cryogenic flare KO drum V-4110-1 | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| KO drum heater | Cryogenic flare KO drum includes electric immersion heater H-4112-1 | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems; Tagged Equipment table |
| Header combining | Cryogenic flare header combines with HP flare downstream of both KO drums before the common HP/cryo stack | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| Header material and sizing | 304SS, 610 mm cryogenic flare header; length 140 m / 5 m (TBC at detailed design) | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems materials table |
| Heat tracing basis | Cryogenic flare headers outside buildings are not heat traced because water is not expected in this system | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| Drain segregation | Cryogenic flare header is a segregated drain header with minimum 300# ANSI design-pressure basis; streams have passed through molecular sieve dehydration and contain less than 0.1 ppm H2O | `4-25_Deepcut_DBM.md`, SEC-09 Drains; Cryogenic drain row |
| Drain insulation | Personnel protection insulation only; not insulated in pipe rack or inaccessible areas | `4-25_Deepcut_DBM.md`, SEC-09 Drains; Cryogenic drain row |
| Service sour basis | Non-sour service per brief (to be re-confirmed in source basis review) | `SCOPE_LEDGER.csv`, SOW-0070 |
| Spacing - flare tanks/KO drums to fire hazards | 10 m (32 ft) to vegetation or other fire hazards | `4-25_Deepcut_DBM.md`, SEC-02 Flare and Incinerator Spacing; OGAOM Sec. 9.6.15 |
| Common HP/cryo stack | Common HP/cryo flare stack physically located at 03-25 and shared with 04-25; 660 mm (26 in) OD x 200 ft tall (TBC), sonic tip, pilot, pilot proving, auto ignition, smokeless design basis | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |
| Relief volumes | TBD; preliminary Aspen Flare System Analyzer models support current header sizing; to be confirmed at detailed engineering | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems |

## Construction

| Item | Value |
|---|---|
| Scope-of-work deliverable contents | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record |
| Boundaries to define | Cryogenic relief header tie-in upstream of V-4110-1; downstream tie-in where cryogenic header combines with HP flare; immersion heater electrical and EHT tie-ins; instrumentation and controls tie-ins; drain header tie-in; structural/foundation footprint; maintenance access |
| Tagged equipment | V-4110-1 (cryogenic flare KO drum); H-4112-1 (electric immersion heater) |
| Design values for drum dimensions, retention, MAWP, MDMT, material grades, nozzle schedule, heater rating, control philosophy, foundation loads, and tie-in coordinates | TBD; not stated at the deliverable level in accessible source slices and will be set by Package Datasheet (DEL-053-02) and detailed engineering |
| Required verification interfaces | Cryogenic flare relief volume study; flare KO drum sizing; immersion heater duty and electrical design; drain header sizing and segregation; structural and spacing checks; HP/cryo stack backpressure model |

## References

- `_CONTEXT.md`, DEL-053-01_scope-of-work.
- `_REFERENCES.md`, DEL-053-01_scope-of-work.
- `_DEPENDENCIES.md`, DEL-053-01_scope-of-work.
- `PACKAGE_REGISTER.csv`, PKG-053.
- `DELIVERABLE_REGISTER.csv`, DEL-053-01_scope-of-work.
- `SCOPE_LEDGER.csv`, SOW-0067; SOW-0068; SOW-0069; SOW-0070.
- `INTERFACE_REGISTER.csv`, PKG-053.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-053-01_scope-of-work.
- `ARTIFACT_REGISTER.csv`, DEL-053-01_scope-of-work rows.
- `26020-Package_Requirements.docx`, package heading 8 (Flare KO Drum (Cryo)).
- `4-25_Deepcut_DBM.md`, SEC-01, SEC-02, SEC-09.
