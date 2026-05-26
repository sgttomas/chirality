# Datasheet — DEL-042-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-042-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` Identity |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-042` | `_CONTEXT.md` Identity |
| ParentWorkbookID | 42 | `_CONTEXT.md` Identity |
| PackageName | Control Room Building | `_CONTEXT.md` Identity |
| Discipline | Electrical | `_CONTEXT.md` Identity; `PACKAGE_REGISTER.csv` row PKG-042 |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row DEL-042-06 |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` Identity |
| Covers Scope Item | `SOW-0043` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` row SOW-0043 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject vendor package | Control Room Building vendor-engineered electrical package | `PACKAGE_REGISTER.csv` row PKG-042 |
| Acceptance posture | EPC Integrator review and acceptance of Package Vendor deliverables against the EPC-authored Scope of Work, Package Datasheet, and Construction Work Package | `DELIVERABLE_REGISTER.csv` row DEL-042-06 (Description) |
| Reference EPC anchor deliverables | `DEL-042-01_scope-of-work`, `DEL-042-02_package-datasheet`, `DEL-042-03_construction-work-package` | `DELIVERABLE_REGISTER.csv` rows DEL-042-01..03 |
| Reference vendor production deliverables | `DEL-042-04_vendor-engineered-equipment-package`, `DEL-042-05_vendor-document-turnover-package` | `DELIVERABLE_REGISTER.csv` rows DEL-042-04, DEL-042-05 |
| Applicable interface types (acceptance scope) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row PKG-042; `INTERFACE_REGISTER.csv` PKG-042 rows |
| Supported objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Sour-service applicability | TBD — not stated in available decomposition slices for PKG-042. | `PACKAGE_REGISTER.csv` row PKG-042 (no sour-service flag) |
| Site/environmental conditions | TBD (location TBD — depend on facility DBM source slices not locally referenced by this deliverable) | `_REFERENCES.md` Missing/Deferred |
| Vendor identity | TBD | not in available source set |
| Acceptance schedule milestones | TBD | not in available source set |

## Construction (Anticipated Artifacts of This Deliverable)

| Artifact | Source |
|---|---|
| Vendor document review log | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row DEL-042-06 |
| Package acceptance checklist | `_CONTEXT.md` Anticipated Artifacts |
| Test / inspection evidence | `_CONTEXT.md` Anticipated Artifacts |
| Turnover evidence | `_CONTEXT.md` Anticipated Artifacts |

## References

- `_CONTEXT.md` — deliverable identity and scope.
- `_REFERENCES.md` — authoritative decomposition basis and shared source root.
- `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot) — row DEL-042-06.
- `PACKAGE_REGISTER.csv` (GATE-07 snapshot) — row PKG-042.
- `INTERFACE_REGISTER.csv` (GATE-07 snapshot) — interfaces tagged to PKG-042.
- `SCOPE_LEDGER.csv` (GATE-07 snapshot) — row SOW-0043.
- `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (GATE-07 snapshot) — supported objectives.
- Workbook Packages row 44 (source of record cited by the decomposition; not locally accessible as a parsed slice — `location TBD`).
- 26020-Package_Requirements.docx vendor-document tables (referenced by OBJ-004 and OBJ-010; `location TBD` — not parsed locally).
