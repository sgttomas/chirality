# Specification — DEL-098-04 Vendor Engineered Equipment Package

> Normative requirements on the Package Vendor's engineered equipment package for PKG-098 "Tanks, Sour Water (API 650) 3-25", anchored by the EPC Scope of Work and Package Datasheet.

## Scope

This Specification governs the Package Vendor production unit comprising engineering, design, fabrication/supply, and the physical equipment package developed from the EPC package Scope of Work and Package Datasheet (`_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-098-04).

**In scope** (per SOW-0221, SOW-0222, SOW-0223):
- Engineering and design of seven (7) 3,800 bbl produced-water tanks: three sour produced-water tanks (TK-9030-2/9040-2/9050-2), two sour inlet produced-water tanks (TK-9010-2/9020-2), and two produced-water tanks (TK-9010-1/9020-1).
- Fabrication / supply of the tanks and associated vendor-supplied package components (Kennilworth HCL float skim system one per tank; internal coating; external insulation; external electric heating).
- Vendor package design basis and datasheet set (per anticipated artifacts).

**Out of scope — By Others** (per SOW-0224):
- Foundations.
- Mounting tanks at site.
- Electrical and instrumentation.
- Platforms, staircase, and similar field-installed access steel.

## Requirements

### R-1. Code of Construction
The tanks SHALL be designed and fabricated to **Modified API 650**. (Source: SOW-0223.)

### R-2. Internal Coating
The tank floor, walls, and roof SHALL be internally coated with **Devchem 253**. (Source: SOW-0223; corroborated by 3-25 DBM "Produced-Water Storage, Treatment, and Transfer".)

### R-3. External Insulation and Heating
The tanks SHALL be externally insulated and equipped with **external electric heating**. (Source: SOW-0223; DBM confirms.) Heat-tracing and winterization design SHALL satisfy the -40 °C minimum ambient site basis (3-25 DBM "Site Conditions"); detailed parameters are ASSUMPTION pending vendor design.

### R-4. Skim System
Each tank SHALL include one **Kennilworth-type HCL float skim system**. (Source: SOW-0223.)

### R-5. Operating Conditions
Tank design SHALL accommodate the operating conditions stated in SOW-0224:
- Pressure: Atmospheric.
- Temperature: 10 °C for Items 1 and 3; **TBD for Item 2** (source-declared TBD).

### R-6. Design Conditions
The tanks SHALL be designed to:
- **32 oz test pressure** (SOW-0224).
- Minimum temperature **-40 °C** and maximum **60 °C** (SOW-0224).

### R-7. Capacity
Each tank SHALL provide nominal **3,800 bbl** storage volume (SOW-0222, SOW-0223). Capacity / design throughput per the source's **Appendix A** SHALL be honored (**location TBD** — Appendix A text not in locally accessible source slices).

### R-8. Tag Identity
The vendor package SHALL deliver tanks bearing the tags listed in the Datasheet (TK-9030-2, TK-9040-2, TK-9050-2, TK-9010-2, TK-9020-2, TK-9010-1, TK-9020-1). (Source: SOW-0223.)

### R-9. Fluid Service Basis
The vendor design SHALL use the produced-water service basis carried in the 3-25 DBM:
- Pump-fluid SG basis 1.18.
- Tank design SG 1.25 (**TBC** per source).
- The SG discrepancy (1.18 vs 1.25) SHALL be closed during detailed design between EPC Integrator and Package Vendor (3-25 DBM). See Conflict C-2 in `Guidance.md`.

### R-10. Sour Service (ASSUMPTION)
Because the package is named "sour" service and Items 1 and 2 are explicitly sour, the vendor SHALL apply applicable sour-service material, corrosion allowance, NDE, and PWHT requirements consistent with Modified API 650 and applicable referenced standards (e.g., NACE MR0175 / ISO 15156). **ASSUMPTION**: specific clause set not enumerated in locally accessible source slices — location TBD.

### R-11. Driver
Vendor SHALL specify any drivers required by package components per detailed design; the source indicates **Driver: TBD** (SOW-0224).

### R-12. Interface Boundary
The vendor's mechanical boundary SHALL terminate at flanges defined by the EPC Integrator Package Datasheet (DEL-098-02). Items "By Others" (foundations; mounting; E/I; platforms/staircase per SOW-0224) SHALL NOT be supplied or executed by the vendor.

### R-13. Documentation Deliverable
The vendor SHALL produce the vendor package **design basis** and a **datasheet set** for each tagged tank (anticipated artifacts in `_CONTEXT.md`); turnover documentation is governed separately by DEL-098-05.

## Standards

| Standard | Application | Locally Accessible? |
|---|---|---|
| API 650 (Modified) | Tank design and fabrication (R-1) | Referenced; full clause text not in `_Sources/` — location TBD |
| 26020 Package Requirements (Vendor / EPC source document) | Package scope basis | Source `.docx` not directly readable; key slices captured in SCOPE_LEDGER |
| 3-25 Liquids Hub Design Basis Memorandum (DBM) | Service basis, site ambient, fluid SG | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| NACE MR0175 / ISO 15156 | Sour-service materials (ASSUMPTION; R-10) | Not in `_Sources/` — location TBD |

## Verification

| Req | Verification Approach |
|---|---|
| R-1 | Design review of vendor calculations and drawings against API 650 (Modified); EPC Integrator review per DEL-098-06. |
| R-2 | Coating procedure qualification, surface prep records, DFT/holiday test reports per Devchem 253 product data (TBD — vendor to confirm). |
| R-3 | Insulation and heat-trace design package; thermal performance check against -40 °C ambient basis. |
| R-4 | Vendor data sheets and shop test of Kennilworth HCL float skim system per tank. |
| R-5, R-6 | Stamped design calculations; hydrostatic / pneumatic test per API 650 (Modified) acceptance. |
| R-7 | Tank dimensional certification; verify nominal 3,800 bbl per tank. Appendix A throughput confirmation when source text obtained (location TBD). |
| R-8 | Nameplate inspection / tag verification against vendor BOM and Package Datasheet. |
| R-9 | Detailed-design closure record for SG basis discrepancy (1.18 vs 1.25). |
| R-10 | Sour-service materials certifications, NDE, PWHT records (ASSUMPTION pending EPC clarification). |
| R-11 | Vendor driver selection record. |
| R-12 | Interface check against Package Datasheet (DEL-098-02) and Construction Work Package (DEL-098-03). |
| R-13 | Vendor design basis and datasheet set audited by EPC Integrator (DEL-098-06). |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):
- Vendor engineered physical equipment package (the supplied tanks and integral package components).
- Vendor package design basis.
- Vendor datasheet set (one per tagged tank, minimum).

Turnover-class documentation (vendor document register, submittals, source-required vendor documents, turnover records) is the scope of **DEL-098-05** and is NOT duplicated here.
