# Specification: DEL-105-04 — EPC / Structural Discipline Production Package

## Scope

This specification governs the EPC / Structural Discipline Production Package for `PKG-105 — Platforms` (workbook ID `26020-01-36-005`, WBS `01`).

**In scope** (from `DELIVERABLE_REGISTER.csv` row `DEL-105-04` and `_CONTEXT.md`):
- The non-vendor package scope of the Platforms structural package, produced by the EPC Integrator or assigned discipline subcontractor.
- Production-package evidence carried conservatively from workbook and DBM support.
- A source-limited requirements closure record that documents which discipline requirements are not present in current source materials.

**Out of scope:**
- Vendor-package engineering and supply (this deliverable is explicitly the *non-vendor* package scope) — source: `DELIVERABLE_REGISTER.csv` row `DEL-105-04`.
- The EPC anchor deliverables produced under the same package — Scope of Work (`DEL-105-01`), Package Datasheet (`DEL-105-02`), and Construction Work Package (`DEL-105-03`).
- Package-level exclusions are otherwise TBD — `PACKAGE_REGISTER.csv` row PKG-105 records "no package-specific exclusions stated in source materials."

## Requirements

| ReqID | Requirement | Authority | Type |
|---|---|---|---|
| R-01 | Produce a discipline production package basis as workbook- and DBM-supported production package evidence for PKG-105 (Platforms). | `ARTIFACT_REGISTER.csv` ART-16D83D7454 | FACT |
| R-02 | Produce a (currently TBD) discipline deliverable register enumerating the structural deliverables required to execute the non-vendor scope of PKG-105. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-105-04` | FACT |
| R-03 | Produce a source-limited requirements closure record listing the discipline requirements that are not present in the current source set and that remain open. | `ARTIFACT_REGISTER.csv` ART-10C0D579FC; `DELIVERABLE_REGISTER.csv` Notes | FACT |
| R-04 | Respect and carry forward the recorded PKG-105 interface facts: Area / Exterior Lighting (IFC-26E3DCAD56), Grading / Site Drainage / Spill Containment (IFC-07C472C58B), and Structural / Foundations / Supports (IFC-B7C0A01E38). | `INTERFACE_REGISTER.csv` PKG-105 rows | FACT |
| R-05 | Treat platform-to-equipment tie-ins as EPC Integrator responsibility through the overall 3D model and integrated P&ID set (Gate 6 disposition recorded on PKG-105 interfaces). | `INTERFACE_REGISTER.csv` PKG-105 Notes | FACT |
| R-06 | Conservatively carry forward workbook and DBM-supported information without inventing requirements not present in source. | `DELIVERABLE_REGISTER.csv` row `DEL-105-04` description | FACT |
| R-07 | Demonstrate support for OBJ-001, OBJ-005, OBJ-008, OBJ-010 through traceable evidence in the production-package basis. | `OBJECTIVE_DELIVERABLE_MAP.csv` (explicit deliverable-ID mapping) | FACT |
| R-08 | Structural design requirements (loads, load combinations, materials, codes, connections, deflection limits) | TBD — not present in locally accessible source slices for this deliverable; clause-level extraction must occur from `_Sources/26020-Package_Requirements.docx` and any DBM Platforms-specific slice before this requirement can be elaborated. | TBD |
| R-09 | Fabrication, shop drawing, and inspection requirements | TBD — not present in locally accessible source slices | TBD |
| R-10 | Coatings, fireproofing, and corrosion-protection requirements | TBD — not present in locally accessible source slices | TBD |

## Standards

- Workbook Packages row 106 — primary source reference (`_REFERENCES.md`; `_CONTEXT.md`). Location TBD for clause-level slices; the workbook is present as `_Sources/26020-Package_Requirements.docx` but slices were not copied during PREPARATION.
- DBM-Deepcut basis (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) — referenced by PKG-105 row in `PACKAGE_REGISTER.csv`; no Platforms-specific slice identified.
- Governing structural codes and project structural specifications — TBD; ASSUMPTION: project-level structural code basis is expected to be inherited from the EPC Integrator package basis (DEL-105-01 / DEL-105-02). Confirm by extracting workbook slices before reliance.

## Verification

| ReqID | Verification Approach |
|---|---|
| R-01 | Inspection of the produced production-package basis against `_REFERENCES.md` and the GATE-07 artifact register row ART-16D83D7454. |
| R-02 | Review of the produced discipline deliverable register for completeness against the non-vendor scope statement in `DELIVERABLE_REGISTER.csv` row `DEL-105-04`. |
| R-03 | Review of the closure record against `ARTIFACT_REGISTER.csv` row ART-10C0D579FC and `_REFERENCES.md` Missing/Deferred References section. |
| R-04 | Cross-check of carried interface facts against `INTERFACE_REGISTER.csv` PKG-105 rows. |
| R-05 | Verify all platform-to-equipment tie-ins are routed through the EPC 3D model and integrated P&ID set, with traceable references. |
| R-06 | Source-fidelity audit comparing produced content to accessible workbook and DBM source slices; PROPOSAL — apply the `four-documents` QA expectations. |
| R-07 | Trace matrix from R-01..R-05 evidence to OBJ-001, OBJ-005, OBJ-008, OBJ-010 using the GATE-07 `OBJECTIVE_DELIVERABLE_MAP.csv`. |
| R-08..R-10 | Verification approach TBD pending source-slice extraction. |

## Documentation

Anticipated artifacts produced by this deliverable (from `_CONTEXT.md`; cross-checked with `ARTIFACT_REGISTER.csv` PKG-105 rows for `DEL-105-04`):

1. Discipline production package basis (ART-16D83D7454).
2. TBD discipline deliverable register (no register-row currently in `ARTIFACT_REGISTER.csv`; to be produced and registered).
3. Source-limited requirements closure record (ART-10C0D579FC).
