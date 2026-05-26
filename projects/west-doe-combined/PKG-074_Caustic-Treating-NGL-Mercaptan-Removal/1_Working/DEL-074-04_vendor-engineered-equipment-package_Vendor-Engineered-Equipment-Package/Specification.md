# Specification: Vendor Engineered Equipment Package

## Scope

This specification governs the DEL-074-04 Vendor Engineered Equipment Package for PKG-074 Caustic Treating (NGL Mercaptan Removal). The package is a Package Vendor production unit covering engineering, design, fabrication/supply, and the physical equipment package for a non-regenerative caustic NGL mercaptan treating system, developed from the EPC package Scope of Work (DEL-074-01) and Package Datasheet (DEL-074-02).

The package covers SOW-0059, SOW-0060, SOW-0061, and SOW-0062 and carries the workbook-recorded mechanical interface facts for PKG-074. It excludes EPC Integrator-owned activities (facility integration, tie-ins, constructability, procurement/construction coordination, facility-level integration), the EPC Construction Work Package (DEL-074-03), the Vendor Document Turnover Package (DEL-074-05), and the EPC Vendor Package Review and Acceptance (DEL-074-06). Source-dependent values not present in locally accessible references remain TBD.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-074-04-001 | The vendor package shall be identified as PKG-074 Caustic Treating (NGL Mercaptan Removal), Mechanical discipline, WBS 01, CoA 26020-01-27-002. | PACKAGE_REGISTER.csv, PKG-074 | Check package identity table against Gate 7 register. |
| REQ-074-04-002 | The vendor package shall implement a non-regenerative caustic treating process on cooled C3+ NGL downstream of the de-ethanizer. | 4-25_Deepcut_DBM.md, Current-Scope NGL Mercaptan Treating | Confirm process basis matches DBM unit type. |
| REQ-074-04-003 | The vendor package shall be sized for a design rate of 2,385 m3/d / 15,000 bbl/d. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters | Check vendor design basis against the rate. |
| REQ-074-04-004 | The vendor package shall carry inlet/outlet design pressures of 2,213 kPag inlet and 1,978 kPag outlet, with low/high pressure cases TBC. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters | Check vendor design pressure schedule. |
| REQ-074-04-005 | The vendor package shall be designed for inlet temperatures of 26.7 deg C low, 43.3 deg C design, 48.8 deg C high. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters | Check vendor temperature design basis. |
| REQ-074-04-006 | Fresh caustic shall be 50 wt% NaOH; circulating process caustic concentration is 14.7 wt% NaOH (TBC). | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters | Check vendor chemistry basis. |
| REQ-074-04-007 | The vendor package shall provide 1 x 400 bbl fresh caustic tank, 1 x 400 bbl spent caustic tank, and 1 x 400 bbl DSO tank, atmospheric and heated/insulated, with the connection and protection conventions stated in the DBM. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities; Disulphide Oil, Spent Caustic, and Waste Amine | Check vendor tank schedule and tie-in list. |
| REQ-074-04-008 | NGL contactor caustic outlet filters shall be independent vessels from the contactor, provided as 2 x 100%. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities | Check vendor equipment list. |
| REQ-074-04-009 | Water wash and coalescing filtration shall be provided downstream of the contactor to remove entrained caustic before molecular sieve dehydration. Water wash recycle pumps shall be single-stage vertical inline centrifugal, single mechanical seal, 2 x 100% sparing. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities | Check vendor pump and filter schedules. |
| REQ-074-04-010 | A pressurized caustic drain drum (V-6940-1) shall be provided, heated, insulated, with demister, sized with K factor less than 0.2; vapours route to the stabilizer overheads compressor first-stage suction; remaining caustic flows on level control to spent caustic storage. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities; SOC inlet source table | Check drum datasheet and tie-ins. |
| REQ-074-04-011 | All caustic treating equipment shall be installed indoors in the Mercaptan Treating Unit building or immediately adjacent area to mitigate caustic freezing/crystallization risk. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities | Check building/segregation arrangement. |
| REQ-074-04-012 | The building shall include water safety showers; activation shall provide a discrete control-room alert. Shower quantity and location remain TBD. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities | Check safety shower P&ID and alarm logic. |
| REQ-074-04-013 | No aluminum materials shall be installed in the caustic building; insulation cladding/straps in caustic exposure areas shall be stainless steel; caustic storage tanks shall use polymer or other caustic-compatible materials. Building floor material and caustic tank materials remain TBD pending detailed engineering. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities | Check vendor material specifications. |
| REQ-074-04-014 | The vendor package shall carry the workbook applicable interface types for PKG-074: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | INTERFACE_REGISTER.csv, IFC rows for PKG-074 (IFC-D5E5A136D0 through IFC-00C2D196EA) | Check the interface matrix against the register rows. |
| REQ-074-04-015 | Spent caustic tank vapours and DSO off-gas shall route to the incinerator located at the 3-25 facility through a knock-out drum upstream of the incinerator stack. Supplemental fuel gas rate, incinerator flow basis, and shared-facility operational responsibility are TBD. | 4-25_Deepcut_DBM.md, Incinerator Interface | Check incinerator tie-in scope and operational responsibility log. |
| REQ-074-04-016 | The vendor package shall be designed as common equipment — single train serves the facility, with provision for take-out-of-service for maintenance. | 4-25_Deepcut_DBM.md, Common Equipment discussion | Check sparing philosophy and maintenance access basis. |
| REQ-074-04-017 | The vendor package shall produce a design basis and datasheet set as the design evidence artifact, plus the physical equipment package as the production artifact. | ARTIFACT_REGISTER.csv, ART-04D78DC493; ART-7D22DB55EB | Check artifact register against vendor deliverable list. |
| REQ-074-04-018 | The vendor package shall be developed from the EPC Scope of Work (DEL-074-01) and EPC Package Datasheet (DEL-074-02) as the authoritative EPC handoff basis. ASSUMPTION: drafted on package-grouping heuristic until DEL-074-01 and DEL-074-02 are formally accepted. | DELIVERABLE_REGISTER.csv, DEL-074-01, DEL-074-02, DEL-074-04 | Confirm vendor design basis cites EPC SOW and EPC Package Datasheet. |
| REQ-074-04-019 | The vendor package shall maintain a source-limited requirements closure record because detailed mechanical/process specification text resides in the 26020-Package_Requirements.docx binary source that is not locally readable in this run; content depending solely on that source is TBD. | _REFERENCES.md, Missing / Deferred References; ARTIFACT_REGISTER.csv, ART-EDAC8A3AB7 | Check closure record exists and lists deferred binary-source items. |

## Standards

| Standard / basis | Application | Source |
|---|---|---|
| ASME B31.3-2022 | Process piping design basis for the vendor package and tie-ins. | 4-25_Deepcut_DBM.md, Governing Codes, Standards, Specifications, and Studies |
| ASME BPVC.VIII.1-2023 | Pressure vessel construction basis (contactor outlet filters, drain drum, exchangers, vessels). | 4-25_Deepcut_DBM.md, Governing Codes, Standards, Specifications, and Studies |
| Modified API-650 / API-2000 | Atmospheric storage tank design and venting basis (fresh caustic, spent caustic, DSO tanks). | 4-25_Deepcut_DBM.md, Atmospheric tank basis |
| Vendor proprietary process basis | Third-party proprietary process provider supplies the detailed engineering package for the non-regenerative caustic unit. | 4-25_Deepcut_DBM.md, Current-Scope NGL Mercaptan Treating |
| 26020-Package_Requirements.docx, package heading 28 | Detailed mechanical package scope and vendor documentation requirements. | _REFERENCES.md; ARTIFACT_REGISTER.csv, ART-EDAC8A3AB7 (location TBD; binary source not locally readable) |

## Verification

| Verification item | Acceptance basis |
|---|---|
| Package identity check | Matches Gate 7 PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv entries for PKG-074 / DEL-074-04. |
| Process basis check | Vendor design implements non-regenerative caustic treating per 4-25_Deepcut_DBM.md, Current-Scope NGL Mercaptan Treating. |
| Design parameter check | Vendor datasheets carry the rate, pressures, temperatures, and caustic concentrations stated in the DBM design parameters table; TBC items are flagged. |
| Equipment list check | Vendor equipment list includes contactor/mixer, outlet filters (2 x 100%), water wash + coalescer, recycle pumps (2 x 100%), pressurized caustic drain drum (V-6940-1), fresh/spent caustic and DSO tanks (each 1 x 400 bbl), heater(s), and circulation/transfer pumps. |
| Interface check | Vendor interface matrix includes the 13 PKG-074 workbook interface types cited to INTERFACE_REGISTER.csv. |
| Materials check | No aluminum in caustic building; stainless steel insulation cladding/straps in caustic exposure areas; caustic-compatible tank materials; building floor and tank materials open as TBD. |
| Indoor installation check | All caustic equipment located within or adjacent to the Mercaptan Treating Unit building. |
| Safety shower check | Water safety showers present with discrete control-room alert on activation; quantity/location logged as TBD. |
| Incinerator interface check | DSO and spent caustic vent routing to 3-25 incinerator through upstream knock-out drum, with TBD items captured. |
| Open input check | Process provider selection, contactor stages, caustic concentration confirmation, winter vapour pressure, high-ethane case, low/high pressure cases, and material selections logged as open. |
| Cross-document consistency | Datasheet, Specification, Guidance, Procedure use consistent equipment names, tag numbers, interface labels, and source basis. |

## Documentation

The vendor package should include, at minimum:

- Vendor package design basis and datasheet set (ART-04D78DC493).
- Vendor engineered physical equipment package documentation (ART-7D22DB55EB).
- Major included equipment evidence aligned to ART-EDAC8A3AB7 (caustic contactor/mixer, caustic outlet filtration, water wash and coalescing equipment, caustic regeneration equipment, heaters/exchangers, circulation and transfer pumps, pressurized caustic drain drum, DSO handling, caustic storage interfaces, incinerator interface, instrumentation, controls, building-contained caustic equipment).
- Interface matrix for the 13 PKG-074 workbook interface types.
- Source-limited requirements closure record listing deferred binary-source items, TBC values, and detailed-engineering open items.
- Materials and indoor-installation compliance record.
- Safety shower and control-room alarm documentation.
