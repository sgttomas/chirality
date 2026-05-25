# Guidance: DEL-021-01_scope-of-work

## Purpose

This Guidance explains how the EPC Integrator should interpret and use the Scope of Work for `PKG-021`, the 6.9kV SWITCHGEAR EQUIPMENT package. The Scope of Work is the EPC anchor that defines what is in the package, why the package exists, where it ties into the facility, and how responsibility is split between the Package Vendor and the EPC Integrator. Downstream EPC deliverables (Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover Package, and EPC Vendor Package Review and Acceptance) rely on this scope statement.

## Principles

- **Scope before specification.** The Scope of Work defines *what is in* the package and *who owns it*. Equipment ratings, breaker counts, bus configuration, and protective settings belong in the Package Datasheet (`DEL-021-02`) and the Vendor Engineered Equipment Package (`DEL-021-04`), and shall not be invented here.
- **Source authority over convention.** Where the DBM electrical section provides a value (medium-voltage service basis, neutral grounding resistor, no PFC on MCC-8200 synchronous-transfer bus, Starting VFDs for KM-2150/2250 motors), the source value governs and shall be cited.
- **Decomposition routes; sources define.** The Gate 7 registers define identity and interface facts; the DBM defines the medium-voltage electrical design basis. Convention is not a substitute when the source is locally available.
- **Responsibility discipline.** The package is vendor-owned for engineering/design/equipment. EPC Integrator scope is *integration* (interfaces, tie-ins, constructability, procurement coordination, facility integration). The Scope of Work shall not assign EPC scope tasks that are owned by the vendor, and shall not absorb vendor scope into EPC documents.
- **Open items are surfaced, not hidden.** Lineup ratings, breaker counts, interrupting capacity, and exact installation room are `TBD` until the short-circuit study and vendor engineering are complete. Carry them visibly; do not assume.

## Considerations

- The 6.9 kV switchgear/MCC primarily serves the KM-2150/2250 Inlet/Sales Gas Compressor motors via Starting VFDs with synchronous transfer to a normal-service bus. Compressor frame selection (Ariel KBC/6 vs. KBZ/6) and motor horsepower (6,700 hp vs. 7,000 hp legacy) are flagged in DBM as unresolved — see the Conflict Table.
- The 6.9 kV electrical building (820-1) is shop-fabricated and arrives as a prefab modular building, elevated on piles with bottom cable entry. EPC integration shall plan civil/structural tie-in and cable tray routing accordingly.
- Each 6.9 kV transformer uses a 100 A, 10 s neutral grounding resistor and operates as a tripping system; ground-fault detection on 600 V systems is alarm-only — do not confuse the two grounding regimes when authoring the Scope of Work.
- Medium-voltage cable is shielded three-conductor copper TECK rated 8 kV (100% insulation). This affects cable tray sizing, separation, and termination requirements that the EPC Integrator must coordinate with the building/structural and I&C scopes.
- Spacing rule for MCCs (7.5 m / 25 ft from process equipment, per CEC) may govern building siting; applicability to 6.9 kV switchgear inside a prefab electrical building shall be confirmed in detailed design.
- The package supports OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 by best-effort package-heuristic association from the Gate 7 OBJECTIVE_DELIVERABLE_MAP — treat as directional context (ASSUMPTION), not a hard requirement, unless confirmed.

## Trade-offs

- **Vendor-engineered packaged switchgear vs. site-built lineup.** The DBM/Workbook basis is a vendor-engineered packaged switchgear/MCC delivered as part of a prefab electrical building. This shortens site work but constrains EPC change flexibility once vendor engineering proceeds.
- **MCC-8200 synchronous-transfer bus without PFC capacitors.** DBM explicitly excludes power-factor-correction capacitor banks on this bus. Any future request to add PFC must be evaluated against synchronous-transfer behavior and would require a deviation.
- **Centralized 6.9 kV distribution vs. distributed MV.** The DBM basis is centralized 6.9 kV distribution from the 13.8 kV main; alternative distributed-MV concepts are not in scope here.
- **TBD-now vs. assume-now.** Quantitative gaps (bus rating, breaker count, interrupting capacity) are carried as `TBD` rather than placeholder values to avoid contaminating downstream vendor engineering with unverified numbers.

## Examples

- *Identity statement example*: "PKG-021, workbook row 23, WBS 01, 26020-01-30-012, 6.9kV SWITCHGEAR EQUIPMENT, Electrical, vendor-owned; EPC Integrator integrates into the West Doe Deepcut facility via the 820-1 6.9kV Inlet/Sales Compressor Electrical Building."
- *Function statement example*: "The package provides 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance-grounded medium-voltage distribution to facility process inverter-drive motors rated 5,500 hp and above, including Starting VFDs for the KM-2150/2250 Inlet/Sales Gas Compressor motors with synchronous transfer to a normal-service bus."
- *Interface statement example*: "Applicable interfaces (per `INTERFACE_REGISTER.csv` rows for `PKG-021`): Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-021-01-001 | Inlet/sales compressor frame selection: Ariel KBC/6 (current basis) vs. KBZ/6 (legacy/conflicting reference). Affects the load that the 6.9 kV switchgear must serve. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893 (KBC/6 current basis) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1083 (KBZ/6 reference); line 2196 equipment table (KBZ/6) | Datasheet.Attributes (MCC association); Specification REQ-021-01-009 | Treat compressor frame selection as TBD downstream; do not embed frame choice in this Scope of Work. | TBD |
| CONF-021-01-002 | Inlet/Sales Compressor motor power: 6,700 hp (DBM electric drive narrative) vs. 7,000 hp (equipment-list table row). Affects 6.9 kV switchgear load and Starting VFD sizing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893 (6,700 hp electric drive) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2196 (7,000 hp / 5,220 kW equipment list row) | Datasheet.Attributes (medium-voltage service basis); Specification REQ-021-01-006 | Carry both values as TBD pending detailed electrical study; do not assign single hp value in the Scope of Work. | TBD |
| CONF-021-01-003 | Package-specific exclusions are not stated in source; `PACKAGE_REGISTER.csv` row records exclusions as TBD. | `PACKAGE_REGISTER.csv` row `PKG-021` (exclusions = TBD) | Workbook Packages row 23 (no exclusions stated) | Specification.Scope (Exclusions); Guidance.Trade-offs | Hold package-specific exclusions as TBD; confirm scope boundary with EPC scope owner before publication. | TBD |
