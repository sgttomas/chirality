# Specification: DEL-032-01_scope-of-work — Scope of Work

Normative scope-of-work specification for the EPC Integrator deliverable covering PKG-032 Cathodic Protection Design and Installation.

## Scope

### In Scope

- Definition of the full PKG-032 package scope from the EPC Integrator perspective, including:
  - Tagged equipment and package identity list for the Cathodic Protection package (`26020-03-30-023`).
  - Package function and integration narrative at the facility level.
  - Responsibility assignment record between Package Vendor and EPC Integrator.
  - Source basis and boundary definition.
  - Whole-facility integration narrative covering Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network interfaces (PACKAGE_REGISTER row PKG-032).
- Documentation of facility-side interface support to the owner-provided cathodic protection system (DBM-Deepcut SEC-12 §Cathodic Protection).

### Out of Scope

- Package engineering, package design, vendor documentation, and physical equipment package — owned by Package Vendor (PACKAGE_REGISTER row PKG-032). ASSUMPTION: these are documented by a separate vendor-owned deliverable set, not by this SOW.
- Facility-level cathodic-protection design and supply — explicitly excluded from facility design per DBM-Deepcut (line 3075). The EPC Integrator's role is interface support, not CP engineering authorship.
- Package-specific exclusions beyond those stated in PACKAGE_REGISTER: TBD (none stated in source).

## Requirements

| Req ID | Requirement | Source | Verification |
|---|---|---|---|
| R-SOW-032-01 | The SOW shall identify the package tag `26020-03-30-023` and confirm WBS 03 assignment. | PACKAGE_REGISTER row PKG-032 | Cross-check tag string against PACKAGE_REGISTER |
| R-SOW-032-02 | The SOW shall enumerate Package Vendor scope (package engineering, package design, vendor documentation, physical equipment package). | PACKAGE_REGISTER row PKG-032 | Review against PACKAGE_REGISTER ownership statement |
| R-SOW-032-03 | The SOW shall enumerate EPC Integrator scope (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). | PACKAGE_REGISTER row PKG-032 | Review against PACKAGE_REGISTER ownership statement |
| R-SOW-032-04 | The SOW shall identify applicable interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network. | PACKAGE_REGISTER row PKG-032 | Cross-check against PACKAGE_REGISTER `interface_types` field |
| R-SOW-032-05 | The SOW shall state the DBM exclusion that facility design does not engineer or supply cathodic protection, and that facility design supports owner CP interfaces. | DBM-Deepcut `4-25_Deepcut_DBM.md` line 3073-3075, 3092 | Source-quote review |
| R-SOW-032-06 | The SOW shall present a tagged equipment list for the package. | `_CONTEXT.md` Anticipated Artifacts | Inspect SOW for tagged-equipment register; TBD until vendor data accepted |
| R-SOW-032-07 | The SOW shall include a responsibility assignment record (RACI-style or equivalent) covering Package Vendor and EPC Integrator. | `_CONTEXT.md` Anticipated Artifacts | Inspect SOW for responsibility record |
| R-SOW-032-08 | The SOW shall trace coverage of `SOW-0033`. | `_CONTEXT.md` Covers Scope Items | Cross-check against DELIVERABLE_REGISTER `covers_scope` |
| R-SOW-032-09 | ASSUMPTION: The SOW shall identify directional relevance to OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-009, OBJ-010. | DELIVERABLE_REGISTER row `DEL-032-01_scope-of-work` (package-grouping heuristic) | Human ruling on objective association mode |

## Standards

| Standard | Applicability | Source / Location |
|---|---|---|
| Project DBM — Deepcut Expansion (4-25) | Governs facility-side electrical and CP interface exclusion | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 |
| Project DBM — Comp and Liquids (3-25) | Governs facility-side electrical design support inclusions | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Owner cathodic-protection design basis | Authority for CP engineering content; TBD location | Not present in accessible sources; `location TBD` |
| Applicable cathodic-protection codes/standards (e.g., NACE / AMPP, CSA) | TBD: not enumerated in accessible sources | `location TBD` |

## Verification

| Verification Item | Method |
|---|---|
| Package tag and identity | Document cross-check against PACKAGE_REGISTER |
| Ownership split (Vendor vs EPC Integrator) | Document cross-check against PACKAGE_REGISTER |
| Interface types coverage | Review against PACKAGE_REGISTER `interface_types` |
| DBM exclusion statement | Source-quote audit against DBM-Deepcut SEC-12 |
| Tagged equipment list completeness | Review against vendor package datasheet when available; otherwise TBD |
| Objective coverage | Human ruling on objective-association mode |

## Documentation

Anticipated artifacts in this deliverable (`_CONTEXT.md`):

- Package scope of work narrative
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record
