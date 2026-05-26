# Guidance — DEL-085-01 Scope of Work (PKG-085 Flare Stack (High Pressure))

## Purpose

This Guidance document explains why the EPC Integrator Scope of Work for PKG-085 exists and how it should be read alongside the rest of the PKG-085 deliverable set. Per the accepted GATE-07 decomposition, DEL-085-01 is the mandatory Gate 5 EPC anchor deliverable that fixes package identity, function, tagged equipment, source basis, boundaries, and the whole-facility integration narrative for the High-Pressure (HP/Cryo) flare stack. [DELIVERABLE_REGISTER row 312; `_CONTEXT.md`]

The HP flare stack is a shared-interface asset between the 03-25 compressor/liquids hub and the 04-25 deepcut facility, and is treated as a reference/interface package because the physical equipment is vendor-engineered and budgetary-procured outside the 3-25 DBM cost scope. [PACKAGE_REGISTER row 58; SCOPE_LEDGER SOW-0090; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line ~56]

## Principles

1. **Vendor owns the package; EPC owns the integration.** Package engineering, package design, vendor documentation, and the physical equipment package are Package Vendor scope. Facility-level interfaces, tie-ins, constructability, procurement/construction coordination, and integration acceptance are EPC Integrator scope. [PACKAGE_REGISTER row 58 Responsibility Model]
2. **Source over inference.** Where the DBMs and PACKAGE_REGISTER name explicit equipment, geometry, header sizes, or interface types, the SoW must mirror those values verbatim. Where the source is silent, mark `TBD` rather than infer.
3. **Shared-asset framing.** Because the HP flare stack serves both 03-25 and 04-25, scope text must read as cross-facility and must not collapse the dual service into a single owner's scope. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines ~56, 547-548]
4. **Boundary ruling sensitivity.** SOW-0090 records the stack as 4-25 shared, excluded from 3-25 costing scope, and treated as interface/reference unless the boundary ruling changes. The SoW should not pre-empt that ruling. [SCOPE_LEDGER SOW-0090]
5. **Staggered blowdown as a sizing driver.** Staggered blowdown is required to limit maximum relief; relief and blowdown load coordination drives stack sizing and acceptance criteria. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line ~501]
6. **Anchor for vendor handoff.** This SoW is the upstream anchor for DEL-085-02 (Package Datasheet), DEL-085-03 (Construction Work Package), DEL-085-04 (Vendor Engineered Equipment Package), DEL-085-05 (Vendor Document Turnover Package), and DEL-085-06 (EPC Vendor Package Review and Acceptance). Terminology and tag IDs must be stable across these six deliverables. [DELIVERABLE_REGISTER rows 312-317]

## Considerations

- **Tagged equipment of record.** FL-4120-1 is the explicit HP flare stack tag in SCOPE_LEDGER SOW-0089. The package also carries "downstream shared flare-stack interface content," which is the natural place to capture the V-4100-2 / V-4150-2 KO-drum manifold, the 508 mm HP relief header, and HP loads enumerated across both DBMs.
- **Cryogenic service co-tenant.** The stack is described as the "common HP/Cryo flare stack." Cryogenic loads (from 04-25 deepcut) share the same stack; the SoW should keep the cryo service visible even though the package name uses "High Pressure." [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines ~497-499]
- **Source asymmetry.** The 3-25 DBM markdown carries the explicit stack geometry (660 mm OD x 60,957 mm tall) and header sizes; the 4-25 DBM enumerates many of the served HP-flare loads. Both must be read together.
- **Word package source not locally rendered.** 26020-Package_Requirements.docx package heading 38 is a binary source. Clause-level requirements that depend on it must be carried as `TBD` or `location TBD` rather than paraphrased from the workbook summary.
- **Budgetary PDF is go-by only.** The budgetary "Self Supported Dual Flare Stack" PDF named in PACKAGE_REGISTER row 58 is for pricing/delivery go-by; do not derive design values from it.

## Trade-offs

| Trade-off | Discussion | Source / Authority |
|---|---|---|
| Single shared HP/Cryo stack vs. dedicated stacks | The active basis is a single common HP/Cryo flare stack; this consolidates relief but couples 03-25 and 04-25 availability. Final flare studies remain a closeout requirement. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines ~497-499, ~548 |
| Reference/interface package vs. owned EPC package | Treating PKG-085 as reference/interface preserves vendor authority and keeps 3-25 costing scope clean, but obliges the EPC Integrator to maintain an unusually thorough integration narrative to compensate for not owning the equipment. | PACKAGE_REGISTER row 58; SCOPE_LEDGER SOW-0090 |
| Detail in SoW vs. deferral to Datasheet | The SoW intentionally stays at scope/identity/integration level; technical values (sizes, design conditions) belong in DEL-085-02 Package Datasheet. | DELIVERABLE_REGISTER rows 312-313 |
| Carry budgetary go-by values | Pulling values from the budgetary PDF would risk overstating non-authoritative content. Hold values as `TBD` until vendor datasheet inputs land. | PACKAGE_REGISTER row 58 (go-by qualifier) |

## Examples

- **Identity statement example (source-grounded):** "PKG-085 Flare Stack (High Pressure), workbook tracking 26020-02-25-001, contains HP flare stack FL-4120-1 and downstream shared flare-stack interface content, serving HP and cryogenic flare relief and blowdown for the 03-25 and 04-25 facilities." [PACKAGE_REGISTER row 58; SCOPE_LEDGER SOW-0088, SOW-0089]
- **Boundary statement example (source-grounded):** "HP relief enters the package via the 508 mm HP relief header manifolding V-4100-2 (compressor area) and V-4150-2 (tank farm); knockout liquids transfer via P-4100-2 and P-4150-2 to slop or truck-out." [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line ~497]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| CT-085-01-01 | Cost-scope ownership of the HP/Cryo flare stack: SOW-0090 states it is excluded from 3-25 costing and is a 4-25 shared asset; PACKAGE_REGISTER row 58 carries the package under WBS 02 (Mechanical) without restating the cost-scope exclusion. | `_Decomposition/.../SCOPE_LEDGER.csv` SOW-0090 | `_Decomposition/.../PACKAGE_REGISTER.csv` row 58 | Specification §Scope; Guidance §Principles; Datasheet Attributes (Cost-Scope Treatment) | PROPOSAL: defer to SOW-0090 (treat as 4-25 shared, excluded from 3-25 costing) until human boundary ruling changes; carry SoW text accordingly. | TBD |
| CT-085-01-02 | Stack configuration label: PACKAGE_REGISTER row 58 references a budgetary go-by titled "Self Supported Dual Flare Stack," while 3-25 DBM source slice names only a single "sonic HP/Cryo flare stack" with the stated OD/height. The "dual" configuration claim is not corroborated by an authoritative source slice. | PACKAGE_REGISTER row 58 (budgetary go-by reference) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines ~497-499 | Datasheet §Construction; Specification §Standards | PROPOSAL: do not carry the "Self Supported Dual Flare Stack" wording as design intent; treat configuration as TBD until vendor engineering or a final flare study confirms. | TBD |
| CT-085-01-03 | Governing codes/standards (API 521, API 537, etc.) are conventional for HP flare scope but are not enumerated in any accessible source slice for PKG-085. | Industry convention (not authoritative) | accessible source slices (silent) | Specification §Standards; R-085-01-13 | PROPOSAL: hold standards list at TBD; resolve when 26020-Package_Requirements.docx package heading 38 is rendered or when vendor inputs land. | TBD |
