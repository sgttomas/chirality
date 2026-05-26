# Specification — DEL-049-01 Scope of Work (Sales Gas Booster Compressor)

> Normative EPC Integrator Scope of Work for PKG-049. Requirements are source-grounded where locally accessible DBM material supports them.
> Pass 1/Pass 2 draft. Unsupported claims are marked `TBD`; conservative inferences are labeled `ASSUMPTION`.

## Scope

This Scope of Work covers EPC Integrator responsibilities for the PKG-049 Sales Gas Booster Compressor package at the 04-25 Deep Cut Gas Plant (West Doe Deepcut expansion). The scope includes:

- definition of tagged equipment and package identity for the single sweet-gas booster compression package;
- package function, source-of-design basis, operating envelope, and battery-limit boundaries;
- the whole-facility integration narrative tying the booster into the upstream sales compressor units, downstream HP sales gas coalescer/splitter, TC sales pipeline interface, VRU suction header, and shared utilities;
- the responsibility assignment record between EPC Integrator and the Package Vendor for engineering, supply, documentation, and acceptance.

Source: `_CONTEXT.md` Scope; DBM-Deepcut §SEC-05 Compression Configuration and Sales Gas Booster Compressor Basis.

Excluded from this deliverable: the vendor-engineered package itself (DEL-049-04), vendor documentation register (DEL-049-05), construction work package (DEL-049-03), vendor package acceptance evidence (DEL-049-06), and the EPC Package Datasheet (DEL-049-02). Source: GATE-07 DELIVERABLE_REGISTER rows for PKG-049.

## Requirements

### R-049-01-01 — Package configuration
The package shall consist of one (1) sweet-gas reciprocating compressor package configured as 1 × 100%, with no installed spare package and no spare compressor equipment or instrumentation. Source: DBM-Deepcut §SEC-05 Compression Configuration; Sales Gas Booster Design Conditions table.

### R-049-01-02 — Compression duty
The package shall compress sweet sales gas in a single stage from a suction pressure of 6,137 kPag (890 psig) to a discharge pressure of 12,866 kPag (1,866 psig). Low suction pressure and normal discharge pressure remain TBC. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions.

### R-049-01-03 — Design capacity
The package shall provide a design capacity of 3,962 e3m3/d (140 MMSCFD) in both J-T and expander operating modes of the upstream cryogenic unit. High and excess capacity values are TBC. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Compressor Basis and Design Conditions table.

### R-049-01-04 — Frame and driver
The compressor frame shall be an Ariel KBK/4 with all cylinders dedicated to the single booster compression stage (larger high-efficiency cylinder on a two-throw design to be evaluated during detailed engineering due to low compression ratio). The driver shall be an electric induction motor rated 6,700 hp, 4,000 V, 3-phase, 60 Hz, with NEMA MG 1 testing/labeling, Class F insulation with Class B temperature-rise limit, non-sparking bidirectional cooling fans, and TEFC or WPII enclosure. Starting shall be DOL with soft-start; no driver speed turndown is provided. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Compressor Basis.

### R-049-01-05 — Pressure containment
Minimum MAWP for both suction and discharge sides shall be 13,100 kPag (1,900 psig). Design temperatures shall be 149 °F (300 °F alternate) for suction and 177 °F (350 °F alternate) for discharge. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions.

### R-049-01-06 — Inlet gas quality
Inlet sweet sales gas shall be delivered with water content < 0.1 ppmv, consistent with upstream molecular-sieve dehydration. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions.

### R-049-01-07 — Suction scrubbing
A two-phase suction scrubber shall be provided upstream of compression. Final need shall be re-evaluated in detailed engineering due to the very low inlet-gas dewpoint. Assumed inlet liquid density is 0.61 SG. Demister internals shall be horizontal double-hook vane-style, sized per API-11P or vendor vane-style demister sizing. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Compressor Basis.

### R-049-01-08 — Suction pressure control
The suction pressure control valve shall be a full-port automated ball valve sized for 5 psid differential pressure with upstream manual isolation. Fail position shall be closed. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-09 — Aftercooler
The booster aftercooler shall be a horizontal airflow, single-fan, on-module air cooler with automated pneumatic louver control. Cooler outlet temperatures shall be 35.0 °C (winter) and 43.3 °C (summer). Simulated first-stage aftercooler gas-section pressure drop is 69.0 kPad; design pressure drop is TBC. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-10 — Blowdown and start-up
A single blowdown valve with fail-closed action shall be provided. The package shall be capable of starting from equalization pressure, and equalization pressure shall not exceed system MAWP. Where an additional automated bypass valve is required, the alternate design shall depressure back into the sales compressor discharge header. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-11 — Automation
Isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, and shutdown sequences shall be automated. An electric circulating lube oil heater shall be included for quick start. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-12 — Sweet gas purge interface
Manual sweet-gas purge is not part of the booster package and remains an external-responsibility item. The EPC Integrator shall define the interface, isolation, and source for this external purge in the integration documents. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-13 — Vent and drain recovery
Packing drains and vents shall be collected to a common seal pot. Seal-pot vapour shall be routed to the VRU suction header. Liquids shall be removed by local truck-out connection. Distance-piece sweep purge shall be provided to prevent backflow from the VRU header. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-14 — Recycle valve
A recycle control valve sized for 100% capacity at minimum pipeline operating pressure and high suction pressure (covering initial start-up) shall be provided, with fail-closed action (TBC) and a single full-port manual isolation valve on the outlet. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-15 — Clearance pockets
Automated continuously variable or fixed-volume clearance pockets shall be evaluated against standard manual variable volume clearance pockets to optimize power consumption and reduce recycle at higher suction pressures. Final clearance-volume selection is TBD. Source: DBM-Deepcut §SEC-05 booster description.

### R-049-01-16 — Battery-limit interfaces
The package shall integrate with the following plant systems at defined battery limits:

- Suction tie-in from combined discharge of the two sales compressor units;
- Discharge tie-in to the downstream high-pressure sales gas coalescer and splitter feeding the TC sales pipeline;
- Vent tie-in to the VRU suction header (seal pot route);
- Electrical tie-in for 4,000 V, 3-phase, 60 Hz motor service and starting equipment;
- Control system tie-in for automated sequences and pressure/temperature instrumentation.

Exact tag numbers, line sizes, and isolation point locations are TBD pending detailed engineering. Source: DBM-Deepcut §SEC-05 booster description; §SEC-02 Plant Overview; §SEC-05 Compression Configuration. ASSUMPTION: battery-limit list is the conservative integration set implied by the source narrative.

## Standards

| Standard | Use | Source / location |
|---|---|---|
| NEMA MG 1 | Motor testing/labeling, insulation class, enclosure | DBM-Deepcut §SEC-05 booster description |
| API-11P (or vendor vane-style sizing) | Suction scrubber demister sizing | DBM-Deepcut §SEC-05 booster description |
| API 618 (reciprocating compressors for petroleum, chemical, and gas industry services) | Reciprocating compressor design — ASSUMPTION: applicable per common industry practice; location TBD | not stated explicitly in accessible source |
| ASME B31.3 / ASME Section VIII | Process piping / pressure vessel design — ASSUMPTION: applicable; location TBD | not stated explicitly in accessible source |
| CSA / provincial AB-BC pressure regulation | Provincial pressure equipment registration — ASSUMPTION based on BC site location; location TBD | site location per DBM-Comp_and_Liquids §SEC-01 (Dawson Creek, BC) |

## Verification

| Requirement | Verification approach |
|---|---|
| R-049-01-01 | Vendor configuration drawings and equipment list review; absence of spare package and spare instrumentation confirmed in vendor scope (DEL-049-04) and acceptance check (DEL-049-06). |
| R-049-01-02, R-049-01-03 | Vendor process datasheet / performance curves review; simulation/sizing verification at design and TBC operating points. |
| R-049-01-04 | Vendor mechanical datasheet review for frame/driver selection; motor data sheet and NEMA compliance certificate review. |
| R-049-01-05 | MAWP and design-temperature confirmation on vendor mechanical datasheet, U-1A forms, and pressure-test records. |
| R-049-01-06 | Verification through upstream dehydration design (cross-package interface) and inlet sample acceptance criteria. |
| R-049-01-07 | Demister sizing calculation review per API-11P or vendor method; scrubber datasheet review; detailed-engineering decision record on re-evaluation outcome. |
| R-049-01-08 to R-049-01-15 | Vendor valve schedule, P&ID, sequence-of-operations, lube-oil schematic, and recycle/clearance-pocket sizing calculation review. |
| R-049-01-16 | Interface drawings, plot/3D model coordination reviews, IFC P&IDs, and tie-in punch list at construction handoff (DEL-049-03 / DEL-049-06). |
| Standards | Compliance certificates and code stamping records on vendor submittals; resolution of TBD standard applicability before vendor purchase order. |

## Documentation

The EPC Integrator scope shall produce or coordinate the following documentation set (per `_CONTEXT.md` Anticipated Artifacts and GATE-07 sibling deliverables):

- Package scope of work (this deliverable)
- Tagged equipment and package identity list (this deliverable; tags TBD)
- Package function and integration narrative (this deliverable)
- Responsibility assignment record (this deliverable)
- EPC Package Datasheet (DEL-049-02)
- Construction Work Package, including installation/tie-in workface plan and turnover checklist (DEL-049-03)
- Vendor Engineered Equipment Package (DEL-049-04)
- Vendor Document Turnover Package, including vendor document register, submittals, and turnover records (DEL-049-05)
- EPC Vendor Package Review and Acceptance evidence (DEL-049-06)

Source: GATE-07 DELIVERABLE_REGISTER rows DEL-049-01..06.
