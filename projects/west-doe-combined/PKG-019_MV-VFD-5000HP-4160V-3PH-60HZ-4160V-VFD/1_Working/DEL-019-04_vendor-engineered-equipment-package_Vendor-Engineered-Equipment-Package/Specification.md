# Specification — DEL-019-04 Vendor Engineered Equipment Package

Normative requirements for the vendor-supplied MV VFD engineered equipment package under PKG-019.

## Scope

### In scope

- Package Vendor engineering, design, fabrication/supply, and physical equipment for the MV VFD package described in Workbook Packages row 21 (PKG-019).
- Vendor package design basis and datasheet set, developed from `DEL-019-01_scope-of-work` and `DEL-019-02_package-datasheet`.
- Application: starting VFDs for inlet compressor motors `KM-2150` and `KM-2250` per SCA-001 VE #34 (DBM §326, §756).

### Out of scope

- Facility-level integration, interface execution, tie-ins, constructability, and procurement/construction coordination (owned by EPC Integrator; see `PKG-019` ResponsibilityNarrative).
- Vendor document turnover register (`DEL-019-05_vendor-document-turnover-package`).
- EPC review and acceptance of the vendor package (`DEL-019-06_epc-vendor-package-review-and-acceptance`).
- Detailed harmonic / reactive-power study (to be performed under detailed electrical studies per DBM §756).

## Requirements

| ReqID | Requirement | Source / basis |
|---|---|---|
| REQ-019-04-01 | The vendor package SHALL be engineered, designed, and supplied as the production unit defined by `DEL-019-04` and PKG-019. | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-019-04` |
| REQ-019-04-02 | The vendor package SHALL function as a starting VFD for the inlet compressor motors `KM-2150` and `KM-2250`. | DBM §326, §756 |
| REQ-019-04-03 | The vendor package SHALL interface with the 4160V MCC serving the 4000V motors (line side). | DBM §752, §754 |
| REQ-019-04-04 | The vendor package SHALL be compatible with the driven motor basis (NEMA MG1, 4,000 V nominal, 3-phase, 60 Hz, 5,200 hp / 3,878 kW, continuous inverter-duty, Class F insulation / Class B rise, ~891 rpm). Final ratings TBD per vendor design and Conflict-Table resolution. | DBM §324, §523, §533; ASSUMPTION pending Conflict Table resolution |
| REQ-019-04-05 | Soft-start equipment SHALL NOT be substituted for the starting VFD (SCA-001 VE #34). | DBM §326, §756 |
| REQ-019-04-06 | The vendor package SHALL support communications to the plant PLC central control panel via the EtherNet path provided by the 4160V MCC. | DBM §754 |
| REQ-019-04-07 | The vendor package SHALL provide engineering provisions for the package-level interface types declared for PKG-019: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` (InterfaceTypes) |
| REQ-019-04-08 | The vendor package SHALL include the vendor package design basis and a datasheet set as deliverable artifacts. | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-019-04` (anticipated artifacts) |
| REQ-019-04-09 | Final VFD sizing SHALL be performed as an electrical detailed-design activity, with vendor design substantiated against accepted load and motor data. | DBM §326 (ASSUMPTION: scope allocation to vendor follows from package responsibility narrative) |
| REQ-019-04-10 | Harmonic and reactive-power mitigation requirements SHALL be determined by the detailed electrical studies (SCA-001 VE #37 removes capacitor banks from the synchronous bus on `MCC-8200` where VFDs are present); vendor package SHALL accept the resulting mitigation requirements as design inputs. | DBM §756 |
| REQ-019-04-11 | Nominal package rating (HP / motor voltage) discrepancy between workbook title (5000 HP / 4160 V) and DBM motor basis (5,200 HP / 4,000 V) SHALL be resolved by human ruling before vendor design freeze. | Conflict Table in `Guidance.md` (HRR-019-04-001) |

## Standards

| Standard / authority | Applicability | Location |
|---|---|---|
| NEMA MG1 | Motor basis (driven equipment); informs VFD-motor compatibility | DBM §324, §533 |
| SCA-001 VE #34 | Governs starting-VFD basis for KM-2150 / KM-2250 | DBM §326, §756 |
| SCA-001 VE #37 | Removes capacitor banks from synchronous bus on `MCC-8200` where VFDs are present | DBM §756 |
| IEEE 519 (harmonic distortion limits) | Likely applicable to MV VFD harmonic mitigation | ASSUMPTION: likely applicable; location TBD (not in accessible source slices) |
| IEC 61800-series / NEMA ICS 7 (adjustable-speed drives) | Likely applicable to MV VFD design | ASSUMPTION: likely applicable; location TBD |
| Workbook reference `26020-02-30-009` | Package code in workbook row 21 | Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` |

## Verification

| ReqID | Verification approach |
|---|---|
| REQ-019-04-01 | Vendor design documentation review against `DEL-019-01` and `DEL-019-02` (executed under `DEL-019-06`). |
| REQ-019-04-02 | Functional design review confirming starting-VFD operation for KM-2150 / KM-2250. |
| REQ-019-04-03 | Line-side interface review against 4160V MCC interface drawings. |
| REQ-019-04-04 | Motor-drive compatibility review (vendor calculation / certification) against the accepted motor basis (post Conflict Table ruling). |
| REQ-019-04-05 | Design review confirming no soft-start substitution. |
| REQ-019-04-06 | EtherNet communications test against plant PLC central control panel (factory or site, per FAT/SAT plan). |
| REQ-019-04-07 | Interface checklist review across the six declared interface types. |
| REQ-019-04-08 | Document register check confirming design basis and datasheet set are present in `DEL-019-05`. |
| REQ-019-04-09 | Review of vendor VFD sizing calculations and electrical detailed-design inputs. |
| REQ-019-04-10 | Confirmation that harmonic / reactive mitigation results from detailed electrical studies are incorporated into vendor design. |
| REQ-019-04-11 | Human ruling on HRR-019-04-001 recorded before vendor design freeze. |

## Documentation

Required output artifacts (per Gate 7 anticipated artifacts):

- Vendor engineered physical equipment package (the production unit itself).
- Vendor package design basis.
- Vendor package datasheet set.

Cross-referenced sibling deliverables (not produced here):

- `DEL-019-01_scope-of-work` — EPC scope basis (upstream input).
- `DEL-019-02_package-datasheet` — EPC technical handoff (upstream input).
- `DEL-019-05_vendor-document-turnover-package` — vendor document register and submittals (downstream).
- `DEL-019-06_epc-vendor-package-review-and-acceptance` — EPC review/acceptance (downstream).
