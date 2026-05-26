# Specification — DEL-067-02 Package Datasheet (PKG-067 Tanks, Sour Water (API 650) 4-25)

## Scope

This specification governs the technical content of the EPC Package Datasheet for PKG-067 "Tanks, Sour Water (API 650) 4-25" within the West Doe Deepcut Expansion (facility 04-25). The datasheet defines the equipment data, design conditions, and interface envelope required for third-party vendor or discipline package engineering and fabrication of the produced/sour water storage tanks (TK-9010-1, TK-9020-1) and immediately associated package-internal scope.

**In scope (per PACKAGE_REGISTER row 94 and 4-25_Deepcut_DBM.md §Produced Water):**
- Two atmospheric produced/sour water storage tanks (2 x 2,000 bbl) per modified API-650.
- Tank-mounted appurtenances: PVRVs, level/temperature instrumentation, hydrocarbon skim, heating, insulation, internal coating.
- Tank-level interface points: process inlet, transfer outlet, blanket gas, drains, vents, truck-out connection, secondary containment interface.

**Excluded:**
- Produced water transfer pumps (housed in Tank Farm Pump Building 2; separate package — DBM line 2555).
- Sour water treatment pumps (separate package — DBM line 2555).
- The downstream produced water pipeline to 03-25 Liquids Hub, which is "designed and installed by others" (DBM line 506).
- Package-specific exclusions from the source workbook: TBD (workbook entry states "TBD; no package-specific exclusions stated in source materials" — PACKAGE_REGISTER row 94 Exclusions column).

## Requirements

### R1 — Tank design standard
The tanks shall be designed and fabricated to modified API-650 for atmospheric service with 16 oz (water column) test pressure. (Source: 4-25_Deepcut_DBM.md line 518.)

### R2 — Tank quantity and capacity
Two tanks of 2,000 bbl nominal capacity each shall be supplied. (Source: 4-25_Deepcut_DBM.md line 493; PACKAGE_REGISTER row 94 equipment list.)

### R3 — Fill limit
Maximum normal fill shall be limited to 90% of tank volume. A thermal expansion review of the high-level setpoint is required. (Source: 4-25_Deepcut_DBM.md line 519.)

### R4 — Insulation and heating
Each tank shall be externally insulated and heated for cold-climate (BC, ~22.2 km north of Dawson Creek) operation. Insulation thickness, heat-tracing details, and heating medium are TBD pending detailed engineering. (Source: 4-25_Deepcut_DBM.md lines 7, 524; thickness/medium TBD.)

### R5 — Internal coating
Internal surfaces (floor, walls, roof) shall be coated with Devchem 253 or approved equivalent. (Source: 4-25_Deepcut_DBM.md line 524.)

### R6 — Hydrocarbon skim system
Each tank shall be equipped with a Kennilworth-type hydrocarbon skim float system. (Source: 4-25_Deepcut_DBM.md line 524.)

### R7 — Pressure/vacuum relief
Each tank shall have at least one PVRV. Emergency pressure relief vent (EPRV) sizing shall be reviewed during detailed engineering. PVRV vent disposition (atmospheric versus low-pressure flare/vent header) is TBD pending Relief/Flare/Vent interface resolution. (Source: 4-25_Deepcut_DBM.md line 524; PACKAGE_REGISTER row 94 interface list.)

### R8 — Blanket gas
A blanket gas system shall be provided to prevent winter vacuum. Blanket gas rates shall be sized per API-2000. (Source: 4-25_Deepcut_DBM.md line 523.)

### R9 — Design specific gravity
Tank design specific gravity shall be 1.25 (TBC). Operating produced-water density is 1008 kg/m³ at 26.7 °C; downstream transfer pumps use a conservative design SG of 1.18. (Source: 4-25_Deepcut_DBM.md line 508.)

### R10 — Sour-service vapour-handling
Tank isolation philosophy shall be reviewed in the context of potential sour vapours (H2S risk). Vapour-space classification, vent disposition, and operator-access controls shall reflect the conclusion of this review. (Source: 4-25_Deepcut_DBM.md line 524.)

### R11 — Contents composition
The stored fluid is produced water that may contain trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, and mercaptans. The list is not comprehensive and remains TBC. Materials of construction, coating compatibility, and elastomer selections shall be verified against this contaminant set. (Source: 4-25_Deepcut_DBM.md line 508.)

### R12 — Storage sizing basis
The 2 x 2,000 bbl configuration provides ~8.9 days of storage at a production-rate basis of 380 bbl/d. The summer flow basis is 1,684 kg/h / 39.9 Am³/d; normal and design flows are TBC. Average accumulation is 60 m³/d continuous; batch pump-in to 03-25 is ~240 m³/d. (Source: 4-25_Deepcut_DBM.md lines 493, 506, 511-513.)

### R13 — Truck-out provisions
A common envirobox truck-out connection shall be provided. Sizing assumption: vacuum truck rate 2.75 m³/min (TBC); typical B-train pump-out 55 m³ in 20 minutes. (Source: 4-25_Deepcut_DBM.md lines 514-516.)

### R14 — Plot spacing
Tank-to-tank spacing shall be ≥ 2.35 m (7.72 ft) per NFPA 30 Table 22.4.2.1. Spacing from public road shall be ≥ 80 m (262.5 ft) per OGAOM Sec. 9.6.15 / DPR 48. Spacing from flare shall be ≥ 25 m (82 ft) and from fired heater ≥ 25 m (82 ft) per OGAOM Sec. 9.6.15. (Source: 4-25_Deepcut_DBM.md lines 268, 270, 283, 297.)

### R15 — Interface envelope
The package shall accommodate the interface types declared in PACKAGE_REGISTER row 94: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Each interface's tag-level boundary, supplier-of-record, and acceptance criteria shall be carried in the package interface requirements matrix (Datasheet § Interface Requirements Matrix) and resolved via the INTERFACE_REGISTER for PKG-067 prior to vendor RFQ release. (Source: PACKAGE_REGISTER row 94.)

### R16 — Secondary containment
Tank farm secondary containment per applicable Canadian/BC regulation and OGAOM is required (TBD — specific volume/standard not stated in DBM produced-water section; confirm during civil/site design).

### R17 — Source-document basis
The Package Datasheet shall cite the GATE-07 Final Published PROJECT_DECOMP snapshot and the West Doe Deepcut DBM as its authoritative source set. Any value not traceable to those sources shall be labeled TBD or ASSUMPTION.

## Standards

| Standard | Use | Location/Reference | Source Citation |
|---|---|---|---|
| API-650 (modified) | Atmospheric tank design and fabrication | DBM Process Storage Areas table | 4-25_Deepcut_DBM.md line 518 |
| API-2000 | Tank pressure/vacuum venting (blanket gas sizing basis) | DBM Process Storage Areas | 4-25_Deepcut_DBM.md line 523 |
| NFPA 30 (Table 22.4.2.1, Table 22.4.1.5) | Atmospheric-tank spacing | DBM Spacing tables | 4-25_Deepcut_DBM.md lines 268, 269 |
| OGAOM Sec. 9.6.15 | Spacing from flare, fired heater, public road | DBM Spacing tables | 4-25_Deepcut_DBM.md lines 270, 283, 297 |
| API 2510 | Spacing from pressurized bullets (relevant adjacent storage) | DBM Spacing tables | 4-25_Deepcut_DBM.md lines 258, 265 |
| BC OGC / BC Energy Regulator permitting | Permit basis | DBM §Permitting | 4-25_Deepcut_DBM.md line 133 (context only; permitting handled at facility level) |
| 26020-Package_Requirements.docx package heading 22 | Package-specific requirements paragraph | location TBD (binary not extracted locally) | _CONTEXT.md; PACKAGE_REGISTER row 94 |

## Verification

| Requirement | Verification Method |
|---|---|
| R1 (API-650) | Vendor design review, code-stamp/certification documentation, mill test reports |
| R2 (quantity/capacity) | Drawing review against datasheet |
| R3 (fill limit) | Instrumentation/setpoint review; thermal expansion calculation deliverable |
| R4 (insulation/heating) | Insulation spec submittal; heat-tracing design review; commissioning hot-loop test |
| R5 (coating) | Coating spec submittal; holiday testing per coating-system QA |
| R6 (skim) | Vendor general arrangement drawing; FAT inspection |
| R7 (PVRV/EPRV) | Relief-device sizing calculation; PVRV nameplate verification |
| R8 (blanket gas) | API-2000 sizing calculation; commissioning blanket-gas pressure test |
| R9 (design SG) | Vendor design calculation verified against DBM SG basis |
| R10 (sour vapour) | Isolation philosophy HAZOP/LOPA outcome; vent disposition decision document |
| R11 (contents) | Materials/coating compatibility statement from vendor |
| R12 (sizing) | Sizing calculation traceable to DBM flow basis |
| R13 (truck-out) | Drawing review; commissioning truck-loadout test |
| R14 (spacing) | Plot plan check against NFPA/OGAOM clearances |
| R15 (interfaces) | Interface register sign-off; tag-to-tag boundary verification |
| R16 (containment) | Civil/containment design review |

## Documentation

The Package Datasheet deliverable shall produce / underwrite the following artifacts (per DELIVERABLE_REGISTER row 529 "Anticipated Artifacts"):

- Package technical datasheet (this document set; Datasheet.md is the primary artifact)
- Vendor engineering handoff basis (this document set + transmittal letter)
- Package interface requirements matrix (Datasheet § Interface Requirements Matrix; cross-reference to INTERFACE_REGISTER)
- Source-supported equipment and design criteria (Datasheet § Attributes/Conditions/Construction)
