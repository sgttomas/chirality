# Procedure: DEL-054-04 Vendor Engineered Equipment Package

This procedure describes how to **produce** the vendor engineered equipment package as a production unit. Operation of the installed equipment is governed by the construction work package (DEL-054-03) and downstream operations documentation, not by this deliverable.

## Prerequisites

- DEL-054-01 EPC Scope of Work is issued for vendor use. [Source: `DELIVERABLE_REGISTER.csv` row `DEL-054-01_scope-of-work`]
- DEL-054-02 EPC Package Datasheet is issued for vendor use; this is the controlling technical input. [Source: `DELIVERABLE_REGISTER.csv` row `DEL-054-02_package-datasheet`; `_CONTEXT.md` Scope]
- Vendor has access to the DBM source slice that defines HP flare KO drum context (V-4100-1, P-4100-1, header sizes, freeze-protection, spacing). [Source: `4-25_Deepcut_DBM.md` lines 287, 2028, 2033, 2039, 2534]
- Vendor has access to 26020-Package_Requirements.docx package heading 9 content (clause-level access is TBD - request from EPC Integrator). [Source: `_REFERENCES.md`; `_CONTEXT.md`]
- Declared upstream dependencies: none declared during PREPARATION. [Source: `_DEPENDENCIES.md`]

## Steps

1. **Confirm scope and inputs.** Read DEL-054-01 and DEL-054-02 in full; identify the controlling battery limits, performance basis, and interface points. Record any discrepancies between the EPC inputs and the DBM source slice in a vendor-internal conflict log and surface to EPC Integrator. [Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows DEL-054-01, DEL-054-02]
2. **Establish vendor design basis.** Author the vendor package design basis document covering process duty, mechanical design conditions, materials, instrumentation, electrical/control interfaces, and freeze protection. Anchor on tags V-4100-1 and P-4100-1. Include explicit ASSUMPTIONs for any value not directly traceable to DEL-054-02 or to the DBM, and mark open items per the DBM (relief volumes, backpressures, shared 03-25/04-25 allocation) as TBC during detailed design. [Source: `4-25_Deepcut_DBM.md` lines 1834, 2021, 2028, 2033, 2534]
3. **Produce vendor datasheet set.** Issue vessel datasheet (H.P. FLARE K.O. DRUM, V-4100-1), pump datasheet (HP FLARE K.O. DRUM TRANSFER PUMP, P-4100-1), and ancillary instrument/component datasheets. Datasheet content must align with DEL-054-02 Package Datasheet handoff data. [Source: `4-25_Deepcut_DBM.md` line 2534; `_CONTEXT.md` Anticipated Artifacts]
4. **Produce engineering drawings.** Equipment GA, P&ID extensions to the EPC P&ID, layout drawings respecting >=10 m clearance to vegetation/fire hazards, and heat-tracing/insulation drawings for outside-of-heated-building HP flare piping (with PSV-outlet free-drain exception). [Source: `4-25_Deepcut_DBM.md` lines 287, 2033]
5. **Perform vendor design review.** Conduct an internal vendor design review prior to fabrication release; capture review findings and dispositions. [ASSUMPTION - standard vendor production-unit gate; not stated at clause level in available sources]
6. **Submit to EPC Integrator for integration review.** Issue the vendor design basis, datasheet set, and drawings to the EPC Integrator. Integration review and acceptance evidence is captured under DEL-054-06. [Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-054-06`]
7. **Fabricate and supply equipment.** After acceptance of design, fabricate the vessel and pump, perform vendor-shop inspection and testing (hydrotest, NDE, PMI as applicable), and prepare the physical equipment package for shipment. [ASSUMPTION - standard fabrication path; specific QC plan TBD pending DEL-054-02 issue]
8. **Compile vendor turnover documents.** Assemble vendor data books, MTRs, test certificates, and turnover documentation for delivery into DEL-054-05 Vendor Document Turnover Package. [Source: `DELIVERABLE_REGISTER.csv` row `DEL-054-05`]
9. **Hand off to construction.** Deliver equipment and turnover documents per DEL-054-03 Construction Work Package; provide field engineering support during installation/tie-in as agreed with EPC Integrator. [Source: `DELIVERABLE_REGISTER.csv` row `DEL-054-03`]

## Verification

| Step | Verification | Source |
|---|---|---|
| 1 | Vendor records DEL-054-01 / DEL-054-02 as controlling inputs in the design basis. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| 2 | Vendor design basis covers all required topics; ASSUMPTION/TBD items explicitly labeled. | `4-25_Deepcut_DBM.md` lines 2021, 2028 |
| 3 | Datasheets reference V-4100-1 and P-4100-1; values consistent with DEL-054-02. | `4-25_Deepcut_DBM.md` line 2534 |
| 4 | Drawings show 508 mm (20 in) header tie, heat-tracing extent, and >=10 m spacing. | `4-25_Deepcut_DBM.md` lines 287, 2028, 2033 |
| 5 | Vendor internal design review record exists prior to fabrication release. | ASSUMPTION |
| 6 | EPC Integrator acceptance logged under DEL-054-06. | `DELIVERABLE_REGISTER.csv` row `DEL-054-06` |
| 7 | Hydrotest, NDE, and PMI results within specification; deviations resolved. | TBD pending DEL-054-02 |
| 8 | Vendor data book complete per DEL-054-05 register. | `DELIVERABLE_REGISTER.csv` row `DEL-054-05` |
| 9 | Field receipt and tie-in evidence under DEL-054-03. | `DELIVERABLE_REGISTER.csv` row `DEL-054-03` |

## Records

- Vendor package design basis (single controlled document).
- Vendor datasheet set (vessel V-4100-1, pump P-4100-1, ancillaries).
- Engineering drawings (GA, P&ID extension, layout, heat-tracing/insulation).
- Vendor internal design review record.
- EPC Integrator integration-review correspondence (feeds DEL-054-06).
- Fabrication inspection and test records, MTRs, NDE/PMI reports (feed DEL-054-05).
- Shipping documentation and equipment release notice (feeds DEL-054-03).
