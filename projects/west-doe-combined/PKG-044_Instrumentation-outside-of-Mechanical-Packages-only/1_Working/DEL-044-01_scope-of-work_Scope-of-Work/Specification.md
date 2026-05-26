# Specification — DEL-044-01 Scope of Work

Normative specification for the EPC Integrator Scope of Work deliverable for PKG-044, "Instrumentation (outside of Mechanical Packages only)."

## Scope

### In Scope

The Scope of Work (SoW) MUST cover the full package scope for PKG-044, including (per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`):

- Tagged equipment within the package boundary.
- Package function description.
- Source basis (workbook-traceable rationale).
- Package boundaries (what is and is not in PKG-044).
- Whole-facility integration narrative.
- Responsibility assignment record covering the package.

Scope item covered: `SOW-0045` — "Carry the workbook-defined Instrumentation package 'Instrumentation (outside of Mechanical Packages only)' as a distinct flat project package for WBS 02." (`SCOPE_LEDGER.csv`)

### Out of Scope

- Mechanical package internals: instrumentation already carried inside a Mechanical Package's vendor scope is out of PKG-044 by package definition (`PACKAGE_REGISTER.csv` — name explicitly excludes mechanical-package instrumentation).
- Package technical handoff datasheet content — owned by sibling deliverable `DEL-044-02_package-datasheet`.
- Construction work package content — owned by sibling deliverable `DEL-044-03_construction-work-package`.
- Discipline production unit content — owned by sibling deliverable `DEL-044-04_epc-instrumentation-discipline-production-package`.

### Exclusions (package-level)

`PACKAGE_REGISTER.csv` records `TBD; no package-specific exclusions stated in source materials.` This SoW therefore MUST NOT assert exclusions beyond the package-definition boundary above without source evidence.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| REQ-044-01-001 | The SoW MUST identify the package as PKG-044, Workbook ID 44, Workbook Packages row 46, WBS 02, CoA tracking number 26020-01-32-002. | `PACKAGE_REGISTER.csv` |
| REQ-044-01-002 | The SoW MUST state package discipline as Instrumentation. | `PACKAGE_REGISTER.csv` |
| REQ-044-01-003 | The SoW MUST identify EPC Integrator as the responsible party for delivering this SoW. | `DELIVERABLE_REGISTER.csv` |
| REQ-044-01-004 | The SoW MUST describe the package function consistent with the workbook narrative: an Instrumentation package for instrumentation scope located outside of Mechanical Packages, integrated into WBS 02 under the plug-n-play package philosophy. | `PACKAGE_REGISTER.csv` Description and Notes; `INTERFACE_REGISTER.csv` Gate 6 disposition |
| REQ-044-01-005 | The SoW MUST enumerate the five physical interface types recorded for the package: Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network. | `INTERFACE_REGISTER.csv` (IFC-A0182B4C75, IFC-9E42D79051, IFC-0DD8B45540, IFC-20C7248CDB, IFC-0664000480) |
| REQ-044-01-006 | The SoW MUST state the boundary caveat: "Field supports, power, and communications are not marked unless confirmed by package scope." | `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv` |
| REQ-044-01-007 | The SoW MUST record the Gate 6 disposition that instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy. | `INTERFACE_REGISTER.csv` Notes |
| REQ-044-01-008 | The SoW MUST list the tagged equipment in the package. Where the locally accessible source set does not enumerate equipment for PKG-044, equipment tag list value is TBD pending Workbook Packages row 46 (Excel) extraction. | `_CONTEXT.md` Anticipated Artifacts; ART-764F78E24A |
| REQ-044-01-009 | The SoW MUST link supported facility objectives: OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010. | `OBJECTIVE_DELIVERABLE_MAP.csv` |
| REQ-044-01-010 | The SoW MUST record the responsibility assignment for the package; if EPC Integrator vs. discipline subcontractor allocation is not yet ruled, the assignment is recorded as source-dependent / TBD. | `PACKAGE_REGISTER.csv`; ART-42A035696B |
| REQ-044-01-011 | The SoW MUST trace every claim to a source row in the GATE-07 PROJECT_DECOMP snapshot or to Workbook Packages row 46; assertions not so traceable MUST be marked ASSUMPTION or TBD. | Authority hierarchy; K-PROV-1 |
| REQ-044-01-012 | The SoW MUST cite the accepted upstream decomposition snapshot: GATE-07 Final Published 2026-05-24. | `_REFERENCES.md`; `_CONTEXT.md` |

## Standards

| Standard / Basis | Applicability | Location |
|---|---|---|
| GATE-07 Final Published PROJECT_DECOMP snapshot (2026-05-24) | Authoritative decomposition basis for this deliverable | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` |
| Workbook Packages row 46 | Authoritative workbook row that defines PKG-044 | location TBD within `_Sources/26020-Packages_Interfaces_4_export.xlsx` |
| `26020-Package_Requirements.docx` | Project-wide package requirements basis | `_Sources/26020-Package_Requirements.docx` (not opened this run; location TBD within document) |
| `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Cited as design basis pointer in PACKAGE_REGISTER notes | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (not opened this run; location TBD within document) |
| Discipline / instrumentation standards (e.g., ISA, IEEE, NEC) | TBD; not explicitly named in accessible source slice. ASSUMPTION: likely applicable but no clause-level requirement is derived here. | location TBD |

## Verification

| Req | Verification Approach |
|---|---|
| REQ-044-01-001..003 | Inspect SoW header against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. |
| REQ-044-01-004 | Review SoW narrative against package register Description, Notes, and Gate 6 disposition. |
| REQ-044-01-005 | Compare SoW interface list against `INTERFACE_REGISTER.csv` rows filtered for PKG-044. |
| REQ-044-01-006..007 | Inspect SoW for verbatim boundary caveat and Gate 6 disposition. |
| REQ-044-01-008 | Confirm SoW lists tagged equipment with source citation; if TBD, confirm TBD is labeled and traced to ART-764F78E24A and Workbook Packages row 46. |
| REQ-044-01-009 | Cross-check listed objectives against `OBJECTIVE_DELIVERABLE_MAP.csv`. |
| REQ-044-01-010 | Confirm responsibility section either names assigned party with source or records TBD with rationale (ART-42A035696B). |
| REQ-044-01-011..012 | Provenance audit: every non-trivial claim cites a register row, source row, or is labeled ASSUMPTION/TBD; SoW header cites GATE-07 snapshot. |

## Documentation

Required artifacts to issue (from `_CONTEXT.md` Anticipated Artifacts and `ARTIFACT_REGISTER.csv`):

- Package scope of work (ART-E806968D4A).
- Tagged equipment and package identity list (ART-764F78E24A).
- Package function and whole-facility integration narrative (ART-0F86ED2722).
- Package responsibility assignment record (ART-42A035696B).

Each issued artifact MUST cite GATE-07 PROJECT_DECOMP snapshot and the specific register row(s) it consumes.
