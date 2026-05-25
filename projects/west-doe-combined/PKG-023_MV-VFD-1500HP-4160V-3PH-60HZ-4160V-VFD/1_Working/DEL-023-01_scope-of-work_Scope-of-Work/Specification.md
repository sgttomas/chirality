# Specification — DEL-023-01 Scope of Work (PKG-023)

Normative scope-of-work requirements for the EPC Integrator deliverable of PKG-023 "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD". Requirements that depend on detailed electrical design source slices not currently accessible are marked `TBD` and routed via the Conflict / Human Ruling list in `Guidance.md`.

## Scope

### In scope (this Scope of Work deliverable)

- Author the EPC Integrator-side package Scope of Work that defines the boundaries, function, tagged-equipment basis, source rows, WBS, discipline, integrator/vendor split, and facility integration narrative for PKG-023.
- Carry the responsibility assignment record between Package Vendor and EPC Integrator.
- Identify the applicable interface types between PKG-023 and the rest of the facility for downstream Package Datasheet, Construction Work Package, and Vendor Engineered Equipment Package deliverables to inherit.
- Reference (without re-authoring) the standards and Design Basis Memorandum constraints that govern the package's integration into the West Doe Deepcut expansion.

### Out of scope (handled elsewhere)

- Vendor package engineering, design, and physical equipment (`DEL-023-04_vendor-engineered-equipment-package`).
- Technical handoff data and interface requirements matrix (`DEL-023-02_package-datasheet`).
- Installation, tie-in, inspection, and turnover (`DEL-023-03_construction-work-package`).
- Vendor document register/turnover (`DEL-023-05_vendor-document-turnover-package`).
- EPC vendor package review and acceptance (`DEL-023-06_epc-vendor-package-review-and-acceptance`).
- VFD topology selection, harmonic mitigation design, and protection coordination (carried out under vendor engineering and the Package Datasheet downstream).

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-023-01-001 | The Scope of Work shall identify PKG-023 as a Vendor-owned Electrical package under WBS 01 with project CoA 26020-01-30-014. | `PACKAGE_REGISTER.csv` | Datasheet Identification table cross-check. |
| REQ-023-01-002 | The Scope of Work shall state the package title verbatim as "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD" and reference Workbook Packages row 25. | `PACKAGE_REGISTER.csv`; Workbook Packages row 25 | Title string match. |
| REQ-023-01-003 | The Scope of Work shall record the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` | Responsibility Evidence artifact (ART-A3F647F3C3) review. |
| REQ-023-01-004 | The Scope of Work shall enumerate the six applicable interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv` | Interface list cross-check against six IFC rows for PKG-023. |
| REQ-023-01-005 | The Scope of Work shall list the four anticipated artifacts (Package SoW; Tagged equipment and package identity list; Package function and integration narrative; Responsibility assignment record) and align them to the `ARTIFACT_REGISTER.csv` rows for DEL-023-01. | `ARTIFACT_REGISTER.csv` | Artifact ID cross-check. |
| REQ-023-01-006 | The Scope of Work shall preserve the workbook-stated exclusions as "TBD; no package-specific exclusions stated in source materials." until additional source material is accepted. | `PACKAGE_REGISTER.csv` | Exclusion section review. |
| REQ-023-01-007 | The Scope of Work shall record that for 4.16 kV motors generally, the Deepcut DBM states "VFD and soft-starter requirements for 4.16 kV motors are TBD," and shall not assert a specific MV VFD topology, harmonic class, or bypass arrangement without source support. | `4-25_Deepcut_DBM.md` lines 2957, 3088 | Verification by reviewer against DBM cited slice. |
| REQ-023-01-008 | The Scope of Work shall require that VFD-fed motors located in Zone 2 areas be marked and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study, and pass this obligation to the vendor and construction packages. | `4-25_Deepcut_DBM.md` line 2961 | Cross-reference present in vendor handoff (PKG Datasheet) and construction package. |
| REQ-023-01-009 | The Scope of Work shall identify the driven motor and process service that the 1,500 HP / 4,160 V MV VFD supports. | TBD — not in available DBM slice (HRR-023-01-001) | Pending human ruling. |
| REQ-023-01-010 | The Scope of Work shall state the package quantity, installed-spare basis, and any redundancy expectations. | TBD — not in available DBM slice (HRR-023-01-002) | Pending human ruling. |
| REQ-023-01-011 | The Scope of Work shall reference the site environmental design conditions (ambient temperature range, altitude, seismic, snow/wind) for the MV VFD lineup location. | TBD — not in available DBM slice | Pending source slice. |
| REQ-023-01-012 | The Scope of Work shall identify the upstream 4,160 V source (switchgear lineup, feeder, protection class) from which PKG-023 is fed and the grounding/bonding philosophy applicable at the package terminals. | TBD — `PKG-011 4160V SWITCHGEAR EQUIPMENT` is the likely facility 4,160 V source (ASSUMPTION) | Cross-check against PKG-011 deliverables once available. |

## Standards

- **NEMA MG 1** — Motors and generators; cited by Deepcut DBM for facility motors (`4-25_Deepcut_DBM.md` line 936). Applicability to PKG-023's driven motor is ASSUMPTION pending vendor handoff.
- **IEEE 519** — Harmonic control on power systems (industry standard for MV VFD installations). Applicability to PKG-023 is ASSUMPTION; not explicitly cited in available DBM slice (location TBD).
- **CSA / CEC and area-classification governance** — VFD-fed motors in Zone 2 marking requirement (`4-25_Deepcut_DBM.md` line 2961).
- **Workbook 26020 Packages** — row 25 governs package identity (cited; source file `26020-Packages_Interfaces_4_export.xlsx` not opened in this run).

Additional governing standards (IEC 61800 series, CSA C22.2 No. 14, project electrical specifications) are likely applicable but their specific clauses are `location TBD` until source slices are accessible.

## Verification

| Verification Approach | Applies To |
|---|---|
| Cross-check of identity, package title, WBS, CoA, and responsibility split against Gate 7 registers. | REQ-023-01-001..006 |
| Cross-check of interface list against `INTERFACE_REGISTER.csv` rows for PKG-023. | REQ-023-01-004 |
| Cross-check of cited DBM source slices for 4,160 V MCC policy and Zone 2 marking. | REQ-023-01-007, REQ-023-01-008 |
| Human ruling on driven service, quantity, environmental, and feeder identification. | REQ-023-01-009..012 |

## Documentation

The following artifacts shall be produced or referenced under this Scope of Work:

| Artifact ID | Artifact | Anticipated From |
|---|---|---|
| ART-D70FE712E8 | Package scope of work | This deliverable |
| ART-2C8B496DD1 | Tagged equipment and package identity list | This deliverable |
| ART-26BB26779C | Package function and whole-facility integration narrative | This deliverable |
| ART-A3F647F3C3 | Package responsibility assignment record | This deliverable |
