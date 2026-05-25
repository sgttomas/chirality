# Procedure: DEL-011-02_package-datasheet - Package Datasheet

## Purpose

Define the working procedure for producing and checking the `PKG-011` 4160V SWITCHGEAR EQUIPMENT package datasheet as an EPC Integrator technical handoff deliverable.

## Prerequisites

- Accepted Gate 7 decomposition snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- No declared upstream dependencies are listed for this deliverable in `_DEPENDENCIES.md`.
- Accessible source slices include:
  - `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-09 and SEC-12.
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`: `DEL-011-02_package-datasheet`, `PKG-011`, 4160V SWITCHGEAR EQUIPMENT, Electrical, EPC Package Datasheet, EPC Integrator.
2. Confirm package responsibility from `PACKAGE_REGISTER.csv`: Package Vendor owns package engineering, design, documentation, and physical equipment; EPC Integrator owns facility-level integration and interfaces.
3. Build the datasheet interface matrix from `INTERFACE_REGISTER.csv` for `PKG-011`: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
4. Populate electrical basis fields from `3-25_Comp_and_Liquids_DBM.md`, SEC-12:
   - shared cross-facility utility supplied from 04-25;
   - 13.8 kV incoming feed from the 04-25 Main Switchgear Electrical Building;
   - 13.8 kV to 4.16 kV, 12 MVA transformer serving the 4160V MCC for 4000V motors;
   - 4,160 V, 3 phase, 3 wire, 60 Hz, low-resistance grounded service basis;
   - contactors, motor protection relays, EtherNet communication port, and plant PLC data acquisition interface;
   - `KM-2150` and `KM-2250` starting VFD basis;
   - detailed-study status for harmonic and reactive-power mitigation.
5. Populate environmental, area-classification, raceway, grounding/bonding, and winterization notes from the DBM source slices.
6. List applicable standards and specifications from `4-25_Deepcut_DBM.md`, SEC-12, without extracting clause-level requirements from unavailable specification bodies.
7. Mark final package-specific ratings, settings, lineup configuration, enclosure details, vendor document requirements, and other unavailable values as `TBD`.
8. Record any source discrepancy or terminology issue in `Guidance.md` under the Conflict Table.
9. Cross-check the four documents:
   - Datasheet attributes appear in Specification requirements where appropriate.
   - Specification requirements have Guidance rationale where useful.
   - Specification requirements have verification hooks in this Procedure.
   - Terms and values match across all four documents.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Datasheet and Specification use the same deliverable ID, package ID, package name, discipline, type, and responsible party. |
| Source check | Non-trivial electrical values cite Gate 7 registers or DBM section references. |
| TBD check | Unsupported package-specific values remain `TBD`. |
| Interface check | The six declared `PKG-011` interface facts appear consistently in Datasheet, Specification, and Procedure. |
| Responsibility check | EPC Integrator and Package Vendor responsibilities are not collapsed into one owner. |
| Conflict check | The package-name versus DBM terminology issue is surfaced for human ruling. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-24_1658.md`
