# Datasheet: DEL-027-01_scope-of-work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-027-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-027` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 27 / row 29 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-027` |
| CoA tracking number | 26020-01-30-018 | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-027` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Tagged equipment | `TXP-8301-1` — single step-down distribution transformer. | Workbook Packages row 29 (package name) |
| Package class | Vendor-owned Electrical package. | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Package function | Step-down distribution transformer providing a 13.8 kV-to-6.9 kV step-down to feed the 6.9 kV process motor distribution, with an additional low-voltage winding labelled 0.4 kV in the workbook package name. | Workbook Packages row 29 (package name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical distribution paragraphs (13.8 kV switchgear distributing radially through step-down transformers; 6.9 kV medium-voltage services). |
| Rating (nameplate) | 20/26 MVA — `ASSUMPTION`: workbook labels the rating as "20/26MVA", consistent with conventional ONAN/ONAF dual-rating practice for oil-filled medium-voltage transformers. Cooling class is not stated in accessible sources and remains `TBD`. | Workbook Packages row 29 (package name); cooling class not in source. |
| Primary voltage | 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded (facility medium-voltage backbone). | Workbook Packages row 29 (package name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table (medium-voltage services). |
| Secondary voltage | 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded (facility process AC inverter-drive motor distribution rated 5,500 hp and above). | Workbook Packages row 29 (package name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table; 6.9 kV MCC paragraph. |
| Tertiary / additional winding | 0.4 kV winding identified in the workbook package name. `ASSUMPTION` / `NEEDS_HUMAN_RULING`: 0.4 kV (400 V) is not a defined Canadian project distribution voltage in the accessible DBM (which uses 600 V, 480 V, 208/120 V for low voltage). Treat as a labelling fact carried from the workbook until confirmed by vendor data or a clarifying source. | Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table. |
| Service location | Facility electrical distribution; step-down from the 13.8 kV switchgear bus to the 6.9 kV motor distribution. Building/area assignment is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 13.8 kV switchgear and 6.9 kV electrical building paragraphs. |
| Construction (oil/dry, mounting) | `ASSUMPTION`: oil-filled, outdoor pad-mounted construction is consistent with the DBM's "large oil-filled transformers" guidance and "structural steel transformer bases" practice; vendor confirmation required. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph (oil-filled, structural steel bases, secondary containment review). |
| Neutral grounding | `ASSUMPTION`: 6.9 kV winding to be grounded via a 100 A, 10 s neutral grounding resistor consistent with DBM rule "each 6.9 kV transformer shall be grounded using a 100 A, 10 s NGR and shall operate as a tripping system." 13.8 kV side grounding is established at the facility 13.8 kV switchgear, not at this transformer. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. |

## Conditions

| Interface / condition | Basis | Source |
|---|---|---|
| Electrical Power | Applicable interface — 13.8 kV primary feed from facility 13.8 kV switchgear and 6.9 kV secondary feed to the 6.9 kV MCC / electrical building distribution. | `INTERFACE_REGISTER.csv` rows `IFC-7FDEAE3A5F`; Workbook Packages row 29. |
| Grounding / Bonding | Applicable interface — connection to the facility ground grid at two points; NGR coordination on the 6.9 kV side. | `INTERFACE_REGISTER.csv` row `IFC-868150D715`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. |
| Area / Exterior Lighting | Applicable interface — lighting at the transformer pad for operations and maintenance per facility lighting basis. | `INTERFACE_REGISTER.csv` row `IFC-A7AA374E9F`; Workbook Packages row 29. |
| I&C / Control Cabling | Applicable interface — protective relay, monitoring, alarm, and tap-changer control wiring to the local protection cabinet / electrical building. | `INTERFACE_REGISTER.csv` row `IFC-A771D8D087`; Workbook Packages row 29. |
| Communications / Network | Applicable interface — monitoring/data acquisition to the plant control system. Specific protocol `TBD`. | `INTERFACE_REGISTER.csv` row for `PKG-027` (Communications / Network); Workbook Packages row 29. |
| Maintenance Access | Applicable interface — clearances around the transformer for CEC compliance, oil sampling, bushing access, and tap-changer maintenance. | `INTERFACE_REGISTER.csv` row for `PKG-027` (Maintenance Access); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer spacing paragraph. |
| Structural / Foundations / Supports | Applicable interface — precast concrete bearing foundation or structural steel transformer base; secondary containment per CEC and DBM guidance. | `INTERFACE_REGISTER.csv` row for `PKG-027` (Structural / Foundations / Supports); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformers paragraphs. |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-027`. |
| Facility integration, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-027`. |
| Foundation and containment | Precast concrete bearing foundation or structural steel base; secondary containment to be reviewed and limited where practical per DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformers paragraphs. |
| Spacing / CEC clearances | CEC clearance and spacing requirements apply to large oil-filled transformers. Specific values `TBD` pending detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph. |
| Installation location | `TBD`. Source identifies the facility 13.8 kV switchgear and 6.9 kV electrical buildings (e.g., "820-1 6.9kV Inlet / Sales Compressor Electrical Building") but does not assign `TXP-8301-1` to a specific pad, building, or area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and switchgear paragraphs. |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-027-01_scope-of-work`.
- `PACKAGE_REGISTER.csv`, row `PKG-027`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-027`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-027-01_scope-of-work`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for 13.8 kV switchgear distribution, 6.9 kV services, transformer foundations/spacing, and grounding.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no PKG-027-specific match was located.
