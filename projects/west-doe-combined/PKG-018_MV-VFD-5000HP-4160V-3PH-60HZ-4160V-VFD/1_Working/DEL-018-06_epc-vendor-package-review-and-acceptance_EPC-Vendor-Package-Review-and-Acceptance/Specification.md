# Specification: DEL-018-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC-Integrator-led deliverable that reviews the Package Vendor's documentation for `PKG-018` (MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD), confirms integration acceptance against the EPC Scope of Work (`DEL-018-01`) and the `DEL-018-02` Package Datasheet, and produces handoff-readiness evidence aligned with the Construction Work Package (`DEL-018-03`).

In scope:

- Vendor document review against the accepted Package Datasheet and the EPC Scope of Work.
- Verification that the six applicable package interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are addressed in vendor documentation and the integration design.
- Verification that harmonic and reactive-power mitigation studies are addressed by the vendor or referenced to the EPC detailed-electrical-design package (per DBM SCA-001 VE #37 capacitor-bank removal on MCC-8200 where VFDs are present).
- Acceptance evidence collection: review log, acceptance checklist, test/inspection records, turnover records.
- Status transitions for the deliverable itself.

Out of scope:

- Vendor-internal package engineering and detailed design (owned by the Package Vendor per `PACKAGE_REGISTER.csv` row `PKG-018`).
- Re-derivation of VFD rating, topology, cooling, enclosure, harmonic-filter design, or transformer/reactor configuration — these are vendor outputs and are `TBD` at the package-decomposition level until vendor data is received.
- Modification of the Gate 7 PROJECT_DECOMP snapshot or any other deliverable's metadata.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-018-06-001 | The deliverable shall identify `PKG-018`, workbook row 20, WBS 02, CoA tracking number 26020-02-30-009, discipline Electrical, and package name "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD", and shall reference `DEL-018-01_scope-of-work` and `DEL-018-02_package-datasheet` as the accepted EPC handoff basis. Source: `PACKAGE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv`. | Identity field review against Gate 7 registers and `_CONTEXT.md`. |
| REQ-018-06-002 | The deliverable shall produce a vendor document review log enumerating each received vendor document, its revision, the reviewer, the disposition (Accepted / Accepted with comments / Rejected / Hold), and a pointer to the EPC SoW or Package Datasheet clause it satisfies. Source: anticipated artifacts in `_CONTEXT.md`. | Inspection of the review log; sampled traceability to EPC SoW / Datasheet items. ASSUMPTION: log shape, pending EPC procedure confirmation. |
| REQ-018-06-003 | The deliverable shall produce a package acceptance checklist that confirms each of the six package interfaces is addressed by vendor documentation and the integration design: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: `INTERFACE_REGISTER.csv` rows for `PKG-018`. | Checklist inspection against `INTERFACE_REGISTER.csv`. |
| REQ-018-06-004 | The deliverable shall preserve the accepted responsibility split: Package Vendor for package engineering/design/documentation/equipment; EPC Integrator for facility-level integration. The acceptance evidence shall not impose vendor design choices not stated in the EPC SoW or Package Datasheet. Source: `PACKAGE_REGISTER.csv` row `PKG-018`. | Review-log and checklist language audit; cross-check against `PACKAGE_REGISTER.csv`. |
| REQ-018-06-005 | The deliverable shall capture test and inspection evidence (Factory Acceptance Test, Site Acceptance Test, dielectric/withstand and protective-relay coordination checks, harmonic-distortion and reactive-power verification, control/communication interface checks, and grounding/bonding verification) referenced by the Package Datasheet and EPC SoW. When the EPC SoW clause set is not accessible, the requirement shall record the evidence categories as expected and mark specific test acceptance criteria as `TBD`. Source: anticipated artifacts; `_REFERENCES.md`; `PACKAGE_REGISTER.csv`; DBM compression/electrical context (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 326, 533, 752-760). ASSUMPTION: FAT/SAT scope pending EPC procedure confirmation. | Evidence-file inventory check; mapping to EPC SoW clauses (`TBD` allowed). |
| REQ-018-06-006 | The deliverable shall capture turnover evidence aligned with the Construction Work Package (`DEL-018-03`) for `PKG-018`, including mechanical-complete, energization-readiness, control-system-integration, and handover-to-operations transitions. When the Construction Work Package criteria are not yet accessible, the requirement shall enumerate the transition categories and mark category-specific criteria as `TBD`. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. | Turnover-evidence inventory check; mapping to Construction Work Package transitions (`TBD` allowed). |
| REQ-018-06-007 | The deliverable shall verify that vendor documentation addresses harmonic and reactive-power behavior of the VFD on the 4160V bus, consistent with the DBM constraint that capacitor banks are removed from the synchronous bus on MCC-8200 where VFDs are present (SCA-001 VE #37), and shall record the disposition (vendor-addressed, EPC-study-addressed, or `TBD`). Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 756-760. | Review-log audit for harmonic/reactive-power evidence; cross-check against DBM constraint. |
| REQ-018-06-008 | The deliverable shall record any vendor document or integration item that is not yet accepted as a `NEEDS_HUMAN_RULING` or `TBD` item, including the reason and the source artifact, rather than recording silent acceptance. Source: skill contract `four-documents`; QA expectations. | Run-record review; cross-check against review-log dispositions. |
| REQ-018-06-009 | The deliverable shall not modify the Gate 7 PROJECT_DECOMP snapshot, the upstream `DEL-018-01`/`DEL-018-02`/`DEL-018-03` artifacts, or any deliverable-local metadata file other than `_STATUS.md` per the safe-update rule. Source: `four-documents/SKILL.md`; TASK shell write boundary. | Post-run scope audit. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| EPC Scope of Work for `PKG-018` (`DEL-018-01`) | Authoritative acceptance basis for vendor-package integration. | Applicable; in-project draft per `DEL-018-01/_STATUS.md`; original SoW clause set `location TBD`. |
| Package Datasheet `DEL-018-02` | Accepted technical handoff basis. | Applicable; in-project draft, status per `DEL-018-02/_STATUS.md`. |
| Construction Work Package `DEL-018-03` | Authoritative basis for turnover/handover acceptance. | Applicable; in-project draft, status per `DEL-018-03/_STATUS.md`. |
| Canadian Electrical Code (CEC) | Electrical installation, grounding, conduit, and equipment basis referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| NEMA MG1 and IEEE inverter-duty motor practices | Motor basis (inverter-duty starting via VFD) per DBM motor description. | Applicable as background motor basis; specific clause-level requirements `TBD`. |
| Project electrical specifications (4160V MCC, harmonic and reactive-power study basis) | Voltage/MCC/grounding/cable/raceway basis and detailed-electrical-study basis referenced by the DBM electrical section. | Applicable; document location `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, interface facts, and objective traceability. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare identity fields to `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. | Identity fields match accepted source spelling and IDs. |
| Interface coverage | Compare acceptance checklist entries to `INTERFACE_REGISTER.csv` rows for `PKG-018`. | All six interfaces appear with disposition. |
| Responsibility integrity | Audit review log and checklist language against `PACKAGE_REGISTER.csv` row `PKG-018` responsibility text. | Vendor-owned and EPC-owned scopes are not conflated. |
| Harmonic/reactive-power coverage | Confirm REQ-018-06-007 evidence is recorded with explicit disposition. | Either vendor evidence, EPC-study reference, or explicit `TBD` is present. |
| Source fidelity | For every non-trivial acceptance criterion, cite the EPC SoW clause, the Package Datasheet section, the Construction Work Package section, or mark `TBD`. | No invented acceptance criteria; gaps surfaced as `TBD`. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same identity, interface list, responsibility model, and `TBD` set. | No unresolved internal inconsistency. |
| Status-rule compliance | Confirm `_STATUS.md` is only modified per the safe-update rule and `OPEN → INITIALIZED` is the only transition this run may perform. | `_STATUS.md` history line matches the safe-update rule. |

## Documentation

The deliverable shall produce or preserve the following artifacts inside this folder:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (the four-document kit).
- Vendor document review log (artifact shape `TBD` until EPC procedure is confirmed).
- Package acceptance checklist (one entry per interface and per acceptance category).
- Test/inspection evidence inventory (FAT, SAT, dielectric/protective-relay, harmonic/reactive, control/communication interface, grounding — categories enumerated even when EPC SoW criteria are `TBD`).
- Turnover evidence inventory (mechanical-complete, energization-readiness, control-system-integration, handover-to-operations — categories enumerated even when Construction Work Package criteria are `TBD`).
- `_STATUS.md` history entry for any state change made by this run.
- `_run_records/TASK_RUN_*.md` for this run.

References shall include: this deliverable's `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, the Gate 7 PROJECT_DECOMP snapshot registers, the companion deliverables (`DEL-018-01`, `DEL-018-02`, `DEL-018-03`, `DEL-018-04`, `DEL-018-05`), the DBM compression/electrical source, and (when accessible) the EPC Scope of Work and Construction Work Package clause sets for `PKG-018`.
