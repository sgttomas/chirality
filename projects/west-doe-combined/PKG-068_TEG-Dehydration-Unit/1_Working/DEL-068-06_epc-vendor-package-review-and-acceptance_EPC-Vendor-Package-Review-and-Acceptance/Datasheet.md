# Datasheet — DEL-068-06 EPC Vendor Package Review and Acceptance (TEG Dehydration Unit)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-068-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-068` |
| PackageName | TEG Dehydration Unit |
| Subject Package | TEG Dehydration Unit, one-by-100 percent sour-gas TEG package downstream of inlet compression (`SourcePath: _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SectionRef: SEC-05 — TEG Dehydration Basis / TEG Package Equipment`; also `_Sources/26020-Package_Requirements.docx` package heading 23, `location TBD` at sub-heading level — binary not directly readable in this run) |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | Review and acceptance evidence pack for the Package Vendor production unit (`DEL-068-04`) and the Vendor Document Turnover (`DEL-068-05`) against EPC anchor deliverables (`DEL-068-01` SOW, `DEL-068-02` Package Datasheet, `DEL-068-03` Construction Work Package). | `DELIVERABLE_REGISTER.csv` row `DEL-068-06`; `_CONTEXT.md` |
| Acceptance subject | The TEG dehydration package supplied by the Package Vendor, including all major equipment enumerated under SEC-05 "TEG Package Equipment" (inlet filter coalescer, contactor, level pot, cooler, flash drum, solids filters, charcoal filter, lean/rich exchanger, rich TEG solids filter, TEG pumps, still column, stripping column, reflux condenser, reboiler, surge drum, regen cooler, regen overhead scrubber, regen overhead pumps, makeup tank, makeup pump) and the package's process, utility, and relief interfaces. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 "TEG Package Equipment"; `_Sources/26020-Package_Requirements.docx` package heading 23 (location TBD) |
| Covered SOW IDs | `SOW-0237`, `SOW-0238`, `SOW-0239`, `SOW-0240` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic via `OBJECTIVE_SCOPE_MAP.csv` rows for PKG-068 / SOW-0237..0240) | `OBJECTIVE_SCOPE_MAP.csv`; `_CONTEXT.md` |
| Package configuration | One-by-100 percent TEG unit downstream of inlet compression, treating compressed sour gas before export to 04-25. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 "TEG Dehydration Basis" |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service / facility | Sour-gas dehydration at the 03-25 Compressor Station and Liquids Hub; treated gas exported to 04-25 Deep Cut Gas Plant inlet system. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` facility narrative; SEC-05 "TEG Dehydration Basis" |
| Upstream tie-in (process gas) | Second-stage compressor discharge at 800 psig under SCA-002 basis. | SEC-05 "Compression Design Conditions" |
| Downstream tie-in (treated gas) | Compressed sour gas export to 04-25 inlet gathering system. | SEC-05 "TEG Dehydration Basis" |
| Flash-gas routing | Pressure-regulated to 04-25 SOC first-stage suction under current SCA basis. | SEC-05 "TEG Package Equipment" |
| Contactor blowdown | Automated to HP flare. | SEC-05 "TEG Dehydration Basis" |
| Regeneration relief routing | TEG regeneration overhead routes to LP flare via LP KO drum `V-3900-2`. | SEC-08 utility narrative; SEC-05 |
| Fuel-gas service | LP fuel gas serves TEG stripping (reboiler / stripping column). | "Utility Integration Basis" |
| Hydrocarbon liquids (flash drum) | Manual drain to produced-water drain. | SEC-05 "TEG Package Equipment" |
| Makeup tank | Atmospheric, fuel-gas blanketed, heated/insulated, not connected to VRU. | SEC-05 "TEG Package Equipment" |
| Equipment tagging | Package and equipment tags (e.g., contactor, flash drum, surge drum, pumps) TBD — not enumerated in the SEC-05 source slice at tag level; located in vendor equipment list / GA drawings once submitted by the Package Vendor. | `26020-Package_Requirements.docx` heading 23 (location TBD); vendor equipment list (`MEC-002`/`MEC-005` typical) |
| Acceptance trigger states (upstream maturity) | `DEL-068-04` and `DEL-068-05` reach a maturity state acceptable for integration review. (ASSUMPTION — exact gating values TBD; `_DEPENDENCIES.md` declares no upstream edges as of PREPARATION.) | `_DEPENDENCIES.md`; ASSUMPTION |
| Design pressure / temperature / sizing values | TBD — not enumerated in `26020-Package_Requirements.docx` heading 23 (binary not readable in this run); located in vendor mechanical design basis and vessel data sheets once submitted by the Package Vendor. | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" — Static pressure equipment block (location TBD) |

## Construction

| Acceptance Artifact (per `_CONTEXT.md` / decomposition) | Description | Source |
|---|---|---|
| Vendor document review log | Reviewer-by-document register tracking the Vendor Document Index (`PRQ-009`, typical) and each enumerated vendor engineering deliverable for the TEG Dehydration Unit. | `_CONTEXT.md` Anticipated Artifacts; `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" (location TBD) |
| Package acceptance checklist | Pass/fail acceptance matrix mapped to SOW items `SOW-0237..0240`, the Package Datasheet (`DEL-068-02`), and Construction Work Package (`DEL-068-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Test / inspection evidence | Aggregated Material Test Reports / Certificates, ITP execution records, Inspection Release Certificate, and Equipment FAT / Performance Test reports (e.g., `MEC-022` for rotating equipment, including the TEG pumps and makeup pump). | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" — Core vendor documents and Core package engineering blocks (location TBD) |
| Turnover evidence | Manufacturing Record Book / Vendor Data Book, Hydrotest / Pressure Test Packages, Pressure Equipment Registration Package (typical `REG-022` for the package's coded vessels — contactor, flash drum, surge drum, regen overhead scrubber, still/stripping/reflux column shells where coded), SPIR, IOM, Logistics / Shipping Plan. | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" (location TBD); SEC-05 "TEG Package Equipment" |
| Physical-interface acceptance coverage | Interfaces typical for a packaged TEG unit and supported by the source set: Process Piping (sour-gas in/out, flash-gas, regen overhead); Relief / Flare / Vent (HP flare blowdown, LP flare regen); Drain / Containment (produced-water drain, TEG drain); Utilities (LP fuel gas, instrument air, electrical power); EHT / Insulation; Grounding / Bonding; I&C / Control Cabling (BPCS replication of package PLC values); Maintenance Access; Structural / Foundations / Supports. Authoritative interface row for PKG-068 is `26020-Packages_Interfaces_4_export.xlsx` Packages row 97 (column-level interface flags `location TBD` — binary not readable in this run; per-interface `Yes/No` map to be confirmed at acceptance). | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 97 (location TBD); SEC-05 / SEC-07 / SEC-08 narrative; "Control System Architecture" / "Package and Third-Party Interfaces" |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-05 ("Inlet Compression and Sour-Gas Dehydration", "TEG Dehydration Basis", "TEG Package Equipment"); "Utility Integration Basis"; "Control System Architecture / Package and Third-Party Interfaces"; "Equipment Count Table"
- `_Sources/26020-Package_Requirements.docx` — package heading 23 (TEG Dehydration Unit); location TBD at sub-heading level (binary not directly readable in this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Packages row 97 (interface evidence; location TBD at column level — binary not readable in this run)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row `DEL-068-06`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_SCOPE_MAP.csv` — PKG-068 rows
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
