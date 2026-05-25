# Datasheet: DEL-027-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-027-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-027` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 27 / row 29 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-027` |
| CoA tracking number | 26020-01-30-018 | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Discipline | Electrical | Workbook Packages row 29; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-027` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Package function | Step-down distribution transformer TXP-8301-1, 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV. | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Construction work package scope | EPC-authored description of how the package is physically installed, built, inspected, turned over, and tied into facility systems. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Facility power-system context | Step-down transformers feed 13.8 kV switchgear-derived radial distribution to medium-voltage and low-voltage loads across the plant; medium-voltage step-down transformer requirements derive from the facility's 13.8 kV main distribution architecture. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical system architecture paragraph; ASSUMPTION that TXP-8301-1 participates in this architecture based on voltage class match. |
| Foundation basis | Large oil-filled transformers are generally installed on structural steel transformer bases; secondary containment requirements shall be reviewed and transformer selection shall avoid or limit containment where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph; foundation concepts paragraph (precast concrete bearing foundations for transformers). |
| Spacing basis | Large oil-filled transformers shall be spaced in accordance with CEC requirements. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph |
| Grounding basis | All major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers or electrical buildings shall be provided for maintenance and operational testing. Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Oil-filled vs. dry-type | TBD. Source identifies oil-filled transformer construction practices and dry-type instances for specific small loads; the specific TXP-8301-1 construction type is not declared in accessible sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Physical location / building assignment | TBD. Source allows electrical-building, outdoor pad, or skid configurations but does not assign TXP-8301-1 to a confirmed location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Construction quantity (TXP-8301-1) | 1 step-down transformer asset implied by the tag "TXP-8301-1". | Workbook Packages row 29 (tag in package name); ASSUMPTION based on single-tag identity. |

## Conditions

| Interface / condition | Construction requirement basis | Source |
|---|---|---|
| Electrical Power | Construction tie-in for medium-voltage feeders (13.8 kV primary; 6.9 kV and 0.4 kV secondary distribution) shall be planned, installed, and turned over per facility electrical design. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-7FDEAE3A5F`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical system paragraphs. |
| Grounding / Bonding | Two-point connection to ground grid; ground well at the transformer for maintenance/test access; 6.9 kV transformer neutral grounded via 100 A, 10 s NGR as a tripping system (applicability to the 6.9 kV winding of TXP-8301-1 to be confirmed). | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-868150D715`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` grounding paragraphs. |
| Area / Exterior Lighting | Construction shall coordinate exterior lighting around the transformer pad/yard for maintenance access and safety. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-A7AA374E9F`. Detailed luminaire counts and lux levels TBD. |
| I&C / Control Cabling | Construction shall pull, terminate, and test control cabling for transformer protection, monitoring, alarms, OLTC controls (if applicable), and SCADA interfaces. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-A771D8D087`. |
| Communications / Network | Construction shall provide network drops and terminations needed for transformer monitoring and protective relay communications. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-41603B3260`. Detailed network topology TBD. |
| Maintenance Access | Cable tray and conduit routing, equipment layout, fencing, and lay-down area shall preserve crane access, transformer pull/replacement clearance, and worker maintenance access. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-6D508F385A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` cable tray and conduit paragraphs. |
| Structural / Foundations / Supports | Construction shall execute the structural-steel transformer base or precast concrete bearing foundation per detailed design; secondary containment shall be installed where required. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-1B8FDDED83`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` foundations and transformers paragraphs. |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility (design/fabricate/supply). | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Facility integration, tie-ins, constructability, construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Foundation construction | Structural steel base or precast concrete bearing foundation; secondary containment installation reviewed per source guidance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers + foundation concepts paragraphs. Detailed footing design TBD. |
| Receiving, handling, and setting | TBD. Accessible sources do not specify package-specific rigging plan, lift weight, transport route, or laydown configuration for TXP-8301-1. | Source gap. |
| Oil management (if oil-filled) | TBD. Vacuum-fill/oil-handling/oil-quality acceptance procedures not stated in accessible sources for this package. | Source gap. |
| Field testing and commissioning | TBD. Accessible sources do not list package-specific transformer factory acceptance test (FAT), site acceptance test (SAT), or commissioning protocol for TXP-8301-1. | Source gap; defer to vendor data and project commissioning standard. |
| Interface tie-in to 13.8 kV switchgear, 6.9 kV switchgear, and 0.4 kV distribution | EPC Integrator scope; coordinated with adjacent electrical packages. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` rows for `PKG-027`. Detailed termination drawings TBD. |
| Inspection and turnover checklist | Artifact `ART-6C4FC25B92` is required for this deliverable. | `ARTIFACT_REGISTER.csv` row `ART-6C4FC25B92`. |
| Workface plan | Artifact `ART-16F575F6A0` is required to plan installation and tie-in execution. | `ARTIFACT_REGISTER.csv` row `ART-16F575F6A0`. |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-027-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-027`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-027-03_construction-work-package` (`ART-F3C58917C8`, `ART-16F575F6A0`, `ART-6C4FC25B92`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-027` (`IFC-7FDEAE3A5F`, `IFC-868150D715`, `IFC-A7AA374E9F`, `IFC-A771D8D087`, `IFC-41603B3260`, `IFC-6D508F385A`, `IFC-1B8FDDED83`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-027-03_construction-work-package` (ASSUMPTION: package-heuristic association).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical system architecture, transformers, foundations, grounding, cable tray, conduit, and electrical buildings source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific TXP-8301-1 construction content; no PKG-027 package-specific match was extracted during this run.
