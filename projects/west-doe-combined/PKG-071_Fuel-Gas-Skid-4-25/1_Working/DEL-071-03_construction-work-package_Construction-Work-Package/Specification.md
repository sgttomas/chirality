# Specification — DEL-071-03 Construction Work Package (Fuel Gas Skid 4-25)

## Scope

### Covered

The Construction Work Package (CWP) defines how the Fuel Gas Skid (`26020-01-PT-23-001`, 4-25 West Doe Deepcut) is physically received, set, installed, connected, inspected, tested, and turned over to facility operations. The CWP covers:

- Receipt and set of the vendor-supplied skid containing the low-pressure fuel gas heater and scrubber (`_Sources/26020-Package_Requirements.docx`, Basic Scope and Major Included Equipment).
- Foundation construction and skid anchoring (`_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables — Structural section: STR-001, STR-002, STR-005, STR-006, STR-013, STR-014).
- Field tie-ins called out as applicable in the Physical Interface Summary: process piping; utility piping; relief/flare/vent; drain/containment; structural supports; grounding/bonding; I&C control cabling; fire & gas; area/exterior lighting; maintenance access (`_Sources/26020-Package_Requirements.docx`, Physical Interface Summary).
- Construction inspection and turnover documentation (`_CONTEXT.md` Anticipated Artifacts).
- All "By others" items called out by the source as outside the vendor scope but required to make the package operational: shipping to site, installation, tie-in piping, electrical tie-in (`_Sources/26020-Package_Requirements.docx`, Scope Notes / Open Items).

### Excluded

- Vendor-engineered, vendor-fabricated, and vendor-supplied portions of the skid itself (covered by DEL-071-04 Vendor Engineered Equipment Package).
- Vendor document turnover (covered by DEL-071-05).
- EPC vendor review and acceptance (covered by DEL-071-06).
- Package datasheet content (covered by DEL-071-02).
- Package scope of work (covered by DEL-071-01).
- Interfaces marked `No` in the Physical Interface Summary for this package: EHT; Cathodic Protection; Communications/Network; Building HVAC/Services; Grading/Site Drainage/Spill Containment; Product Loading; Pipeline/Pigging. Note source-internal conflict on Electrical Power (see Conflict Table in `Guidance.md`).

## Requirements

| Req ID | Requirement | Type | Source |
|---|---|---|---|
| CWP-FGS-R-01 | The CWP shall plan and execute receipt, off-loading, and setting of one (1) skid for the low-pressure fuel gas package on prepared foundations. | Construction | `_Sources/26020-Package_Requirements.docx`, Basic Scope and Scope Notes / Open Items ("By others: installation") |
| CWP-FGS-R-02 | Foundations shall be constructed per vendor structural deliverables (STR-005 Foundation Design Calculations, STR-006 Foundation Drawings, STR-013 Anchor Bolt / Embedment Drawings). | Construction | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Structural) |
| CWP-FGS-R-03 | Process piping tie-ins shall be constructed per vendor PIP-007 piping plans/sections, PIP-008/PIP-009 isometrics, and PIP-004 Tie-In List/Scope Sheets. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Process Piping: Yes); Vendor Engineering Deliverables (Process piping interfaces) |
| CWP-FGS-R-04 | Utility piping tie-ins shall be installed per the vendor utility tie-in list. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Utility Piping: Yes) |
| CWP-FGS-R-05 | Relief / flare / vent connections shall be installed and proven per vendor PIP-004 tie-in scope and facility flare network configuration. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Relief/Flare/Vent: Yes) |
| CWP-FGS-R-06 | Drain and secondary containment connections shall be installed per vendor PRO-023 / CIV-014 outputs as they apply at the package boundary. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Drain/Containment: Yes); Vendor Engineering Deliverables (Drainage/containment interfaces) |
| CWP-FGS-R-07 | I&C control cabling shall be terminated per vendor INS-009 wiring/termination diagrams, INS-010 junction box/marshalling, INS-011 cable schedule, and INS-008 loop diagrams. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (I&C/Control Cabling: Yes); Vendor Engineering Deliverables (Instrumentation) |
| CWP-FGS-R-08 | Fire & gas devices shall be installed per vendor TSF-003 mapping study and TSF-004 detector layout drawings, integrated to facility F&G logic. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Fire & Gas/Safety Systems: Yes); Vendor Engineering Deliverables (Fire and gas) |
| CWP-FGS-R-09 | Grounding and bonding shall be installed per vendor ELE-019 Earthing/Bonding Layout Drawings. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Grounding/Bonding: Yes); Vendor Engineering Deliverables (Electrical) |
| CWP-FGS-R-10 | Area/exterior lighting at the package shall be installed per facility ELE-017 Lighting Layout Drawings; interface row from `26020-Packages_Interfaces.3.xlsx` (column M) shall be reconciled prior to fabrication. (ASSUMPTION: row reference 99 in source applies; the source-stated row should be confirmed against the actual 4-25 interface row 61.) | Construction / Coordination | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Area/Exterior Lighting: Yes; referenced row in source) |
| CWP-FGS-R-11 | Structural supports/access platforms shall be installed per vendor STR-002 / STR-011 / STR-012. | Construction | `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary (Structural / Foundations / Supports: Yes; Maintenance Access: Yes); Vendor Engineering Deliverables (Structural) |
| CWP-FGS-R-12 | The electric heater 600 V SCR power feed shall be terminated at the skid even though the Physical Interface Summary row "Electrical Power" is marked "No" — this is a source-internal conflict and shall be resolved by human ruling before fabrication. | Construction / Conflict | `_Sources/26020-Package_Requirements.docx`, Major Included Equipment (SCR 600 V) vs Physical Interface Summary (Electrical Power: No) — see `Guidance.md` Conflict Table |
| CWP-FGS-R-13 | Hydrotest and pressure test packages shall be executed per vendor PIP-024 (Hydrotest / Pressure Test Packages). | Construction Verification | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Process piping interfaces) |
| CWP-FGS-R-14 | Flushing, cleaning, and drying shall be executed per vendor PIP-025. | Construction Verification | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Process piping interfaces) |
| CWP-FGS-R-15 | Electrical FAT/SAT shall be performed per vendor ELE-029 and recorded per ELE-030 (energization package). | Construction Verification | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Electrical) |
| CWP-FGS-R-16 | Mechanical FAT / performance test execution and reporting shall use vendor MEC-021 / MEC-022. | Construction Verification | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Mechanical core package) |
| CWP-FGS-R-17 | Construction shall produce piping as-built drawings (PIP-028), instrument as-built drawings (INS-029), and feed structural/foundation as-builts into the facility as-built set. | Construction Documentation | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Process piping interfaces; Instrumentation) |
| CWP-FGS-R-18 | A construction interface and turnover checklist shall be issued documenting completion of every applicable Physical Interface Summary row. | Construction Documentation | `_CONTEXT.md` Anticipated Artifacts; `_Sources/26020-Package_Requirements.docx`, Physical Interface Summary |
| CWP-FGS-R-19 | An installation and tie-in workface plan shall be produced sequencing the work scope items SOW-0099 through SOW-0102. | Construction Planning | `_CONTEXT.md` Anticipated Artifacts and Covers Scope Items |

## Standards

| Standard | Location | Source |
|---|---|---|
| Vendor-specified codes referenced in MEC-001 Mechanical Design Basis | location TBD | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Mechanical) |
| Facility-level piping code (likely ASME B31.3, ASSUMPTION) | location TBD | ASSUMPTION — discipline convention; not extracted from source slice |
| Facility-level structural code (likely AISC + applicable seismic, ASSUMPTION) | location TBD | ASSUMPTION — discipline convention; not extracted from source slice |
| Facility-level electrical code (likely CEC/NEC depending on jurisdiction, ASSUMPTION) | location TBD | ASSUMPTION — jurisdiction not asserted in source slice |

Hazardous area classification, jurisdictional code edition, and seismic site class are TBD and shall be drawn from the facility design basis when its location is identified.

## Verification

| Requirement Coverage | Verification Approach | Evidence |
|---|---|---|
| CWP-FGS-R-01 to R-02 (set + foundation) | Survey of skid set; foundation inspection; anchor torque records | Foundation inspection report; survey record |
| CWP-FGS-R-03 to R-06 (piping tie-ins) | Visual inspection; PIP-024 hydrotest; PIP-025 flushing/drying | Hydrotest packages; flushing certificates |
| CWP-FGS-R-07 (I&C cabling) | Continuity test; loop check using vendor INS-008 | Loop check records |
| CWP-FGS-R-08 (F&G) | Detector commissioning per vendor TSF-003 / TSF-004 | F&G commissioning records |
| CWP-FGS-R-09 (grounding) | Earth-resistance testing per ELE-019 | Grounding test records |
| CWP-FGS-R-10 (lighting) | Illuminance verification per ELE-017 | Lighting commissioning record |
| CWP-FGS-R-11 (structural/access) | Walkdown vs STR-002/STR-011 | Structural turnover walkdown record |
| CWP-FGS-R-12 (heater power conflict) | Human ruling on Electrical Power applicability; install only after ruling | Conflict ruling record (see Conflict Table) |
| CWP-FGS-R-13 to R-16 (test and FAT/SAT) | Per PIP-024, PIP-025, ELE-029, MEC-021 | Test records (PIP-024 outputs; ELE-030; MEC-022) |
| CWP-FGS-R-17 (as-builts) | Drawing turnover and as-built sign-off | PIP-028, INS-029 |
| CWP-FGS-R-18 to R-19 (CWP documents) | Issue and sign-off of turnover checklist and workface plan | This deliverable's three anticipated artifacts |

## Documentation

Required artifacts delivered by this CWP:

- Construction Work Package (this deliverable's primary artifact; from `_CONTEXT.md` Anticipated Artifacts).
- Installation and Tie-In Workface Plan (from `_CONTEXT.md` Anticipated Artifacts).
- Construction Interface and Turnover Checklist (from `_CONTEXT.md` Anticipated Artifacts).

Consumed upstream documentation (vendor-engineered; not produced here):

- Mechanical: MEC-001, MEC-002, MEC-003, MEC-006, MEC-014, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025.
- Process piping: PRO-008, PIP-003, PIP-004, PIP-006, PIP-007, PIP-008, PIP-009, PIP-017, PIP-018, PIP-024, PIP-025, PIP-028.
- Drainage/containment: PRO-023, CIV-014.
- Electrical: ELE-002, ELE-003, ELE-012, ELE-014, ELE-015, ELE-016, ELE-017, ELE-019, ELE-020, ELE-027, ELE-028, ELE-029, ELE-030.
- Instrumentation: INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, INS-010, INS-011, INS-015, INS-016, INS-017, INS-018, INS-025, INS-029, CTL-003, CTL-005, CTL-006, CTL-026.
- Fire & gas / safety: TSF-002, TSF-003, TSF-004, TSF-009, TSF-011, TSF-013, TSF-028.
- Structural: STR-001, STR-002, STR-004, STR-005, STR-006, STR-011, STR-012, STR-013, STR-014, STR-020.
- Loading/metering: INS-015, PRO-025, PIP-004, PIP-018.
- Quality/manufacturing: QLT-003, QLT-006, QLT-013, QLT-020, QLT-021, PRQ-009, PRQ-013, PRQ-015, PRQ-016, DOC-008.

(All vendor deliverable IDs above are sourced from `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables for the 4-25 instance of `26020-01-PT-23-001 - Fuel Gas Skid`.)
