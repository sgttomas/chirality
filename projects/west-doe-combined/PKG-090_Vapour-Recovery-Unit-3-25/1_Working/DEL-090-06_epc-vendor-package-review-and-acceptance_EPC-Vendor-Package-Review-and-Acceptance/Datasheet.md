# Datasheet: DEL-090-06 — EPC Vendor Package Review and Acceptance

> Descriptive characterization of the EPC Integrator's vendor package review-and-acceptance deliverable for PKG-090 Vapour Recovery Unit 3-25. Values are drawn from accessible decomposition source slices (Gate 7 snapshot) which themselves cite `26020-Package_Requirements.docx package heading 43` and Workbook Packages row 100. Direct access to the binary `.docx`/`.xlsx` source files was not available; affected detail is marked `TBD` or `ASSUMPTION` as noted.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-090-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | `PKG-090` | `_CONTEXT.md` |
| PackageName | Vapour Recovery Unit 3-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Covers Scope Items | SOW-0249, SOW-0250, SOW-0251, SOW-0252 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC; ASSUMPTION — best-effort mapping) |
| Source Reference | Workbook Packages row 100; 26020-Package_Requirements.docx package heading 43 | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Reviewed Package Subject | Two (2) complete 100% capacity Vapour Recovery Unit (VRU) compressor packages in lead-lag configuration, sour service, housed in one building. | SOW-0250 (26020-Package_Requirements.docx package heading 43; Basic scope) |
| Trains | 2 (Train 1, Train 2); each train two-stage. | SOW-0250; SOW-0251 |
| Compressor Make/Model | Ro-Flo 12S/212M, two-stage rotary vane, positive displacement. | SOW-0250; SOW-0251 |
| Compressor Quantity | 4 total (Train 1 Stage 1 + Stage 2; Train 2 Stage 1 + Stage 2). 2 x 100% capacity. | SOW-0251 |
| Driver | 200 HP, 600 V, 3-phase, 60 Hz, VFD-ready; one motor per train drives both Stage 1 and Stage 2. | SOW-0251; SOW-0252 |
| Cooler Motors | VFD-ready, 600 V. | SOW-0252 |
| Service | Sour service: 0.4588 mol% H2S, 0.4314 mol% CO2; NACE designation applies. | SOW-0251 |
| Seal Plan | Dual mechanical pressurized barrier seal (Plan 53 type) using fuel gas; alarms and primary vent to LP flare. | SOW-0251 |
| Expected Flow per Unit | 0.510 MMSCFD | SOW-0252 |
| EPC Review Artifacts (anticipated) | Vendor document review and comment log (ART-08602095B0); vendor package acceptance and turnover checklist (ART-2BE816FC33); factory/shop test and inspection evidence (ART-63586A61E0). | `ARTIFACT_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| 1st-stage intercooler outlet temperature (operating) | 48.9 °C | SOW-0252 |
| 2nd-stage aftercooler outlet temperature (operating) | 60.0 °C | SOW-0252 |
| 1st-stage dewpoint temperature | 45.6 °C | SOW-0252 |
| 2nd-stage dewpoint temperature | 53.2 °C | SOW-0252 |
| Design suction pressure | 0.9 kPag (2 oz/in²) | SOW-0252 |
| Design discharge pressure | 483 kPag (70 psig) | SOW-0252 |
| Design capacity | 28 e3m³/d (1 MMSCFD) | SOW-0252 |
| Design temperature | 102 °C | SOW-0252 |
| Battery-limit boundary (EPC vs Vendor) | Shipping compressor packages to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs are "By others" (EPC Integrator scope). | SOW-0252 |

## Construction (review/acceptance evidence basis)

EPC review-and-acceptance addresses the **vendor package as delivered** against EPC Scope of Work, Package Datasheet, and Construction Work Package. Acceptance evidence is composed of:

- Vendor document review log entries against the EPC document list. Source: `_CONTEXT.md` anticipated artifacts; ART-08602095B0.
- Package acceptance checklist (mechanical, electrical, instrumentation, NACE/sour-service, seal plan, VFD readiness). Source: `_CONTEXT.md`; ART-2BE816FC33.
- Test/inspection evidence (factory/shop test records). Source: ART-63586A61E0.
- Turnover evidence (vendor document turnover from DEL-090-05). Source: `_CONTEXT.md`.

Detailed acceptance checklist line items: `TBD` — depend on the EPC Scope of Work, Package Datasheet, Construction Work Package and Vendor Engineered Equipment Package which are sibling deliverables (DEL-090-01, DEL-090-02, DEL-090-03, DEL-090-04) and on full source text in `26020-Package_Requirements.docx package heading 43` (binary; not locally accessible).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (DEL-090-06 row)
  - `SCOPE_LEDGER.csv` (SOW-0249, SOW-0250, SOW-0251, SOW-0252)
  - `ARTIFACT_REGISTER.csv` (ART-08602095B0, ART-2BE816FC33, ART-63586A61E0)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- `26020-Package_Requirements.docx package heading 43` — Workbook Packages row 100 (binary source; **location TBD** for clause-level slicing; not locally accessible at this time).
