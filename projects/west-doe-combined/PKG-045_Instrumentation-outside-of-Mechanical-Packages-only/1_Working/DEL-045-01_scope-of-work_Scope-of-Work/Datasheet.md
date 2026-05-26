# Datasheet: DEL-045-01_scope-of-work — Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-045-01_scope-of-work | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Name | Scope of Work | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| ParentPackageID | PKG-045 | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Package Name | Instrumentation (outside of Mechanical Packages only) | PACKAGE_REGISTER.csv |
| Workbook Row | 47 | PACKAGE_REGISTER.csv |
| Workbook Package ID | 45 | PACKAGE_REGISTER.csv |
| CoA Tracking Number | 26020-01-32-002 | PACKAGE_REGISTER.csv |
| WBS Code | 03 | PACKAGE_REGISTER.csv |
| Discipline | Instrumentation | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Type | EPC Scope of Work | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Mandatory | TRUE (Gate 5 EPC anchor) | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Scope-of-Work Item Covered | SOW-0046 | DELIVERABLE_REGISTER.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Plug-n-play package philosophy applies | TRUE | INTERFACE_REGISTER.csv (Gate 6 disposition note) |
| Instrumentation field supports included in package scope | TRUE (per Gate 6 disposition where applicable) | INTERFACE_REGISTER.csv |
| Instrumentation power included in package scope | TRUE (per Gate 6 disposition where applicable) | INTERFACE_REGISTER.csv |
| Instrumentation comms included in package scope | TRUE (per Gate 6 disposition where applicable) | INTERFACE_REGISTER.csv |
| Vendor-package ownership model | None inferred from sources | PACKAGE_REGISTER.csv |
| Package-level exclusions | TBD; no package-specific exclusions stated in source | PACKAGE_REGISTER.csv |
| Local 03-25 instrument-air compressors | Superseded; instrument air supplied from 04-25 | 3-25_Comp_and_Liquids_DBM.md (Instrument Air section) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Minimum ambient design temperature | -40 deg C (site basis); governs exposed instrumentation, control panels, field devices unless a more severe process/vendor condition applies | 3-25_Comp_and_Liquids_DBM.md |
| 03-25 instrument-air interface demand | 393 SCFM TBC | 3-25_Comp_and_Liquids_DBM.md (Instrument Air Interface) |
| Combined 03-25/04-25 instrument-air demand | 1,113 SCFM TBC | 3-25_Comp_and_Liquids_DBM.md |
| Remaining 03-25 instrument demand reference | 100 SCFM TBC | 3-25_Comp_and_Liquids_DBM.md |
| Power/control separation requirement | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing | 3-25_Comp_and_Liquids_DBM.md (Electrical) |

## Construction

| Item | Value | Source |
|---|---|---|
| Tagged equipment basis | Workbook-defined Instrumentation package items under PKG-045, WBS 03 | PACKAGE_REGISTER.csv |
| Major-equipment text | TBD (no detailed major-equipment text in current source slice beyond DBM utility-level statements) | TBD |
| Package buildings / self-framing enclosures | Coordinated with civil, electrical, controls, and instrumentation sections per DBM | 3-25_Comp_and_Liquids_DBM.md |
| Field installation included | Shipped-loose instruments and valves, home-run cabling, terminations (per DBM construction scope) | 3-25_Comp_and_Liquids_DBM.md |

## Applicable Interface Types

| Interface ID | Counterpart Discipline | Active | Source |
|---|---|---|---|
| IFC-33F8A9F366 | Process Piping | YES | INTERFACE_REGISTER.csv |
| IFC-AE76B11E50 | Utility Piping | YES | INTERFACE_REGISTER.csv |
| IFC-2D030CA850 | Electrical Power | YES | INTERFACE_REGISTER.csv |
| IFC-210F46B073 | I&C / Control Cabling | YES | INTERFACE_REGISTER.csv |
| IFC-9DAC4D3C4D | Communications / Network | YES | INTERFACE_REGISTER.csv |

## Anticipated Artifacts (this Scope of Work deliverable)

| Artifact ID | Artifact | Source |
|---|---|---|
| ART-E7B3409573 | Package scope of work | ARTIFACT_REGISTER.csv |
| ART-F40323895F | Tagged equipment and package identity list | ARTIFACT_REGISTER.csv |
| ART-F820619A3E | Package function and whole-facility integration narrative | ARTIFACT_REGISTER.csv |
| ART-34E643FBEB | Package responsibility assignment record | ARTIFACT_REGISTER.csv |

## Objectives Associated (PACKAGE_HEURISTIC — ASSUMPTION)

OBJ-002; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-010 — associated via PKG-045 package-grouping heuristic per `_CONTEXT.md` and DELIVERABLE_REGISTER.csv. ASSUMPTION (best-effort mapping) until human-confirmed.

## References

- `_CONTEXT.md`
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot)
- PACKAGE_REGISTER.csv (GATE-07 snapshot)
- INTERFACE_REGISTER.csv (GATE-07 snapshot)
- ARTIFACT_REGISTER.csv (GATE-07 snapshot)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Workbook Packages row 47 — location TBD (source slice not locally copied)
