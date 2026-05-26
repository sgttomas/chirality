# Guidance — DEL-099-03 Construction Work Package (PKG-099)

> Directional guidance for the EPC Integrator team executing the Construction Work Package for the truck product (condensate) loading stations in PKG-099 at the 03-25 Liquids Hub.

## Purpose

This Construction Work Package exists because PKG-099 supplies an engineered equipment package (vendor-owned truck loading stations and associated equipment) that the EPC Integrator must physically install, tie into the 03-25 facility, commission, inspect, accept, and turn over. The package handles custody-transfer-quality loading of sweet stabilized condensate to atmospheric trucks, so it carries metering, electrical, F&G, and spill-containment integration responsibilities in addition to the mechanical/process tie-ins (PACKAGE_REGISTER.csv row PKG-099; DELIVERABLE_REGISTER.csv row DEL-099-03; DBM SEC-06 Liquids Hub Process).

## Principles

- **Vendor-EPC boundary discipline.** Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package. EPC Integrator owns integration: interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. The Construction Work Package must make this boundary explicit at every interface (PACKAGE_REGISTER.csv row PKG-099).
- **Interface coverage by type.** PKG-099 declares eleven applicable interface types (including Product Loading and Fire & Gas / Safety Systems, which are not present in many sibling packages); each must be addressed in the workface plan and on the turnover checklist (PACKAGE_REGISTER.csv row PKG-099).
- **Source-grounded acceptance.** Construction acceptance criteria flow from 26020-Package_Requirements.docx heading 51 (package requirements) and the 26020-03-PT-RFQ-23-001 RFQ. Where the source slice is not text-accessible, mark `location TBD` rather than invent clause references.
- **Cold-climate site basis.** -40 deg C ambient governs equipment selection, winterization, heat tracing, loading-arm cold-weather handling, and concrete pour planning at this site (DBM Site Basis; SEC-11; SEC-12).
- **Spill, drainage, and static-electricity discipline.** Truck loading is a high-consequence interface for condensate releases and ignition. Spill containment, drainage segregation, static bonding, and F&G coverage are inspectable items at turnover (DBM SEC-11 Roads and Access; Surface Water and Drainage; SEC-13 references).
- **Custody-transfer integrity.** Loading meters must be installed and proved before first product load; metering installation tolerances, straight-run requirements, and proving access are constructibility items, not just measurement items (DBM SEC-09 Metering context; ASSUMPTION on standard practice).

## Considerations

- The package interfaces with the condensate booster pumps (P-9211-2 / P-9221-2) and condensate loading pumps (one per station), and pulls from the product condensate storage tanks; sequencing of tie-ins must respect commissioning logic of upstream storage and pumping systems (DBM Condensate Storage and Product Handling).
- Vapour handling for truck loading must be coordinated with the liquids hub VRU basis (two 200 hp electric-drive VRUs collecting tank-system vapours); the truck-loading vapour return point and routing are TBD in the accessible source set (DBM Vapour Recovery).
- The number of truck loading stations is a source conflict (PACKAGE_REGISTER: 2 stations 2x2; DBM SEC-06/SEC-10: 3 stations, one loading pump per station). Workface scope, civil slab quantity, electrical tie-in count, and metering count all scale with this number — it must be resolved early and recorded in the Conflict Table.
- Electrical supply is from the shared 04-25 cross-facility system; tie-in scheduling must coordinate with 04-25 commissioning windows (DBM SEC-12).
- F&G detection placement (LEL, H2S, methyl mercaptan, fire) for truck loading is TBD pending detailed safety design; the workface plan should reserve placeholders rather than firm device counts (DBM SEC-13 references).
- Truck access, queuing, and turning radii are civil constructability items; coordinate with the plot plan, retention pond, and adjacent caustic/H2O2/produced-water truck-out routing (DBM SEC-11).
- Inspection and turnover artifacts feed DEL-099-06 (EPC Vendor Package Review and Acceptance); evidence captured here is consumed downstream (DELIVERABLE_REGISTER.csv).

## Trade-offs

- **Civil pour timing vs winter window.** Truck-loading slabs are large flat pours that benefit from warm-season placement; deferring to summer trades construction schedule against winter concrete cost and risk.
- **Metering proving sequence.** Proving meters before facility-level commissioning gives clean baseline but may require temporary product or recirculation; proving after first product can compress the commissioning window and risk lost loading availability.
- **Loading-arm pre-commissioning testing.** Functional testing of loading arms with water trades early defect detection against the cost of water sourcing and disposal; loading-arm vendor recommendations should govern.
- **F&G integration timing.** Bringing F&G live before first hydrocarbon improves safety but requires the BPCS/ESD integration to be complete; integration delay shifts first-load schedule.
- **Static-bonding test method.** Continuous-monitoring static-bonding interlocks (interlocked to pump permissive) versus checklist-based bonding verification per load — trade between equipment cost and operations procedure burden.

## Examples

- The Construction Interface and Turnover Checklist for PKG-099 should enumerate one row per declared interface type per loading station (eleven interface types × N stations where N is the resolved station count), each with EPC and Vendor sign-off columns (ASSUMPTION on structure; basis: PACKAGE_REGISTER.csv interface types list).
- Workface packages should be sized to ~one station per package (civil/slab, mechanical/piping, electrical/instrumentation, metering, commissioning) for crew scheduling (ASSUMPTION; conventional practice).
- The narrative should explicitly cite the EPC/Vendor boundary at each of: loading-arm flange, metering skid flange, control-panel terminal strip, electrical MCC feeder, F&G junction box, drain/containment tie-in flange (ASSUMPTION; conventional truck-loading split).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-099-03-01 | Number of truck loading stations: PACKAGE_REGISTER row PKG-099 deliverable narrative states "Two truck loading and unloading stations, each capable of loading two trucks simultaneously (2x2)". DBM SEC-06 Condensate Storage and Product Handling and SEC-10 Miscellaneous Facilities state "three product truck-loading stations, each with a dedicated loading pump". | PACKAGE_REGISTER.csv row PKG-099 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling; Miscellaneous Facilities | Datasheet Attributes (station count); Specification R-099-03-01, R-099-03-06; Workface plan scope; Checklist row count | Treat as TBD until final vendor equipment list and RFQ 26020-03-PT-RFQ-23-001 are read; do not pick a count by default | TBD |
| C-099-03-02 | Package-level clause requirements: package name and PACKAGE_REGISTER point to 26020-Package_Requirements.docx package heading 51 and the RFQ 26020-03-PT-RFQ-23-001 (both binary .docx), which were not text-accessible this run. Clause-level installation, metering, F&G, and static-bonding criteria therefore remain TBD. | PACKAGE_REGISTER.csv row PKG-099 (Word Source Basis) | 26020-Package_Requirements.docx heading 51 / RFQ 26020-03-PT-RFQ-23-001 (binary) | Specification R-099-03-02, R-099-03-05, R-099-03-09, R-099-03-10, R-099-03-11; Datasheet Construction; Procedure clause references | Treat package-requirements heading 51 and the RFQ as governing once their slices are text-accessible; do not invent clause numbers in the interim | TBD |
| C-099-03-03 | Truck-loading vapour return routing to the VRU: DBM Vapour Recovery describes VRU collection from condensate and produced-water tank systems and "selected process vents as defined by the active process basis"; truck-loading vapour collection routing is not explicit in the accessible source set. | DBM SEC-06 Vapour Recovery | (no second source — gap) | Datasheet Conditions (Vapour handling); Specification R-099-03-06 (interface coverage); Procedure Steps 4 and 5 | Reserve a vapour-return tie-in placeholder; resolve when active process basis / vendor scope is read | TBD |
