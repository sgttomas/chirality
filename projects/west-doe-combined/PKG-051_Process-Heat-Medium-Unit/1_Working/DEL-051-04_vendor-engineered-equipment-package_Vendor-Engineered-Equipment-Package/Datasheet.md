# Datasheet — DEL-051-04 Vendor Engineered Equipment Package (PKG-051 Process Heat Medium Unit)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-051-04_vendor-engineered-equipment-package |
| Name | Vendor Engineered Equipment Package |
| Parent Package | PKG-051 — Process Heat Medium Unit |
| Workbook Package Row | 79 (`SourcePath`: 26020-Packages_Interfaces_4_export.xlsx; `SectionRef`: Packages row 79) |
| Package Source Heading | 26020-Package_Requirements.docx package heading 6 |
| Word Source Basis | Bid Docs/Budgetary/26020-01-PT-15-001_Heat Medium System.docx (referenced by PACKAGE_REGISTER; not locally accessed) |
| Tag (per PACKAGE_REGISTER) | 26020-01-PT-15-001 — Process Heat Medium Unit |
| Discipline | Mechanical |
| WBS | 01 |
| Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering / design / fabrication / supply / physical equipment) with EPC Integrator integration review |
| Decomposition Snapshot | _Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24 |

## Attributes

The package, as scoped by `26020-Package_Requirements.docx` heading 6 (Workbook source basis), comprises two modules:

| Module | Major Equipment (per workbook source) |
|---|---|
| Supply Pump Module | One expansion tank; three (3) heat medium pumps (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Basic scope, via SCOPE_LEDGER SOW-0166) |
| Medium Heater Module | One medium heater; one heater blower; one air intake pre-heater (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Basic scope, via SCOPE_LEDGER SOW-0166) |

CONFLICT: A later facility-level basis document (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Heat Medium Basis", lines 1945-2002) retires the hot/cold loop segregation and consolidates to a single unified loop with a single pump module and single expansion tank. See Conflict Table in `Guidance.md`. The workbook-source attributes above are retained as the EPC package scope basis for the Vendor Package Production Unit; the unified-loop basis is captured for human ruling on whether the vendor scope is updated.

## Conditions (workbook source basis — `SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6, via SCOPE_LEDGER SOW-0167 / SOW-0168)

| Parameter | Value |
|---|---|
| Heat medium fluid | Petro Canada Peterotherm |
| Assumed start-up temperature | 20 deg C (68 deg F) |
| Maximum bulk temperature | 260 deg C (500 deg F) |
| Heat medium pump type | Single-stage vertical inline, 3 x 66% |
| Heat medium pump design pressure | 2413 kPag (350 psig) |
| Heat medium pump operating pressure | 695 kPag (100 psig) |
| Expansion tank arrangement | Horizontal; size & capacity to be advised by vendor |
| Expansion tank fill fraction at 274 deg C | Maximum 85% |
| Expansion tank operating pressure | 125 to 240 kPag (18 to 23 psig) — depends on heat medium NPSHR |
| Expansion tank operating temperature | 20 to 260 deg C |
| Pumps design temperature | 274 deg C |
| Total heat medium supply (approximate) | 151.6 m3/day |

ASSUMPTION: Expansion tank operating pressure range of "125 to 240 Kapg (18 to 23 Psig)" is recorded as-is from SOW-0167 transcription. The numeric and unit consistency (kPag vs psig conversion) is TBD pending vendor confirmation.

## Construction

- Modular skid-mounted package: Supply Pump Module skid + Medium Heater Module skid. (ASSUMPTION: modular skid construction is conventional for vendor packages of this type; not explicitly stated in the accessible source slice.)
- Heater air-side equipment includes a heater blower and an air intake pre-heater (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Basic scope, via SCOPE_LEDGER SOW-0166).
- Heat medium loop arrangement per workbook source: hot loop and cold loop, with mix to deliver optimum supply (SOW-0166). CONFLICT vs DBM-Deepcut single unified loop — see Guidance Conflict Table.
- Material, code, area-classification and structural specifications: TBD — not specified in the accessible source slice for PKG-051.

## References

- `_REFERENCES.md` (this deliverable folder)
- 26020-Package_Requirements.docx — package heading 6 (`_Sources/26020-Package_Requirements.docx`; not text-extracted locally; content reached via SCOPE_LEDGER SOW-0165..0168 extractions)
- 26020-Packages_Interfaces_4_export.xlsx — Packages row 79 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`)
- DBM-Deepcut 4-25 Deepcut DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`), §"Heat Medium Basis" lines 1945-2002 — referenced in CONFLICT entries
- Bid Docs/Budgetary/26020-01-PT-15-001_Heat Medium System.docx — Word Source Basis per PACKAGE_REGISTER (location TBD; not locally accessed)
- Decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER, PACKAGE_REGISTER, SCOPE_LEDGER)
