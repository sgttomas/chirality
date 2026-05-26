# Procedure — DEL-088-04 Vendor Engineered Equipment Package

This Procedure describes the steps to **produce** the vendor-engineered equipment package deliverable: engineered design, supplied physical package, and the vendor package design basis and datasheet set listed in `_CONTEXT.md`. Operational steps for the package in service are out of scope here and fall to operations and to DEL-088-06 (acceptance) and downstream commissioning scope.

## Prerequisites

- DEL-088-01 (Scope of Work) and DEL-088-02 (Package Datasheet) issued by EPC Integrator and provided to Package Vendor. (Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER row 267.)
- Authoritative source references accessible to the vendor:
  - `26020-Package_Requirements.docx` package heading 41 (location TBD; binary in current state).
  - DBM-Comp_and_Liquids §"Condensate Mercaptan Treating" (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 387–402).
- Open items identified in `Guidance.md` Conflict Table addressed or carried as TBC closures in vendor design basis.
- No declared upstream dependencies in `_DEPENDENCIES.md`; ASSUMPTION: DEL-088-01 and DEL-088-02 are functional upstreams (per `_CONTEXT.md` Notes). Confirmation TBD.

## Steps

1. **Receive and confirm anchoring documents.** Vendor receives DEL-088-01 Scope of Work and DEL-088-02 Package Datasheet from EPC Integrator. Vendor confirms scope coverage (SOW-0055..0058) and identifies discrepancies between Datasheet and DBM source slice. (Source: DELIVERABLE_REGISTER row 267; SCOPE_LEDGER rows 56–59.)
2. **Establish vendor package design basis.** Develop a written design basis covering: capacity (20,000 BPD C5+ condensate), non-regenerative caustic technology, caustic concentration (50 wt% NaOH, SG TBC), extractable slate (H2S, CO2, C1-C4 RSH), product targets (C1-C3 RSH < 175 ppmw S; total S < 0.5 wt%), DSO entrainment expected/design (30/50 ppmw S TBC), indoor caustic building, no aluminum. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating; SOW-0056..0058.)
3. **Close vendor TBC items.** Confirm caustic SG, DSO entrainment design, and caustic tank material/coating selections. Record each closure with rationale in the design basis. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
4. **Engineer the package.** Design and size the caustic C5+ contactor, pre-heater, caustic outlet filter, water wash, pumps, instrumentation, piping, controls, and the DSO/spent-caustic/fresh-caustic/fresh-water tankage. Layout for the indoor caustic building; specify non-aluminum materials. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating; SOW-0057; SOW-0058.)
5. **Define interface flanges.** Specify and document the package's external interfaces: condensate inlet/outlet, fresh caustic and water make-up, spent caustic and DSO outlets, incinerator overhead vent, dilution gas, enrichment gas. Confirm no fresh-caustic VRU connection. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
6. **Produce the vendor datasheet set.** Issue datasheets for each major equipment item and tank, including the spent caustic tank atmospheric 32-oz with LP fuel-gas blanket, heating, insulation, and flame-arrestor venting/truck-out provisions. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
7. **Submit for EPC Integrator integration review.** Submit design basis, datasheets, and package GA for EPC review under the DEL-088-06 acceptance flow. Address EPC comments. (Source: DELIVERABLE_REGISTER row 269.)
8. **Fabricate/supply the engineered equipment package.** Manufacture, assemble, and FAT-test the package in accordance with the issued-for-construction design. Quality and inspection regime per vendor QA plan. (Steps: ASSUMPTION; standard vendor package execution flow; specific QA standards location TBD.)
9. **Deliver the package and supporting documentation.** Ship the physical equipment package and provide the vendor package design basis and datasheet set as the deliverable artifacts listed in `_CONTEXT.md`. Vendor document register and turnover records are handled under DEL-088-05. (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER rows 267, 268.)

## Verification

| Step | Verification |
|---|---|
| 1 | Scope traceability matrix: SOW-0055..0058 ↔ vendor design basis sections. |
| 2 | Design basis document review and red-line against DBM-Comp_and_Liquids §Condensate Mercaptan Treating. |
| 3 | TBC closure log audit; each TBC has a closure entry with vendor source. |
| 4 | Sizing calculation review; product target margin demonstration (REQ-088-04-04, -05). |
| 5 | Interface schedule cross-checked against EPC-side tie-in schedule (DEL-088-01/02). |
| 6 | Datasheet audit against `Specification.md` REQ-088-04-09..-16. |
| 7 | EPC Integrator integration review record (DEL-088-06). |
| 8 | FAT report; material certifications (no aluminum in caustic building). |
| 9 | Delivery acceptance receipt; design basis and datasheet set archived. |

## Records

- Vendor package design basis (deliverable artifact).
- Vendor package datasheet set (deliverable artifact).
- TBC closure log.
- Scope traceability matrix (SOW ↔ vendor design basis).
- FAT report and inspection/material certifications (location TBD; vendor QA system).
- EPC integration review and acceptance record (held under DEL-088-06).
- Delivery and turnover documentation (held under DEL-088-05).
