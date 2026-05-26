# Specification — DEL-067-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope
This deliverable specifies the EPC Integrator's review-and-acceptance work product for the Tanks, Sour Water (API 650) 4-25 package (`PKG-067`, `26020-01-PT-19-005`; expected vessel tags `TK-9010-1`, `TK-9020-1`). It defines the evidence the EPC Integrator must produce to demonstrate that the Package Vendor's `DEL-067-04` Vendor Engineered Equipment Package and `DEL-067-05` Vendor Document Turnover Package satisfy the EPC Scope of Work (`DEL-067-01`), Package Datasheet (`DEL-067-02`), and Construction Work Package (`DEL-067-03`).

Sources: `PACKAGE_REGISTER.csv` row `PKG-067`; `ARTIFACT_REGISTER.csv` `ART-5AF4728A78`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Produced Water (lines 502-524).

### Out of scope
- Authoring or modifying the vendor-side engineering deliverables themselves; those are `DEL-067-04` / `DEL-067-05` outputs.
- Acceptance of other tank packages (e.g., PKG-093 Sweet Produced Water, PKG-096 Sour Inlet Condensate, PKG-097 Condensate Product, PKG-098 multi-service produced-water tanks, PKG-094/PKG-065 caustic, PKG-063 DSO, PKG-095 slop) — separate deliverables.
- Design or installation of the downstream produced-water pipeline to the 03-25 Liquids Hub ("designed and installed by others" per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 506).

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| `R-067-06-01` | The acceptance evidence MUST cover all SOW items mapped to this deliverable: `SOW-0225`, `SOW-0226`, `SOW-0227`, `SOW-0228`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-067-06` |
| `R-067-06-02` | The vendor document review log MUST enumerate every vendor engineering deliverable listed by the Package Vendor for `26020-01-PT-19-005` and record disposition (accepted / rejected / open) against `DEL-067-02` Package Datasheet values. | `_CONTEXT.md`; standard vendor-document review pattern (decomposition `DELIVERABLE_REGISTER.csv` row `DEL-067-05`) |
| `R-067-06-03` | The package acceptance checklist MUST verify scope inclusions: two API 650 modified atmospheric produced-water / sour-water storage tanks; expected vessel tags `TK-9010-1`, `TK-9020-1`; internal Devchem 253 coating on floor, walls, and roof; external insulation and electric heating where required; Kennilworth-type hydrocarbon skim float system; PVRV (each tank, at least one); EPRV; LP fuel gas blanket connection; VRU suction/header connection as applicable; tank instrumentation and standard appurtenances. | `ARTIFACT_REGISTER.csv` `ART-5AF4728A78`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 (tank construction/appurtenances); line 518 (design code / test pressure) |
| `R-067-06-04` | The acceptance evidence MUST verify tank design code and test pressure: "Modified API-650 atmospheric tank; 16 oz test pressure" for produced-water tanks at 04-25. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 518 |
| `R-067-06-05` | The acceptance evidence MUST verify storage-basis sizing intent: 2 × 2,000 bbl tanks supporting 380 bbl/d production basis and ~8.9 days storage, with outlet to the produced-water pipeline to 03-25 Liquids Hub and a truck-out provision for emergency / local handling. Final tank capacity MUST reconcile to `DEL-067-02` Package Datasheet. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 493 |
| `R-067-06-06` | The acceptance evidence MUST verify fluid-characterization assumptions used in vendor design: produced water may contain trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, and mercaptans (composition to be confirmed); tank design SG 1.25 (TBC); transfer-pump design SG 1.18; density 1008 kg/m3 at 26.7 °C. Vendor-submitted values MUST be reconciled with `DEL-067-02`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 508 |
| `R-067-06-07` | The acceptance evidence MUST verify PVRV and EPRV scope: at least one PVRV per tank, with EPRV sizing reviewed during detailed engineering and carried into the acceptance record. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 |
| `R-067-06-08` | The acceptance evidence MUST verify tank isolation philosophy review in the context of potential sour vapours, including blanket-gas / VRU header arrangement. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 |
| `R-067-06-09` | The acceptance evidence MUST verify internal-coating application records (Devchem 253, floor / walls / roof) and external insulation + electric heating records. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 |
| `R-067-06-10` | The acceptance evidence MUST cover each physical interface marked `YES` for `PKG-067` in `INTERFACE_REGISTER.csv`: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-067 rows |
| `R-067-06-11` | Plant-spacing acceptance MUST confirm: minimum 2.35 m between atmospheric tanks (NFPA 30 22.4.2.1); minimum 25 m between flare and atmospheric produced-water tanks (OGAOM 9.6.15); minimum 25 m between fired heaters and atmospheric tanks (OGAOM 9.6.15); minimum 10 m between flare KO drums / tanks and vegetation or other fire hazards (OGAOM 9.6.15). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 261-297 |
| `R-067-06-12` | The acceptance evidence MUST include pressure / leak-test packages; nameplate records; provincial pressure equipment registration package where applicable; Manufacturing Record Book / Vendor Data Book; SPIR; and IOM. Specific provincial regime is location TBD; ASSUMPTION: ABSA (Alberta) or BC equivalent depending on final regulatory jurisdiction. | ASSUMPTION based on standard pressure-equipment acceptance practice; provincial location not stated in accessible sources. |
| `R-067-06-13` | Numeric design/operating values used in acceptance (final tank dimensions, EPRV sizing, heater sizing, final fluid composition, final tank design SG) MUST be traceable to the Package Vendor's accepted submittals; specific numeric values are TBD until those submittals are accepted. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 508, 524, 564-565 |
| `R-067-06-14` | All open items from accessible source materials ("Produced water transfer pumps suction from produced water storage"; "Produced water treating: No current provision; filtration requirement to be confirmed"; design SG TBC; EPRV review pending; tank isolation philosophy review pending) MUST be closed or carried with explicit disposition in the acceptance record. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 521-524, 564-565 |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| API STD 650 (modified) | Governing tank design and fabrication code per DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 518; package name "Tanks, Sour Water (API 650) 4-25" |
| API STD 2000 | Likely governing for tank venting / blanket gas system. | location TBD — not explicitly cited for PKG-067 in accessible sources; ASSUMPTION by analogy to PKG-097 (`ART-800458BCA8`: "blanket gas system per API 2000") and PKG-093 (`ART-7A680151FF`). |
| NFPA 30 | Governs atmospheric-tank spacing rules used at 04-25. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 268-269 (Table 22.4.2.1, 22.4.1.5) |
| OGAOM (BC Oil and Gas Activities Operations Manual), Sec. 9.6.15 | Governs flare-to-tank, fired-heater-to-tank, and tank-to-road spacing at 04-25. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 270, 282-287, 297 |
| NACE / MR-0175 (sour-service materials) | Likely applicable for sour-water service materials selection. | location TBD — not explicitly cited for PKG-067 in accessible sources; ASSUMPTION based on the package's sour-service designation and the analogous citation for PKG-096 sour inlet condensate tanks (`ART-BE664573F5`: "Sour service (H2S present), NACE compliant"). |
| Provincial pressure equipment registration regime (typically ABSA in Alberta or equivalent in BC) | Required where modified-API-650 tanks fall under provincial pressure-equipment registration. | location TBD — not stated in accessible sources; ASSUMPTION. |

## Verification

| Req ID | Verification Approach |
|---|---|
| `R-067-06-01` | Traceability matrix mapping each SOW item (`SOW-0225..0228`) to acceptance-checklist rows and evidence artifacts. |
| `R-067-06-02` | Document-by-document review log inspection; every vendor deliverable submitted has a tracked disposition; cross-walk against `DEL-067-02`. |
| `R-067-06-03` | Walk-down and as-built/IFC drawing review against the Major Included Equipment list (`ART-5AF4728A78`) and the DBM appurtenance basis (line 524). |
| `R-067-06-04` | Vendor Material Test Reports, vendor data report, and hydrotest / leak-test packages reviewed against API 650 (modified) and 16 oz test-pressure basis. |
| `R-067-06-05` | Capacity reconciliation between `DEL-067-02` Package Datasheet, vendor data sheet, and the DBM storage-basis row (line 493). |
| `R-067-06-06` | Reconciliation table between fluid-characterization assumptions in `DEL-067-02` and vendor-submitted process inputs; TBD entries flagged. |
| `R-067-06-07` | Review of PVRV / EPRV sizing calculations and tank-protection P&ID; per-tank PVRV count check; EPRV sizing report acceptance. |
| `R-067-06-08` | Review of tank isolation / blanket-gas / VRU header arrangement against the DBM sour-vapour concern; commissioning isolation valve / interlock review. |
| `R-067-06-09` | Coating QA records (Devchem 253 application, DFT, holiday testing); insulation acceptance; heat-trace energization and commissioning records. |
| `R-067-06-10` | Interface-by-interface checklist against `INTERFACE_REGISTER.csv` PKG-067 rows; field walk-down and ITR closure. |
| `R-067-06-11` | Plot-plan and as-built dimensional check against NFPA 30 / OGAOM 9.6.15 spacing values. |
| `R-067-06-12` | Pressure-equipment registration acceptance; MRB / Vendor Data Book compiled; SPIR accepted; IOM in turnover bundle. |
| `R-067-06-13` | Reconciliation of vendor-submitted numeric values to `DEL-067-02`; outstanding TBDs explicitly listed in acceptance record. |
| `R-067-06-14` | Open-items log carried into commissioning; explicit closure or carryover noted with responsible-party assignment. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log (per-document disposition).
- Package acceptance checklist (SOW-, interface-, and artifact-indexed).
- Test / inspection evidence bundle (MTRs, ITP execution, IRC, hydrotest, coating QA, heat-trace energization, instrumentation FAT).
- Turnover evidence bundle (MRB / VDB, pressure-test packages, registration package where applicable, SPIR, IOM).
- Open-items disposition log (including produced-water transfer pumps suction arrangement, filtration requirement TBC, design SG TBC, EPRV sizing review, tank isolation philosophy review).

Standards-related and numeric design values that depend on vendor submittals carry `TBD` placeholders until the Package Vendor deliverables are accepted.
