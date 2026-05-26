# Guidance — Vendor Engineered Equipment Package (DEL-100-04)

> Directional guidance for engineering, designing, and reviewing the Hydrogen Peroxide
> Sweetening Unit vendor package. Rationale is drawn from the locally accessible source
> slice (`_Sources/26020-Package_Requirements.docx`, package heading 52). Items not
> supported by source are `TBD` or surfaced in the Conflict Table.

## Purpose

This deliverable exists to produce a single, integrated, vendor-engineered Hydrogen
Peroxide Sweetening Unit that satisfies the EPC Scope of Work and the Package Datasheet
(decomposition route, `_CONTEXT.md`). The vendor package is the physical realization step:
its design and supply close the gap between the EPC's bid-basis package requirements and a
field-ready, registerable piece of equipment with a complete document set.

It supports project objectives `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`,
`OBJ-008`, `OBJ-009`, `OBJ-010` (source: `_CONTEXT.md`; objective association recorded as
**ASSUMPTION (PACKAGE_HEURISTIC)** because the objective-to-deliverable map is
package-grouped — see `OBJECTIVE_DELIVERABLE_MAP.csv` in the Gate 7 snapshot).

## Principles

1. **Source fidelity over convention.** Anchor design choices to package heading 52 (the
   accepted package requirements text) and the RFQ basis (`26020-03-PT-RFQ-27-001-H202_
   Sweet_Unit.docx`, `location TBD`). Where the source says "Vendor to design", the vendor
   owns the design choice — but it must be defensible against the stated operating and
   ambient conditions.
2. **Treat "by others" as a hard scope boundary.** Interconnecting piping, DCS
   integration, foundations, and electrical supply to MCC are explicitly out of vendor
   scope. Vendor engineering must terminate cleanly at the interface boundary and
   communicate tie-in requirements via the tie-in list (`PIP-004`).
3. **Engineer to confirm "TBC" values early.** Two items are explicitly TBC in the
   source — design conditions and pump capacity. Close these via the vendor's Mechanical
   Design Basis (`MEC-001`) before downstream engineering depends on them.
4. **Carry the full vendor document set.** The vendor deliverable set in package heading
   52 is broad (core vendor, mechanical, rotating, static, tanks, process, relief, piping,
   drainage, electrical, I&C, building, fire & gas, structural). Omissions translate
   directly to gaps in `DEL-100-05` (turnover) and `DEL-100-06` (acceptance).
5. **Respect ambient envelope.** The −40 °C minimum / +35 °C maximum ambient envelope
   should drive material selection (cold-service toughness), insulation, heat tracing
   (EHT), and freeze-protection of the H₂O₂ chemistry. (Source: package heading 52,
   "Design conditions".)

## Considerations

- **Chemistry handling.** Hydrogen peroxide is an oxidizer. Material compatibility,
  passivation of wetted surfaces, venting, and contamination control are material to
  reactor, pump, mixer, and tank design. Source slice does not specify materials —
  `TBD`; rely on vendor's process safety information (`PRO-027`) and HAZOP input
  (`PRO-026`).
- **Freeze protection.** Sour-water inlet at 9 °C and ambient minimum −40 °C imply
  EHT/insulation on exposed lines and freeze-protected building heating. EHT applicability
  is marked Yes in the interface summary.
- **Sizing of the H₂O₂ pump and reactor(s).** Capacity 24,154 BBL/D of sour water at
  160 m³/h sets the reactor residence time and H₂O₂ dose envelope; vendor sizing logic
  should be captured in `PRO-005` (Heat & Material Balance) and `PRO-012` (Line Sizing /
  Hydraulic Calculation).
- **Electrical starting strategy.** 575 V, 3-PH, 60 Hz with DOL or VFD: choice affects
  inrush, MCC sizing, and motor starting study (`ELE-011`). Local H-O-A allows manual
  isolation for maintenance.
- **Pressure equipment registration.** Static pressure equipment (likely the reactors)
  requires registration via `REG-022`. Jurisdictional code is not stated in source —
  ASSUMPTION (likely Alberta ABSA or equivalent given "West Doe" naming convention); to be
  confirmed.
- **Building.** A self-framing building shifts structural responsibility partly to the
  vendor; coordination with site civil/foundation scope (by others) is essential.

## Trade-offs

| Trade-off | Direction |
|---|---|
| Reactor sizing vs H₂O₂ dose vs residence time | Source gives capacity but not target sweetening efficiency; vendor must balance reactor volume against dose rate. `TBD` performance target. |
| DOL vs VFD pump starting | DOL is simpler; VFD enables flow turndown for dose control. Source allows either — vendor selection. |
| Skid-mount vs in-building install | Source explicitly requires self-framing building; trade-off resolved by source. |
| Carbon steel vs stainless wetted parts | Source silent on material — `TBD`. Oxidizer service generally favors compatible alloys; vendor responsibility. |

## Examples / Worked Notes

No worked examples are present in the source slice. Worked examples (e.g., reactor
residence time sizing, EHT load calc, MCC feeder sizing) would normally appear in vendor
calculation packages `MEC-014`, `PRO-012`, `ELE-011`. `TBD` until those vendor deliverables
are produced.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | RFQ basis document `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` is cited in package heading 52 but is not locally accessible. Detailed RFQ-level requirements (e.g., warranty terms, FAT scope, performance guarantees) cannot be source-grounded. | `_Sources/26020-Package_Requirements.docx` package heading 52, "Source Basis" | RFQ docx — not locally accessible | Datasheet §References; Specification §Standards, §Verification | PROPOSAL: treat package heading 52 as authoritative until RFQ document is obtained; flag RFQ as missing reference. | TBD |
| CT-002 | The package PFD ("see attached PFD") is referenced from package heading 52 but is not locally accessible. "Additional equipment shown in PFD" cannot be enumerated. | Package heading 52, "Process function" / "Major Included Equipment" | PFD — not locally accessible | Datasheet §Attributes; Specification §R-MEC-006 | PROPOSAL: keep R-MEC-006 open and require vendor's `PRO-004` PFD to close. | TBD |
| CT-003 | Design conditions are stated as "TBC" and pump capacity as "TBC" in source. These cannot be specified now. | Package heading 52, "Design conditions"; "Capacity/design throughput" | — | Specification §R-DESN; Datasheet §Conditions | PROPOSAL: close TBC values in vendor `MEC-001` Mechanical Design Basis and `MEC-007` Pump Data Sheets. | TBD |
| CT-004 | Governing standards (pressure vessel code, tank standard, electrical code, jurisdictional pressure registration authority) are not enumerated in source. | Package heading 52 | — | Specification §Standards | PROPOSAL: vendor to declare governing codes in `MEC-001`; project to confirm jurisdiction (likely ABSA — ASSUMPTION). | TBD |
| CT-005 | Interface row references both row 63 (from `_CONTEXT.md`) and "column M (row 63)" (from package heading 52 for Area/Exterior Lighting only). The interpretation of "column M" is not explicit in the locally accessible source slice. | `_CONTEXT.md` ("Workbook Packages row 63") | Package heading 52 inline note ("column M (row 63)") | Datasheet §Physical Interface Summary | PROPOSAL: validate row 63 in `_Sources/26020-Packages_Interfaces_4_export.xlsx` and reconcile the column-M nuance. | TBD |
