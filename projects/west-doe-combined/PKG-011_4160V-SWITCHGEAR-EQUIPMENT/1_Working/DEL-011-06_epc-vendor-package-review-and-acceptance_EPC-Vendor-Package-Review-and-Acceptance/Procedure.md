# Procedure: EPC Vendor Package Review and Acceptance

## Purpose

Define the bounded procedure for producing and using the DEL-011-06 EPC Vendor Package Review and Acceptance file for PKG-011, 4160V SWITCHGEAR EQUIPMENT.

## Prerequisites

- Gate 7 PROJECT_DECOMP snapshot accepted as upstream truth.
- DEL-011-06 `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` available.
- EPC Scope of Work, Package Datasheet, Construction Work Package, vendor documents, vendor test/inspection evidence, and turnover records available for review when produced.
- Declared upstream dependencies: none during PREPARATION.
- Declared downstream dependencies: none during PREPARATION.
- Source basis available for initial procedure: workbook row 13, Gate 7 registers, and DBM SEC-12 Electrical Basis.
- Package-specific vendor requirements, test procedures, inspection points, and turnover form templates: TBD.

## Steps

1. Confirm the acceptance file identity: DEL-011-06 for PKG-011, 4160V SWITCHGEAR EQUIPMENT, discipline Electrical, responsible party EPC Integrator with Package Vendor input.
2. Confirm the responsibility split from Gate 7: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment; EPC Integrator owns integration review and facility-level acceptance.
3. Compile the required acceptance artifacts:
   - Vendor document review and comment log.
   - Vendor package acceptance and turnover checklist.
   - Factory/shop test and inspection evidence.
   - Turnover evidence.
4. Review the vendor document log for status, comment disposition, accepted-with-comments items, and unresolved open items. Specific log fields are ASSUMPTION pending document-control template.
5. Review the acceptance checklist against each declared interface type:
   - Electrical Power.
   - Grounding / Bonding.
   - I&C / Control Cabling.
   - Communications / Network.
   - Maintenance Access.
   - Structural / Foundations / Supports.
6. Check vendor electrical and interface information against the DBM SEC-12 basis where applicable:
   - 4,160 V, 3 phase, 3 wire, 60 Hz LRG medium-voltage service.
   - 4160V MCC contactors, motor protection relays, and EtherNet communication to the plant PLC central control panel.
   - Separation of 13.8 kV, 4,160 V, and 600 V power circuits from control and instrument circuits by distance, shielding, or routing as required.
7. Record every missing vendor document, missing test/inspection record, unresolved interface point, or acceptance deviation as `TBD` or an open item with owner, due date, and disposition status. Owner/due-date fields are ASSUMPTION pending project open-item process.
8. Confirm turnover readiness only when required review evidence, interface evidence, test/inspection evidence, and open-item dispositions are present or explicitly accepted by the responsible reviewer.
9. Preserve the completed acceptance file as turnover evidence for downstream facility handoff.

## Verification

| Check | Acceptance result |
|---|---|
| Identity verified | DEL-011-06 / PKG-011 / 4160V SWITCHGEAR EQUIPMENT match Gate 7 and `_CONTEXT.md`. |
| Responsibility boundary verified | EPC acceptance does not assume Package Vendor engineering/design ownership. |
| Required artifacts present | Review log, acceptance checklist, test/inspection evidence, and turnover evidence are present or explicitly marked TBD/open. |
| Interfaces reviewed | All six declared PKG-011 interface types are checked or carried as open items. |
| Electrical basis checked | Applicable vendor data aligns with DBM SEC-12 or deviations/open items are recorded. |
| Open items controlled | Missing or unresolved evidence has owner and disposition status, or is marked TBD where the project form is unavailable. |

## Records

- Vendor document review and comment log.
- Vendor package acceptance and turnover checklist.
- Factory/shop test and inspection evidence.
- Turnover evidence.
- ASSUMPTION: Open-item / exception log for unresolved acceptance conditions.
- Human ruling record for HRR-011-06-001 when resolved.
