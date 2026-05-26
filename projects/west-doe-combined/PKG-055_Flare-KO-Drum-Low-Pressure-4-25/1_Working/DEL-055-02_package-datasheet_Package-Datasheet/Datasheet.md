# Package Datasheet — DEL-055-02

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-055-02_package-datasheet |
| Deliverable Name | Package Datasheet |
| Parent Package ID | PKG-055 |
| Package Name | Flare KO Drum (Low Pressure) 4-25 |
| Workbook Row | 57 |
| WBS | 01 |
| Vendor Package Number | 26020-01-17-003 (Flare KO Drum (LP)) |
| Discipline | Mechanical |
| Type | EPC Package Datasheet |
| Responsible Party | EPC Integrator |
| Facility | 04-25 West Doe Deepcut |
| Source Basis | Workbook Packages row 57; 26020-Package_Requirements.docx package heading 10; DBM-Deepcut/4-25_Deepcut_DBM.md |

## Attributes

### Package Equipment (FACT — `DBM-Deepcut/4-25_Deepcut_DBM.md` Equipment / Module tables)

| Tag | Description | Facility | Qty |
|---|---|---|---|
| V-3900-1 | L.P Flare KO Drum | 4-25 (Deepcut) | 1 |
| P-3900-1 | L.P Flare KO Drum Transfer Pump | 4-25 (Deepcut) | 1 |

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list table and "390-1 LP Flare KO Drum Module" entry (Shop assembly).

### Package Function (FACT)

Receive liquid carry-over from the 04-25 LP flare relief header (508 mm / 20 in), separate free liquids ahead of the LP flare element on the common HP/cryo stack, and provide truck-out via the LP KO drum transfer pump.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` — "Low-pressure flare" row of flare-system summary table; LP flare stack piggy-back description.

### LP Flare Service Sources (FACT — non-exhaustive, drawn from DBM)

- Amine regeneration automated LP-flare pressure control.
- TEG flash drum automated LP-flare blowdown; TEG still overheads recovered to VRU (low backpressure).
- VRU package blowdown; VRU suction header bypass when VRUs are not operational; VRU primary seal vent.
- Reciprocating compressor seal-pot vents.
- Mole-sieve regeneration gas blowdown if contaminated.
- Pressurized caustic drain tank vapour route when overheads compressor is down.
- Possible analyzer vent routing (TBC during detailed engineering).

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` lines describing LP flare connections and routing.

## Conditions

### Header / Stack Data (FACT — DBM)

| Parameter | Value | Source |
|---|---|---|
| LP flare relief header diameter | 508 mm (20 in) | DBM "Low-pressure flare" row |
| LP flare header material | SA-106 | DBM "Flare Header Materials" table |
| LP flare header nominal size | 324 mm (listed) | DBM "Flare Header Materials" table |
| LP flare header length (above ground / below ground) | 270 m / 50 m | DBM "Flare Header Materials" table |
| LP flare element configuration | Piggy-back on common HP/cryo stack | DBM "Low-pressure flare" row and "LP stack" row |
| LP element OD | TBD | DBM "LP stack" row |
| Smokeless operation | Air blower on LP element | DBM "LP stack" row |
| Ringelmann criterion | Ringelmann 1 at ~5% (TBC) of emergency design case flare loads | DBM "LP stack" row |
| Pilot gas requirement | TBC | DBM "LP flare stack pilot and purge gas" row |
| Purge gas requirement | TBC | DBM "LP flare stack pilot and purge gas" row |
| Supplemental fuel gas to LP flare stack | Required for complete combustion; blended LHV ≥ 20 MJ/Sm³ | DBM flare system narrative |
| Heat trace / insulation requirement on LP header outside heated buildings | TBD — DBM specifies HP flare headers; LP not explicitly stated | DBM "HP flare headers outside heated buildings shall be electrically heat traced..." |

### LP Flare Pilot / Purge Estimates (FACT — DBM source-level estimate tables)

| Item | Value | Units |
|---|---|---|
| LP Flare Pilot — total | 37.18 / 6.288 / 0.019 / 43.484 | Published source-level estimate (composition columns) |
| LP Flare Header Purge — total | 523.272 / 88.872 / 0.264 / 612.408 | Overall summary value |

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` "LP Flare Pilot" and "LP Flare Header Purge" rows.

### Relief Volumes / Backpressures

- Relief volumes, actual backpressures, LP stack element OD, stack opacity scenarios, air-assist basis, and the shared 03-25/04-25 allocation are open at the DBM stage. TBD pending detailed-design Aspen Flare System Analyzer modelling.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` "Flare" row of system summary; "Relief volumes remain to be determined during detailed design; preliminary Aspen Flare System Analyzer models support current header sizing."

### Spacing / Layout Constraints (FACT — DBM spacing table)

| Constraint | Value | Code Ref |
|---|---|---|
| Distance between flare tanks (including KO drums) and vegetation or other fire hazards | 10 m (32 ft) | OGAOM, Sec. 9.6.15 |
| Flare inside boundary blackened area thermal radiation flux | ≤ 9 kW/m² | OGPFR Appendix 1, Schedule 1, Sec. 2 (regulatory reference not in package; verify) |
| Flare outside boundary thermal radiation flux | ≤ 5 kW/m² | OGPFR Appendix 1, Schedule 1, Sec. 2 (regulatory reference not in package; verify) |

## Construction

### Modular Scope (FACT — DBM module table)

- `390-1 LP Flare KO Drum Module` — Shop-assembled module.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` module list.

### Package Vendor Construction Responsibilities (FACT — Package Register row 57)

Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration).

Source: `PACKAGE_REGISTER.csv` row 57 (PKG-055).

### Vessel / Pump Mechanical Detail

- Vessel internal coating: TBD (analogous HP/MPFF systems use Devchem 253; LP KO drum coating not explicitly stated in DBM).
- Pump head / capacity / NPSH: TBD (not in DBM; vendor budgetary go-by `24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` cited in PACKAGE_REGISTER is for HP service and is budgetary only).
- Truck-out arrangement: included (DBM "LP KO drum pump P-3900-1 and truck-out provided").

### Interface Types (FACT — Package Register row 57)

Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.

Source: `PACKAGE_REGISTER.csv` row 57.

### Anticipated Artifacts (carries package interface evidence) (FACT — `_CONTEXT.md`)

- Package technical datasheet
- Vendor engineering handoff basis
- Package interface requirements matrix
- Source-supported equipment and design criteria

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — accessible, primary technical basis.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — package heading 10 referenced; binary, not locally extracted (location TBD inside binary).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — workbook Packages row 57; binary, not locally extracted (location TBD inside binary).
- Gate 7 Decomposition snapshot — `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Budgetary go-by: `24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` (HP service; budgetary pricing/delivery only — NOT design authority for LP service).
