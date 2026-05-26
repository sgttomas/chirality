# Specification — DEL-055-01 Scope of Work (Flare KO Drum (Low Pressure) 4-25)

> Normative scope, requirements, governing standards, verification approach, and documentation for the EPC Scope of Work production unit for PKG-055.

## Scope

### In Scope (covered by this Scope of Work)

| Item | Description | Source |
|---|---|---|
| S-1 | Carry PKG-055 ("Flare KO Drum (Low Pressure) 4-25") as a distinct flat project package for WBS 01 with the responsibility split: Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration | SCOPE_LEDGER SOW-0083 |
| S-2 | Supply one LP flare knock-out drum and one LP flare KO drum transfer pump | SCOPE_LEDGER SOW-0084 |
| S-3 | Include LP flare KO drum `V-3900-1`, transfer pump `P-3900-1`, liquid transfer to condensate slop tank, truck-out provision, and package tie-ins | SCOPE_LEDGER SOW-0085 |
| S-4 | Define and document facility-level integration responsibilities of the EPC Integrator: interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER.csv (Responsibility Description) |
| S-5 | Identify applicable interface types as: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv (Interface Types) |

### Out of Scope (excluded from this Package's Scope of Work)

| Item | Description | Source |
|---|---|---|
| X-1 | LP flare stack sizing and flare tip details (described as connected system equipment) | SCOPE_LEDGER SOW-0086 |
| X-2 | Air-assist blower (described as connected system equipment) | SCOPE_LEDGER SOW-0086 |
| X-3 | Common HP/cryo flare stack (LP element piggy-backs on it but stack is not part of this package) | DBM-Deepcut/4-25_Deepcut_DBM.md lines 2029, 2031 |

### Coverage

This Scope of Work deliverable carries the following Scope Ledger items in full: `SOW-0083`, `SOW-0084`, `SOW-0085`, `SOW-0086` (SCOPE_LEDGER.csv; cross-referenced in `_CONTEXT.md`).

## Requirements

### R-1 Package Identity and Tag Mapping (binding)

The Scope of Work shall record:

- the package identifier `PKG-055` / `26020-01-PT-17-003`,
- the package name "Flare KO Drum (Low Pressure) 4-25",
- the package's tagged equipment list (`V-3900-1`, `P-3900-1`).

Source: PACKAGE_REGISTER.csv PKG-055; SCOPE_LEDGER SOW-0084, SOW-0085.

### R-2 Package Function Statement (binding)

The Scope of Work shall state the package function: provide low-pressure flare knock-out, including liquid separation, liquid transfer to the condensate slop tank, and truck-out provision (SCOPE_LEDGER SOW-0085).

### R-3 Responsibility Split (binding)

The Scope of Work shall reproduce the workbook-defined responsibility split:

- Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package.
- EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Source: PACKAGE_REGISTER.csv (Responsibility Description); SCOPE_LEDGER SOW-0083.

### R-4 Whole-Facility Integration Narrative (binding)

The Scope of Work shall describe how the LP KO drum package fits into the facility flare system, citing at minimum:

- LP relief header size and routing (508 mm / 20 in LP relief header),
- the LP flare stack arrangement (LP element piggy-backs on the common HP/cryo flare stack),
- the connected LP equipment list (amine regeneration, TEG regeneration, VRU, reciprocating compressor seal pot).

Source: DBM-Deepcut/4-25_Deepcut_DBM.md lines 2029, 2031.

### R-5 Interface Type Coverage (binding)

The Scope of Work shall enumerate the package interface types defined in the package register row, and assign EPC Integrator vs. Package Vendor responsibility for each interface type.

Source: PACKAGE_REGISTER.csv (Interface Types column).

### R-6 Source Basis Traceability (binding)

The Scope of Work shall cite, for each in-scope statement, the source clause(s) it is derived from (workbook row, 26020-Package_Requirements.docx heading 10, DBM-Deepcut for facility integration).

Source: SCOPE_LEDGER source-basis columns (SOW-0083..0086).

### R-7 Exclusion Statement (binding)

The Scope of Work shall include an explicit exclusion list for adjacent flare-system equipment that is not part of this package (LP flare stack, common stack, air-assist blower).

Source: SCOPE_LEDGER SOW-0086.

### R-8 Objective Linkage (informational; package-grouped, ASSUMPTION)

The Scope of Work may record the package-level objective linkages: `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (objective association at the deliverable level is package-grouped — recorded as ASSUMPTION per `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`).

Source: DELIVERABLE_REGISTER.csv DEL-055-01_scope-of-work; PACKAGE_REGISTER.csv PKG-055.

## Standards

| Standard / Reference | Applicability | Locally Accessible? | Notes |
|---|---|---|---|
| 26020-Package_Requirements.docx | Source-of-truth package requirements; heading 10 governs PKG-055 | DOCX present in `_Sources/`; text not extracted to markdown locally | `location TBD` for clause-level extraction beyond the four SOW slices in SCOPE_LEDGER |
| Workbook Packages row 57 (26020-Packages_Interfaces_4_export.xlsx) | Workbook-level package definition (responsibility split, interface type list) | XLSX present in `_Sources/`; not extracted to markdown locally | Coverage captured via PACKAGE_REGISTER.csv row PKG-055 |
| 4-25 Deepcut DBM | Whole-facility integration context for the 4-25 LSD area | Locally accessible (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) | Used for R-4 facility integration narrative |
| Project EPC / regulatory codes | TBD — no governing code list stated for PKG-055 in accessible source slices | n/a | location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 | Inspect Scope of Work artifact for the listed identifiers and tags; cross-check against PACKAGE_REGISTER.csv and SCOPE_LEDGER. |
| R-2 | Inspect Scope of Work artifact for an explicit package function statement; cross-check against SOW-0085 wording. |
| R-3 | Inspect Scope of Work artifact for the responsibility split text; cross-check against PACKAGE_REGISTER.csv Responsibility Description. |
| R-4 | Inspect facility-integration narrative section; cross-check tags, header size, stack arrangement against DBM-Deepcut. |
| R-5 | Inspect Scope of Work artifact for interface type table with responsibility assignment per type. |
| R-6 | Each in-scope statement carries a citation to the SCOPE_LEDGER row, PACKAGE_REGISTER row, or DBM section that supports it. |
| R-7 | Inspect Scope of Work for explicit exclusion list including LP flare stack, common stack, and air-assist blower. |
| R-8 | Confirm objective linkage rows are present and labeled as package-grouped ASSUMPTION (per skill mode). |

## Documentation

The deliverable shall produce the four anticipated artifacts identified in `_CONTEXT.md`:

| Artifact | Description |
|---|---|
| Package scope of work | Narrative SOW document combining R-1 through R-7. |
| Tagged equipment and package identity list | Tabular listing referencing R-1. |
| Package function and integration narrative | Narrative section referencing R-2 and R-4. |
| Responsibility assignment record | Tabular assignment for R-3 and R-5 (interface-by-interface). |
