# Specification — Construction Work Package (DEL-095-03)

## Scope

This Construction Work Package (CWP) defines how the **PKG-095 Tanks, Slop (API 650)** scope is physically installed at the facility, inspected, turned over, and tied into the larger facility process, relief, drainage, electrical, and instrumentation systems. The CWP covers field execution of one API 650 modified atmospheric slop storage tank (likely tagged TK-9130-2), its appurtenances, its connections to relevant drain/recycle/truck-out systems, and standard tank instrumentation, from foundation acceptance through hydrotest, mechanical completion, inspection, and Gate 5 turnover.

### Out of scope (executed by other deliverables/packages)

- Vendor package engineering, design, fabrication/supply, and the physical equipment package as a vendor production unit — covered by `DEL-095-04_vendor-engineered-equipment-package`.
- Vendor document register, submittals, and source-required vendor documentation — covered by `DEL-095-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance — covered by `DEL-095-06_epc-vendor-package-review-and-acceptance`.
- Package scope of work and package datasheet narratives — covered by `DEL-095-01` and `DEL-095-02`.
- Civil site grading, ringwall/pad foundation design, and earthworks (separate civil packages).
- Process/flow determination of slop disposition path and slop source list (process engineering scope; flagged open in SOW-0216).
- TBD; no package-specific exclusions stated in source materials (per PACKAGE_REGISTER.csv PKG-095).

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| R-095-03-01 | The CWP shall install one API 650 modified atmospheric slop storage tank (likely TK-9130-2) per the Package Vendor's certified design package. | SCOPE_LEDGER.csv SOW-0215; SOW-0214 |
| R-095-03-02 | The CWP shall install the tank in slop service — off-spec condensate or contaminated hydrocarbon liquids requiring segregation from on-spec condensate product — and shall not commission the tank into product (on-spec condensate) service. | SCOPE_LEDGER.csv SOW-0214, SOW-0216 |
| R-095-03-03 | The CWP shall complete tie-ins for slop inlet lines from the slop sources identified by process engineering (off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, treating-unit drains, and other contaminated hydrocarbon liquids), per certified P&IDs. Final source list TBD per process. | SCOPE_LEDGER.csv SOW-0216 |
| R-095-03-04 | The CWP shall complete tie-ins for tank recycle/disposition and truck-out connections to support the slop disposition path defined by process engineering. Disposition path TBD per process. | SCOPE_LEDGER.csv SOW-0215, SOW-0216 |
| R-095-03-05 | The CWP shall complete tie-ins for the nine Workbook-declared interfaces applicable to PKG-095: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | INTERFACE_REGISTER.csv PKG-095 rows; PACKAGE_REGISTER.csv PKG-095 Applicable interface types |
| R-095-03-06 | Tank construction (welding, bottom, shell, roof, hydrotest, settlement criteria, NDE) shall conform to API 650 as modified by the Package Vendor's certified design package. | SCOPE_LEDGER.csv SOW-0215 (API 650 modified); ASSUMPTION (standard API 650 construction code application) |
| R-095-03-07 | The CWP shall hydrotest the tank per API 650 and the vendor's test plan, performing a settlement survey before and after hydrotest, and shall not commission the tank into service until hydrotest and settlement acceptance criteria are met. | ASSUMPTION (standard API 650 commissioning; not explicit in accessible source slices) |
| R-095-03-08 | Drain and secondary containment tie-ins shall route to the facility drain/containment system such that slop liquid releases are contained and routed to a slop-compatible drain destination. | INTERFACE_REGISTER.csv (Drain / Containment); SCOPE_LEDGER.csv SOW-0214 (segregation from on-spec product) |
| R-095-03-09 | Grounding, bonding, and cathodic protection shall be installed and commissioned per vendor specification and applicable electrical/corrosion standards before energization of associated electrical and instrumentation circuits. | INTERFACE_REGISTER.csv (Grounding / Bonding; Cathodic Protection) |
| R-095-03-10 | Standard tank instrumentation (level, temperature, pressure as applicable, high-level/overfill protection per process design) shall be installed, loop-checked, and integrated into the host control system. Specific instrument set and trip values TBD per process design. | SCOPE_LEDGER.csv SOW-0215 (standard tank instrumentation); ASSUMPTION (overfill protection per standard tank-farm practice) |
| R-095-03-11 | Vent / relief routing (atmospheric vent and/or pressure-vacuum relief to vent or flare per process design) shall be installed per certified P&IDs and the Relief / Flare / Vent interface. Final routing TBD per process. | INTERFACE_REGISTER.csv (Relief / Flare / Vent) |
| R-095-03-12 | The CWP shall produce documented evidence of construction completion sufficient to support Gate 5 turnover, including foundation acceptance, weld/NDE records, hydrotest record, settlement survey, instrument loop checks, cathodic protection commissioning, and punch list. | _CONTEXT.md anticipated artifacts; OBJ-010 (carried in _CONTEXT Supports Objectives) |
| R-095-03-13 | The CWP shall coordinate the workface plan across civil/structural (foundation/ringwall acceptance), electrical (grounding, area lighting, CP, motor power if any), instrumentation (loop checks), piping (process, relief, drain tie-ins), and grading/drainage (spill containment) interfaces. | INTERFACE_REGISTER.csv PKG-095; PACKAGE_REGISTER.csv PKG-095 |
| R-095-03-14 | The construction interface and turnover checklist shall document responsibility handoff between Package Vendor (engineering/design/equipment) and EPC Integrator (site assembly, tie-ins, turnover). | PACKAGE_REGISTER.csv PKG-095 Responsibility narrative; _CONTEXT.md anticipated artifacts |
| R-095-03-15 | Lift plans, rigging studies, and crane positions for any large prefabricated tank sub-assemblies (e.g., shell courses, roof) shall be developed by the EPC Integrator's construction contractor. | ASSUMPTION (standard EPC modular/erection practice; not explicit in accessible source slices) |

## Standards

| Standard / Regulation | Applicability | Location |
|---|---|---|
| API 650 (modified) | Atmospheric tank design, fabrication, erection, inspection, hydrotest, settlement, and acceptance | Cited in SCOPE_LEDGER.csv SOW-0215; standard text location TBD (not in accessible source slices) |
| 26020-Package_Requirements.docx, package heading 47 | Vendor/EPC document expectations and process mechanical requirements for the Slop Tank package | Source binary; text slice location TBD |
| ASME B31.3 | Process piping code for tie-ins | ASSUMPTION (not explicitly stated in accessible source slice; location TBD) |
| Applicable welding/NDE codes (e.g., ASME Sec. IX for welder qualification; API 650 weld/NDE provisions) | Standard mechanical construction codes | ASSUMPTION (not explicitly stated in accessible source slice; location TBD) |
| Site-applicable jurisdiction / regulatory framework (e.g., for tank-farm spacing, secondary containment, environmental) | Tank-farm regulatory and environmental constraints | TBD — not stated in accessible source slices |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-095-03-01 | Vendor data book review; field verification of installed tank against certified design package; tag verification (TK-9130-2 once confirmed). |
| R-095-03-02 | P&ID and tag verification at commissioning; service-segregation walkdown vs. on-spec product tankage. |
| R-095-03-03, R-095-03-04 | Walkdown vs. certified P&IDs; pressure test of completed tie-in spools; punch list closure. |
| R-095-03-05 | Per-interface sign-off rows on the construction interface and turnover checklist. |
| R-095-03-06 | Vendor QA records (welding, NDE, materials) reviewed and accepted by EPC Integrator. |
| R-095-03-07 | Hydrotest record and signed pre/post hydrotest settlement survey. |
| R-095-03-08 | Drain/containment walkdown; functional flow check on designated containment drain. |
| R-095-03-09 | Grounding continuity test record; cathodic protection commissioning record. |
| R-095-03-10 | Instrument loop check sheets; overfill protection functional test record. |
| R-095-03-11 | Relief/vent routing walkdown vs. P&IDs. |
| R-095-03-12 | Turnover document package completeness review by EPC Integrator (Gate 5 readiness). |
| R-095-03-13 | Workface plan execution review; interface checklist sign-off. |
| R-095-03-14 | Signed vendor/EPC responsibility split on interface checklist. |
| R-095-03-15 | Lift plan submitted, reviewed, and executed under supervision; lift records retained. |

## Documentation

Anticipated artifacts (per `_CONTEXT.md`):

- Construction work package narrative (this document and accompanying field execution plan).
- Installation and tie-in workface plan (operational detail; see `Procedure.md`).
- Construction interface and turnover checklist (TBD form; one row per interface item, sign-off columns; covers the nine PKG-095 interface types).

Additional turnover evidence expected (ASSUMPTION — itemized list TBD):

- Vendor data book (API 650 slop tank).
- Foundation acceptance / anchor bolt / ringwall survey record.
- Weld map and NDE reports (bottom vacuum-box, shell, roof).
- Hydrotest record.
- Settlement survey records (pre/post hydrotest).
- Grounding/bonding continuity test record.
- Cathodic protection commissioning record.
- Instrument loop check records; overfill protection functional test.
- Area lighting commissioning record.
- As-built redlines and punch-list closeout.
