# Specification — DEL-068-06 EPC Vendor Package Review and Acceptance (TEG Dehydration Unit)

## Scope

### In scope
This deliverable specifies the EPC Integrator's review-and-acceptance work product for the TEG Dehydration Unit package (`PKG-068`, one-by-100 percent sour-gas TEG package downstream of inlet compression at 03-25). It defines the evidence the EPC Integrator must produce to demonstrate that the Package Vendor's `DEL-068-04` Vendor Engineered Equipment Package and `DEL-068-05` Vendor Document Turnover Package satisfy the EPC Scope of Work (`DEL-068-01`), Package Datasheet (`DEL-068-02`), and Construction Work Package (`DEL-068-03`).

Sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 ("TEG Dehydration Basis", "TEG Package Equipment"); `_Sources/26020-Package_Requirements.docx` heading 23 (location TBD at sub-heading level); `DELIVERABLE_REGISTER.csv` row `DEL-068-06`.

### Out of scope
- Authoring or modifying the vendor-side engineering deliverables themselves; those are `DEL-068-04` / `DEL-068-05` outputs.
- Authoring the EPC SOW (`DEL-068-01`), Package Datasheet (`DEL-068-02`), or Construction Work Package (`DEL-068-03`); this deliverable references and verifies against them.
- Acceptance of upstream inlet-compression packages, downstream 04-25 inlet gathering, or shared utility systems (LP fuel gas, LP flare, HP flare, BPCS) beyond the package boundary; those are governed by their own packages.
- Operations procedures for the TEG unit (covered by IOM and operating procedures, not by this acceptance pack).

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| `R-068-06-01` | The acceptance evidence MUST cover all SOW items mapped to this deliverable: `SOW-0237`, `SOW-0238`, `SOW-0239`, `SOW-0240`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `OBJECTIVE_SCOPE_MAP.csv` |
| `R-068-06-02` | The vendor document review log MUST enumerate every vendor engineering deliverable listed for the TEG Dehydration Unit at `26020-Package_Requirements.docx` heading 23 and record disposition (`SUBMITTED`, `ACCEPTED`, `REJECTED`, `OPEN`). Specific enumerated rows are `TBD` until the heading 23 sub-list is extracted from the binary source. | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" (location TBD) |
| `R-068-06-03` | The package acceptance checklist MUST verify the TEG package equipment scope: inlet filter coalescer, contactor, level pot, lean TEG cooler, flash drum, full-flow rich-TEG solids filters, charcoal (carbon/particle) filter, lean/rich exchanger, rich-TEG solids filter, TEG pumps (2 x 100 percent), still column, stripping column, reflux condenser, reboiler, surge drum, regen cooler, regen overhead scrubber, regen overhead pumps, makeup tank, and makeup pump. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 "TEG Package Equipment" |
| `R-068-06-04` | The acceptance evidence MUST confirm the package process tie-ins: inlet from second-stage compressor discharge (800 psig SCA-002 basis); treated-gas export to 04-25 inlet gathering; flash-gas pressure-regulated to 04-25 SOC first-stage suction; contactor blowdown automated to HP flare; regen overhead to LP flare via LP KO drum `V-3900-2`. | SEC-05 "TEG Dehydration Basis", "TEG Package Equipment", "Compression Design Conditions"; SEC-08 utility narrative |
| `R-068-06-05` | The acceptance evidence MUST confirm utility tie-ins: LP fuel-gas supply to TEG stripping (reboiler / stripping column); instrument air; electrical power; heat-tracing/insulation where applicable. | "Utility Integration Basis"; SEC-05 |
| `R-068-06-06` | The acceptance evidence MUST cover each physical interface flagged for `PKG-068` at `26020-Packages_Interfaces_4_export.xlsx` Packages row 97 (per-interface `Yes/No` flags are `location TBD` until the spreadsheet is read). | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 97 (location TBD) |
| `R-068-06-07` | The acceptance evidence MUST include pressure-vessel registration and pressure-test evidence for coded vessels in the TEG package (contactor, flash drum, surge drum, regen overhead scrubber, lean/rich exchanger shells where coded, reflux condenser/reboiler shells where coded): Pressure Equipment Registration Package, Pressure Vessel Data Sheets, and Hydrotest / Pressure Test Packages. | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" — Static pressure equipment / Process piping interfaces (location TBD) |
| `R-068-06-08` | The acceptance evidence MUST include rotating-equipment FAT and performance evidence for `TEG pumps` (2 x 100 percent, rotary gear or positive-displacement, single mechanical seals), regen overhead pumps, and makeup pump: pump data sheets, NPSH calculations, mechanical seal / lube oil specifications, motor starting study, and Equipment FAT / Performance Test Reports. | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" — Rotating equipment / pumps (location TBD); SEC-05 "TEG Package Equipment" |
| `R-068-06-09` | Quality records MUST be assembled: Supplier Quality Plan, ITP execution evidence, Material Test Reports / Certificates, Inspection Release Certificate, and Manufacturing Record Book / Vendor Data Book. | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" — Core vendor documents (location TBD) |
| `R-068-06-10` | Turnover MUST include the SPIR, Logistics / Shipping Plan, and Mechanical Equipment IOM Manual. | `26020-Package_Requirements.docx` heading 23, "Vendor Engineering Deliverables" (location TBD) |
| `R-068-06-11` | Numeric design/operating values used in acceptance (gas flow 82.5 MMSCFD normal/design; inlet pressures 4,502 / 5,378 / 4,502 / 6,205 kPag low/normal/design/maximum; expected inlet temperature 110 deg F; outlet water content not more than 4 lb H2O/MMSCF; contactor turndown 3:1 TBC; regeneration turndown 2:1; surge drum 30 min retention at 50 psig; contactor Fs not more than 3.0 with at least three theoretical stages and inlet/outlet demisters; rich-TEG 5 micron full-flow filtration plus 20 percent carbon/particle slipstream) MUST be reconciled to vendor-submitted equipment data sheets and process calculations. Where vendor data has not been submitted or differs from SEC-05, the variance MUST be flagged and either resolved or carried in the open-items log. | SEC-05 "TEG Dehydration Basis"; SEC-05 "TEG Package Equipment"; "Equipment Count Table" |
| `R-068-06-12` | Open items called out in `26020-Package_Requirements.docx` heading 23 ("Scope Notes / Open Items") MUST be closed or carried with explicit disposition in the acceptance record. Specific open items are `TBD` until the heading 23 sub-list is extracted. | `26020-Package_Requirements.docx` heading 23 (location TBD) |
| `R-068-06-13` | The acceptance evidence MUST verify the integration of the package PLC / Unit Control System with the BPCS per the project control-system architecture: replicated values, alarm priorities, trip interfaces, and protocol (Modbus / Kepware KepserverEX where applicable). Final package data maps, permissive logic, and trip interfaces are resolved during vendor integration. | "Control System Architecture"; "Package and Third-Party Interfaces" |
| `R-068-06-14` | The acceptance evidence MUST confirm the makeup tank configuration (atmospheric, fuel-gas blanketed, heated/insulated, NOT connected to VRU) and the flash-drum hydrocarbon-liquid manual drain to produced-water drain. | SEC-05 "TEG Package Equipment" |
| `R-068-06-15` | TEG identified among produced-water contaminants in the current source set MUST be carried into the acceptance review's interface to the produced-water disposition (for awareness, not for re-engineering produced-water treatment in this acceptance scope). | SEC-05 / SEC-06 narrative on produced-water contaminants |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Provincial pressure equipment registration regime applicable to the project (typically ABSA in Alberta) | Required for the Pressure Equipment Registration Package referenced for TEG-package coded vessels. | location TBD — not stated in available source slices; ASSUMPTION based on project jurisdiction. |
| Pressure vessel design code (ASME BPVC Section VIII or CSA B51 as applicable) | Governs vessel data sheets and acceptance of coded vessels in the TEG package (contactor, flash drum, surge drum, regen overhead scrubber, etc.). | location TBD — not stated in available source slices; ASSUMPTION typical to scope. |
| Industry TEG / glycol dehydration design references (e.g., GPSA Engineering Data Book, API Spec 12GDU) | Likely governing for TEG unit sizing/configuration and FAT acceptance. | location TBD — not stated in available source slices; ASSUMPTION. |
| Industry rotating equipment standards (API 676 for rotary positive-displacement pumps; API 682 for mechanical seals where applicable) | Likely governing for TEG pumps and makeup pump acceptance. | location TBD — not stated in available source slices; ASSUMPTION. |
| NEMA MG1 / area-classification standards (typical) | Governs motors and electrical area classification at the TEG package skid. | location TBD — not stated for the TEG skid in the available source slice; ASSUMPTION (consistent with electrification basis described elsewhere in the DBM). |

## Verification

| Req ID | Verification Approach |
|---|---|
| `R-068-06-01` | Traceability matrix mapping each SOW item (`SOW-0237..0240`) to acceptance-checklist rows and to evidence artifacts. |
| `R-068-06-02` | Document-by-document review log inspection; every heading 23 vendor deliverable has a tracked disposition. (Heading 23 sub-list extraction is a precondition.) |
| `R-068-06-03` | Walk-down and as-built/IFC drawing review against the SEC-05 "TEG Package Equipment" list; equipment list reconciled to vendor GA drawings and equipment list. |
| `R-068-06-04` | P&ID and tie-in list inspection; reconciliation with `DEL-068-03` Construction Work Package and `DEL-068-02` Package Datasheet; confirmation of HP-flare and LP-flare interfaces with the respective flare packages. |
| `R-068-06-05` | Utility tie-in inspection against the LP fuel-gas, instrument-air, and electrical-power packages; heat-trace energization records where applicable. |
| `R-068-06-06` | Interface-by-interface checklist against the heading 23 Physical Interface Summary equivalent and `26020-Packages_Interfaces_4_export.xlsx` Packages row 97 (per-interface flags to be confirmed at acceptance). |
| `R-068-06-07` | Hydrotest packages signed off; Pressure Equipment Registration Package accepted by registration authority; vessel data sheets reconciled with as-built. |
| `R-068-06-08` | FAT witness records for TEG pumps, regen overhead pumps, and makeup pump; NPSH calculation review; mechanical seal / lube oil acceptance; motor starting study accepted. |
| `R-068-06-09` | Quality records audit; Inspection Release Certificate issued; MRB / VDB compiled and accepted. |
| `R-068-06-10` | Receipt inspection records; SPIR provided and accepted; IOM in turnover bundle. |
| `R-068-06-11` | Reconciliation table between EPC Package Datasheet (`DEL-068-02`) / SEC-05 values and vendor-submitted values; TBD entries flagged with named owner. |
| `R-068-06-12` | Open-items log carried into commissioning; explicit closure or carryover noted. |
| `R-068-06-13` | Package-PLC / BPCS integration test records; signal-list and alarm/trip cause-and-effect review; protocol conformance evidence. |
| `R-068-06-14` | Walk-down of makeup tank blanketing, heating, insulation, and (absence of) VRU connection; flash-drum drain configuration confirmed. |
| `R-068-06-15` | Cross-reference note in the acceptance pack linking TEG presence in produced water to the produced-water package interface; no re-engineering performed here. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log.
- Package acceptance checklist (SOW-, interface-, equipment-, and artifact-indexed).
- Test / inspection evidence bundle (FAT, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, registration package, SPIR, IOM).
- Open-items disposition log.

Standards-related and numeric design values that depend on vendor submittals carry `TBD` placeholders until the Package Vendor deliverables are accepted. Tag-level identifiers for TEG package equipment are `TBD` until the vendor equipment list / GA drawings are submitted.
