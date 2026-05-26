# Specification — DEL-065-01 Scope of Work — Tanks, Caustic (API 650) 4-25 (PKG-065)

## Scope

This Scope of Work establishes the EPC Integrator-authored package scope for PKG-065 "Tanks, Caustic (API 650) 4-25" (Workbook Packages row 87; Mechanical; WBS 01; Vendor Tracking No. 26020-01-PT-19-003). It defines:

- the tagged equipment inside the package boundary;
- the process function of each tank;
- the responsibility split between Package Vendor and EPC Integrator;
- the by-others items explicitly excluded from the Package Vendor's supply;
- the package's role in the whole-facility integration narrative for the 4-25 Deep Cut Gas Plant non-regenerative NGL mercaptan caustic treating system.

In scope:
- (1) Spent Caustic Storage Tank `TK-6780-1` (per SOW-0199).
- (1) Fresh Caustic Storage Tank (tag `TBD`; per SOW-0198 and DBM-Deepcut).
- Package vendor engineering, design, vendor documentation, and the physical equipment package for the two tanks (per PACKAGE_REGISTER row PKG-065, Responsibility field; SOW-0197).
- EPC Integrator integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (per PACKAGE_REGISTER row PKG-065).

Out of scope (explicit by-others — Package Vendor does NOT supply):
- Foundations.
- Mounting tanks at site.
- Electrical and instrumentation.
- Platforms.
- Staircase.
- "etc." (SOW-0200 wording — additional by-others items `TBD` against the source document section).
Source: SOW-0200 (workbook scope notes and open items).

Out of scope (clarifying boundary, ASSUMPTION):
- On-site caustic regeneration (the active basis is non-regenerative per DBM-Deepcut).
- The pressurized caustic drain drum `V-6940-1` is NOT asserted as part of this package by available source slices; its inclusion is `TBD`.

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-065-01-01 | The package shall deliver two atmospheric storage tanks: one (1) spent caustic and one (1) fresh caustic. | SOW-0198 |
| REQ-065-01-02 | The Spent Caustic Storage Tank shall be tagged `TK-6780-1`. | SOW-0199 |
| REQ-065-01-03 | Tanks shall be designed and fabricated to modified API 650. | SOW-0199 |
| REQ-065-01-04 | Tank nominal capacity shall be 400 bbl each. | SOW-0199; SOW-0200 |
| REQ-065-01-05 | Tank design pressure shall be 32 oz with 1.0 oz vacuum (atmospheric service). | SOW-0199; SOW-0200 |
| REQ-065-01-06 | Tank design temperature shall accommodate minimum ambient temperature at the 4-25 site. | SOW-0200 |
| REQ-065-01-07 | The Spent Caustic Tank shall be provided with a heater maintaining a minimum of 32.2 degC (90 degF); the vendor shall design the heater. | SOW-0199 |
| REQ-065-01-08 | The Fresh Caustic Tank shall be heated and insulated. | DBM-Deepcut/4-25_Deepcut_DBM.md (caustic tanks subsection) |
| REQ-065-01-09 | Tank materials shall be polymer or other caustic-compatible material; aluminum shall not be used in the caustic building; insulation cladding/straps in caustic exposure areas shall be stainless steel. | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-065-01-10 | The Spent Caustic Tank vapours shall be routed to the incinerator header with flame-arrestor protection and low-pressure fuel-gas blanket. | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-065-01-11 | The Fresh Caustic Tank shall be fuel-gas blanketed and shall NOT be connected to the VRU header. | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-065-01-12 | The Fresh Caustic Tank shall accommodate truck-in delivery; the Spent Caustic Tank shall accommodate truck-out disposal. | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-065-01-13 | Fresh caustic design concentration is 50 wt% NaOH; fresh caustic tank design specific gravity is 1.75 (TBC per DBM). | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-065-01-14 | Tanks shall be installed indoors (caustic freezing/crystallization risk). | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-065-01-15 | The Spent Caustic Tank shall receive flow from the pressurized caustic drain drum on level control. | SOW-0199; DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-065-01-16 | Package flow-rate basis (operating throughput) shall be confirmed during vendor engineering. | SOW-0200 (flow rate TBD) |
| REQ-065-01-17 | Package boundaries shall exclude foundations, site mounting, electrical/instrumentation, platforms, and staircase (by others). | SOW-0200 |

## Standards

| Standard | Applicability | Locally Accessible? |
|---|---|---|
| API 650 (modified) | Tank design and fabrication | Standard text NOT in `_Sources` (location TBD); applicability is asserted in SOW-0199 |

Additional standards (RP / PIP / vendor specs) referenced in `26020-Package_Requirements.docx` package heading 20 are `TBD` — that document is `.docx` and not directly readable in this run.

## Verification

| ReqID(s) | Verification Approach |
|---|---|
| REQ-065-01-01, 02, 04 | Vendor datasheet review against this Scope of Work; tag list reconciliation against `TK-6780-1` and fresh-tank tag (to be issued). |
| REQ-065-01-03 | Vendor design calculation package and code-stamped fabrication records reviewed against modified API 650 basis. |
| REQ-065-01-05, 06 | Design conditions verification at FAT and vendor design review. |
| REQ-065-01-07, 08 | Heater design package review; insulation/heat-trace witness test as applicable. |
| REQ-065-01-09, 14 | Material certificates (MTRs) and building installation inspection (no aluminum, SS cladding, indoor location). |
| REQ-065-01-10, 11 | P&ID review confirming spent-tank-to-incinerator routing, flame arrestor, and fresh-tank fuel-gas blanket isolated from VRU. |
| REQ-065-01-12 | Truck-in/truck-out interface walkdown. |
| REQ-065-01-13 | Vendor datasheet check of design SG and confirmation of 50 wt% NaOH fresh basis. |
| REQ-065-01-15 | P&ID and instrument loop verification with PKG containing the pressurized caustic drain drum (cross-package interface). |
| REQ-065-01-16 | EPC-approved flow basis transmittal to vendor prior to detailed design. |
| REQ-065-01-17 | Construction work package (DEL-065-03) confirms by-others scope is executed by EPC Integrator construction. |

## Documentation

Anticipated artifacts produced by this Scope of Work deliverable:
- Package scope of work narrative.
- Tagged equipment and package identity list.
- Package function and integration narrative.
- Responsibility assignment record (Package Vendor vs EPC Integrator).
Source: `_CONTEXT.md` Anticipated Artifacts and DELIVERABLE_REGISTER row DEL-065-01_scope-of-work.

Downstream documentation requirements (vendor document register, datasheets, turnover) are governed by sibling deliverables DEL-065-02 (Package Datasheet) and DEL-065-05 (Vendor Document Turnover Package); not duplicated here.
