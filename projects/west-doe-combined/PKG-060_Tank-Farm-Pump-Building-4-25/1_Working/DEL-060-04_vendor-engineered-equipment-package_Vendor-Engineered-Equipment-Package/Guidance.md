# Guidance — DEL-060-04 Vendor Engineered Equipment Package

## Purpose

This deliverable is the Package Vendor's production unit for the PKG-060 Tank Farm Pump Building 4-25. It carries the engineering, design, fabrication/supply, and physical equipment package developed from the EPC Integrator's anchoring deliverables (DEL-060-01 Scope of Work, DEL-060-02 Package Datasheet). It is the central artifact that the EPC Integrator subsequently reviews and accepts in DEL-060-06. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` rows 474-479.

## Principles

- **Source authority follows the package datasheet.** The EPC Integrator's Package Datasheet (DEL-060-02) is the authoritative technical handoff document. The vendor design basis must trace to that datasheet plus the underlying DBM source slice.
- **Module orientation.** The package is shop-fabricated as Module 920-1 "Tank Farm Pump Module" (DBM line 2817). Vendor engineering shall preserve the shop-built modular character of the deliverable.
- **Sour, caustic, and cold-startup duty.** The tag mix (sour water, caustic, condensate, produced water) and the -40 deg C startup envelope (DBM line 1679) drive material selection and motor sizing. Caustic-compatibility rules (DBM line 1566) constrain materials in caustic service.
- **Tank-farm coordination.** The pump module exists to service tank-farm tanks owned by separate line items (API 650 condensate, caustic, DSO, sour water, water tanks — DBM lines 2623-2628). Vendor must coordinate suction NPSH and tie-in elevations because condensate tanks are not elevated to accommodate pump NPSH (DBM line 1677).

## Considerations

- **NPSH risk.** DBM line 1677 explicitly notes that if vendor NPSHR exceeds 0.75 m, unacceptable usable tank volume loss results. Booster pumps may be required; this is a fundamental design risk for vendor selection.
- **Simultaneous-pump operation.** Both condensate transfer pumps must be capable of running simultaneously for upset pump-down (DBM line 1675). Vendor controls and suction header sizing must support this.
- **Sparing philosophy.** Multiple services use 2 x 150% (condensate transfer), 2 x 100% (sour water, process water, fresh caustic), and 1 x 100% (product recycle, condensate skim) configurations. Sparing assumptions for water transfer pumps remain unresolved (see Conflict Table).
- **Interface with VRU.** Condensate tanks tie into the VRU suction header and require blanket gas to prevent winter vacuum (DBM line 1663). Vendor scope likely excludes VRU equipment but must support these tank interfaces.
- **Trade-off: shop module vs field-erected.** Source line 2817 designates "Shop" fabrication. A field-erected alternative would increase weather risk and reduce QA control but might reduce shipping constraints; not a current basis.

## Trade-offs

- **NPSH margin vs tank elevation.** Source-stated trade-off: tanks are not elevated to preserve usable volume, transferring the NPSH burden to vendor pump selection (DBM line 1677). Vendor may need higher-cost low-NPSH pumps or accept a booster configuration.
- **Caustic compatibility vs cost.** Polymer or caustic-compatible materials are required in caustic service (DBM line 1566); these typically cost more than carbon steel but eliminate embrittlement risk.
- **Startup density vs steady-state efficiency.** Motors sized for -40 deg C JT-mode startup density (DBM line 1679) will be over-sized for steady-state duty, with associated efficiency penalty.

## Examples

- Condensate transfer service (P-9210-1/P-9220-1): 2 x 150%, simultaneous capable, 350 kPad to liquids hub. Source: DBM line 1673.
- Module precedent: NGL Booster and Transfer Pumps Building uses "Pumps (API 610, multi-stage can)" notation (DBM line 2609). ASSUMPTION: similar API 610 application to the condensate transfer multi-stage horizontal pumps in this package.
- Building finish precedent: "Safety Green" trim, galvanized walls, bright white interior across shop buildings (DBM lines 2824-2826).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Water Transfer Pump quantity: x4 vs x2 | DBM line 2555 (line-item summary: WATER TRANSFER PUMP (x4)) | DBM line 2619 (detailed package table: count 2, tags P-9290-1, P-9293-1) | Datasheet attributes; Spec REQ-10 | PROPOSAL: detailed package table (x2) is authoritative; "(x4)" in the summary may refer to total impeller stages or be a typo. Source line 2619 is the package roster row. | TBD |
| CONF-02 | Package name mismatch: "Tank Farm Pump Building 2" (DBM SEC-10) vs "Tank Farm Pump Building 4-25" (decomposition deliverable name) | DBM lines 2555, 2618-2622 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 477 | All four documents | PROPOSAL: same package; DBM "2" suffix denotes the 4-25 facility instance vs the 3-25 facility instance. | TBD |
| CONF-03 | VRU 2 package summary inclusion / total equipment | DBM line 2564 (Vapour Recovery Unit 2 absence from package roster; status TBD) | DBM lines 2631-2632 (line-item basis includes VRU 2 - Train 1/2) | Spec scope (out-of-scope confirmation) | PROPOSAL: VRU 2 is NOT in PKG-060 vendor scope; tracked as DBM-level open item only. | TBD |
| CONF-04 | "Inlet Condensate Heater" equipment tags TBD | DBM lines 2584-2585 (tags TBD) | n/a | Datasheet attributes (interfacing) | PROPOSAL: not in PKG-060 vendor scope; flagged as interface dependency only. | TBD |

## Notes on Assumption Labels

- Objective associations (OBJ-001, OBJ-003 through OBJ-010) are PACKAGE_HEURISTIC ASSUMPTIONs per the brief's `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`. Source: `_CONTEXT.md`.
- API 610 applicability to specific pump services is an ASSUMPTION based on the DBM precedent for related pump packages (DBM line 2609). Source confirmation TBD.
