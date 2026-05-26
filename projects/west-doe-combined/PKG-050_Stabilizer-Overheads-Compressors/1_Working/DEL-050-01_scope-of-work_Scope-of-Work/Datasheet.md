# Datasheet — DEL-050-01_scope-of-work (Scope of Work, PKG-050 Stabilizer Overheads Compressors)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-050-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | PKG-050 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Package Name | Stabilizer Overheads Compressors | PACKAGE_REGISTER.csv (PKG-050) |
| CoA Tracking Number | 26020-01-12-005 | PACKAGE_REGISTER.csv (PKG-050) |
| Workbook Row | 81 | PACKAGE_REGISTER.csv (PKG-050) |
| WBS | 01 | PACKAGE_REGISTER.csv (PKG-050) |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; PACKAGE_REGISTER.csv (responsibility narrative) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package count | Two (2) identical induction-motor-driven separable reciprocating compressor packages, each 100% capacity | SCOPE_LEDGER.csv SOW-0174 |
| Major equipment family | Ariel KBC/6 four-stage separable reciprocating compressor packages | SCOPE_LEDGER.csv SOW-0175 |
| Driver | 8-pole electric induction motor, 2700 HP @ 891 RPM, with speed control, 4000 V, 3PH, 60 Hz; "No Toshiba motors"; non-spring bidirectional cooling fans; enclosure TBD (quote TEFC); tested/labelled to NEMA MG 1 | SCOPE_LEDGER.csv SOW-0175, SOW-0176 |
| Process function | Compress and recycle multiple streams from 50 psig to 1100 psig; final discharge to amine inlet filter coalescer or recycled back to first stage | SCOPE_LEDGER.csv SOW-0174 |
| Stages | 4 (interstage cooling and scrubbing) | SCOPE_LEDGER.csv SOW-0175 |
| Automated recycle valve | Required | SCOPE_LEDGER.csv SOW-0175 |
| Intercooler | Forced-air after each stage; common-frame air-cooler; AP-661 (modified); warm-air recirculation plenum heater; non-sparking, bidirectional cooling | SCOPE_LEDGER.csv SOW-0175 |
| 1st stage scrubber | Two-phase with cyclonic element; vendor sizes capacity | SCOPE_LEDGER.csv SOW-0175 |
| 2nd/3rd/4th stage scrubbers | Two-phase with demister; vendor sizes capacity | SCOPE_LEDGER.csv SOW-0175 |
| Packing vent/drain separation pot | Two-phase; DP 101 kPag; vendor sized | SCOPE_LEDGER.csv SOW-0175 |
| Auxiliaries | Vacuum pump; seal-pot waste-oil transfer pump (both vendor-sized) | SCOPE_LEDGER.csv SOW-0175 |

## Conditions (Operating)

Source: SCOPE_LEDGER.csv SOW-0176 (`26020-Package_Requirements.docx package heading 5`).

| Stage | Suction Pressure | Discharge Pressure | Cooler Discharge Temperature |
|---|---|---|---|
| 1 | 345 kPag | 799.09 kPag | 65.56 °C |
| 2 | 723.48 kPag | 1696.74 kPag | 87.78 °C |
| 3 | 1594.72 kPag | 3600.16 kPag | TBD (source records "3rd." truncated) |
| 4 | 3423.59 kPag | 7585 kPag (final compression) | TBD |

Capacity / turndown:

| Item | Value | Source |
|---|---|---|
| Stage 1 design capacity | 2.5 MMSCFD | SOW-0176 |
| Stage 2 design capacity | 5 MMSCFD | SOW-0176 |
| Stage 3 design capacity | 17 MMSCFD | SOW-0176 |
| Stage 4 design capacity | 17 MMSCFD | SOW-0176 |
| Turndown | 3:1 | SOW-0176 |

## Conditions (Design)

| Item | Value | Source |
|---|---|---|
| Design temperature, each-stage suction | 149 °C | SOW-0176 |
| Design temperature, each-stage discharge | 177 °C | SOW-0176 |
| MAWP, 1st-stage suction | 1723 kPag | SOW-0176 |
| Minimum MAWP, final-stage discharge | 9101 kPag at 177 °C | SOW-0176 |
| Other MAWP | TBC (per source: "Other MAWP is TBC") | SOW-0176 |

## Construction

| Item | Value | Source |
|---|---|---|
| Mounting | Common frame for air-cooler train | SOW-0175 |
| Installation by others | Shipping packages to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs | SOW-0176 |
| Package vendor responsibility | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv (PKG-050 responsibility narrative) |
| EPC Integrator responsibility | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv (PKG-050 responsibility narrative) |

## Tagged-Equipment / Package Identity List

| Field | Value | Source |
|---|---|---|
| Package long identity | 26020-01-PT-12-005 — Stabilizer Overheads Compressors | PACKAGE_REGISTER.csv (PKG-050) |
| Compressor frame | Ariel KBC/6 (four-stage separable reciprocating) | SOW-0175 |
| Per-package quantity | 2 (each 100% capacity) | SOW-0174 |
| Driver motor | 2700 HP induction, 4000 V, 3PH, 60 Hz | SOW-0175 / SOW-0176 |
| Air cooler | AP-661 (modified) forced-air, after each stage | SOW-0175 |

## Applicable Interfaces (Workbook-Declared)

Source: INTERFACE_REGISTER.csv (PKG-050) — Workbook Packages row 81.

- Process Piping (IFC-67DA240B8B)
- Utility Piping (IFC-725FBB759B)
- Relief / Flare / Vent (IFC-3A2F10ED86)
- Drain / Containment (IFC-061B960A40)
- Electrical Power (IFC-8FFD5DC476)
- EHT (IFC-99FA28FF5B)
- Grounding / Bonding (IFC-5857EDB26F)
- Area / Exterior Lighting (IFC-13F6E55BFA)
- I&C / Control Cabling (IFC-9E7E48AE7C)
- Building HVAC / Services (IFC-91754EC616)
- Fire & Gas / Safety Systems (IFC-B0A2ACD972)
- Maintenance Access (IFC-4256CB6534)
- Structural / Foundations / Supports (IFC-3F75046AAC)

## References

- `_CONTEXT.md` (DeliverableID, package identity, anticipated artifacts)
- `_REFERENCES.md` (authoritative decomposition snapshot and source root)
- GATE-07 snapshot SCOPE_LEDGER.csv rows SOW-0173 / SOW-0174 / SOW-0175 / SOW-0176
- GATE-07 snapshot PACKAGE_REGISTER.csv row PKG-050
- GATE-07 snapshot INTERFACE_REGISTER.csv rows for PKG-050
- GATE-07 snapshot ARTIFACT_REGISTER.csv rows for DEL-050-01
- Workbook Packages row 81 (`26020-Packages_Interfaces_4_export.xlsx`)
- `26020-Package_Requirements.docx` package heading 5 — `location TBD` (not parsed locally; carried via SCOPE_LEDGER extracts)
- Word Source Basis (cited only): `Bid Docs/Budgetary/26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx` — `location TBD` (not locally extracted)
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — accessible at `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (referenced as Word Source Basis; specific section TBD)
