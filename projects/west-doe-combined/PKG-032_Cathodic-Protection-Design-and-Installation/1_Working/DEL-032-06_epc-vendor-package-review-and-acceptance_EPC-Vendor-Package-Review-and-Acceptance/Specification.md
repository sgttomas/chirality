# Specification: DEL-032-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC Integrator-led vendor package review, integration acceptance, and handoff-readiness evidence for `PKG-032`, the Cathodic Protection Design and Installation package. It is a Gate 5 EPC integrator deliverable that evaluates vendor outputs against the EPC Scope of Work (`DEL-032-01`), Package Datasheet (`DEL-032-02`), and Construction Work Package (`DEL-032-03`), and accepts vendor engineered equipment (`DEL-032-04`) and vendor document turnover (`DEL-032-05`) into the facility.

Exclusions:

- Cathodic protection engineering and supply are excluded from facility design scope; acceptance shall not re-import vendor CP engineering into the facility design responsibility.
- Detailed CP design values (anode bed sizing, rectifier rating, current density, coating allowances, test-station design) are vendor/owner-defined and not produced here; their acceptance is evidence review, not re-engineering.
- Vendor detailed design calculations, certified drawings, and final equipment selections are reviewed as submitted; this deliverable does not re-derive them.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-032-06-001 | The acceptance deliverable shall identify `PKG-032`, workbook row 34, WBS 03, CoA tracking number 26020-03-30-023, discipline Electrical, and package name "Cathodic Protection Design and Installation." Source: Workbook Packages row 34; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-032-06-002 | The acceptance deliverable shall preserve the package responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. Source: `PACKAGE_REGISTER.csv` row `PKG-032`. | Responsibility review; no conflation of vendor design with EPC facility design scope. |
| REQ-032-06-003 | The acceptance deliverable shall produce a vendor document review log capturing each vendor submittal under `DEL-032-05`, its review status, comment disposition, and EPC integration acceptance decision. Source: `ARTIFACT_REGISTER.csv` rows `ART-581D762C15`, `ART-A82FC3C3ED`; `_CONTEXT.md` anticipated artifacts. | Review log completeness check against the vendor document register. |
| REQ-032-06-004 | The acceptance deliverable shall produce a package acceptance and turnover checklist that evidences acceptance of `DEL-032-04` (vendor engineered equipment package) and `DEL-032-05` (vendor document turnover package) into the facility. Source: `ARTIFACT_REGISTER.csv` row `ART-43C50697CD`. | Checklist closure review; every item is dispositioned or carried as a TBD with owner. |
| REQ-032-06-005 | The acceptance deliverable shall include all four applicable PKG-032 interface facts (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network) and confirm vendor compliance with each. Source: Workbook Packages row 34; `INTERFACE_REGISTER.csv` rows `IFC-C2719906C1`, `IFC-F1FE9DF9DD`, `IFC-4D092EC70F`, `IFC-8594557BD3`. | Interface matrix check; per-interface acceptance status recorded. |
| REQ-032-06-006 | The acceptance deliverable shall verify that vendor grounding and bonding submittals do not create stray-current paths that defeat the cathodic protection of buried/immersed steel and shall coordinate with facility grounding basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs and section "Cathodic Protection". | Electrical interface review with grounding/CP coordination evidence. |
| REQ-032-06-007 | The acceptance deliverable shall capture factory/shop test and inspection evidence as turnover evidence, with each accepted test traceable to a vendor submittal. Source: `ARTIFACT_REGISTER.csv` row `ART-B84E5EEC19`. | Test/inspection traceability review. |
| REQ-032-06-008 | The acceptance deliverable shall confirm that the facility-design exclusion of cathodic-protection engineering and supply is preserved and that vendor-supplied engineering remains the owner/vendor responsibility under EPC integration only. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, section "Cathodic Protection". | Scope-boundary review against DBM exclusion text. |
| REQ-032-06-009 | The acceptance deliverable shall mark vendor-detail values, vendor-document register entries, and vendor test lists as `TBD` when not present in accessible source material rather than inventing acceptance criteria. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Source-fidelity / TBD-handling review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Governs electrical installation, grounding, and bonding referenced in the DBM electrical section that the acceptance review must respect when accepting vendor electrical submittals. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Govern voltage, grounding, cable, and raceway basis referenced by the DBM electrical section. | Applicable; document location TBD. |
| Owner cathodic-protection standard / specification | Governs vendor CP engineering, materials, and test methods; the facility design supports owner CP interfaces only. | Applicable; owner-issued document required; not present locally — `location TBD`. |
| Area classification standards | Apply to electrical equipment placement and conduit sealing where vendor equipment is installed. | Applicable; package-specific classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, interface facts, and objective associations. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare acceptance deliverable identity to workbook row 34 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Vendor document review log completeness | Compare review log entries to the vendor document register and submittal list. | Every submittal has a status, disposition, and decision. |
| Acceptance checklist closure | Verify each checklist item is dispositioned (accept, reject with comment, accept with reservation, or TBD with owner). | No silent acceptance of incomplete vendor content. |
| Interface acceptance | Compare per-interface acceptance to `INTERFACE_REGISTER.csv` rows for `PKG-032`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network are each evaluated. |
| Scope boundary preservation | Confirm acceptance language does not transfer CP engineering or supply into facility design scope. | DBM exclusion text is honored. |
| Test/inspection traceability | Confirm each accepted test/inspection maps to a vendor submittal or source-supported requirement. | No accepted test without traceable basis. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package IDs, interfaces, exclusions, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document review and comment log (`ART-581D762C15`).
- Vendor package acceptance and turnover checklist (`ART-43C50697CD`).
- Factory/shop test and inspection evidence (`ART-B84E5EEC19`).
- Source-gap / `TBD` list for vendor or owner resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 34, applicable Gate 7 registers, and the DBM cathodic-protection and electrical source slices used for scope boundary, interface, and grounding coordination.
