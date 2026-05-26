# Datasheet: DEL-057-02_package-datasheet — Package Datasheet (PKG-057 Stabilizers)

> Descriptive document. Values are extracted from accessible decomposition source slices. Unverified items are marked `TBD`. Inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-057-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-057` Stabilizers | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-057 |
| WBS | 01 (Workbook row 82) | `PACKAGE_REGISTER.csv` row PKG-057 |
| Workbook Tracking No. | `26020-01-17-005` | `PACKAGE_REGISTER.csv` row PKG-057 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Source Basis | Workbook Packages row 82; 26020-Package_Requirements.docx package heading 12; `Bid Docs/Budgetary/26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md` | `PACKAGE_REGISTER.csv` row PKG-057; `_REFERENCES.md` |

## Attributes (Package Definition)

| Attribute | Value | Source / Note |
|---|---|---|
| Package Function | Stabilization of raw condensate from MPFF bottoms; produces stabilized hydrocarbon liquid product | `SCOPE_LEDGER.csv` SOW-0178 |
| Number of Packages | 3 (three) Inlet Stabilizer Packages, configured 3 x 40% | `SCOPE_LEDGER.csv` SOW-0178, SOW-0179 |
| Design Throughput (each package) | 1,272 m3/d (8,000 bbl/d) | `SCOPE_LEDGER.csv` SOW-0179, SOW-0180 |
| Turndown Ratio | 3:1 | `SCOPE_LEDGER.csv` SOW-0180 |
| Ownership Split | Package Vendor: package engineering, design, vendor documentation, physical equipment package. EPC Integrator: integration into facility, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` row PKG-057; `SCOPE_LEDGER.csv` SOW-0177 |
| By-others (excluded from package supply) | Interconnecting piping at skid edge; DCS integration; foundations; electrical power supply from plant MCC; installation/erection | `SCOPE_LEDGER.csv` SOW-0180 |

## Conditions

### Operating Conditions

| Item | Value | Source |
|---|---|---|
| Flash Feed Separator — Pressure | 345 kPag | SOW-0180 |
| Flash Feed Separator — Temperature | 30.6 °C | SOW-0180 |
| Flash Feed Separator — Retention Time | ~15 minutes | SOW-0180 |
| Feed / Bottoms Exchangers — Pre-heat outlet | 71 °C (liquid hydrocarbons pre-heated) | SOW-0180 |
| Stabilizer Column — Inlet Temperature | 71 °C | SOW-0180 |

### Design Conditions

| Item | Value | Source |
|---|---|---|
| Flash Feed Separator — Design Inlet Pressure | 1724 kPag | SOW-0180 |
| Flash Feed Separator — Design Inlet Temperature | 60 °C | SOW-0180 |
| Feed / Bottoms Exchanger — Minimum approach | 16.7 °C (30 °F) | SOW-0180 |
| Stabilizer Column — Minimum pressure | 793 kPag | SOW-0180 |
| Turndown ratio | 3:1 | SOW-0180 |
| Stabilizer Product Cooler — Sizing | 130% | SOW-0180 |

### Driver / Motor Conditions

| Item | Value | Source |
|---|---|---|
| Feed Pumps Driver | Electric motor; VFD compatible | SOW-0180 |
| Product Cooler Fan Driver | Electric motor; VFD compatible | SOW-0180 |

## Construction (Major Included Equipment per Package)

| Equipment | Quantity / Spec | Source |
|---|---|---|
| Trayed Reboiled Distillation Columns | Included | SOW-0179 |
| Floating Valve Trays | 20 trays per column | SOW-0179 |
| Level Indicating Transmitter (LIT) | 1 | SOW-0179 |
| Temperature Indicating Transmitter (TIT) | 1 | SOW-0179 |
| Stabilizer Flash Feed Separator | Included (process function) | SOW-0178 |
| Basket Strainers | Included | SOW-0178 |
| Stabilizer Feed Pumps | Included, electric VFD-compatible | SOW-0178, SOW-0180 |
| Feed/Bottoms Exchanger | Included | SOW-0178, SOW-0180 |
| Stabilizer Product Cooler | Included (130% sizing) | SOW-0180 |
| Additional equipment items (full BOM) | TBD — full vendor BOM not enumerated in accessible source extracts | location TBD (26020-Package_Requirements.docx package heading 12) |

## Package Interface Requirements Matrix

All interface types listed are required (`Required = YES` per `INTERFACE_REGISTER.csv` rows for PKG-057):

| InterfaceID | Interface Type | Required |
|---|---|---|
| IFC-D21E8C7B5A | Process Piping | YES |
| IFC-6BCC2E3C15 | Utility Piping | YES |
| IFC-779052A021 | Relief / Flare / Vent | YES |
| IFC-679E4A8B7B | Drain / Containment | YES |
| IFC-B993178278 | Electrical Power | YES |
| IFC-776A72E139 | EHT (Electric Heat Trace) | YES |
| IFC-76F627A820 | Grounding / Bonding | YES |
| IFC-FB548C4A05 | Area / Exterior Lighting | YES |
| IFC-C11289330C | I&C / Control Cabling | YES |
| IFC-95B54D41DE | Building HVAC / Services | YES |
| IFC-F92745CB89 | Fire & Gas / Safety Systems | YES |
| IFC-FE5CDE7BA5 | Maintenance Access | YES |
| IFC-8F5B9774B3 | Structural / Foundations / Supports | YES |

Source: `INTERFACE_REGISTER.csv` (Gate-07 snapshot), all rows scoped to `PKG-057`, workbook row 82.

## References

- `PACKAGE_REGISTER.csv` row `PKG-057` — Gate-07 snapshot
- `DELIVERABLE_REGISTER.csv` row `DEL-057-02_package-datasheet` — Gate-07 snapshot
- `SCOPE_LEDGER.csv` rows `SOW-0177`, `SOW-0178`, `SOW-0179`, `SOW-0180` — Gate-07 snapshot
- `INTERFACE_REGISTER.csv` rows scoped to `PKG-057` — Gate-07 snapshot
- Workbook Packages row 82 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) — referenced source, slice not opened (location TBD beyond extracts already promoted into Gate-07 ledgers)
- `26020-Package_Requirements.docx` package heading 12 — referenced source, slice TBD (binary `.docx` not directly read; extracts in SCOPE_LEDGER are authoritative for the items reproduced above)
- `Bid Docs/Budgetary/26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx` — referenced source, slice TBD (binary not directly read)
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — referenced source, slice TBD (not re-read in this pass; OBJ-001 narrative confirms 04-25 Deepcut sour-gas stabilization context)
