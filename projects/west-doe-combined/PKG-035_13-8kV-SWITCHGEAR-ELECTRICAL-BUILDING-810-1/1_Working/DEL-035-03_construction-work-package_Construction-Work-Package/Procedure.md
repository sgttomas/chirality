# Procedure: DEL-035-03_construction-work-package

## Purpose

This procedure describes how the EPC Integrator produces the Construction Work Package for `PKG-035` (13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)) and how that work package is then used during physical installation, tie-in, inspection, energization, and turnover of Electrical Building 810-1 into the facility.

## Prerequisites

- Accepted Gate 7 upstream snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Accepted `DEL-035-01_scope-of-work` for PKG-035.
- Accepted `DEL-035-02_package-datasheet` for PKG-035.
- Package Vendor engineered package basis (from `DEL-035-04_vendor-engineered-equipment-package`) sufficient for construction planning; specific submittal status is TBD.
- Confirmed Gate 7 interface set at PKG-035 (`INTERFACE_REGISTER.csv` rows for `PKG-035`).
- Accessible authoritative source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis sections (facility electrical system, Electrical Buildings, grounding, cable tray, cable schedule, buildings list row "810-1").
- Civil/structural readiness at the Building 810-1 site (piles, grading, drainage); package-specific civil source slice TBD.
- No declared upstream or downstream coordination dependencies in `_DEPENDENCIES.md` at PREPARATION time; coordination mode DECLARED.

## Steps

### Phase A — Produce the Construction Work Package

1. Re-read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` to confirm scope, references, and state.
2. Resolve PKG-035 facts from Gate 7 registers: `PACKAGE_REGISTER.csv` row `PKG-035`, `DELIVERABLE_REGISTER.csv` row `DEL-035-03_construction-work-package`, `SCOPE_LEDGER.csv` row `SOW-0036`, `INTERFACE_REGISTER.csv` rows for `PKG-035`, and `OBJECTIVE_SCOPE_MAP.csv` rows for `SOW-0036` / `PKG-035`.
3. Read the authoritative source slices in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` for facility electrical system, Electrical Buildings, grounding/bonding, cable tray, cable schedule, and the buildings list row "810-1 13.8kV Switchgear Electrical Building".
4. Draft the construction work package master document covering scope, sequence, organization, safety, quality, and turnover, grounded in the source slices.
5. Draft the installation and tie-in workface plan addressing receipt and setting of Building 810-1, incoming utility feed, outgoing radial 13.8 kV feeders, grounding, cable tray/conduit, HVAC commissioning, and energization sequencing.
6. Draft the construction interface and turnover checklist with one section per PKG-035 interface type from `INTERFACE_REGISTER.csv` (twelve interfaces).
7. Cross-check the three artifacts against Specification requirements `REQ-035-03-01` through `REQ-035-03-15` and resolve gaps as `TBD` rather than guessing.
8. Submit the Construction Work Package package for EPC Integrator internal acceptance.

### Phase B — Use the Construction Work Package on site

9. Verify civil/structural readiness (piles, grading, drainage) at the 810-1 location before mobilizing the building.
10. Receive shop-built Building 810-1, transport to site, set on piles, and anchor per the workface plan.
11. Install incoming 25 kV / 13.8 kV utility feed connection to the switchgear; install outgoing radial 13.8 kV feeders to dependent electrical building locations.
12. Install grounding/bonding: connect major equipment to the ground grid at two points; install ground wells with bolted test points; route above-grade conductors per DBM.
13. Install cable tray and conduit consistent with bottom-entry geometry; install 13.8 kV cables as three-conductor TECK rated 15 kV with 133% insulation, shielded; ensure routing does not interfere with maintenance access.
14. Install the outdoor GFI receptacle; confirm door/transom configuration is suitable for largest-equipment removal.
15. Commission building HVAC and demonstrate n+1 redundancy.
16. Execute the construction interface and turnover checklist for each of the twelve PKG-035 interface types.
17. Execute pre-energization checks (ground continuity, cable acceptance, vendor protection settings verification, lockout/tagout) per the energization sequence.
18. Energize the 13.8 kV bus per the planned sequence and confirm readiness for downstream radial feeder energization to dependent electrical buildings.

## Verification

- Specification requirements `REQ-035-03-01` through `REQ-035-03-15` are each addressed in the construction work package, workface plan, or turnover checklist.
- Grounding two-point connection verified by ground continuity test (`REQ-035-03-07`, `REQ-035-03-08`).
- 13.8 kV cables verified as TECK three-conductor 15 kV / 133% insulation, shielded (`REQ-035-03-06`).
- HVAC n+1 redundancy demonstrated (`REQ-035-03-11`).
- All twelve PKG-035 interface checklist rows complete and signed (`REQ-035-03-13`).
- Energization sequence executed without re-work to upstream tie-ins (`REQ-035-03-14`).

## Records

- Construction work package master document (Phase A output).
- Installation and tie-in workface plan (Phase A output).
- Construction interface and turnover checklist, one per PKG-035 interface type (Phase A and Phase B output).
- Pre-energization checklist record and energization sequence record (Phase B output).
- Grounding/bonding installation and test records.
- Cable installation and acceptance test records.
- HVAC commissioning record.
- Inspection records, NCRs, and resolutions.
- Turnover package to operations.

Source references:
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis sections.
- `DELIVERABLE_REGISTER.csv` row `DEL-035-03_construction-work-package` (anticipated artifacts).
- `INTERFACE_REGISTER.csv` rows for `PKG-035` (twelve interface types).
