# Specification: DEL-023-04_vendor-engineered-equipment-package

## Scope

This Specification governs the Package Vendor production unit for `PKG-023` — `MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD`. The vendor production unit covers package engineering, package design, fabrication/supply, and delivery of the physical equipment package developed from the EPC package Scope of Work (`DEL-023-01`) and Package Datasheet (`DEL-023-02`), together with the vendor's own design basis and datasheet set.

**In scope**

- Package-internal engineering and design of the medium-voltage variable frequency drive package and its supporting equipment.
- Fabrication, factory testing, and supply of the physical equipment package.
- Production of the vendor package design basis and the vendor datasheet set.
- Definition of all package-side termination points for the six declared `PKG-023` interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).

**Out of scope (EPC Integrator)**

- Facility-level integration, tie-ins, constructability, procurement/construction coordination, and facility integration review (handled by `DEL-023-06` and adjacent EPC deliverables).
- Vendor document register management and turnover packaging (handled by `DEL-023-05`).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-023-04-01 | The vendor package shall be engineered, designed, fabricated, and supplied as one production unit consistent with the EPC Scope of Work and EPC Package Datasheet for `PKG-023`. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` |
| REQ-023-04-02 | The package shall provide a 4160 V class variable frequency drive sized for a nominal 1500 HP, 4160 V, 3-phase, 60 Hz motor application as identified in the workbook package title; final motor electrical and process duty parameters shall be confirmed against the accepted EPC Package Datasheet. (`ASSUMPTION` until the EPC Package Datasheet content is accepted.) | Workbook Packages row 25; `_CONTEXT.md` |
| REQ-023-04-03 | The vendor package shall expose package-side termination/connection points for each declared `PKG-023` interface: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-023` |
| REQ-023-04-04 | Major electrical equipment within the package shall comply with the DBM grounding rule (direct connection to the ground grid at two points; separate copper ground conductors for distribution transformers, panelboards, and three-phase motors larger than 100 HP, sized per CEC), subject to detailed-design confirmation of applicability to the PKG-023 vendor package boundary. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding slice |
| REQ-023-04-05 | Where any package component or VFD-fed motor is installed in a Zone 2 area, it shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2961 |
| REQ-023-04-06 | Cable tray and conduit routing supplied as part of the vendor package shall not interfere with maintenance access to package equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray / conduit slice |
| REQ-023-04-07 | Cable types for VFD-fed motor circuits shall be coordinated with the DBM cable type basis. (DBM specifies copper TECK cable for low-voltage power cable fed from VFDs; the medium-voltage VFD-fed motor cable type for the 4160 V class is `TBD` pending source-supported confirmation.) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3013 |
| REQ-023-04-08 | The vendor package shall be packaged for the deliverable type "Vendor Package Production Unit" and shall provide the artifacts listed in the Documentation section. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` |
| REQ-023-04-09 | The detailed drive topology, harmonic-mitigation strategy, cooling method, enclosure rating, and supply-side bus assignment are `TBD` and shall be fixed in the vendor design basis when source-supported. | Source gap (no PKG-023-specific source slice) |
| REQ-023-04-10 | If the package is to be housed inside a prefabricated modular electrical building, building accommodation shall be coordinated with EPC Integrator under the Maintenance Access and Structural / Foundations / Supports interfaces. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2973 |

## Standards

| Standard / source | Status / location |
|---|---|
| EPC Scope of Work (`DEL-023-01`) | Governing upstream document for vendor package scope. `location TBD` until issued and accepted. |
| EPC Package Datasheet (`DEL-023-02`) | Governing upstream document for vendor technical handoff. `location TBD` until issued and accepted. |
| Project Design Basis Manual (DBM) — electrical sections | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (medium-voltage MCC/VFD/MV-soft-starter, motor voltage class, Zone 2, electrical buildings, grounding, cable/conduit). |
| Canadian Electrical Code (CEC) | Referenced by DBM for grounding conductor sizing. `location TBD` for clause-level requirements. |
| `26020-Package_Requirements.docx` | Project package-requirements document; not parsed for a PKG-023-specific match. `location TBD`. |

## Verification

| Req ID | Verification approach |
|---|---|
| REQ-023-04-01 | Review of vendor package design basis and vendor datasheet set against EPC Scope of Work and EPC Package Datasheet during EPC Vendor Package Review and Acceptance (`DEL-023-06`). |
| REQ-023-04-02 | Review of vendor motor/drive ratings against accepted EPC Package Datasheet. |
| REQ-023-04-03 | Interface-by-interface check using the package interface requirements matrix against `INTERFACE_REGISTER.csv` rows for `PKG-023`. |
| REQ-023-04-04 | Grounding design review against the DBM grounding slice; verification of two-point ground connection and separate copper ground conductors where applicable. |
| REQ-023-04-05 | Area-classification check at detailed design; confirmation of equipment marking and temperature code against the area-classification drawing. |
| REQ-023-04-06 | Routing review during detailed design and at construction turnover. |
| REQ-023-04-07 | Cable schedule review against DBM cable type basis; resolution of MV cable type `TBD`. |
| REQ-023-04-08 | Verification that the artifact set listed in Documentation is present in the vendor package turnover (`DEL-023-05`). |
| REQ-023-04-09 | Acceptance of vendor design basis updates that close each `TBD` against source. |
| REQ-023-04-10 | Coordination check with EPC Integrator on building accommodation, lifting paths, and maintenance access. |

## Documentation

The vendor package shall deliver, at minimum, the artifact set declared in the deliverable register:

- Vendor engineered physical equipment package (`ART-21EF7BEFD2`).
- Vendor package design basis and datasheet set (`ART-B3660C159F`).

Vendor documentation submittals, the vendor document register, and turnover records are produced under `DEL-023-05_vendor-document-turnover-package` and are not duplicated here.
