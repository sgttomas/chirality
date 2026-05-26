# Guidance — DEL-078-06: EPC Vendor Package Review and Acceptance

## Purpose

This deliverable is the EPC Integrator's audit-quality record that the Pig Receivers (Inlet) 4-25 vendor package has been reviewed and accepted against the EPC triad (Scope of Work, Package Datasheet, Construction Work Package) and is ready for construction handoff, commissioning, and turnover. It is not a re-engineering deliverable; it consumes accepted upstream vendor work (DEL-078-04, DEL-078-05) and produces traceable evidence of integration acceptance.

[Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row DEL-078-06.]

## Principles

1. Acceptance is anchored to the EPC triad, not to the vendor's preferred conventions. When the vendor package and the EPC triad disagree, the EPC triad is authoritative pending a ruling.
2. Source fidelity is non-negotiable. Each accepted item cites the source artifact and revision it was accepted against.
3. The EPC Integrator reviews; it does not author the vendor design. Acceptance does not imply re-warranty of vendor scope.
4. Open interface items are surfaced, not silently absorbed. Items previously called TBD in the DBM body remain TBD here until evidence closes them.
5. Conflict surfacing is preferred over silent reconciliation. Quantity, pressure, and interface conflicts are escalated to human ruling.

## Considerations

- **Sour service environment.** The package is in sour natural gas service per DBM body. Materials and welding programs should be scrutinized for sour-service conformance; vendor's NACE/ISO 15156 compliance should be evidenced rather than assumed.
- **Pigging hazards at the plant gate.** The DBM body identifies two-phase flow during winter or shutdown cooling, methanol injection requirements, and the need for full-port upstream isolation. The acceptance review should verify the pig receiver and associated isolation are consistent with these operating realities, not only steady-state pigging.
- **HP flare connection.** The pig receiver vents to the HP flare. Acceptance review should confirm vent header pressure rating, slope, drainage routing to the HP flare KO drum, and that the vent does not violate HP-flare design assumptions.
- **Barred tees downstream.** Barred-tee installation is a safety-critical interface that prevents pig migration into facility piping; acceptance should include a walkdown verification, not only a drawing check.
- **Second-receiver provision.** The DBM body explicitly leaves open "any second inlet pipeline pig receiver/isolation requirements." The acceptance record should state explicitly which configuration was accepted and which were deferred.
- **Document-review coding.** The owner's document review code system (e.g., Code 1/2/3) should be confirmed before the review log is finalized.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Strict triad adherence vs. accepted vendor deviations | A formal deviation record (with EPC ruling) is preferred over silent acceptance of vendor variation. |
| Witness-everything FAT vs. risk-based sampling | Risk-based witness sampling is operationally efficient but must document the basis; high-consequence items (pressure test, closure interlocks) should be witnessed. |
| Early conditional acceptance vs. full acceptance at MC | Conditional acceptance can unblock construction but introduces punch-list discipline burden. |

## Examples

(No worked examples in accessible sources. Examples will be incorporated when vendor submittals are received and the acceptance record becomes populated.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-DEL-078-06-001 | Quantity of inlet pig receivers: DBM body says one 24" pig receiver; package roster lists three tags (`PR-1010-1`, `PR-1020-1`, `PR-1030-1`, equipment count 3). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Inlet Pig Receiving narrative (one 24" pig receiver) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Package Line-Item Requirements row 61 (`Pig Receivers (Inlet) 2` — 3 equipment items) | `Datasheet.md` Attributes/Conditions; `Specification.md` R3.3 | PROPOSAL: treat the package roster (3 tags) as governing equipment count pending confirmation, and treat DBM body "one 24" pig receiver" as the inlet-pipeline arrangement basis for the single inlet pipeline currently described. | TBD |
| CONF-DEL-078-06-002 | Second inlet pipeline pig receiver/isolation arrangement: DBM body explicitly states "Inlet pipeline final configuration, detailed tie-ins, and any second inlet pipeline pig receiver/isolation requirements are TBD." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Inlet Pipeline section (TBD note) | (no opposing source — open item) | `Specification.md` R6.2 | PROPOSAL: accept current-scope single-receiver basis; defer second-receiver configuration to a separate deliverable or revision. | TBD |
| CONF-DEL-078-06-003 | Delivery point ESDV pressure shutdown setpoint is stated as TBC in DBM; needs vendor input to close. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Inlet Separator/ESDV narrative (TBC) | (vendor submittal not yet provided) | `Datasheet.md` Conditions; `Specification.md` R3.2 | PROPOSAL: hold acceptance of ESDV configuration until vendor sets and EPC confirms setpoint. | TBD |
| CONF-DEL-078-06-004 | HIPPS requirement on inlet pipeline if upstream MAOP exceeds facility inlet design pressure: DBM body identifies as possibly required, TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Inlet Separator/HIPPS narrative | (no opposing source) | `Datasheet.md` Conditions; `Specification.md` R6.1 | PROPOSAL: track HIPPS necessity as an open interface item; do not accept package as HIPPS-closed without explicit evidence. | TBD |
| CONF-DEL-078-06-005 | Objective association mode is PACKAGE_HEURISTIC (ASSUMPTION); `OBJ-001..010` are package-grouped, not deliverable-specific. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped) | `Datasheet.md` Covers Scope Items / Supports Objectives | PROPOSAL: retain package-heuristic association unless the human confirms a deliverable-specific objective list. | TBD |
