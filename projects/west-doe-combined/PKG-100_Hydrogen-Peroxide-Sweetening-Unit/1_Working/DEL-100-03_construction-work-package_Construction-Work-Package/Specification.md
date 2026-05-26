# Specification: DEL-100-03_construction-work-package — Construction Work Package

## Scope

This specification defines the minimum content requirements for the PKG-100 Construction Work Package for the Hydrogen Peroxide Sweetening Unit. The package covers how the vendor-supplied H2O2 sweetening package and its self-framing building will be physically installed, built, inspected, turned over, and tied into the larger 03-25 facility systems.

The work package shall include:

- construction work package content for PKG-100;
- installation and tie-in workface plan content;
- construction interface and turnover checklist content;
- interface controls for all PKG-100 interfaces: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

Exclusions: Package internal engineering, package design, vendor documentation, and physical equipment supply (H2O2 pumps, reactors, static mixer, 400 BBL H2O2 tank, additional PFD-listed equipment) are Package Vendor scope per Gate 7 and PACKAGE_REGISTER.csv row PKG-100; the Construction Work Package does not redesign these items. Per SOW-0110, interconnecting piping, DCS integration, foundations, and electrical supply to MCC are "by others" relative to the vendor package and are EPC-Integrator construction scope (i.e., they are covered by THIS Construction Work Package, not by the vendor). No further package-specific exclusions are stated in source materials (TBD).

## Requirements

| Req ID | Requirement | Verification |
|---|---|---|
| CWP-100-001 | The Construction Work Package shall identify the package as PKG-100, Hydrogen Peroxide Sweetening Unit, WBS 03, CoA tracking number 26020-03-27-001, Mechanical discipline. | Check against workbook Packages row 63 and Gate 7 package/deliverable registers. |
| CWP-100-002 | The Construction Work Package shall include a construction-facing plan for physical installation, construction, inspection, turnover, and tie-in to larger facility systems. | Confirm document sections or attached workface plan cover each named function. |
| CWP-100-003 | The Construction Work Package shall address every PKG-100 package interface: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | Cross-check interface matrix/checklist against workbook Packages row 63 and INTERFACE_REGISTER.csv rows for PKG-100. |
| CWP-100-004 | The Construction Work Package shall preserve the Package-Vendor / EPC-Integrator split: Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Review responsibility matrix against PACKAGE_REGISTER.csv row PKG-100 and OBJECTIVE_REGISTER.csv OBJ-004. |
| CWP-100-005 | The Construction Work Package shall plan and execute the SOW-0110 "by others" items as EPC-Integrator construction scope: interconnecting piping; DCS integration tie-ins; foundations (for the vendor package and the self-framing building); electrical supply to MCC. | Confirm workface plan and turnover checklist cover each item; check open-item register for residual TBDs. |
| CWP-100-006 | The Construction Work Package shall include the field erection of the self-framing building called out in SOW-0109. | Confirm workface plan covers building erection sequencing, lifts, anchorage, weather closure, and inspection holdpoints. |
| CWP-100-007 | The Construction Work Package shall plan offloading, setting, and anchoring of the vendor-supplied major equipment: Hydrogen Peroxide Pumps; Hydrogen Peroxide Reactors; Static Mixer; 400 BBL Hydrogen Peroxide Storage Tank; additional PFD equipment. | Cross-check setting plan against vendor general arrangement, shipping splits, and rigging plan. |
| CWP-100-008 | Electrical hookup planning shall reflect the package driver basis: 575V / 3PH / 60 Hz motors fed from a 600V MCC, with DOL or VFD starting, and one local control station (H-O-A or On-Off) adjacent to each motor, hard-wired back to the motor starter circuit in the MCC by the field construction contractor. | Check single-line and termination drawings against DBM-Comp_and_Liquids SEC-12 (600V MCC narrative) and SOW-0110. |
| CWP-100-009 | The Construction Work Package shall carry sour-service, relief/flare, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory requirements applicable to the installed package per Gate 7 (OBJ-009). | Review interface checklist and turnover record for fire/gas devices, drains/containment, relief routing, and sour-service tags. |
| CWP-100-010 | The Construction Work Package shall identify all unresolved inputs affecting construction readiness, including: pump capacity (TBC, Vendor to design); package design conditions (TBC); vendor design of pumps, reactors, and static mixer; DCS integration scope detail; foundation design for the vendor package and the self-framing building; final electrical loads from the MCC; and any open items in INTERFACE_REGISTER or OPEN_ISSUES affecting PKG-100. | Review open-item log and turnover checklist. |
| CWP-100-011 | The Construction Work Package shall carry operability, maintainability, sparing, isolation, winterization, vendor-document, commissioning, turnover, and open-item closure evidence per OBJ-010 (handoff readiness). | Verify turnover package indexes vendor documents, sparing, isolation list, winterization (consistent with -40 °C / +35 °C ambient design basis), commissioning records, and closed/deferred open items. |
| CWP-100-012 | ASSUMPTION: Objective associations (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010) were carried from `_CONTEXT.md` under the package-grouping heuristic and are best-effort context, not deliverable-level confirmed requirements. | Human review of objective-deliverable mapping. |

## Standards

| Standard or basis | Applicability | Source |
|---|---|---|
| Vendor package engineering standards (per 26020-Package_Requirements.docx) | Vendor scope — pumps, reactors, static mixer, tank, building — engineered per Vendor's controlled engineering practice; specific clauses TBD because exact extract of the Word source is not locally machine-readable (location TBD). | 26020-Package_Requirements.docx package heading 52 (referenced via decomposition) |
| 03-25 facility DBM (Comp_and_Liquids) governing basis | Governs facility-side construction scope, MCC/motor wiring, building/structural conventions, environmental and ambient design conditions, and construction-scope items applied to this package. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Construction Scope Summary; SEC-04; SEC-12 |
| Sour-service, environmental, regulatory, codes-and-standards basis | Carried into the package per OBJ-009; specific codes (e.g., CSA Z662 sour-service applicability) TBD because applicable clauses are not directly extracted from source slices for this deliverable. | OBJECTIVE_REGISTER.csv OBJ-009; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-15 (location TBD for clause-level requirements) |

## Verification

The Construction Work Package is ready for controlled review when:

- identity fields match Gate 7 and workbook row 63;
- all PKG-100 interface facts (13 interface types listed above) are carried into the construction interface checklist;
- the Vendor / EPC Integrator responsibility split is clearly stated;
- each SOW-0110 "by others" item (interconnecting piping, DCS integration, foundations, electrical supply to MCC) has a workface plan section;
- the self-framing building erection sequence is documented;
- all `TBC` / `TBD` values cited above are listed in the open-item register or are backed by vendor-supplied data;
- inspection and turnover records are named, even where final forms remain TBD.

## Documentation

The following documentation shall be produced or attached to the Construction Work Package:

- construction work package;
- installation and tie-in workface plan;
- construction interface and turnover checklist (all 13 PKG-100 interface types);
- responsibility matrix distinguishing Package-Vendor scope from EPC-Integrator construction scope;
- open input and TBD register (capacity TBC, design conditions TBC, DCS integration detail, foundation design, MCC loads, OPEN_ISSUES residuals);
- inspection and turnover record index, with final forms TBD;
- vendor document references list (linked to DEL-100-05_vendor-document-turnover-package).
