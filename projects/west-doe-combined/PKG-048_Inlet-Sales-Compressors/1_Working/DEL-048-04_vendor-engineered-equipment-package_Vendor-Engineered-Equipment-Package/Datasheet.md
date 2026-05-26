# Datasheet: DEL-048-04 — Vendor Engineered Equipment Package

> Descriptive data sheet for the Inlet / Sales Compressors vendor-engineered equipment package. Values are extracted from the Gate-07 PROJECT_DECOMP snapshot (SCOPE_LEDGER rows SOW-0115..SOW-0118 and PACKAGE_REGISTER row PKG-048). Underlying source documents (26020-Package_Requirements.docx) exist in `_Sources/` but were not text-extracted at PREPARATION; values relying on text not surfaced in the decomposition snapshot are marked TBD.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-048-04_vendor-engineered-equipment-package | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | PKG-048 Inlet / Sales Compressors | `_CONTEXT.md`; PACKAGE_REGISTER PKG-048 |
| Workbook Row | 65 | PACKAGE_REGISTER PKG-048 |
| Discipline | Mechanical | PACKAGE_REGISTER PKG-048 |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| WBS | 01 | PACKAGE_REGISTER PKG-048 |
| Package Tag (project) | 26020-01-PT-12-003 - Inlet / Sales Compressors | PACKAGE_REGISTER PKG-048 |
| Responsible Party | Package Vendor (engineering/design/equipment); EPC Integrator (facility integration) | PACKAGE_REGISTER PKG-048 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Equipment count | 5 (Five) inlet/sales gas compressors | SOW-0117 |
| Compressor make/model | Ariel KBC/6 | SOW-0117 |
| Compressor type | 3-stage reciprocating, DOL driver with soft-start | SOW-0117 |
| Service split | Inlet gas single-stage; Sales gas double-stage | SOW-0116 |
| Sizing margin | Each compressor sized for 120% | SOW-0116 |
| Driver | 8-pole induction motor | SOW-0117, SOW-0118 |
| Driver rating (per unit, basic scope) | 5,000 kW (6,700 HP); ~10% excess at design | SOW-0117 |
| Driver rating (per unit, design conditions) | 5,220 kW (7,000 HP); ~10% excess at design | SOW-0118 |
| Driver electrical | 6600 V / 3-phase / 60 Hz | SOW-0117 |
| Driver speed | 891 RPM | SOW-0117 |
| Driver frame (preferred) | KBZ Frame, 6,700 hp, preferred WEG motor | SOW-0118 |
| Driver enclosure | TEFC or WPII, non-sparking bidirectional cooling fan; NEMA MG 1 | SOW-0118 |
| Total connected load (5 units) | 26,100 kW (35,000 HP) | SOW-0118 |
| Suction scrubbers | Two-phase, upstream of each stage; vertical flow vane-style demisters (horizontal and vertical acceptable) | SOW-0117 |
| Demister K factor | <= 0.5 Imperial plus de-ration for pressure | SOW-0117 |
| Liquid density basis | 0.61 SG | SOW-0117 |
| Cooler | One common air cooler frame per package serving both services | SOW-0117 |
| Cooler control | Automated louver control via pneumatic temperature control on each process bundle | SOW-0117 |
| Turndown | None | SOW-0118 |

## Conditions (Operating / Design)

| Parameter | Inlet Service | Sales Service | Source |
|---|---|---|---|
| Suction pressure (operating) | 4,309 kPag (625 psig) | 3,034 kPag (440 psig) | SOW-0118 |
| Discharge pressure (operating) | 7,791 kPag (1,130 psig) | 10,343 kPag (1,500 psig) | SOW-0118 |
| Design capacity (each) | 1,766 e3m3/d (62.4 MMSCFD) | 1,630 e3m3/d (57.6 MMSCFD) | SOW-0118 |
| Process compositions (gas) | TBD | TBD | not surfaced in decomposition snapshot |
| Site/ambient design conditions | TBD | TBD | not surfaced in decomposition snapshot |

## Construction

| Item | Value | Source |
|---|---|---|
| Mounting | By others (mounting platform and stairs by others) | SOW-0118 |
| Tie-in piping | By others | SOW-0118 |
| Electrical connections | By others | SOW-0118 |
| Installation on piles | By others | SOW-0118 |
| Shipping to site | By others | SOW-0118 |
| Skid / package fabrication | Package Vendor scope (engineering, design, fabrication/supply, physical equipment package) | `_CONTEXT.md`; PACKAGE_REGISTER PKG-048 |
| Vendor documentation set | Package vendor design basis and datasheet set | `_CONTEXT.md` (Anticipated Artifacts) |
| Materials of construction | TBD | not surfaced in decomposition snapshot |
| Coatings / insulation | TBD | not surfaced in decomposition snapshot |
| Area classification | TBD | not surfaced in decomposition snapshot |

## Applicable Interfaces (package-level)

ASSUMPTION (PACKAGE_HEURISTIC): the package-level interface list applies to this vendor-engineered equipment package and must be honored by the vendor-engineered design.

- Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports
- Source: PACKAGE_REGISTER PKG-048 (Applicable interface types)

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row `DEL-048-04`
- GATE-07 PROJECT_DECOMP snapshot: `PACKAGE_REGISTER.csv` row `PKG-048`
- GATE-07 PROJECT_DECOMP snapshot: `SCOPE_LEDGER.csv` rows `SOW-0115`, `SOW-0116`, `SOW-0117`, `SOW-0118`
- Upstream source (not text-extracted at PREPARATION; location TBD for clause-level citations): `26020-Package_Requirements.docx` package heading 3; `Bid Docs/Budgetary/RFQ/Bid Docs/26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md`
