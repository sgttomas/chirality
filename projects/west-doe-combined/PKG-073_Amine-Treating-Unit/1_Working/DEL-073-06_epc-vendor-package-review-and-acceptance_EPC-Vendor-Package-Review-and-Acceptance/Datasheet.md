# Datasheet — DEL-073-06 EPC Vendor Package Review and Acceptance (PKG-073 Amine Treating Unit)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-073-06_epc-vendor-package-review-and-acceptance | `_CONTEXT.md` |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| Parent Package | PKG-073 Amine Treating Unit | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-073 |
| Workbook Row | 49 | `PACKAGE_REGISTER.csv` row PKG-073 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Tracking Number | 26020-01-27-001 | `PACKAGE_REGISTER.csv` |
| CoA Tracking | 26020-01-PT-27-001 — Amine Treating Unit | `PACKAGE_REGISTER.csv` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-073-06 |
| Deliverable Type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Source Basis (Word) | 26020-Package_Requirements.docx package heading 27 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (binary; clause-level text not locally accessible — `location TBD`) |
| Source Basis (Workbook) | 26020-Packages_Interfaces_4_export.xlsx, Packages row 49 | `PACKAGE_REGISTER.csv` |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_CONTEXT.md`; `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Review Function | EPC Integrator review, integration acceptance, and handoff readiness of the Package Vendor scope against the EPC Scope of Work (DEL-073-01), Package Datasheet (DEL-073-02), and Construction Work Package (DEL-073-03) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-073-06 |
| Upstream Vendor Deliverables Reviewed | DEL-073-04 Vendor Engineered Equipment Package; DEL-073-05 Vendor Document Turnover Package | `DELIVERABLE_REGISTER.csv` rows DEL-073-04, DEL-073-05 |
| Acceptance Frame | Verification that vendor package satisfies SOW (SOW-0051..SOW-0054) and supports facility-level integration | `SCOPE_LEDGER.csv` SOW-0051..SOW-0054; `_CONTEXT.md` |
| Vendor Ownership Boundary | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` row PKG-073; OBJ-004 |
| EPC Integrator Ownership Boundary | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration; review and acceptance of vendor package | `PACKAGE_REGISTER.csv` row PKG-073; OBJ-004 |
| Supported Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_REGISTER.csv` |
| Scope Coverage | SOW-0051, SOW-0052, SOW-0053, SOW-0054 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour natural gas (H₂S, CO₂) treated via continuous MDEA absorption-regeneration across two modules | `PACKAGE_REGISTER.csv` row PKG-073; `SCOPE_LEDGER.csv` SOW-0052 |
| Coordination Mode | DECLARED (no upstream/downstream edges declared at PREPARATION) | `_DEPENDENCIES.md` |
| Review Scope Boundary | Limited to vendor package conformance and facility integration acceptance; does not redo vendor engineering | `PACKAGE_REGISTER.csv` row PKG-073 (vendor/EPC split); OBJ-004 |
| Interface Set Reviewed | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-073 rows |
| Acceptance Threshold | Vendor package documentation and physical equipment package suitable for facility integration and downstream construction/commissioning; explicit thresholds for quantitative acceptance are `TBD` | `_CONTEXT.md`; clause-level source `location TBD` |
| Closure Condition | Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and controlled open-item closure evidence | OBJ-010 |

## Construction

### Anticipated Artifacts (this deliverable produces)

| Artifact | Description | Source |
|---|---|---|
| ART-B556C47357 | Vendor document review and comment log | `ARTIFACT_REGISTER.csv` |
| ART-0C77AD875E | Vendor package acceptance and turnover checklist | `ARTIFACT_REGISTER.csv` |
| ART-C9A6D6903F | Factory/shop test and inspection evidence | `ARTIFACT_REGISTER.csv` |
| Turnover evidence | Compiled handoff record (acceptance, open-item disposition, transferred documents) | `_CONTEXT.md`; OBJ-010 |

### Review Targets (deliverables under acceptance)

| Target | Description | Source |
|---|---|---|
| DEL-073-01 Scope of Work | EPC Scope of Work used as conformance baseline | `DELIVERABLE_REGISTER.csv` |
| DEL-073-02 Package Datasheet | Package Datasheet used as conformance baseline | `DELIVERABLE_REGISTER.csv` |
| DEL-073-03 Construction Work Package | Construction Work Package used as facility-integration baseline | `DELIVERABLE_REGISTER.csv` |
| DEL-073-04 Vendor Engineered Equipment Package | Vendor-owned engineering/design/equipment package under review | `DELIVERABLE_REGISTER.csv` |
| DEL-073-05 Vendor Document Turnover Package | Vendor document register, submittals, and turnover records under review | `DELIVERABLE_REGISTER.csv` |

### By Others (excluded from EPC acceptance scope)

| Item | Source |
|---|---|
| Vendor package engineering, design, fabrication, and documentation production (owned by Package Vendor in DEL-073-04, DEL-073-05) | `PACKAGE_REGISTER.csv` row PKG-073; OBJ-004 |
| Authoring of SOW/Datasheet/CWP (those are the upstream EPC deliverables, not produced here) | `DELIVERABLE_REGISTER.csv` rows DEL-073-01..03 |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- `_DEPENDENCIES.md` (this deliverable; DECLARED mode, no edges)
- GATE-07 PROJECT_DECOMP snapshot:
  - `PACKAGE_REGISTER.csv` row PKG-073
  - `DELIVERABLE_REGISTER.csv` row DEL-073-06_epc-vendor-package-review-and-acceptance
  - `SCOPE_LEDGER.csv` rows SOW-0051..SOW-0054
  - `INTERFACE_REGISTER.csv` PKG-073 rows
  - `ARTIFACT_REGISTER.csv` rows ART-B556C47357, ART-0C77AD875E, ART-C9A6D6903F
  - `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-003..OBJ-010
- Source workbook: `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; consumed via decomposition extract)
- Source Word doc: `_Sources/26020-Package_Requirements.docx` package heading 27 (binary; clause-level text not locally accessible in markdown form — `location TBD` for direct quotations)
