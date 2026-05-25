# Guidance — DEL-016-01 Scope of Work (PKG-016 Transformer TXP-8200-1)

## Purpose

This deliverable is the Gate 5 EPC anchor that establishes a single, authoritative description of what PKG-016 is, what it does for the facility, where its boundary lies, who is responsible for what, and which interfaces it presents. Downstream deliverables (`DEL-016-02` through `DEL-016-06`) consume this SoW as their integration baseline. [Source: DELIVERABLE_REGISTER.csv; `_CONTEXT.md` "Mandatory Gate 5 EPC anchor deliverable defined by user instruction"]

## Principles

1. **Boundary first, parameters second.** The SoW fixes identity (tag, function, package row), responsibility, and interface inventory. Detailed transformer parameters (impedance, BIL, cooling, taps) belong to the Package Datasheet (`DEL-016-02`) and the Vendor Engineered Equipment Package (`DEL-016-04`). [Source: DELIVERABLE_REGISTER.csv row scopes]
2. **Anchor to DBM SEC-12.** The package's role and voltage step-down are anchored in DBM SEC-12 Incoming Power and Transformers, row `13.8 kV to 600V, 3 MVA transformer | 600V MCC for LV loads`. Restating this row is the load-bearing source-grounded claim of the SoW. [Source: DBM SEC-12]
3. **RACI is the integration contract.** Package Vendor owns package engineering, design, vendor documentation, and the equipment itself; EPC Integrator owns facility integration. Every later integration question reduces to this split. [Source: PACKAGE_REGISTER.csv RACI text]
4. **Interface inventory is closed at the type level.** PKG-016 has 7 declared interface types in INTERFACE_REGISTER.csv. New interface types should not be invented in the SoW; if a new type emerges in design, route it through the change/decomposition surface, not through this document. [Source: INTERFACE_REGISTER.csv rows for PKG-016]
5. **Do not overstate package-grouped objective associations.** OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 are mapped to this deliverable through the package-grouping heuristic in OBJECTIVE_DELIVERABLE_MAP.csv. Carry them as directional context, not as hard deliverable-level requirements. [Source: OBJECTIVE_DELIVERABLE_MAP.csv; skill OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC]

## Considerations

- The package name carries `600/347V` notation. This is the standard line-to-line / line-to-neutral notation for a 600 V wye system with a 347 V neutral derivation; the DBM low-voltage service is `600 V, 3-phase, 3-wire, 60 Hz, HRG`. **CONFLICT_FLAGGED**: see Conflict Table item C-016-01-01 below.
- The 600 V system per DBM SEC-12 is High-Resistance Grounded (HRG) with a 5 A continuous resistor. A 347 V neutral is typically a wye-connected secondary characteristic; reconciling "600/347V" with "3-wire HRG" is a downstream design question for `DEL-016-02` and the package vendor.
- The DBM also records the prior 13.8 kV / 3 MW emergency generator concept being superseded by LV standby generation. The PKG-016 step-down transformer is the normal (non-emergency) LV feed; emergency power architecture is out of this SoW's scope. [Source: DBM SEC-12 "600V MCC and Standby Power"]
- Tracking number `26020-02-30-007` is recorded as both COA Tracking Number and Workbook Tracking Number in the package row; carry it as the single canonical identifier. [Source: PACKAGE_REGISTER.csv]
- The package row notes "TBD; no package-specific exclusions stated in source materials." Treat that as the authoritative exclusion stance until source-supported exclusions are issued. [Source: PACKAGE_REGISTER.csv]

## Trade-offs

- **Specificity vs. anchoring scope.** The SoW could be enriched with transformer construction detail; doing so risks substituting inference for the downstream Package Datasheet's source-grounded values. Prefer holding such detail as `TBD` here and routing it to `DEL-016-02`.
- **Single-document vs. dispersed responsibility narrative.** Concentrating RACI here (rather than repeating it across `DEL-016-02` through `DEL-016-06`) keeps responsibility authoritative in one place at the cost of requiring downstream deliverables to reference back.

## Examples

- DBM SEC-12 explicitly attributes "Low-voltage service | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5A continuous resistor" to "Motors 3/4 hp through 250 hp, DOL starting, lighting transformers, building heaters, UPS larger than 10 kVA." This is the downstream load family that PKG-016 ultimately serves via the 600 V MCC.
- The interface inventory (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) maps directly onto routine substation/transformer integration scope items (e.g., grounding-grid tie-in, control cabling for monitoring/alarms, foundation/anchorage). The SoW can use the inventory as the section structure for its integration narrative.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-016-01-01 | Package name "3MVA 13.8kV/600/347V" implies a 4-wire wye secondary (with 347 V phase-to-neutral). DBM SEC-12 System Voltages table records the 600 V low-voltage service as "600 V, 3-phase, 3-wire, 60 Hz HRG with 5 A continuous resistor" (i.e., 3-wire). | PACKAGE_REGISTER.csv row PKG-016 (package name) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 System Voltages | Datasheet.Attributes (Secondary Voltage, Low-Voltage System Basis); Specification.Requirements R02, R03 | Carry both facts in the SoW as-is; defer reconciliation (secondary configuration: 3-wire HRG vs. 4-wire with derived neutral) to `DEL-016-02_package-datasheet` and the Package Vendor's electrical design. | TBD |
| C-016-01-02 | Objective associations OBJ-002/004/005/006/008/009/010 are mapped to DEL-016-01 by package-grouping heuristic, not by an explicit deliverable-level mapping. | OBJECTIVE_DELIVERABLE_MAP.csv (PKG-016 grouped rows) | skill `four-documents` Step 1 (PACKAGE_HEURISTIC mode) | Specification.Requirements R06 | Treat as ASSUMPTION (best-effort mapping); do not derive hard deliverable-level requirements from these objective rows unless a human ruling promotes them. | TBD |
| C-016-01-03 | DBM SEC-12 states emergency power is moved from a 13.8 kV / 3 MW generator concept to LV standby gas generation. The naming overlap "3 MVA / 3 MW" can confuse readers into associating PKG-016 with emergency power. | DBM SEC-12 "600V MCC and Standby Power" | PACKAGE_REGISTER.csv row PKG-016 (3 MVA normal step-down) | Guidance.Considerations; Specification.Scope (Out of scope) | Explicitly state in the SoW that PKG-016 is the normal 3 MVA step-down feed, not the emergency 3 MW generator (which has been superseded). | TBD |
