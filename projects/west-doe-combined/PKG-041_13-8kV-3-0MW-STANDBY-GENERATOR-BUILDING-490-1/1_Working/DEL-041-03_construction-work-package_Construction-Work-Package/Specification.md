# Specification — DEL-041-03 Construction Work Package

## Scope

### In scope

This deliverable is the EPC Integrator's Construction Work Package for PKG-041 (13.8 kV, 3.0 MW Standby Generator Building, 490-1). It defines how the package is physically installed, built, inspected, turned over, and tied into the larger facility systems (`_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv`).

The deliverable must produce, at minimum, the anticipated artifacts declared in `_CONTEXT.md`:

- Construction work package (anchor artifact ART-55CB0F50C6)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

### Out of scope

- Package engineering, package design, vendor documentation, and the physical equipment package itself — owned by the Package Vendor on DEL-041-04 / DEL-041-05 (GATE-07 `PACKAGE_REGISTER.csv` responsibility split).
- Vendor package review and acceptance — owned by DEL-041-06 (GATE-07 `DELIVERABLE_REGISTER.csv`).
- Authoring the Scope of Work (DEL-041-01) and Package Datasheet (DEL-041-02), although both are upstream inputs.
- Package-specific exclusions stated in source materials: none declared (GATE-07 `PACKAGE_REGISTER.csv` exclusions = TBD).

## Requirements

### REQ-CWP-01 — EPC Integrator authorship

The Construction Work Package SHALL be authored by the EPC Integrator (GATE-07 `DELIVERABLE_REGISTER.csv` responsible-party field; `PACKAGE_REGISTER.csv` responsibility narrative). Vendor inputs may be incorporated by reference.

### REQ-CWP-02 — Coverage of declared package interfaces

The work package SHALL plan, install, inspect, and turn over each of the twelve workbook-declared interface types on PKG-041 (GATE-07 `INTERFACE_REGISTER.csv`):

Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.

Interface fact evidence is carried on DEL-041-02 (Package Datasheet); the construction work package SHALL consume those facts as the integration basis (GATE-07 `ARTIFACT_REGISTER.csv` interface-fact artifacts on DEL-041-02).

### REQ-CWP-03 — Installation and tie-in workface plan

The work package SHALL include an installation and tie-in workface plan covering sequencing, predecessor/successor relationships, crew/discipline assignments, and field tie-in procedures for each interface in REQ-CWP-02. Quantitative sequencing values: TBD (not present in accessible registers; resolve from source slices).

### REQ-CWP-04 — Construction interface and turnover checklist

The work package SHALL include a construction interface and turnover checklist that, for each interface in REQ-CWP-02, records: interface ID, tie-in physical scope, inspection criteria, sign-off responsibility, and turnover acceptance status (`_CONTEXT.md` Anticipated Artifacts; structure inferred — ASSUMPTION).

### REQ-CWP-05 — Consistency with upstream deliverables

The Construction Work Package SHALL be consistent with:

- DEL-041-01 Scope of Work (boundaries and tagged equipment),
- DEL-041-02 Package Datasheet (interface requirements matrix and interface fact evidence), and
- the accepted vendor-furnished design captured on DEL-041-04 once available.

Conflicts SHALL be raised against the originating deliverable rather than silently reconciled.

### REQ-CWP-06 — Objective alignment

The Construction Work Package SHALL demonstrably support objectives `OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` mapped to DEL-041-03 in GATE-07 `OBJECTIVE_DELIVERABLE_MAP.csv`. Each objective's specific acceptance criteria: TBD (objective texts not opened in this run; location TBD).

### REQ-CWP-07 — Source-grounded values

Values, dimensions, ratings, and design points used in installation procedures SHALL be traceable to source slices (Workbook Packages row 43, Design Basis Memorandum at `_Sources/DBM-Deepcut`, or vendor-furnished documentation on DEL-041-04). Unsupported values SHALL be marked `TBD` and SHALL NOT be invented (project K-PROV-1; `_REFERENCES.md` Missing/Deferred References).

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| Workbook Packages row 43 | Authoritative source of package identity, responsibility split, and declared interfaces | `_Sources/26020-Packages_Interfaces_4_export.xlsx`; specific clause references TBD |
| Design Basis Memorandum (DBM-Deepcut) | Facility-level design basis | `_Sources/DBM-Deepcut`; specific clauses TBD |
| Discipline codes for 13.8 kV electrical work (e.g., NFPA 70, IEEE 142, IEEE 80) | ASSUMPTION: likely applicable to standby generator building construction; not derived from accessible sources in this run | location TBD |
| Site-specific construction standards | TBD | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-CWP-01 | Document review of authorship metadata on the issued work package |
| REQ-CWP-02 | Cross-check of construction work package interface coverage against GATE-07 `INTERFACE_REGISTER.csv` rows for PKG-041 (12 of 12 interfaces accounted for) |
| REQ-CWP-03 | Inspection that workface plan exists and addresses each interface in REQ-CWP-02 |
| REQ-CWP-04 | Inspection of turnover checklist for each interface (sign-off rows complete) |
| REQ-CWP-05 | Cross-document review against DEL-041-01, DEL-041-02, and DEL-041-04 (when available); conflicts logged in Conflict Table on `Guidance.md` |
| REQ-CWP-06 | Traceability matrix from each construction sub-activity to listed objectives; gaps logged as TBD |
| REQ-CWP-07 | Source-grounding audit: each non-trivial value cites a source path and section reference, or is marked `TBD` with `location TBD` |

## Documentation

The deliverable SHALL produce the following documentation, corresponding to the anticipated artifacts on `_CONTEXT.md`:

| Documentation item | Maps to artifact |
|---|---|
| Construction work package narrative | ART-55CB0F50C6 (EPC Construction Work Package) |
| Installation and tie-in workface plan | Anticipated artifact (`_CONTEXT.md`); artifact ID TBD until extracted on closeout |
| Construction interface and turnover checklist | Anticipated artifact (`_CONTEXT.md`); artifact ID TBD until extracted on closeout |
| Traceability record to OBJ-001/004/005/006/007/008/009/010 | Internal evidence; not a standalone artifact (ASSUMPTION) |
