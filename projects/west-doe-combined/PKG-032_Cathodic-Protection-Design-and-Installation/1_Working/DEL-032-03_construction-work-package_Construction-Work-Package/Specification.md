# Specification: DEL-032-03_construction-work-package

## Scope

### In scope

The Construction Work Package for `PKG-032 Cathodic Protection Design and Installation` describes how the cathodic protection (CP) package shall be physically installed, built, inspected, turned over, and tied into the larger 03-25 Comp and Liquids facility. The deliverable covers:

- Installation of the CP equipment package on its foundation(s) within the facility electrical scope.
- Tie-in of CP power feed(s), grounding/bonding coordination (including required isolation/decoupling), CP monitoring and control cabling, and CP communications/network cabling per the four interface types declared for `PKG-032`.
- Workface planning evidence (installation and tie-in workface plan) and construction interface, inspection, and turnover checklist evidence.

Source: `_CONTEXT.md` scope; `DELIVERABLE_REGISTER.csv` row `DEL-032-03_construction-work-package`; `INTERFACE_REGISTER.csv` rows `IFC-C2719906C1`, `IFC-F1FE9DF9DD`, `IFC-4D092EC70F`, `IFC-8594557BD3`.

### Out of scope

- Package engineering, package design, vendor documentation, and the physical equipment package — Package Vendor scope (`PACKAGE_REGISTER.csv` row `PKG-032`).
- Process-side construction work outside CP installation and CP tie-ins.
- Cross-facility scopes belonging to 04-25, NRM, or pipeline contractors except at defined facility-side tie-in points (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Commercial and Facility Interfaces and Exclusions sections).

## Requirements

| Req ID | Requirement | Source / status |
|---|---|---|
| R-032-03-01 | The construction work package shall execute the CP installation as part of the facility electrical design scope, consistent with the DBM identification of cathodic protection as in-scope electrical work. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Design Scope (line 718, 770) |
| R-032-03-02 | The construction work package shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Miscellaneous Facilities (line 661) |
| R-032-03-03 | CP power feed installation shall comply with project electrical specifications and the DBM cable/tray/grounding basis; power circuits shall be separated from control and instrument circuits by distance, shielding, or routing as required. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Cable and Power Circuit Segregation (line 768) |
| R-032-03-04 | CP system installation shall be coordinated with facility grounding/bonding so that cathodic protection effectiveness is preserved; isolation/decoupling between protected assets and the facility ground grid shall be implemented per detailed design (specific devices and locations `TBD`). ASSUMPTION: CP-to-ground-grid isolation is required for impressed-current systems on facilities with extensive grounding; confirm against vendor design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Cable and Bonding paragraph (line 768); ASSUMPTION |
| R-032-03-05 | CP monitoring/control cabling (rectifier status, test-station leads, remote monitoring) shall be installed and terminated per project cable schedules and the DBM controls/communications basis; control protocol selection (hardwired, Modbus TCP/IP, protocol converter) shall follow the facility package/third-party interface rules. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Package and Third-Party Interfaces (line 812) |
| R-032-03-06 | The construction work package shall include workface planning evidence (installation and tie-in workface plan) and construction interface, inspection, and turnover checklist evidence as artifacts. | `ARTIFACT_REGISTER.csv` rows `ART-655045CC72`, `ART-7FA44ED0D3`, `ART-9C1116778C` |
| R-032-03-07 | Construction execution shall account for site conditions including the -40 deg C to +35 deg C ambient range, winter operation, snow loading, and the unconfirmed geotechnical basis (treated as design placeholder until the final geotechnical report is accepted). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Design Implications (line 145); Foundation paragraph (line 141) |
| R-032-03-08 | Construction tie-in timing for CP shall be established jointly with adjacent package construction (tanks, vessels, buried piping) so that bonding, isolation, anode placement, and test-station leads are installed before associated assets become inaccessible. PROPOSAL pending vendor sequence. | PROPOSAL; not directly stated in source |
| R-032-03-09 | Pre-commissioning shall include native potential survey, system energization, polarized potential acceptance criteria, and interference testing with adjacent buried metallic systems. Acceptance values and survey procedure `TBD` pending vendor CP design and project commissioning plan. | Source gap; `TBD` |
| R-032-03-10 | Construction interface and turnover checklist shall document CP system handover to operations, including rectifier energization records, test-station as-built records, and initial potential survey records. | `ARTIFACT_REGISTER.csv` row `ART-9C1116778C` |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Governs electrical installation including grounding/bonding basis used for the facility. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Standards table (line 893); location TBD for CP-specific clauses |
| Project electrical specifications | Cable tray, conduit, grounding, and bonding shall comply with project electrical specifications. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Cable paragraph (line 768); document path TBD |
| Project painting/coating/corrosion specifications | Coordination of CP with coatings and corrosion basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Standards table (line 897); document path TBD |
| NACE/AMPP CP standards (e.g., SP0169, SP0286, SP0177) | ASSUMPTION: industry-standard CP design/installation/safety references typically apply but are not cited in accessible source slices for PKG-032. | ASSUMPTION; location TBD |
| Area classification basis (API RP 505; Class I Zone 2, Gas Groups IIA/IIB) | Applies to electrical equipment in classified areas, including CP rectifiers if located in hazardous areas. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification (line 722) |
| NBCC / geotechnical report | Civil basis for foundations, including any CP equipment shelter or rectifier foundation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Standards table (line 895); Foundation paragraph (line 141) |

## Verification

| Req ID | Verification approach | Records |
|---|---|---|
| R-032-03-01 | Construction inspection records confirming CP installation aligns with facility electrical scope. | Installation inspection records |
| R-032-03-02 | Document control check confirming plot-plan and equipment-list alignment prior to IFC. | IFC release record |
| R-032-03-03 | Electrical installation inspection; power/control segregation walkdown. | Inspection report |
| R-032-03-04 | Continuity and isolation tests at CP-to-ground-grid decoupling points; confirmation of isolating joints/flange kits where specified. | Test records |
| R-032-03-05 | Cable schedule completion check; termination inspection; loop check for CP monitoring signals. | Loop check records |
| R-032-03-06 | Document control verification that workface plan and turnover checklist exist and are signed. | Document register |
| R-032-03-07 | Construction QA confirms winter-operation provisions and geotechnical caveats applied. | Construction QA records |
| R-032-03-08 | Construction sequence/look-ahead alignment with adjacent package install schedule. | Sequencing record (`TBD`) |
| R-032-03-09 | Native potential survey, energization records, polarized potential acceptance test, interference test results. | Commissioning records (`TBD` acceptance values) |
| R-032-03-10 | Turnover checklist signed by Construction, EPC Integrator, and Operations. | Turnover package |

## Documentation

- Construction work package document (`ART-655045CC72`).
- Installation and tie-in workface plan (`ART-7FA44ED0D3`).
- Construction interface and turnover checklist (`ART-9C1116778C`).
- Inspection and test records (per requirement table above).
- CP commissioning records (native potentials, energized potentials, interference survey) — `TBD` pending vendor commissioning procedure.
