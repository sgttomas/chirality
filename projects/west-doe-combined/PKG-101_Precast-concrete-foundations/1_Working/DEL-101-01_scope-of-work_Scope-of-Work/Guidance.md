# Guidance: DEL-101-01 Scope of Work

## Purpose

This document guides preparation of the PKG-101 Scope of Work. The deliverable exists to anchor the Structural package "Precast concrete foundations" for WBS 01, identify its source-supported interfaces, state its package function and boundaries, and provide an integration narrative for downstream package datasheet, construction work package, and discipline production package work.

Source basis: Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, and workbook Packages row 102.

## Principles

- Treat workbook Packages row 102 and Gate 7 registers as the package identity authority.
- Treat accessible DBM civil/structural sections (DBM-Deepcut SEC-11 in particular) as source basis for foundation, geotechnical, survey, governing-code, and external-input requirements.
- Frame precast concrete foundations narrowly: the DBM identifies them as a specific support concept used for transformers (precast bearing foundations) and for compressors (precast block on driven steel piles). The default support basis remains driven steel piles for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures.
- Use `TBD` for package-specific element counts, dimensions, reinforcement schedules, pour quantities, final geotechnical parameters, final survey data, final drainage sizing, plot-plan coordinates, and compressor dynamic analysis results until authoritative inputs are available.
- Do not invent tagged equipment for this structural package. The accepted deliverable requires a tagged equipment and package identity list, but the accessible row does not identify package-specific tags. The DBM identifies equipment types whose foundation concept uses precast concrete; it does not assign equipment tags to PKG-101.

## Considerations

The accepted package row identifies two interface types: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. These interfaces should drive the scope boundary and integration narrative.

The DBM identifies two distinct precast concrete applications: precast concrete bearing foundations for transformers (no open requirement identified) and precast concrete blocks for compressors supported on driven steel piles subject to dynamic analysis (with open compressor dynamic analysis TBD and skid leak-containment design TBD). The Scope of Work should preserve both applications and the corresponding open items.

Field construction responsibility is not the same as EPC scope definition responsibility. The Comp_and_Liquids DBM Construction Scope Summary assigns grading, piling, foundation work, and setting of modules/pipe racks/equipment on foundations to Tourmaline field construction scope, while Gate 7 assigns this Scope of Work deliverable to the EPC Integrator.

OBJ-001 and OBJ-008 are associated to this deliverable via Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`. The association is recorded as directional context per the PACKAGE_HEURISTIC objective-association mode.

## Trade-offs

| Topic | Conservative treatment |
|---|---|
| Package breadth | Include the source-supported structural and grading interfaces and DBM foundation basis, but avoid expanding into civil pads, retention pond, roads, or steel-pile-only structures unless directly needed for PKG-101 boundaries. |
| Design detail | State current design basis (driven steel piles default; precast for transformers; precast block on piles for compressors) and external inputs, not final design values. |
| Responsibility | Separate EPC Integrator deliverable ownership from Tourmaline field construction execution. |
| Standards | List DBM governing standards (NBCC, CAN/CSA A23.3, CSA A23.1/A23.2, Canadian Foundation Engineering Manual, etc.) as basis items; do not create clause-level requirements without source text. |
| Compressor support concept | Carry the alternate "steel skid welded directly to piles" concept as a TBD verification item only; the DBM marks it as unlikely. |

## Examples

- Supported: "PKG-101 carries Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces." Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-101; workbook Packages row 102.
- Supported: "Transformers are generally supported on precast concrete bearing foundations." Source: DBM-Deepcut SEC-11 Piles and Foundations.
- Supported: "Compressors use precast concrete blocks supported on driven steel piles, subject to dynamic analysis (results TBD)." Source: DBM-Deepcut SEC-11 Piles and Foundations.
- Supported: "Final geotechnical parameters are TBD pending completion and review of the geotechnical assessment." Source: DBM-Deepcut SEC-11.
- Unsupported unless later sourced: "PKG-101 supplies a specific count of precast pads, reinforcement schedule, pour volume, or equipment tag list."

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-101-01-001 | Package name "Precast concrete foundations" is narrow, while DBM-Deepcut SEC-11 Piles and Foundations treats precast concrete as a sub-application within a default driven-steel-pile basis used across many structures. Reading the package as a full "foundations" package risks scope creep beyond precast elements. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-101 (name + Structural discipline + WBS 01) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations | Datasheet Attributes/Conditions; Specification Scope and Requirements; Guidance Principles | PROPOSAL: bound PKG-101 to the precast concrete applications identified by the DBM (transformer bearing foundations and compressor precast blocks on driven steel piles) and treat default-pile foundations as outside PKG-101 unless human ruling extends the package | TBD |
| CONF-101-01-002 | Equipment tag list is required by the deliverable definition, but accessible sources do not assign tags to PKG-101. The DBM names equipment categories (transformers, compressors) for precast application without project tag IDs at the package level. | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-101-01 anticipated artifact "tagged equipment and package identity list" | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations; workbook Packages row 102 | Datasheet Attributes (Tagged equipment); Specification Requirements SOW-REQ-101-04 | PROPOSAL: mark tagged equipment TBD and request human ruling on whether transformer and compressor equipment tags from other packages should be linked to PKG-101 as supported items | TBD |

## Open Items

- TBD: package-specific precast element counts, dimensions, reinforcement schedules, and pour quantities.
- TBD: final geotechnical design parameters (bearing capacity, LPILE curves, dynamic design criteria).
- TBD: final topographical survey and grade surface file content.
- TBD: final plot-plan coordinates and resulting foundation layout.
- TBD: compressor dynamic analysis results.
- TBD: detailed compressor skid/foundation arrangement for on-skid oil leak containment.
- TBD: verification of direct steel skid-to-pile welding alternative for compressors.
- TBD: package-specific tagged equipment list.
- TBD: scope-boundary disposition between PKG-101 and other foundation-bearing packages (see CONF-101-01-001).
