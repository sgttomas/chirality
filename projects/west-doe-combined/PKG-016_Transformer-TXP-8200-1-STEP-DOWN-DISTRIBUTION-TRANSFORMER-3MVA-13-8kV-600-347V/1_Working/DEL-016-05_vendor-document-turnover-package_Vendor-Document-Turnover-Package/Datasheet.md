# Datasheet: DEL-016-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-016-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-016` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Tag | TXP-8200-1 | `PACKAGE_REGISTER.csv`; package name string |
| Workbook ID / row | 16 / row 18 | `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-007 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-016` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Deliverable class | Single Package Vendor deliverable for the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05` |
| Artifact set | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05` |
| Companion artifact role | Individual source document rows remain artifacts/evidence within this deliverable; they are not separate deliverables. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05`, notes |
| Equipment subject (package identity context) | Step-down distribution transformer, nominal 13.8 kV to 600 V, 3 MVA, serving the 600V MCC for LV loads at the 03-25 facility. (347V secondary phase-to-neutral implied by 600V three-phase wye; 347V not separately confirmed in accessible source slice.) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 745 ("13.8 kV to 600V, 3 MVA transformer — 600V MCC for LV loads") |
| Package documentation expectation (general) | Vendor packages shall include vendor document registers as part of the package deliverable expectation defined in the DBM mechanical packages paragraph. The DBM articulates this rule generally for mechanical packages and the PKG-016 Electrical transformer scope inherits the same package-deliverable discipline through the Gate 7 register. ASSUMPTION (best-effort mapping) that the general rule applies to PKG-016 Electrical. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, packages paragraph (line 617) |
| Vendor document content per package (line-item enumeration) | TBD. The accessible DBM source slice enumerates a general package-deliverable set (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers) but does not specify the line-item vendor document list for a medium-voltage step-down distribution transformer. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, packages paragraph (line 617) |
| Source-required vendor documents (PKG-016-specific) | TBD. No PKG-016-specific match was located in `_Sources/26020-Package_Requirements.docx` or the DBM source slices accessible to this deliverable. | Source gap; `26020-Package_Requirements.docx` not slice-extracted for `PKG-016` |
| Turnover record set | TBD. No package-specific turnover record list (e.g., factory test reports, routine/type test certificates, nameplate data, as-built drawings, spares list, oil/insulation certificates, warranty) is defined in accessible source slices for PKG-016. | Source gap |

## Conditions

| Interface / condition | Documentation implication | Source |
|---|---|---|
| Electrical Power | Vendor document register and submittals shall carry the artifacts evidencing the Electrical Power interface (13.8 kV primary feeder from the 04-25 main switchgear sub-feed, 600 V secondary to the 600V MCC, ratings, protection, no-load and load losses, impedance). | `INTERFACE_REGISTER.csv` `IFC-0C63CABBEC`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 738-745 |
| Grounding / Bonding | Vendor documentation shall include grounding/bonding details for the transformer enclosure, neutral grounding scheme (HRG with 5A continuous resistor per LV service basis), and bonding to facility ground grid sufficient for EPC facility integration. | `INTERFACE_REGISTER.csv` `IFC-C4343B4BCA`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 734 |
| Area / Exterior Lighting | Vendor documentation shall describe any local indication/illumination integral to the transformer enclosure relevant to area lighting interfaces. Applicability TBD for a distribution transformer. | `INTERFACE_REGISTER.csv` `IFC-C649F648C5` |
| I&C / Control Cabling | Vendor documentation shall include I&C / control cabling termination details, monitoring/alarm wiring (temperature, pressure, level, gas), and protection relay interface basis required by EPC integration. | `INTERFACE_REGISTER.csv` `IFC-AC26461656` |
| Communications / Network | Vendor documentation shall include any communications/network interface descriptions (e.g., transformer monitor relay, IED) when applicable. Applicability TBD. | `INTERFACE_REGISTER.csv` `IFC-D3B7348DC6` |
| Maintenance Access | Vendor documentation shall include arrangement, clearance, lifting, and de-energization access data sufficient to support facility maintenance access. | `INTERFACE_REGISTER.csv` `IFC-4A94795733` |
| Structural / Foundations / Supports | Vendor documentation shall include shipping weight, operating weight, oil weight (if liquid-filled), seismic load, anchor pattern, and support load data sufficient for the EPC structural/foundation interface. | `INTERFACE_REGISTER.csv` `IFC-E3BE98E89B` |
| EPC review hook | EPC Integrator interface/integration review applies to the vendor document turnover package. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05`, responsible party |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document register format | TBD. No facility- or project-specific vendor document register template is referenced in accessible PKG-016 source slices. | Source gap |
| Submittal workflow | EPC Integrator interface/integration review of vendor submittals applies. Detailed submittal/transmittal mechanics (numbering, status codes, review cycle days) TBD. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05` |
| Source-required vendor documents | Where the source basis (e.g., `26020-Package_Requirements.docx`) defines specific required vendor documents for the medium-voltage distribution transformer scope, those rows become artifacts under this deliverable. ASSUMPTION (best-effort mapping) until the package-specific source slice is extracted. | `_REFERENCES.md`, Missing/Deferred References |
| Turnover record set | Turnover records (likely including factory routine and type test reports, impulse/dielectric test certificates, oil test certificate or dry-type insulation certificate, nameplate data, as-built marked drawings, spares list, warranty/maintenance documentation, operating and maintenance manual) shall accompany the package. Specific list TBD pending the project turnover standard. | Source gap; record types ASSUMPTION |
| Boundary against other DEL-016 deliverables | This deliverable owns vendor documentation artifacts and turnover records only; equipment engineering/design lives in `DEL-016-04`; EPC review/acceptance evidence lives in `DEL-016-06`. | `DELIVERABLE_REGISTER.csv` rows `DEL-016-04`, `DEL-016-05`, `DEL-016-06` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared coordination edges (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-016-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-016`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-016-05_vendor-document-turnover-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-016` (`IFC-0C63CABBEC`, `IFC-C4343B4BCA`, `IFC-C649F648C5`, `IFC-AC26461656`, `IFC-D3B7348DC6`, `IFC-4A94795733`, `IFC-E3BE98E89B`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-016-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 18.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages paragraph (vendor document register expectation, line 617); incoming power and transformers (lines 738-748); LV service basis (line 734).
- `_Sources/26020-Package_Requirements.docx`, not slice-extracted for `PKG-016`; package-specific vendor document set TBD pending extraction.
