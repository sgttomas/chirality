# Specification: DEL-048-02 — PKG-048 Inlet / Sales Compressors Package Datasheet

## Scope

This specification governs the production and content of the **PKG-048 Inlet / Sales Compressors Package Datasheet** — the mandatory EPC Integrator technical handoff document containing the package data required for third-party vendor or discipline package engineering and design (per `_CONTEXT.md`).

**In scope:**
- Identification, attribute, condition, and construction fields for the five (5) parallel multi-service inlet/sales reciprocating compressor packages (DBM-Deepcut SEC-05).
- Package interface requirements matrix (interface types from PACKAGE_REGISTER.csv row PKG-048).
- Source-supported equipment and design criteria traceable to DBM-Deepcut SEC-05 and PACKAGE_REGISTER.csv.
- Vendor engineering handoff basis.

**Out of scope:**
- Detailed mechanical design of vendor-supplied internals (cylinders, valves, rod packing, pulsation bottles, clearance pockets).
- Electrical detailed design beyond start-method, motor ratings, and MCC interface (deferred to electrical detailed-design deliverables).
- Process simulation, hydraulic, and pulsation studies (vendor and EPC detailed design).
- Sales Gas Booster Compressor (PKG-049) — separately decomposed package.
- Acid Gas Injection Compressors — separately decomposed packages.
- Construction work package content (DEL-048-03), vendor-engineered-equipment package content (DEL-048-04), vendor-document-turnover (DEL-048-05), and EPC vendor package review and acceptance (DEL-048-06) — separate sibling deliverables in PKG-048.

## Requirements

### R1 — Source-grounded identification
The datasheet MUST populate Identification fields from `_CONTEXT.md` and the PROJECT_DECOMP `PACKAGE_REGISTER.csv` row PKG-048.
Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-048.

### R2 — Five-package, parallel multi-service architecture
The datasheet MUST record five (5) identical parallel multi-service reciprocating compressor packages with a 5 x 20 percent capacity philosophy and no installed spare. The multi-service basis (one inlet stage + two sales stages on a common frame) MUST be stated.
Source: DBM-Deepcut SEC-05 "Compression Configuration"; "Inlet / Sales Compressor Basis"; PACKAGE_REGISTER.csv row PKG-048.

### R3 — Inlet-service capacity
Per-package inlet-service capacity SHALL be recorded as 62.4 MMSCFD (current supported basis); facility inlet-service total SHALL be recorded as approximately 312 MMSCFD. The detailed-table 60 MMSCFD / 300 MMSCFD alternates SHALL be carried as TBC.
Source: DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions"; "Open Items / TBC Items".

### R4 — Sales-service capacity
Per-package sales-service capacity SHALL be recorded as 57.6 MMSCFD; facility sales-service total SHALL be recorded as 288 MMSCFD (TBC).
Source: DBM-Deepcut SEC-05.

### R5 — Compressor frame and arrangement
The datasheet SHALL record compressor frame as Ariel KBC/6 (TBC), three-stage multi-service separable reciprocating (1 inlet stage + 2 sales stages on a common frame). The legacy conflicting frame reference SHALL be carried as a TBD pending human ruling.
Source: DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis"; "Open Items / TBC Items".

### R6 — Inlet-service operating envelope
The datasheet SHALL carry inlet-service suction 4,309 kPag (625 psig) upstream / 385 psig at compressor-cylinder inlet, discharge 7,791 kPag (1,130 psig) service basis (detailed table 1,135 psig normal/design), inlet temperatures 27.3 deg C winter / 35.7 deg C summer, J-T mode TBD, minimum MAWP basis 9,032 kPag.
Source: DBM-Deepcut SEC-05 "Inlet / Sales Compressor Design Conditions".

### R7 — Sales-service operating envelope
The datasheet SHALL carry sales-service first-stage suction 440 psig (430 psig normal in detailed table), discharge 10,343 kPag (1,500 psig) current supported basis with 1,700 psig detailed-table alternate as TBC, first-stage suction temperature 43.3 deg C, second-stage suction temperature 71.1 deg C, J-T mode TBD, minimum MAWP basis 9,032 kPag (lower stages) and 13,100 kPag (third-stage discharge).
Source: DBM-Deepcut SEC-05.

### R8 — Air-cooler basis
The datasheet SHALL specify a common air-cooler frame per package with one process bundle per stage, automated pneumatic louver control, and the winter/summer cooler outlet and simulated dP basis verbatim from DBM-Deepcut SEC-05.
Source: DBM-Deepcut SEC-05.

### R9 — Scrubber sizing basis
Suction scrubbers SHALL be two-phase; sales-service scrubber necessity SHALL be marked "evaluate during detailed engineering". Inlet liquid SG 0.61, K-factor not more than 0.5 Imperial, horizontal or vertical vane-style demisters acceptable.
Source: DBM-Deepcut SEC-05.

### R10 — Control-valve fail actions
The datasheet SHALL record: inlet-service suction PCV ET-type, fails closed, 5 psid; sales-service suction PCV absent (regulated upstream by J-T valve/expander); inlet-service blowdown fails OPEN; sales-service blowdown fails CLOSED; inlet-service recycle fail-open (TBD); sales-service recycle fail-closed (TBD).
Source: DBM-Deepcut SEC-05.

### R11 — Electric driver basis
Each package SHALL be specified with a 6,700 hp three-phase electric induction motor (current basis; 7,000 hp legacy value remains TBD). Start method SHALL be starting VFD with synchronous transfer to a normal-service bus. The PACKAGE_REGISTER.csv "DOL with soft-start" wording SHALL be flagged as superseded by the DBM under Authority Hierarchy item 1; NEMA MG1 compliance applies by ASSUMPTION pending heading 3 reconfirmation.
Source: DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis"; PACKAGE_REGISTER.csv row PKG-048.

### R12 — Auxiliary systems
The datasheet SHALL record: electric circulating lube-oil heater; manual sweet-gas purge from fuel gas for sour-inlet maintenance; common seal pot for packing drains/vents with vapour to VRU and liquids to local truck-out; distance-piece sweep purge on sweet-service cylinders.
Source: DBM-Deepcut SEC-05.

### R13 — Start basis
The datasheet SHALL record start-from-equalization-pressure capability in both services; if equalization > MAWP, alternate depressuring back into respective inlet headers SHALL be noted.
Source: DBM-Deepcut SEC-05.

### R14 — Interface matrix
The datasheet SHALL list applicable interface types verbatim from PACKAGE_REGISTER.csv row PKG-048 and SHOULD anchor each to a source-cited counterpart system where DBM evidence exists.
Source: PACKAGE_REGISTER.csv row PKG-048; DBM-Deepcut SEC-05/SEC-08.

### R15 — Sour-service material/code basis
Sour-service inlet wetted parts SHALL be flagged for NACE/MR-class requirements. Specific material clauses SHALL be cited from `26020-Package_Requirements.docx` heading 3 when accessible; otherwise the datasheet MUST mark "location TBD" rather than invent values.
Source: DBM-Deepcut SEC-05 (composition); `26020-Package_Requirements.docx` heading 3 (location TBD — ASSUMPTION).

### R16 — Provenance discipline
Every non-trivial value in the datasheet MUST cite source path and section reference. Inferences MUST be labelled ASSUMPTION; unknowns MUST be `TBD` or `location TBD`. No invention.
Source: `skills/four-documents/SKILL.md`; `docs/CONTRACT.md` K-PROV-1.

### R17 — Objective association
Supports-Objectives field MUST list OBJ-001 and OBJ-003 through OBJ-010 as carried in `_CONTEXT.md` (package-grouped heuristic per brief `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`, ASSUMPTION) until a human ruling confirms strict deliverable-level mapping.
Source: `_CONTEXT.md`; PROJECT_DECOMP objective-deliverable map (mapping convention).

## Standards

| Standard / Code | Applicability | Location in source |
|---|---|---|
| NEMA MG1 | Inlet/sales compressor motors | DBM-Deepcut SEC-05 (general compression-motor basis) — ASSUMPTION applied; explicit re-statement `location TBD` in heading 3 |
| NACE/MR (sour service) | Inlet-service compressor pressure-containing materials | location TBD (`26020-Package_Requirements.docx` heading 3 not locally accessible) — ASSUMPTION applicable |
| API 618 (reciprocating compressors for petroleum service) | Likely governing API standard for multi-stage separable reciprocating package | ASSUMPTION (not cited in accessible source); location TBD |
| Provincial/jurisdictional pressure equipment code (e.g., ABSA/CRN) | Package pressure-containing equipment | TBD — not stated in accessible source |
| CSA Z662 | Any tie-in pipeline scope in/out of package boundary | DBM-Deepcut SEC-04 (general pipeline basis) — APPLIES at interface; package-internal applicability `location TBD` |
| Local building / electrical / fire codes | Self-framing buildings, MCC interfaces, F&G | TBD — not stated in accessible source |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Cross-check Identification table against `_CONTEXT.md` and PACKAGE_REGISTER.csv row PKG-048. |
| R2 | Cross-check Attributes "Number of packages" and "Spare philosophy" against DBM-Deepcut SEC-05 Compression Configuration. |
| R3, R4 | Cross-check capacity rows against DBM-Deepcut SEC-05 Inlet/Sales Compressor Design Conditions; confirm TBC alternates carried. |
| R5 | Cross-check compressor type/model rows; confirm Ariel KBC/6 (TBC) flagged with Conflict Table row for legacy frame. |
| R6, R7 | Cross-check Conditions tables against DBM-Deepcut SEC-05 pressure/temperature tables; flag TBC labels. |
| R8 | Cross-check air-cooler basis table against DBM-Deepcut SEC-05. |
| R9 | Cross-check scrubber rows; confirm K-factor and SG. |
| R10 | Cross-check control-valve fail-action rows; confirm sales-service PCV is recorded as absent with upstream J-T basis. |
| R11 | Cross-check driver rows; confirm hp and start-method conflicts logged in Conflict Table; confirm DBM authority over register wording. |
| R12, R13 | Cross-check auxiliary-systems and start-basis rows against DBM-Deepcut SEC-05. |
| R14 | Confirm interface list matches PACKAGE_REGISTER.csv row PKG-048 verbatim; verify DBM-cited anchors. |
| R15 | Confirm sour-service flag present; confirm material clauses either cited from heading 3 or marked `location TBD`. |
| R16 | Audit every non-trivial cell for source citation; reject uncited values. |
| R17 | Confirm objective list matches `_CONTEXT.md` and that the mapping is labelled ASSUMPTION until human-confirmed. |

## Documentation

The following artifacts are produced under this deliverable:

- `Datasheet.md` — the package datasheet (primary artifact).
- `Specification.md` — this file (normative content rules).
- `Guidance.md` — directional notes, rationale, conflict table.
- `Procedure.md` — operational steps to produce/maintain the datasheet.
- `_run_records/TASK_RUN_*.md` — auditable run records.

Anticipated artifacts (from `_CONTEXT.md`, also satisfied by content of `Datasheet.md`):
- Package technical datasheet — covered by `Datasheet.md`.
- Vendor engineering handoff basis — covered by `Datasheet.md` Attributes + Construction + Interface anchors.
- Package interface requirements matrix — covered by `Datasheet.md` "Applicable Interface Types".
- Source-supported equipment and design criteria — covered by `Datasheet.md` with provenance.
