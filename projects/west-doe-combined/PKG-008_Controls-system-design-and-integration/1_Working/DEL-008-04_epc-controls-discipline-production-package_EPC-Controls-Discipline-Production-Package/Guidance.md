# Guidance: EPC / Controls Discipline Production Package

## Purpose

This guidance explains how to use DEL-008-04 as a source-limited controls discipline production package for PKG-008. The package exists to carry the accepted Gate 7 controls scope into discipline production without inventing detailed non-vendor controls deliverables that are not present in the current source set.

## Principles

- Treat Gate 7 registers as accepted decomposition truth for package identity, deliverable identity, scope item SOW-0008, objectives, and PKG-008 interface facts.
- Treat the workbook Packages row 9 and DBM controls sections as the accessible source basis for controls discipline content.
- Keep detailed-design decisions open where the DBM marks them as TBD or final design items.
- Carry controls power-panel interfaces as interface facts/artifacts under the package basis; do not split them into a new package or deliverable without human/project authority.
- Use the controls DBM basis for architecture, network, controller, Remote I/O, Modbus, and safety-interface requirements.

## Considerations

The production package should be conservative. Gate 7 states that detailed non-vendor package deliverable requirements are source-limited and remain open for Gate 5 disposition. That means the discipline deliverable register should be treated as a required artifact but not populated with unsupported internal deliverable names.

The DBM gives enough controls source basis to define architecture and verification hooks, including central control room operation, packaged-equipment monitoring, PCN/IDMZ/I/O/controller networks, Allen-Bradley controller and Remote I/O basis, Propak/FactoryTalk configuration basis, Modbus restrictions, and safety-device Remote I/O interfaces. It does not fully resolve final cabinet locations, controller sizing, DLR versus PRP selection, final package data maps, permissive logic, trip interfaces, or alarm priorities.

The 3-25 and 4-25 DBM controls sections are not identical in every detail. For this DEL-008-04 package, the 4-25 Deepcut SEC-13 basis is the primary cited controls source because the accepted PKG-008 package row cites DBM-Deepcut. The 3-25 SEC-13 section is used only as supporting context where it states shared controls/interface behavior.

## Trade-offs

| Topic | Conservative handling |
|---|---|
| Discipline deliverable register | Mark as TBD until the responsible controls authority enumerates required drawings, calculations, configuration files, FAT/SAT records, and turnover documents. |
| PRP versus DLR | Preserve as detailed-design selection unless a later approved source fixes the topology. |
| Controller redundancy | Use the 4-25 Deepcut basis for PKG-008 and record any cross-facility differences as a source-context issue instead of forcing one answer globally. |
| Package controls | Require integration of standalone unit control systems into the BPCS HMI where source-supported; keep final data maps and logic as detailed-design items. |
| Modbus | Use for monitoring/data collection only; do not imply process control over Modbus. |

## Examples

- Source-supported requirement: "Modbus data shall be used for monitoring and data collection only." Source: `4-25_Deepcut_DBM.md`, SEC-13 Modbus Data Basis.
- Source-supported open item: "Remote I/O cabinet locations shall be determined during detailed design." Source: `4-25_Deepcut_DBM.md`, SEC-13 Physical Layout and Equipment Placement and open design development table.
- Unsupported detail to avoid inventing: a complete controls drawing index for DEL-008-04. Current source set identifies a TBD discipline deliverable register but does not enumerate it.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-001 | Detailed internal deliverable list for DEL-008-04 is required as an anticipated artifact, but current accepted sources do not enumerate it. | `_CONTEXT.md`, Anticipated Artifacts; Gate 7 `DELIVERABLE_REGISTER.csv` DEL-008-04 | Available source set, no enumerated controls discipline deliverable register found | Datasheet Construction; Specification Documentation; Procedure Records | Treat the register as TBD and require responsible controls authority/Gate 5 disposition before closure. | TBD |
| HRR-002 | 4-25 DBM states the process control system uses redundant controller configuration; 3-25 DBM states BPCS is simplex in the current basis. | `4-25_Deepcut_DBM.md`, SEC-13 Controls System Hardware | `3-25_Comp_and_Liquids_DBM.md`, SEC-13 BPCS and Remote I/O | Datasheet Attributes; Specification REQ-008; Procedure verification | Use 4-25 Deepcut SEC-13 for PKG-008 because Gate 7 `PACKAGE_REGISTER.csv` cites DBM-Deepcut for PKG-008; retain 3-25 as supporting shared-interface context only. | TBD |
