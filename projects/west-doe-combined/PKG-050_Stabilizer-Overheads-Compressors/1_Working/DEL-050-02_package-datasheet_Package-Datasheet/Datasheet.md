# Datasheet — DEL-050-02 Package Datasheet (Stabilizer Overheads Compressors)

> Authoring pass: P1 (initial generation) + P2 (consistency). Pass 3 (semantic lensing) deferred — `_SEMANTIC_LENSING.md` not yet produced.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-050-02_package-datasheet` | `_CONTEXT.md` |
| Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | `PKG-050` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-050 |
| ParentWorkbookID | 50 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WorkbookPackagesRow | 81 | `PACKAGE_REGISTER.csv` row PKG-050 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-050 |
| Package Name | Stabilizer Overheads Compressors | `PACKAGE_REGISTER.csv` row PKG-050 |
| CoA Tracking Number | 26020-01-PT-12-005 — Stabilizer Overheads Compressors | `PACKAGE_REGISTER.csv` row PKG-050 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-050-02 |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Word Source Basis | `Bid Docs/Budgetary/26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx` | `PACKAGE_REGISTER.csv` row PKG-050 SourceBasis |

## Attributes

### Package Configuration

| Attribute | Value | Source |
|---|---|---|
| Compressor count | Two (2x) identical packages, each at 100% capacity | `SCOPE_LEDGER.csv` SOW-0174 (`26020-Package_Requirements.docx` heading 5 — Basic scope) |
| Compressor type | Induction motor-driven separable reciprocating compressor packages | SOW-0174 |
| Compressor frame | Ariel KBC/6 four-stage separable reciprocating | `SCOPE_LEDGER.csv` SOW-0175 (`26020-Package_Requirements.docx` heading 5 — Major included equipment); `ARTIFACT_REGISTER.csv` ART-15F17CEA07 |
| Process function | Compresses and recycles multiple streams from 50 psig to 1100 psig; final discharge routed to amine inlet filter coalescer or recycled back to first stage | SOW-0174 |
| Stages | Four | SOW-0175; SOW-0176 |

### Driver / Motor

| Attribute | Value | Source |
|---|---|---|
| Driver type | 8-Pole electric induction motor | `SCOPE_LEDGER.csv` SOW-0176 (Driver) |
| Power | 2700 HP | SOW-0175 (Compressor Motor); SOW-0176 |
| Speed | 891 RPM with speed control | SOW-0176 |
| Voltage / Phase / Frequency | 4000 V, 3 PH, 60 Hz | SOW-0175; SOW-0176 |
| Recycle valve | Automated recycle valve | SOW-0175 |
| Enclosure | TBD (quote TEFC) | SOW-0176 |
| Cooling fans | Non-spark, bidirectional | SOW-0176 |
| Test/label standard | NEMA MG 1 | SOW-0176 |
| Manufacturer exclusion | No Toshiba motors | SOW-0175; SOW-0176 |

### Capacity / Turndown

| Stage | Design Capacity | Source |
|---|---|---|
| Stage 1 | 2.5 MMSCFD | SOW-0176 (Capacity/design throughput) |
| Stage 2 | 5 MMSCFD | SOW-0176 |
| Stage 3 | 17 MMSCFD | SOW-0176 |
| Stage 4 | 17 MMSCFD | SOW-0176 |
| Turndown ratio | 3:1 | SOW-0176 |

### Operating Conditions (per stage)

| Stage | Suction | Discharge | Cooler Discharge Temp | Source |
|---|---|---|---|---|
| 1 | 345 kPag | 799.09 kPag | 65.56 C | SOW-0176 (Operating conditions; Cooler discharge temperatures) |
| 2 | 723.48 kPag | 1696.74 kPag | 87.78 C | SOW-0176 |
| 3 | 1594.72 kPag | 3600.16 kPag | 3rd stage value TBD (source truncated as "3rd.") | SOW-0176 |
| 4 | 3423.59 kPag | 7585 kPag (compression) | TBD | SOW-0176 |

### Design Conditions

| Attribute | Value | Source |
|---|---|---|
| Design temperature, each stage suction | 149 C | SOW-0176 (Design conditions) |
| Design temperature, each stage discharge | 177 C | SOW-0176 |
| MAWP, 1st stage suction | 1723 kPag | SOW-0176 |
| Minimum MAWP, final stage discharge | 9101 kPag @ 177 C | SOW-0176 |
| Other MAWP values | TBC (per source) | SOW-0176 |

### Auxiliaries / Included Equipment (Major)

| Equipment | Detail | Source |
|---|---|---|
| Air Cooler | Forced air intercooler after each stage; mounted on common frame; Ap-661 (modified); warm air recirculation plenum heater; non-sparking, bidirectional cooling | SOW-0175; ART-15F17CEA07 |
| 1st-stage scrubber | Two-phase c/w Cyclonic Element; vendor to design size/capacity | SOW-0175 |
| 2nd/3rd/4th-stage scrubbers | Two-phase c/w Demister; vendor to design size and capacity | SOW-0175 |
| Packing vent/drain separation pot | Two-phase; DP 101 kPag; vendor to design size and capacity | SOW-0175 |
| Vacuum pump | Vendor to design size and capacity | SOW-0175 |
| Seal Pot waste-oil transfer pump | Vendor to design size and capacity | SOW-0175 |

### Battery-Limit / Interface Inventory

The following interfaces are flagged as applicable to PKG-050 in `INTERFACE_REGISTER.csv` (Workbook Packages row 81) and are carried here as datasheet evidence per the deliverable's `_CONTEXT.md` note that interface facts are intentionally carried in this datasheet rather than as standalone deliverables.

| InterfaceID | Type | Applicable |
|---|---|---|
| IFC-67DA240B8B | Process Piping | YES |
| IFC-725FBB759B | Utility Piping | YES |
| IFC-3A2F10ED86 | Relief / Flare / Vent | YES |
| IFC-061B960A40 | Drain / Containment | YES |
| IFC-8FFD5DC476 | Electrical Power | YES |
| IFC-99FA28FF5B | EHT | YES |
| IFC-5857EDB26F | Grounding / Bonding | YES |
| IFC-13F6E55BFA | Area / Exterior Lighting | YES |
| IFC-9E7E48AE7C | I&C / Control Cabling | YES |
| IFC-91754EC616 | Building HVAC / Services | YES |
| IFC-B0A2ACD972 | Fire & Gas / Safety Systems | YES |
| IFC-4256CB6534 | Maintenance Access | YES |
| IFC-3F75046AAC | Structural / Foundations / Supports | YES |

Detailed tie-in points, sizes, and elevations: `TBD` — not stated in accessible sources.

## Conditions

### Process Service

- Service: Stabilizer overhead compression and recycle. Stream routed to amine inlet filter coalescer or recycled back to first stage. (SOW-0174)
- Pressure envelope: 50 psig suction to 1100 psig final discharge (SOW-0174); per-stage SI-unit values listed under Operating Conditions above (SOW-0176).
- Composition: `TBD` — not stated in accessible source slices for this deliverable.
- Site / ambient conditions: `TBD` — not in accessible source slices.

### Scope Carried By Others (excluded from package vendor supply)

- Shipping compressor packages to site (SOW-0176)
- Installation on piles (SOW-0176)
- Tie-in piping (SOW-0176)
- Electrical connections (SOW-0176)
- Mounting platform and stairs (SOW-0176)

## Construction

| Attribute | Value | Source |
|---|---|---|
| Common frame | Yes — air cooler mounted on common frame (Ap-661 modified) | SOW-0175 |
| Mounting | Installation on piles is by others; package mounting platform and stairs by others | SOW-0176 |
| Materials of construction | `TBD` — not stated in accessible source slices |  |
| Code/standard stamps (vessels, piping, electrical) | `TBD` — not stated; ASSUMPTION: ASME / NEC / NEMA likely applicable given service and motor parameters |  |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` (row PKG-050)
  - `DELIVERABLE_REGISTER.csv` (row DEL-050-02)
  - `SCOPE_LEDGER.csv` (SOW-0173, SOW-0174, SOW-0175, SOW-0176)
  - `INTERFACE_REGISTER.csv` (PKG-050 interface rows)
  - `ARTIFACT_REGISTER.csv` (ART-* rows for DEL-050-02)
- Workbook Packages row 81 (cited in registers; raw workbook not opened in this run — `location TBD` for column-level slices).
- `26020-Package_Requirements.docx` package heading 5 (cited in registers; `.docx` not directly readable in this run — `location TBD` for sub-heading verbatim text).
- Word source basis: `Bid Docs/Budgetary/26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx` (not locally read in this run — `location TBD`).
