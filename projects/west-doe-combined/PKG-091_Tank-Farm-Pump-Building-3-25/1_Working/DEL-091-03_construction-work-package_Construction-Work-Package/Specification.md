# Specification — DEL-091-03 Construction Work Package

## Scope

### In scope

This Construction Work Package (CWP) is the EPC Integrator's mandatory Gate 5 anchor deliverable for **PKG-091 Tank Farm Pump Building 3-25**. It normatively governs how the package will be physically installed, built, inspected, tied in to adjacent facility systems, and turned over for commissioning (PROJECT_DECOMP §Gate 5; DEC-013).

The CWP covers, at minimum, the installation and tie-in of the equipment enumerated in SOW-0187 — the building drain pump, two water transfer pumps, two sour condensate booster pumps, two condensate sweetening feed pumps, one condensate skim pump, one sour condensate recycle pump, two condensate booster pumps, and one condensate product recycle pump — together with their piping, electrical, and instrumentation interfaces to the broader 03-25 facility (SOW-0186; SOW-0187).

### Out of scope (excluded — by Others, per SOW-0188)

- DCS integration.
- Foundations.
- Electrical supply up to the 600 V MCC.

### Boundary clarifications

- The CWP terminates at the package-to-facility tie-in flanges and electrical/instrumentation termination points; the package itself is engineered/supplied by the Package Vendor under DEL-091-04 (`DELIVERABLE_REGISTER.csv` row 471).
- Vendor documentation flows are governed by DEL-091-05; package acceptance is governed by DEL-091-06.

## Requirements

### REQ-091-03-001 — Installation of supplied pump equipment

The EPC Integrator shall install all pumps listed in SOW-0187 in their tagged locations within the Tank Farm Pump Building 3-25 per the vendor's installation, alignment, and grouting requirements. Source: SOW-0187.

### REQ-091-03-002 — Power supply integration

All motor-driven pumps shall be connected to the 600 V MCC (electrical supply to MCC by Others) via 575 V / 3-ph / 60 Hz feeders, with starting method **DOL or VFD** as specified per pump, and **local control (H-O-A or On-Off switch)** installed at each pump. Source: SOW-0188.

### REQ-091-03-003 — Cold start capability

Motors shall be installed and commissioned consistent with sizing for **inlet stabilizer composition density at -40 °C start-up**. Source: SOW-0188. (Sizing is vendor scope; installation shall not invalidate that sizing — `ASSUMPTION` regarding heat tracing/insulation scope split; specific provisions `TBD`.)

### REQ-091-03-004 — Building Drain Pump installation

The Graco 1050A pneumatic diaphragm Building Drain Pump (P-9295-2; 11.34 m3/h @ 689 kPag, pneumatically driven) shall be installed with its pneumatic supply tie-in and drain piping connection. Source: SOW-0187; SOW-0188.

### REQ-091-03-005 — Water transfer pump suction filtration tie-in

The two Water Transfer Pumps (P-9290-2 / P-9293-2) shall be installed in parallel pulling produced water from the produced-water tanks through a bag filter, with discharge piped to the produced-water pipeline. Source: SOW-0186.

### REQ-091-03-006 — Sour condensate transfer path tie-in

The two Sour Condensate Booster Pumps (P-9215-2 / P-9216-2) shall be tied in to move sour condensate from the sour condensate storage tanks to the Condensate Sweetening Feed Pumps (P-9210-2 / P-9220-2). Source: SOW-0186.

### REQ-091-03-007 — API-682 mechanical seal plans

Vertical inline centrifugal pumps in sour/sweet condensate service (P-9210/9211/9215/9216/9220/9221-2) shall be installed in accordance with **API-682 Plan 14/52** mechanical seal arrangements as supplied by the vendor. Source: SOW-0187. Detailed installation provisions for seal flush/buffer fluid routing: `location TBD` (refer to vendor data and 26020-Package_Requirements.docx package heading 44).

### REQ-091-03-008 — Sealless diaphragm pump installation

Diaphragm positive-displacement, sealless Hydracell pumps (P-9200-2, P-9230-2, P-9240-2) shall be installed including the inlet basket strainer at P-9240-2 (strainer size `TBC`). Source: SOW-0187.

### REQ-091-03-009 — Construction interfaces and turnover

The CWP shall produce, maintain, and close out the **construction interface and turnover checklist** identified as an anticipated artifact (`_CONTEXT.md`), recording mechanical completion, electrical termination/megger results, instrumentation loop checks, pre-commissioning, and handover to commissioning. Detailed checklist items: `TBD` (not source-resolved at this pass).

### REQ-091-03-010 — Workface planning

An **installation and tie-in workface plan** shall be produced as an anticipated artifact (`_CONTEXT.md`) covering the construction sequence, work packs by discipline, and tie-in coordination with adjacent packages. Specific workface-plan structure: `TBD`.

### REQ-091-03-011 — Boundary respect for "By Others" items

The EPC Integrator shall not include DCS integration, foundation engineering, or upstream electrical supply to the MCC within its construction execution scope; these remain "By Others" per SOW-0188.

## Standards

| Standard / governing reference | Applicability | Source / location |
|---|---|---|
| API-682 (Plans 14/52) | Mechanical seal arrangements for vertical inline centrifugal pumps in condensate service | SOW-0187 |
| 26020-Package_Requirements.docx package heading 44 | Package-level requirements for Tank Farm Pump Building 3-25 | `_REFERENCES.md`; `DELIVERABLE_REGISTER.csv` row 470; `location TBD` (binary not directly slice-read in this run) |
| Workbook Packages row 84 | Workbook package definition for PKG-091 | `_REFERENCES.md`; `SCOPE_LEDGER.csv` row 186 |
| Local jurisdictional construction codes (CSA, ABSA/BCSA pressure piping, CEC) | Applicability to BC site construction | `ASSUMPTION` from BC site (DBM §Site); explicit code list `TBD` |

## Verification

| Requirement | Verification approach | Records |
|---|---|---|
| REQ-091-03-001 | Mechanical completion inspection; alignment records | Installation records; alignment reports |
| REQ-091-03-002 | Electrical termination and megger test; HOA/On-Off function check; starter type verification | Electrical termination records; starter test records |
| REQ-091-03-003 | Cold-condition readiness review (heat tracing/insulation walk-down — `ASSUMPTION`) | Walk-down checklist (`TBD` form) |
| REQ-091-03-004 | Functional test of pneumatic drain pump on air supply | Functional test record |
| REQ-091-03-005 | Hydrotest / line check of suction-bag-filter-discharge path | Line check / hydrotest records |
| REQ-091-03-006 | Hydrotest / line check of sour condensate booster to sweetening feed path | Line check / hydrotest records |
| REQ-091-03-007 | API-682 seal plan installation verification per vendor IOM | Seal-plan installation record |
| REQ-091-03-008 | Strainer install verification; pump dry-run / wet-run per vendor IOM | Pump pre-commissioning record |
| REQ-091-03-009 | Closed construction interface and turnover checklist | Turnover checklist; mechanical completion certificate |
| REQ-091-03-010 | Workface plan issued, used, and signed off | Workface plan (issued revision); sign-off |
| REQ-091-03-011 | Scope-of-work boundary check at package acceptance | DEL-091-06 acceptance record |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):

- Construction work package (this document set)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Additional construction records consistent with the verification table above (`ASSUMPTION` — record list not explicitly enumerated in source; subject to EPC Integrator standard practice and the 26020 package requirements document).
