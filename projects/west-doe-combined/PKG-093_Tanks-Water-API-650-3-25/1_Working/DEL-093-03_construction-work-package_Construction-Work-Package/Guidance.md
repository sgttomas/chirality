# Guidance — DEL-093-03 Construction Work Package (PKG-093)

> Directional guidance for the EPC Integrator team executing the Construction Work Package for the two sweet produced-water storage tanks (TK-9060-2, TK-9070-2) in PKG-093 at 03-25.

## Purpose

This Construction Work Package exists because PKG-093 supplies an engineered equipment package (vendor-owned) that the EPC Integrator must physically install, tie into the 03-25 facility, hydrotest, inspect, accept, and turn over. The Construction Work Package is the integrating document that turns vendor scope plus EPC scope into a constructible, sequenced, inspectable site activity (PACKAGE_REGISTER.csv row PKG-093; DELIVERABLE_REGISTER.csv row DEL-093-03).

## Principles

- **Vendor-EPC boundary discipline.** Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package. EPC Integrator owns integration: interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. The Construction Work Package must make this boundary explicit at every interface (PACKAGE_REGISTER.csv row PKG-093).
- **Interface coverage by type.** PKG-093 declares nine applicable interface types; each must be addressed in the workface plan and on the turnover checklist (PACKAGE_REGISTER.csv row PKG-093).
- **Source-grounded acceptance.** Construction acceptance criteria flow from API 650 (tank fabrication/erection) and 26020-Package_Requirements.docx heading 45 (package requirements). Where the source slice is not yet text-accessible, mark `location TBD` rather than invent clause references.
- **Cold-climate site basis.** -40 deg C ambient governs equipment selection, winterization, heat tracing, and concrete pour planning at this site (DBM Site Basis).
- **Spill and drainage discipline.** Produced water is treated/stored at 03-25 then trucked or pipelined out (DBM Produced Water section); spill containment and drainage interfaces are explicit interface types and must be inspectable at turnover.

## Considerations

- The package interfaces with the produced-water transfer pumps, H2O2 treatment package, vent/relief network, and site drainage; sequencing of tie-ins must respect commissioning logic of upstream/downstream systems (DBM Produced Water section).
- Tank design SG is currently 1.25 TBC against a produced-water density of 1.18 SG; foundation design and hydrotest plans must accommodate the design SG when finalized (DBM Raw Gas and Water Design Conditions).
- 03-25 receives produced water from both 03-25 wellstreams and 04-25 sources; storage availability during commissioning may need to coordinate with the 04-25 ramp-up schedule (DBM Condensate and Produced-Water Receipts).
- Sweet produced-water service distinguishes this package from sour produced-water tanks elsewhere in the liquids hub; materials and venting requirements should be confirmed accordingly (DBM Site Basis lists sour and sweet PW tanks).
- Inspection and turnover artifacts feed DEL-093-06 (EPC Vendor Package Review and Acceptance); evidence captured here is consumed downstream (DELIVERABLE_REGISTER.csv).

## Trade-offs

- **Hydrotest water sourcing vs schedule.** Hydrotesting two 3,800 bbl tanks requires significant water volume; sourcing options (site water, trucked) trade against site-water availability and schedule.
- **Insulation/coating sequencing.** Doing final coating before hydrotest risks rework after weld repairs; deferring it risks cold-weather application windows. Standard practice is to hydrotest first; confirm against vendor recommendations.
- **Cold-weather concrete vs schedule.** Foundation pours during winter require additional thermal protection and curing time, trading cost against schedule.
- **CP commissioning timing.** Cathodic protection may be commissioned at handover or during operations; earlier commissioning protects tank bottoms but may complicate facility electrical commissioning sequence.

## Examples

- The Construction Interface and Turnover Checklist for PKG-093 should enumerate one row per declared interface type per tank (nine interface types × two tanks = eighteen interface checkpoints minimum), each with EPC and Vendor sign-off columns (ASSUMPTION on structure; basis: PACKAGE_REGISTER.csv interface types list).
- Workface packages should be sized to ~one tank major activity per package (foundation, ring wall, shell, roof, hydrotest, tie-ins, finish) for crew scheduling (ASSUMPTION; conventional practice).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-093-03-01 | Tank design SG: PACKAGE_REGISTER lists "Sweet Produced Water & Process Water" service without an SG; DBM gives produced-water density 1.18 SG with tank design SG 1.25 TBC. | PACKAGE_REGISTER.csv row PKG-093 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Raw Gas and Water Design Conditions | Datasheet Conditions; Specification R-093-03-03 | DBM (SG 1.25 TBC) as design basis until vendor datasheet confirms | TBD |
| C-093-03-02 | API 650 clause set governing erection, hydrotest, settlement: package name asserts API 650 but the clause-level requirements live in 26020-Package_Requirements.docx package heading 45, which is a binary .docx not text-accessible this run. | PACKAGE_REGISTER.csv row PKG-093 (package name) | 26020-Package_Requirements.docx heading 45 (binary) | Specification R-093-03-02/06/07; Datasheet Construction | Treat API 650 as governing; resolve clause-level checklist when source slice is read | TBD |
