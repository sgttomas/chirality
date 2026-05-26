# Specification: DEL-080-02 — PKG-080 Inlet Compressors Package Datasheet

## Scope

This specification governs the production and content of the **PKG-080 Inlet Compressors Package Datasheet** — the mandatory EPC Integrator technical handoff document containing the package data required for third-party vendor or discipline package engineering and design (per `_CONTEXT.md`).

**In scope:**
- Identification, attribute, condition, and construction fields for the two parallel sour inlet gas reciprocating compressor packages (DBM SEC-05).
- Package interface requirements matrix (interface types from PACKAGE_REGISTER.csv row PKG-080).
- Source-supported equipment and design criteria traceable to the DBM and the package register.
- Vendor engineering handoff basis.

**Out of scope:**
- Detailed mechanical design of vendor-supplied internals (cylinders, valves, rod packing, pulsation bottles).
- Electrical detailed design beyond starter basis, motor ratings, and MCC interface (deferred to electrical detailed-design deliverables per DBM SEC-09).
- Process simulation, hydraulic, and pulsation studies (vendor and EPC detailed design).
- Construction work package content (DEL-080-03), vendor-engineered-equipment package content (DEL-080-04), vendor-document-turnover (DEL-080-05), and EPC vendor package review and acceptance (DEL-080-06) — these are separate sibling deliverables.

## Requirements

### R1 — Source-grounded identification
The datasheet MUST populate Identification fields from `_CONTEXT.md` and the PROJECT_DECOMP `PACKAGE_REGISTER.csv` row PKG-080.
Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-080.

### R2 — Two-package, parallel, no-spare architecture
The datasheet MUST record two identical parallel reciprocating compressor packages with a 2 x 50 percent capacity philosophy and no installed spare.
Source: DBM SEC-05 "Inlet Compression Overview"; PACKAGE_REGISTER.csv row PKG-080.

### R3 — Per-unit and total compression capacity
Per-package capacity SHALL be recorded as 40 MMSCFD; facility total compression basis SHALL be recorded as 80 MMSCFD.
Source: DBM SEC-05 Compressor Item table.

### R4 — Compressor type and arrangement
The datasheet SHALL record compressor type as two-stage separable reciprocating, with three first-stage and three second-stage cylinders, preliminary model Ariel KBC/6 (TBC).
Source: DBM SEC-05 Compressor Item table.

### R5 — Process operating envelope
The datasheet SHALL carry the pressure, temperature, and pressure-drop conditions in `Datasheet.md` "Conditions". Fixed values (e.g., 800 psig second-stage discharge under current supersession basis) MUST be marked as such; values labelled TBC in source MUST be carried as TBC.
Source: DBM SEC-05 "Compression Design Conditions" and "Scrubbers, Coolers, Recycle, and Purge".

### R6 — Electric driver basis
Each package SHALL be specified with a 4,000 V, three-phase, 60 Hz, 5,200 hp / 3,878 kW electric motor; NEMA MG1 compliant; TEFC or WPII; Class F insulation with Class B rise; approximately 891 rpm 8-pole; continuous inverter-duty; starting VFD per SCA-001 VE #34. Motor tags KM-2150 and KM-2250.
Source: DBM SEC-05 "Electric Driver and Starting Basis"; DBM SEC-09.

### R7 — Package mechanical equipment scope
The datasheet SHALL identify per-package suction scrubbers (cyclonic first-stage; mesh/vane second-stage; design liquid SG 0.68), aerial coolers (10 percent excess surface area; 43.3 deg C outlet each stage), dedicated recycle control valves, sweet-gas start-up purge from fuel-gas, and common-seal-pot packing drains/vents.
Source: DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge".

### R8 — Modularization and field installation
Packages SHALL be shop-assembled, disassembled into three pieces for transport, and field-installed in self-framing buildings.
Source: DBM SEC-05 Inlet Compression Overview.

### R9 — Interface matrix
The datasheet SHALL list applicable interface types verbatim from PACKAGE_REGISTER.csv row PKG-080 (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) and SHOULD anchor each to a source-cited counterpart system where DBM evidence exists.
Source: PACKAGE_REGISTER.csv row PKG-080; DBM SEC-05/SEC-08/SEC-09.

### R10 — Sour-service material/code basis
Sour service (approximately 0.296 mol% H2S) SHALL be flagged. Specific NACE/MR-class metallurgy clauses SHALL be cited from `26020-Package_Requirements.docx` package heading 33 when accessible; otherwise the datasheet MUST mark "location TBD" rather than invent values.
Source: DBM SEC-05 (composition); `26020-Package_Requirements.docx` heading 33 (location TBD — ASSUMPTION).

### R11 — Provenance discipline
Every non-trivial value in the datasheet MUST cite source path and section reference. Inferences MUST be labelled ASSUMPTION; unknowns MUST be `TBD` or `location TBD`. No invention.
Source: `skills/four-documents/SKILL.md`; `docs/CONTRACT.md` K-PROV-1.

### R12 — Objective association
Supports-objectives field MUST list OBJ-002 through OBJ-010 as carried in `_CONTEXT.md` (package-grouped heuristic, ASSUMPTION) until a human ruling confirms strict deliverable-level mapping.
Source: `_CONTEXT.md`; PROJECT_DECOMP objective-deliverable map (mapping convention).

## Standards

| Standard / Code | Applicability | Location in source |
|---|---|---|
| NEMA MG1 | Inlet compressor motors | DBM SEC-05 "Electric Driver and Starting Basis" |
| NACE/MR (sour service) | Compressor pressure-containing materials | location TBD (`26020-Package_Requirements.docx` heading 33 not locally accessible) — ASSUMPTION applicable |
| API 618 (reciprocating compressors for petroleum service) | Likely governing API standard for two-stage separable reciprocating package | ASSUMPTION (not cited in accessible source); location TBD |
| Provincial/jurisdictional pressure equipment code (e.g., ABSA/CRN) | Package pressure-containing equipment | TBD — not stated in accessible source |
| Local building / electrical / fire codes | Self-framing buildings, MCC, F&G | TBD — not stated in accessible source |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Cross-check Identification table against `_CONTEXT.md` and PACKAGE_REGISTER.csv row PKG-080. |
| R2, R3 | Cross-check Attributes table values against DBM SEC-05 Compressor Item table. |
| R4 | Cross-check Attributes against DBM SEC-05 (type, model, cylinder count). |
| R5 | Cross-check Conditions tables against DBM SEC-05 pressure/temperature tables; flag fixed-vs-TBC labels. |
| R6 | Cross-check driver attributes against DBM SEC-05 + SEC-09. |
| R7 | Cross-check Construction rows against DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge". |
| R8 | Cross-check Construction modularization rows against DBM SEC-05 Inlet Compression Overview. |
| R9 | Confirm interface list matches PACKAGE_REGISTER.csv row PKG-080 verbatim; verify DBM-cited anchors. |
| R10 | Confirm sour-service flag present; confirm material clauses either cited from heading 33 or marked `location TBD`. |
| R11 | Audit every non-trivial cell for source citation; reject uncited values. |
| R12 | Confirm objective list matches `_CONTEXT.md` and that the mapping is labelled ASSUMPTION until human-confirmed. |

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
