# Guidance — EPC Vendor Package Review and Acceptance (DEL-064-06)

## Purpose

This deliverable closes the loop between vendor scope and EPC-Integrator scope for the Tanks, Water (API 650) 4-25 package (PKG-064, tag `26020-01-PT-19-002`). It tells the EPC Integrator what to check, in what order, against which sources, before declaring the package accepted and ready to feed the Construction Work Package (DEL-064-03) and Vendor Document Turnover (DEL-064-05).

It exists because the vendor and the EPC Integrator carry split scope: vendor designs, fabricates, and supplies the engineered package (DEL-064-04); the EPC Integrator installs, ties in, and operates the broader facility (DEL-064-03 and downstream). The acceptance gate is the only point where source intent (SRC1) is reconciled against what the vendor actually produced.

## Principles

- **Source authority, not narrative authority.** Acceptance decisions are made against `_Sources/26020-Package_Requirements.docx` heading 19 and downstream vendor design basis, not against decomposition prose. Where prose differs from source, treat the source as authoritative and surface the discrepancy.
- **Acceptance is binary; deviations are explicit.** A vendor item is either accepted, accepted-with-comment (deviation logged and ruled), or rejected. There is no implicit acceptance through silence.
- **Interface "No" entries are walls, not soft preferences.** Source explicitly marks interfaces such as Utility Piping, Electrical Power, EHT, Communications, Building HVAC, F&G, Maintenance Access, Product Loading, and Pipeline/Pigging as not applicable. Vendor deliverables claiming work in these areas require explicit human ruling before acceptance.
- **"By others" exclusions are honored.** Foundations, mounting at site, electrical/instrumentation, platforms, and staircase are EPC-side scope per the source. Accepting them as vendor scope inflates vendor liability and breaks the construction plan.
- **Modified API 650 is not API 650.** The source cites *modified* API 650. The acceptance gate must locate and accept the modification points (expected in vendor MEC-001); failure to do so quietly silently re-interprets the standard.
- **TBDs travel.** Open items in the source ("Other throughputs", "Operating temperature for Item No. 1", "Interface Coordination Notes") must either close with evidence or be explicitly carried into acceptance as named deviations with human ruling.

## Considerations

- **Sequencing with sibling deliverables.** The acceptance gate consumes outputs of DEL-064-04 (vendor engineering) and DEL-064-05 (turnover). It is constrained by DEL-064-01 (SOW), DEL-064-02 (Datasheet), and DEL-064-03 (CWP). Reviewing without those references present is premature; review log entries should cite the version/snapshot of each reference used.
- **Two-population check on the Acceptance Inventory.** The Inventory in `Datasheet.md` is comprehensive per source. Real vendor submittals will be a subset (some items combined, some renumbered). Build a mapping table; do not assume one-to-one.
- **Interface deliverables are cross-discipline.** Items like CTL-026 (Package Vendor Interface Specification), STR-013 (Anchor Bolt / Embedment Drawings), and PIP-004 (Tie-In List / Tie-In Scope Sheets) only become meaningful at acceptance when reviewed alongside the EPC-side counterparts (foundations, control system, tie-in drawings). Schedule cross-discipline review windows.
- **Interface artifact ambiguity.** Source cites `26020-Packages_Interfaces.3.xlsx`; the locally accessible file is `26020-Packages_Interfaces_4_export.xlsx`. Version delta is unverified. Treat as ASSUMPTION until reconciled.
- **Modification points to API 650 are the principal technical risk.** They are not enumerated in the source slice. Plan an early targeted review of MEC-001 before broader acceptance, so modification-driven changes to MEC-005, MEC-011, and MEC-014 are caught upstream.
- **Vapour-space safety basis.** LP fuel gas blanket on a water tank is non-trivial; expect HAZOP/SIL implications usually addressed through CTL-005 (Cause and Effect) and PRO-014 (Relief and Flare Design Basis). Acceptance should include explicit review of these against the blanketing requirement.
- **Arctic/sub-arctic detail.** External insulation and heating to prevent freezing imply tracing, controls, and power loads that interact with EPC scope (heater power may overlap with the "Electrical Power: No" interface line). Confirm whether the heater is vendor-supplied skid-internal or EPC-supplied site service before accepting.

## Trade-offs

- **Strict vs. lenient acceptance criteria.** Strict acceptance forces vendor rework but protects downstream construction. Lenient acceptance accelerates schedule but pushes risk into commissioning. Default position: strict on safety-related items (relief, blanketing, structural anchoring, cathodic protection); negotiable on documentation completeness for non-critical items, recorded as deviations.
- **Sequenced vs. batch review.** Sequenced (per discipline group) review allows early issue detection but spreads reviewer attention. Batch review at vendor "issue for acceptance" milestone concentrates effort but compresses risk surfacing.
- **Inventory granularity.** The full Acceptance Inventory (80+ deliverables) may include items the vendor combines or omits with justification. Forcing exact one-to-one alignment can create fictional gaps; allowing aggregation can hide real gaps. Use the mapping table and explicit "covered-by" entries.

## Examples

The source slice does not provide worked examples of vendor acceptance decisions for this package. Examples are TBD until at least one cycle of vendor submittal has occurred.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-1 | Interface workbook version: source SRC1 cites `26020-Packages_Interfaces.3.xlsx`; locally available file is `26020-Packages_Interfaces_4_export.xlsx`. | `_Sources/26020-Package_Requirements.docx` heading 19, "Physical Interface Summary" | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (file listing) | Datasheet "Interfaces Subject to Review"; Specification R-6, R-7 | Treat local `_4_export.xlsx` as the most recent superseding version; verify with package owner. | TBD |
| CT-2 | Heater for freeze prevention: SRC1 lists "External insulation required, heater required" within vendor scope, but also lists "Electrical Power" interface as "No". | SRC1 "Major Included Equipment" | SRC1 "Physical Interface Summary" | Specification R-3, R-6; Guidance "Arctic/sub-arctic detail" | Confirm whether heater is process-fluid (e.g., steam/glycol) and integral to vendor skid, with EPC supplying only an insulated jacket utility tie-in; otherwise the "Electrical Power: No" entry requires re-rating. | TBD |
| CT-3 | API 650 modification points are not enumerated in the source slice. | SRC1 "Major Included Equipment" | (none — absent from source slice) | Specification R-4; Datasheet "Governing tank standard (modified)" | Require vendor MEC-001 to enumerate modification points; do not accept tank deliverables until modifications are recorded. | TBD |
