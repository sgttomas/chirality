# Datasheet: DEL-014-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-014-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-014` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 14 / row 16 | `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-005 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-014` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Deliverable class | Single Package Vendor deliverable for the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05` |
| Artifact set | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05` |
| Companion artifact role | Individual source document rows remain artifacts/evidence within this deliverable; they are not separate deliverables. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05`, notes |
| Package documentation expectation (general) | Vendor packages shall include vendor document registers as part of the package deliverable expectation defined for mechanical packages. The DBM articulates this rule generally and the PKG-014 electrical/contactor scope inherits the same package-deliverable discipline through the Gate 7 register. ASSUMPTION (best-effort mapping) that the general rule applies to PKG-014. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, packages paragraph (line 617) |
| Vendor document content per package (line-item enumeration) | TBD. The accessible DBM source slice enumerates a general package-deliverable set (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers) but does not specify the line-item vendor document list for low-voltage contactor panels. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, packages paragraph (line 617) |
| Source-required vendor documents (PKG-014-specific) | TBD. No PKG-014-specific match was located in `_Sources/26020-Package_Requirements.docx` or the DBM source slices accessible to this deliverable. | Source gap; `26020-Package_Requirements.docx` not slice-extracted for `PKG-014` |
| Turnover record set | TBD. No package-specific turnover record list (e.g., FAT/SAT reports, test records, warranty, as-built drawings, spares list, nameplate data) is defined in the accessible source slices for PKG-014. | Source gap |

## Conditions

| Interface / condition | Documentation implication | Source |
|---|---|---|
| Electrical Power | Vendor document register and submittals must carry the artifacts evidencing the Electrical Power interface to the facility (e.g., feeder, breaker, protection coordination data). Specifics TBD pending detailed design. | `INTERFACE_REGISTER.csv` `IFC-78CF31138D` |
| Grounding / Bonding | Vendor documentation must include grounding/bonding details for the contactor panels and lighting/exhaust-fan loads sufficient for EPC facility integration. | `INTERFACE_REGISTER.csv` `IFC-31C88BB424` |
| Area / Exterior Lighting | Vendor documentation must enumerate lighting circuit / contactor control wiring and switching basis served by the package. | `INTERFACE_REGISTER.csv` `IFC-EF784327FA` |
| I&C / Control Cabling | Vendor documentation must include I&C / control cabling termination details and panel control schematics required by EPC integration. | `INTERFACE_REGISTER.csv` `IFC-C715E9AA3E` |
| Communications / Network | Vendor documentation must include any communications/network interface descriptions (if applicable to the panel scope). Applicability TBD. | `INTERFACE_REGISTER.csv` `IFC-2D60238809` |
| Maintenance Access | Vendor documentation must include arrangement and clearance data sufficient to support facility maintenance access. | `INTERFACE_REGISTER.csv` `IFC-52B07B0D36` |
| Structural / Foundations / Supports | Vendor documentation must include weights, mounting, and support loads sufficient for the EPC structural interface. | `INTERFACE_REGISTER.csv` `IFC-53646D26A1` |
| EPC review hook | EPC Integrator interface/integration review applies to the vendor document turnover package. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05`, responsible party |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document register format | TBD. No facility- or project-specific vendor document register template is referenced in accessible PKG-014 source slices. | Source gap |
| Submittal workflow | EPC Integrator interface/integration review of vendor submittals applies. Detailed submittal/transmittal mechanics (numbering, status codes, review cycle days) TBD. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05` |
| Source-required vendor documents | Where the source basis (e.g., `26020-Package_Requirements.docx`) defines specific required vendor documents for the contactor panel scope, those rows become artifacts under this deliverable. ASSUMPTION (best-effort mapping) until the package-specific source slice is extracted. | `_REFERENCES.md`, Missing/Deferred References |
| Turnover record set | Turnover records (e.g., FAT/SAT, test reports, certifications, as-built marked drawings, nameplate data, spares list, warranty documentation) shall accompany the package. Specific list TBD. | Source gap |
| Boundary against other DEL-014 deliverables | This deliverable owns vendor documentation artifacts and turnover records only; equipment engineering/design lives in `DEL-014-04`; EPC review/acceptance evidence lives in `DEL-014-06`. | `DELIVERABLE_REGISTER.csv` rows `DEL-014-04`, `DEL-014-05`, `DEL-014-06` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared coordination edges (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-014-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-014`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-014-05_vendor-document-turnover-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-014` (`IFC-78CF31138D`, `IFC-31C88BB424`, `IFC-EF784327FA`, `IFC-C715E9AA3E`, `IFC-2D60238809`, `IFC-52B07B0D36`, `IFC-53646D26A1`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-014-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 16.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages paragraph (vendor document register expectation, line 617).
- `_Sources/26020-Package_Requirements.docx`, not slice-extracted for `PKG-014`; package-specific vendor document set TBD pending extraction.
