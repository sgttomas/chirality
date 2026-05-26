# Specification — DEL-086-04 Vendor Engineered Equipment Package

Status labels: `FACT`, `ASSUMPTION`, `TBD`, `location TBD` as in Datasheet.

## Scope

### Included

The Package Vendor production unit covers engineering, design, fabrication/supply, and the physical equipment package for the Flare Stack (Low Pressure), PKG-086, developed from the EPC Scope of Work (`DEL-086-01`) and Package Datasheet (`DEL-086-02`). The package is a reference/interface package for the LP flare stack and the associated LP flare stack blower. (`_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 59 — FACT)

Anticipated artifacts:
- Vendor engineered physical equipment package
- Vendor package design basis and datasheet set

(`_CONTEXT.md` Anticipated Artifacts — FACT)

### Excluded

- EPC Integrator scope: integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (`PACKAGE_REGISTER.csv` row 59 PrimaryResponsibilities — FACT)
- Upstream LP KO drum V-3900-2 and pump P-3900-2 are not vendor scope (they are facility scope per DBM line 499 — FACT).
- Package-specific exclusions beyond the above: TBD; no package-specific exclusions stated in source materials per `PACKAGE_REGISTER.csv` row 59 PackageExclusions (FACT).

## Requirements

| Req ID | Requirement | Source / Label |
|---|---|---|
| R-01 | The vendor package shall realize the EPC Scope of Work (`DEL-086-01`) and Package Datasheet (`DEL-086-02`) for tag 26020-02-PT-25-002 Flare Stack (Low Pressure). | `_CONTEXT.md` Scope; `PACKAGE_REGISTER.csv` row 59 (FACT) |
| R-02 | The LP flare shall be capable of receiving TEG regeneration, VRU, and compressor seal-pot services as defined by the active LP relief routing. | DBM line 499 (FACT) |
| R-03 | The LP relief header interface to the package shall be sized for 508 mm / 20 in carried in the current source basis (subject to final flare studies). | DBM line 499 (FACT) |
| R-04 | The package shall support staggered blowdown sequencing to limit maximum simultaneous relief load. | DBM line 501 (FACT) |
| R-05 | Final blowdown sequencing shall be in accordance with `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy (location TBD). | DBM line 501 |
| R-06 | The LP flare element shall be implemented within an HP/Cryo + LP dual flare stack arrangement, shared between 03-25 and 04-25, with service split governed by the current 03-25/04-25 allocation (open interface item). | DBM lines 56, 497 (FACT) |
| R-07 | LP stack OD and overall height shall be confirmed by detailed design; current source basis carries LP stack OD as TBD. | DBM line 499 (FACT — TBD) |
| R-08 | Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. | DBM line 617 (FACT) |
| R-09 | Package buildings, self-framing enclosures, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins shall be coordinated with the civil, electrical, controls, and instrumentation sections of the DBM. | DBM line 619 (FACT) |
| R-10 | Isolation provisions shall support safe operation, maintenance, and turnaround, including isolation at skid edge where required. | DBM lines 605, 607 (FACT) |
| R-11 | For sour service portions, isolation philosophy shall consider double block/bleed or equivalent safeguards per operations/HAZOP. | DBM line 607 (FACT) |
| R-12 | Flare/stack foundation and anchorage shall be designed per the final geotechnical report, equipment loads, snow/wind/seismic, frost, vibration, and settlement criteria. | DBM line 700 (FACT) |
| R-13 | The associated LP flare stack blower shall be included in the package as a reference/interface element. | `PACKAGE_REGISTER.csv` row 59 RationaleNotes (FACT) |
| R-14 | The package shall produce a vendor design basis and datasheet set as anticipated artifacts. | `_CONTEXT.md` (FACT) |
| R-15 | Burner tip, pilot/ignition, and flame-monitoring details shall be defined by the vendor and consistent with the EPC Package Datasheet. | ASSUMPTION (typical vendor flare package practice); details TBD |
| R-16 | The package shall identify and align with all applicable interface types for PKG-086: Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports. | `PACKAGE_REGISTER.csv` row 59 InterfaceTypes (FACT) |

## Standards

| Standard / Document | Use | Provenance |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 39 | Governing package requirements section | `_CONTEXT.md`; `_REFERENCES.md` — location TBD (.docx not text-extracted in workspace) |
| `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy | Final blowdown sequencing | DBM line 501 — location TBD |
| `Bid Docs/Budgetary/brief.md` (Word Source Basis) | Source basis for package | `PACKAGE_REGISTER.csv` row 59 — location TBD |
| `Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf` | Budgetary pricing/delivery go-by only (not authority) | `PACKAGE_REGISTER.csv` row 59 — location TBD |
| Industry flare design codes (e.g., API 521 / API 537) | Governing flare disposal / equipment standards | ASSUMPTION: likely applicable; not enumerated in accessible sources |
| Pressure-vessel/piping codes (ASME B31.3, ASME Sec VIII) | Governing pressure equipment design | ASSUMPTION; not enumerated in accessible sources |
| Sour-service standards (NACE MR0175 / ISO 15156) | Governing sour-service materials where applicable | ASSUMPTION; DBM line 607 implies sour-service philosophy |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-01 | Cross-check vendor package documents against `DEL-086-01` SOW and `DEL-086-02` Package Datasheet. |
| R-02, R-06 | Process review of LP relief tie-ins (TEG regen, VRU, seal pots); confirm service split allocation with EPC Integrator. |
| R-03 | Mechanical/piping review of LP header tie-in against 508 mm/20 in carried basis. |
| R-04, R-05 | Blowdown study review against W242510-PRC-REP-000003-001 (when accessible). |
| R-07 | Detailed-design confirmation of LP stack OD and height; update Datasheet TBDs. |
| R-08, R-14 | Document review of vendor deliverables register against the DBM §6.X list. |
| R-09 | Multi-discipline interface review (civil, electrical, controls, I&C). |
| R-10, R-11 | HAZOP and operability review for isolation philosophy and sour service. |
| R-12 | Geotechnical and structural review of stack foundation and anchorage calculations. |
| R-13 | Verify LP flare stack blower is in vendor scope and properly tied to LP suction interface. |
| R-15 | Vendor datasheet and FAT review of burner tip and pilot system. |
| R-16 | Interface register cross-check against `INTERFACE_REGISTER.csv`. |

## Documentation

Required documentation set (anticipated artifacts):
- Vendor engineered physical equipment package (the physical package handover).
- Vendor package design basis and datasheet set.
- Vendor document register and submittals (turnover-relevant content is handled by `DEL-086-05`).
- Cause-and-effect inputs, utility load summary, relief/load data, field tie-in list, operating/design envelopes, sparing philosophy, materials and coating basis, maintenance access list, shipped-loose item list. (DBM line 617 — FACT)

(`_CONTEXT.md` Anticipated Artifacts; DBM line 617)
