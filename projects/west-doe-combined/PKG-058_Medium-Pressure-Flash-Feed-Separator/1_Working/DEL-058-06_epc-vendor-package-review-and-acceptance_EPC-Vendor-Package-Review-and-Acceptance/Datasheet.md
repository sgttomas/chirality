# Datasheet — DEL-058-06 EPC Vendor Package Review and Acceptance

> Descriptive datasheet for the EPC Integrator's review-and-acceptance evidence deliverable for PKG-058 Medium Pressure Flash Feed Separator (MPFF). Values cite the locally accessible 04-25 Deepcut DBM source slices and the decomposition register. Where the source carries `TBD/TBC`, this datasheet preserves those markers.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-058-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | `PKG-058` | `_CONTEXT.md` |
| PackageName | Medium Pressure Flash Feed Separator | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Subject Equipment Tags | V-7110-1, V-7310-1 (MPFF separators, x2); E-7120-1, E-7320-1 (MPFF HCL heater bundles, x2) | DBM-Deepcut `4-25_Deepcut_DBM.md` equipment register rows 52-53; §"MPFF Operating and Capacity Basis"; Heat Medium Users table |
| Modules | 710-1 Medium Pressure Flash Feed Module; 730-1 Medium Pressure Flash Feed Module (shop-assembled) | DBM-Deepcut `4-25_Deepcut_DBM.md` module table |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Decomposition Snapshot | `GATE-07_Final_Published_2026-05-24` | `_REFERENCES.md` |
| Source Reference (decomposition row) | Workbook Packages row 71; `26020-Package_Requirements.docx` package heading 13 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | Review-and-acceptance evidence pack for the Package Vendor production unit (`DEL-058-04`) and the Vendor Document Turnover (`DEL-058-05`), checked against EPC anchor deliverables `DEL-058-01` (Scope of Work), `DEL-058-02` (Package Datasheet), and `DEL-058-03` (Construction Work Package). | `DELIVERABLE_REGISTER.csv` row `DEL-058-06`; `_CONTEXT.md` |
| Acceptance subject | Two MPFF separators (V-7110-1, V-7310-1) and two MPFF HCL heater bundles (E-7120-1, E-7320-1), shop-assembled within modules 710-1 and 730-1 with self-framing enclosures. | DBM-Deepcut §"MPFF Operating and Capacity Basis"; equipment register rows 52-53; module table |
| Covered SOW IDs | `SOW-0139`, `SOW-0140`, `SOW-0141`, `SOW-0142` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic applied; not deliverable-ID-explicit) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; objective association mode `PACKAGE_HEURISTIC` |
| Sparing basis to be verified | 2 x 100% normal; no sparing for off-design line-pack maximum (both MPFF and stabilizer trains required) | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" |
| Train coupling to be verified | One MPFF assigned to one stabilizer; MPFF out of service if its stabilizer is out of service | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" |
| Heater bundle disposition status | Open — retention, de-rate, or removal pending thermal re-simulation; tube-sheet seal-weld requirements TBC; vessel nozzle provisions to be preserved until disposition confirmed | DBM-Deepcut §"MPFF Operating and Capacity Basis" |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service / location | 4-25 West Doe Deepcut MPFF service, between inlet separator liquid outlet and downstream stabilizer flash/feed separator. | DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"MPFF and Stabilizer Train Relationship" |
| Operating pressure (each MPFF) | 1724 kPag expected normal and design; low and expected-high values TBD. | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Design operating temperature (each MPFF) | 40 deg C (ASSUMPTION pending detailed engineering confirmation; post-HEX MPFF inlet temperatures TBD/TBC) | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Winter design two-phase inlet (per separator) | 12.91 MMSCFD design and maximum; expected normal 6.681 MMSCFD | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Winter liquid inlet (per separator) | 19.58 m3/h design and maximum; expected normal <15.3 m3/h | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Winter vapour inlet (per separator) | 4.143 MMSCFD design and maximum; expected normal <1.151 MMSCFD | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Summer inlet basis | Total two-phase, liquid, and vapour values "Minimal" at design and maximum cases; zero at low/expected-normal | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Overhead routing | Pressure-regulated to SOC third-stage suction | DBM-Deepcut §"MPFF Operating and Capacity Basis"; SOC source capacity table (V-7110-1 / V-7310-1 → SOC stage 3) |
| Heater bundle heat-medium duty (each E-7120-1 / E-7320-1) | 762 kW (2.6 MM BTU/h); supply 118 deg C / 245 deg F; return 80 deg C / 175 deg F | DBM-Deepcut §"Heat Medium Users and Duties" |
| Acceptance trigger states (upstream maturity) | `DEL-058-04` (Vendor Engineered Equipment Package) and `DEL-058-05` (Vendor Document Turnover Package) reach a maturity state acceptable for integration review. (ASSUMPTION — exact gating values TBD; `_DEPENDENCIES.md` declares no formal upstream edges as of PREPARATION.) | `_DEPENDENCIES.md`; ASSUMPTION |
| Vessel design pressure / temperature / sizing | TBD — not enumerated in accessible source slices at MPFF level; located in vendor mechanical design basis and Pressure Vessel Data Sheet once submitted by the Package Vendor. | DBM-Deepcut §"MPFF Operating and Capacity Basis"; location TBD in source |
| Materials of construction | TBD — not stated at MPFF level in accessible source. | location TBD |

## Construction

| Acceptance Artifact (per `_CONTEXT.md` / decomposition) | Description | Source |
|---|---|---|
| Vendor document review log | Reviewer-by-document register tracking each enumerated vendor engineering deliverable for V-7110-1, V-7310-1, E-7120-1, and E-7320-1 within modules 710-1 and 730-1. | `_CONTEXT.md` Anticipated Artifacts; `26020-Package_Requirements.docx` package heading 13 (location TBD at section level — binary source) |
| Package acceptance checklist | Pass/fail matrix mapped to SOW items `SOW-0139..0142`, the Package Datasheet (`DEL-058-02`), and Construction Work Package (`DEL-058-03`); includes Mistex demister presence, ≥10-minute liquid residence between weir and NLL-interface, automated blowdown valve presence, LP fuel-gas purge configuration, and methanol injection safeguard. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Test / inspection evidence | Aggregated Material Test Reports / Certificates, ITP execution records, Inspection Release Certificate, and FAT records for the MPFF vessels, heater bundles (if retained), and ancillary instrumentation. | `26020-Package_Requirements.docx` package heading 13 (location TBD at section level — binary source); aligned with the EPC Integrator review-and-acceptance evidence pattern in `DELIVERABLE_REGISTER.csv` |
| Turnover evidence | Manufacturing Record Book / Vendor Data Book, Hydrotest / Pressure Test Packages, Pressure Equipment Registration Package, SPIR, and Mechanical Equipment IOM. (ASSUMPTION — artifact set mirrors typical EPC vendor package turnover; exact list in `26020-Package_Requirements.docx` heading 13 binary source, location TBD.) | `_CONTEXT.md`; ASSUMPTION |
| Physical-interface acceptance coverage | Interfaces to be verified at acceptance include process piping (inlet from inlet-separator liquid outlet header, overhead to SOC third-stage suction, liquid bottoms to stabilizer flash/feed, LP fuel-gas purge, methanol injection), relief / flare / blowdown (automated blowdown valve to HP flare — ASSUMPTION on destination), heat medium supply/return to E-7120-1 / E-7320-1, drains/containment, electrical power and EHT, grounding/bonding, I&C control cabling, maintenance access, and structural / foundations / supports. | DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"Heat Medium Users and Duties"; `26020-Packages_Interfaces_4_export.xlsx` package row for PKG-058 (location TBD at column level — binary source) |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"MPFF Operating and Capacity Basis"; §"MPFF and Stabilizer Train Relationship"; equipment register rows 52-53; module table; Heat Medium Users and Duties table
- `_Sources/26020-Package_Requirements.docx` — package heading 13 (binary source; section-level location TBD)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — package row for PKG-058 (interface evidence; column-level location TBD)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- Sibling deliverable for cross-reference (not authoritative): `../DEL-058-02_package-datasheet_Package-Datasheet/Datasheet.md`
