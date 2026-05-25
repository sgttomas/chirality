# Specification: DEL-028-03_construction-work-package — Construction Work Package

## Scope

This specification governs the EPC Integrator Construction Work Package (CWP) for **Transformer TXP-8801-1 — STEP DOWN DISTRIBUTION TRANSFORMER (7.5 MVA, 13.8 kV / 4160 / 2400 V)** under PKG-028.

**Covers:**
- Constructibility requirements for receipt, rigging, setting, alignment, grounding, termination, and pre-energization checkout of TXP-8801-1.
- Construction tie-in to facility electrical, grounding, lighting, I&C/control cabling, communications/network, structural/foundation, and maintenance-access systems as declared in PACKAGE_REGISTER and INTERFACE_REGISTER for PKG-028.
- Construction-side inspection and turnover evidence.

**Excludes:**
- Vendor package engineering, design, fabrication, and factory testing — owned by Package Vendor under DEL-028-04. (PACKAGE_REGISTER.csv, Workbook Packages row 30)
- Vendor document register and turnover documentation — owned under DEL-028-05.
- EPC review/acceptance of the vendor package — covered under DEL-028-06.
- Process-side commissioning beyond pre-energization construction checkout.

Source basis: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv (DEL-028-03); PACKAGE_REGISTER.csv (PKG-028); DBM-Deepcut §§2745, 2919, 2985.

## Requirements

| ID | Requirement | Basis / Source | Notes |
|---|---|---|---|
| REQ-028-03-001 | The CWP shall document the physical installation, build sequence, inspection, turnover, and tie-in of PKG-028 into the larger facility systems. | `_CONTEXT.md` (Scope); DELIVERABLE_REGISTER.csv | Mandatory deliverable scope. |
| REQ-028-03-002 | The CWP shall include an installation and tie-in workface plan covering rigging, setting on the precast concrete bearing foundation, primary 13.8 kV termination, secondary 4160 V and 2400 V terminations, grounding/bonding to the facility ground grid, and ancillary controls / communications / lighting tie-ins. | ARTIFACT_REGISTER.csv (ART-D64770700D); INTERFACE_REGISTER.csv PKG-028 rows; DBM-Deepcut §2745 | Foundation type per DBM. |
| REQ-028-03-003 | The CWP shall include a construction interface and turnover checklist addressing each declared interface type for PKG-028: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | ARTIFACT_REGISTER.csv (ART-790F01D335); INTERFACE_REGISTER.csv PKG-028 rows | All seven declared interface types. |
| REQ-028-03-004 | Grounding of the transformer enclosure and neutral shall be installed in accordance with the facility grounding scheme, with NGR / HRG configuration confirmed by detailed engineering for the specific 4160 V and 2400 V secondaries. | DBM-Deepcut §2985 (analogous transformer grounding scheme — 6.9 kV via 100 A NGR, 600 V via 5 A HRG) | ASSUMPTION pending detailed engineering; rating for 4160 / 2400 V is `TBD`. |
| REQ-028-03-005 | All distribution transformers shall have a separate copper ground conductor connected directly to ground, sized per CEC, in addition to grounding conductors run with power wiring. | DBM-Deepcut §2991 | Direct DBM requirement. |
| REQ-028-03-006 | Construction activities shall hold for vendor Installation, Operation, and Maintenance (IOM) instructions, factory test report acceptance, and EPC Inspection & Test Plan (ITP) prior to energization. | ASSUMPTION (standard EPC practice; specific IOM/ITP not in PREPARATION source set) | `TBD` until vendor documentation is accepted under DEL-028-05/06. |
| REQ-028-03-007 | The CWP shall identify constructibility hold points for foundation acceptance, ground grid continuity, transformer setting/alignment, primary and secondary terminations, insulation resistance and turns-ratio pre-energization tests, and SAT-ready turnover. | ASSUMPTION based on standard transformer commissioning practice | Specific hold-point list `TBD`. |
| REQ-028-03-008 | Construction interface management shall coordinate with adjacent packages providing 13.8 kV feeder, 4160 V and 2400 V downstream feeders, ground grid, area lighting, control and communications cabling, and structural supports. | INTERFACE_REGISTER.csv (PKG-028 rows) | Adjacent package IDs `TBD` (cross-package mapping is downstream coordination work, out of this deliverable's scope). |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding conductor sizing for distribution transformers | DBM-Deepcut §2991 (cited); specific clause `location TBD` |
| Project Design Basis Memoranda (DBM) — Deepcut | Plant-level electrical distribution architecture and transformer grounding | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §§2745, 2919, 2985, 2991 |
| Vendor IOM for TXP-8801-1 | Manufacturer installation, torque, and pre-energization requirements | `TBD` (not in PREPARATION source set) |
| ANSI / IEEE C57 series (liquid-filled power transformers) | Industry-standard installation and acceptance testing | ASSUMPTION: likely applicable; `location TBD` |
| CSA C88 / CSA C802 (Canadian distribution transformer standards) | Industry-standard installation and acceptance | ASSUMPTION: likely applicable; `location TBD` |

## Verification

| Requirement | Verification Approach | Records |
|---|---|---|
| REQ-028-03-001 | CWP document review; checklist confirms scope coverage | CWP approval record |
| REQ-028-03-002 | Workface plan walk-down; rigging plan review; pre-installation foundation acceptance | Foundation acceptance, rigging plan, workface plan record |
| REQ-028-03-003 | Construction turnover checklist completion; interface sign-offs by counterpart package owners | Interface turnover checklist, sign-off log |
| REQ-028-03-004 / 005 | Ground continuity test; verification against grounding design drawings | Ground continuity test report |
| REQ-028-03-006 | Construction hold-point sign-off contingent on IOM and ITP acceptance | Hold-point register; ITP record |
| REQ-028-03-007 | Pre-energization tests (insulation resistance, turns ratio, winding resistance, oil DGA if liquid-filled) per IOM and ITP | Pre-energization test reports |
| REQ-028-03-008 | Cross-package interface walk-down with adjacent packages | Interface walk-down record |

## Documentation

Anticipated artifacts (per `_CONTEXT.md` and ARTIFACT_REGISTER.csv):

- Construction work package (ART-C0CF6D35AA)
- Installation and tie-in workface plan (ART-D64770700D)
- Construction interface and turnover checklist (ART-790F01D335)

Supporting evidence to be captured during execution:
- Foundation acceptance record
- Rigging and setting plan
- Ground continuity test report
- Pre-energization test reports (insulation resistance, turns ratio, etc.)
- Interface turnover sign-off log
- Hold-point register
- Punch list and closeout record
