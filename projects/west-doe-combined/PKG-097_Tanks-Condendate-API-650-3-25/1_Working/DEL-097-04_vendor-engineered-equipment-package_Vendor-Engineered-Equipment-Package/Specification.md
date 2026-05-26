# Specification — Vendor Engineered Equipment Package (PKG-097 Tanks, Condensate, API 650)

## Scope

This specification governs the Package Vendor's production unit for `PKG-097 Tanks, Condensate (API 650) 3-25`. It covers vendor engineering, design, fabrication/supply, and delivery of the physical equipment package for the 03-25 Liquids Hub condensate storage tankage, developed from and bounded by:

- DEL-097-01 EPC Scope of Work (anchor)
- DEL-097-02 EPC Package Datasheet (anchor)

Includes:

- Vendor engineering and design of the condensate storage tanks (sour inlet, sour, product, slop allocations as defined by the EPC Package Datasheet).
- Fabrication / supply of the physical equipment package.
- Vendor package design basis and vendor datasheet set as production-unit outputs.

Excludes:

- EPC anchor deliverables (DEL-097-01, DEL-097-02, DEL-097-03).
- Vendor document turnover register and submittals (covered by DEL-097-05).
- EPC integration review acceptance evidence (covered by DEL-097-06).
- Downstream installation, tie-in, and turnover (covered by DEL-097-03 Construction Work Package).

Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv (GATE-07).

## Requirements

| Req ID | Requirement | Basis | Verification |
|---|---|---|---|
| R-01 | Vendor shall engineer and supply the condensate tank package consistent with the EPC Scope of Work (DEL-097-01) and EPC Package Datasheet (DEL-097-02). | DELIVERABLE_REGISTER.csv (DEL-097-04 description) | EPC integration review (DEL-097-06) confirms alignment with anchor inputs. |
| R-02 | Tank count and functional allocation shall conform to the accepted DBM basis: 11 x 3,800 bbl condensate tanks allocated as 2 sour inlet / 4 sour / 4 product / 1 slop, unless superseded by the final tank register issued via EPC Package Datasheet. | DBM §"Condensate Storage and Product Handling" line 406 | Vendor datasheet set check vs. EPC Package Datasheet (DEL-097-02). |
| R-03 | Tank construction shall comply with API 650 (per package title). Specific clause set, edition, and addenda — **ASSUMPTION**; final clause set governed by 26020-Package_Requirements.docx heading 49 (location TBD). | `_CONTEXT.md` package title; `_REFERENCES.md` | Vendor design basis review; vendor compliance matrix vs. API 650. |
| R-04 | Sour-service tanks shall be designed for sour condensate duty (sour inlet and sour service classes). | DBM §"Condensate Storage and Product Handling" line 406 | Material/coating review vs. sour-service requirements. |
| R-05 | Tank vapour interfaces shall be compatible with the LP VRU collection header serving condensate and produced-water tanks (2 x 100% VRU, SCA-002 routes VRU discharge to 04-25 SOC suction). | DBM §"Vapour Recovery" line 423 ff. | Interface check against EPC Package Datasheet vapour interface matrix. |
| R-06 | Tank blanket-gas interface and set pressures — **TBD**, to be defined by EPC Package Datasheet. | location TBD | Vendor datasheet vs. EPC Package Datasheet. |
| R-07 | Internal coating / lining — **TBD** for condensate service; produced-water tanks at site use Devchem 253 internal coating (**ASSUMPTION** for condensate, not authoritative). | DBM §"Produced-Water Storage…"; location TBD | Coating specification review. |
| R-08 | External insulation and heating — **TBD** for condensate; produced-water tanks are externally insulated and heated. | DBM §"Produced-Water Storage…" | Cold-climate operability review. |
| R-09 | Design temperature, design pressure, and design specific gravity — **TBD**, governed by EPC Package Datasheet. | location TBD | Vendor design basis review. |
| R-10 | Seismic, wind, and snow loads — site-specific values **TBD**, governed by EPC Package Datasheet and applicable jurisdictional codes. | location TBD | Structural calculations review. |
| R-11 | Vendor shall produce a vendor package design basis and vendor datasheet set as part of the production-unit outputs. | `_CONTEXT.md` Anticipated Artifacts | Artifact presence check at acceptance (DEL-097-06). |
| R-12 | Integration with adjacent systems (condensate booster pumps P-9211-2 / P-9221-2, loading pumps, VRU header, slop TK-9130-2) shall conform to the interfaces declared in DEL-097-02 EPC Package Datasheet. | DBM §"Condensate Storage and Product Handling"; DBM §"Vapour Recovery" | Interface matrix check. |

## Standards

| Standard | Applicability | Notes |
|---|---|---|
| API 650 | Construction code for the condensate tanks | Per package title `Tanks, Condensate (API 650) 3-25`. Specific edition/clauses **TBD** (location: 26020-Package_Requirements.docx heading 49). |
| API 650 Modified | Used at site for related produced-water tanks; applicability to condensate tanks — **ASSUMPTION** | DBM §"Produced-Water Storage…"; condensate-side scope to be confirmed by EPC Package Datasheet. |
| Sour service codes (e.g., NACE MR0175 / ISO 15156) | Likely applicable to sour-service tanks — **ASSUMPTION** | location TBD; not stated explicitly in available DBM slice. |
| Jurisdictional / provincial pressure & storage regulations | Applicable to facility location (03-25 site) | location TBD. |

## Verification

| Verification activity | Maps to requirements |
|---|---|
| Vendor design basis review (EPC Integrator) | R-01, R-03, R-06–R-10 |
| Vendor datasheet set check vs. EPC Package Datasheet | R-02, R-04, R-06, R-09, R-12 |
| Coating / material compliance review | R-04, R-07 |
| Interface matrix check (vapour, blanket, pumps, slop) | R-05, R-12 |
| Code compliance matrix (API 650 et al.) | R-03 |
| Structural calculations review | R-10 |
| Acceptance evidence under DEL-097-06 | All |

## Documentation

Required deliverable artifacts (per `_CONTEXT.md` Anticipated Artifacts and DELIVERABLE_REGISTER.csv DEL-097-04 row):

- Vendor engineered physical equipment package (the equipment itself, with nameplates and as-built marks).
- Vendor package design basis (engineering basis adopted from EPC Package Datasheet).
- Vendor datasheet set (per-tank datasheets covering identification, attributes, conditions, construction).

Vendor document submittals (drawings, calculations, certifications, weld/coating records) are routed through DEL-097-05 Vendor Document Turnover Package, not duplicated here.
