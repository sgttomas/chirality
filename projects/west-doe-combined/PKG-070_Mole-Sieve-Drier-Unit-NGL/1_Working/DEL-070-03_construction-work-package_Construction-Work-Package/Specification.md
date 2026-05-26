# Specification — DEL-070-03 Construction Work Package (Mole Sieve Drier Unit, NGL)

## Scope

This specification governs the EPC Integrator Construction Work Package (CWP) for PKG-070 Mole Sieve Drier Unit (NGL), describing how the vendor-supplied package and supporting EPC scope are physically installed, built, inspected, turned over, and tied into facility systems.

**In scope (this deliverable):**
- The CWP narrative and tie-in workface plan covering physical installation of the package within facility battery limits.
- Construction-interface controls for the interface categories marked Applicability=Yes in the source Physical Interface Summary.
- Construction inspection and turnover checklist for the EPC scope of work around the vendor package.

**Out of scope (this deliverable):**
- Vendor package engineering, design, fabrication, FAT (covered by DEL-070-04).
- Vendor document turnover register (covered by DEL-070-05).
- EPC vendor package review and acceptance (covered by DEL-070-06).
- By-others items called out in the source Scope Notes / Open Items (upstream mercaptan treating, downstream NGL storage / loading / LACT / export, sales-gas and stabilizer-overheads compression, produced-water tank and facility drain header beyond package nozzles, flare header).

## Requirements

Source-grounded (S) requirements are drawn from `_Sources/26020-Package_Requirements.docx` heading `26020-01-PT-22-003`. Inferred (A=ASSUMPTION) requirements are conventional EPC CWP content not directly stated in the available source slice; they are retained as `TBD` for human ruling rather than as binding requirements.

| ReqID | Requirement | Type | Source / Note |
|---|---|---|---|
| R-CWP-01 | The CWP shall identify and physically install all major in-scope equipment listed in the source Major Included Equipment section (three molecular sieve vessels with 3A sieve and silica-gel layer; inlet liquid/liquid coalescer; regen-gas heater, aerial cooler with winterization features, three-phase regen scrubber; outlet particulate filter; moisture analyzer with vaporizing regulator; heated enclosure as required). | S | source Major Included Equipment |
| R-CWP-02 | The CWP shall plan and execute battery-limit tie-ins for interface categories with Applicability=Yes in the source Physical Interface Summary: Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Area/Exterior Lighting; EHT; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety; Maintenance Access; Structural/Foundations/Supports. | S | source Physical Interface Summary |
| R-CWP-03 | The CWP shall not introduce scope for interface categories with Applicability=No in the source: Utility Piping; Cathodic Protection; Communications/Network; Building HVAC/Services; Grading/Site Drainage/Spill Containment; Product Loading; Pipeline/Pigging. | S | source Physical Interface Summary |
| R-CWP-04 | The CWP shall be consistent with the operating and design conditions in the source Scope Notes (adsorption inlet 1,978 kPag design, outlet 1,943 kPag design, inlet 29.7/46.3/51.8 °C low/design/high, start-of-life bed dP < 4 psid / 27.6 kPad, end-of-life bed dP < 10 psid including vessel nozzles, 24-hour adsorption cycle). | S | source Scope Notes / Operating + Design conditions |
| R-CWP-05 | The CWP shall use vendor-issued installation, lifting, and test references as the basis for site work: MEC-017 (Equipment Installation/Setting Drawings), MEC-018 (Lifting/Handling Study), PIP-024 (Hydrotest/Pressure Test Packages), PIP-025 (Flushing/Cleaning/Drying Procedure). | S | source Vendor Engineering Deliverables |
| R-CWP-06 | The CWP shall include a construction interface and turnover checklist that covers each in-scope interface category in R-CWP-02 and references the applicable vendor deliverable (e.g., ELE-027/ELE-028, INS-006/INS-008/INS-009, TSF-004, STR-006/STR-013). | S | source Vendor Engineering Deliverables |
| R-CWP-07 | The CWP shall exclude by-others scope per source Scope Notes / Open Items and shall not commit EPC construction effort against those items. | S | source Scope Notes / Open Items |
| R-CWP-08 | Construction sequencing and workface plan structure (work packages, IWP boundaries, schedule). | A | TBD — not in available source slice; ASSUMPTION pending EPC construction-management input |
| R-CWP-09 | Pre-commissioning and mechanical completion criteria specific to the dryer package. | A | TBD — not in available source slice; ASSUMPTION pending vendor IOM (MEC-025) and pre-commissioning standards |
| R-CWP-10 | Construction QA/QC inspection categories beyond vendor ITP (QLT-003) and Inspection Release Certificate (QLT-020). | A | TBD — not in available source slice |

## Standards

| Standard | Applicability | Source / Location |
|---|---|---|
| API-661 (modified) | Referenced for air-cooled exchangers elsewhere in the source workbook; applicability to this package's aerial cooler is plausible but not stated for heading 22-003 | location TBD; ASSUMPTION |
| Pressure equipment registration | REG-022 listed as a vendor deliverable for this package | source Vendor Engineering Deliverables (Static pressure equipment) |
| Jurisdictional pressure-vessel construction / hydrotest code | Required for vessel installation and hydrotest | TBD — not stated in available source slice |
| Site-specific electrical code (area classification) | Implied by heated enclosure and electrical tie-ins | TBD — not stated in available source slice |

## Verification

| ReqID | Verification Approach | Evidence |
|---|---|---|
| R-CWP-01 | Equipment receipt, setting, and installation walk-down per MEC-017; lifting per MEC-018 | Installation records; setting reports; lifting study sign-off |
| R-CWP-02 | Tie-in scope sheets per PIP-004; tie-in walk-down per interface category | Tie-in list; tie-in inspection records |
| R-CWP-03 | Exclusion noted in CWP scope; no scope items raised against Applicability=No categories | CWP scope register; change-control log |
| R-CWP-04 | Confirmation that installed configuration matches design-condition envelope on vendor MEC-016 / PRO-008 | As-installed marked drawings; nameplate checks |
| R-CWP-05 | Vendor-deliverable transmittal record; field use of latest revision | Transmittal log; field document control records |
| R-CWP-06 | Construction turnover checklist signed per interface category | Turnover checklists; punch-list closure records |
| R-CWP-07 | CWP scope cross-check against source Scope Notes / Open Items by-others list | Scope review record |
| R-CWP-08 | TBD | TBD |
| R-CWP-09 | TBD | TBD |
| R-CWP-10 | TBD | TBD |

## Documentation

Anticipated artifacts produced by this deliverable (from `_CONTEXT.md` Anticipated Artifacts and source vendor-deliverable references):

- Construction Work Package document (CWP narrative).
- Installation and tie-in workface plan (anchored to PIP-004 Tie-In List and MEC-017 Installation/Setting Drawings).
- Construction interface and turnover checklist (one row per Applicability=Yes interface category).
- Records consumed (vendor-issued, not produced here): MEC-017, MEC-018, PIP-024, PIP-025, MEC-025 IOM, QLT-003 ITP, QLT-020 Inspection Release Certificate, QLT-021 Manufacturing Record Book, ELE-029/030 FAT/SAT and energization records, INS-029 Instrument As-Built Drawings, PIP-028 Piping As-Built Drawings, PRO-028 Process As-Built PFD/P&ID Package.
