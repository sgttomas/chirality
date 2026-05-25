# Procedure: DEL-018-04 — Vendor Engineered Equipment Package (PKG-018 MV VFD)

Operational procedure for producing the Package Vendor production unit for PKG-018 (engineering, design, fabrication/supply, equipment package).

## Purpose

Define the step sequence the Package Vendor follows to produce the MV VFD equipment package, with verification hooks that map back to the Specification and Guidance, so the EPC Integrator can review and accept the package under `DEL-018-06`.

## Prerequisites

- Issued EPC Scope of Work for PKG-018 (`DEL-018-01`).
- Issued EPC Package Datasheet for PKG-018 (`DEL-018-02`) — provides the authoritative motor rating, electrical interface data, environment, area classification, and communications requirement.
- Accepted DBM context: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- GATE-07 PROJECT_DECOMP snapshot for PKG-018 row 20 and DEL-018-04 row 93.
- Resolution (or documented deferral) of the Conflict Table entries in `Guidance.md`, in particular CONF-018-04-001 (motor rating basis) and CONF-018-04-002 (starting vs continuous duty).
- No declared upstream dependencies in `_DEPENDENCIES.md`; coordination mode is DECLARED. Where `DEL-018-01` / `DEL-018-02` issuance is required, treat as an undeclared but procedurally required input and surface to the EPC Integrator if not yet issued.

## Steps

1. **Confirm package identity and scope.**
   - Re-read `_CONTEXT.md`, GATE-07 `DELIVERABLE_REGISTER.csv` row 93, and `PACKAGE_REGISTER.csv` row 20.
   - Confirm vendor ownership of engineering/design/vendor documentation/physical equipment; confirm EPC Integrator ownership of facility-level integration.
2. **Ingest EPC anchors.**
   - Load motor rating, electrical interface data, environment, area classification, hazardous-area zone, and communications requirements from the issued EPC Package Datasheet.
   - Cross-check against the EPC Scope of Work for boundary and responsibility statements.
3. **Resolve open basis questions.**
   - Apply the human ruling(s) on the Guidance Conflict Table; if any item remains `TBD`, escalate to the EPC Integrator before committing to a drive topology.
4. **Define package boundary.**
   - Produce a package boundary diagram and terminal-point schedule covering the six declared PKG-018 interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
5. **Vendor electrical engineering.**
   - Size the drive lineup for the confirmed motor data and duty cycle (starting vs continuous per ruling).
   - Perform harmonic and reactive-power studies; select filter / transformer / topology approach consistent with the no-capacitor-bank constraint at the synchronous-transfer bus.
   - Coordinate motor T-code envelope for Zone 2 areas (do not produce drive-output conditions that prevent motor T-code compliance).
6. **Vendor mechanical / packaging engineering.**
   - Lay out the drive cubicle(s), transformers/reactors/filters, controls, and HMI for electrical-building installation (default facility basis).
   - Define shipping splits, lifting/handling, and maintenance access consistent with the Maintenance Access interface type.
7. **Vendor controls and communications engineering.**
   - Define HMI and controls; provide EtherNet (or EPC-specified) port for the plant PLC central control panel for data acquisition.
   - Define alarm, trip, and status signals consistent with the EPC Package Datasheet I&C interface.
8. **Produce vendor design documentation set.**
   - Issue vendor package design basis and vendor datasheets for the VFD lineup and associated equipment.
   - Issue boundary diagram, terminal-point schedules, and study reports.
9. **Fabricate / procure the physical equipment package.**
   - Manufacture or procure per issued vendor design.
   - Apply vendor factory acceptance testing per vendor QA plan.
10. **Support EPC Integrator integration review.**
    - Respond to integration questions; resolve action items prior to acceptance under `DEL-018-06`.
11. **Hand off vendor documentation to `DEL-018-05`.**
    - Vendor document register, submittals, and turnover records are assembled under `DEL-018-05` and reviewed under `DEL-018-06` — this deliverable does not own that assembly.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Package identity confirmed | Trace to GATE-07 row 93 / row 20 | Confirmed in Vendor Package Design Basis |
| Motor rating sourced from EPC Package Datasheet (R-018-04-002, R-018-04-012) | Audit vendor sizing inputs | All motor parameters cite `DEL-018-02` |
| Boundary covers six declared interface types (R-018-04-003) | Boundary diagram + terminal-point schedule review | All six interface types represented |
| Drive output / motor T-code (R-018-04-004) | T-code compatibility analysis | Motor T-code remains lower than area classification value |
| Harmonic / reactive-power posture (R-018-04-005) | Vendor study review | Studies issued; no capacitor-bank reliance at sync-transfer bus |
| Starting / continuous duty (R-018-04-006) | Conflict Table closure | Duty selected per human ruling; vendor design matches |
| Communications port (R-018-04-007) | Vendor controls review | Port type matches EPC Package Datasheet (or recorded ASSUMPTION confirmed) |
| LV cabling type from VFDs (R-018-04-008) | Cable schedule review | Copper TECK for LV power cables fed from VFDs |
| Vendor design basis / datasheet set issued (R-018-04-009) | Document register review | Issued and reviewable |
| Integration review action closure (R-018-04-010) | Action log review | All items closed before `DEL-018-06` acceptance |
| Enclosure rating matches installation environment (R-018-04-011) | Cross-check vendor enclosure to EPC Package Datasheet | Match confirmed |

## Records

- Vendor Package Design Basis.
- Vendor datasheet set (drive lineup; transformers/reactors/filters; controls/HMI as designed).
- Package boundary diagram and terminal-point schedules.
- Harmonic and reactive-power study reports.
- Motor T-code coordination memo (if applicable).
- Factory acceptance test records (vendor QA).
- Integration-review action log closures supporting `DEL-018-06`.
- Cross-reference notes pointing to `DEL-018-05` for vendor document turnover and `DEL-018-06` for EPC acceptance.
