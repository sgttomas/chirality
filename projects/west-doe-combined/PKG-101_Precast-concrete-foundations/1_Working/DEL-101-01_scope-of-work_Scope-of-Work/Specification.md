# Specification: DEL-101-01 Scope of Work

## Scope

This deliverable shall define the EPC Scope of Work for PKG-101, "Precast concrete foundations," as a distinct Structural package under WBS 01. It shall include the package identity, source basis, boundaries, source-supported interfaces, whole-facility integration narrative, and responsibility assignment record.

The scope shall cover SOW-0257 from the accepted Gate 7 decomposition basis: carry the workbook-defined Structural package "Precast concrete foundations" as a distinct flat project package for WBS 01. Source: Gate 7 `SCOPE_LEDGER.csv`, SOW-0257.

The scope excludes package-specific precast element counts, dimensions, reinforcement schedules, pour quantities, final geotechnical values, final survey values, final plot-plan coordinates, final compressor dynamic analysis values, and final detailed design criteria unless those inputs are provided by authoritative sources. These items are currently `TBD`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-REQ-101-01 | The Scope of Work shall identify PKG-101 as "Precast concrete foundations," Discipline Structural, WBS 01, CoA tracking number 26020-01-36-001. Source: Gate 7 `PACKAGE_REGISTER.csv`, PKG-101; workbook Packages row 102. | Confirm identity fields match Datasheet and Gate 7 package row. |
| SOW-REQ-101-02 | The Scope of Work shall state that the package is a distinct flat project package as recorded by SOW-0257. Source: Gate 7 `SCOPE_LEDGER.csv`, SOW-0257. | Confirm SOW-0257 is cited and the package is not merged with other PKGs without source evidence. |
| SOW-REQ-101-03 | The Scope of Work shall include the source-supported interfaces marked for Workbook Packages row 102: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-101 (IFC-26343B703C, IFC-BED3DE4194); `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 102. | Confirm both interface types appear in the package boundary and integration sections. |
| SOW-REQ-101-04 | The Scope of Work shall identify tagged equipment as `TBD` unless a source-supported equipment list is provided for this structural package. The DBM identifies transformers and compressors as equipment whose foundation concept involves precast concrete, but does not assign these tags to PKG-101. ASSUMPTION: equipment-tag-to-package assignment is decomposition-driven, not DBM-driven. Source: Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-101-01; workbook Packages row 102; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations. | Confirm no unsupported equipment tags are introduced; ASSUMPTION is marked. |
| SOW-REQ-101-05 | The Scope of Work shall carry the DBM foundation basis: driven steel piles are the default support basis; precast concrete bearing foundations apply to transformers; precast concrete blocks supported on driven steel piles apply to compressors subject to dynamic analysis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations. | Confirm precast concrete foundation usage is described as current basis and not final design. |
| SOW-REQ-101-06 | The Scope of Work shall preserve the open requirement that compressor foundation dynamic analysis results are TBD and that compressor skid/foundation design shall consider containment and management of on-skid oil leaks. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations; External Dependencies; Assumptions/TBDs. | Confirm both open items are listed. |
| SOW-REQ-101-07 | The Scope of Work shall preserve the current civil/structural basis that geotechnical assessment and topographical survey inputs are required before final foundation, grading, drainage, and structural support design closure. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Geotechnical and Topographical Assumptions; External Dependencies. | Confirm required external inputs and open TBDs are listed. |
| SOW-REQ-101-08 | The Scope of Work shall state that grading and drainage interfacing with foundations is to prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management. | Confirm grading/drainage interface narrative includes the surface-water containment intent. |
| SOW-REQ-101-09 | The Scope of Work shall distinguish EPC Integrator scope definition from field construction responsibility. Field construction, including grading, piling, and foundation work and setting of modules, pipe racks, and equipment on foundations, is assigned to Tourmaline field construction scope. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary. | Confirm responsibility assignment record separates scope definition from field construction execution. |
| SOW-REQ-101-10 | The Scope of Work shall include the integration narrative tying PKG-101 to the supported objectives OBJ-001 (04-25 Deepcut facility scope) and OBJ-008 (civil/structural/site/foundation scope). ASSUMPTION (PACKAGE_HEURISTIC): objective association is at package level via Gate 7 mapping. Source: Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-101-01. | Confirm objectives are cited as directional context, not derived requirements. |

## Standards

| Standard or basis | Applicability | Source |
|---|---|---|
| National Building Code of Canada | Building, structural, foundation, snow/rain/wind/seismic loading basis where applicable | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| CAN/CSA-S16 Design of Steel Structures | Steel design basis where structural steel (e.g., embedded supports, anchorage) is implicated | Same as above |
| CAN/CSA A23.3 Design of Concrete Structures | Concrete design basis for precast concrete foundations and bearing elements | Same as above |
| Canadian Foundation Engineering Manual | Foundation engineering basis | Same as above |
| CSA G40.20/G40.21 (350W for W-flange and HSS; 300W for channels, plates, angles) | Structural steel material basis where applicable to precast concrete foundation interfaces | Same as above |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing basis directly applicable to precast concrete production and acceptance | Same as above |
| Rational Method, Q = CIA | Runoff calculation basis for grading/drainage interface | Same as above |
| Manning's equation | Ditch and culvert sizing basis for grading/drainage interface | Same as above |

## Verification

- Verify the package identity against Gate 7 `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, and workbook Packages row 102.
- Verify that only the two source-supported interface types are claimed unless additional source evidence is added.
- Verify that the DBM foundation basis for transformers and compressors is described as current basis, not final design.
- Verify that all final design parameters depending on geotechnical assessment, topographical survey, plot plan, compressor dynamic analysis, or detailed engineering remain `TBD` until source-supported.
- Verify that responsibility language does not assign vendor-package ownership; the accepted package row states EPC Integrator or discipline subcontractor responsibility is source-dependent.
- Verify that concrete and structural standards are cited as governing basis without inventing clause-level requirements.
- Verify that objective association language is marked ASSUMPTION under PACKAGE_HEURISTIC mode.

## Documentation

The completed Scope of Work shall include:

- package scope of work;
- tagged equipment and package identity list, with tagged equipment marked `TBD` if not source-supported;
- package function and integration narrative;
- responsibility assignment record;
- interface basis for Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports;
- foundation basis carried from DBM SEC-11 for transformers, compressors, and the default driven-steel-pile concept;
- list of open inputs and `TBD` items requiring later closure (geotechnical, topographical, plot plan, compressor dynamic analysis, compressor skid leak management arrangement).
