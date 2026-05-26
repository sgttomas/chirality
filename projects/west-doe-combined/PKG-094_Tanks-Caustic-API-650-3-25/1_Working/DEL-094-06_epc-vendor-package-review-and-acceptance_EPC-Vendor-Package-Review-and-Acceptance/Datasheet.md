# Datasheet — DEL-094-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-094-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | `PKG-094` | `_CONTEXT.md` |
| PackageName | Tanks, Caustic (API 650) 3-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Source Reference | Workbook Packages row 86; `26020-Package_Requirements.docx` package heading 46 | `_CONTEXT.md` (clause-level slice `location TBD` — binary source) |

## Attributes

The deliverable is an EPC-Integrator-led acceptance record set for the caustic (API 650) tank package supplied by the Package Vendor for facility 03-25. It collects vendor document review outcomes, integration acceptance findings, test/inspection evidence, and turnover readiness evidence against the EPC Scope of Work (`DEL-094-01`), Package Datasheet (`DEL-094-02`), and Construction Work Package (`DEL-094-03`).

| Attribute | Value | Source |
|---|---|---|
| Acceptance target package | Tanks, Caustic (API 650) 3-25 — caustic-service atmospheric tankage for the C5+ non-regenerative caustic mercaptan treating unit | DBM `3-25_Comp_and_Liquids_DBM.md` lines 40, 389, 400, 402 |
| Subject equipment scope | 400 bbl caustic process-water, fresh-caustic, spent-caustic, and H2O2 tanks (one each — ASSUMPTION on count; DBM lists tank set but not explicit unit counts per row) | DBM line 40; line 400 |
| Tank construction basis | Atmospheric 32 oz tanks (fresh and spent caustic) with LP fuel-gas blanket, heating, and insulation; framed as API 650 per package title | DBM line 402; `_CONTEXT.md` package name |
| Caustic solution basis | 50 wt% NaOH/H2O, SG 1.75 TBC | DBM line 402 |
| Material/coating | Caustic tank material/coating details remain TBC; aluminum SHALL NOT be used in the caustic building | DBM line 402 |
| Vapour/vent interface | Spent caustic tank vents through a flame arrestor to the incinerator header and supports truck-out; fresh caustic is NOT connected to the VRU | DBM line 402 |
| Drain interface | Caustic drain design pressure governed by upstream equipment terminating at a 300# flange at the spent-caustic tank; max temp 121 °C / 250 °F TBC; min drain tank temp 80 °F | DBM line 493 |
| Minimum ambient design driver | -40 °C minimum ambient governs exposed equipment, packages, panels, instrumentation | DBM Site Basis line 145 |
| Adjacent treatment context | C5+ non-regenerative caustic mercaptan treating package (Merichem or equivalent), treats 20,000 bbl/d C5+ condensate; produces DSO and spent caustic waste | DBM line 389 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Fresh caustic (50 wt% NaOH); spent caustic with DSO carryover; caustic process water; H2O2 | DBM lines 40, 389, 400, 402 |
| Caustic regeneration | NOT in 03-25 basis; fresh caustic and make-up water consumed continuously; spent caustic and DSO produced | DBM line 389 |
| Tank type | Atmospheric, 32 oz vapour space (fresh/spent caustic) with LP fuel-gas blanket, heating, insulation | DBM line 402 |
| Spent-caustic vent path | Flame arrestor to incinerator header; truck-out supported | DBM line 402 |
| Fresh-caustic vent path | NOT connected to VRU (explicit) | DBM line 402 |
| Caustic drain max temp | 121 °C / 250 °F TBC | DBM line 493 |
| Caustic drain min temp | 80 °F (minimum drain tank temperature) | DBM line 493 |
| Heat tracing basis (drain) | 37.8 °C / 100 °F with redundant circuits under consideration | DBM line 493 |
| Material embrittlement consideration | Caustic drain service material selection requires detailed review for embrittlement | DBM line 493 |
| Ambient minimum | -40 °C | DBM Site Basis line 145 |
| Aluminum exclusion | Aluminum SHALL NOT be used in the caustic building | DBM line 402 |
| Vendor responsibility split | Vendor engineers/designs/supplies; EPC reviews/accepts/integrates | OBJ-004; `DEL-094-04` register row |

## Construction (Acceptance Evidence Items)

These are the categories of evidence the acceptance record captures. Specific tank construction values reside in `DEL-094-02 Package Datasheet`; this deliverable verifies them, it does not redefine them.

| Evidence Item | Description | Source/Driver |
|---|---|---|
| Vendor document review log | Review status per item against Vendor Document Turnover Package (`DEL-094-05`) | OBJ-010; `DEL-094-05` register row |
| Package acceptance checklist | EPC verification that vendor scope conforms to SOW, Datasheet, and CWP | OBJ-004; `_CONTEXT.md` Anticipated Artifacts |
| Test and inspection evidence | API 650 hydrotest, NDE, coating/lining verification, insulation/heating function check, blanket-gas system functional check, flame arrestor verification on spent-caustic vent | DBM line 402; ASSUMPTION on specific API 650 clause-level acceptance tests — `location TBD` (clause-level catalog not extracted from local source) |
| Material/MTR verification | Caustic-service material selection, coating, and MTRs reviewed against detailed-design closure (DBM TBC); aluminum exclusion confirmed | DBM line 402; line 493 |
| Turnover evidence | Mechanical completion, punch lists, commissioning records, custody handoff to facility operations | OBJ-010 |
| Integration interface acceptance | Tie-ins to caustic treating package contactor/pre-heater/water-wash/filter, incinerator header (via flame arrestor), LP fuel-gas blanket, caustic drain (300# flange at spent-caustic tank), truck-out connections, EHT/heating, fire/gas, and shutdown signals | DBM lines 389, 400, 402, 493; OBJ-005, OBJ-006, OBJ-009 |
| Non-conformance and open-item closure | Documented dispositions for vendor NCRs and EPC-identified gaps | OBJ-010 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- DBM `3-25_Comp_and_Liquids_DBM.md` sections SEC-06 (Liquids Hub / Caustic treating, lines 389-402), SEC-07 (Utilities — caustic drain, line 493), Site Basis (line 145), SEC-15 (specifications/codes/standards — clause-level `location TBD`)
- Decomposition snapshot `GATE-07_Final_Published_2026-05-24`:
  - `DELIVERABLE_REGISTER.csv` rows `DEL-094-01` … `DEL-094-06`
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC association)
- Workbook Packages row 86; `26020-Package_Requirements.docx` package heading 46 (binary; not directly read — clause-level content `location TBD`)

## TBD / ASSUMPTION Inventory

- `TBD`: API 650 clause-level test/inspection acceptance criteria — not extracted from accessible source slices; reside in `26020-Package_Requirements.docx` heading 46 (binary, not read).
- `TBD`: Caustic tank material and internal coating selection — DBM line 402 explicitly states "remain TBC".
- `TBD`: Caustic drain max temperature 121 °C / 250 °F (DBM marks TBC), heat-tracing redundancy configuration (under consideration).
- `TBD`: Caustic solution SG 1.75 (DBM marks TBC).
- `ASSUMPTION`: Unit count per caustic tank service (one each of process-water, fresh-caustic, spent-caustic, H2O2 at 400 bbl) — DBM line 40 enumerates the set but does not explicitly state per-service unit counts.
- `ASSUMPTION`: Specific vendor document categories captured by the review log mirror those listed in `DEL-094-05` register row (vendor document register; submittals; source-required documentation; turnover records).
- `ASSUMPTION` (PACKAGE_HEURISTIC): Objectives `OBJ-002`…`OBJ-010` apply via the package-grouping mapping; not deliverable-ID-explicit.
