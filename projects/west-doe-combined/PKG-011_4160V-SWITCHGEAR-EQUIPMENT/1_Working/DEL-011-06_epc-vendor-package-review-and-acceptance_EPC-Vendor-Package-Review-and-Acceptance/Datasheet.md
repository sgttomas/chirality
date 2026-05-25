# Datasheet: EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-011-06_epc-vendor-package-review-and-acceptance |
| Deliverable name | EPC Vendor Package Review and Acceptance |
| Parent package | PKG-011 - 4160V SWITCHGEAR EQUIPMENT |
| Workbook row / ID | Row 13 / ID 11 |
| WBS | 02 |
| CoA tracking number | 26020-02-30-002 |
| Discipline | Electrical |
| Deliverable type | EPC Vendor Package Acceptance |
| Responsible party | EPC Integrator (lead) with Package Vendor input |
| Scope item | SOW-0012 |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: Gate 7 `PACKAGE_REGISTER.csv`, PKG-011. |
| Acceptance purpose | Review vendor documentation, confirm integration acceptance, and preserve handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package. Source: Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-011-06. |
| Required acceptance evidence | Vendor document review and comment log; vendor package acceptance and turnover checklist; factory/shop test and inspection evidence. Source: Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-06. |
| Declared interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: workbook row 13 in `26020-Packages_Interfaces_4_export.xlsx` and Gate 7 `INTERFACE_REGISTER.csv`, PKG-011. |
| Objective association | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010. Source: Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-011-06. |

## Conditions

| Condition | Source-grounded value |
|---|---|
| Facility electrical basis | Medium-voltage service is 4,160 V, 3 phase, 3 wire, 60 Hz LRG for process AC inverter-drive motors from 250 hp to 5,500 hp. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis, System Voltages. |
| 4160V MCC basis | The 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition; it serves large 4000V motors including KM-2150 and KM-2250. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis, 4160V MCC. |
| Power and controls separation | Power circuits at 13.8 kV, 4,160 V, and 600 V are to be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing. |
| Declared upstream dependencies | None declared during PREPARATION. Source: `_DEPENDENCIES.md`. |
| Declared downstream dependencies | None declared during PREPARATION. Source: `_DEPENDENCIES.md`. |

## Construction

| Item | Acceptance data needed |
|---|---|
| Vendor document review log | Document number, revision, review status, comment disposition, accepted-with-comments status, and unresolved open items. Source basis: Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-06; specific log fields are ASSUMPTION pending project document-control template. |
| Package acceptance checklist | Checklist linking vendor documents, package datasheet requirements, interface requirements, test evidence, turnover records, and open items. Source basis: Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-06; checklist line-item format is TBD. |
| Test/inspection evidence | Factory/shop test and inspection records for acceptance. Source basis: Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-06; required test names, hold points, and acceptance criteria are TBD because no package-specific vendor test procedure was available. |
| Turnover evidence | Turnover package confirming integration and handoff readiness. Source basis: Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-06; required turnover index is TBD. |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 13.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, DEL-011-06.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, PKG-011.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`, DEL-011-06.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`, PKG-011.
