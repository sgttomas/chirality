# Guidance: DEL-008-01_scope-of-work — Scope of Work

## Purpose

The Scope of Work exists to establish the EPC Integrator's bounded work definition for the PKG-008 Controls system design and integration package. It is the package-level anchor for identity, function, interfaces, and responsibility before downstream package datasheet, construction work package, and controls discipline production work proceed.

## Principles

- Use the Gate 7 final published PROJECT_DECOMP snapshot as the accepted upstream truth for this Phase 2.2 run.
- Keep the Scope of Work at package-boundary level: package identity, function, interfaces, source basis, and responsibility assignment.
- Preserve source limits explicitly. If the accepted snapshot does not provide detailed controls values, tagged equipment details, exclusions, or clause-level standards, mark them as TBD.
- Treat objective associations as context, not standalone requirements, unless the deliverable row or accepted snapshot explicitly supports the requirement.
- Keep controls power-panel items as interface facts/artifacts under the package datasheet; do not split them into a separate package or deliverable.

## Considerations

The package is associated with objectives for facility scope, commercial boundary interfaces, electrical basis, controls/instrumentation/communications integration, utilities/support systems, safety/regulatory carry-through, and turnover readiness. These objectives are directionally relevant because DEL-008-01 is explicitly mapped to OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, and OBJ-010 in the accepted deliverable register and objective-deliverable map.

The most important source-grounded content for this Phase 2.2 draft is:

- WBS 01 Controls package identity.
- CoA tracking number 26020-01-32-001.
- Workbook Packages row 9 as the accepted source reference.
- Declared interface types: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems.
- The responsibility-model statement that EPC Integrator or discipline subcontractor responsibility is source-dependent and that no separate vendor-package ownership model is inferred.
- The Gate 6 disposition that controls power-panel interfaces remain interface facts/artifacts under the package datasheet.

## Trade-offs

| Topic | Guidance |
|---|---|
| Scope completeness vs. source fidelity | Prefer a complete structure with TBD fields over invented technical detail. |
| Interface breadth vs. separate deliverables | Name all accepted PKG-008 interface types, but do not create new deliverables beyond Gate 7. |
| Objective coverage vs. enforceable requirements | Use mapped objectives to shape coverage and review questions; derive requirements only from accepted snapshot entries. |
| Responsibility assignment | Preserve source-dependent responsibility wording until a later human ruling or source-verification workflow assigns discipline subcontractor responsibility more specifically. |

## Examples

- Acceptable: "The Scope of Work covers Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems interfaces." Source: PACKAGE_REGISTER.csv and INTERFACE_REGISTER.csv for PKG-008.
- Acceptable: "Package-specific exclusions are TBD." Source: PACKAGE_REGISTER.csv, PKG-008.
- Not acceptable in this run: a clause-level controls-system design requirement not present in the accepted Gate 7 snapshot.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-008-01-001 | Whether EPC Integrator alone or a discipline subcontractor is the final responsible party for the PKG-008 Scope of Work. | _CONTEXT.md Identity lists ResponsibleParty as EPC Integrator. | PACKAGE_REGISTER.csv PKG-008 states EPC Integrator or discipline subcontractor responsibility is source-dependent. | Datasheet Identification; Specification Requirements; Procedure prerequisites and records. | Use EPC Integrator as deliverable owner and preserve source-dependent execution responsibility until human assignment. | TBD |
| HRR-008-01-002 | Whether controls power-panel interfaces need separate tracking beyond package-datasheet interface facts. | INTERFACE_REGISTER.csv PKG-008 asks to confirm separate tracking. | ARTIFACT_REGISTER.csv DEL-008-02 interface rows record Gate 6 disposition: no separate package or deliverable. | Specification Scope; Procedure review steps. | Follow Gate 6 disposition; keep as package datasheet interface facts/artifacts. | TBD |
