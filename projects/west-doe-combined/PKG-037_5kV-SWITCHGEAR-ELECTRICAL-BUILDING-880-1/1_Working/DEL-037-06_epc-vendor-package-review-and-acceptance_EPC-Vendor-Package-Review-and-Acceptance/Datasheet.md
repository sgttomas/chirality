# Datasheet: DEL-037-06 — EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-037-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-037` |
| PackageName | 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) |
| Discipline | Electrical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| CoversScopeItems | `SOW-0038` |
| SupportsObjectives | `OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010` |

Source: `DELIVERABLE_REGISTER.csv` row 209 (Gate 7 snapshot); `PACKAGE_REGISTER.csv` row 39.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Acceptance scope | Vendor package review, integration acceptance, and handoff readiness against the EPC Scope of Work (`DEL-037-01`), Package Datasheet (`DEL-037-02`), and Construction Work Package (`DEL-037-03`). | `DELIVERABLE_REGISTER.csv` row 209 |
| Vendor production unit under review | `DEL-037-04` Vendor Engineered Equipment Package; `DEL-037-05` Vendor Document Turnover Package. | `DELIVERABLE_REGISTER.csv` rows 207-208 |
| Acceptance evidence artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row 209 |
| Interface scope (package-level) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` row 39 |
| Ownership split | Package Vendor owns package engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination. | `PACKAGE_REGISTER.csv` row 39 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Package class | Prefabricated, shop-fabricated modular Electrical Building. | DBM-Deepcut/4-25_Deepcut_DBM.md "Electrical Buildings" section |
| Building service voltage (package title) | 5 kV class switchgear (per workbook package title). The Gate 7 PACKAGE_REGISTER does not provide a 5 kV switchgear-specific design narrative; the DBM section "Electrical Buildings" lists 13.8 kV, 6.9 kV, 4.16 kV, and 600 V building variants only. | `PACKAGE_REGISTER.csv` row 39; DBM-Deepcut/4-25_Deepcut_DBM.md "Electrical Buildings" |
| HVAC redundancy basis (when applicable to building review) | n+1 HVAC sizing for electrical buildings. | DBM-Deepcut/4-25_Deepcut_DBM.md "Electrical Buildings" |
| Cable entry basis (when applicable to building review) | Bottom-entry cabling; elevated/piled building. | DBM-Deepcut/4-25_Deepcut_DBM.md "Electrical Buildings" |
| Package-specific exclusions | TBD (no package-specific exclusions stated in source materials). | `PACKAGE_REGISTER.csv` row 39 |

## Construction

| Item | Value | Source |
|---|---|---|
| Review-and-acceptance scope owner | EPC Integrator (lead). | `DELIVERABLE_REGISTER.csv` row 209 |
| Vendor input required | Package Vendor provides vendor documentation, test/inspection evidence, and turnover records for acceptance. | `DELIVERABLE_REGISTER.csv` rows 208-209 |
| Acceptance gate basis | Vendor package outputs must be assessed against EPC SOW (`DEL-037-01`), Package Datasheet (`DEL-037-02`), and Construction Work Package (`DEL-037-03`) before handoff. | `DELIVERABLE_REGISTER.csv` row 209 |
| Interface verification touchpoints | Each interface type listed under Attributes must have an acceptance entry confirming tie-in readiness with the facility. | `PACKAGE_REGISTER.csv` row 39 |

## References

- Gate 7 PROJECT_DECOMP final snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- `DELIVERABLE_REGISTER.csv` (Gate 7) row 209 — DEL-037-06
- `PACKAGE_REGISTER.csv` (Gate 7) row 39 — PKG-037
- `OBJECTIVE_DELIVERABLE_MAP.csv` (Gate 7)
- DBM-Deepcut source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections: Electrical Buildings; Grounding and Bonding; Cable, Wire, and Raceways)
- Companion deliverables: `DEL-037-01` SOW; `DEL-037-02` Package Datasheet; `DEL-037-03` Construction Work Package; `DEL-037-04` Vendor Engineered Equipment Package; `DEL-037-05` Vendor Document Turnover Package
