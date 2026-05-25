# Guidance — DEL-031-01 Scope of Work (PKG-031 Transformer TXP-8500-1)

## Purpose

This deliverable is the Gate 5 EPC anchor that establishes a single, authoritative description of what PKG-031 is, what it does for the facility, where its boundary lies, who is responsible for what, and which interfaces it presents. Downstream deliverables (`DEL-031-02` through `DEL-031-06`) consume this SoW as their integration baseline. [Source: DELIVERABLE_REGISTER.csv; `_CONTEXT.md` "Mandatory Gate 5 EPC anchor deliverable defined by user instruction"]

## Principles

1. **Boundary first, parameters second.** The SoW fixes identity (tag, function, package row), responsibility, and interface inventory. Detailed transformer parameters (impedance, BIL, cooling, taps) belong to the Package Datasheet (`DEL-031-02`) and the Vendor Engineered Equipment Package (`DEL-031-04`). [Source: DELIVERABLE_REGISTER.csv row scopes]
2. **Anchor to DBM-Deepcut Electrical Basis.** The package's role and voltage step-down are anchored in the DBM-Deepcut Power Distribution narrative, which states that 13.8 kV switchgear distributes radially through step-down transformers to facility loads, and that LV service is 600 V HRG. Restating these facts is the load-bearing source-grounded claim of the SoW. [Source: DBM-Deepcut lines 2917–2937]
3. **RACI is the integration contract.** Package Vendor owns package engineering, design, vendor documentation, and the equipment itself; EPC Integrator owns facility integration. Every later integration question reduces to this split. [Source: PACKAGE_REGISTER.csv RACI text]
4. **Interface inventory is closed at the type level.** PKG-031 has 7 declared interface types in INTERFACE_REGISTER.csv. New interface types should not be invented in the SoW; if a new type emerges in design, route it through the change/decomposition surface, not through this document. [Source: INTERFACE_REGISTER.csv rows for PKG-031]
5. **Do not overstate package-grouped objective associations.** OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 are mapped to this deliverable through the package-grouping heuristic in OBJECTIVE_DELIVERABLE_MAP.csv. Carry them as directional context, not as hard deliverable-level requirements. [Source: OBJECTIVE_DELIVERABLE_MAP.csv; skill OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC]

## Considerations

- The package name carries `600/347V` notation. This is the standard line-to-line / line-to-neutral notation for a 600 V wye system with a 347 V neutral derivation; the DBM-Deepcut System Voltages table records the 600 V low-voltage service as "600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor". **CONFLICT_FLAGGED**: see Conflict Table item C-031-01-01 below.
- The 600 V system per DBM-Deepcut is High-Resistance Grounded (HRG) with a 5 A continuous resistor at the transformer neutral; 600 V ground-fault protection is alarm-only to maintain continuity of operations. A 347 V neutral is typically a wye-connected secondary characteristic; reconciling "600/347V" with "3-wire HRG" is a downstream design question for `DEL-031-02` and the package vendor. [Source: DBM-Deepcut lines 2937, 2985]
- PKG-031 is a normal (non-emergency) LV feed. The DBM records that the prior 13.8 kV emergency-generator concept has been superseded by LV TOU standby generators connected at the 600 V MCC level via transfer switches; PKG-031 is not part of that standby architecture. [Source: DBM-Deepcut line 2943]
- The DBM does not name TXP-8500-1 by tag. The package identity (TXP-8500-1, 3 MVA, 13.8 kV/600/347V, WBS 01, CoA 26020-01-30-022, row 33) is carried by the workbook/PACKAGE_REGISTER.csv row; the DBM supplies the facility electrical basis that the package operates within. [Source: PACKAGE_REGISTER.csv; DBM-Deepcut]
- The package row states "TBD; no package-specific exclusions stated in source materials." Treat that as the authoritative exclusion stance until source-supported exclusions are issued. [Source: PACKAGE_REGISTER.csv]
- WBS 01 places PKG-031 in the Deepcut (04-25) facility scope; PKG-016 is the corresponding 3 MVA 13.8kV/600/347V step-down transformer for the Comp & Liquids (03-25) facility (WBS 02). The two packages share equipment class and rating but serve different facilities and are anchored to different DBMs.

## Trade-offs

- **Specificity vs. anchoring scope.** The SoW could be enriched with transformer construction detail; doing so risks substituting inference for the downstream Package Datasheet's source-grounded values. Prefer holding such detail as `TBD` here and routing it to `DEL-031-02`.
- **Single-document vs. dispersed responsibility narrative.** Concentrating RACI here (rather than repeating it across `DEL-031-02` through `DEL-031-06`) keeps responsibility authoritative in one place at the cost of requiring downstream deliverables to reference back.

## Examples

- DBM-Deepcut explicitly attributes "Low-voltage services | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor" to motors 3/4 hp through 250 hp DOL-started, lighting and utility distribution transformers, building heaters, and UPS systems larger than 10 kVA. This is the downstream load family that PKG-031 ultimately serves via the 600 V MCC.
- The interface inventory (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) maps directly onto routine substation/transformer integration scope items (e.g., grounding-grid tie-in, control cabling for monitoring/alarms, foundation/anchorage). The SoW can use the inventory as the section structure for its integration narrative.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-031-01-01 | Package name "3MVA 13.8kV/600/347V" implies a 4-wire wye secondary (with 347 V phase-to-neutral). DBM-Deepcut System Voltages table records the 600 V low-voltage service as "600 V, 3-phase, 3-wire, 60 Hz HRG with 5 A continuous resistor" (i.e., 3-wire). | PACKAGE_REGISTER.csv row PKG-031 (package name) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages (line 2937) | Datasheet.Attributes (Secondary Voltage, Low-Voltage System Basis); Specification.Requirements R02, R03, R10 | Carry both facts in the SoW as-is; defer reconciliation (secondary configuration: 3-wire HRG vs. 4-wire with derived neutral) to `DEL-031-02_package-datasheet` and the Package Vendor's electrical design. | TBD |
| C-031-01-02 | Objective associations OBJ-001/004/005/006/008/009/010 are mapped to DEL-031-01 by package-grouping heuristic, not by an explicit deliverable-level mapping. | OBJECTIVE_DELIVERABLE_MAP.csv (PKG-031 grouped rows) | skill `four-documents` Step 1 (PACKAGE_HEURISTIC mode) | Specification.Requirements R06 | Treat as ASSUMPTION (best-effort mapping); do not derive hard deliverable-level requirements from these objective rows unless a human ruling promotes them. | TBD |
| C-031-01-03 | The DBM-Deepcut electrical basis does not name TXP-8500-1 by tag; the equipment tag, MVA rating, and 600/347V notation come only from the workbook package row. | PACKAGE_REGISTER.csv row PKG-031 (package name and tracking number) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power Distribution narrative (lines 2917–2929) | Datasheet.Identification/Attributes; Specification.Requirements R01, R02 | Carry tag and rating as workbook-authoritative; carry the facility electrical context as DBM-authoritative; do not synthesize source agreement that is not in the DBM. | TBD |
