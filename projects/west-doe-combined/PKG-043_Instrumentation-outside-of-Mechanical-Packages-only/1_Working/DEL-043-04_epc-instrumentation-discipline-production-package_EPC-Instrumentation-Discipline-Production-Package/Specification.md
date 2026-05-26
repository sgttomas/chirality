# Specification — DEL-043-04 EPC / Instrumentation Discipline Production Package

## Scope

### In scope
- EPC Integrator or discipline-subcontractor production work for the non-vendor Instrumentation package scope under `PKG-043` (Instrumentation outside of Mechanical Packages only) (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04; `PACKAGE_REGISTER.csv` row PKG-043).
- Production-unit basis carried conservatively from workbook and DBM support (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04 Description).
- Coverage of `SOW-0044` (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04 CoversScopeItems).
- Support for objectives `OBJ-001`, `OBJ-003`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-010` (source: `OBJECTIVE_DELIVERABLE_MAP.csv`).

### Out of scope / exclusions
- Vendor-package ownership model — not inferred from current sources (source: `PACKAGE_REGISTER.csv` row PKG-043 ResponsibleParty note).
- Mechanical-package-internal instrumentation (excluded by the package name itself: "Instrumentation outside of Mechanical Packages only") (source: `PACKAGE_REGISTER.csv` row PKG-043 PackageName).
- Detailed non-vendor package deliverable requirements are deferred to Gate 5 disposition (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04 Notes).

## Requirements

| ID | Requirement | Source / Status |
|---|---|---|
| REQ-043-04-01 | The deliverable shall produce a Discipline Production Package basis covering instrumentation scope outside of mechanical packages. | `DELIVERABLE_REGISTER.csv` row DEL-043-04 AnticipatedArtifacts |
| REQ-043-04-02 | The deliverable shall produce a discipline deliverable register; specific register contents are TBD pending Gate 5 disposition. | `DELIVERABLE_REGISTER.csv` row DEL-043-04 AnticipatedArtifacts; TBD |
| REQ-043-04-03 | The deliverable shall produce a source-limited requirements closure record documenting which requirements could be sourced and which remain TBD. | `DELIVERABLE_REGISTER.csv` row DEL-043-04 AnticipatedArtifacts; Notes |
| REQ-043-04-04 | Responsibility allocation between EPC Integrator and discipline subcontractor shall be confirmed; current source state is TBD. | `DELIVERABLE_REGISTER.csv` row DEL-043-04 ResponsibleParty; `PACKAGE_REGISTER.csv` PKG-043 |
| REQ-043-04-05 | The production package shall be consistent with the five package-level interfaces recorded for PKG-043: Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network. | `INTERFACE_REGISTER.csv` rows IFC-AE83B2D0FC, IFC-F41620D435, IFC-E5A8000199, IFC-4929B68CCD, IFC-35EBF9CD91 |
| REQ-043-04-06 | Per Gate 6 disposition, instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy; the production package shall reflect this. | `INTERFACE_REGISTER.csv` rows (Gate 6 disposition note) |
| REQ-043-04-07 | Detailed discipline requirements not sourced from workbook or accessible DBM material shall be marked TBD rather than invented; Gate 5 disposition is required for closure. | `DELIVERABLE_REGISTER.csv` row DEL-043-04 Notes |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| Workbook Packages row 45 | Authoritative source row for PKG-043 / DEL-043-04 | location TBD (slice not present in `_REFERENCES.md` accessible set) |
| DBM-Deepcut (4-25_Deepcut_DBM.md) | Source basis referenced by `PACKAGE_REGISTER.csv` SourceRef | location TBD (slice not locally extracted) |
| Discipline / code standards (e.g., I&C, electrical, instrumentation codes) | ASSUMPTION: likely applicable; specific clauses TBD | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-043-04-01 | Inspection of produced discipline production package basis against `_CONTEXT.md` AnticipatedArtifacts |
| REQ-043-04-02 | Review that a discipline deliverable register is produced and that gaps are explicitly TBD rather than invented |
| REQ-043-04-03 | Review of closure record listing sourced vs. TBD requirements with provenance |
| REQ-043-04-04 | Confirmation by human ruling at Gate 5 (responsibility allocation) |
| REQ-043-04-05 | Cross-check production package interface coverage against `INTERFACE_REGISTER.csv` rows for PKG-043 |
| REQ-043-04-06 | Inspection that field supports, power, and comms inclusion is reflected per Gate 6 disposition |
| REQ-043-04-07 | Audit of all unsourced statements for explicit TBD labels and Gate 5 referral |

## Documentation

- Discipline production package basis document
- Discipline deliverable register (TBD content)
- Source-limited requirements closure record
- Interface coverage cross-reference (against `INTERFACE_REGISTER.csv` rows for PKG-043)
- TBD: Gate 5 disposition record (when produced)
