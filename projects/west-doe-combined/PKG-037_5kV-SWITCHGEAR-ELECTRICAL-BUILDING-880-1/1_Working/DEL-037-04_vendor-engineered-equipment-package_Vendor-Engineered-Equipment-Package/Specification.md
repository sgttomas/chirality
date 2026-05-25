# Specification: DEL-037-04_vendor-engineered-equipment-package

## Scope

This specification defines normative requirements for the **Vendor Engineered Equipment Package** for `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)`. The deliverable is a Package Vendor production unit comprising:

- engineering and design of the prefabricated electrical building (880-1) and its switchgear lineup,
- fabrication and supply of the physical equipment package, and
- the vendor package design basis and datasheet set.

In scope:
- the building enclosure and its installed electrical equipment as required by detailed design,
- the medium-voltage switchgear lineup designated by the workbook title "5kV",
- vendor-supplied auxiliary equipment within the building (e.g., control power, protective relaying, station service, lighting, HVAC interfaces, cable terminations),
- the vendor design basis and datasheet set documenting the package.

Out of scope (governed by other deliverables and the EPC Integrator):
- facility integration, interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration (`PACKAGE_REGISTER.csv` row `PKG-037`),
- the EPC Scope of Work (`DEL-037-01`), Package Datasheet (`DEL-037-02`), Construction Work Package (`DEL-037-03`), Vendor Document Turnover Package (`DEL-037-05`), and EPC Vendor Package Review and Acceptance (`DEL-037-06`).

## Requirements

| # | Requirement | Basis |
|---|---|---|
| R-037-04-01 | The vendor package shall be developed from the EPC package Scope of Work (`DEL-037-01`) and Package Datasheet (`DEL-037-02`). | `_CONTEXT.md`; `SCOPE_LEDGER.csv` `SOW-0038` |
| R-037-04-02 | The building shall be a prefabricated, modular electrical building suitable for installation in a general-purpose area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| R-037-04-03 | The building shall house, as required by detailed design, the applicable subset of: medium-voltage switchgear, medium-voltage motor control centers, reduced-voltage soft starters, medium-voltage VFDs, 600 V MCCs, 120 V AC UPS systems with battery banks and distribution panels, 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, and network racks. The exact constituents for 880-1 are `TBD` pending detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| R-037-04-04 | Medium-voltage equipment design shall be consistent with the DBM medium-voltage service basis (13.8 kV, 6.9 kV, 4.160 kV — all 3-phase, 3-wire, 60 Hz, low-resistance grounded). The mapping of the workbook "5kV" label to a specific facility service voltage is an **ASSUMPTION (likely 4.160 kV / 5 kV insulation class)** pending human ruling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage and service table; Workbook Packages row 39 |
| R-037-04-05 | Switchgear breaker control circuits and protective relays shall be supplied from 120 VAC and/or 125 VDC UPS services per detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row |
| R-037-04-06 | Major electrical equipment in the building shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp shall have separate copper ground conductors sized per CEC. Applicability to specific vendor switchgear lineup elements shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| R-037-04-07 | Medium-voltage cables originating in or terminating at the vendor switchgear shall conform to the DBM cable basis: 6.9 kV — three-conductor copper TECK, 8 kV rated, 100 percent insulation, shielded; 4.160 kV — three-conductor copper TECK, 5 kV rated, 100 percent insulation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage cable table |
| R-037-04-08 | Cable tray and conduit routing inside the building shall not interfere with maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| R-037-04-09 | The vendor package shall provide compliant interface points for all twelve PKG-037 interface types: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-037`; Workbook Packages row 39 |
| R-037-04-10 | The Package Vendor shall produce a package design basis document and a complete equipment datasheet set covering the building enclosure, switchgear lineup, and ancillary equipment (`ART-8870C8E2DE`). | `ARTIFACT_REGISTER.csv` row `ART-8870C8E2DE` |
| R-037-04-11 | The Package Vendor shall deliver the engineered physical equipment package (`ART-7491C7E69C`) as the package's primary fabricated/supplied artifact. | `ARTIFACT_REGISTER.csv` row `ART-7491C7E69C` |
| R-037-04-12 | Where this specification conflicts with a unit-specific or vendor requirement that is stricter or more specific, the stricter or more specific requirement shall govern. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, scope precedence paragraph |

## Standards

| Standard / source | Applicability to PKG-037 | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding conductor sizing for distribution transformers, panelboards, and large motors. | Referenced in DBM; specific clause `location TBD` |
| DBM Deepcut Electrical Design Basis (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) | Medium-voltage service basis, electrical buildings basis, UPS, grounding, cabling, cable tray, conduit. | Accessible source |
| ANSI / IEEE / CSA medium-voltage switchgear standards | Standard reference set for 5 kV class metal-clad switchgear. | **ASSUMPTION: likely applicable**; not cited in accessible source slices |
| `26020-Package_Requirements.docx` | Project-wide package requirements document. | No PKG-037 / 880-1 / 5kV switchgear match found in this run; `location TBD` |

## Verification

| Requirement | Verification approach |
|---|---|
| R-037-04-01 | Document review confirming vendor package is traceable to `DEL-037-01` SOW and `DEL-037-02` Package Datasheet inputs. |
| R-037-04-02, R-037-04-03 | Vendor design basis review; submittal of building general arrangement and equipment list against the DBM electrical buildings paragraph. |
| R-037-04-04 | Human ruling on the "5kV" → facility service voltage mapping; verification by reviewing switchgear nameplate ratings against the selected service voltage. |
| R-037-04-05 | Schematic review of breaker control and protective relay supply against UPS services basis. |
| R-037-04-06 | Grounding plan review against the DBM grounding basis and CEC sizing rules. |
| R-037-04-07 | Cable schedule review against DBM medium-voltage cable basis. |
| R-037-04-08 | Cable tray and conduit routing review against maintenance access requirements. |
| R-037-04-09 | Interface compliance check against `INTERFACE_REGISTER.csv` rows for `PKG-037` by EPC Integrator. |
| R-037-04-10, R-037-04-11 | Receipt and acceptance of vendor design basis, datasheet set, and physical package, recorded against `ART-7491C7E69C` and `ART-8870C8E2DE`. |
| R-037-04-12 | EPC Integrator precedence ruling on any conflict surfaced during vendor document review (`DEL-037-06`). |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`, `ARTIFACT_REGISTER.csv`):

- Vendor engineered physical equipment package (`ART-7491C7E69C`).
- Vendor package design basis and datasheet set (`ART-8870C8E2DE`).

Supporting documentation expected from the vendor package:

- Building general arrangement, equipment list, and single-line diagrams.
- Switchgear datasheet(s), bus and breaker schedule, protective relay schedule.
- Grounding plan and cable schedule.
- Interface drawings for the twelve PKG-037 interface types.
- Vendor design basis document tying selections to DBM and Package Datasheet (`DEL-037-02`) inputs.
