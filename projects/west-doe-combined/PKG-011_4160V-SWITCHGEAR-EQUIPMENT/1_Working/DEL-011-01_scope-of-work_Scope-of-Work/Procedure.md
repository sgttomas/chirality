# Procedure: DEL-011-01 Scope of Work

## Purpose

Define the bounded procedure for producing and checking the EPC Integrator Scope of Work for PKG-011, `4160V SWITCHGEAR EQUIPMENT`, using accepted Gate 7 decomposition truth and accessible local source slices.

## Prerequisites

- Accepted decomposition truth: Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24.
- Deliverable-local context files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Source slices:
  - Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-011-01.
  - Gate 7 `PACKAGE_REGISTER.csv` row PKG-011.
  - Gate 7 `SCOPE_LEDGER.csv` row SOW-0012.
  - Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-011-01.
  - Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-011.
  - Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-011-01.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 electrical basis.
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 electrical basis.
- Declared upstream dependencies: none declared during PREPARATION. Source: `_DEPENDENCIES.md`.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED` for this run).
2. Read `_CONTEXT.md` and confirm the deliverable identity: DEL-011-01_scope-of-work, Scope of Work, PKG-011, 4160V SWITCHGEAR EQUIPMENT, Electrical, EPC Scope of Work, responsible party EPC Integrator.
3. Read `_REFERENCES.md` and use the Gate 7 snapshot as the accepted upstream decomposition truth; do not reinterpret the raw source corpus beyond accessible source slices needed to ground the draft.
4. Read the Gate 7 deliverable, package, scope, artifact, interface, and objective rows listed in the prerequisites.
5. Draft the Scope of Work content so it includes:
   - Package identity and source basis.
   - WBS and CoA tracking number.
   - Package function and whole-facility integration narrative.
   - Tagged equipment and package identity basis where source-supported.
   - Responsibility assignment record.
   - Declared interface categories.
   - `TBD` for package-specific exclusions and unsupported design values.
6. Apply the DBM electrical source slices only where they support boundary/interface context for 4.16 kV switchgear/MCC integration.
7. Check that vendor-owned package engineering, package design, vendor documentation, and physical equipment supply are not assigned to the EPC Integrator.
8. Check that all six declared PKG-011 interface categories appear consistently across the draft.
9. Check that unresolved items remain `TBD` or are listed in the Conflict Table for human ruling.
10. Update `_STATUS.md` from `OPEN` to `INITIALIZED` only if the current state remains `OPEN`.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity consistency | Datasheet, Specification, Guidance, and Procedure use the same deliverable ID, package ID, package name, WBS, CoA tracking number, discipline, and responsible party. |
| Source grounding | Non-trivial requirements cite Gate 7 rows or DBM source sections. |
| Interface coverage | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are all present. |
| Responsibility boundary | Vendor and EPC Integrator responsibilities match Gate 7 `PACKAGE_REGISTER.csv` row PKG-011. |
| Unknown handling | Package-specific exclusions, final ratings, unresolved electrical coordination items, and unsupported values remain `TBD` or appear in the Conflict Table. |
| Dependency handling | No blockers are asserted because no declared upstream dependencies exist. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-24_1658.md`
