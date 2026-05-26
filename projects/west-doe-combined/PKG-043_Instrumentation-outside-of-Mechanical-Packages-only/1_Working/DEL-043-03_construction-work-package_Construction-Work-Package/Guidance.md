# Guidance — DEL-043-03 Construction Work Package

## Purpose

The Construction Work Package (CWP) exists so the EPC Integrator can demonstrate, in one auditable document set, how the `PKG-043 Instrumentation (outside of Mechanical Packages only)` scope will be **physically installed, built, inspected, turned over, and tied into the larger facility systems** (`DELIVERABLE_REGISTER.csv` row 242). It is one of the four mandatory Gate 5 EPC anchor deliverables defined by user instruction (`_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` row 242 Notes).

The CWP is the *constructability and execution* face of the package. It complements:

- `DEL-043-01_scope-of-work` — what the package is, what it includes, and how it integrates with the whole facility (`DELIVERABLE_REGISTER.csv` row 240).
- `DEL-043-02_package-datasheet` — the technical handoff data and interface requirements matrix (`DELIVERABLE_REGISTER.csv` row 241).
- `DEL-043-04_epc-instrumentation-discipline-production-package` — non-vendor discipline production unit, source-limited and conservatively carried (`DELIVERABLE_REGISTER.csv` row 243).

## Principles

1. **Constructability is the lens.** Every section should be readable by a construction supervisor planning crews, sequence, and rigging — not only by engineers.
2. **Interface honesty.** Every recorded physical interface (Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network — `PACKAGE_REGISTER.csv` row 45) is treated as a real construction handoff with a workface, an inspection moment, and a turnover entry.
3. **Boundary discipline.** Instrumentation that belongs to vendor mechanical packages is out of scope; the package name itself states the boundary (`PACKAGE_REGISTER.csv` row 45). Field supports, power, and communications are excluded unless package scope confirms (`PACKAGE_REGISTER.csv` row 45).
4. **Source-grounded, gap-honest.** When a construction value, code citation, or standard cannot be resolved from accessible source slices, mark it `TBD` and name the source dependency rather than fabricating a number or convention.
5. **Workbook authority.** The Workbook package row is authoritative; duplicate tracking numbers are not merged (`PACKAGE_REGISTER.csv` row 45).

## Considerations

- **WBS 01 alignment.** The package sits under WBS 01 (`PACKAGE_REGISTER.csv` row 45); the workface plan should align with the WBS 01 execution structure rather than re-invent a sequence.
- **Vendor-package ownership model.** "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources" (`PACKAGE_REGISTER.csv` row 45). The CWP should not presume a vendor split that has not been declared.
- **Interface-driven sequencing.** Because PKG-043 carries five interface types, sequencing should be driven by interface readiness windows (e.g., process piping ready for instrument installation; cable tray populated before I&C pulls) rather than by instrument count alone.
- **ITP and turnover content.** ITP detail and turnover content are placeholders until governing project specifications and the facility commissioning system structure are accessible.
- **Objective coverage.** PKG-043 supports OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 at the package level (`PACKAGE_REGISTER.csv` row 45). The deliverable register row for DEL-043-03 additionally lists OBJ-008 (`DELIVERABLE_REGISTER.csv` row 242). The CWP traceability matrix should account for all seven listed on the deliverable row.

## Trade-offs

| Trade-off | Discussion | Disposition |
|---|---|---|
| Detail depth vs. source availability | Greater construction detail would require design-basis source slices not yet locally accessible. | Hold detail at structural / outline level; mark depth items `TBD` rather than invent. |
| Interface coverage breadth vs. document volume | All five interface types must be covered, even where their share of the package is small. | Cover all five; allow proportional treatment. |
| Vendor-split presumption vs. source silence | Sources are silent on a clean vendor / EPC split. | Do not presume a split; describe responsibility as source-dependent (`PACKAGE_REGISTER.csv` row 45). |
| EPC artifact reuse vs. project-specific authoring | Many EPCs have standard CWP templates. | Reuse only structure that does not contradict the package's recorded scope, interfaces, and exclusions. |

## Examples

Accessible source slices do not contain worked CWP examples for PKG-043. Examples will be added once governing project construction specifications and at least one analogous executed CWP become locally accessible (`TBD`).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Objective list for PKG-043 differs between PACKAGE_REGISTER (6 objectives) and the DEL-043-03 row (7 objectives — adds OBJ-008). | `PACKAGE_REGISTER.csv` row 45 (objectives column: OBJ-001; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-010) | `DELIVERABLE_REGISTER.csv` row 242 (objectives column: OBJ-001; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-010) | Datasheet (SupportsObjectives), Specification R-06, Guidance Considerations, traceability matrix | PROPOSAL: accept the seven-objective list from the deliverable register row as the authoritative scope for DEL-043-03 (deliverable-level objectives may exceed package-level objectives). | TBD |
