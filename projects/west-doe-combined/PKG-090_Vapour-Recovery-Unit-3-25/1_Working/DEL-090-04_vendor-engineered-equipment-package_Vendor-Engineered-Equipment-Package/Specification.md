# Specification — DEL-090-04 Vendor Engineered Equipment Package (PKG-090 Vapour Recovery Unit 3-25)

> Normative view. Requirements are drawn from accessible sources; inferences are labeled `ASSUMPTION`; missing source detail is `TBD`.

## Scope

This specification governs the Vendor Engineered Equipment Package for PKG-090, Vapour Recovery Unit 3-25 at the 03-25 West Doe Compressor Station and Liquids Hub. The deliverable is the Package Vendor's production unit covering engineering, design, fabrication / supply, and the physical equipment package, developed from the EPC Integrator's `DEL-090-01 Scope of Work` and `DEL-090-02 Package Datasheet`. (`_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row 567.)

### In scope
- Vendor engineering and design of two (2) 100% capacity VRU compressor packages in lead-lag configuration, both housed in one building, with two-stage Ro-Flo 12S/212M positive-displacement rotary-vane compressors and 200 HP VFD motor drivers. (PACKAGE_REGISTER.csv row 100.)
- Vendor package design basis and datasheet set covering the package and its sub-components. (`_CONTEXT.md` Anticipated Artifacts.)
- Vendor-side mechanical / electrical / I&C scope within the package boundary, including package internal piping, vessels, skid structure, package PLC and local controls, package electrical, and package safety devices. (PACKAGE_REGISTER.csv row 100 "Detailed process mechanical scope and vendor documentation requirements from the Word package section"; ASSUMPTION: itemization aligns with package-vendor industry practice — exact split confirmed against `26020-Package_Requirements.docx` heading 43, which was not locally readable during this pass.)
- Vendor recycle control configuration meeting DBM intent: second-stage discharge to first-stage suction, sized for 100 percent flow at minimum driver speed and lowest discharge pressure. (`3-25_Comp_and_Liquids_DBM.md` L438.)
- Vendor make-up / blanket gas pressure regulation from LP fuel gas to maintain minimum suction pressure at maximum turndown. (DBM L438.)
- Vendor LP-flare bypass arrangement on the VRU suction header (V-ball valve operated by VRU suction pressure; header free-drain or slope toward flare KO interface) up to the package boundary. (DBM L438.)

### Out of scope (allocated to EPC Integrator or other deliverables)
- Whole-facility integration, tie-ins, constructability, procurement / construction coordination, and facility-level integration. (PACKAGE_REGISTER.csv row 100.)
- Routing of VRU discharge to 04-25 SOC suction (handled at the facility / interface level under SCA-002). (DBM L36, L66.)
- Detailed flare KO interface design downstream of the VRU suction header drain point. (DBM L438; ASSUMPTION: confirmed against EPC Scope of Work DEL-090-01.)
- Construction installation, commissioning, and turnover (covered by `DEL-090-03 Construction Work Package` and `DEL-090-06 EPC Vendor Package Review and Acceptance`).

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| REQ-090-04-001 | The vendor shall supply two (2) complete 100% capacity VRU compressor packages in lead-lag configuration for sour service, both housed in one building. | PACKAGE_REGISTER.csv row 100; DBM L436 |
| REQ-090-04-002 | Each train shall include a two-stage Ro-Flo 12S/212M positive-displacement rotary-vane compressor. | PACKAGE_REGISTER.csv row 100 |
| REQ-090-04-003 | Each compressor shall be driven by a 200 HP VFD electric motor. | PACKAGE_REGISTER.csv row 100; DBM L36, L524 |
| REQ-090-04-004 | The VRU package shall collect vapours from condensate and produced-water tank systems and selected process vents as defined by the active process basis. | DBM L436 |
| REQ-090-04-005 | The VRU recycle valve shall return second-stage discharge to first-stage suction to maintain suction pressure, sized for 100 percent flow at minimum driver speed and lowest discharge pressure. | DBM L438 |
| REQ-090-04-006 | The vendor shall provide a make-up / blanket-gas pressure regulator from low-pressure fuel gas to maintain minimum suction pressure at maximum turndown. | DBM L438 |
| REQ-090-04-007 | The VRU suction header shall include an LP flare bypass V-ball valve operated by VRU suction pressure. The header shall free-drain or slope toward the flare KO interface as defined by detailed design. | DBM L438 |
| REQ-090-04-008 | Discharge interface — VRU discharge shall be configured to deliver to the 04-25 SOC suction interface under the current SCA-002 basis; the package shall not assume any local 03-25 SOC. | DBM L36, L66, L436 |
| REQ-090-04-009 | The vendor scope shall include package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility-level integration. | PACKAGE_REGISTER.csv row 100 |
| REQ-090-04-010 | The package shall provide / coordinate the following interface types with the EPC Integrator: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row 100 |
| REQ-090-04-011 | Package sizing redundancy shall meet 2 x 100 percent train arrangement with 50 percent flow contribution per train basis as carried in the facility DBM. | DBM L574, L597 |
| REQ-090-04-012 | Detailed process-mechanical scope and vendor documentation requirements as set out in `26020-Package_Requirements.docx` package heading 43 shall be incorporated. (`location TBD` — source not locally readable this pass.) | PACKAGE_REGISTER.csv row 100 "Detailed process mechanical scope and vendor documentation requirements from the Word package section" |
| REQ-090-04-013 | The package shall be designed for sour service consistent with the facility sour-gas basis. Specific composition / H2S level for the VRU stream: `TBD`. | PACKAGE_REGISTER.csv row 100 |
| REQ-090-04-014 | Final failure action for recycle / control valves shall align with package safety analysis. (Inlet-compressor analogue: recycle valves expected fail-open; final action TBC at facility level.) `ASSUMPTION` carry-over pending VRU-specific source confirmation. | DBM L334 (analogue) |

## Standards

| Standard / Code | Applies To | Notes |
|---|---|---|
| Sour-service / sulphide-stress materials (e.g. NACE MR0175 / ISO 15156) | Compressor wetted parts, piping, vessels | `ASSUMPTION` — sour service is stated in source; specific code citation not in accessible slice. `location TBD`. |
| Canadian electrical code; hazardous-area classification (CSA / IEC) | Package electrical and instrumentation | `ASSUMPTION`; specific code references `TBD` pending `26020-Package_Requirements.docx` access. |
| ASME / CRN pressure-equipment requirements | Vessels, piping > scope thresholds | `ASSUMPTION`; specific citation `TBD`. |
| Detailed vendor-documentation requirements from `26020-Package_Requirements.docx` heading 43 | Vendor documentation set | `location TBD` (source not locally readable this pass). |

## Verification

| Req ID | Verification Approach |
|---|---|
| REQ-090-04-001..003 | Vendor datasheet / nameplate review against package datasheet (DEL-090-02). |
| REQ-090-04-004 | P&ID and process-flow review against active process basis; tank-vapour source list confirmed. |
| REQ-090-04-005..006 | Sizing calculation review (recycle valve at minimum-speed / lowest-discharge case); regulator sizing case at maximum turndown. |
| REQ-090-04-007 | Suction-header drawing review; bypass V-ball valve sizing; drain-slope check. |
| REQ-090-04-008 | Interface document review against 04-25 SOC suction conditions and SCA-002. |
| REQ-090-04-009..010 | Responsibility matrix and interface-register review with EPC Integrator. |
| REQ-090-04-011 | Compressor performance curves at 100% per train; turndown demonstration. |
| REQ-090-04-012 | Document-register cross-check against `26020-Package_Requirements.docx` heading 43 (`location TBD` until source accessed). |
| REQ-090-04-013..014 | Materials traceability / mill certs; sour-service compliance; safety review of recycle / control-valve fail action. |

## Documentation

The vendor shall supply the documentation set comprising the vendor package design basis and datasheet set, as anticipated by `_CONTEXT.md`. Specific document list (drawings, datasheets, calculations, test plans, ITPs, manuals, spare-parts list, etc.) governed by `26020-Package_Requirements.docx` package heading 43 — `location TBD` until source is accessible. Vendor documentation delivery is captured separately under `DEL-090-05 Vendor Document Turnover Package`.
