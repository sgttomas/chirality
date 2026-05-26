# Datasheet: DEL-046-05 — Vendor Document Turnover Package (PKG-046 Acid Gas Compressors)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-046-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| Parent Package | `PKG-046` — Acid Gas Compressors | `_CONTEXT.md`; PROJECT_DECOMP/PACKAGE_REGISTER.csv row PKG-046 |
| Workbook Row | 48 | PACKAGE_REGISTER.csv row PKG-046 (location TBD inside 26020-Packages_Interfaces_4_export.xlsx) |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Deliverable Type | Vendor Document Turnover | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation); EPC Integrator (interface/integration review) | `_CONTEXT.md` |
| Tag (package) | `26020-01-12-001` / `26020-01-PT-12-001 - Acid Gas Compressor` | PACKAGE_REGISTER.csv row PKG-046 |
| Equipment instances covered | Acid Gas Compressors Unit 1 (K-5450-1) and Unit 2 (V-5530-1) | DBM-Deepcut/4-25_Deepcut_DBM.md §"Acid Gas Compressors" rows (lines 2529, 2572-2573) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Number of compressor packages in scope | 2 (two identical packages, each 100% of acid gas capacity) plus one spare compressor in detailed basis | DBM-Deepcut line 878, 885, 994 |
| Driver type | Electric induction motor | DBM-Deepcut line 2198; PACKAGE_REGISTER PKG-046 narrative |
| Compression stages | 5 | DBM-Deepcut lines 1023, 1057 |
| Compressor model (vendor basis) | Ariel KBT/6 (detailed basis); KBK/6 referenced as TBC — final model **TBD** | DBM-Deepcut lines 1090, 2198 |
| Service | Acid gas (H2S + CO2) compression for acid gas injection (AGI) / disposal | PACKAGE_REGISTER PKG-046; DBM-Deepcut line 885 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Acid gas water content basis | Water-saturated from amine unit; dehydration recycle to 35-60 lb H2O/MMSCF if required | DBM-Deepcut line 988 |
| Stages 1-4 cooler outlet temperature | 110 deg F (43.33 deg C) | DBM-Deepcut line 1023 |
| Stage 5 cooler outlet temperature | 150 deg F (65.56 deg C) | DBM-Deepcut line 1023 |
| Discharge pressure (normal vs. design) | 1,200 psig normal vs. 1,500 psig design-discharge reference — final pressure **TBD** | DBM-Deepcut line 1091 |
| Pipeline NPS (assumed) | 3 in. NPS (ASSUMPTION per Tourmaline; final sizing TBD) | DBM-Deepcut line 1061 |

## Construction (Vendor Document Set — Anticipated Composition)

The turnover package shall comprise a controlled vendor document register (VDR) and the associated submittal artifacts and certified records. The following categories are anticipated; the authoritative VDR line items are defined in `26020-Package_Requirements.docx` package heading 1 (location TBD — file not text-accessible).

| Category | Representative Artifacts | Source |
|---|---|---|
| Vendor Document Register (VDR) | Master VDR with document numbers, revisions, status, transmittal dates | `_CONTEXT.md` Anticipated Artifacts; 26020-Package_Requirements.docx (location TBD) |
| Engineering submittals | Datasheets, GA drawings, P&IDs, electrical schematics, instrument index, cause-and-effect | DBM-Comp_and_Liquids line 617 ("vendor document registers", "datasheets", "cause-and-effect inputs") |
| Quality / inspection records | Material certs, NDE records, hydrotest records, ITP sign-offs | TBD — confirm against 26020-Package_Requirements.docx |
| Operations & maintenance | IOM manuals, lube/seal lists, spare parts lists | TBD — confirm against 26020-Package_Requirements.docx |
| Certifications | Code stamps (ASME / CRN), PED / CSA, electrical area classification certs | TBD — confirm against 26020-Package_Requirements.docx |
| Turnover records | Transmittals, punch lists, mechanical completion certificate, handover sign-offs | TBD — confirm against 26020-Package_Requirements.docx |

The full numeric VDR line count, required revisions (e.g., IFA / IFR / IFC / AB), and submittal schedule are **TBD** pending access to the .docx source slice.

## References

- `_REFERENCES.md` — authoritative reference index
- PROJECT_DECOMP GATE-07 snapshot:
  - `DELIVERABLE_REGISTER.csv` row `DEL-046-05_vendor-document-turnover-package`
  - `PACKAGE_REGISTER.csv` row `PKG-046`
- DBM-Deepcut: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Acid Gas Compressor design basis sections)
- DBM-Comp_and_Liquids: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (vendor document register expectation)
- Package Requirements document (not locally text-accessible): `_Sources/26020-Package_Requirements.docx` package heading 1 — **location TBD**
- Workbook (not locally text-accessible): `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 48 — **location TBD**
