# Specification: DEL-029-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC Integrator's review and acceptance of the Package Vendor deliverable set for `PKG-029`, the Transformer TXP-8600-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 2.5 MVA 13.8 kV / 600 / 347 V package. The deliverable produces the acceptance evidence required for handoff readiness against the EPC Scope of Work (`DEL-029-01`), the Package Datasheet (`DEL-029-02` family), and the Construction Work Package for `PKG-029`.

`PKG-029` is a vendor-owned Electrical package under WBS 01 with CoA tracking 26020-01-30-020. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are not authored by this deliverable. They are received and reviewed.
- Project-level commissioning system test plans beyond package boundaries are excluded unless explicitly required by the Construction Work Package.
- Package-specific transformer ratings, impedance, vector group, BIL, cooling class, tap configuration, neutral treatment, secondary 347 V utilization scheme, weight, and physical envelope are `TBD` until vendor data is received; this deliverable evaluates rather than originates those values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-029-06-001 | The acceptance review shall confirm vendor submittals reflect package identity `PKG-029`, workbook row 31, WBS 01, CoA 26020-01-30-020, tag TXP-8600-1, 2.5 MVA, 13.8 kV / 600 / 347 V. Source: `PACKAGE_REGISTER.csv`; `_CONTEXT.md`. | Identity check against Gate 7 `PACKAGE_REGISTER.csv` row for `PKG-029`. |
| REQ-029-06-002 | The acceptance review shall preserve the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv`. | Responsibility wording check vs. `PACKAGE_REGISTER.csv`. |
| REQ-029-06-003 | The acceptance review shall verify each interface listed for `PKG-029` is addressed by the vendor submittal set: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: `INTERFACE_REGISTER.csv`. | Interface coverage check vs. `INTERFACE_REGISTER.csv` rows for `PKG-029`. |
| REQ-029-06-004 | The acceptance review shall confirm vendor design respects facility primary supply at 13.8 kV from the plant 13.8 kV switchgear and secondary 600 V high-resistance grounding (5 A continuous resistor). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical Power System; §System Voltages; §System Grounding. | Source citation check; discrepancies recorded as findings. |
| REQ-029-06-005 | The acceptance review shall confirm physical installation aligns with DBM transformer rules: CEC spacing for oil-filled transformers (if applicable), structural steel transformer base, foundation general approach on precast concrete bearing, and containment review. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Transformers; foundations table. | Layout/foundation submittal review against DBM clauses. |
| REQ-029-06-006 | The acceptance review shall confirm grounding evidence demonstrates two ground-grid connection points, ground well provisions for major equipment, and a dedicated copper ground conductor for distribution transformers per CEC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §System Grounding. | Grounding submittal and as-installed test record review. |
| REQ-029-06-007 | The acceptance review shall produce the four anticipated artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence. Source: `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md`. | Artifact presence check at deliverable closeout. |
| REQ-029-06-008 | The acceptance review shall declare unresolved values as `TBD` rather than inventing values where vendor submittals are silent or accessible sources do not support them. Source: `_REFERENCES.md`; this specification's exclusions. | Source-fidelity review; gap items raised as findings. |
| REQ-029-06-009 | The acceptance review shall record any disagreement between vendor submittals and EPC SOW / Package Datasheet / Construction Work Package as a documented finding with disposition; binding acceptance is reserved to human authority (K-AUTH-1). | Finding log review at closeout. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Spacing, grounding, conduit support, and installation basis for distribution transformers and electrical equipment. | Applicable; clause locations TBD. |
| Project electrical specifications (referenced by DBM) | Voltage, MCC, grounding, cable, raceway basis for the facility. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment installation classification (hazardous vs non-hazardous). Package-specific area classification not stated in accessible sources. | Applicable; package classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted upstream decomposition basis for package identity, interface set, and deliverable framing. | Authoritative upstream snapshot. |
| Vendor / IEEE / CSA transformer standards (e.g., IEEE C57 family, CSA C9/C802 family) | Applicable to distribution transformer design, ratings, and testing; specific governing standards depend on vendor submittal and project specification. | ASSUMPTION: likely applicable; not asserted as binding without source confirmation. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare vendor submittals to `PACKAGE_REGISTER.csv` row for `PKG-029`. | Identity matches accepted Gate 7 values. |
| Interface completeness | Compare submittal coverage to `INTERFACE_REGISTER.csv` rows for `PKG-029`. | All seven interface rows are addressed or explicitly waived with finding. |
| Source fidelity | Check each acceptance assertion against cited DBM source slices and registers. | Unsupported values are `TBD` or `ASSUMPTION`; not asserted as binding requirements. |
| Responsibility split | Compare submittal scope to `PACKAGE_REGISTER.csv` responsibility wording. | Vendor and EPC scopes are not conflated. |
| Artifact completeness | Confirm the four anticipated artifacts exist at acceptance closeout. | All artifacts present or finding logged. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure of this deliverable use the same identity, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Human ruling | Binding acceptance requires human approval per K-AUTH-1. | Agent proposes; human decides. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document review log.
- Package acceptance checklist mapping EPC SOW / Package Datasheet / Construction Work Package requirements to acceptance status.
- Test/inspection evidence (factory and/or site).
- Turnover evidence for handoff to operations/commissioning.
- Findings log capturing TBD/conflict items raised during review.
