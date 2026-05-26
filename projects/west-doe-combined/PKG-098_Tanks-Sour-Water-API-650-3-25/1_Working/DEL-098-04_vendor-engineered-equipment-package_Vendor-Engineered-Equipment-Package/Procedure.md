# Procedure — DEL-098-04 Vendor Engineered Equipment Package

> Operational steps to produce the Vendor Engineered Equipment Package. Steps marked TBD require vendor judgment or EPC clarification.

## Purpose

To produce the Package Vendor's engineering, design, fabrication/supply, and physical equipment package for PKG-098 (seven 3,800 bbl produced-water tanks, Modified API 650, coated/insulated/heated, with skim systems) in a manner that satisfies `Specification.md`, honors `Guidance.md`, and provides verifiable records to support EPC review and acceptance (DEL-098-06).

## Prerequisites

1. **Inputs from EPC Integrator** (declared upstream — formal declarations are TBD per `_DEPENDENCIES.md`; logical dependencies inferred from `_CONTEXT.md` and DELIVERABLE_REGISTER):
   - DEL-098-01 Scope of Work — accepted (state ≥ INITIALIZED ASSUMPTION).
   - DEL-098-02 Package Datasheet — accepted; provides interface boundary, tag list, design conditions, and Modified-API-650 deviations.
   - DEL-098-03 Construction Work Package — available for interface alignment.
2. **Sources** (locally accessible):
   - `_Decomposition/.../GATE-07.../SCOPE_LEDGER.csv` rows SOW-0221, SOW-0222, SOW-0223, SOW-0224.
   - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
3. **Source clarifications** resolved or carried as TBD per Conflict Table (C-1 … C-5) in `Guidance.md`.
4. **Vendor capability**: tank fabrication shop qualified for Modified API 650, sour-service material handling (ASSUMPTION), and Devchem 253 coating application.
5. **Tagged equipment list confirmed** with EPC Integrator: TK-9030-2, TK-9040-2, TK-9050-2, TK-9010-2, TK-9020-2, TK-9010-1, TK-9020-1.

## Steps

### Step 1 — Receive and confirm EPC handoff
1.1. Receive the Package Datasheet (DEL-098-02) and SOW (DEL-098-01).
1.2. Log document numbers, revisions, and date of receipt.
1.3. Confirm the seven tagged tanks listed in the Package Datasheet match the Datasheet of this deliverable.

### Step 2 — Compile design basis
2.1. Consolidate operating and design conditions per `Specification.md` R-5, R-6.
2.2. Adopt produced-water fluid basis (SG, temperature) per R-9 and `Guidance.md` Conflict C-2 closure.
2.3. Apply -40 °C site ambient envelope from 3-25 DBM.
2.4. Document any vendor-standard assumptions explicitly and submit to EPC for ratification.

### Step 3 — Resolve TBD / Conflict Table items
3.1. Issue technical clarification requests (TQs) to EPC for C-1 (Item 3 service), C-2 (SG), C-3 (scope tank count), C-4 (standards), C-5 (Item 2 op temp, driver, Appendix A).
3.2. Carry every unresolved item as TBD on vendor design documents; do not proceed past IFD without resolution of items material to design.

### Step 4 — Mechanical and process design of tanks
4.1. Perform Modified API 650 calculations for each tank (shell, bottom, roof, anchorage, seismic/snow per site loads from 3-25 DBM context).
4.2. Apply sour-service materials, NDE, and PWHT per applicable standards (ASSUMPTION; see R-10).
4.3. Specify corrosion allowance per EPC Package Datasheet (location TBD if not provided).
4.4. Design venting per Modified API 650 (atmospheric; 32 oz test pressure) per R-6.
4.5. Design manways, drains, gauging connections, and inspection access TBD per vendor standard plus Package Datasheet.

### Step 5 — Internal coating system design
5.1. Specify Devchem 253 application to floor, walls, and roof per R-2.
5.2. Define surface preparation, DFT control, application environment, and holiday-test acceptance per coating manufacturer data.
5.3. Coordinate cure schedule with fabrication sequence.

### Step 6 — External insulation and electric heating design
6.1. Size insulation and electric heating to maintain process temperature envelope above -40 °C ambient per R-3.
6.2. Coordinate electrical demand and circuit segmentation with EPC Integrator (electrical execution by Others per SOW-0224).
6.3. Define heat-trace power densities, control philosophy, and redundancy (TBD pending EPC electrical interface confirmation).

### Step 7 — Skim system integration
7.1. Procure or detail the Kennilworth-type HCL float skim system, one per tank, per R-4.
7.2. Integrate skim nozzle, support, and access with tank shell design.

### Step 8 — Vendor datasheet set and design basis production
8.1. Produce a vendor datasheet for each tagged tank (TK-9030-2, TK-9040-2, TK-9050-2, TK-9010-2, TK-9020-2, TK-9010-1, TK-9020-1).
8.2. Produce the vendor package design basis covering inputs, assumptions, calculations, and verification.
8.3. Submit for EPC Integrator review (interface with DEL-098-06).

### Step 9 — Fabrication, inspection, and testing
9.1. Material procurement with sour-service certifications (ASSUMPTION; per R-10 closure).
9.2. Welding and NDE per Modified API 650 and any EPC-specified sour-service overlays.
9.3. Hydrostatic / pneumatic testing per API 650 (Modified) acceptance.
9.4. Coating application and DFT/holiday verification.
9.5. Insulation and heat-trace installation, factory verification where applicable; field commissioning is by Others per SOW-0224.
9.6. Fit, function, and shop-test the skim system on each tank.

### Step 10 — Pre-shipment package readiness
10.1. Confirm tag identity, nameplate, and BOM against Package Datasheet (R-8, R-12).
10.2. Confirm "By Others" interface flanges are correctly prepared (capped/blinded) for site mounting by Others.
10.3. Compile shipment records; turnover documentation set is delivered under DEL-098-05.

## Verification

| Step | Verification | Evidence |
|---|---|---|
| 1 | Receipt log signed by Package Vendor and EPC Integrator. | Document control entry. |
| 2 | Design-basis document reviewed by EPC Integrator. | Design basis review record. |
| 3 | All Conflict Table items closed or TBD-listed in design-basis document. | TQ log; design basis appendix. |
| 4 | Stamped mechanical calculations per Modified API 650. | Calc package; engineer's stamp. |
| 5 | Coating procedure qualification; surface-prep, DFT, and holiday test records. | Coating QC records. |
| 6 | Heat-trace and insulation thermal study; electrical demand sheet. | Thermal model output; load list submission to EPC. |
| 7 | Skim system functional test record. | Vendor shop test report. |
| 8 | Vendor datasheets and design basis accepted by EPC. | EPC review log (linked to DEL-098-06). |
| 9 | Material MTRs, weld maps, NDE reports, hydrostatic test report, coating QC report. | Fabrication QC dossier. |
| 10 | Pre-shipment punch list closed. | Pre-shipment inspection report. |

## Records

- Vendor design basis document.
- Vendor datasheet set (one per tagged tank; seven minimum).
- Mechanical calculation package (stamped).
- Coating procedure qualification and QC records (surface prep, DFT, holiday).
- Material test reports, weld maps, NDE reports.
- Hydrostatic / pneumatic test report.
- Heat-trace and insulation design package.
- Skim system shop test reports.
- Technical clarification (TQ) log linking each Conflict Table item to its closure.
- Pre-shipment inspection report and BOM/tag verification.

(Aggregation, submission register, and turnover package of these records is the scope of **DEL-098-05**; this Procedure delivers them as evidence of the vendor production unit.)
