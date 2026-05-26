# Datasheet — DEL-071-05 Vendor Document Turnover Package (PKG-071 Fuel Gas Skid 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-071-05_vendor-document-turnover-package | `_CONTEXT.md` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| Parent Package | PKG-071 Fuel Gas Skid 4-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | Vendor Document Turnover | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation), with EPC Integrator interface/integration review | `_CONTEXT.md` |
| Covered Scope Items | SOW-0099, SOW-0100, SOW-0101, SOW-0102 | `_CONTEXT.md` |
| Supported Objectives (ASSUMPTION, package heuristic) | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC |
| Source Decomposition Row | Workbook Packages row 61 | `_CONTEXT.md` (cited; binary source not locally readable) |
| Source Requirements Heading | `26020-Package_Requirements.docx` heading 25 | `_CONTEXT.md` (cited; binary source not locally readable) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Equipment package covered | Low-pressure fuel gas system / fuel gas skid located at 04-25 | DBM-Deepcut L1839-L1841 |
| Key equipment items expected in turnover (representative) | LP fuel gas scrubber V-3210-1, LP fuel gas heater (electric resistance, SCR-controlled), main fuel gas regulators (2 x 100 % spared), emergency-generator start-gas regulators (quick-acting), buyback fuel gas regulators (independent from plant main regulators) | DBM-Deepcut L1864-L1878 |
| Turnover artifact classes (expected) | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records | `_CONTEXT.md` Anticipated Artifacts |
| Document control numbering scheme | TBD | not locally specified |
| Required revision levels at turnover (As-Built, Certified, etc.) | TBD | not locally specified |
| Native + PDF deliverable requirement | TBD | not locally specified |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Fuel gas system service location | 04-25 (shared utility with 03-25 coordination) | DBM-Deepcut L1841 |
| Operating regime relevant to vendor documents | J-T mode and Expander mode supply pressures, flows, heating values, and hydrocarbon dewpoints per Fuel Gas Design Values table | DBM-Deepcut L1843-L1862 |
| Sour service exposure | Sweet gas purge required to sweep H2S/mercaptan from corrosive or H2S-rich equipment; vendor materials documentation must address sour-service compatibility where applicable | DBM-Deepcut L1899 |
| Emergency-generator fuel gas supply pressure ceiling | < 66 psig under normal operation (general-purpose classification compliance) | DBM-Deepcut L1870 |
| Turnover schedule milestones (MC, Pre-Comm, Comm, Hand-Over) | TBD | not locally specified |

## Construction

| Item | Value | Source |
|---|---|---|
| Vendor turnover package format | TBD (paper/digital index; folder structure) | not locally specified |
| Required document classes (representative; ASSUMPTION pending vendor scope) | Equipment data sheets, fabrication drawings, P&IDs (vendor), GA / arrangement drawings, BOMs, MOC (material test reports), welding records (WPS/PQR/welder qualifications, NDE), pressure-test records, electrical schematics, instrument index and loop diagrams, calibration certificates, surface-prep / painting records, lifting plans, spare parts list, recommended commissioning spares, O&M manuals, vendor IOM, training materials, factory acceptance test (FAT) records, site acceptance test (SAT) records, preservation records | ASSUMPTION — typical vendor turnover scope; vendor-master document register not locally accessible |
| Code/standard packages typically included (ASSUMPTION) | ASME (pressure vessel U-stamp, B31.3), CRN (BC for pressure equipment), CSA electrical, area classification | ASSUMPTION — drawn from analogous fuel-gas-skid practice and DBM Section 13 context; not from source slice for this deliverable |

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (decomposition basis and source pointers)
- `_DEPENDENCIES.md` (no declared upstream/downstream)
- Decomposition snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Locally accessible source: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Fuel Gas Basis, L1839-L1905
- Cited but not locally readable (binary):
  - `26020-Package_Requirements.docx` heading 25 — location TBD inside binary
  - `26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 61
