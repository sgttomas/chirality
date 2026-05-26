# Guidance: DEL-098-02 Package Datasheet

## Purpose

The package datasheet exists to turn the accepted Gate 7 decomposition basis and the 26020-Package_Requirements.docx package heading 50 ("26020-03-PT-19-007 - Tanks, Sour Water") into a concise EPC Integrator technical handoff for `PKG-098` Tanks, Sour Water (API 650) 3-25. Its role is to preserve package identity, scope, responsibility split, named equipment, stated operating/design conditions, interface facts, and objective context for downstream vendor package engineering and design.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet`; `PACKAGE_REGISTER.csv` row `PKG-098`; `ARTIFACT_REGISTER.csv` artifacts `ART-1458F2586B`, `ART-F958B0973F`, `ART-119F7B5D2B`, `ART-914A0B9939`; 26020-Package_Requirements.docx package heading 50.

## Principles

- Preserve workbook and CoA identity exactly: `PKG-098`, workbook ID 98, workbook row 93, WBS 03, Mechanical, "Tanks, Sour Water (API 650) 3-25", CoA tracking number `26020-03-19-007`. Source: `PACKAGE_REGISTER.csv` row `PKG-098`.
- Keep the package vendor / EPC integrator split explicit. Vendor owns engineering, design, vendor documentation, and physical equipment; EPC owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. Source: `PACKAGE_REGISTER.csv` row `PKG-098`; `SCOPE_LEDGER.csv` row `SOW-0221`.
- Reproduce the package heading 50 Basic Scope and Major Included Equipment verbatim (tag numbers, item counts, construction features). Source: 26020-Package_Requirements.docx package heading 50, Basic Scope and Major Included Equipment.
- Carry the Scope Notes / Open Items conditions exactly as stated, including the explicit TBDs (Item No. 2 operating temperature, driver, capacity per Appendix A). Source: 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items.
- Treat the nine physical interface facts as datasheet evidence, not as standalone deliverables. Source: Gate 7 `PROJECT_DECOMP.md`; `INTERFACE_REGISTER.csv` rows for `PKG-098`; `ARTIFACT_REGISTER.csv` Interface Fact Evidence rows.
- Use objective mappings (`OBJ-002` through `OBJ-010`) as context, not as mechanical design values. Source: `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-098-02_package-datasheet`; `OBJECTIVE_REGISTER.csv`.
- Leave unsupported codes, materials, plate thicknesses, nozzle schedules, NACE/H2S detail, capacities, and modifications-to-API-650 specifics as `TBD`. Source: 26020-Package_Requirements.docx package heading 50; `_REFERENCES.md` Missing / Deferred References.

## Considerations

The strongest accepted facts for this deliverable are package identity, the responsibility split, the named tank items and tags, the four common construction features, the explicit operating and design conditions, and the nine interface facts. Items not stated at heading 50 — including the underlying RFQ Source Basis document (Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx) and Appendix A capacity data — are not locally accessible at the deliverable folder during this run, so capacity/throughput, driver, Item No. 2 operating temperature, and detailed engineering parameters must remain `TBD`.

The analog Sour Condensate package (heading 49 in the same document) explicitly names blanket gas per API 2000, PVRV/EPRV detail, VRU header connection, NACE compliance, and fill-rate constraints. Heading 50 for Sour Water does not repeat those statements. Carrying those features into this datasheet would be reading across packages and is not done here; they appear in this guidance as ASSUMPTIONS that the vendor package engineering will need to resolve, not as datasheet content.

The package maps to nine objectives:

- `OBJ-002`: 3-25 compressor station and liquids hub scope (produced-water handling).
- `OBJ-003`: commercial/boundary preservation for produced water and cross-facility flows.
- `OBJ-004`: vendor-owned mechanical package execution with separate EPC integration review.
- `OBJ-005`: facility electrical integration (grounding/bonding, area lighting, cathodic protection).
- `OBJ-006`: controls/instrumentation and package interface integration (I&C / control cabling).
- `OBJ-007`: shared utilities and ancillary support (relief/flare/vent, drains).
- `OBJ-008`: civil/structural/site/foundation support (foundations and structural supports by others).
- `OBJ-009`: sour-service safety, relief, drain/containment, environmental, codes/standards visibility.
- `OBJ-010`: vendor-documentation, sparing, operability, and turnover evidence (carried via DEL-098-04 / DEL-098-05).

Sources: `OBJECTIVE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-098-02_package-datasheet`.

## Trade-offs

| Topic | Conservative handling | Reason |
|---|---|---|
| Codes beyond modified API 650 | Mark API 2000 (venting), NACE MR0175/MR0103 (sour service), coating qualification, and electric heat-trace standards as ASSUMPTION (likely applicable) and `TBD` for clause-level requirements. | Heading 50 names only modified API 650; other codes are not stated at heading 50. The analog Sour Condensate heading names API 2000 and NACE, but cross-reading packages is not authoritative. |
| Capacity / driver / Item No. 2 temperature | Hold as `TBD` (driver and Item No. 2 temperature) and reference Appendix A (capacity) until the appendix or vendor RFQ slice is locally accessible. | Heading 50 explicitly defers these to Appendix A and "TBD" in the source. |
| H2S concentration and NACE compliance | Leave as `TBD`. | Heading 50 implies sour service through tank function but does not state H2S concentration or NACE compliance. |
| Items-by-others scope | Reproduce verbatim ("foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase etc."). | This boundary statement controls vendor-versus-EPC scope; paraphrasing risks shifting responsibility. |
| Interface set | Carry only the nine YES interfaces named in `INTERFACE_REGISTER.csv`. | The register is the accepted truth for this package's applicable interfaces. |
| Vendor engineering deliverable list | Do not enumerate the full list inside this datasheet; track it via DEL-098-04 / DEL-098-05 with reference to package heading 50, Vendor Engineering Deliverables. | The list is large and operationally belongs in the vendor turnover and equipment-package deliverables. |
| Raw RFQ source (Bid Docs/Budgetary/...) | Do not reinterpret without local access. | RFQ document is named in heading 50 but not locally accessible in this deliverable's references. |

## Examples

A direct example of a Sour Water tanks package datasheet for `PKG-098` is not separately available. The closest analog within the same source document is heading 49 ("26020-03-PT-19-005 - Tanks, Sour Condensate"), which uses the same vendor-package structure and provides additional named features (blanket gas per API 2000, PVRV/EPRV, VRU header, NACE compliance, fill-rate). That analog is cited only as a directional reference and not transcribed into this deliverable. Source: 26020-Package_Requirements.docx headings 49 and 50.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-098-02-001 | Codes beyond modified API 650 (API 2000 venting, NACE MR0175/MR0103, coating qualification, electric heat-trace standards) are likely applicable but not stated at package heading 50 for Sour Water; the analog Sour Condensate heading (49) names some of them. | 26020-Package_Requirements.docx package heading 50, Major Included Equipment | 26020-Package_Requirements.docx package heading 49 (Sour Condensate), Major Included Equipment | Datasheet Construction; Specification Standards/Requirements; Procedure Steps/Verification | Hold additional codes as ASSUMPTION/TBD pending vendor RFQ slice or explicit human ruling; do not transcribe the Sour Condensate features into the Sour Water datasheet. | TBD |
| HRR-098-02-002 | Capacity / design throughput is deferred to Appendix A and the driver is "TBD" at the heading, but Appendix A is not locally accessible. | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items | `_REFERENCES.md` Missing / Deferred References | Datasheet Conditions; Specification Requirements; Procedure Records | Mark capacity, driver, and Item No. 2 operating temperature as `TBD` and route to vendor package engineering for closure. | TBD |
| HRR-098-02-003 | The underlying RFQ "Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx" is named as Source Basis but is not locally accessible in this deliverable's references. | 26020-Package_Requirements.docx package heading 50, Source Basis line | `_REFERENCES.md` Missing / Deferred References | Datasheet References; Specification Standards; Guidance Considerations | Resolve a local source slice of the RFQ in PREPARATION or via human ruling before adding values that depend on it. | TBD |
| HRR-098-02-004 | Sour service is implicit in the tank function and product, but H2S concentration and NACE compliance are not stated at heading 50 for Sour Water. | 26020-Package_Requirements.docx package heading 50, Basic Scope and Major Included Equipment | `OBJECTIVE_REGISTER.csv` row `OBJ-009` (sour-service safety/environmental visibility) | Datasheet Conditions/Construction; Specification Requirements/Standards | Treat H2S characterization and NACE compliance as ASSUMPTION (likely applicable) and hold clause-level requirements as `TBD` pending source slice or human ruling. | TBD |
