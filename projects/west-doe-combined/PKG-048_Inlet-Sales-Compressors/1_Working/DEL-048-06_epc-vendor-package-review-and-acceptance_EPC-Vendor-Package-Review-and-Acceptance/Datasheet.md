# Datasheet — DEL-048-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-048-06_epc-vendor-package-review-and-acceptance | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | PKG-048 | `_CONTEXT.md` |
| Package | Inlet / Sales Compressors | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| ScopeItemsCovered | SOW-0115, SOW-0116, SOW-0117, SOW-0118 | GATE-07 SCOPE_LEDGER rows 116-119 |
| ObjectivesSupported | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | GATE-07 OBJECTIVE_DELIVERABLE_MAP |

## Attributes (Subject Package Under Review)

The subject of EPC review is the Inlet/Sales Gas Compressor package supplied by the Package Vendor.

| Attribute | Value | Source |
|---|---|---|
| Compressor count | Five (5) inlet/sales gas compressors | SCOPE_LEDGER SOW-0116 (26020-Package_Requirements.docx, heading 3, Basic scope) |
| Compressor model | Ariel KBC/6, 3-stage reciprocating | SOW-0116 |
| Service | Inlet (single stage) and Sales (double stage) | SOW-0116 |
| Per-unit sizing | 120% of design | SOW-0116 |
| Driver | 8-pole DOL induction motor with soft-start; 5,000 kW (6,700 HP) per unit (Major Equipment) / 5,220 kW (7,000 HP) per unit (Scope Notes) — value discrepancy, see Guidance Conflict Table | SOW-0117, SOW-0118 |
| Motor electrical | 6600 V / 3PH / 60 Hz, 891 RPM | SOW-0117 |
| Motor enclosure | TEFC or WPII, non-sparking bidirectional cooling fan; NEMA MG 1 | SOW-0118 |
| Preferred motor frame/make | KBZ Frame, 6700 hp, preferred WEG motor | SOW-0118 |
| Total connected load (5 units) | 26,100 kW (35,000 HP) | SOW-0118 |
| Suction scrubbers | Two-phase, upstream of each stage; vertical flow vane-style demisters (horizontal and vertical acceptable); K factor ≤ 0.5 Imperial plus de-ration for pressure; liquid density basis 0.61 SG | SOW-0117 |
| Air cooler | One common air cooler frame per package for both services; automated louver control via pneumatic temperature control on each process bundle | SOW-0117 |

## Conditions (Operating / Design)

| Parameter | Value | Source |
|---|---|---|
| Inlet compressor design capacity (each) | 1,766 e3m3/d (62.4 MMSCFD) | SOW-0118 |
| Sales compressor design capacity (each) | 1,630 e3m3/d (57.6 MMSCFD) | SOW-0118 |
| Turndown | None | SOW-0118 |
| Inlet operating suction / discharge pressure | 4,309 kPag (625 psig) / 7,791 kPag (1,130 psig) | SOW-0118 |
| Sales operating suction / discharge pressure | 3,034 kPag (440 psig) / 10,343 kPag (1,500 psig) | SOW-0118 |

## Construction (By-Others / Scope Splits)

| Item | Owner | Source |
|---|---|---|
| Shipping compressor package to site | By others | SOW-0118 |
| Installation on piles | By others | SOW-0118 |
| Tie-in piping | By others | SOW-0118 |
| Electrical connections | By others | SOW-0118 |
| Mounting platform and stairs | By others | SOW-0118 |

ASSUMPTION: "By others" in this package context refers to the EPC Integrator scope (consistent with SOW-0115 split between Package Vendor and EPC Integrator).

## Review/Acceptance Artifacts (Deliverable Outputs)

| Artifact | ID | Source |
|---|---|---|
| Vendor document review and comment log | ART-F8E220700B | ARTIFACT_REGISTER row 3496 |
| Vendor package acceptance and turnover checklist | ART-7862D9EB63 | ARTIFACT_REGISTER row 3497 |
| Factory/shop test and inspection evidence | ART-00AE5AE3CA | ARTIFACT_REGISTER row 3498 |
| Turnover evidence | TBD (artifact ID not registered separately) | `_CONTEXT.md` anticipated artifacts |

## References

- `_CONTEXT.md`
- GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row 359; `SCOPE_LEDGER.csv` rows 116-119; `ARTIFACT_REGISTER.csv` rows 3496-3498; `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Original source: `26020-Package_Requirements.docx` package heading 3 (binary; not directly readable in this run — source slices accessed via GATE-07 extracted SCOPE_LEDGER rows). Location TBD for clause-level detail.
- Workbook Packages row 65 (`26020-Packages_Interfaces_4_export.xlsx`; binary; location TBD).
