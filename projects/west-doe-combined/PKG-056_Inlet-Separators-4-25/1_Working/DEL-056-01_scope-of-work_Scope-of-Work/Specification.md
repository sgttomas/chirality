# Specification — DEL-056-01 Scope of Work (PKG-056 Inlet Separators 4-25)

## Scope

### In-scope

This Scope of Work governs the EPC Integrator deliverable that defines, for `PKG-056 Inlet Separators 4-25`, the package identity, tagged equipment, package function, source basis, package boundaries, and the whole-facility integration narrative. It is the anchor deliverable on which `DEL-056-02 Package Datasheet`, `DEL-056-03 Construction Work Package`, `DEL-056-04 Vendor Engineered Equipment Package`, `DEL-056-05 Vendor Document Turnover Package`, and `DEL-056-06 EPC Vendor Package Review and Acceptance` depend.

Covered scope items: `SOW-0127`, `SOW-0128`, `SOW-0129`, `SOW-0130` (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 372).

Supports objectives: `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (`_CONTEXT.md`). ASSUMPTION (package-grouping heuristic): objective associations are inherited from the package-level objective set in `PACKAGE_REGISTER.csv` row 68; not independently confirmed at deliverable-ID granularity.

### Out of scope

- Detailed package engineering, package design, vendor documentation, and physical equipment fabrication/supply (these are the Package Vendor scope captured in `DEL-056-04` and `DEL-056-05`). Source: `PACKAGE_REGISTER.csv` row 68.
- Facility-wide integration approval/acceptance evidence (handled by `DEL-056-06`).
- Standalone derivation of design values that belong in `DEL-056-02 Package Datasheet`; values appear here only as identity/integration anchors.

## Requirements

### R1 — Package identity and tagged equipment

R1.1 The Scope of Work SHALL state the package identifier `PKG-056` and the package name `Inlet Separators 4-25`. (Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 68.)

R1.2 The Scope of Work SHALL list the tagged equipment that constitutes the package per current authority: `V-1600-1` (Inlet Separators 2 — Unit 1) and `V-1700-1` (Inlet Separators 2 — Unit 2). (Source: `4-25_Deepcut_DBM.md` rows 2540, 2596–2597.)

R1.3 The Scope of Work SHALL record the unresolved installed-quantity conflict (current authority: two installed plus plot provision for a third; legacy: four inlet separator packages) and SHALL NOT silently resolve it. (Source: `4-25_Deepcut_DBM.md` §Inlet separator system; Conflict Table in `Guidance.md`.)

### R2 — Package function

R2.1 The Scope of Work SHALL describe the package function as receiving raw inlet gas from upstream and separating it into three phases — sour natural gas (vapour), sour raw condensate (light liquid), and sour water (heavy liquid). (Source: `PACKAGE_REGISTER.csv` row 68; `4-25_Deepcut_DBM.md` §Inlet separator system.)

R2.2 The Scope of Work SHALL identify the package's role upstream of the MPFF and stabilizer systems, including slug handling and liquid separation. (Source: `4-25_Deepcut_DBM.md` §Inlet separator system.)

### R3 — Source basis

R3.1 The Scope of Work SHALL cite Workbook Packages row 68 and `26020-Package_Requirements.docx` package heading 11 as the authoritative package source. (Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 68.)

R3.2 The Scope of Work SHALL cite the Word Source Basis: `Bid Docs/Budgetary/26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` and `DBM-Deepcut/4-25_Deepcut_DBM.md`. (Source: `PACKAGE_REGISTER.csv` row 68.)

### R4 — Package boundaries and interfaces

R4.1 The Scope of Work SHALL declare the applicable interface types: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. (Source: `PACKAGE_REGISTER.csv` row 68.)

R4.2 The Scope of Work SHALL identify the package boundaries between Package Vendor authority (package engineering, package design, vendor documentation, physical equipment package) and EPC Integrator authority (integration into the functional process facility, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). (Source: `PACKAGE_REGISTER.csv` row 68.)

R4.3 The Scope of Work SHALL identify downstream interfaces (MPFF heated hydrocarbon liquid outlet lines; gas processing train overhead gas) and upstream interfaces (inlet ESDV station; drive-gas tie-in upstream of plant inlet gas meters with separate per-package metering). (Source: `4-25_Deepcut_DBM.md` lines ~809, 811, 834.)

### R5 — Whole-facility integration narrative

R5.1 The Scope of Work SHALL include a narrative describing how the package integrates into the West Doe Deepcut (04-25) facility, including the upstream inlet gathering scope, downstream MPFF/stabilizer systems, drive-gas, flare/relief, drain, and utility tie-ins. (Source: `4-25_Deepcut_DBM.md` §Front-end process basis.)

R5.2 The Scope of Work SHALL incorporate the unit-level isolation principle for parallel inlet separator packages. (Source: `4-25_Deepcut_DBM.md` line ~2408.)

### R6 — Responsibility assignment record

R6.1 The Scope of Work SHALL produce a responsibility assignment record covering EPC Integrator and Package Vendor responsibilities consistent with `PACKAGE_REGISTER.csv` row 68. (Source: `_CONTEXT.md` Anticipated Artifacts; `PACKAGE_REGISTER.csv` row 68.)

### R7 — Scope item traceability

R7.1 The Scope of Work SHALL trace its content to scope items `SOW-0127`, `SOW-0128`, `SOW-0129`, `SOW-0130`. (Source: `_CONTEXT.md` Covers Scope Items.) Mapping at the SOW-item level: TBD (individual scope-item text not opened in this run; `_REFERENCES.md` does not list a deliverable-local slice).

## Standards

| Standard / Document | Role | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 11 | Authoritative package source | `_Sources/26020-Package_Requirements.docx` — binary; location TBD (clause-level reading not performed) |
| `26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` | RFQ Word source basis | `Bid Docs/Budgetary/...` — location TBD (not opened in this run) |
| `4-25_Deepcut_DBM.md` | Design basis memorandum (Deepcut) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| OGAOM Sec. 9.6.15 (spacing — flare/heater to separators) | Site-spacing context only | `4-25_Deepcut_DBM.md` lines ~283, ~297 |
| ASSUMPTION: typical EPC SOW practice (e.g., applicable ASME / API vessel codes) | Governing codes likely apply to the underlying equipment but are NOT introduced by this Scope of Work | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| R1.1, R1.2 | Documentation review: identity block matches `_CONTEXT.md` and DBM tag rows. |
| R1.3 | Documentation review: Conflict Table present in `Guidance.md`; quantity stated as "TBD pending human ruling." |
| R2.1, R2.2 | Documentation review: function narrative cites `PACKAGE_REGISTER.csv` row 68 and DBM §Inlet separator system. |
| R3.1, R3.2 | Documentation review: source-basis citations present and resolvable. |
| R4.1, R4.2, R4.3 | Documentation review: interface-type list matches `PACKAGE_REGISTER.csv` row 68 verbatim; boundary statement matches package-row construction model. |
| R5.1, R5.2 | Documentation review: integration narrative traces to DBM §Front-end process basis and unit-isolation guidance. |
| R6.1 | Documentation review: responsibility record present and consistent with package register. |
| R7.1 | Trace check: every claim in the Scope of Work resolves to one of `SOW-0127`–`SOW-0130` or is labelled ASSUMPTION/TBD. Granular SOW-item text TBD. |

## Documentation

This deliverable produces the following artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Package scope of work narrative.
- Tagged equipment and package identity list (per R1).
- Package function and integration narrative (per R2 and R5).
- Responsibility assignment record (per R6).

Companion deliverable-local files: `Datasheet.md`, `Guidance.md`, `Procedure.md`. Cross-cutting metadata files (`_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md`) are not modified by this deliverable except `_STATUS.md` via the safe-update path.
