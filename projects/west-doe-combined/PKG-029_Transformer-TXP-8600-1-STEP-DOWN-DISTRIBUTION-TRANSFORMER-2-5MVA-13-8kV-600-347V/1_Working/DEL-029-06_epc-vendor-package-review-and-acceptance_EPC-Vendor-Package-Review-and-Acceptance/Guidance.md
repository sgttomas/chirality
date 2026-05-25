# Guidance: DEL-029-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable lets the EPC Integrator demonstrate that the Package Vendor's deliverable set for `PKG-029` (Transformer TXP-8600-1, 2.5 MVA, 13.8 kV / 600 / 347 V) is consistent with the EPC Scope of Work, Package Datasheet, and Construction Work Package, and that the package is ready for handoff. It is review and acceptance evidence, not vendor engineering.

## Principles

- **Vendor authors, EPC integrates.** Accept what the vendor designs; verify only that it fits the facility scope, interfaces, and accepted decomposition basis.
- **Source-anchored acceptance.** Acceptance assertions cite an accepted source — `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, DBM source slices, EPC SOW, Package Datasheet, Construction Work Package — or are marked `TBD`.
- **No agent approval.** Agents prepare review evidence and disposition recommendations. Binding acceptance is a human act (K-AUTH-1).
- **Preserve TBDs.** Where vendor submittals are silent or accessible sources do not support a value, the acceptance record carries `TBD`, not inferred numbers.

## Considerations

- **Identity precision.** TXP-8600-1 must be tracked by tag, package ID, and CoA tracking number on every acceptance record to avoid confusion with sibling transformer packages (`PKG-015`, `PKG-016`, `PKG-026`, `PKG-027`, `PKG-028`).
- **Interface scope.** The Gate 7 interface register lists seven interface types for `PKG-029`. Acceptance should address each one or flag absence as a finding; missing interface coverage is a handoff risk.
- **Secondary 347 V.** 347 V appears in the package name as the secondary-derived phase-to-neutral voltage of a 600 V WYE system. The accessible DBM slice does not state the 347 V utilization at the TXP-8600-1 level. Treat the 347 V scheme as `TBD` until vendor submittals or a project electrical specification confirms it.
- **Oil vs dry-type.** The DBM describes large oil-filled transformers as a general class. Whether TXP-8600-1 is oil-filled or dry-type is not stated in accessible sources; containment, fire-spacing, and CEC rules differ materially. Resolve via vendor data, not inference.
- **Grounding.** DBM mandates 5 A continuous high-resistance grounding on 600 V transformers and a two-point ground-grid connection for major equipment with ground wells; acceptance evidence should explicitly point to vendor compliance for these clauses.
- **Standby/TOU.** Standby power is at the 600 V MCC level via TOU generators with transfer switches; this is a facility-level concern but may influence transformer secondary load profile assumptions during acceptance.

## Trade-offs

- **Strict source citation vs schedule.** Insisting on cited source slices for every value slows acceptance but is required to prevent the review from inventing requirements the vendor never agreed to.
- **Containment vs selection.** DBM directs to limit containment where practical; over-containment is cost; under-containment is environmental and CEC risk. Acceptance carries the trade-off as a documented disposition, not a unilateral choice.
- **`TBD` markers vs apparent completeness.** A clean checklist with hidden gaps is worse than one with explicit `TBD`s. Surface gaps; do not paper over them.

## Examples

- The vendor submittal lists tag "TXP-8600-1, 2500 kVA, 13800-600/347V Dyn1" — acceptance can cite `PACKAGE_REGISTER.csv` and accept identity. Vector group (e.g., Dyn1) is from the submittal, not from the accessible source set, so it is recorded as vendor-supplied rather than as a project requirement.
- The vendor proposes 8 % impedance — accessible sources do not specify; acceptance records the vendor value, raises a finding if a project specification later mandates a different value, and marks the cross-reference `location TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-029-06-001 | Oil-filled vs dry-type construction for TXP-8600-1 is not specified in accessible sources; DBM speaks of "large oil-filled transformers" as a class but does not commit TXP-8600-1 specifically. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Transformers | Package name in `PACKAGE_REGISTER.csv` (no construction descriptor) | Datasheet "Conditions"; Specification REQ-029-06-005; Guidance Considerations | Defer to vendor submittal; record as `TBD` until vendor data is accepted. | TBD |
| HRR-029-06-002 | Secondary 347 V utilization at the TXP-8600-1 level is not explicitly described in the accessible DBM electrical section (which describes 600 V services and a separate 120/208 V lighting/utility system). | Package name "13.8kV/600/347V" in `PACKAGE_REGISTER.csv` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §System Voltages | Datasheet "Attributes"; Specification REQ-029-06-004; Guidance Considerations | Treat 347 V as the WYE phase-to-neutral derivative for area/lighting; record loading scheme as `TBD` until vendor or project electrical spec confirms. | TBD |
| HRR-029-06-003 | Package-specific area classification for the TXP-8600-1 installation location is not stated in accessible sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (general area classification references) | Package row in `PACKAGE_REGISTER.csv` (no location field) | Specification "Standards"; Guidance Considerations | Defer to vendor submittal aligned with project area classification drawings; record as `TBD`. | TBD |
| HRR-029-06-004 | `26020-Package_Requirements.docx` is present at `_Sources` root but its package-specific slice for `PKG-029` was not extracted during PREPARATION. It may contain authoritative acceptance requirements. | `_REFERENCES.md` shared source root | This deliverable's accessible source set | All four documents | Extract `PKG-029` slice as a follow-up source resolution task; current acceptance basis remains as cited. | TBD |
