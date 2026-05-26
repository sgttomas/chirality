# Datasheet — DEL-067-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-067-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-067` |
| PackageName | Tanks, Sour Water (API 650) 4-25 |
| Subject Equipment Tag | `26020-01-PT-19-005` — Tanks, Sour Water (per `PACKAGE_REGISTER.csv` row `PKG-067`). Expected vessel tags `TK-9010-1`, `TK-9020-1` (per `ARTIFACT_REGISTER.csv` `ART-5AF4728A78`; source: `26020-Package_Requirements.docx` Heading 22, "Major Included Equipment"). |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | Review-and-acceptance evidence pack for the Package Vendor production unit (`DEL-067-04`) and the Vendor Document Turnover (`DEL-067-05`) against the EPC anchor deliverables (`DEL-067-01` SOW, `DEL-067-02` Package Datasheet, `DEL-067-03` Construction Work Package). | `DELIVERABLE_REGISTER.csv` row `DEL-067-06`; `_CONTEXT.md` |
| Acceptance subject | Two API 650 modified atmospheric produced-water / sour-water storage tanks for 4-25 service, matching the 4-25 tank pair identified in the 3-25 sour-water analog. | `PACKAGE_REGISTER.csv` row `PKG-067`, "Major Included Equipment / Scope" (source: `26020-Package_Requirements.docx` Heading 22) |
| Tagged equipment evidence | "Two API 650 modified atmospheric produced-water storage tanks, expected tags TK-9010-1 and TK-9020-1, with internal coating, external insulation and electric heating where required, PVRV/EPRV protection, LP fuel gas blanket, VRU suction/header connection as applicable, tank instrumentation, and standard tank appurtenances." | `ARTIFACT_REGISTER.csv` `ART-5AF4728A78` (source: `26020-Package_Requirements.docx` Heading 22, "Major Included Equipment") |
| Covered SOW IDs | `SOW-0225`, `SOW-0226`, `SOW-0227`, `SOW-0228` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`; per-deliverable confirmation TBD) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service / location | 4-25 West Doe Deepcut produced-water / sour-water storage at the 04-25 facility. | `PACKAGE_REGISTER.csv` row `PKG-067` (Workbook row 94; WBS 01); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §5 (Produced Water) lines 502-524 |
| Tank design code | "Modified API-650 atmospheric tank; 16 oz test pressure" — applied to produced-water tanks at 04-25. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 518 (Produced Water design table) |
| Storage basis | "2 x 2,000 bbl tanks; 380 bbl/d production rate; 8.9 days storage; outlet to pipeline to 03-25 Liquids Hub; truck-out for emergency/local handling." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 493 (storage summary table) |
| Process service | Produced water from 04-25 pumped via new water pipeline to 03-25 Liquids Hub; trucking only in emergencies. Average accumulated rate ~60 m3/d continuous; batch pump-in to Hub ~240 m3/d. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 504-506 |
| Fluid characterization | Produced water "may contain trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, and mercaptans. The list is not comprehensive and is to be confirmed." Density 1008 kg/m3 at 26.7 °C; transfer pump design SG 1.18; tank design SG 1.25 (TBC). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 508 |
| Tank appurtenance basis | "Produced water tanks are externally insulated, heated, internally coated with Devchem 253 on floor, walls, and roof, and fitted with a Kennilworth-type hydrocarbon skim float system. Each tank has at least one PVRV, and EPRV sizing is to be reviewed during detailed engineering. Tank isolation philosophy must be reviewed in the context of potential sour vapours." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 |
| Spacing constraints applicable to acceptance | Distance between atmospheric tanks 2.35 m (NFPA 30 22.4.2.1); flare-to-atmospheric-produced-water tank 25 m (OGAOM 9.6.15); flare-to-tank KO drum / vegetation 10 m (OGAOM 9.6.15); fired heater to atmospheric tank 25 m (OGAOM 9.6.15). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Atmospheric Tank and General Plant Spacing, lines 261-297 |
| Acceptance trigger states (upstream maturity) | `DEL-067-04` (Vendor Engineered Equipment Package) and `DEL-067-05` (Vendor Document Turnover) reach a maturity state acceptable for integration review. Exact gating values TBD; `_DEPENDENCIES.md` declares no upstream/downstream edges as of PREPARATION. | `_DEPENDENCIES.md`; ASSUMPTION |
| Numeric design / sizing values requiring vendor confirmation | Tank design SG (1.25 TBC); EPRV sizing; final tank dimensions; heater sizing; final fluid composition. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 508, 524, 564-565 |

## Construction

| Acceptance Artifact (per `_CONTEXT.md` / decomposition) | Description | Source |
|---|---|---|
| Vendor document review log | Reviewer-by-document register tracking the Package Vendor's Vendor Document Index and each enumerated vendor engineering deliverable for the Tanks, Sour Water package (`26020-01-PT-19-005`). | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-067-05` |
| Package acceptance checklist | Pass/fail acceptance matrix mapped to SOW items `SOW-0225..0228`, the Package Datasheet (`DEL-067-02`), and the Construction Work Package (`DEL-067-03`); covers tank design code, internal coating, insulation/heating, PVRV/EPRV, VRU/blanket interface, Kennilworth skim, instrumentation. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-067`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 518-524 |
| Test / inspection evidence | Material Test Reports / Certificates, ITP execution records, Inspection Release Certificate(s), hydrotest / leak-test packages for the tanks, internal coating application records (Devchem 253 floor/walls/roof), heat-trace and insulation acceptance records, and any vendor FAT records for skim systems and instrumentation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 (coating, insulation, heating, skim, PVRV); standard vendor-engineering deliverable pattern observed across PKG sister packages (ASSUMPTION — specific artifact IDs TBD until vendor document index issued) |
| Turnover evidence | Manufacturing Record Book / Vendor Data Book; pressure / leak-test packages; nameplate and registration records; SPIR; IOM (operation, maintenance, and inspection); commissioning energization records for heat tracing and instrumentation; pre-startup walk-down records. | ASSUMPTION based on standard tank-package turnover practice and the deliverable's stated "turnover evidence" artifact in `_CONTEXT.md`. |
| Physical-interface acceptance coverage | Interfaces marked `YES` for PKG-067 in `INTERFACE_REGISTER.csv`: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows `IFC-1CB18EBD35`, `IFC-44474541F7`, `IFC-C5A70E8F73`, `IFC-A172213C86`, `IFC-0152A5CE44`, `IFC-A3C5E09CBC`, `IFC-789528648B`, `IFC-E6F955CD2C`, `IFC-2815BE772E` |

## References

- `_Sources/26020-Package_Requirements.docx` — Heading 22, "Tanks, Sour Water (API 650) 4-25" (`26020-01-PT-19-005`) — location TBD at clause level; not directly accessible as Markdown. Decomposition rows summarize the relevant content.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §Produced Water (lines 502-524); §Atmospheric Tank and General Plant Spacing (lines 261-297); §Storage Tankage Summary (line 493).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row `DEL-067-06`.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` — row `PKG-067`.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` — PKG-067 rows.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv` — `ART-5AF4728A78`, `ART-E14BC1C993`.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local).
