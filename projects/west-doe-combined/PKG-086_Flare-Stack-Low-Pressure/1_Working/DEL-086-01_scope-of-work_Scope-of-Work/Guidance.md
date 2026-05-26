# Guidance: DEL-086-01_scope-of-work — Scope of Work

> Directional guidance for authoring the EPC Integrator Scope of Work for PKG-086 (Flare Stack — Low Pressure). Rationale is grounded in the Gate 7 PROJECT_DECOMP snapshot; missing source detail is preserved as `TBD` rather than invented.

## Purpose

The Scope of Work is the **EPC anchor deliverable** for PKG-086. It exists to:

- Establish the package identity and boundary as a single, named, vendor-supplied production unit within the EPC's facility scope. [Source: `PACKAGE_REGISTER.csv` PKG-086; `SCOPE_LEDGER.csv` SOW-0091]
- Make the **Package Vendor vs EPC Integrator responsibility split** unambiguous so that downstream deliverables (datasheet, CWP, vendor package, document turnover, review and acceptance) inherit a consistent ownership model. [Source: `PACKAGE_REGISTER.csv` PKG-086 responsibility column; `OBJECTIVE_REGISTER.csv` OBJ-004]
- Carry the upstream source basis (workbook row 59 and 26020-Package_Requirements.docx package heading 39) forward into Gate 5 execution. [Source: `DELIVERABLE_REGISTER.csv` SourceRef]

## Principles

- **EPC integrates; Vendor engineers and supplies.** The SoW shall not assign vendor design or vendor documentation work to the EPC. [Source: `OBJECTIVE_REGISTER.csv` OBJ-004 ValidationQuestion]
- **Package-as-reference/interface.** PKG-086 is described in the source as a reference/interface package. The SoW shall treat the package as a defined interface boundary rather than as an EPC engineered system. [Source: `PACKAGE_REGISTER.csv` PKG-086 description; `SCOPE_LEDGER.csv` SOW-0092]
- **Sour-service and safety carry-through.** Sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory considerations are carried into package scope via OBJ-009. The SoW shall expose this carry-through rather than absorb it silently. [Source: `OBJECTIVE_REGISTER.csv` OBJ-009]
- **Interfaces are first-class.** All eight applicable interface types are part of the SoW's scope boundary, not afterthoughts. [Source: `INTERFACE_REGISTER.csv` PKG-086 rows]
- **Procurement-boundary preservation.** The 4-25 procurement-authority note shall be preserved verbatim until a boundary ruling changes it. [Source: `SCOPE_LEDGER.csv` SOW-0094]

## Considerations

- **Sibling deliverable separation.** Detailed datasheet content (DEL-086-02), construction workface (DEL-086-03), vendor engineering/equipment (DEL-086-04), vendor document turnover (DEL-086-05), and vendor package acceptance (DEL-086-06) are explicitly carved out. The SoW should point to siblings rather than reproduce their content.
- **Air-assist blower coupling.** The major-equipment list ties the LP flare stack to its air-assist blower. The SoW shall treat the blower as in-package rather than as an external utility supply unless the source contradicts this. [Source: `SCOPE_LEDGER.csv` SOW-0093]
- **Supplemental fuel gas / dilution gas provisions.** These are listed as part of the major included equipment and should be carried as an interface to the fuel-gas utility system (OBJ-007). [Source: `SCOPE_LEDGER.csv` SOW-0093; `OBJECTIVE_REGISTER.csv` OBJ-007]
- **Pilot, pilot proving, and auto-ignition.** These are explicitly included and have downstream implications for I&C/Control Cabling and Fire & Gas / Safety Systems interfaces. [Source: `SCOPE_LEDGER.csv` SOW-0093; `INTERFACE_REGISTER.csv` PKG-086 rows]
- **Tagged equipment list.** The full per-tag list lives in the source package heading; until that slice is locally accessible, the SoW must use `TBD — location TBD` rather than invent tag numbers. [Source: ASSUMPTION pending source slice]

## Trade-offs

- **Narrative depth vs. delegation discipline.** Adding tagged equipment detail to the SoW improves discoverability but risks duplicating DEL-086-02. Default behavior: keep the SoW at identity/list-level and let DEL-086-02 own attribute-level depth.
- **Standards naming vs. clause-level requirements.** Naming likely-applicable standards (API 537, API 521, NACE MR0175) helps downstream users orient, but writing clause-level requirements from those standards without local source slices would violate the authority hierarchy. Default behavior: name standards as ASSUMPTION, defer clause-level requirements to source-grounded later passes.
- **Procurement-boundary clarity vs. open-item exposure.** Preserving the SOW-0094 4-25/3-25 note surfaces an open boundary question; suppressing it would mislead downstream consumers. Default behavior: preserve verbatim.

## Examples

- **Example responsibility statement (verbatim from source):** "Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration." [Source: `PACKAGE_REGISTER.csv` PKG-086]
- **Example package-function statement (verbatim from source):** "Reference/interface package for the LP flare stack and associated LP flare stack blower." [Source: `PACKAGE_REGISTER.csv` PKG-086]
- Example tagged-equipment table content: `TBD — location TBD` (source: 26020-Package_Requirements.docx package heading 39; slice not yet locally copied).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| (none recorded in Pass 2) | No cross-source conflicts identified within the locally accessible decomposition snapshot for this deliverable. | n/a | n/a | n/a | n/a | n/a |

Note: cross-source conflicts cannot be fully ruled out until the 26020-Package_Requirements.docx package heading 39 source slice and the DBM SEC-15 regulatory sections are locally accessible. New conflicts may surface in a later pass with source slices in hand.
