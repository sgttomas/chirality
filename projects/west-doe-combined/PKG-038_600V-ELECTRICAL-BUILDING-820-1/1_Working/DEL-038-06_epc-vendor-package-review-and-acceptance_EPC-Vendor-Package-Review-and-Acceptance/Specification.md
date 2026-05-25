# Specification: DEL-038-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC-Integrator-led deliverable that reviews the Package Vendor's documentation for `PKG-038` (600V ELECTRICAL BUILDING (820-1)), confirms integration acceptance against the EPC Scope of Work (`DEL-038-01`) and the `DEL-038-02` Package Datasheet, and produces handoff-readiness evidence aligned with the Construction Work Package (`DEL-038-03`).

In scope:

- Vendor document review against the accepted Package Datasheet and the EPC Scope of Work.
- Verification that the twelve applicable package interfaces (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) are addressed in vendor documentation and the integration design.
- Acceptance evidence collection: review log, acceptance checklist, test/inspection records, turnover records.
- Status transitions for this deliverable per the safe-update rule.

Out of scope:

- Vendor-internal package engineering and detailed design (owned by the Package Vendor per `PACKAGE_REGISTER.csv` row `PKG-038`).
- Re-derivation of 600V building lineup configuration, distribution/MCC/panelboard selection, protective scheme, bus rating, short-circuit interrupting rating, HVAC capacity, fire & gas configuration, or structural/foundation design — these are vendor outputs and remain `TBD` at the package-decomposition level until vendor data is received.
- Modification of the Gate 7 PROJECT_DECOMP snapshot or any other deliverable's metadata.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-038-06-001 | The deliverable shall identify `PKG-038`, workbook row 40, WBS 01, CoA tracking number 26020-01-30-029, discipline Electrical, and package name "600V ELECTRICAL BUILDING (820-1)", and shall reference `DEL-038-02_package-datasheet` as the accepted EPC handoff basis and `DEL-038-01_scope-of-work` as the EPC SoW basis. Source: `PACKAGE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv`. | Identity field review against Gate 7 registers and `_CONTEXT.md`. |
| REQ-038-06-002 | The deliverable shall produce a vendor document review log enumerating each received vendor document, its revision, the reviewer, the disposition (Accepted / Accepted with comments / Rejected / Hold), and a pointer to the EPC SoW or Package Datasheet clause it satisfies. Source: anticipated artifacts in `_CONTEXT.md`. | Inspection of the review log; sampled traceability to EPC SoW / Datasheet items. ASSUMPTION: log shape, pending EPC procedure confirmation. |
| REQ-038-06-003 | The deliverable shall produce a package acceptance checklist that confirms each of the twelve package interfaces is addressed by vendor documentation and the integration design: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: `INTERFACE_REGISTER.csv` rows for `PKG-038`. | Checklist inspection against `INTERFACE_REGISTER.csv`. |
| REQ-038-06-004 | The deliverable shall preserve the accepted responsibility split: Package Vendor for package engineering/design/documentation/equipment; EPC Integrator for facility-level integration. The acceptance evidence shall not impose vendor design choices not stated in the EPC SoW or Package Datasheet. Source: `PACKAGE_REGISTER.csv` row `PKG-038`. | Review-log and checklist language audit; cross-check against `PACKAGE_REGISTER.csv`. |
| REQ-038-06-005 | The deliverable shall capture test and inspection evidence (Factory Acceptance Test, Site Acceptance Test, building/equipment commissioning checks, dielectric/insulation testing, breaker timing/operation, grounding/bonding verification, lighting verification, fire & gas integration test, HVAC commissioning, and — when EPC SoW requires — arc-flash labeling and short-circuit/coordination study compliance) referenced by the Package Datasheet and EPC SoW. When the EPC SoW clause set is not accessible, the requirement shall record the evidence categories as expected and mark specific test acceptance criteria as `TBD`. Source: anticipated artifacts; `_REFERENCES.md`; `PACKAGE_REGISTER.csv`. ASSUMPTION: FAT/SAT, commissioning, and arc-flash scope pending EPC procedure confirmation. | Evidence-file inventory check; mapping to EPC SoW clauses (`TBD` allowed). |
| REQ-038-06-006 | The deliverable shall capture turnover evidence aligned with the Construction Work Package for `PKG-038` (`DEL-038-03`), including mechanical-complete, energization-readiness, and handover-to-operations transitions. When the Construction Work Package content is not accessible at acceptance-criteria fidelity, the requirement shall enumerate the transition categories and mark category-specific criteria as `TBD`. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. | Turnover-evidence inventory check; mapping to Construction Work Package transitions (`TBD` allowed). |
| REQ-038-06-007 | The deliverable shall record any vendor document or integration item that is not yet accepted as a `NEEDS_HUMAN_RULING` or `TBD` item, including the reason and the source artifact, rather than recording silent acceptance. Source: skill contract `four-documents`; QA expectations. | Run-record review; cross-check against review-log dispositions. |
| REQ-038-06-008 | The deliverable shall not modify the Gate 7 PROJECT_DECOMP snapshot, the upstream `DEL-038-02` Datasheet, the upstream `DEL-038-01` Scope of Work, or any deliverable-local metadata file other than its own `_STATUS.md` per the safe-update rule. Source: `four-documents/SKILL.md`; TASK shell write boundary. | Post-run scope audit. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| EPC Scope of Work for `PKG-038` (`DEL-038-01` in-project; external SoW reference) | Authoritative acceptance basis for vendor-package integration. | Applicable; in-project draft status per `DEL-038-01/_STATUS.md`; external SoW document location `TBD`. |
| Package Datasheet `DEL-038-02` | Accepted technical handoff basis. | Applicable; in-project draft, status per `DEL-038-02/_STATUS.md`. |
| Construction Work Package `DEL-038-03` | Authoritative basis for turnover/handover acceptance. | Applicable; in-project, status per `DEL-038-03/_STATUS.md`. |
| Canadian Electrical Code (CEC) | Electrical installation, grounding, conduit, and equipment basis referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| IEEE/NEMA low-voltage switchgear, MCC, and panelboard standards | Likely-applicable for 600V-class distribution equipment basis. | ASSUMPTION (likely applicable); clause locations `TBD` until EPC SoW confirms. |
| IEEE 1584 / CSA Z462 (arc flash) | Likely-applicable arc-flash hazard analysis and labeling basis for 600V distribution equipment acceptance. | ASSUMPTION (likely applicable); clause locations `TBD` until EPC SoW confirms. |
| NFPA / NBCC fire and life-safety standards | Likely-applicable for electrical-building fire & gas / safety system integration. | ASSUMPTION (likely applicable); clause locations `TBD` until EPC SoW confirms. |
| Project electrical specifications | Voltage/distribution/grounding/cable/raceway basis referenced by the DBM electrical section. | Applicable; document location `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, interface facts, and objective traceability. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare identity fields to `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. | Identity fields match accepted source spelling and IDs. |
| Interface coverage | Compare acceptance checklist entries to `INTERFACE_REGISTER.csv` rows for `PKG-038`. | All twelve interfaces appear with disposition. |
| Responsibility integrity | Audit review log and checklist language against `PACKAGE_REGISTER.csv` row `PKG-038` responsibility text. | Vendor-owned and EPC-owned scopes are not conflated. |
| Source fidelity | For every non-trivial acceptance criterion, cite the EPC SoW clause, the Package Datasheet section, or mark `TBD`. | No invented acceptance criteria; gaps surfaced as `TBD`. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same identity, interface list, responsibility model, and `TBD` set. | No unresolved internal inconsistency. |
| Status-rule compliance | Confirm `_STATUS.md` is only modified per the safe-update rule and `OPEN → INITIALIZED` is the only transition this run may perform. | `_STATUS.md` history line matches the safe-update rule. |

## Documentation

The deliverable shall produce or preserve the following artifacts inside this folder:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (the four-document kit).
- Vendor document review log (artifact shape `TBD` until EPC procedure is confirmed).
- Package acceptance checklist (one entry per interface and per acceptance category).
- Test/inspection evidence inventory (FAT, SAT, commissioning, insulation, breaker timing, grounding, lighting, fire & gas, HVAC, arc-flash labeling when required — categories enumerated even when EPC SoW criteria are `TBD`).
- Turnover evidence inventory (mechanical-complete, energization-readiness, handover-to-operations — categories enumerated even when Construction Work Package criteria are `TBD`).
- `_STATUS.md` history entry for any state change made by this run.
- `_run_records/TASK_RUN_*.md` for this run.

References shall include: this deliverable's `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, the Gate 7 PROJECT_DECOMP snapshot registers, the companion Package Datasheet `DEL-038-02`, the companion Construction Work Package `DEL-038-03`, the companion Scope of Work `DEL-038-01`, and (when accessible) the EPC Scope of Work external reference and vendor data package for `PKG-038`.
