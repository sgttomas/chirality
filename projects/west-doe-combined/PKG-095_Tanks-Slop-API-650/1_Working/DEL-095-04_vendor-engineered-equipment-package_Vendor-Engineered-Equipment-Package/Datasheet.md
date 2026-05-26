# Datasheet: DEL-095-04 Vendor Engineered Equipment Package (PKG-095 Tanks, Slop API 650)

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-095-04_vendor-engineered-equipment-package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent package | PKG-095 - Tanks, Slop (API 650) | `_CONTEXT.md` |
| Workbook ID / row | 95 / Workbook Packages row 91 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Covered scope items | SOW-0213, SOW-0214, SOW-0215, SOW-0216 | `_CONTEXT.md` |
| Supported objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION - package-grouping heuristic per OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package subject | Slop tankage production unit (API 650 atmospheric tanks for slop service) | `_CONTEXT.md`; `3-25_Comp_and_Liquids_DBM.md` line 406; `4-25_Deepcut_DBM.md` lines 494, 498, 518 |
| Anchoring tag (03-25 condensate slop) | TK-9130-2 (condensate slop tank) | `3-25_Comp_and_Liquids_DBM.md` line 463 |
| 03-25 slop tank capacity / count | 1 x 3,800 bbl condensate slop tank | `3-25_Comp_and_Liquids_DBM.md` line 406; `4-25_Deepcut_DBM.md` line 498 |
| 04-25 slop tank capacity / count | 2 x 2,000 bbl slop tanks (Deepcut) | `4-25_Deepcut_DBM.md` line 494 |
| Tank specification basis | Modified API 650 atmospheric tank; 16 oz test pressure | `4-25_Deepcut_DBM.md` line 518; `3-25_Comp_and_Liquids_DBM.md` line 1646 |
| Condensate slop tank design SG | 1.00 TBC | `3-25_Comp_and_Liquids_DBM.md` line 1643 |
| Condensate slop tank insulation | Fully insulated | `3-25_Comp_and_Liquids_DBM.md` line 1644 |
| Coating (general API-650 Modified tank basis) | Devchem 253 internal coating on floor, walls, and roof (produced-water tank basis; applicability to slop service TBC) | `3-25_Comp_and_Liquids_DBM.md` line 421; `4-25_Deepcut_DBM.md` (Produced water tank coating basis) - ASSUMPTION for slop service |
| Vendor-supplied equipment scope | Vendor engineered physical slop tank package and associated vendor design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts |
| Engineering input basis | EPC package Scope of Work (DEL-095-01) and Package Datasheet (DEL-095-02) | `_CONTEXT.md` Scope |
| Integration review responsibility | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Slop collection and storage for hydrocarbon liquids, condensate slop, and segregated drain routing; truck-in/out service | `3-25_Comp_and_Liquids_DBM.md` lines 463, 497-499, 656, 1661-1665; `4-25_Deepcut_DBM.md` lines 494, 498 |
| Site ambient minimum | -40 deg C minimum ambient governs exposed equipment, instrumentation, and winterization | `3-25_Comp_and_Liquids_DBM.md` (site basis statements, line near 376) |
| Vapour management | Tank vapours managed via VRU (03-25) when applicable; blanket-gas regulation from LP fuel gas; slop tank may be tied to LP flare KO bypass routing under operational scenarios | `3-25_Comp_and_Liquids_DBM.md` lines 438, 463, 1787 |
| Inputs to 03-25 condensate slop tank | Inlet-tank manual cascades, hydrocarbon drain header, LP condensate pump header, stabilizer outlet header, HP/LP flare KO drum pumps to slop, amine surge skim pump, caustic unit drain drum (TBD), amine/TEG flash tank manual skims, amine hydrocarbon skims (TBD) | `3-25_Comp_and_Liquids_DBM.md` lines 1665, 497-499 |
| Truck-out / truck-in interface | 03-25 condensate slop tank has a dedicated truck-in/out envirobox connection | `3-25_Comp_and_Liquids_DBM.md` line 1661 |
| Slop holdup (03-25) | 80 bbl/d into 1 x 3,800 bbl tank ~= 40.4 days holdup (DBM equipment register) | `4-25_Deepcut_DBM.md` line 498 |
| Slop holdup (04-25) | 200 bbl/d into 2 x 2,000 bbl tanks ~= 17.0 days holdup | `4-25_Deepcut_DBM.md` line 494 |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Maximum fill / thermal expansion | 90% of tank volume; thermal expansion review required (Modified API-650 atmospheric tank basis) | `4-25_Deepcut_DBM.md` line 519 (Tank maximum fill row, Modified API-650 basis); ASSUMPTION applies to slop tank by family |
| Final tank register and detailed sizing | TBD - functional allocation "unless superseded by final tank register" (DBM) | `3-25_Comp_and_Liquids_DBM.md` line 406 |
| Amine slop tank applicability | Amine regeneration module includes an amine slop tank (separate from condensate slop tank); inclusion in PKG-095 vendor package scope is TBD pending DEL-095-02 | `3-25_Comp_and_Liquids_DBM.md` lines 532, 1132, 1143, 1715-1717 |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction-facing companion deliverable | DEL-095-03 Construction Work Package | `DELIVERABLE_REGISTER.csv` row DEL-095-03 |
| Document-turnover companion deliverable | DEL-095-05 Vendor Document Turnover Package | `DELIVERABLE_REGISTER.csv` row DEL-095-05 |
| Acceptance / review companion deliverable | DEL-095-06 EPC Vendor Package Review and Acceptance | `DELIVERABLE_REGISTER.csv` row DEL-095-06 |
| Tank specification | Modified API 650 atmospheric tank (16 oz test pressure equivalent class) | `4-25_Deepcut_DBM.md` line 518; `3-25_Comp_and_Liquids_DBM.md` line 1646 |
| Internal coating | Devchem 253 (floor/walls/roof) - confirmed for produced-water tanks; ASSUMPTION for slop service pending DEL-095-02 | `3-25_Comp_and_Liquids_DBM.md` line 421 |
| External insulation / heating | Externally insulated and heated (API-650 Modified tank basis at 03-25); condensate slop tank fully insulated | `3-25_Comp_and_Liquids_DBM.md` lines 421, 1644 |
| Heat tracing | Electrical heat tracing for winterization and freeze protection on tank and drain lines per facility heat-trace philosophy | `3-25_Comp_and_Liquids_DBM.md` (drain systems section ~line 477); ASSUMPTION on tank-specific extent pending DEL-095-02 |
| PVRV / EPRV | At least one PVRV per tank; EPRV sizing to be reviewed during detailed engineering (produced-water tank basis; applicability to slop TBC) | `4-25_Deepcut_DBM.md` line 522 (PVRV/EPRV produced-water-tank statement); ASSUMPTION for slop |
| Foundation / civil tie | Tank foundations per final geotechnical report; equipment-specific foundation and anchorage required | `3-25_Comp_and_Liquids_DBM.md` (civil / foundations section near line 700-730) |
| Vendor engineering deliverables expected | Vendor package design basis, datasheets, equipment GA, P&ID extensions, instrumentation list, weld map, pressure/leak test plan | ASSUMPTION - standard vendor package production unit content; specific list TBD pending DEL-095-02 issue and `26020-Package_Requirements.docx` package heading 47 clause-level read |
| Material of construction (MOC) | TBD - not specified in accessible DBM slices for slop tanks at clause level; carbon steel is the typical default for Modified API-650 atmospheric tanks but must be confirmed against `26020-Package_Requirements.docx` heading 47 |
| Aluminum prohibition | Aluminum shall not be used in the caustic building (DBM); not directly applicable to slop tank package but flagged for site-wide consistency | `3-25_Comp_and_Liquids_DBM.md` (caustic section, near line 398-400) |

## References

- `_CONTEXT.md` (deliverable context)
- `_REFERENCES.md` (authoritative decomposition basis and shared source root)
- `_DEPENDENCIES.md` (declared dependency view)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (PKG-095 deliverable rows)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (PKG-095 row)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — slop and tank slices: lines 406, 421, 463, 497-499, 656, 1643-1646, 1661-1665, 1715-1717, 1787
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — slop and tank slices: lines 494, 498, 518-522
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — package heading 47 (location TBD at clause level; not text-extracted)
