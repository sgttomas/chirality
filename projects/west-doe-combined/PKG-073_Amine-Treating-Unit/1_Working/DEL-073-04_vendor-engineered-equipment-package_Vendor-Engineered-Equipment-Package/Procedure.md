# Procedure — Vendor Engineered Equipment Package (DEL-073-04)

> Operational procedure for **producing** the vendor-engineered amine treating unit package as a deliverable (vendor-side engineering and supply path) with EPC Integrator review. Steps for **operating** the package are deferred to vendor O&M manuals at turnover.
>
> Source-grounded against DBM-Deepcut SEC-06 / SEC-02 and the deliverable's `_CONTEXT.md` / `_DEPENDENCIES.md`. Operational details not in the DBM are marked `TBD`.

## Purpose

Produce, fabricate, and deliver the PKG-073 vendor-engineered Amine Treating Unit package such that the EPC Integrator can accept it for installation, tie-in, and commissioning at the 04-25 facility.

## Prerequisites

| Prerequisite | Source |
|---|---|
| Accepted EPC Scope of Work (DEL-073-01) | DELIVERABLE_REGISTER row 258 |
| Accepted EPC Package Datasheet (DEL-073-02) | DELIVERABLE_REGISTER row 259 |
| Accepted Design Basis Memorandum SEC-06 (Amine Treating Basis) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Site design ambient envelope confirmed: −40 °C to +35 °C | DBM SEC-02 L198 |
| Authoritative reference: `26020-Package_Requirements.docx` h.27 | `_REFERENCES.md` (location TBD — not locally parseable) |
| Declared upstream dependencies in `_DEPENDENCIES.md` | None declared at PREPARATION; vendor should request explicit upstream-dependency declaration before detailed design starts. |

## Steps

### Step 1 — Vendor onboarding and brief
1.1 Receive and acknowledge EPC SOW (DEL-073-01) and EPC Package Datasheet (DEL-073-02).
1.2 Confirm scope split per Specification §Scope; raise Conflict C-002 if Module 520 boundary requires resolution.
1.3 Confirm process performance targets per Specification R-1.

### Step 2 — Process design
2.1 Build vendor process simulation across the design envelope (R-1.4–R-1.7).
2.2 Demonstrate Sweet-gas H2S ≤4 ppmv (R-1.1) with MDEA solvent (R-1.2) and ≤2 mol% sales-gas CO2 (R-1.2 driver). Reference: DBM SEC-06 L1156, L1158.
2.3 Produce heat-and-material balance and acid-gas composition for downstream acid-gas compressor coordination (DBM SEC-06 L1143, L1371).
2.4 Document open items C-003 (low operating pressure) and C-004 (heat-medium terminology) and resolve with EPC.

### Step 3 — Mechanical equipment design
3.1 Issue equipment datasheets for each equipment item in Specification R-2.
3.2 Confirm pump selection model (R-2.9 — charge pumps, currently API-610 axial-split TBC).
3.3 Confirm material selection at low H2S/CO2 ratios (DBM L1183/L1388).
3.4 Document anti-foam pump flow rate (R-2/L1169 — currently TBD).

### Step 4 — Module engineering
4.1 Develop Module 530 (regeneration module/building) general arrangement per DBM SEC-06 L1132.
4.2 Coordinate Module 520 amine portion (inlet coalescers, absorbers) GA with the EPC Integrator (Module 520 interface with TEG dehydration).
4.3 Apply minimum spacing criteria (DBM SEC-02 §2.5).
4.4 Apply cold-climate provisions (winterization, heat tracing, insulation, package building heat) per DBM SEC-02 L198 and L145 analog (SEC-02 General Layout Basis).

### Step 5 — Fabrication and shop assembly
5.1 Fabricate pressure equipment to ASME B&PV Section VIII (ASSUMPTION — confirm against `26020-Package_Requirements.docx` h.27).
5.2 Register pressure equipment for BC CRN (ASSUMPTION — confirm against EPC site standards).
5.3 Perform shop hydrotest and NDE per ITP.
5.4 Conduct shop FAT for controls, instrumentation, and pumps.

### Step 6 — Documentation and turnover preparation
6.1 Assemble vendor document set per Specification §Documentation.
6.2 Coordinate with DEL-073-05 (Vendor Document Turnover Package) for register and submittal flow.
6.3 Prepare cause-and-effect for amine controls per DBM SEC-06 L1359.

### Step 7 — Shipping
7.1 Ship Module 530 as a shop-assembled module/building per DBM SEC-06 L1132 (basis: shop assembly, field erection).
7.2 Ship Module 520 amine equipment per EPC modularization plan.

### Step 8 — EPC integration review and acceptance handoff
8.1 Support EPC Integrator review under DEL-073-06.
8.2 Provide commissioning support and performance test execution at site.

## Verification

| Step | Verification |
|---|---|
| Step 2 | EPC review of process simulation and HMB against DBM SEC-06 envelope. |
| Step 3 | EPC review of equipment datasheets against Specification R-2. |
| Step 4 | EPC review of module GAs and spacing. |
| Step 5 | Witness/hold points per ITP; FAT acceptance. |
| Step 6 | DEL-073-05 vendor document register completion. |
| Step 8 | DEL-073-06 acceptance evidence (review log, acceptance checklist, test/inspection evidence, turnover evidence — DELIVERABLE_REGISTER row 263). |

## Records

- Vendor process simulation files and HMB issued for review
- Equipment datasheet revisions (issued for review, issued for fabrication, as-built)
- Hydrotest reports and NDE records
- FAT reports
- Vendor document register (linked to DEL-073-05)
- Cause-and-effect issued and approved
- Performance test record (site)
- EPC acceptance evidence (linked to DEL-073-06)
