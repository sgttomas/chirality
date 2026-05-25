# Procedure: Construction Work Package

## Purpose

Define the bounded procedure for producing and using the Phase 2.2 Construction Work Package for PKG-011, 4160V SWITCHGEAR EQUIPMENT, based on accepted Gate 7 decomposition truth and deliverable-local context.

## Prerequisites

- Accepted upstream Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, and _STATUS.md are available.
- Current status permits overwrite. For this run, _STATUS.md was OPEN.
- Declared dependency review is complete. No upstream or downstream dependencies were declared during PREPARATION.
- Source-dependent details not present in Gate 7 or deliverable-local context are carried as TBD.

## Steps

1. Confirm the deliverable identity: DEL-011-03_construction-work-package, Construction Work Package, PKG-011, 4160V SWITCHGEAR EQUIPMENT, discipline Electrical, responsible party EPC Integrator.
2. Confirm the package ownership split from Gate 7: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
3. Establish the required artifact set: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
4. Build the installation and tie-in workface plan around the accepted interface types:
   - Electrical Power.
   - Grounding / Bonding.
   - I&C / Control Cabling.
   - Communications / Network.
   - Maintenance Access.
   - Structural / Foundations / Supports.
5. For each interface type, identify construction readiness items, installation/tie-in activities, inspection evidence, turnover records, and source-dependent details that remain TBD.
6. Confirm that no undeclared dependency is treated as a blocker. Record any discovered coordination concern as an advisory open item until a declared dependency edge is created by the appropriate workflow.
7. Preserve unsupported details as TBD. Do not add equipment ratings, cable identifiers, relay settings, test values, installation tolerances, energization sequence, or code clauses unless a locally accessible accepted source supports them.
8. Assemble the construction interface and turnover checklist with fields for responsible party, evidence record, status, outstanding TBD/source need, and human ruling where required.
9. Cross-check the Datasheet, Specification, Guidance, and Procedure for consistent identity, interface terminology, responsibility split, and TBD treatment.
10. Update the deliverable state to INITIALIZED when the four documents have been created and the Phase 2.2 consistency sweep is complete.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Identity matches _CONTEXT.md and Gate 7 DELIVERABLE_REGISTER.csv row 50. |
| Responsibility check | No procedure step assigns Package Vendor design obligations to EPC Integrator. |
| Interface check | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are all represented. |
| Artifact check | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are included or listed as records. |
| Dependency check | No blockers are asserted from undeclared relationships. |
| Source-fidelity check | Missing detailed construction requirements remain TBD or Human Ruling Required. |

## Records

- Datasheet.md.
- Specification.md.
- Guidance.md, including Conflict Table for human ruling.
- Procedure.md.
- _STATUS.md showing INITIALIZED after successful Phase 2.2 initialization.
- TASK run record under _run_records/.
- Future source-resolution records for vendor installation documents, electrical construction standards, commissioning/energization criteria, and inspection/turnover forms.
