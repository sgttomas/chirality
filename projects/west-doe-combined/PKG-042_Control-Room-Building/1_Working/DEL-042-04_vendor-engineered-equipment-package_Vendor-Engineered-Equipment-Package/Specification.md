# Specification — DEL-042-04 Vendor Engineered Equipment Package

Normative requirements for the vendor-supplied Control Room Building engineered equipment package under PKG-042.

## Scope

### In scope

- Package Vendor engineering, design, fabrication/supply, and physical equipment for the Control Room Building described in Workbook Packages row 44 (PKG-042; `26020-03-39-010`).
- Vendor package design basis and datasheet set, developed from `DEL-042-01_scope-of-work` and `DEL-042-02_package-datasheet`.
- Provisions for hosting the operations control-room environment, including the primary control-system server host location (DBM §796), operator and engineering workstations, and core network switches (DBM §3141, §3119).
- Engineering provisions for the eleven PKG-042 InterfaceTypes (see Requirements).

### Out of scope

- Facility-level integration, interface execution, tie-ins, constructability, and procurement/construction coordination (owned by EPC Integrator; see `PKG-042` ResponsibilityModel).
- Construction work package execution (`DEL-042-03_construction-work-package`).
- Vendor document turnover register (`DEL-042-05_vendor-document-turnover-package`).
- EPC review and acceptance of the vendor package (`DEL-042-06_epc-vendor-package-review-and-acceptance`).
- BPCS controller selection, RIO node design, and unit-control-system integration beyond the building infrastructure boundary (BPCS basis is project-wide per DBM §"BPCS and Remote I/O").
- Detailed area classification, fire-and-gas detection design, and HVAC equipment selection (treated as `TBD` inputs to vendor design at deliverable scope).

## Requirements

| ReqID | Requirement | Source / basis |
|---|---|---|
| REQ-042-04-01 | The vendor package SHALL be engineered, designed, and supplied as the production unit defined by `DEL-042-04` and PKG-042. | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-042-04`; `PACKAGE_REGISTER.csv` `PKG-042` |
| REQ-042-04-02 | The vendor package SHALL host the operations control-room environment, providing the physical space and services for operator workstations, engineering workstations, primary servers, and core network switches. | DBM `4-25_Deepcut_DBM.md` §3119, §3141 |
| REQ-042-04-03 | The vendor package SHALL provide the building location for the primary control-system server host; the secondary host is located in the low-voltage MCC room (not in this package). | DBM `3-25_Comp_and_Liquids_DBM.md` §796 |
| REQ-042-04-04 | The vendor package SHALL provide engineering provisions for the eleven package-level interface types declared for PKG-042: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` (InterfaceTypes) |
| REQ-042-04-05 | Building design SHALL be coordinated with area classification, ventilation, heating, emergency egress, fire and gas detection, ESD pushbutton placement, RIO panel locations, power distribution, and maintenance access. | DBM `3-25_Comp_and_Liquids_DBM.md` §704 |
| REQ-042-04-06 | Foundations SHALL be designed for the final geotechnical report, equipment loads, snow/wind/seismic criteria, frost protection, vibration, settlement, and maintenance access, with equipment-specific foundation and anchorage checks. | DBM `3-25_Comp_and_Liquids_DBM.md` §700 |
| REQ-042-04-07 | Building siting SHALL respect DBM separation criteria, including ≥ 15.24 m (50 ft) from pressurized bullets (API 2510) and ≥ 25 m (82 ft) from fired heaters (OGAOM §9.6.15). | DBM `4-25_Deepcut_DBM.md` §254, §298 |
| REQ-042-04-08 | Interior building wiring SHALL comply with the Canadian Electrical Code and applicable area classification. EMT MAY be used in the non-process building interior; minimum conduit size SHALL be 21 mm (3/4 in); conduit SHALL be sealed where it crosses a change in area classification or enters explosion-proof / flameproof enclosures. | DBM `4-25_Deepcut_DBM.md` §3025 |
| REQ-042-04-09 | Where the building is fabricated and erected in the assembly shop before shipment, rigid conduit SHALL be used for systems such as building lighting, exhaust fans, receptacles, and switches. | DBM `4-25_Deepcut_DBM.md` §3025 |
| REQ-042-04-10 | The vendor package SHALL include the vendor package design basis and a datasheet set as deliverable artifacts, suitable for handoff to `DEL-042-05`. | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-042-04` (anticipated artifacts) |
| REQ-042-04-11 | Building HVAC, fire & gas detection design, and area classification SHALL be confirmed by the EPC Package Datasheet (`DEL-042-02`) before vendor design freeze; values are `TBD` at this deliverable's scope. | DBM `3-25_Comp_and_Liquids_DBM.md` §704; ASSUMPTION pending EPC-side resolution |
| REQ-042-04-12 | Vendor design SHALL accept facility-level integration, tie-ins, and constructability requirements as inputs from the EPC Integrator; vendor SHALL NOT unilaterally specify facility integration provisions. | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` (ResponsibilityModel) |

## Standards

| Standard / authority | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Governs interior building wiring, conduit sizing, and area-classification sealing | DBM `4-25_Deepcut_DBM.md` §3025 |
| API 2510 | Spacing between pressurized bullets and buildings related to facility control (control room) | DBM `4-25_Deepcut_DBM.md` §254 |
| OGAOM §9.6.15 | Spacing between fired heaters and control room / electrical buildings | DBM `4-25_Deepcut_DBM.md` §298 |
| National Building Code of Canada / provincial building code | Likely applicable to building structural, envelope, egress, and life-safety design | ASSUMPTION: likely applicable; location TBD |
| NFPA 70 / 72 / 92 (or Canadian equivalents) for fire alarm and smoke control | Likely applicable to building fire-alarm / smoke / detection systems | ASSUMPTION: likely applicable; location TBD |
| Workbook reference `26020-03-39-010` | Package code in workbook row 44 | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` |

## Verification

| ReqID | Verification approach |
|---|---|
| REQ-042-04-01 | Vendor design documentation review against `DEL-042-01` and `DEL-042-02` (executed under `DEL-042-06`). |
| REQ-042-04-02 | Functional design review confirming building accommodates operator/engineering workstations, primary servers, and core network switches with required environmental services. |
| REQ-042-04-03 | Layout review confirming primary-server host location in the control room (separate from the secondary host location in the low-voltage MCC room). |
| REQ-042-04-04 | Interface checklist review across all eleven declared PKG-042 InterfaceTypes. |
| REQ-042-04-05 | Cross-discipline design review against area classification, ventilation, heating, egress, fire and gas, ESD, RIO, power distribution, and maintenance-access checklists. |
| REQ-042-04-06 | Foundation design review against final geotechnical report and loading basis. |
| REQ-042-04-07 | Plot-plan separation verification against API 2510 (bullets) and OGAOM §9.6.15 (fired heaters). |
| REQ-042-04-08 | Electrical drawing review against CEC, area classification drawing, and conduit-sealing details. |
| REQ-042-04-09 | Assembly-shop conduit specification review (where shop pre-assembly is used). |
| REQ-042-04-10 | Document register check confirming design basis and datasheet set are present in `DEL-042-05`. |
| REQ-042-04-11 | Confirmation that HVAC, F&G, and area-classification inputs from `DEL-042-02` are incorporated before design freeze. |
| REQ-042-04-12 | EPC integration review (`DEL-042-06`) confirming vendor design accepts facility-integration inputs and does not pre-empt EPC-owned scope. |

## Documentation

Required output artifacts (per Gate 7 anticipated artifacts):

- Vendor engineered physical equipment package (the production unit itself).
- Vendor package design basis.
- Vendor package datasheet set.

Cross-referenced sibling deliverables (not produced here):

- `DEL-042-01_scope-of-work` — EPC scope basis (upstream input).
- `DEL-042-02_package-datasheet` — EPC technical handoff (upstream input).
- `DEL-042-03_construction-work-package` — facility-side construction work package.
- `DEL-042-05_vendor-document-turnover-package` — vendor document register and submittals (downstream).
- `DEL-042-06_epc-vendor-package-review-and-acceptance` — EPC review/acceptance (downstream).
