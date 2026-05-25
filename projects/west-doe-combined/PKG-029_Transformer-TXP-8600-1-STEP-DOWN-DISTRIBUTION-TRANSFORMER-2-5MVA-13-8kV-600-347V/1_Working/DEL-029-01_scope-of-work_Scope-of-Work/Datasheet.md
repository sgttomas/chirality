# Datasheet: DEL-029-01_scope-of-work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-029-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-029` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 29 / row 31 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-029 |
| CoA tracking number | 26020-01-30-020 | `PACKAGE_REGISTER.csv` row PKG-029 |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Scope Items covered | `SOW-0030` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC, ASSUMPTION) |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-029` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Package function (title-derived) | Step-down distribution transformer rated 2.5 MVA, 13.8 kV primary to 600/347 V secondary, identified by tag `TXP-8600-1`. | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Facility role (ASSUMPTION) | The TXP-8600-1 transformer steps down the facility 13.8 kV medium-voltage distribution to a 600 V low-voltage service for an electrical building or distributed loads in WBS 01 (04-25 Deepcut). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System and System Voltages tables (lines 2917-2937) |
| Primary voltage | 13.8 kV (title-derived) | Workbook Packages row 31 |
| Secondary voltage | 600/347 V (title-derived; corresponds to a wye secondary with 600 V line-line and 347 V line-neutral) | Workbook Packages row 31 |
| Continuous rating | 2.5 MVA (title-derived; basis — ONAN/ONAF/duty cycle — TBD) | Workbook Packages row 31 |
| Insulating medium | TBD. DBM-Deepcut references "Large oil-filled transformers" generally (line 2949); specific selection (oil-filled vs. dry-type) for TXP-8600-1 is not confirmed by an accessible package-specific source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers paragraph |
| Tagged equipment list | One transformer tag: `TXP-8600-1`. Additional skid-mounted equipment (e.g., LV section breakers, surge arresters, RTDs, fan controls) is TBD pending vendor package data. | Workbook Packages row 31; package-specific source slice not available |
| Secondary system grounding | 600 V services are facility-wide high-resistance grounded with a 5 A continuous resistor; each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor. Confirmation that TXP-8600-1 follows this rule is the EPC Integrator responsibility. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table (line 2937); Grounding paragraph (line 2985) |
| Primary system grounding | 13.8 kV facility distribution is low-resistance grounded per System Voltages table; primary-side grounding scheme for TXP-8600-1 is governed by the facility 13.8 kV system, not by this transformer. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table (line 2937) |
| Standards (facility level) | Canadian Electrical Code (CEC) referenced for spacing, ground conductor sizing, and installation. Equipment standards (e.g., CSA C9, IEEE C57) are TBD pending package-specific source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers and Grounding paragraphs (lines 2949, 2991) |

## Conditions

| Interface / condition | Datasheet basis | Source |
|---|---|---|
| Electrical Power | Source-confirmed interface for PKG-029. Primary feed from facility 13.8 kV switchgear; secondary feed to 600 V loads/distribution. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-717D0187BA`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System (lines 2917-2919) |
| Grounding / Bonding | Source-confirmed interface. Major electrical equipment shall be directly connected to the ground grid at two points; ground wells shall be provided at power transformers; secondary HRG resistor required for 600 V transformer per facility rule. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-C49653E450`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding paragraphs (lines 2985, 2989, 2991) |
| Area / Exterior Lighting | Source-confirmed interface. Specific lighting tie-ins for the transformer pad/area are TBD. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-DFC1A10C2D` |
| I&C / Control Cabling | Source-confirmed interface. Control/monitoring signals (winding RTDs, oil temp, fan/cooling control, BCT, etc.) are TBD pending vendor data. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-A5C9438164` |
| Communications / Network | Source-confirmed interface. Network connectivity (e.g., transformer monitor, Ethernet) is TBD. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-81CFD2A32C` |
| Maintenance Access | Source-confirmed interface. Cable tray and conduit routing shall not interfere with maintenance access; CEC spacing applies. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-2C14FA1228`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers and routing notes |
| Structural / Foundations / Supports | Source-confirmed interface. Foundation concept (DBM): transformers generally installed on structural steel transformer bases on precast concrete bearing foundations. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-380F4773FB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` foundation concepts (line 2660); Transformers paragraph (line 2949); Civil table row 2745 |
| Secondary containment | DBM directs that secondary-containment requirements shall be reviewed and transformer selection shall avoid or limit containment requirements where practical. Outcome for TXP-8600-1 is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers paragraph (line 2949) |
| CEC spacing | CEC spacing requirements apply to large oil-filled transformers; selection outcome for TXP-8600-1 determines applicability. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers paragraph (line 2949) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, package design, vendor documentation, physical equipment package | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Installation location | TBD. DBM Power System lists radial distribution targets including a "4.16 kV/600 V General Area/Tank Farm/Process Electrical Building", but PKG-029 has not been assigned by accessible source to a specific electrical building or yard location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System (lines 2919-2925) |
| Foundation / supports | Structural / Foundations / Supports interface applies; DBM directs structural-steel transformer base on precast concrete bearing foundation as a general approach. Package-specific support basis is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2660, 2745, 2949 |
| Primary feeder | TBD. Feeder routing, cable type, length, and protective device coordination with the 13.8 kV switchgear are not defined in available source slices. | Source gap |
| Secondary feeder / distribution | TBD. Downstream 600 V distribution (electrical building MCC, RDC, or other) is not assigned in available source slices. | Source gap |
| Vendor-specific construction (cooling type, tap changer, BIL, impedance, weight, dimensions) | TBD. No package-specific source slice provides these values. `_Sources/26020-Package_Requirements.docx` was searched; no PKG-029-specific match was returned. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-029-01_scope-of-work`.
- `PACKAGE_REGISTER.csv`, row `PKG-029`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-029-01_scope-of-work`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-029` (`IFC-717D0187BA`, `IFC-C49653E450`, `IFC-DFC1A10C2D`, `IFC-A5C9438164`, `IFC-81CFD2A32C`, `IFC-2C14FA1228`, `IFC-380F4773FB`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, package-grouped objective rows for `PKG-029` (PACKAGE_HEURISTIC, ASSUMPTION).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 31.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System, System Voltages, Transformers, Standby Power, 208/120 V Systems, Electrical Buildings, Grounding and Bonding paragraphs.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers context (analog only; PKG-029 belongs to WBS 01 / Deepcut, not 03-25).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific TXP-8600-1 / PKG-029 content; no package-specific match was found.
