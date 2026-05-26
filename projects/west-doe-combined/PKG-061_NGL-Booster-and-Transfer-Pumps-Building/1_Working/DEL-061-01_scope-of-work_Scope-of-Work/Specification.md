# Specification — DEL-061-01 Scope of Work (PKG-061 NGL Booster and Transfer Pumps Building)

## Scope

### In scope

This Scope of Work covers the EPC Integrator's definition of the NGL Booster and Transfer Pumps Building package (PKG-061) for the 4-25 Deepcut facility, including:

- Identity and function of the package within the whole-facility integration narrative (transfer of NGL/LPG product from storage to LACT, where booster pressure may be required). [Source: SOW-0149, SOW-0150]
- Tagged equipment list and configuration (two parallel booster pumps P-9570-1 and P-9580-1). [Source: SOW-0150, SOW-0151; DBM-Deepcut equipment table line 2609]
- Package-supplied content and vendor responsibility boundaries (pumps, seals, drivers, skid, package piping, instrumentation, electrical, HVAC/enclosure, CRN/TSBC, commissioning support). [Source: SOW-0151]
- Exclusions and EPC-Integrator-supplied scope (DCS integration, foundations, MCC electrical supply). [Source: SOW-0152]
- Responsibility assignment (Package Vendor for engineering/design/equipment; EPC Integrator for facility integration). [Source: SOW-0149]

### Out of scope

- Detailed mechanical/hydraulic design of the pumps (Package Vendor deliverable; see DEL-061-04 Vendor Engineered Equipment Package).
- LACT unit design and ownership — LACT inclusion is TBD at facility level (DBM-Deepcut line 62) and is not assigned to PKG-061.
- Upstream NGL storage bullets and downstream NGL pipeline / NEBC Connector tie-ins beyond the package skid edge.
- Detailed construction and tie-in execution (see DEL-061-03 Construction Work Package).

## Requirements

### R-1: Package function

The vendor shall supply the NGL Booster and Transfer Pumps Building as a complete package whose function is to transfer LPG/NGL product from LPG storage to the LACT unit, where booster pressure may be required. [Source: SOW-0150]

### R-2: Equipment configuration

The vendor shall supply two LPG/NGL booster pumps arranged in parallel, tagged P-9570-1 and P-9580-1. [Source: SOW-0150, SOW-0151]

### R-3: Pump construction

Each pump shall be a vertical multistage can-type pump in accordance with API 610, with API 682 seal plan 13/52 (as referenced in SOW-0151). [Source: SOW-0151; DBM-Deepcut equipment table line 2609 (API 610, multi-stage can)]

### R-4: Pump hydraulic sizing

Each pump shall be sized for 145 m3/h at 150% capacity; booster pump design differential is 25 psid / 172 kPad. TDH at rated point is TBD. [Source: SOW-0152]

### R-5: Pump driver

Each pump motor shall be 575 V, 3-phase, 60 Hz. [Source: SOW-0151]

### R-6: Mechanical seals

Mechanical seals shall be supplied per API 610 / API 682 with the seal plan combination 13/52 (single seal with self-flushing plan 13 and unpressurized buffer-fluid plan 52, as named in SOW-0151). ASSUMPTION: this is the conventional reading of "seal plan 13/52"; to be confirmed during detailed engineering against the source slice. [Source: SOW-0151]

### R-7: Package boundary content

The vendor package shall include: structural skid, package piping, instrumentation, electrical, HVAC/enclosure, and CRN/TSBC documentation as applicable, and shall provide commissioning support. [Source: SOW-0151]

### R-8: Regulatory documentation

Pressure-containing components shall carry CRN registration; package pressure equipment shall carry TSBC documentation as applicable (Alberta TSBC jurisdiction inferred from facility location; ASSUMPTION pending confirmation). [Source: SOW-0151]

### R-9: Exclusions (Integrator scope)

The following items are NOT part of the vendor package and shall be supplied by others under EPC Integrator coordination: DCS integration, foundations, and electrical supply to the MCC. [Source: SOW-0152]

### R-10: Responsibility split

The Package Vendor is responsible for engineering, design, fabrication/supply, and the physical equipment package. The EPC Integrator is responsible for facility integration, including tie-ins, structural foundation design, MCC supply, and DCS configuration. [Source: SOW-0149, SOW-0152]

### R-11: Interface — upstream (NGL storage)

The package suction shall connect to NGL storage (current basis sixteen 120,000 USG NGL storage bullets at 4-25). Detailed suction conditions (pressure, NPSHA, temperature, composition) are TBD and shall be confirmed during detailed engineering. [Source: DBM-Deepcut line 448; TBD per absence in heading 17]

### R-12: Interface — downstream (LACT / NEBC Connector)

The package discharge shall deliver NGL C3+ product to the LACT unit for transfer to the NRM NEBC Connector. LACT scope, ownership, and design responsibility remain TBD at the facility level and must be reconciled before pump discharge pressure can be finalized. [Source: DBM-Deepcut lines 57, 62, 82, 446]

### R-13: Whole-facility integration narrative

The EPC Integrator shall include in this Scope of Work the package's whole-facility integration narrative, source basis, boundaries, and the responsibility assignment record. [Source: DELIVERABLE_REGISTER.csv DEL-061-01 description; SOW-0149]

## Standards

| Standard | Application | Location |
|---|---|---|
| API 610 | Pump type/design (vertical multistage can-type) | Referenced by SOW-0151 and DBM-Deepcut line 2609 |
| API 682 seal plans 13/52 | Mechanical seal arrangement | Referenced by SOW-0151 (seal plan number convention is from API 682) |
| CRN (Canadian Registration Number) | Pressure-containing components | SOW-0151 |
| TSBC | Pressure equipment regulatory documentation | SOW-0151 (jurisdiction-specific — ASSUMPTION: BC/Alberta TSBC analogue; location TBD) |
| CSA/CEC (electrical) | 575 V / 3-phase / 60 Hz motors and package electrical | ASSUMPTION: Canadian electrical code applies given CRN/TSBC framing; location TBD |

Standards beyond those explicitly named in heading 17 are recorded as ASSUMPTION or location TBD until confirmed in detailed engineering.

## Verification

| Requirement | Verification approach |
|---|---|
| R-1, R-2 | EPC Integrator review of vendor package P&ID and equipment list against this Scope of Work |
| R-3, R-5 | Vendor datasheet review (DEL-061-02) and vendor engineering submittal (DEL-061-04) |
| R-4 | Vendor pump curve and head/flow certified test (FAT) per API 610; sizing confirmation against design differential 25 psid |
| R-6 | Seal arrangement drawing and seal plan piping verification at FAT |
| R-7, R-9 | Package boundary drawing and battery-limits list reviewed at EPC Vendor Package Review (DEL-061-06) |
| R-8 | CRN registration certificate and TSBC documentation submitted with vendor turnover package (DEL-061-05) |
| R-10 | Responsibility matrix maintained in this Scope of Work and tracked in DEL-061-06 acceptance |
| R-11, R-12 | Interface confirmation with facility process and instrument data; LACT TBD resolution captured in Conflict Table (Guidance) |
| R-13 | EPC Integrator review against deliverable register description |

## Documentation

Per anticipated artifacts for DEL-061-01:

- Package scope of work (this document set)
- Tagged equipment and package identity list (Datasheet identification + equipment tables)
- Package function and integration narrative (Guidance + Specification scope)
- Responsibility assignment record (Specification R-9, R-10; cross-referenced in DEL-061-03 and DEL-061-06)

Related downstream deliverables (out of scope for this document but listed for traceability): DEL-061-02 Package Datasheet, DEL-061-03 Construction Work Package, DEL-061-04 Vendor Engineered Equipment Package, DEL-061-05 Vendor Document Turnover, DEL-061-06 EPC Vendor Package Review and Acceptance.
