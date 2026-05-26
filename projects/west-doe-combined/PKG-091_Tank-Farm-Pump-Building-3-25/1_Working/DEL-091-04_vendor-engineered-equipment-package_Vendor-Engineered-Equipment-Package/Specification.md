# Specification — Vendor Engineered Equipment Package (DEL-091-04)

EpistemicDefault: requirements anchored to accessible source slices; otherwise `TBD` or `ASSUMPTION`.

## Scope

This specification governs the Package Vendor's engineering, design, fabrication/supply, and physical delivery of the Tank Farm Pump Building 3-25 (PKG-091) equipment package as a Vendor Package Production Unit. It covers the pump-house equipment set (drain, water transfer, sour condensate, condensate sweetening feed pumps), associated mechanical/electrical/I&C internals, and the package boundary interfaces. It excludes facility-level integration, tie-ins, and constructability — those are owned by the EPC Integrator (PACKAGE_REGISTER row 84).

Included scope items: `SOW-0185`, `SOW-0186`, `SOW-0187`, `SOW-0188` (per DEL-091-04 `_CONTEXT.md` and OBJECTIVE_SCOPE_MAP rows 226–229).

Excluded from this deliverable:
- Facility-side integration design (covered by `DEL-091-01_scope-of-work` and `DEL-091-02_package-datasheet`).
- Construction execution and turnover (covered by `DEL-091-03_construction-work-package`).
- EPC vendor review/acceptance (covered by `DEL-091-06_epc-vendor-package-review-and-acceptance`).
- LACT custody-transfer equipment (third-party NRM scope, DBM 3-25 line 417). `FACT` — not in 3-25 facility equipment scope.

## Requirements

R1. The vendor shall supply the major equipment listed in `Datasheet.md` Attributes table at the stated quantities and configurations (PACKAGE_REGISTER row 84).

R2. The vendor shall design the package to perform the process functions stated in PACKAGE_REGISTER row 84: water transfer pumps in parallel pulling from produced-water tanks through a bag filter to the produced-water pipeline; sour-condensate pumps moving sour condensate from sour-condensate storage tanks to condensate sweetening feed pumps. (`FACT`, PACKAGE_REGISTER row 84.)

R3. Produced-water transfer pumps shall be sized as `2 x 100 percent` configuration consistent with the 3-25 Liquids Hub basis. (`FACT`, DBM 3-25 line 429.)

R4. The package shall accommodate the 3-25 produced-water service condition: reference flow 3,600 m3/d at 10 °C, 150 kPag. (`FACT`, DBM 3-25 line 188. ASSUMPTION: this is the relevant sizing reference for water transfer pumps; vendor shall confirm against final tank register and end-user pipeline interface.)

R5. The condensate sweetening feed pumps shall be sized consistent with the 20,000 bbl/d non-regenerative caustic mercaptan treating throughput. (`FACT`, DBM 3-25 line 389. ASSUMPTION on sizing margin pending vendor design basis.)

R6. The package shall present a single, coordinated boundary for each applicable interface type listed in `Datasheet.md` Construction. (`FACT`, PACKAGE_REGISTER row 84.)

R7. The vendor shall produce a vendor package design basis and a datasheet set as the anticipated artifacts of this deliverable. (`FACT`, DELIVERABLE_REGISTER row 471.)

R8. The vendor's design shall not reintroduce process functions that the SCA basis has removed from 3-25 (local stabilization, local SOC, condensate dehydration, local instrument-air compression, local heat-medium). (`FACT`, DBM 3-25 lines 65–68, 366, 442.)

R9. Detailed performance criteria (rated flow, head, NPSHr, efficiency at duty point, motor service factor, seal flush plan, materials of construction, design temperature/pressure, area classification, seismic and wind loads): `TBD` — to be set by the vendor design basis grounded in the EPC Package Datasheet (`DEL-091-02`). Specification does not invent these values.

R10. Materials/coatings/insulation: `TBD` (vendor design basis grounded in EPC Package Datasheet).

R11. Quality plan, ITPs, factory acceptance testing, hydrostatic and performance testing acceptance criteria: `TBD` (vendor design basis; EPC Package Datasheet and EPC Scope of Work).

## Standards

The locally accessible source set does not enumerate clause-level codes for this package. The following are listed as `ASSUMPTION: likely applicable` based on Vendor Package Production Unit type and Mechanical discipline; clause-level applicability `location TBD`:

- API 610 — centrifugal pumps for petroleum, petrochemical, and natural gas industries (ASSUMPTION).
- API 674/675/676 — positive displacement / metering / rotary pumps as applicable (ASSUMPTION).
- ASME B31.3 — Process Piping (ASSUMPTION; vendor interface piping).
- CSA Z662 — Oil and gas pipeline systems (ASSUMPTION; produced-water pipeline tie-in).
- CSA B51 / ABSA registration — Alberta/BC pressure equipment registration (ASSUMPTION; BC site per DBM line 12).
- Canadian Electrical Code (CSA C22.1) and IEC/CSA hazardous-location classification (ASSUMPTION).
- NFPA / Fire & Gas standards as referenced by the EPC Scope of Work (ASSUMPTION).

Authoritative standards list shall be confirmed against the EPC Package Datasheet (`DEL-091-02`) and the source `26020-Package_Requirements.docx` heading 44 once that slice is locally readable.

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Document review of vendor bill of materials against Attributes table; FAT equipment inspection. |
| R2 | Design review of P&IDs and pump schedules against PACKAGE_REGISTER row 84 functions. |
| R3 | Sizing review of pump performance curves against `2 x 100 percent` redundancy claim. |
| R4, R5 | Hydraulic review against DBM 3-25 service conditions; performance test at FAT to API/AHRI applicable acceptance band. |
| R6 | Interface matrix review against EPC Package Datasheet (`DEL-091-02`); interface punch at integration review. |
| R7 | Vendor document register check against turnover package (`DEL-091-05`). |
| R8 | Design review confirming absence of superseded process functions. |
| R9–R11 | Vendor design basis review; FAT/ITP execution; turnover documentation. |

EPC Integrator vendor review and acceptance is performed under `DEL-091-06`.

## Documentation

Anticipated vendor-issued artifacts (DELIVERABLE_REGISTER row 471):

- Vendor engineered physical equipment package (the equipment itself).
- Vendor package design basis.
- Vendor package datasheet set.

Vendor documentation register, submittals, and turnover records are tracked separately under `DEL-091-05_vendor-document-turnover-package`.
