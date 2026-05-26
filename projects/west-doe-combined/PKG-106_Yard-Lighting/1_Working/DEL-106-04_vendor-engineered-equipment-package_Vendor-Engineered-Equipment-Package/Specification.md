# Specification — DEL-106-04 Vendor Engineered Equipment Package (Yard Lighting)

## Scope

This specification defines what the Package Vendor must engineer, design, and supply as the physical equipment package for `PKG-106` Yard Lighting, and what is excluded from this deliverable.

**In scope:**
- Vendor package engineering and design (photometric layout, fixture and pole selection, support and foundation interface definition, wiring within the vendor scope) for the yard / outdoor / area-lighting portion of the facility.
- Vendor package design basis and datasheet set (vendor-side documentation supporting the engineered package).
- Fabrication and supply of the physical equipment package (fixtures, poles/mast poles where applicable, vendor-scope wiring, vendor-supplied mounting hardware) per the EPC Scope of Work (`DEL-106-01`) and EPC Package Datasheet (`DEL-106-02`).
- Package compliance with the three declared package interface types: Electrical Power; Grounding / Bonding; Area / Exterior Lighting (`INTERFACE_REGISTER.csv` rows IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087).
- Vendor compliance with the lighting design basis text in the accepted DBM (`4-25_Deepcut_DBM.md` `## Lighting and Receptacles`).

**Out of scope (this deliverable):**
- EPC integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) — owned by EPC Integrator per `PACKAGE_REGISTER.csv` row PKG-106.
- EPC Scope of Work (`DEL-106-01`) and EPC Package Datasheet (`DEL-106-02`) authoring.
- Construction Work Package authoring (`DEL-106-03`).
- Vendor Document Turnover Package itself (`DEL-106-05`) — turnover records are an adjacent deliverable.
- EPC Vendor Package Review and Acceptance (`DEL-106-06`).
- Cathodic protection engineering and supply (excluded from facility design scope per DBM `## Cathodic Protection`).
- Indoor MCC room, control room, office, and warehouse interior lighting where those are inside other building/package scopes (yard-scope deliverable is the outdoor/area subset; ASSUMPTION pending EPC SOW/Datasheet resolution).

## Requirements

| ID | Requirement | Source / Rationale |
|---|---|---|
| VEEP-REQ-001 | Vendor shall deliver the engineered physical equipment package and the vendor package design basis and datasheet set as the two anticipated artifacts. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row DEL-106-04 |
| VEEP-REQ-002 | Vendor engineering, design, fabrication, and supply shall be developed from the EPC Scope of Work (`DEL-106-01`) and the EPC Package Datasheet (`DEL-106-02`). | `_CONTEXT.md` Scope; decomposition row DEL-106-04 |
| VEEP-REQ-003 | All lighting supplied in the vendor package shall be LED type. | DBM-Deepcut `## Lighting and Receptacles` ("All lighting shall be LED type…") |
| VEEP-REQ-004 | Process area and outdoor lighting fixtures shall be LED fixtures. | DBM-Deepcut `## Lighting and Receptacles` paragraph 2 |
| VEEP-REQ-005 | General-purpose lighting shall be designed for 120/208 V, 3 phase, 4 wire, 60 Hz, solidly grounded service, fed from the nearest Power Distribution Centre. | DBM-Deepcut Electrical Services table (Lighting and utility services row); `## Lighting and Receptacles` paragraph 1 |
| VEEP-REQ-006 | Fixtures shall be suitable for the area classification in which they are installed; vendor shall identify required fixture certifications per location. | DBM-Deepcut `## Lighting and Receptacles` paragraph 1 |
| VEEP-REQ-007 | Exterior / yard lighting shall implement the regulatory light-pollution controls: downcast floodlights only (no horizontally aimed floodlights); selective minimization of exterior lighting to working areas; photocell or switch control; and mast pole locations away from the pad edge where mast poles are required. | DBM-Deepcut `## Lighting and Receptacles` final paragraph |
| VEEP-REQ-008 | Vendor-supplied lighting branch-circuit conductor sizing shall support facility-side selection of conductors not larger than #10 AWG where possible by locating RDCs closer to lighting loads (vendor coordinates termination ratings and circuit lengths with EPC Integrator). | DBM-Deepcut cable section paragraph (lighting and electric heat tracing conductors) |
| VEEP-REQ-009 | Where the vendor supplies shop-fabricated/erected buildings or building-mounted assemblies that include lighting, building lighting wiring shall use rigid conduit, sealed at area-classification boundaries, with minimum conduit size 21 mm (3/4 in), CEC-compliant. (ASSUMPTION on applicability — only if the vendor scope includes shop-built buildings/assemblies.) | DBM-Deepcut conduit paragraph preceding `## Lighting and Receptacles`; ASSUMPTION |
| VEEP-REQ-010 | Vendor design shall not mix receptacle circuits with lighting circuits within vendor-supplied panels or branch wiring. | DBM-Deepcut `## Lighting and Receptacles` receptacles paragraph |
| VEEP-REQ-011 | Vendor package shall provide grounding/bonding provisions consistent with the declared package interface "Grounding / Bonding" (IFC-DA0D60681B) to allow EPC Integrator to tie into facility grounding. | `INTERFACE_REGISTER.csv` row IFC-DA0D60681B; facility-integration ownership |
| VEEP-REQ-012 | Vendor package shall provide electrical-power termination provisions consistent with the declared package interface "Electrical Power" (IFC-6FCF1B30D6) for facility-side feed from the nearest RDC at 120/208 V. | `INTERFACE_REGISTER.csv` row IFC-6FCF1B30D6; DBM Electrical Services table |
| VEEP-REQ-013 | Vendor package shall expose an "Area / Exterior Lighting" interface (IFC-ED86F51087) defining photometric coverage, mounting, and control points sufficient for EPC integration and acceptance. | `INTERFACE_REGISTER.csv` row IFC-ED86F51087 |
| VEEP-REQ-014 | Vendor package documentation shall include the vendor package design basis and datasheet set sufficient to support `DEL-106-05` vendor document turnover and `DEL-106-06` EPC review and acceptance. | `_CONTEXT.md` Anticipated Artifacts; decomposition rows DEL-106-05, DEL-106-06 |
| VEEP-REQ-015 | Quantitative photometric criteria (lux levels, uniformity ratios), pole height, spacing, foundation loads, fixture catalogue numbers, and lighting control schedule shall be defined by vendor design subject to EPC review; values are TBD in source basis and shall be carried in the vendor package design basis and datasheet set. | location TBD; ASSUMPTION on EPC-review gate |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Conduit material/wiring methods; area-classification rules; supports | DBM-Deepcut conduit paragraph preceding `## Lighting and Receptacles` ("Complete conduit systems… shall comply with the Canadian Electrical Code and the applicable area classification.") |
| Applicable building code (exit/emergency lighting backup) | Where vendor scope includes building-mounted lighting requiring battery-backed exit/emergency fixtures | DBM-Deepcut `## Lighting and Receptacles` paragraph 2 (battery backup as required by building code); applicability TBD for yard scope |
| Regulatory light-pollution requirements (British Columbia jurisdiction) | Yard / exterior lighting design controls | DBM-Deepcut `## Lighting and Receptacles` final paragraph; jurisdiction implied by site (DBM `## Permitting and External Basis`) — location TBD for the specific regulation citation |
| Hazardous area classification standards (CEC Section 18 / equivalent) | Fixture suitability where installed in classified areas | DBM-Deepcut `## Lighting and Receptacles` paragraph 1; specific clause location TBD |
| Project package specifications (`26020-Package_Requirements.docx`) | Vendor package general requirements | `_REFERENCES.md`; PKG-106-specific slice not extracted (location TBD) |

## Verification

| Requirement | Verification Approach |
|---|---|
| VEEP-REQ-001 | Package Vendor delivers both artifacts; logged in `DEL-106-05` vendor document register and accepted in `DEL-106-06`. |
| VEEP-REQ-002 | Cross-reference matrix in vendor design basis citing rows of `DEL-106-01` SOW and `DEL-106-02` Package Datasheet. |
| VEEP-REQ-003, REQ-004 | Vendor datasheet declares LED technology for every supplied fixture; EPC review verifies. |
| VEEP-REQ-005 | Vendor electrical schedule shows 120/208 V supply origin (nearest RDC); EPC integration review confirms feeder availability. |
| VEEP-REQ-006 | Vendor area-classification fixture schedule cross-checked against the facility hazardous area drawings during EPC review. |
| VEEP-REQ-007 | Photometric and layout drawings show downcast distribution, working-area minimization, photocell/switch controls, and mast-pole offset; EPC review confirms compliance. |
| VEEP-REQ-008 | Branch-circuit schedule shows conductor sizing and assumed RDC proximity; EPC confirms during integration. |
| VEEP-REQ-009 | Where applicable, vendor wiring drawings show rigid conduit with required seals and CEC compliance notes. |
| VEEP-REQ-010 | Vendor panel schedules show no mixed receptacle/lighting circuits. |
| VEEP-REQ-011, REQ-012, REQ-013 | Vendor interface drawings declare termination points, grounding lugs, and photometric/control interface; reviewed in `DEL-106-06`. |
| VEEP-REQ-014 | Vendor document register lists design basis and datasheet set; delivered via `DEL-106-05`; accepted via `DEL-106-06`. |
| VEEP-REQ-015 | Vendor calculations and datasheet set include photometric, pole, and foundation design values; EPC review and acceptance gate (`DEL-106-06`) confirms readiness. |

## Documentation

The vendor shall produce, at minimum, the artifacts named in `_CONTEXT.md`:

- Vendor engineered physical equipment package (the equipment itself, with its identification and bill of materials).
- Vendor package design basis and datasheet set, including:
  - Photometric design basis and calculations (lux levels, uniformity, layout) — values TBD until vendor design.
  - Fixture datasheets and area-classification certifications.
  - Pole / mast-pole datasheets with mounting and foundation interface data.
  - Vendor wiring and termination schedules.
  - Grounding/bonding interface details.
  - Control/photocell schedule.
  - Standards-compliance declarations (CEC; light-pollution controls; building code where applicable).

Document handoff and acceptance are governed by `DEL-106-05` (Vendor Document Turnover Package) and `DEL-106-06` (EPC Vendor Package Review and Acceptance).
