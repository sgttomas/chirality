# Datasheet: DEL-030-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-030-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-030` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 30 / row 32 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-030` |
| CoA tracking number | 26020-01-30-021 | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-030` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Package function | Step-down distribution transformer, 2.5 MVA, 13.8 kV primary / 600/347 V secondary | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Deliverable function | Vendor document register, vendor document submittals, source-required vendor documentation, and turnover records, with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Mechanical package documentation basis | Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverable paragraph (line 617) |
| Electrical distribution context | 13.8 kV to 600 V step-down transformers feed 600 V MCC for LV loads; medium-voltage switchgear and low-voltage MCCs are part of the facility electrical distribution. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical distribution table (line 745) |
| Vendor document register content | TBD. The artifact register identifies "TBD vendor document register" with a documented gap: detailed vendor-document requirements are not present in current source material for this package. | `ARTIFACT_REGISTER.csv` row `ART-8B1CB2D887` |
| Specific vendor document list (drawings, IOM, test reports, factory acceptance test records, name-plate data, etc.) | TBD. No package-specific vendor-document content found in accessible sources for `PKG-030`. | Source gap |
| Turnover record content | TBD. Source material does not define package-specific turnover record content for `PKG-030`. | Source gap |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-030`; vendor documentation set shall capture primary/secondary connection data, feeder reference, and protection coordination data needed to evidence package electrical interface. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-009C48E7FF` |
| Grounding / Bonding | Interface fact applies; vendor documentation shall include transformer neutral grounding, enclosure bonding, and ground grid connection evidence. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-6C663BF69D` |
| Area / Exterior Lighting | Interface fact applies; vendor documentation shall reference local lighting needs around the transformer installation if vendor-supplied. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-0B28AED229` |
| I&C / Control Cabling | Interface fact applies; vendor documentation shall describe control terminal blocks, monitoring outputs (temperature, alarm, gas, oil level as applicable), and termination diagrams. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-D000451C37` |
| Communications / Network | Interface fact applies; vendor documentation shall identify any vendor-supplied communications interface and protocol. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-9EF13A0FC1` |
| Maintenance Access | Interface fact applies; vendor documentation shall preserve maintenance clearances and identify components requiring access. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-345609CB34`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray/conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies; vendor documentation shall include loading, anchor pattern, and support requirements for the transformer foundation. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-4B50D76AF1` |
| Document support artifact basis | Vendor-documentation gaps that would normally be confirmed from missing appendices remain governed by applicable engineering sections or remain `TBD`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, document support artifact register paragraphs (line 3438+) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document register ownership | Package Vendor responsibility, with EPC Integrator review for facility integration impact. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-030` |
| Document register baseline content | TBD. Source material does not enumerate the specific document types required for `PKG-030`; conservative baseline derived from DBM mechanical-package deliverable basis (datasheets, utility load summaries, tie-in lists, operating envelopes, sparing philosophy, materials/coating basis, maintenance access, shipped-loose item lists, vendor document register). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617; otherwise source gap |
| Submittal sequence | TBD. No package-specific submittal sequence or schedule found in accessible sources. | Source gap |
| Source-required vendor documentation | TBD. Individual source vendor-document table rows are carried as artifacts/evidence (per `_CONTEXT.md` Notes), not as separate deliverables. | `_CONTEXT.md` Notes; `ARTIFACT_REGISTER.csv` |
| Turnover records | TBD. No package-specific turnover record schema/list found in accessible sources. | Source gap |
| EPC Integrator review interface | EPC Integrator owns interface/integration review of the vendor document turnover package; review record format is TBD. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-030` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-030-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-030`.
- `ARTIFACT_REGISTER.csv`, row `ART-8B1CB2D887` (TBD vendor document register, with documented vendor-documentation gap).
- `INTERFACE_REGISTER.csv`, rows for `PKG-030` (`IFC-009C48E7FF`, `IFC-6C663BF69D`, `IFC-0B28AED229`, `IFC-D000451C37`, `IFC-9EF13A0FC1`, `IFC-345609CB34`, `IFC-4B50D76AF1`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-030-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverable basis (line 617), electrical distribution table (line 745), and document support artifact register (line 3438+).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray/conduit and grounding/bonding source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific PKG-030 vendor-document content; no package match found.
