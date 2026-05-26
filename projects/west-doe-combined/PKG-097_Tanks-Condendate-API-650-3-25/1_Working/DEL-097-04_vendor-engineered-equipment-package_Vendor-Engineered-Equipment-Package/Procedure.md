# Procedure — Vendor Engineered Equipment Package (PKG-097 Tanks, Condensate, API 650)

This procedure describes the steps to **produce** the Vendor Engineered Equipment Package as a production-unit deliverable. Operation of the installed tanks is downstream and out of scope.

## Purpose

To direct the Package Vendor through engineering, design, fabrication/supply, and handoff of the PKG-097 condensate tank package, anchored by EPC Scope of Work (DEL-097-01) and EPC Package Datasheet (DEL-097-02), and consistent with the 03-25 Liquids Hub DBM basis.

## Prerequisites

- DEL-097-01 EPC Scope of Work issued.
- DEL-097-02 EPC Package Datasheet issued (including final tank register, design SG, design temperature/pressure, blanket basis, coating spec, insulation/heating, structural loads).
- Accepted upstream snapshot: GATE-07_Final_Published_2026-05-24 (PROJECT_DECOMP).
- Locally accessible reference materials:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-06 Liquids Hub: Condensate Storage and Product Handling; Produced-Water Storage; Vapour Recovery).
  - `_Sources/26020-Package_Requirements.docx` heading 49 (**inaccessible as text in current run — required for clause-level requirements; location TBD**).
- Declared upstream/downstream dependencies: none declared (per `_DEPENDENCIES.md`); coordination via PKG-097 sibling deliverables (DEL-097-01, -02, -03, -05, -06).

## Steps

1. **Confirm anchor inputs.** Vendor confirms receipt of DEL-097-01 and DEL-097-02 (and any update to the final tank register). Flag any anchor gap to EPC Integrator before proceeding.
2. **Establish vendor package design basis.** Compile the vendor design basis from the EPC Package Datasheet: tank count, allocation, capacity, code (API 650 / API-650 Modified — per C-01), design SG, design T/P, blanket gas, coating, insulation, heating, structural loads, sour-service requirements.
3. **Engineer the tank package.** Produce vendor mechanical/structural/instrumentation engineering: shell/bottom/roof design per API 650 (clause set per heading 49 — TBD), foundations interface, nozzles and manways, vapour and blanket connections (per VRU/blanket interface), heating and insulation, internal coating per spec.
4. **Produce vendor datasheet set.** One vendor datasheet per tank class (sour inlet, sour, product, slop) covering Identification, Attributes, Conditions, Construction — cross-checked against DEL-097-02.
5. **Verify interfaces.** Cross-check interfaces vs. EPC Package Datasheet interface matrix: VRU header (LP), blanket gas (LP fuel gas), booster pump suction (P-9211-2 / P-9221-2), slop routing to TK-9130-2, loading pump suction.
6. **Compliance matrix.** Produce code/standard compliance matrix vs. API 650 and any additional standards declared by DEL-097-02 (NACE / ISO 15156 if specified, jurisdictional codes — TBD).
7. **Fabricate and supply.** Procure materials, fabricate (shop and/or field as applicable), inspect per code and project ITP, apply coatings, deliver to site.
8. **Hand off to EPC Integrator.** Submit vendor engineering, design basis, and vendor datasheet set into DEL-097-05 (Vendor Document Turnover) and into DEL-097-06 (EPC Vendor Package Review and Acceptance). This deliverable's content is then "frozen" against the issued vendor revision.

## Verification

| Step | Check | Evidence |
|---|---|---|
| 1 | Anchor inputs present | Vendor receipt log; EPC anchor revision IDs cited in vendor design basis. |
| 2 | Vendor design basis traces every parameter to DEL-097-02 (or to a recorded TBD/Conflict ruling) | Vendor design basis document. |
| 3 | API 650 clauses cited per item | Vendor calculations and drawings. |
| 4 | Vendor datasheets aligned with DEL-097-02 per tank class | Datasheet cross-reference matrix. |
| 5 | Interface matrix matches DEL-097-02 | Vendor interface drawing/list with EPC sign-off. |
| 6 | Compliance matrix complete vs. listed standards | Compliance matrix table. |
| 7 | ITP signed off; coatings/welds/NDE records complete | ITP records, MTRs, NDE reports. |
| 8 | DEL-097-05 and DEL-097-06 submittals accepted by EPC Integrator | EPC acceptance log entry. |

## Records

- Vendor package design basis document.
- Vendor datasheet set (per tank class).
- Vendor engineering drawings, calculations, and code compliance matrix.
- ITP and inspection records (MTRs, weld logs, NDE reports, coating records, hydro/pressure test records as applicable).
- Vendor compliance matrix vs. API 650 (and other applicable standards).
- Cross-references into DEL-097-05 (turnover register) and DEL-097-06 (acceptance log).
- Any deviation requests and their EPC dispositions (linked to Guidance Conflict Table entries C-01..C-05 where relevant).
