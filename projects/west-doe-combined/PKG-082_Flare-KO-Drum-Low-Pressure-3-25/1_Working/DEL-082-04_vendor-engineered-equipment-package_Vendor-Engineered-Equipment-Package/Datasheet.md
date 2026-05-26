# Datasheet: DEL-082-04 — Vendor Engineered Equipment Package (Flare KO Drum, Low Pressure, 3-25)

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-082-04_vendor-engineered-equipment-package |
| Deliverable Name | Vendor Engineered Equipment Package |
| Parent Package | PKG-082 — Flare KO Drum (Low Pressure) 3-25 |
| Workbook Row | 56 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Primary Tag (subject equipment) | LP flare KO drum V-3900-2 (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Flare and Blowdown, line 499) |
| Associated Transfer Pump | P-3900-2, 1 x 100 percent, slop service (Source: DBM §Sparing Philosophy, line 584; §Flare and Blowdown, line 499) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | LP flare knock-out — receives TEG regeneration, VRU, and compressor seal-pot LP relief | DBM line 499 |
| Tag | V-3900-2 | DBM line 499 |
| Sparing | 1 x 100 percent transfer pump (P-3900-2) | DBM line 584 |
| Liquid disposition | Pump to slop | DBM line 499 |
| LP relief header size | 508 mm / 20 inch (header basis; drum nozzle sizing TBD by vendor) | DBM line 499 |
| LP flare stack OD | TBD in source basis (drum is upstream of stack; stack OD does not size the drum) | DBM line 499 (location TBD for resolved value) |
| Design pressure | TBD — to be set by vendor against LP relief load case | TBD |
| Design temperature | TBD — to be set by vendor against LP relief load case | TBD |
| Material of construction | TBD — sour-service review required (ASSUMPTION: facility is sour per DBM §Drains and isolation guidance, line 607) | TBD |
| Orientation / geometry | TBD — vendor selection (typical horizontal KO drum) | TBD |
| Internals (demister, vortex breaker, baffle) | TBD — vendor design per relief load and droplet specification | TBD |
| Nozzle schedule | TBD — inlet (LP relief header), vapor outlet to flare, liquid outlet to P-3900-2, drains, instrument and PSV connections | TBD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Upstream services routed to drum | TEG regeneration, VRU, compressor seal-pot LP relief | DBM line 499 |
| Downstream of drum (vapor) | LP flare stack (shared HP/Cryo+LP dual stack basis) | DBM line 497, 499 |
| Downstream of drum (liquid) | P-3900-2 to slop | DBM line 499 |
| Relief / blowdown sequencing basis | External Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 (referenced; not accessible in workspace) | DBM line 501 (location TBD for final values) |
| Site / facility | 03-25 facility, shared flare interface with 04-25 | DBM line 56, 497 |

## Construction

| Item | Value | Source |
|---|---|---|
| Code basis | TBD — vendor to identify governing pressure vessel and relief code(s) | TBD |
| Fabrication scope | Vendor-engineered, vendor-fabricated/supplied skidded or field-erected drum and accessories | _CONTEXT.md Scope |
| Accessories in scope | Transfer pump P-3900-2 and associated mechanical interfaces; level/pressure/temperature instrumentation; relief and isolation valving as defined by detailed design | DBM line 499, 584; ASSUMPTION on instrumentation scope |
| Inspection / test | TBD — vendor ITP per applicable code | TBD |
| Painting / insulation / tracing | TBD — facility specifications not yet sliced to this deliverable | TBD |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Flare and Blowdown; Sparing Philosophy)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row for DEL-082-04)
- `_REFERENCES.md` (deliverable-local reference set; many source slices marked deferred)
- 26020-Package_Requirements.docx package heading 35 (referenced by decomposition; not locally accessible as sliced text) — location TBD
- Workbook Packages row 56 (referenced by decomposition; not locally accessible as sliced text) — location TBD
- EPC Scope of Work (DEL-082-01) and EPC Package Datasheet (DEL-082-02) — upstream EPC anchor deliverables that will govern vendor inputs once accepted (status: peer deliverables in the same package; not yet INITIALIZED at time of this draft — TBD)
