# Specification — Vendor Engineered Equipment Package (DEL-100-04)

> Normative requirements for the Package Vendor's engineered Hydrogen Peroxide Sweetening
> Unit production unit. Requirements are drawn from the locally accessible source slice
> `26020-03-PT-27-001 — Hydrogen Peroxide Sweetening Unit` in
> `_Sources/26020-Package_Requirements.docx` (package heading 52). Inferences are labeled
> **ASSUMPTION**; values not present in source are `TBD`.

## Scope

### In Scope

The Package Vendor shall engineer, design, fabricate/supply, and deliver one (1) hydrogen
peroxide sour-water treatment package suitable for installation at the 3-25 West Doe
Liquids Hub site, consisting of (source: package heading 52, "Basic Scope" and "Major
Included Equipment"):

1. Hydrogen Peroxide Storage Tank — 400 BBL capacity.
2. Hydrogen Peroxide chemical injection pumps (Vendor to design).
3. Static Mixer (Vendor to design).
4. Hydrogen Peroxide Reactor(s) (Vendor to design).
5. Additional equipment as shown in the package PFD (PFD `location TBD`).
6. Self-framing building, erected at site.

### Out of Scope (by others)

Per package heading 52 "Scope Notes / Open Items", the following are by others:

- Interconnecting piping (tie-ins between package and site).
- DCS integration.
- Foundations.
- Electrical supply to MCC.

### Scope Items Covered

This deliverable covers Scope of Work items `SOW-0107`, `SOW-0108`, `SOW-0109`, `SOW-0110`
(source: `_CONTEXT.md`).

## Requirements

### R-PROC — Process Design Requirements

| ID | Requirement | Source |
|---|---|---|
| R-PROC-001 | The package shall treat sour water by routing it through a static mixer and then to hydrogen peroxide reactor(s). | Package heading 52, "Process function" |
| R-PROC-002 | Hydrogen peroxide shall be metered into the process from the H₂O₂ storage tank via chemical injection pumps. | Package heading 52, "Process function" |
| R-PROC-003 | Treated water shall be routed to produced water storage tanks (downstream interface). | Package heading 52, "Process function" |
| R-PROC-004 | Package shall be designed for a treatment capacity of 24,154 BBL/D (160 m³/h). | Package heading 52, "Capacity/design throughput" |
| R-PROC-005 | Package shall be designed for sour-water inlet conditions: 9 °C, 340.54 kPag, 160 m³/h. | Package heading 52, "Operating conditions" |
| R-PROC-006 | H₂O₂ shall be supplied from onsite tanks. | Package heading 52, "Design conditions" |

### R-MEC — Mechanical / Equipment Requirements

| ID | Requirement | Source |
|---|---|---|
| R-MEC-001 | Provide one (1) 400 BBL Hydrogen Peroxide Storage Tank. | Package heading 52, "Major Included Equipment" |
| R-MEC-002 | Provide chemical injection (hydrogen peroxide) pumps; sizing/quantity vendor-designed. Pump capacity `TBC` per source. | Package heading 52, "Major Included Equipment"; "Capacity/design throughput" |
| R-MEC-003 | Provide static mixer (vendor-designed). | Package heading 52, "Major Included Equipment" |
| R-MEC-004 | Provide hydrogen peroxide reactor(s) (vendor-designed). | Package heading 52, "Major Included Equipment" |
| R-MEC-005 | Provide self-framing building suitable for site erection. | Package heading 52, "Major Included Equipment" |
| R-MEC-006 | Provide any additional equipment depicted in the package PFD. | Package heading 52, "Major Included Equipment" (PFD `location TBD`) |

### R-ENV — Environmental / Ambient Requirements

| ID | Requirement | Source |
|---|---|---|
| R-ENV-001 | Equipment shall be suitable for ambient temperature range −40 °C (min) to +35 °C (max). | Package heading 52, "Design conditions" |

### R-ELE — Electrical Requirements

| ID | Requirement | Source |
|---|---|---|
| R-ELE-001 | All pumps shall be driven by 575 V / 3-phase / 60 Hz motors. | Package heading 52, "Driver" |
| R-ELE-002 | Pump motor starting method shall be Direct-On-Line (DOL) or VFD. | Package heading 52, "Driver" |
| R-ELE-003 | Each pump motor shall be provided with local control (H-O-A or On-Off switch). | Package heading 52, "Driver" |
| R-ELE-004 | Electric motors shall be fed from a 600 V MCC. | Package heading 52, "Driver" |

### R-INT — Physical Interface Requirements (Applicability)

The package shall accommodate the following physical interfaces marked "Yes" in the
Physical Interface Summary (source: package heading 52). Cathodic Protection,
Communications/Network, Building HVAC/Services, Grading/Site Drainage/Spill Containment,
Product Loading, and Pipeline/Pigging are marked "No" and are not within the package
interface scope.

| ID | Interface |
|---|---|
| R-INT-PP | Process Piping |
| R-INT-UP | Utility Piping |
| R-INT-RFV | Relief / Flare / Vent |
| R-INT-DC | Drain / Containment |
| R-INT-EP | Electrical Power |
| R-INT-AEL | Area / Exterior Lighting |
| R-INT-EHT | EHT |
| R-INT-GB | Grounding / Bonding |
| R-INT-IC | I&C / Control Cabling |
| R-INT-FG | Fire & Gas / Safety Systems |
| R-INT-MA | Maintenance Access |
| R-INT-SF | Structural / Foundations / Supports |

### R-DESN — Design Condition Closure (open at source)

| ID | Requirement | Source / Status |
|---|---|---|
| R-DESN-001 | Process design conditions (pressure/temperature design margins, design pressure, design temperature) shall be confirmed (TBC). | Package heading 52: "Design conditions TBC" — `TBD` |
| R-DESN-002 | Pump capacity shall be confirmed by vendor design (TBC). | Package heading 52: pump capacity TBC — `TBD` |

## Standards

The source slice does not enumerate governing codes by clause. Standards/codes applicable
to vendor-designed pressure equipment, tanks, electrical, and instrumentation typically
apply via the vendor deliverable categories below; specific code citations are
**ASSUMPTION (likely applicable)** until confirmed by source review.

| Standard family | Applicability | Status |
|---|---|---|
| Pressure equipment registration (jurisdictional) | Required via `REG-022` Pressure Equipment Registration Package | Source — Vendor Engineering Deliverables list, "Static pressure equipment" |
| Pressure vessel code (e.g., ASME BPVC Sec. VIII Div. 1) | Likely applicable to reactor and any pressure vessels | ASSUMPTION — `location TBD` |
| Storage tank standard (e.g., API 650 / API 12F) | Likely applicable to 400 BBL H₂O₂ storage tank | ASSUMPTION — `location TBD` |
| Electrical area classification / wiring (e.g., CEC / CSA C22.1) | Likely applicable to onsite Canadian liquids hub | ASSUMPTION — `location TBD` |
| Fire & Gas / SIL framework | Source vendor deliverables include `TSF-009` SIL Determination and `TSF-011` SRS | Source — Vendor Engineering Deliverables list |
| Building / fire code | Source vendor deliverables include `REG-021` Fire Code / Building Code Compliance Package | Source — Vendor Engineering Deliverables list |

## Verification

| Requirement(s) | Verification Approach | Vendor Deliverable Anchors |
|---|---|---|
| R-PROC-001..006 | Review of vendor PFD, P&IDs, Process Description, Heat & Material Balance | `PRO-004`, `PRO-005`, `PRO-007`, `PRO-008`, `PRO-010` |
| R-MEC-001..006 | Review of mechanical equipment list, data sheets, GA drawings; FAT for pumps and rotating equipment | `MEC-002`, `MEC-003`, `MEC-007`, `MEC-009`, `MEC-011`, `MEC-016`, `MEC-021`, `MEC-022` |
| R-ENV-001 | Vendor design basis confirming ambient envelope; equipment data sheets | `MEC-001`, `MEC-003`, `ELE-020` |
| R-ELE-001..004 | Review of electrical load list, SLDs, motor data sheets, motor starting study; FAT/SAT | `ELE-002`, `ELE-003`, `ELE-020`, `ELE-011`, `ELE-029`, `ELE-030` |
| R-INT-* | Review of physical interface coordination; tie-in list; cause-and-effect; piping & cable schedules | `PIP-004`, `CTL-005`, `INS-011`, `PIP-003` |
| R-DESN-001..002 | TBC closure during vendor engineering; recorded in mechanical design basis and rotating equipment specs | `MEC-001`, `MEC-004`, `PRO-013` |
| Registration / code conformance | Submission of pressure equipment registration; fire/building code compliance package | `REG-022`, `REG-021` |
| Safety system integrity | SIL determination, SRS, supplier SIL documentation | `TSF-009`, `TSF-011`, `TSF-013` |

Acceptance is by EPC Integrator review per the downstream review and acceptance
deliverable (`DEL-100-06`).

## Documentation

The Package Vendor shall provide the deliverable set enumerated in
`Datasheet.md` §"Vendor Engineering Deliverables" (reproduced verbatim from package
heading 52). The set covers core vendor documents, core package engineering, rotating
equipment, static pressure equipment, storage tanks, process package design, relief/flare/
vent design, process piping, drainage/containment, electrical, instrumentation & controls,
building/HVAC/code, fire & gas / technical safety, and structural/foundations/access.

The final consolidated Vendor Data Book shall be provided per `PRQ-016` (Vendor Data
Book / Final Supplier Documentation) and `MEC-023` (Vendor Data Book / Mechanical Final
Documentation). The vendor document control framework is governed by `PRQ-009` (Vendor
Document Index) and `DOC-008` (Vendor Document Control Procedure). (Source: package
heading 52, "Vendor Engineering Deliverables".)

Anticipated artifact set for this deliverable (from `_CONTEXT.md`):

- Vendor engineered physical equipment package.
- Vendor package design basis and datasheet set.

Vendor document turnover is captured separately by `DEL-100-05` (Vendor Document Turnover
Package).
