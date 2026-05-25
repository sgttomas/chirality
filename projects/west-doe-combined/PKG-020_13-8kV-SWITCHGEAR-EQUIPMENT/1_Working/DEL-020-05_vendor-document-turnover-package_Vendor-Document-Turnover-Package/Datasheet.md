# Datasheet: DEL-020-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-020-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-020` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 13.8kV SWITCHGEAR EQUIPMENT | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 20 / row 22 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-011 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-020` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Deliverable class | Single Package Vendor deliverable for the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review. | `DELIVERABLE_REGISTER.csv` row `DEL-020-05_vendor-document-turnover-package` |
| Anticipated artifact set | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Vendor document register | TBD. ASSUMPTION: a vendor-issued register listing each document by number, title, revision, type, and status is the standard project-control instrument; the specific document list is not enumerated by the currently accessible source slices. | Source gap; `_Sources/26020-Package_Requirements.docx` not parsed in accessible form; `ART-FA0DE34BAB` records "TBD vendor document register". |
| Vendor submittal set | TBD. Document classes typically include datasheets, GA/outline drawings, schematics, wiring/termination drawings, BOMs, FAT/SAT records, manuals, and spare-parts lists; package-specific list and quantities are not stated in the accessible DBM slice. | ASSUMPTION (industry-standard MV switchgear submittal set); not anchored to a PKG-020-specific source slice. |
| Turnover record set | TBD. ASSUMPTION: turnover typically comprises FAT reports, factory test certificates, inspection releases, shipping releases, site receipt/inspection records, SAT records, calibration records, and final as-built documentation; the package-specific turnover content is not specified in the available source slice. | Source gap; no DBM slice enumerates PKG-020 turnover content. |
| Source vendor document rows | Individual source document rows remain artifacts/evidence, not separate deliverables. | `DELIVERABLE_REGISTER.csv` notes column |
| Document control / numbering | TBD. ASSUMPTION: vendor documentation is numbered against the project document-numbering convention and the package CoA tracking number `26020-01-30-011`; the project document-control procedure governs final numbering. | Source gap; project document-control procedure not present in the accessible source slice. |

## Conditions

| Interface / condition | Datasheet basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-020 and must be represented in package interface evidence and the vendor document register. | `INTERFACE_REGISTER.csv` `IFC-611474D99C` |
| Grounding / Bonding | Interface fact applies to PKG-020 and must be represented in package interface evidence and the vendor document register. | `INTERFACE_REGISTER.csv` `IFC-F3098CE7CD` |
| I&C / Control Cabling | Interface fact applies to PKG-020 and must be represented in package interface evidence and the vendor document register. | `INTERFACE_REGISTER.csv` `IFC-8BF7209227` |
| Communications / Network | Interface fact applies to PKG-020 and must be represented in package interface evidence and the vendor document register. | `INTERFACE_REGISTER.csv` `IFC-340091634A` |
| Maintenance Access | Interface fact applies to PKG-020 and must be represented in package interface evidence and the vendor document register. | `INTERFACE_REGISTER.csv` `IFC-2FB786FC10` |
| Structural / Foundations / Supports | Interface fact applies to PKG-020 and must be represented in package interface evidence and the vendor document register. | `INTERFACE_REGISTER.csv` `IFC-08E563D004` |
| Vendor-document register binding scope | The register and submittals govern only PKG-020 13.8kV switchgear equipment. Other packages (PKG-011 4160V switchgear, PKG-021 6.9kV switchgear, transformer packages) have their own separate vendor-document deliverables. | `DELIVERABLE_REGISTER.csv`; `PACKAGE_REGISTER.csv` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document authorship | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-020`; `DELIVERABLE_REGISTER.csv` |
| Vendor document review and integration acceptance | EPC Integrator interface/integration review. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Storage / repository for the turnover set | TBD. ASSUMPTION: the vendor documentation set will be turned over electronically through the project document control system and physically through marked-up O&M binders; the actual repository, transmittal format, and acceptance route are not stated in the accessible source slice. | Source gap. |
| Document numbering and revision control | TBD. ASSUMPTION: project document-numbering convention applies; vendor revisions follow vendor practice but each transmittal is logged in the register. | Source gap; project document-control procedure not present in accessible source slice. |
| Turnover gating | TBD. ASSUMPTION: turnover acceptance is gated by `DEL-020-06_epc-vendor-package-review-and-acceptance` per the package decomposition. | `DELIVERABLE_REGISTER.csv` row `DEL-020-06`. |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared upstream/downstream lists (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-020-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-020`.
- `ARTIFACT_REGISTER.csv`, row `ART-FA0DE34BAB` (TBD vendor document register).
- `INTERFACE_REGISTER.csv`, PKG-020 interface rows `IFC-611474D99C`, `IFC-F3098CE7CD`, `IFC-8BF7209227`, `IFC-340091634A`, `IFC-2FB786FC10`, `IFC-08E563D004`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, package-grouping heuristic only.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 22 (binary; not parsed by this run).
- `_Sources/26020-Package_Requirements.docx`, package-requirements document searched for PKG-020-specific vendor-documentation content; no accessible slice found.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, project-basis source; no PKG-020 vendor-documentation slice enumerated.
