# Specification — DEL-078-04 Vendor Engineered Equipment Package

> Normative requirements for the Pig Receivers (Inlet) 4-25 vendor-engineered equipment package. Requirements without explicit source backing are labelled `ASSUMPTION` or `TBD`.

## 1. Scope

### 1.1 Covered
The Package Vendor's engineering, design, fabrication/supply, and the physical equipment package for three (3) identical 610 mm OD (24") plant-inlet pig receivers, each on a dedicated structural steel non-enclosed skid, with associated HIPPS package.
Source: `PACKAGE_REGISTER.csv` row 78; `_CONTEXT.md`; `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.

### 1.2 Excluded
- Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (owned by EPC Integrator). Source: `PACKAGE_REGISTER.csv` row 78.
- Vendor document register, submittals, and turnover records (tracked under `DEL-078-05_vendor-document-turnover-package`).
- EPC review and acceptance evidence (tracked under `DEL-078-06_epc-vendor-package-review-and-acceptance`).
- No further package-specific exclusions stated in source materials (`PACKAGE_REGISTER.csv` row 78: "TBD; no package-specific exclusions stated in source materials").

## 2. Requirements

### 2.1 Equipment Quantity and Identity
- REQ-01: The package shall comprise three (3) identical pig receivers tagged PR-1010-1, PR-1020-1, PR-1030-1. Source: `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` Line-Item row 61.

### 2.2 Mechanical Configuration
- REQ-02: Each pig receiver shall be 610 mm OD (24 in.) nominal. Source: `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.
- REQ-03: Each receiver shall be mounted on a dedicated structural steel non-enclosed skid. Source: `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.
- REQ-04: Skid-mounted isolation valves or ESDVs upstream of each pig receiver shall be full port for pigging. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.
- REQ-05: Barred tees shall be provided to prevent pigs from entering facility piping. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.

### 2.3 Safety Instrumentation
- REQ-06: A HIPPS package shall be provided with the pig receiver skids. Source: `PACKAGE_REGISTER.csv` row 78.
- REQ-07: A full-port piggable ESDV with position transmitters shall be provided on the pig receiver inlet skid. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809.
- REQ-08: HIPPS architecture, independent pressure control/shutdown configuration, and shutdown setpoints shall be confirmed during detailed engineering. **TBD** — Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` §Assumptions/TBDs.
- REQ-09: Shutdown setpoints shall account for the high-pressure gas volume between plant inlet ESDVs and inlet separator inlet PCVs. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809.

### 2.4 Auxiliary Services
- REQ-10: Each receiver shall include a low-pressure fuel gas connection downstream of a manual isolation valve for sweet-gas purge of the receiver before opening. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.
- REQ-11: Each receiver vent shall route to the HP flare system. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.

### 2.5 Design Conditions (carried forward from facility basis)
- REQ-12: The package design shall be consistent with the inlet pipeline MAWP of 1440 psig (TBC). Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` §Assumptions/TBDs.
- REQ-13: The package shall be compatible with sour wet natural gas service from multiple upstream sources, including 03-25 high-pressure wet sour gas at 4,482–5,516 kPag (650–800 psig). Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` §Inlet Pipeline.
- REQ-14: Receiver vessel design pressure, design temperature, and materials of construction shall be specified by the Package Vendor consistent with REQ-12 and REQ-13. **TBD** values — not stated in accessible sources (`location TBD`).

### 2.6 Interfaces
- REQ-15: The package shall be engineered to accommodate the declared PKG-078 interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Pipeline / Pigging. Source: `PACKAGE_REGISTER.csv` row 78.
- REQ-16: Vendor-supplied I&C shall integrate with the EPC Integrator's balance-of-plant control system (interface detail per EPC handoff). Source: `PACKAGE_REGISTER.csv` row 78 (ASSUMPTION on protocol; not specified in accessible sources).

## 3. Standards

| Standard | Applicability | Status |
|---|---|---|
| 26020-Package_Requirements.docx package heading 31 | Project-internal package requirements for PKG-078 | `location TBD` — .docx referenced by decomposition row, not locally rendered |
| Project DBM (4-25 Deepcut) | Facility design basis; informs service conditions, isolation, HIPPS driver, purge, and vent routing | `DBM-Deepcut/4-25_Deepcut_DBM.md` (locally accessible) |
| ASME pressure-vessel and piping codes; CSA/provincial requirements applicable to Alberta sour service | **ASSUMPTION** — likely applicable but not enumerated in accessible source slices | `location TBD` |
| RFQ source basis `26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` | Vendor scope and procurement | `location TBD` — RFQ not locally accessible |

## 4. Verification

| Requirement | Verification Approach |
|---|---|
| REQ-01 (qty, tags) | Vendor BOM / nameplates checked against PKG-078 register row. |
| REQ-02 (size) | Vendor mechanical datasheets and fabrication drawings. |
| REQ-03 (skids) | Vendor structural drawings and shop inspection. |
| REQ-04, REQ-07 (full-port ESDVs) | Valve datasheets and trim verification; FAT. |
| REQ-05 (barred tees) | P&ID and isometric review; visual inspection at fabrication. |
| REQ-06, REQ-08, REQ-09 (HIPPS) | SIL verification report and HIPPS FAT; final setpoints captured during detailed engineering. |
| REQ-10 (purge), REQ-11 (HP flare) | P&ID review; tie-in punchlist. |
| REQ-12, REQ-13 (service conditions) | Vendor design report; calculations cross-checked against DBM. |
| REQ-14 (vessel design) | Vendor pressure-vessel U-stamp / equivalent documentation; mill test certificates. |
| REQ-15 (interfaces) | EPC interface matrix sign-off (see `DEL-078-06`). |
| REQ-16 (I&C integration) | Loop checks during commissioning. |

## 5. Documentation

- Vendor engineered physical equipment package (three receiver skids with HIPPS). Source: `_CONTEXT.md` Anticipated Artifacts.
- Vendor package design basis and datasheet set. Source: `_CONTEXT.md` Anticipated Artifacts.
- Mechanical drawings, P&IDs, datasheets, pressure-vessel documentation, HIPPS SIL report, FAT records, and turnover documentation (forwarded to `DEL-078-05`). **ASSUMPTION** on the precise document list pending the RFQ scope.
