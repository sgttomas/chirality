# Specification — DEL-078-01 Scope of Work (PKG-078 Pig Receivers (Inlet) 4-25)

> Normative scope-of-work specification for the EPC Integrator anchor deliverable of `PKG-078`. Requirements derive from accessible decomposition source slices (`SCOPE_LEDGER.csv` rows SOW-0161–0164 and `PACKAGE_REGISTER.csv` row PKG-078 in the GATE-07 snapshot), which are themselves extracted from `26020-Package_Requirements.docx` package heading 31 and Workbook Packages row 78.

## Scope

### In Scope (this Scope-of-Work deliverable)

The Scope of Work documents the full EPC-integrator-owned scope for `PKG-078` — Pig Receivers (Inlet) 4-25 — and serves as the package anchor for downstream deliverables (`DEL-078-02` … `DEL-078-06`). It MUST include:

- The tagged equipment and package identity for the three (3) 610 mm (24") OD pig receivers `PR-1010-1`, `PR-1020-1`, `PR-1030-1` with associated HIPPS packages, ESDVs, and skid-mounted isolation. (Source: `SCOPE_LEDGER.csv` SOW-0162, SOW-0163.)
- Package function statement: pig receivers receive plant inlet pipeline gas at the facility boundary and pass it to the inlet separators. (Source: `PACKAGE_REGISTER.csv` PKG-078; `SCOPE_LEDGER.csv` SOW-0162.)
- Source basis: Workbook Packages row 78; `26020-Package_Requirements.docx` package heading 31. (Source: `PACKAGE_REGISTER.csv` PKG-078.)
- Boundaries, By-Others items, and applicable interface types. (Source: `SCOPE_LEDGER.csv` SOW-0164; `PACKAGE_REGISTER.csv` PKG-078.)
- Whole-facility integration narrative connecting `PKG-078` to upstream pipeline and downstream inlet separators (the comparable 04-25 separator package is `PKG-082` — TBD: verify exact 04-25 separator package ID; the only Inlet Separators row examined in this pass was `PKG-083` (3-25)). (Source: `PACKAGE_REGISTER.csv` PKG-078 process-function text; package-ID for 04-25 separators is `ASSUMPTION` pending direct check of the register row.)
- Responsibility assignment record stating Package Vendor vs EPC Integrator split. (Source: `PACKAGE_REGISTER.csv` PKG-078 ResponsibilityModel.)

### Out of Scope (excluded from this package, called out by source)

- Interconnecting piping outside the skid boundary.
- DCS integration.
- Foundations.
- Electrical supply to MCC.

(Source: `SCOPE_LEDGER.csv` SOW-0164 "By others".)

`SCOPE_LEDGER.csv` SOW-0161 confirms `PKG-078` is carried as a distinct flat project package for WBS 01; the Package Vendor owns engineering/design/equipment and the EPC Integrator owns facility integration.

## Requirements

### R-1 — Package Identity and Carriage

R-1.1 The Scope of Work MUST identify `PKG-078` as a workbook-defined vendor-responsible Mechanical package carried as a distinct flat project package for WBS 01. (Source: SOW-0161.)
R-1.2 The Scope of Work MUST state the package tracking number `26020-01-35-001`. (Source: `PACKAGE_REGISTER.csv` PKG-078.)

### R-2 — Equipment and Tagging

R-2.1 The Scope of Work MUST list three (3) identical 610 mm (24") OD pig receiver assemblies on dedicated structural steel non-enclosed skids, tagged `PR-1010-1`, `PR-1020-1`, `PR-1030-1`. (Source: SOW-0162, SOW-0163.)
R-2.2 Each skid MUST include skid-mounted isolation or an ESDV. (Source: SOW-0163.)

### R-3 — HIPPS

R-3.1 Each receiver skid MUST include a HIPPS package with ESDV(s) upstream of the pig receiver. (Source: SOW-0163.)
R-3.2 The HIPPS package MUST include a pressure control valve and an outlet pressure transmitter operated via PID control to maintain inlet-separator vessel operating pressure below the applicable limit. (Source: SOW-0163. **TBD:** the applicable numerical setpoint is not given in the extracted source slice.)
R-3.3 The HIPPS package MUST include a shutdown valve using pneumatic hi-low shutoff, with an additional shutdown valve and pneumatic hi-low for redundancy, to close the high-pressure inlet. (Source: SOW-0163.)

### R-4 — Sour Service and Purge

R-4.1 The package MUST be designed for sour service at 1.0 mol% H2S design composition. (Source: SOW-0163.)
R-4.2 A sweet-gas purge downstream of the manual isolation valve MUST be provided for sour-gas purge of the receiver barrel prior to opening for pig retrieval. (Source: SOW-0163.)

### R-5 — Relief / Venting

R-5.1 The pig receivers MUST be vented to the HP flare system. (Source: SOW-0163.)

### R-6 — Process / Operating Envelope

R-6.1 Design throughput: 225 MMSCFD. (Source: SOW-0164.)
R-6.2 Operating pressure: 653–725 psig; MAOP 1300 psig. (Source: SOW-0164.)
R-6.3 Design pressure: low 653 psig / normal high 725 psig; MAWP 1440 psig. (Source: SOW-0164.)
R-6.4 Ambient temperature design range: −40 °C to +35 °C; historical ambient −19 °C to 22.2 °C. (Source: SOW-0164.)
R-6.5 Normal flowrate per receiver: `TBC` per source. (Source: SOW-0164.)

### R-7 — Boundaries and By-Others

R-7.1 The Scope of Work MUST state the following items are by others and excluded from this package: interconnecting piping; DCS integration; foundations; electrical supply to MCC. (Source: SOW-0164.)

### R-8 — Interface Coverage

R-8.1 The Scope of Work MUST acknowledge the applicable interface types for `PKG-078`: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Pipeline / Pigging. (Source: `PACKAGE_REGISTER.csv` PKG-078.)

### R-9 — Responsibility Assignment

R-9.1 The Scope of Work MUST state: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: `PACKAGE_REGISTER.csv` PKG-078; `OBJ-004`.)

### R-10 — Objective Traceability

R-10.1 The Scope of Work MUST trace to objectives `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. (Source: `DELIVERABLE_REGISTER.csv` DEL-078-01; `OBJECTIVE_REGISTER.csv`.)

## Standards

The following are cited by upstream sources and govern the deliverable; specific clause-level requirements are `location TBD` because the extracted source slice does not include clause text:

- `26020-Package_Requirements.docx` package heading 31 — package requirements (authoritative source, not re-read locally in this pass; cited via `PACKAGE_REGISTER.csv` PKG-078 SourceBasis).
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — Design Basis Memorandum for the 04-25 Deepcut facility (cited via `PACKAGE_REGISTER.csv` PKG-078 SourceBasis; `OBJ-001`).
- `Bid Docs/Budgetary/26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` — Word source basis (cited via `PACKAGE_REGISTER.csv` PKG-078 SourceBasis).
- Sour-service codes/standards (ASSUMPTION: NACE/ISO sour-service practice likely applicable given 1.0 mol% H2S sour-service basis; **location TBD** — not stated in extracted source slice).
- HP flare / relief codes (ASSUMPTION: API 521 / API 520 likely applicable given HP flare vent routing; **location TBD**).

## Verification

| Requirement | Verification Approach | Evidence | Source |
|---|---|---|---|
| R-1 | Document review of `DEL-078-01` against `PACKAGE_REGISTER.csv` PKG-078 and `SCOPE_LEDGER.csv` SOW-0161 | Cross-reference in `_REFERENCES.md`; register row match | This Spec; register |
| R-2 | Tagged-equipment-list review against `SOW-0162`, `SOW-0163` | Equipment list section in Scope of Work narrative | SOW-0163 |
| R-3 | HIPPS-architecture review against `SOW-0163`; vendor HIPPS package datasheet review at `DEL-078-04` | HIPPS narrative + interface to `DEL-078-02 Package Datasheet` | SOW-0163 |
| R-4 | Sour-service design-review against `SOW-0163`; materials selection record at `DEL-078-04` | Sour-service statement in SoW + vendor materials selection | SOW-0163 |
| R-5 | Relief-routing review against P&ID/relief schedule (downstream evidence) | Vent-to-HP-flare line item; relief-system integration record | SOW-0163 |
| R-6 | Design envelope cross-check against `SOW-0164` and `DEL-078-02 Package Datasheet` | Datasheet pressure/temperature/throughput rows | SOW-0164 |
| R-7 | Boundary review against `SOW-0164` "By others" | Boundary list in SoW; interface register entries | SOW-0164 |
| R-8 | Interface-register reconciliation against `PACKAGE_REGISTER.csv` PKG-078 InterfaceTypes | Interface matrix in SoW | PKG-078 |
| R-9 | Responsibility-model review against `PACKAGE_REGISTER.csv` PKG-078 ResponsibilityModel and `OBJ-004` | Responsibility section in SoW | PKG-078; OBJ-004 |
| R-10 | Objective traceability matrix against `DELIVERABLE_REGISTER.csv` DEL-078-01 ObjectiveMap | Objective trace table in SoW | DELIVERABLE_REGISTER.csv |

## Documentation

The Scope of Work itself produces, at minimum, the following anticipated artifacts (from `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` DEL-078-01):

- Package scope of work narrative
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

Downstream deliverables anchored by this SoW (informational; not produced here):

- `DEL-078-02` Package Datasheet
- `DEL-078-03` Construction Work Package
- `DEL-078-04` Vendor Engineered Equipment Package
- `DEL-078-05` Vendor Document Turnover Package
- `DEL-078-06` EPC Vendor Package Review and Acceptance
