# Guidance: DEL-033-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-033` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)" because that is the workbook and Gate 7 register spelling.
- Treat the twelve workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned package engineering (switchgear and prefabricated electrical building) with the Package Vendor and facility-level integration (tie-ins, plot location, civil/structural and process interfaces) with the EPC Integrator.
- Use `TBD` for switchgear ratings, breaker complement, protection scheme, bus configuration, single-line details, dimensions, and building plot-plan location until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: medium-voltage service voltage, electrical-building configuration, grounding/bonding, raceway, HVAC, area classification, and standby power interface.

## Considerations

The DBM electrical design basis supports a facility-wide distribution architecture in which 13.8 kV main switchgear feeds step-down transformers that distribute power radially to several electrical buildings, including a 4.16 kV building serving acid gas / overheads compressors (830-1). The 830-2 designation associated with PKG-033 is not explicitly enumerated in the DBM building list (lines 2811-2816), which presents an ambiguity that must be resolved by human ruling (see Conflict Table).

The DBM "Electrical Buildings" section supports the building configuration for any 4.16 kV switchgear electrical building: prefabricated modular, climate-controlled with n+1 HVAC, elevated on piles, bottom cable entry, TECK/ACIC cabling, EMT conduit between adjacent panels, and door/transom sizing for the largest equipment. These items can be carried as requirements for 830-2 without overstating.

The DBM equipment list identifies "Medium Voltage Switchgear" quantity 1 for the deep-cut scope (line 2880). Whether PKG-033 (830-2) is that single MV switchgear, a second/duplicate unit, or a building unrelated to the deep-cut tally cannot be determined from the accessible source slices and is left `TBD`.

Grounding, bonding, raceway, and maintenance-access requirements are well-supported by DBM source slices and can be applied at the level the source states (two-point grounding for major equipment, ground wells at electrical buildings, compression connections, shop-installed main tray, maintenance-preserving routing).

Area classification is supported: the building shall be located in a general purpose area for convenient power distribution.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Switchgear ratings (continuous, SC, BIL) | Mark `TBD` pending project electrical specifications and short-circuit/protection studies. | DBM does not provide package-specific MV switchgear ratings. |
| "830-2" building tag | Treat as workbook-defined identifier; flag as HRR; do not invent a process service. | DBM enumerates 830-1 (4.16 kV Acid Gas / Overheads Compressor Electrical Building) but not 830-2. |
| Switchgear quantity | Mark `TBD`. | DBM electrical equipment list shows MV switchgear quantity 1 for the deep-cut scope; allocation to PKG-033 not confirmed. |
| Plot location | Identify as general purpose area only; specific location `TBD`. | DBM gives area-classification guidance, not plot coordinates. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations `TBD`; treat MV switchgear product standards as `ASSUMPTION`. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 35 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Switchgear short-circuit withstand: TBD. No package-specific source slice available."
- Not acceptable without new source: "PKG-033 (830-2) serves the acid gas/overheads compressor train as a redundant 4.16 kV bus." The accessible source set does not establish this allocation; only 830-1 is enumerated for that service.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-033-02-001 | The workbook package name uses building tag "830-2", but the DBM electrical-buildings list enumerates 810-1, 820-1, 830-1, 840-1, 850-1, 860-1 without "830-2". The process service of 830-2 is therefore not source-confirmed. | Workbook Packages row 35; `PACKAGE_REGISTER.csv` row `PKG-033` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building list (lines 2811-2816) | Datasheet Identification/Attributes; Specification REQ-033-02-011; Procedure Steps | Carry "830-2" as the workbook-defined identifier; do not assign a specific process service in the datasheet; treat building as a 4.16 kV switchgear electrical building per the workbook name until human ruling resolves the tag. | TBD |
| HRR-033-02-002 | The DBM electrical equipment list identifies "Medium Voltage Switchgear" quantity 1 for the deep-cut scope, but allocation to PKG-033 (830-2) is not confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical equipment list (line 2880) | Workbook Packages row 35; Gate 7 `PACKAGE_REGISTER.csv` | Datasheet Attributes; Specification Requirements | Do not assign MV switchgear quantity to PKG-033; record switchgear count/rating as `TBD` pending confirmation. | TBD |
| HRR-033-02-003 | No package-specific requirements slice for PKG-033 (830-2) was located in `26020-Package_Requirements.docx` during this run. | `_REFERENCES.md`, missing/deferred references list | `_Sources/26020-Package_Requirements.docx` | Datasheet Construction; Specification Requirements; Procedure Steps | Re-run package-requirements search after sources are decomposed at package granularity; until then, vendor-facing detailed switchgear and building parameters remain `TBD`. | TBD |
