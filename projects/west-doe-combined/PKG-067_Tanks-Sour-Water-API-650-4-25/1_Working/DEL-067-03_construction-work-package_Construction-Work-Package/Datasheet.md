# Datasheet — DEL-067-03 Construction Work Package (Tanks, Sour Water (API 650) 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-067-03_construction-work-package | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | PKG-067 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-067 |
| PackageName | Tanks, Sour Water (API 650) 4-25 | `PACKAGE_REGISTER.csv` row PKG-067 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` row PKG-067 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-067 |
| Workbook Source | Workbook Packages row 94 | `DELIVERABLE_REGISTER.csv` row DEL-067-03 |
| Type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-067-03 |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-067-03 |
| Covers Scope Items | SOW-0225, SOW-0226, SOW-0227, SOW-0228 | `SCOPE_LEDGER.csv` rows SOW-0225..SOW-0228; `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `DELIVERABLE_REGISTER.csv` row DEL-067-03 (ASSUMPTION: package-heuristic mapping) |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_CONTEXT.md`; `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Two produced-water / sour-water storage tanks for 4-25 service, matching the 4-25 tank pair identified in the 3-25 sour water analog. | `SCOPE_LEDGER.csv` SOW-0226; `PACKAGE_REGISTER.csv` PKG-067 ScopeStatement |
| Vendor / EPC Split | Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. | `PACKAGE_REGISTER.csv` PKG-067 ResponsibilityModel |
| Applicable Interfaces (9) | Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-067 (9 rows, all Applicable=YES) |
| Package Exclusions | TBD — no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` PKG-067 Exclusions ("TBD; no package-specific exclusions stated in source materials.") |
| Tagged Equipment (expected) | TK-9010-1 and TK-9020-1 — two API 650 modified atmospheric produced-water storage tanks (final tag confirmation TBD per SOW-0228). | `SCOPE_LEDGER.csv` SOW-0227, SOW-0228 |
| Major Included Equipment Features | Internal coating; external insulation and electric heating where required; PVRV/EPRV protection; LP fuel gas blanket; VRU suction / header connection as applicable; tank instrumentation; standard tank appurtenances. | `SCOPE_LEDGER.csv` SOW-0227 |
| Tracking Number | 26020-01-PT-19-005 — Tanks, Sour Water | `PACKAGE_REGISTER.csv` PKG-067 (TrackingNumber) |
| Sour Service Applicability | Applies — sour-water / produced-water service per package basic scope; final service naming (sour produced water vs. produced water vs. sour water) is an open item per SOW-0228. | `SCOPE_LEDGER.csv` SOW-0226, SOW-0228; `OBJECTIVE_REGISTER.csv` OBJ-009 |
| Atmospheric Tank Class | API 650 modified atmospheric storage tanks. | `SCOPE_LEDGER.csv` SOW-0227 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / Facility | 04-25 Deepcut facility, WBS 01 | `OBJECTIVE_REGISTER.csv` OBJ-001; `PACKAGE_REGISTER.csv` PKG-067 |
| Tank Count | Two (2) tanks | `SCOPE_LEDGER.csv` SOW-0226, SOW-0227 |
| Tank Tags (expected) | TK-9010-1, TK-9020-1 (confirmation TBD per SOW-0228) | `SCOPE_LEDGER.csv` SOW-0227, SOW-0228 |
| Service | Sour-water / produced-water (final naming TBD) | `SCOPE_LEDGER.csv` SOW-0226, SOW-0228 |
| Source Headers | TBD (location TBD — confirmation called out as open item in SOW-0228; underlying analog basis in 3-25 sour-water package and DBM-Deepcut not deliverable-local for clause-level citation) | `SCOPE_LEDGER.csv` SOW-0228 |
| Design Specific Gravity | TBD (location TBD — open item SOW-0228) | `SCOPE_LEDGER.csv` SOW-0228 |
| Heating / Insulation Requirements | External insulation and electric heating "where required" (extent TBD per SOW-0228 confirmation). | `SCOPE_LEDGER.csv` SOW-0227, SOW-0228 |
| Vapor Conservation / Blanket | Low-pressure (LP) fuel-gas blanket; PVRV/EPRV protection; VRU suction/header connection "as applicable" (final applicability TBD per SOW-0228). | `SCOPE_LEDGER.csv` SOW-0227, SOW-0228 |
| Internal Coating | Required (extent and system specification TBD — location TBD; not deliverable-local) | `SCOPE_LEDGER.csv` SOW-0227 |
| Ambient Design Temperatures | TBD (location TBD — DBM-Deepcut/4-25_Deepcut_DBM.md sections governing ambient design temperatures not extracted into deliverable-local references) | `_REFERENCES.md` |
| Whether full 3-25 sour-water design basis applies | TBD — explicit open item to confirm whether 3-25 sour-water design basis applies to the 4-25 tank pair. | `SCOPE_LEDGER.csv` SOW-0228 |
| Construction Sequencing Constraint | TBD — sequencing with civil/foundations, secondary containment, electrical EHT (where required), instrumentation, and blanket-gas / VRU tie-ins. | location TBD |
| Turnover Target | Mechanical completion to commissioning handoff per OBJ-010 (commissioning/turnover and controlled open-item closure). | `OBJECTIVE_REGISTER.csv` OBJ-010 |

## Construction (Artifacts Produced)

| ArtifactID | Artifact | Type | Source |
|---|---|---|---|
| ART-EE79CD3464 | Construction work package | EPC Construction Work Package | `ARTIFACT_REGISTER.csv` DEL-067-03 |
| ART-FE1E5417F6 | Installation and tie-in workface plan | Construction Tie-In Evidence | `ARTIFACT_REGISTER.csv` DEL-067-03 |
| ART-09F3991C52 | Construction interface and turnover checklist | Construction Interface Evidence | `ARTIFACT_REGISTER.csv` DEL-067-03 |

## References

- `_CONTEXT.md` (deliverable identity, scope, objectives mapping)
- `_REFERENCES.md` (decomposition basis pointers)
- `DELIVERABLE_REGISTER.csv` row DEL-067-03
- `PACKAGE_REGISTER.csv` row PKG-067
- `SCOPE_LEDGER.csv` rows SOW-0225, SOW-0226, SOW-0227, SOW-0228
- `ARTIFACT_REGISTER.csv` rows ART-EE79CD3464, ART-FE1E5417F6, ART-09F3991C52
- `INTERFACE_REGISTER.csv` PKG-067 rows (9 interface facts)
- `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010
- 26020-Package_Requirements.docx package heading 22 — present under `_Sources/` as binary `.docx`; section-level text not deliverable-local (location TBD for clause-level citation)
- 26020-03-PT-RFQ-19-007 — Sour Water Tanks (3-25 analog) — analog basis cited by `PACKAGE_REGISTER.csv` PKG-067 (location TBD; not deliverable-local)
- DBM-Deepcut/4-25_Deepcut_DBM.md — design basis referenced by `PACKAGE_REGISTER.csv` PKG-067 (location TBD; not extracted into deliverable-local references)
