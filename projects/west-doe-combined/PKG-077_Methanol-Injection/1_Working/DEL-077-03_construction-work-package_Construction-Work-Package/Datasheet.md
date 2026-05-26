# Datasheet — DEL-077-03 Construction Work Package (Methanol Injection)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-077-03_construction-work-package | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | PKG-077 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-077 |
| PackageName | Methanol Injection | `PACKAGE_REGISTER.csv` row PKG-077 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` row PKG-077 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-077 |
| Workbook Source | Workbook Packages row 72 | `DELIVERABLE_REGISTER.csv` row DEL-077-03 |
| Type | EPC Construction Work Package | `DELIVERABLE_REGISTER.csv` row DEL-077-03 |
| ResponsibleParty | EPC Integrator | `DELIVERABLE_REGISTER.csv` row DEL-077-03 |
| Covers Scope Items | SOW-0143 | `SCOPE_LEDGER.csv` row SOW-0143 |
| Supports Objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `DELIVERABLE_REGISTER.csv` row DEL-077-03 (ASSUMPTION: package-heuristic mapping) |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Methanol injection system for the WBS 01 Deepcut facility (sour-service hydrate inhibition context inferred) | `PACKAGE_REGISTER.csv` PKG-077; ASSUMPTION on function detail |
| Vendor / EPC Split | Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | `PACKAGE_REGISTER.csv` row PKG-077 ResponsibilityModel |
| Applicable Interfaces | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-077 (13 IFC rows) |
| Package Exclusions | TBD — no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` row PKG-077 |
| Tagged Equipment List | TBD — equipment tag list not present in decomposition rows; expected from DEL-077-01 / DEL-077-02 | location TBD |
| Process Conditions (P, T, flow, composition) | TBD — not available in registers; design basis to be drawn from DBM-Deepcut SEC-07/SEC-08/SEC-10 (location TBD; source slice not copied locally) | location TBD |
| Hazardous Area Classification | TBD — methanol service is flammable (Class I); specific area classification not in accessible sources | ASSUMPTION (flammable service); value TBD |
| Sour Service Applicability | ASSUMPTION: applies (PKG-077 lies within sour-service Deepcut scope per OBJ-009 mapping) | `OBJECTIVE_REGISTER.csv` OBJ-009 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / Facility | 04-25 Deepcut facility, WBS 01 | `OBJECTIVE_REGISTER.csv` OBJ-001 |
| Construction Environment | TBD — winterization, ambient design temperatures not in accessible sources | location TBD |
| Construction Sequencing Constraint | TBD — sequencing with adjacent PKG-077 deliverables (vendor package delivery, foundations, electrical, controls tie-ins) | location TBD |
| Turnover Target | Mechanical completion to commissioning handoff per OBJ-010 (commissioning/turnover and controlled open-item closure) | `OBJECTIVE_REGISTER.csv` OBJ-010 |

## Construction (Artifacts Produced)

| ArtifactID | Artifact | Type | Source |
|---|---|---|---|
| ART-D62FFA7E43 | Construction work package | EPC Construction Work Package | `ARTIFACT_REGISTER.csv` |
| ART-F3B0D2F531 | Installation and tie-in workface plan | Construction Tie-In Evidence | `ARTIFACT_REGISTER.csv` |
| ART-EC659AD03C | Construction interface and turnover checklist | Construction Interface Evidence | `ARTIFACT_REGISTER.csv` |

## References

- `_CONTEXT.md` (deliverable identity, scope, objectives mapping)
- `_REFERENCES.md` (decomposition basis pointers)
- `DELIVERABLE_REGISTER.csv` row DEL-077-03
- `PACKAGE_REGISTER.csv` row PKG-077
- `SCOPE_LEDGER.csv` row SOW-0143
- `ARTIFACT_REGISTER.csv` rows ART-D62FFA7E43, ART-F3B0D2F531, ART-EC659AD03C
- `INTERFACE_REGISTER.csv` PKG-077 rows (13 interface facts)
- `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010
- DBM-Deepcut/4-25_Deepcut_DBM.md — location TBD (not copied to deliverable-local references)
- 26020-Package_Requirements.docx — location TBD (referenced by OBJ-004/OBJ-010 but not deliverable-local)
