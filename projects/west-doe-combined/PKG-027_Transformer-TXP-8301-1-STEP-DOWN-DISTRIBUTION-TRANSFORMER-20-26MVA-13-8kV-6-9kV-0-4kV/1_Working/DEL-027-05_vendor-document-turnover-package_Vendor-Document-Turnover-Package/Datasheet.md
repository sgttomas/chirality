# Datasheet: DEL-027-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-027-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-027` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 27 / row 29 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-027` |
| CoA tracking number | 26020-01-30-018 | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Discipline | Electrical | Workbook Packages row 29; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-027` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Document set scope | Vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for the TXP-8301-1 step-down distribution transformer package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-027-05_vendor-document-turnover-package` |
| Tagged equipment | Transformer TXP-8301-1 — step-down distribution transformer rated 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV (package title designation). | Workbook Packages row 29 (package title) |
| Step-down service context | Power from the 13.8 kV switchgear shall be distributed radially through step-down transformers to plant loads; package transformer is a step-down distribution transformer within that radial distribution architecture. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plant power distribution section |
| Vendor document register | TBD. The artifact register records that detailed vendor-document requirements are not present in current source material for this package. The deliverable shall produce a vendor document register populated from vendor submittals. | `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF`; `_REFERENCES.md` |
| Submittal list | TBD. Specific vendor submittals (drawings, datasheets, test reports, certifications, manuals) are not enumerated in accessible source slices and shall be defined by the vendor scope and EPC review. | `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF`; Source gap |
| Source-required documentation | TBD. No accessible source slice enumerates required vendor documentation (e.g., factory test reports, routine/type tests, oil reports, nameplate records) specific to PKG-027. | Source gap; `_REFERENCES.md` |
| Turnover records | TBD. Turnover record format, content, and acceptance criteria are not defined in accessible source slices for this package. | Source gap; `_REFERENCES.md` |
| Grounding test record applicability | The DBM requires ground wells at power transformers for maintenance and operational testing with bolted ground connections at test points; vendor documentation should support post-installation grounding tests. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph |
| Neutral grounding documentation | Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and operate as a tripping system; vendor documentation should reflect this grounding configuration for the 6.9 kV winding. ASSUMPTION: applies to the 6.9 kV winding of TXP-8301-1 by virtue of voltage class; confirmation required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, neutral grounding paragraph |

## Conditions

| Interface / condition | Datasheet/turnover documentation basis | Source |
|---|---|---|
| Electrical Power | Vendor documentation shall record electrical power interface terminations, ratings, and acceptance evidence; interface applies per `IFC-7FDEAE3A5F`. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-7FDEAE3A5F` |
| Grounding / Bonding | Vendor documentation shall include grounding/bonding evidence consistent with package interface `IFC-868150D715` and DBM grounding requirements. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-868150D715`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Area / Exterior Lighting | Vendor documentation shall preserve area/exterior lighting interface fact for the package per `IFC-A7AA374E9F`. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-A7AA374E9F` |
| I&C / Control Cabling | Vendor documentation shall include I&C / control cabling termination, signal list, and tag evidence per `IFC-A771D8D087`. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-A771D8D087` |
| Communications / Network | Vendor documentation shall include communications/network interface evidence per `IFC-41603B3260` where applicable. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-41603B3260` |
| Maintenance Access | Vendor documentation shall preserve maintenance access requirements (clearances, access doors, oil sampling, bushings) per `IFC-6D508F385A`. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-6D508F385A` |
| Structural / Foundations / Supports | Vendor documentation shall include foundation loads, mounting, and support data for the transformer per `IFC-1B8FDDED83`; DBM notes transformers are generally supported on precast concrete bearing foundations. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-1B8FDDED83`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations table |
| Transformer secondary cabling documentation | Where the secondary feeds 600 V MCCs, ACWU is the cable type and single-conductor cables are avoided; vendor documentation should be consistent with this cable convention where applicable. ASSUMPTION: applies if the 0.4 kV winding of TXP-8301-1 feeds 600 V-class equipment; the package nameplate is 0.4 kV which is below 600 V — confirmation required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor documentation authorship | Package Vendor is responsible for producing the vendor documentation set. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-027-05_vendor-document-turnover-package`; `PACKAGE_REGISTER.csv` row `PKG-027` |
| EPC Integrator role | EPC Integrator performs interface/integration review of the vendor documentation set and uses it for facility integration. | `DELIVERABLE_REGISTER.csv` row `DEL-027-05_vendor-document-turnover-package`; `PACKAGE_REGISTER.csv` row `PKG-027` |
| Document register format | TBD. No source slice specifies vendor document register schema, numbering, status codes, or revision conventions for PKG-027. | Source gap; `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF` |
| Submittal workflow | TBD. Submittal/return-code workflow (e.g., AFC, AFI, Hold) is not defined in accessible source slices for this package. | Source gap |
| Turnover package contents | TBD. Required turnover package contents (e.g., as-built drawings, O&M manuals, certified test reports, spare parts list, warranty documents) are not enumerated in accessible source slices. | Source gap; `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF` |
| Foundation/installation evidence | DBM notes transformers are generally installed on structural steel transformer bases with CEC-compliant spacing and secondary containment review; vendor documentation should support these installation conditions. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers section |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- `DELIVERABLE_REGISTER.csv`, row `DEL-027-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-027`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-027-05_vendor-document-turnover-package` (notably `ART-AACDC8D0FF` documenting the vendor-document source gap).
- `INTERFACE_REGISTER.csv`, rows for `PKG-027` (`IFC-7FDEAE3A5F`, `IFC-868150D715`, `IFC-A7AA374E9F`, `IFC-A771D8D087`, `IFC-41603B3260`, `IFC-6D508F385A`, `IFC-1B8FDDED83`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-027-05_vendor-document-turnover-package` (`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29 (workbook source row).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for plant power distribution, transformers, neutral grounding, grounding/bonding, foundations, and secondary cabling.
- `_Sources/26020-Package_Requirements.docx`, no package-specific vendor-document content located for `PKG-027`.
