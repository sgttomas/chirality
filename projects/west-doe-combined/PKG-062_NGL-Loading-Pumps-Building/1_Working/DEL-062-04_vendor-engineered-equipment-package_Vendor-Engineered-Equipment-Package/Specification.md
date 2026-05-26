# Specification — DEL-062-04 Vendor Engineered Equipment Package (NGL Loading Pumps Building)

> Normative requirements for the Package Vendor's engineered NGL Loading Pumps Building equipment package. Requirements are derived from accessible source slices in the GATE-07 PROJECT_DECOMP snapshot (which extracts `26020-Package_Requirements.docx` package heading 16 and workbook Packages row 76). Inferences are labelled `ASSUMPTION`; missing values are marked `TBD`.

## Scope

### Included

- Vendor engineering, package design, fabrication/supply, and the physical equipment package for the NGL Loading Pumps Building (PKG-062). [SOW-0153]
- Supply of four (4) identical Blackmer Model LGL4B rotary vane pumps arranged in parallel, sized to move LPG product from storage to LPG Truck Loading. [SOW-0154; SOW-0155]
- Self-framing building to be erected at site as part of the vendor-supplied package. [SOW-0155]
- Pump electric motor drivers (575 V / 3-phase / 60 Hz) with local Hand-Off-Auto or On-Off control. [SOW-0156]
- Vendor package design basis and datasheet set as anticipated artifacts. [`_CONTEXT.md` Anticipated Artifacts]

### Excluded ("By Others")

- DCS integration. [SOW-0156]
- Foundations. [SOW-0156]
- Electrical supply to the MCC (i.e., the 600 V MCC and its upstream feed). [SOW-0156]

EPC Integrator retains responsibility for facility integration review and for the excluded items above. [OBJ-004]

## Requirements

### R1 — Pump quantity, type, and configuration

- R1.1 The package SHALL include four (4) pumps. [SOW-0154; SOW-0155]
- R1.2 Pumps SHALL be Blackmer Model LGL4B rotary vane pumps. [SOW-0154; SOW-0155]
- R1.3 Pumps SHALL be arranged in parallel. [SOW-0154]
- R1.4 Pumps SHALL be tagged P9510-1, P9520-1, P9530-1, P9540-1. [SOW-0155]

### R2 — Capacity

- R2.1 Each pump SHALL deliver 68 m³/hr (300 USGPM) at 345 kPad (50 psid). [SOW-0155; SOW-0156]
- R2.2 Total developed head (TDH) is identified TBC and SHALL be confirmed by the vendor against the LPG service and the storage-to-truck-loading hydraulic profile. [SOW-0155; SOW-0156]

### R3 — Process function and service

- R3.1 The pumps SHALL move LPG product from storage to LPG Truck Loading. [SOW-0154]
- R3.2 The vendor SHALL confirm material and seal selection for LPG service. [ASSUMPTION; OBJ-009 sour-service applicability TBD]

### R4 — Drivers and motor sizing

- R4.1 Drivers SHALL be electric motors rated 575 V / 3-phase / 60 Hz. [SOW-0156]
- R4.2 Motors SHALL be sized for inlet stabilizer composition density at the −40 °C start-up condition. [SOW-0156]
- R4.3 Motors SHALL be fed from the 600 V MCC (supply by others). [SOW-0156]

### R5 — Local control

- R5.1 Each pump SHALL include local control (Hand-Off-Auto or On-Off switch). [SOW-0156]
- R5.2 DCS integration is by others; the package SHALL provide the interfaces required for the EPC's DCS integration. [SOW-0156; OBJ-006]

### R6 — Building

- R6.1 A self-framing building SHALL be supplied as part of the package and erected at site. [SOW-0155]
- R6.2 Building dimensions, layout, ventilation/HVAC, lighting, and electrical area classification are TBD and SHALL be vendor-engineered consistent with LPG service and site conditions. [TBD; OBJ-005; OBJ-007]

### R7 — Site / environmental basis

- R7.1 The package SHALL be designed for the site start-up condition of −40 °C (motor sizing basis). [SOW-0156]
- R7.2 Operating and design conditions are TBC; vendor SHALL confirm against capacity and site conditions. [SOW-0156]

### R8 — Boundary and interfaces

- R8.1 The package SHALL exclude DCS integration, foundations, and the electrical supply to the MCC (these are "by others"). [SOW-0156]
- R8.2 The vendor SHALL provide interface information (mechanical/process, electrical load, controls/instrumentation) sufficient to support EPC integration. [ASSUMPTION; OBJ-004; OBJ-005; OBJ-006]

### R9 — Responsibility model

- R9.1 The Package Vendor SHALL own package engineering, package design, vendor documentation, and physical equipment supply. [OBJ-004]
- R9.2 The EPC Integrator SHALL own facility integration and interface review of the vendor package. [OBJ-004]

### R10 — Vendor documentation (turnover)

- R10.1 The vendor SHALL produce the vendor package design basis and datasheet set declared as anticipated artifacts. [`_CONTEXT.md`]
- R10.2 Detailed vendor-document turnover requirements are governed by DEL-062-05 (Vendor Document Turnover Package). [ASSUMPTION based on PKG-062 deliverable set; OBJ-010]

## Standards

- Workbook Packages row 76 and `26020-Package_Requirements.docx` package heading 16 (cited; section text not directly accessible in PREPARATION set) — location TBD for clause-level reads.
- Applicable codes/standards for LPG service, electrical area classification, and sour-service applicability: TBD (location TBD; to be resolved against `OBJ-009` regulatory/codes basis when the source slice becomes accessible).
- Project DBM references (relevant to objectives, not necessarily clause-binding for this package): `DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-12, SEC-13, SEC-14, SEC-15), `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-12..SEC-15). [OBJ-005, OBJ-006, OBJ-009 source references]

## Verification

| Req | Verification approach |
|---|---|
| R1.1–R1.4 | Inspection of vendor data sheets and bill of materials; receipt inspection. |
| R2.1 | Vendor performance curves; factory acceptance test (FAT) at rated point. |
| R2.2 | Vendor hydraulic calculation review confirming TDH against actual storage-to-truck profile. |
| R3.1 | Process design review against package datasheet (DEL-062-02). |
| R3.2 | Material/seal selection review against service definition. |
| R4.1–R4.3 | Electrical data sheet review; motor nameplate inspection; MCC coordination review with EPC. |
| R5.1 | Inspection of local control devices; functional checkout. |
| R5.2 | I/O list and interface schedule review with EPC controls. |
| R6.1 | Building delivery and erection inspection. |
| R6.2 | Vendor building drawings review (architectural, HVAC, lighting, area classification). |
| R7.1 | Motor sizing calculation review; low-temperature start-up demonstration (FAT or site). |
| R7.2 | Vendor confirmation memo of operating/design conditions. |
| R8.1 | Interface boundary drawing review with EPC. |
| R8.2 | Interface package transmittal to EPC; EPC integration review (DEL-062-06). |
| R9.1–R9.2 | Compliance with EPC Scope of Work (DEL-062-01) and responsibility matrix. |
| R10.1 | Document register checkoff at turnover (DEL-062-05). |
| R10.2 | Turnover package acceptance per DEL-062-05. |

## Documentation

Vendor SHALL deliver, at minimum:

- Vendor package design basis. [`_CONTEXT.md`]
- Vendor package datasheet set (pumps, motors, building, instrumentation). [`_CONTEXT.md`]
- Equipment data sheets for the four LGL4B pumps and motors. [derived from R1, R4]
- Building drawings and area classification drawing. [derived from R6]
- Interface drawings/schedules for mechanical, electrical, controls, fire/gas (TBD applicability). [OBJ-004..OBJ-006]
- Test reports (FAT) and certifications applicable to LPG service. [TBD]
- Additional turnover deliverables per DEL-062-05. [ASSUMPTION; OBJ-010]
