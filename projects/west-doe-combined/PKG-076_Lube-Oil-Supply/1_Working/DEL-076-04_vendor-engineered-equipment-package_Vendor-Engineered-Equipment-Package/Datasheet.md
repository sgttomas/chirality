# Datasheet — Vendor Engineered Equipment Package (DEL-076-04)

> Pass 1/Pass 2 draft. Source-grounded where the locally accessible Deepcut Design Basis Memorandum (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-08 "Lube Oil Storage and Pump Basis") supports specific values. Other values marked `TBD` or `ASSUMPTION` per the four-documents skill.
>
> NOTE on source availability: The decomposition row cites `26020-Package_Requirements.docx package heading 30`. The .docx is present in `_Sources/` but is a binary file and is NOT locally accessible as parseable text. Anchoring is done against the Deepcut DBM (SEC-08 and the Packages register in SEC-16), which is the locally accessible authoritative basis for the 04-25 Lube Oil Supply utility package (PKG-076). Items that would have been confirmed by the package-requirements heading are left as `location TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-076-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-076` (Lube Oil Supply) | `_CONTEXT.md` |
| Facility | 04-25 Deep Cut Gas Plant (West Doe Deepcut expansion) | DBM-Deepcut SEC-01 (Facility Identity) |
| Workbook row | Packages row 70 | `_CONTEXT.md` / DELIVERABLE_REGISTER row 387 |
| Discipline | Mechanical (vendor-led, EPC integration review) | `_CONTEXT.md` |
| Production-unit type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible party | Package Vendor (engineering/design/equipment); EPC Integrator integration review | `_CONTEXT.md` |
| Covered SOW items | SOW-0135, SOW-0136, SOW-0137, SOW-0138 | `_CONTEXT.md` |
| Supported objectives | OBJ-001, OBJ-004 through OBJ-010 (ASSUMPTION — package-grouping heuristic) | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP |

## Package Function (Attributes)

| Attribute | Value | Source |
|---|---|---|
| Unit purpose | Provide heated bulk storage and transfer of compressor cylinder lube oil and compressor crank-case lube oil to compressor frame day tanks at the 04-25 facility | DBM SEC-08 §"Lube Oil Storage and Pump Basis" (L2059–L2071); SEC-08 §"Utility System Summary" (L1835) |
| Service category | Plant-support utility (compressor lubrication supply) | DBM SEC-08 L1822, L1835 |
| Service basis | Heated compressor-cylinder and crank-case lube oil storage with transfer pumps to frame day tanks | DBM SEC-08 L1835 |
| Principal users | SOC inlet/sales compressor packages; stabilizer overheads compressor; sales gas booster compressor; acid gas compressor (lube-oil consuming reciprocating frames per SEC-05 L828) | DBM SEC-08 L1835; SEC-05 L828 |
| Multi-oil provision (ASSUMPTION) | Multiple compressor cylinder oils may be required (sulphur content, rich gas, H2S); manufacturer-recommended cylinder oil types remain TBC for inlet, sales, stabilizer overheads, acid gas, and sales gas booster reciprocating services | DBM SEC-08 L2072 |
| Plant equipment line-item (count) | "Lube Oil Supply Pumps" line item, 2 equipment items | DBM SEC-16 Packages register row 51 (L2602); also Packages summary L2543 |
| Tag list (line-item) | P-9240-1 (cylinder lube oil transfer pump); P-9250-1 (crank-case lube oil transfer pump) | DBM SEC-16 Packages register row 51 (L2602); confirmed in SEC-08 L2068, L2070 |

## Design / Operating Conditions

| Parameter | Value | Source |
|---|---|---|
| Site design ambient | −40 °C to +35 °C | DBM SEC-02 L198 |
| Plant elevation | 673 m AMSL | DBM SEC-02 L195 |
| Service temperature | Heated storage (specific target temperature TBC); heating provided to maintain pumpability and meet vendor-required supply temperature to compressor frame day tanks | DBM SEC-08 L1835, L2059; specific heated-tank temperatures **TBD** |
| Compressor cylinder lube oil tank design specific gravity | 1.00 (TBC) | DBM SEC-08 L2065 |
| Compressor crank-case lube oil tank design specific gravity | 1.00 (TBC) | DBM SEC-08 L2066 |
| Cylinder lube oil storage volume | 400 bbl heated tank in the storage tank area | DBM SEC-08 L2067 |
| Crank-case lube oil storage volume | 200 bbl heated tank in the storage tank area | DBM SEC-08 L2069 |
| Pump duty | Fill compressor frame day tanks "as needed" (intermittent transfer service, not continuous circulation) | DBM SEC-08 L2068, L2070 |
| Pump flow / head | TBD (vendor sizing against frame day-tank fill cycle and run-distance) | not stated in DBM |
| Pump type | TBD (typical: positive-displacement gear or rotary for heated oil transfer) — `ASSUMPTION`; vendor selects against viscosity, suction conditions, and heat tracing | not stated in DBM |
| Cylinder oil grade(s) | TBC — manufacturer-recommended per service (inlet, sales, stabilizer overheads, acid gas, sales-gas booster) | DBM SEC-08 L2072 |
| Crank-case oil grade(s) | TBC — per compressor manufacturer | ASSUMPTION; DBM SEC-08 L2072 (analog) |
| Additional storage requirements | TBD | DBM SEC-08 L2072 |

## Construction / Equipment Composition

The deliverable is the physical vendor-engineered Lube Oil Supply utility package serving the 04-25 facility. At minimum it consists of the items below. Source: DBM SEC-08 §"Lube Oil Storage and Pump Basis" (L2059–L2072), the SEC-16 Packages register (row 51, L2602), and SEC-08 utility-summary line (L1835).

| Function | Configuration | Source |
|---|---|---|
| Compressor cylinder lube oil storage tank | 400 bbl heated tank, storage tank area; tank design specific gravity 1.00 (TBC); tank tag implied as TK-9240-x — **TBD** (no tank tag in DBM); insulation, heat tracing, secondary containment per site standard — **TBD** | DBM SEC-08 L2065, L2067 |
| Compressor cylinder lube oil transfer pump | P-9240-1; fills compressor frame day tanks as needed | DBM SEC-08 L2068; SEC-16 L2602 |
| Compressor crank-case lube oil storage tank | 200 bbl heated tank, storage tank area; tank design specific gravity 1.00 (TBC); tank tag implied as TK-9250-x — **TBD** (no tank tag in DBM); insulation, heat tracing, secondary containment per site standard — **TBD** | DBM SEC-08 L2066, L2069 |
| Compressor crank-case lube oil transfer pump | P-9250-1; fills compressor frame day tanks as needed | DBM SEC-08 L2070; SEC-16 L2602 |
| Heating provisions | Heated storage explicitly required; heating medium (electric trace or hot-medium coil) — **TBD**; control basis — **TBD** | DBM SEC-08 L1835, L2059 |
| Pump spares / parallel arrangement | Not specified in DBM (basis lists 1 pump per service) — vendor proposal to add spare pump(s) is **TBD** (single-pump basis carries availability risk for compressor lubrication) | ASSUMPTION; DBM SEC-08 L2068, L2070 |
| Filtration / strainers | Not specified in DBM — vendor scope; **TBD** | ASSUMPTION |
| Distribution piping to frame day tanks | Heat-traced and insulated piping from storage tank area to compressor frame day tanks — **TBD** routing per facility layout | ASSUMPTION; DBM SEC-08 L1835 (interfaces to "Compressor packages and storage tank area") |
| Containment / spill control | Per site standard for hydrocarbon storage and heated oil — **TBD** | ASSUMPTION |
| Area classification | General Purpose (lube oil is not a process hydrocarbon stream); fired/heated provisions to be reviewed against site classification — **TBD** | ASSUMPTION |

## References

- `_REFERENCES.md`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-01, SEC-02, SEC-05 (compressor lube-oil requirements driving demand), SEC-08 (Lube Oil Storage and Pump Basis), SEC-16 (Packages register row 51)
- `26020-Package_Requirements.docx` package heading 30 — cited by decomposition; **location TBD** (binary not parseable in this environment)
- GATE-07 PROJECT_DECOMP snapshot — DELIVERABLE_REGISTER row 387 for DEL-076-04; PACKAGE_REGISTER row for PKG-076

## Open / TBD Items

- Heated tank service temperature for both cylinder oil and crank-case oil — **TBD**.
- Tank tags (TK-) for cylinder and crank-case storage — not present in DBM; **TBD**.
- Transfer pump flow, head, type, and material — **TBD** (vendor sizing).
- Whether transfer pumps are 1 × 100% (current basis line items) or include spares — **TBD**; recommend vendor proposal with availability rationale.
- Cylinder oil grade(s) per compressor service (inlet, sales, stabilizer overheads, acid gas, sales-gas booster) — **TBC** by compressor manufacturers (DBM SEC-08 L2072).
- Additional storage requirements (e.g., used-oil and waste-oil storage) — **TBD** (DBM SEC-08 L2072).
- Heating method (electric trace vs. hot-oil coil) and heat-medium tie-in — **TBD**.
- Distribution piping routing and heat-tracing scope split between PKG-076 and compressor packages — **TBD**.
- Confirmation against `26020-Package_Requirements.docx` heading 30 — **TBD** (source not locally parseable).
- Spill containment, secondary containment, and bunding scope — **TBD** against site civil standard.
