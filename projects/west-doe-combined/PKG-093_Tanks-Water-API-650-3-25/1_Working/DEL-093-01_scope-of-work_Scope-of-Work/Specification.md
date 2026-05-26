# Specification — DEL-093-01 Scope of Work (PKG-093 Tanks, Water (API 650) 3-25)

## Scope

### Included

This Scope of Work governs the EPC Integrator scope for PKG-093 "Tanks, Water (API 650) 3-25" and binds the Package Vendor to deliver the engineered equipment package described herein. The package consists of two (2) 3,800 bbl sweet produced water storage tanks (TK-9060-2 and TK-9070-2) plus a second item (Item No. 2) referenced in the source with `TBD` design parameters. The tanks store sweet produced water and process water at the 03-25 Liquids Hub. (Source: SOW-0229; SOW-0230; PACKAGE_REGISTER.csv PKG-093.)

The package includes engineering, design, fabrication/supply, and physical equipment delivery of the tanks and integral skim systems, internal coatings, heating provisions, blanket-gas provisions, and vendor documentation as required by 26020-Package_Requirements.docx heading 45. (Source: SOW-0231; PACKAGE_REGISTER.csv.)

### Excluded

The following are by others (not in the Package Vendor scope): foundations; site mounting of tanks; electrical and instrumentation installation; platforms; staircases; and other site-installed appurtenances. (Source: SOW-0232 "By others".) PACKAGE_REGISTER.csv records no further package-specific exclusions (TBD).

## Requirements

### REQ-093-01-01 — Code and Construction Basis

The tanks shall be designed and fabricated to modified API 650. (Source: SOW-0231; DBM §Produced-Water Storage.)

### REQ-093-01-02 — Tagged Equipment

The package shall include the following tanks at the listed capacity: TK-9060-2 (1 x 3,800 bbl); TK-9070-2 (1 x 3,800 bbl). (Source: SOW-0230; SOW-0231.) Tank dimensional volume is `TBD` per SOW-0231.

### REQ-093-01-03 — Item No. 2

Item No. 2, referenced in SOW-0232, shall be defined during detailed design. Design flow, operating temperature, tag, and capacity are `TBD`. (Source: SOW-0232; see CT-02.)

### REQ-093-01-04 — Process Service

The fluid service shall be non-sour produced water and process water. (Source: SOW-0230; SOW-0231.)

### REQ-093-01-05 — Internal Coating

Tank internal surfaces (floors, walls, roofs) shall be coated with Devchem 253. (Source: SOW-0231; DBM §Produced-Water Storage.)

### REQ-093-01-06 — External Insulation and Heating

The tanks shall be externally insulated and provided with heating sufficient to prevent freezing across the design temperature range. (Source: SOW-0231; DBM.)

### REQ-093-01-07 — Blanket Gas

The tanks shall be provided with LP fuel-gas blanket gas, designed in accordance with API-2000, to prevent vacuum during winter operation. (Source: SOW-0231.)

### REQ-093-01-08 — Skim System

Each tank shall be equipped with a Kennilworth-type HCL float skim system (one per tank). Skim float design SG shall be less than or equal to 0.67. (Source: SOW-0231.)

### REQ-093-01-09 — Design and Operating Conditions (Item No. 1)

Operating pressure: atmospheric. Operating temperature: 5 °C. Design pressure: 32 oz test pressure. Design temperature: -40 °C minimum / 60 °C maximum. Design flow: 15,300 kg/h; 3,584 Am3/d from compressor station and 240 Am3/d from cryo (4-25). (Source: SOW-0232.)

### REQ-093-01-10 — Fluid SG Basis

The tank design fluid SG is 1.25 (TBC per DBM). The downstream produced-water pump system is sized on SG 1.18. The discrepancy is a held item to be closed during detailed design. (Source: DBM §Produced-Water Storage; see Conflict Table CT-01 in Guidance.md.)

### REQ-093-01-11 — By Others

Foundations, site tank mounting, electrical/instrumentation, platforms, and staircase are excluded from the Package Vendor scope and are EPC Integrator / facility-side responsibility. (Source: SOW-0232.)

### REQ-093-01-12 — Interface Types

The package supports the following facility-integration interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. (Source: PACKAGE_REGISTER.csv PKG-093.)

### REQ-093-01-13 — Responsibility Split

Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: PACKAGE_REGISTER.csv; SOW-0229.)

## Standards

| Standard | Application | Source |
|---|---|---|
| API 650 (modified) | Tank design and fabrication | SOW-0231 (location TBD — clause reference unavailable in accessible sources) |
| API 2000 | Tank venting / blanket-gas design (vacuum prevention) | SOW-0231 (location TBD) |
| 26020-Package_Requirements.docx heading 45 | Project-specific package requirements | SOW-0229..0232 (location TBD — original Word source not opened) |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-093-01-01 | Vendor design dossier traced to API 650 (modified) clauses; EPC review per DEL-093-06. |
| REQ-093-01-02 | Tank tag list reconciled against TK-9060-2 / TK-9070-2 in package datasheet (DEL-093-02). |
| REQ-093-01-03 | Item No. 2 closure during detailed design; status carried in Conflict Table CT-02 until resolved. |
| REQ-093-01-04 | Service description on package datasheet; consistency check vs. DBM §Produced-Water. |
| REQ-093-01-05 | Coating spec on vendor data sheet; coating QA records in turnover (DEL-093-05). |
| REQ-093-01-06 | Insulation and heating design records; field acceptance per DEL-093-03 / DEL-093-06. |
| REQ-093-01-07 | API-2000 sizing calc in vendor doc package; blanket-gas tie-in shown on P&IDs. |
| REQ-093-01-08 | Skim system data sheet; float SG record. |
| REQ-093-01-09 | Operating/design condition row in package datasheet; nameplate vs. design check. |
| REQ-093-01-10 | Held-item closure record in design HOLD log; pump sizing reconciliation. |
| REQ-093-01-11 | Battery-limit drawing; EPC scope split table in EPC documentation. |
| REQ-093-01-12 | Interface matrix in DEL-093-02 Package Datasheet. |
| REQ-093-01-13 | Responsibility matrix endorsed in DEL-093-06 acceptance. |

## Documentation

Anticipated artifacts to be produced by this deliverable (per `_CONTEXT.md`):

- Package scope of work (this document set)
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

Companion deliverables (downstream consumers within PKG-093): DEL-093-02 (Package Datasheet); DEL-093-03 (Construction Work Package); DEL-093-04 (Vendor Engineered Equipment Package); DEL-093-05 (Vendor Document Turnover Package); DEL-093-06 (EPC Vendor Package Review and Acceptance).
