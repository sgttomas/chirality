# Specification: DEL-008-01_scope-of-work — Scope of Work

## Scope

This specification governs the contents of the EPC Scope of Work for `DEL-008-01_scope-of-work`, covering the full `PKG-008` Controls system design and integration package under WBS 01.

The deliverable shall cover:

- Package scope of work.
- Tagged equipment and package identity list.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.

The deliverable shall identify the Controls package basis from Workbook Packages row 9 and the Gate 7 final published PROJECT_DECOMP snapshot. It shall not create a separate controls power-panel package or deliverable, because Gate 6 disposition records those items as interface facts/artifacts under the package datasheet.

Exclusions:

- Package-specific exclusions are TBD; no package-specific exclusions are stated in the Gate 7 package register.
- Detailed discipline requirements are TBD where the accepted snapshot states that detailed non-vendor package deliverable requirements are source-limited.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-008-01-001 | The Scope of Work shall identify DEL-008-01, PKG-008, package name, WBS 01, workbook ID 8, workbook row 9, CoA tracking number 26020-01-32-001, discipline Controls, responsible party EPC Integrator, and scope item SOW-0008. Source: _CONTEXT.md; PACKAGE_REGISTER.csv, PKG-008; DELIVERABLE_REGISTER.csv, DEL-008-01. | Verify identification table against _CONTEXT.md and Gate 7 registers. |
| REQ-008-01-002 | The Scope of Work shall describe the package as a workbook-defined Controls package for controls system design and integration under WBS 01 with recorded physical interfaces. Source: PACKAGE_REGISTER.csv, PKG-008. | Verify wording against PACKAGE_REGISTER.csv. |
| REQ-008-01-003 | The Scope of Work shall include the anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. Source: _CONTEXT.md; DELIVERABLE_REGISTER.csv, DEL-008-01; ARTIFACT_REGISTER.csv rows 100-103. | Verify artifact list against _CONTEXT.md and ARTIFACT_REGISTER.csv. |
| REQ-008-01-004 | The Scope of Work shall address the declared PKG-008 interface types: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. Source: PACKAGE_REGISTER.csv, PKG-008; INTERFACE_REGISTER.csv, PKG-008. | Verify each interface type is named in the interface/boundary section. |
| REQ-008-01-005 | The Scope of Work shall record that controls power-panel interfaces remain interface facts/artifacts under the package datasheet and that no separate package or deliverable is created. Source: INTERFACE_REGISTER.csv, PKG-008; ARTIFACT_REGISTER.csv rows for DEL-008-02 interface facts. | Verify the interface review note is preserved without converting it into a new deliverable. |
| REQ-008-01-006 | The Scope of Work shall state that the responsibility model is source-dependent and that no separate vendor-package ownership model is inferred from current sources. Source: PACKAGE_REGISTER.csv, PKG-008. | Verify responsibility assignment wording against PACKAGE_REGISTER.csv. |
| REQ-008-01-007 | The Scope of Work shall mark missing exclusions, detailed design values, tagged equipment details beyond package identity, and clause-level controls requirements as TBD unless supported by accepted snapshot data. Source: _REFERENCES.md; PACKAGE_REGISTER.csv, PKG-008. | Verify unsupported detail is not invented. |

## Standards

| Standard / source | Status | Use |
|---|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Accessible and accepted upstream truth. | Governs package, deliverable, artifact, objective, and interface basis for this Phase 2.2 run. |
| Workbook Packages row 9 | Referenced by the accepted snapshot; raw workbook not reinterpreted in this run. | Source reference for PKG-008 identity and interface basis as accepted by Gate 7. |
| DBM-Deepcut/4-25_Deepcut_DBM.md | Referenced by Gate 7 for PKG-008 and associated objectives; raw source corpus not reinterpreted per runtime instruction. | Context reference only through accepted Gate 7 snapshot unless later source-verification workflow is authorized. |
| Controls, instrumentation, fire/gas, shutdown, communications, and electrical codes/standards | TBD. | Clause-level standards cannot be specified from the accepted snapshot alone. |

## Verification

Verification shall include:

- Cross-check identity and source basis against _CONTEXT.md, DELIVERABLE_REGISTER.csv, and PACKAGE_REGISTER.csv.
- Cross-check interface names against PACKAGE_REGISTER.csv and INTERFACE_REGISTER.csv for PKG-008.
- Confirm all anticipated artifacts from ARTIFACT_REGISTER.csv rows for DEL-008-01 are represented.
- Confirm that unsupported technical values and detailed controls requirements are marked TBD.
- Confirm the Scope of Work does not create separate deliverables for controls power-panel interfaces.

## Documentation

The completed Scope of Work package shall retain or produce:

- Package scope of work.
- Tagged equipment and package identity list.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.
- Source/reference list identifying the Gate 7 snapshot and applicable register rows.
- TBD/open-item list for source-limited controls requirements, exclusions, and detailed technical data.
