# Specification: DEL-012-01_scope-of-work — Scope of Work

## Scope

This specification defines the required content and control checks for the EPC Integrator Scope of Work for `PKG-012`, the 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package.

The Scope of Work shall cover:

- package identity for `PKG-012`, workbook ID 12, workbook row 14, WBS 02, CoA tracking number 26020-02-30-003;
- the package's Electrical discipline classification;
- the vendor/EPC responsibility split accepted in Gate 7;
- the package function and whole-facility integration narrative, using `TBD` where the available source slice does not provide detail;
- the interface boundaries identified in Workbook Packages row 14: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports;
- anticipated artifacts listed for `DEL-012-01_scope-of-work`.

The Scope of Work shall not invent detailed UPS design parameters that are not present in the accepted source slice or Gate 7 decomposition registers.

## Requirements

| Req ID | Requirement | Source / basis | Verification |
|---|---|---|---|
| SOW-012-01 | The document shall identify the package as `PKG-012`, 10KVA AC UNINTERRUPTIBLE POWER SUPPLY, workbook ID 12, workbook row 14, WBS 02, CoA tracking number 26020-02-30-003. | Workbook Packages row 14; Gate 7 `PACKAGE_REGISTER.csv` | Check identity fields against workbook row and package register. |
| SOW-012-02 | The document shall state that the package discipline is Electrical. | Workbook Packages row 14; Gate 7 `PACKAGE_REGISTER.csv` | Check discipline field. |
| SOW-012-03 | The document shall state that the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. | Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 PROJECT_DECOMP responsibility model | Check responsibility section. |
| SOW-012-04 | The document shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 PROJECT_DECOMP responsibility model | Check responsibility section. |
| SOW-012-05 | The document shall include interface boundaries for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. | Workbook Packages row 14; Gate 7 `INTERFACE_REGISTER.csv` | Check interface register alignment. |
| SOW-012-06 | The document shall list the anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | `_CONTEXT.md`; Gate 7 `ARTIFACT_REGISTER.csv` | Check artifact list. |
| SOW-012-07 | The document shall mark unavailable technical details as `TBD` rather than assigning unsupported values. | Four-documents no-invention rule; `_REFERENCES.md` missing/deferred source note | Review for unsupported technical values. |
| SOW-012-08 | The document shall treat objective mappings as context and not as clause-level design requirements unless supported by source material. | Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`; four-documents objective-association guidance | Check objective references are contextual. |

## Standards

| Standard / governing basis | Status |
|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Available and accepted as upstream decomposition truth. |
| `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 14 | Available local source slice for package identity and interface facts. |
| UPS-specific electrical standards, runtime criteria, battery standards, environmental criteria, or testing standards | TBD; not present in the available deliverable-specific source slice. |
| DBM-Comp_and_Liquids electrical basis | Directionally relevant through Gate 7 objective/package mapping for WBS 02, but no deliverable-specific clause was reinterpreted for this Phase 2.2 run. |

## Verification

Verification shall include:

- identity check against Workbook Packages row 14 and Gate 7 `PACKAGE_REGISTER.csv`;
- interface check against Workbook Packages row 14 and Gate 7 `INTERFACE_REGISTER.csv`;
- artifact check against `_CONTEXT.md` and Gate 7 `ARTIFACT_REGISTER.csv`;
- responsibility check against Gate 7 package responsibility model;
- no-invention check confirming unsupported UPS design details remain `TBD`;
- dependency check confirming no declared upstream blockers exist in `_DEPENDENCIES.md`.

## Documentation

The completed EPC Scope of Work package should include or point to:

- package scope of work;
- tagged equipment and package identity list;
- package function and whole-facility integration narrative;
- responsibility assignment record;
- interface boundary summary for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports;
- list of `TBD` technical data requiring human or source follow-up.
