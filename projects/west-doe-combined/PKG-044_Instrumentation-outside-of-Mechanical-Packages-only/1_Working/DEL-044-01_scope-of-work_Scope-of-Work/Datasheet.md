# Datasheet — DEL-044-01 Scope of Work

Descriptive datasheet for the EPC Integrator Scope of Work deliverable covering package PKG-044, "Instrumentation (outside of Mechanical Packages only)."

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-044-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (GATE-07) |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Parent Package ID | `PKG-044` | `_CONTEXT.md` |
| Parent Workbook ID | 44 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Workbook Source Row | Workbook Packages row 46 | `PACKAGE_REGISTER.csv` |
| Package Name | Instrumentation (outside of Mechanical Packages only) | `PACKAGE_REGISTER.csv` |
| Discipline | Instrumentation | `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-32-002 | `PACKAGE_REGISTER.csv` |
| Covered Scope Item | `SOW-0045` | `SCOPE_LEDGER.csv` |
| Supported Objectives | OBJ-002; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-010 | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Decomposition Basis | GATE-07 Final Published PROJECT_DECOMP snapshot (2026-05-24) | `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (summary) | Workbook-defined Instrumentation package for "Instrumentation (outside of Mechanical Packages only)" under WBS 02 with recorded physical interfaces. | `PACKAGE_REGISTER.csv` |
| Inclusion Disposition (Gate 6) | Instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy. | `INTERFACE_REGISTER.csv` Notes; `PACKAGE_REGISTER.csv` Notes |
| Boundary Caveat | Field supports, power, and comms are not marked unless confirmed by package scope. | `PACKAGE_REGISTER.csv` |
| Package Exclusions | TBD; no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` |
| Vendor-Package Ownership Model | Not inferred from current sources; EPC Integrator vs. discipline subcontractor responsibility is source-dependent. | `PACKAGE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-42A035696B) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle Gate | Mandatory Gate 5 EPC anchor deliverable | `DELIVERABLE_REGISTER.csv` Notes |
| Coordination Mode | DECLARED | `_DEPENDENCIES.md` |
| Declared Upstream Dependencies | None declared | `_DEPENDENCIES.md` |
| Declared Downstream Dependencies | None declared | `_DEPENDENCIES.md` |
| Decomposition Frozen | Gate 7 final published snapshot 2026-05-24 | `_REFERENCES.md` |

## Construction (Anticipated Artifacts)

Artifacts the Scope of Work compiles or references, sourced from the artifact register entries that map to this deliverable.

| Artifact | Artifact Type | Source |
|---|---|---|
| Package scope of work (ART-E806968D4A) | EPC Scope of Work | `ARTIFACT_REGISTER.csv` |
| Tagged equipment and package identity list (ART-764F78E24A) | Tagged Equipment Evidence | `ARTIFACT_REGISTER.csv` |
| Package function and whole-facility integration narrative (ART-0F86ED2722) | EPC Integration Narrative | `ARTIFACT_REGISTER.csv` |
| Package responsibility assignment record (ART-42A035696B) | Responsibility Evidence | `ARTIFACT_REGISTER.csv` |

Major-equipment text content TBD: specific tagged equipment for PKG-044 is not enumerated in the locally accessible decomposition rows (source slice in Workbook Packages row 46 not opened in this run).

## Interfaces (carried as datasheet-relevant context)

Physical interface set assigned to PKG-044 in the interface register; the SoW narrative must acknowledge each.

| Interface ID | Type | Status | Source |
|---|---|---|---|
| IFC-A0182B4C75 | Process Piping | YES | `INTERFACE_REGISTER.csv` |
| IFC-9E42D79051 | Utility Piping | YES | `INTERFACE_REGISTER.csv` |
| IFC-0DD8B45540 | Electrical Power | YES | `INTERFACE_REGISTER.csv` |
| IFC-20C7248CDB | I&C / Control Cabling | YES | `INTERFACE_REGISTER.csv` |
| IFC-0664000480 | Communications / Network | YES | `INTERFACE_REGISTER.csv` |

## References

- `_CONTEXT.md` — deliverable identity and anticipated artifacts.
- `_REFERENCES.md` — authoritative decomposition basis pointers.
- `_DEPENDENCIES.md` — declared dependency view.
- GATE-07 Final Published PROJECT_DECOMP snapshot (2026-05-24):
  - `DELIVERABLE_REGISTER.csv`
  - `PACKAGE_REGISTER.csv`
  - `ARTIFACT_REGISTER.csv`
  - `INTERFACE_REGISTER.csv`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
  - `OBJECTIVE_PACKAGE_MAP.csv`
  - `SCOPE_LEDGER.csv`
- Cited but not opened in this run (location TBD within source): Workbook Packages row 46 (Excel); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
