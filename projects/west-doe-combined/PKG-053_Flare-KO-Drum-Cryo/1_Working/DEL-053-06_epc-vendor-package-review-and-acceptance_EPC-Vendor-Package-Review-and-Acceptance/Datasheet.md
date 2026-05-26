# Datasheet — DEL-053-06: EPC Vendor Package Review and Acceptance (Flare KO Drum (Cryo))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-053-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| Parent Package ID | `PKG-053` | `_CONTEXT.md` |
| Parent Workbook Row | 53 | `_CONTEXT.md` |
| Package Name | Flare KO Drum (Cryo) | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Covered Scope Items | SOW-0067, SOW-0068, SOW-0069, SOW-0070 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supported Objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION: package-heuristic association) |

## Attributes

### Package Under Review

| Attribute | Value | Source |
|---|---|---|
| Package Function | Supply the cryogenic flare knock-out drum and associated electric immersion heater as a single equipment package. | `PACKAGE_REGISTER.csv` row PKG-053; `SCOPE_LEDGER.csv` SOW-0068 |
| Major Included Equipment | Cryogenic flare KO drum V-4110-1; electric immersion heater H-4112-1 | `SCOPE_LEDGER.csv` SOW-0069; `4-25_Deepcut_DBM.md` §Flare Equipment and Routing; §Equipment Schedule row 11 |
| Service Class | Cryogenic; receives PSV reliefs from cryogenic unit and molecular-sieve-dehydrated systems relieving below -45.5 degC; treated as non-sour in the brief | `SCOPE_LEDGER.csv` SOW-0070; `4-25_Deepcut_DBM.md` §Flare Equipment and Routing |
| Package Tag (Workbook) | 26020-01-PT-17-001 — Flare KO Drum (Cryo) | `PACKAGE_REGISTER.csv` PKG-053 |
| WBS | 01 | `PACKAGE_REGISTER.csv` PKG-053 |

### Acceptance Review Subject Matter

| Attribute | Value | Source |
|---|---|---|
| EPC Acceptance Scope | Vendor package review, integration acceptance, and handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-053-06 |
| Anticipated Artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` |
| Upstream Source-of-Truth Deliverables (within PKG-053) | DEL-053-01 (Scope of Work); DEL-053-02 (Package Datasheet); DEL-053-03 (Construction Work Package); DEL-053-04 (Vendor Engineered Equipment Package); DEL-053-05 (Vendor Document Turnover Package) | `DELIVERABLE_REGISTER.csv` PKG-053 rows |

## Conditions

| Attribute | Value | Source |
|---|---|---|
| Inlet/Service Conditions for V-4110-1 | TBD — vendor datasheet values to be confirmed against EPC Package Datasheet (DEL-053-02); design temperature minimum bounded by relief sources below -45.5 degC | `4-25_Deepcut_DBM.md` §Flare Equipment and Routing; vessel-specific values not available in accessible sources |
| Relief Header Connection | 610 mm (24 in) cryogenic relief header upstream of V-4110-1; cryogenic flare header combines with HP flare downstream of both KO drums before the common HP/cryo stack | `4-25_Deepcut_DBM.md` §Flare Equipment and Routing |
| Built-up Backpressure (design basis) | Estimated 695 kPag (100 psig) HP/cryo built-up backpressure during peak blowdown coincident with highest fire-zone load; PSV maximum total backpressure target < 1172 kPag (170 psig) under 150# flange rating; actual values to be verified during detailed engineering | `4-25_Deepcut_DBM.md` §Flare Radiation Criteria preface |
| Sour Service Classification | Non-sour (per brief) | `SCOPE_LEDGER.csv` SOW-0070 |
| Heat Tracing Requirement on Header | Cryogenic flare headers outside buildings are NOT heat traced (water not expected in this system) | `4-25_Deepcut_DBM.md` §Flare Equipment and Routing |
| Immersion Heater Service | Provides vaporization/maintenance heat for liquid collected in the cryogenic KO drum; specific kW rating and control basis | TBD — not present in accessible source slices |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Package Vendor Construction Scope | Engineering, design, fabrication/supply, and the physical equipment package developed from the EPC package Scope of Work and Package Datasheet | `DELIVERABLE_REGISTER.csv` DEL-053-04 |
| EPC Construction Scope | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` PKG-053 |
| Applicable Interface Types (facility-level) | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` PKG-053 |
| Inspection / Test Evidence Required | TBD — to be enumerated from EPC Package Datasheet (DEL-053-02) inspection/test plan and vendor ITP |
| Turnover Records Required | TBD — to be enumerated from Construction Work Package (DEL-053-03) turnover checklist and Vendor Document Turnover Package (DEL-053-05) |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row PKG-053
  - `DELIVERABLE_REGISTER.csv` row DEL-053-06 and sibling DEL-053-0x rows
  - `SCOPE_LEDGER.csv` rows SOW-0067, SOW-0068, SOW-0069, SOW-0070
  - `OBJECTIVE_SCOPE_MAP.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv` (objective association: PACKAGE_HEURISTIC, recorded as ASSUMPTION)
- Source documents (mediated via decomposition extracts):
  - `_Sources/26020-Package_Requirements.docx` package heading 8 — location TBD (binary; not locally accessible as text)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Flare Equipment and Routing; §Equipment Schedule row 11; §Flare Radiation Criteria preface
- Workbook Packages row 53 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) — location TBD (binary; not locally accessible as text)
