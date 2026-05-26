# Guidance — DEL-096-06 EPC Vendor Package Review and Acceptance (PKG-096 Tanks, Sour Condendate (API 650))

## Purpose

The EPC Vendor Package Review and Acceptance dossier records the EPC Integrator's evaluation of the Package Vendor's submittals for PKG-096 (Tanks, Sour Condendate (API 650)) against the EPC-authored acceptance basis (SOW, Package Datasheet, Construction Work Package). It is the evidence layer that closes the loop between what the EPC asked for (SOW + datasheet + CWP) and what the vendor delivered (engineered package + turnover package), and it documents handoff readiness for construction and operations.

Source: `_CONTEXT.md` Scope; deliverable Type "EPC Vendor Package Acceptance".

## Principles

- **Acceptance is evidence, not certification.** This deliverable produces a defensible review record. Binding approval (reliance) is recorded only by a human per K-AUTH-1.
- **Source-grounded comparison.** Every acceptance check ties back to a source attribute (package heading, SOW, Package Datasheet, CWP) — not to convention. Where the source is silent, the open item is recorded, not silently passed.
- **Boundary clarity.** "By Others" items in the package source (foundations, mounting, electrical/instrumentation, platforms, staircase) are out of vendor scope and must be tracked elsewhere; review must confirm correct boundary handling, not absorb the work into vendor acceptance.
- **Interface integrity.** The package heading's Physical Interface Summary is the authoritative applicability matrix for this package — applicable interfaces must be evidenced; non-applicable interfaces must be confirmed absent from vendor scope.
- **Single point of acceptance disposition.** One overall disposition (with open-items list) closes the dossier; per-item statuses feed into it.

## Considerations

- **"Modified API 650" qualifier.** The package heading invokes "Modified API 650" without enumerating modifications. The reviewer must locate the modifications (likely in the RFQ `Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` — **location TBD**, not locally accessible) before accepting code-conformance claims. Until then, code-conformance items remain open.
- **NACE document specificity.** The package heading says "NACE compliant" without naming the specific NACE document (e.g., MR0175). Reviewer should identify the applicable NACE document from the SOW / Package Datasheet (DEL-096-01 / DEL-096-02) or RFQ and check the vendor's claim against it.
- **Design pressure "32 oz test pressure".** The phrasing in the source merges design and test pressure. The reviewer should clarify whether 32 oz refers to the tank design pressure or the test pressure (and what vacuum design value applies — analogous packages in the same source list `32 oz / 1.0 oz vacuum` for similar tanks; this is **ASSUMPTION** for PKG-096 — confirm from datasheet).
- **Item No. 2 conditions.** The package source narrative for "Tanks, Sour Condensate" centers on Item No. 1 (two 3800 bbl sour inlet condensate tanks); the source phrase "Design Flow: 94,940 kg/h / 3187 Am3/d for Item No. 2" and "Temperature: 5 °C (min) & 40 °C (max) for Item No. 2" implies an Item No. 2 within the same package. Reviewer should confirm whether Item No. 2 is in PKG-096 or split into another package, and adjust acceptance scope accordingly. Marked **ASSUMPTION** pending confirmation.
- **VRU / blanket gas interface.** Even though "Utility Piping" is "No" in the interface matrix, the vendor package includes VRU header connection and a blanket gas system per API 2000 (Process Piping / Relief-Vent interfaces handle these). Reviewer should confirm interface routing matches the matrix.
- **Cathodic Protection (Yes) + "Non-insulated".** CP is "Yes" in the interface matrix; the reviewer should confirm vendor's CP provisions (external coating system, isolation, test station provisions) and reconcile with the EPC-side CP scope.
- **Document control conventions.** Status code-sets for vendor-document review and for acceptance disposition are not declared in the package source; the dossier should reference the project document control procedure (location TBD) rather than inventing codes.

## Trade-offs

- **Depth of review vs. schedule pressure.** Deeper line-by-line review on calculations and drawings improves confidence but increases turnaround. Recommendation: prioritize depth on safety-critical items (PVRV/EPRV sizing, blanket gas, NACE compliance, fill-protection logic) and on items that drive interfaces with other EPC scopes.
- **Acceptance with open items vs. rejection.** Accepting with open items can preserve schedule but obligates clear tracking and closure. Recommendation: only accept with open items when open items do not block downstream construction or commissioning steps.
- **Source-only vs. analog-package inference.** Where the PKG-096 source is silent, sibling packages in the same workbook may suggest values. Treat any analog-derived inference as **ASSUMPTION**, not as accepted vendor data.

## Examples

- A vendor-supplied PVRV/EPRV calculation matches API 2000 sizing and the package heading's stated relief provisions → checklist item REQ-4 (relief) accepted; cross-checked against PRO-015 (PSV / Pressure Relief Sizing Calculations).
- A vendor MTR is missing for a sour-service plate heat → open item logged under REQ-7; acceptance status "Accepted with Open Items"; closure tracked via vendor re-submittal.
- A vendor proposes to include foundation anchor-bolt setting drawings inside vendor scope → boundary check (REQ-9): foundations are "By Others" per source; vendor's anchor-bolt setting drawings (MEC-017 "Equipment Installation / Setting Drawings") are accepted as interface information, but foundation design remains with EPC discipline package.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | "Design pressure" stated only as "32 oz test pressure" — ambiguous whether 32 oz is design or test pressure, and vacuum design value not stated for PKG-096 (analog packages list 1.0 oz vacuum) | `26020-Package_Requirements.docx` heading "Tanks, Sour Condensate" — Scope Notes / Open Items | Analog tank packages in same workbook (e.g., Produced Water tanks, Spent Caustic tank) listing "Design pressure: 32 oz, 1.0 oz vacuum" | Datasheet Conditions; Specification REQ-4; Guidance Considerations | PROPOSAL: confirm 32 oz as design pressure with 1.0 oz vacuum by analog, but verify against the PKG-096 datasheet (DEL-096-02) and the RFQ before acceptance | TBD |
| C-2 | "Item No. 2" alluded to (Design Flow 94,940 kg/h / 3187 Am3/d; Temp 5 / 40 °C) but only Item No. 1 (two 3800 bbl Sour Inlet Condensate tanks) is named under Basic Scope / Major Included Equipment for PKG-096 | `26020-Package_Requirements.docx` heading "Tanks, Sour Condensate" — Scope Notes / Open Items (mentions Item No. 2) | Same heading — Basic Scope (names only Item No. 1) | Datasheet Conditions; Specification REQ-4; Guidance Considerations | PROPOSAL: confirm with EPC whether Item No. 2 is in PKG-096 scope or migrated to a different package; treat Item No. 2 conditions as out-of-scope for PKG-096 acceptance unless confirmed | TBD |
| C-3 | "Modified API 650" — modifications not enumerated in package heading | `26020-Package_Requirements.docx` heading "Tanks, Sour Condensate" — Major Included Equipment | (no second source locally accessible) | Specification Standards; REQ-4 (code); Guidance Considerations | PROPOSAL: enumerate modifications from RFQ `26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` (location TBD) and from PKG-096 Package Datasheet (DEL-096-02) before accepting code-conformance | TBD |
| C-4 | "NACE compliant" — specific NACE document not named | `26020-Package_Requirements.docx` heading "Tanks, Sour Condensate" — Major Included Equipment | (no second source locally accessible) | Specification REQ-4; Standards | PROPOSAL: confirm applicable NACE document (likely MR0175, **ASSUMPTION**) from EPC SOW (DEL-096-01) and Package Datasheet (DEL-096-02) | TBD |
| C-5 | Interface matrix: "Utility Piping = No" but vendor scope includes blanket gas system per API 2000 (a utility) and VRU header connection | `26020-Package_Requirements.docx` heading — Physical Interface Summary (Utility Piping: No) | Same heading — Major Included Equipment (blanket gas system; VRU header connection) | Specification REQ-5; Guidance Considerations | PROPOSAL: blanket gas / VRU are routed under "Process Piping" (Yes) and "Relief / Flare / Vent" (Yes) rather than Utility Piping; confirm interface routing during review | TBD |
