# Specification — Vendor Engineered Equipment Package (DEL-099-04)

> Normative document. Requirements are derived from locally accessible source slices in the 03-25 Compressor Station and Liquids Hub DBM and the deliverable context. Where the EPC anchor deliverables (`DEL-099-01` Scope of Work, `DEL-099-02` Package Datasheet) would normally govern vendor scope but are not yet drafted, the requirement is labeled `ASSUMPTION` or `TBD` and surfaced in the `Guidance.md` Conflict Table. Non-trivial values cite `SourcePath` + `SectionRef` or are marked `location TBD`.

## Scope

**In scope** for this Vendor Engineered Equipment Package (vendor production unit):

- Engineering, design, fabrication / supply, and delivery of the physical equipment package for the 03-25 Truck Product Loading Unit, comprising three product condensate truck-loading stations and their associated loading pumps and skid-mounted ancillaries, developed against the EPC Scope of Work and Package Datasheet for `PKG-099`.
  - Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row for DEL-099-04; DBM `SEC-06` (line 414, 415, 526, 654).
- Vendor package design basis and datasheet set covering the supplied equipment.
  - Source: `_CONTEXT.md` Anticipated Artifacts.
- Engineering and EPC-integration interfaces required to integrate the vendor package into the 03-25 Liquids Hub (product condensate storage, VRU vapour-return interface, electrical and control interfaces, fire/gas detection placement coordination).
  - Source: DBM `SEC-06` (lines 414–417, 434–438); `SEC-08` (line 718, 768); `SEC-12` (lines 838, 862).

**Out of scope** for DEL-099-04 (carried by other deliverables / parties):

- EPC Scope of Work itself (`DEL-099-01`) and EPC Package Datasheet (`DEL-099-02`) — these are EPC Integrator deliverables that drive this vendor package.
- Construction installation, tie-in, and turnover workface execution (`DEL-099-03` Construction Work Package).
- Vendor document register / turnover submittals (`DEL-099-05`).
- EPC vendor package review and acceptance (`DEL-099-06`).
- LACT units and downstream sales custody transfer — third-party NRM scope (DBM SEC-02 line 22; SEC-06 line 417).
- Caustic truck-out and produced-water truck-out interfaces — separate equipment (DBM SEC-06 lines 402, 430).

## Requirements

Requirement IDs (`REQ-VEEP-*`) are local to this deliverable.

| ID | Requirement | Source / Basis | Label |
|---|---|---|---|
| REQ-VEEP-001 | The vendor shall supply three (3) product condensate truck-loading stations for the 03-25 Liquids Hub. | DBM SEC-06 (line 40, 414, 654) | FACT (source-grounded) |
| REQ-VEEP-002 | Each loading station shall be sized for 103 m³/h at 345 kPad differential pressure (product condensate service). | DBM SEC-06 (line 415) | FACT |
| REQ-VEEP-003 | The vendor shall supply one (1) electric-motor-driven condensate loading pump per loading station (three pumps total). | DBM SEC-06 (line 414, 526) | FACT |
| REQ-VEEP-004 | Loading-station suction shall be configured to draw from product condensate storage (4 × 3,800 bbl product condensate tanks within the 11-tank liquids-hub set). | DBM SEC-06 (line 406, 417) | FACT |
| REQ-VEEP-005 | The vendor package shall provide a vapour-return interface compatible with the 03-25 VRU header (suction-pressure controlled, free-draining/sloped to the flare KO interface as defined by detailed design); under SCA-002 the VRU discharge routes to 04-25 SOC suction. | DBM SEC-06 (line 436, 438) | FACT (interface boundary) |
| REQ-VEEP-006 | The vendor shall coordinate placement of LEL, H2S, methyl mercaptan, and fire detection devices for the loading area with the EPC Integrator. Final quantity, tag list, set points, voting logic, placement, and calibration remain detailed-design items. | DBM SEC-12 (line 838) | FACT framing; placement detail TBD |
| REQ-VEEP-007 | The vendor shall integrate loading-station shutdown with the facility BPCS / ESD logic and package PLC, with replicated values/alarms as required. Final trip lists, cause-and-effect actions, and reset responsibilities are detailed-design deliverables. | DBM SEC-12 (line 862) | FACT framing; cause-and-effect TBD |
| REQ-VEEP-008 | Electrical design (motors, cabling, grounding, area classification) shall comply with the Canadian Electrical Code (CEC), project electrical specifications, and project voltage / MCC / grounding basis. | DBM SEC-08 (line 768, 893) | FACT (standards anchor) |
| REQ-VEEP-009 | The package shall be suitable for the 03-25 site environmental envelope (LSD 03-25-80-15 W6M, BC; elevation 673 m AMSL). Specific ambient temperature, wind, snow, and seismic design values: `TBD`. | DBM SEC-02 (line 85); other site design values not in accessible slice | ASSUMPTION + TBD |
| REQ-VEEP-010 | The product handled is stabilized C5+ condensate downstream of the non-regenerative caustic mercaptan treating unit. The vendor package shall be material-compatible with stabilized condensate service; trace-residual product mercaptan specification: `location TBD`. | DBM SEC-06 (line 376, 389) | FACT + TBD on product spec |
| REQ-VEEP-011 | Overfill protection on tanker loading (e.g., API 2350 or equivalent owner-specified scheme): `TBD` (not stated in accessible DBM slice; expected to be carried by EPC Package Datasheet `DEL-099-02`). | TBD | TBD |
| REQ-VEEP-012 | Loading-arm configuration, metering, ticket printing, and vapour-recovery hose / dry-disconnect arrangement: `TBD` (not stated in accessible DBM slice). | TBD | TBD |
| REQ-VEEP-013 | Truck grounding / bonding scheme for loading apron: `TBD` (CEC general requirement applies per REQ-VEEP-008; specific scheme not in accessible source). | TBD | TBD |
| REQ-VEEP-014 | Hazardous-area classification of loading apron: `TBD` (CEC general requirement applies; specific zone classification not in accessible source). | TBD | TBD |
| REQ-VEEP-015 | The vendor shall produce a vendor package design basis and datasheet set (per `_CONTEXT.md` Anticipated Artifacts), traceable to the requirements in this Specification. | `_CONTEXT.md` | FACT |
| REQ-VEEP-016 | The vendor package shall integrate with the EPC Scope of Work (`DEL-099-01`) and EPC Package Datasheet (`DEL-099-02`) once those deliverables are issued by the EPC Integrator; current state of both is `OPEN`. | Sibling deliverable `_STATUS.md` files; decomposition row | ASSUMPTION (no issued upstream) |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical, grounding, area classification | Cited generically in DBM SEC-08 (line 893); clause-level location TBD |
| Project electrical specifications | Voltage / MCC / grounding basis | DBM SEC-08 (line 768, 893); specification document set not in accessible source — `location TBD` |
| API 650 (Modified) | Atmospheric tankage (governs storage tanks upstream of loading; vendor package interfaces with these) | DBM SEC-06 (line 421); applicable to upstream tanks, not loading skid directly |
| API 2350 (overfill protection for storage tanks transferring petroleum) | Likely applicable to tanker loading overfill protection | `ASSUMPTION: likely applicable`; not cited in accessible DBM slice |
| HAZOP / safety-study products | Cause-and-effect, ESD trip levels, detector voting | Carried as detailed-design items (DBM SEC-12 line 862) |
| External `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy | ESD / blowdown sequencing alignment | DBM SEC-07 (line 501); document not in accessible source — `location TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-VEEP-001 | Inspection of vendor equipment list / GA drawings against count of 3 stations. |
| REQ-VEEP-002 | Hydraulic calculation review + factory performance test of loading pumps at duty point (103 m³/h, 345 kPad). |
| REQ-VEEP-003 | Visual inspection / motor nameplate verification. |
| REQ-VEEP-004 | P&ID review against tank register and product-condensate tank tag set. |
| REQ-VEEP-005 | P&ID and interface drawing review; functional walk-down of vapour-return tie-in to VRU suction header. |
| REQ-VEEP-006 | Detector placement walk-down against EPC layout; F&G cause-and-effect matrix review. |
| REQ-VEEP-007 | ESD/BPCS interface test; package PLC FAT and integration SAT with cause-and-effect matrix. |
| REQ-VEEP-008 | Electrical drawing/spec review; field inspection of grounding and area-classification labelling. |
| REQ-VEEP-009 | Vendor design conditions vs. site basis cross-check (TBD values to be resolved against site spec). |
| REQ-VEEP-010 | Material certificates; service-compatibility statement. |
| REQ-VEEP-011 to REQ-VEEP-014 | Pending: cannot be verified until source TBDs are closed by EPC Package Datasheet or owner ruling. |
| REQ-VEEP-015 | Document inspection: vendor datasheet/design basis set delivered and traced to this Spec. |
| REQ-VEEP-016 | Documented alignment review against `DEL-099-01` and `DEL-099-02` once issued. |

## Documentation

The vendor shall produce, at minimum (from `_CONTEXT.md` Anticipated Artifacts and ordinary vendor package conventions — convention items labeled `ASSUMPTION`):

- Vendor engineered physical equipment package (the equipment itself) — `FACT`.
- Vendor package design basis and datasheet set — `FACT`.
- Equipment GA drawings, P&IDs, electrical schematics, control narratives — `ASSUMPTION` (conventional; not explicitly enumerated in accessible source).
- Performance test records, FAT/SAT records — `ASSUMPTION` (conventional).
- Material certificates and code stamps as applicable — `ASSUMPTION` (conventional).

The vendor document register / turnover record is carried in `DEL-099-05` (separate deliverable).
