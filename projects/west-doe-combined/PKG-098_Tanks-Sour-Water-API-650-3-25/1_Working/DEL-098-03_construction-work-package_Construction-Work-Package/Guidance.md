# Guidance — DEL-098-03 Construction Work Package

> Pass: P1_P2 (initial draft + cross-reference). Directional guidance for the EPC Integrator producing this CWP.

## Purpose

The Construction Work Package (CWP) translates Package Vendor engineering for PKG-098 (Tanks, Sour Water, API 650, 3-25 — `26020-03-PT-19-007`) into field-executable work covering foundations, tank setting, platforms/staircases, electrical/instrumentation, coatings, insulation/EHT, hydrotest, and all package-to-facility interfaces. It anchors the EPC Integrator's accountability for physical installation, inspection, turnover, and tie-in into the larger facility systems. Source: `_CONTEXT.md` Scope; `PACKAGE_REGISTER.csv` row PKG-098 (EPC Integrator integration scope).

## Principles

P-01. **Vendor drawings govern installation; CWP does not redesign.** Tank design, internals, and coating selection are owned by the Package Vendor (modified API 650, Devchem 253, Kennilworth float skim). CWP executes to those drawings and records evidence. Source: `26020-Package_Requirements.docx` heading 50.

P-02. **EPC scope is the "By others" list plus interfaces.** The vendor's Scope Notes explicitly assign foundations, site mounting, E&I, and platforms/staircases to "others" — those are the EPC Integrator's primary execution domains, in addition to the Yes-marked interface scopes. Source: `26020-Package_Requirements.docx` heading 50, Scope Notes; Physical Interface Summary.

P-03. **Cold-weather construction is normative, not optional.** -40 °C minimum ambient governs exposed equipment, winterization sequencing, EHT installation order, and concrete pour planning. Source: DBM §Site Basis (line 145).

P-04. **Sour service drives QA stringency.** Sour produced-water service implies attention to coating integrity (Devchem 253 DFT and holiday testing), weld NDE, drain-tie-in materials, and PSV handling. Source: DBM §Produced-Water Storage; §Pressure vessels (line 611) — sour-service requirements cited as a vessel design driver and carry into field QA. ASSUMPTION extending to tank field QA.

P-05. **Interface clarity is the highest-leverage CWP work product.** Nine interface categories are marked Yes on this package. Tie-in walkdowns, line-list reconciliation, and turnover-boundary definition should be settled before bulk piping fabrication. Source: `26020-Package_Requirements.docx` heading 50 Physical Interface Summary.

## Considerations

C-01. **Tank package boundary versus PKG-098 deliverable boundary.** The vendor section under heading 50 lists Item 1 (three TK-90x0-2 sour produced water tanks), Item 2 (two TK-90x0-2 sour inlet PW tanks), and Item 3 (two TK-90x0-1 PW tanks). The `_CONTEXT.md` scope statement names the three Item-1 tanks. Whether Items 2 and 3 are inside DEL-098-03 CWP scope or covered by adjacent packages (PKG-096 Sour Condensate; other PW packages) is **TBD** — see Conflict Table.

C-02. **Tank SG discrepancy (1.25 vs 1.18).** Tank design SG basis is 1.25 TBC; pump fluid SG basis is 1.18; DBM flags discrepancy to be closed during detailed design. Construction proceeds to whichever value the vendor's final stamped drawings specify. Source: DBM §Produced-Water Storage. The CWP should flag if vendor-stamped drawings still carry an unresolved value.

C-03. **Hydrotest medium for tanks in sour service at a cold site.** API 650 hydrotest typically uses water; freezing-risk handling and disposal of contaminated test water need a written plan. Source/values TBD; project HSE plan governs.

C-04. **Vendor deliverable list is the CWP's input manifest.** Each `MEC-`, `STR-`, `PIP-`, `INS-`, `ELE-`, `PLN-`, `CTL-`, `CIV-`, `PRO-`, `QLT-`, `PRQ-`, `DOC-` deliverable enumerated under heading 50 is a CWP input. CWP must register receipt, revision tracking, and as-built loop-back for the relevant ones (As-Built series: `PIP-028`, `INS-029`).

C-05. **Drain rating consistency.** Drain header minimum rating is 300# ANSI per DBM §Drain systems (line 493). PKG-098 drain tie-in must respect this. CWP shall verify field-fabricated drain tie-ins to that rating where applicable.

C-06. **Turnover binder consolidation.** The CWP's turnover checklist should consolidate vendor's Vendor Data Book (`PRQ-016` / `MEC-023`), Manufacturing Record Book (`QLT-021`), Inspection Release Certificate (`QLT-020`), MTRs (`QLT-013`), and ITP sign-offs (`QLT-003`) with field execution records into one mechanical-completion package.

## Trade-offs

T-01. **Pre-erection coating touch-up versus post-erection.** Vendor applies Devchem 253 prior to shipment. Field touch-up after erection covers transport/handling damage but adds critical-path schedule risk if extensive. CWP should plan for inspection at receipt to recover early.

T-02. **EHT installation before or after insulation.** Standard practice is EHT first, then insulation; sequencing affects test access. Source-supported value TBD.

T-03. **Bulk vs work-pack issue strategy.** Multi-tank construction can be packaged as one CWP (efficiency) or per-tank (granular control). DEL-098-03 deliverable name suggests one CWP, but per-tank work packs may be defined inside it. ASSUMPTION.

## Examples

- **Foundation work pack** (example structure): site grading and surveying → piling/footing per `STR-005`/`STR-006` → anchor-bolt embedment per `STR-013` → as-built survey → release for tank erection. Source: vendor STR deliverable categories under heading 50.
- **Tank erection work pack**: shell-plate receipt and storage → ring-wall handover → bottom-plate placement → shell erection per `MEC-017` → roof installation → internals (Kennilworth skim) per vendor drawings → coating touch-up → punchlist closure. ASSUMPTION on sequencing detail; vendor `MEC-017` governs.
- **Tie-in walkdown example**: jointly with vendor / commissioning, verify each row in `PIP-004` Tie-In List against P&ID `PRO-008` and field condition before line-pack issue. Source: vendor deliverable list categories.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | PKG-098 scope: does DEL-098-03 CWP cover only Item-1 tanks (TK-9030/9040/9050-2) or also Item-2 (TK-9010/9020-2) and Item-3 (TK-9010/9020-1)? | `_CONTEXT.md` Scope (names only the three Item-1 tanks) | `26020-Package_Requirements.docx` heading 50, Major Included Equipment (lists Items 1–3 under same RFQ tag `26020-03-PT-19-007`) | Datasheet Attributes; Specification R-01; Procedure scope of work packs | PROPOSAL: scope CWP to all Items 1–3 under tag `26020-03-PT-19-007` because they share a single vendor RFQ; explicitly call out tank IDs. | TBD |
| CT-02 | Tank SG basis discrepancy: 1.25 (tank design TBC) vs 1.18 (pump fluid basis). | DBM `3-25_Comp_and_Liquids_DBM.md` §Produced-Water Storage (1.25 TBC) | DBM same section (1.18 pump basis) | Datasheet Conditions; Specification R-06 (hydrotest planning) | PROPOSAL: CWP defers to vendor stamped drawings; flag if unresolved at IFC. | TBD |
| CT-03 | Heading 50 lists `Maintenance Access = No` and `Building HVAC = No` in the interface table; the package-register PACKAGE_REGISTER.csv `InterfaceTypes` field for PKG-098 lists Maintenance Access? (verify) | `26020-Package_Requirements.docx` heading 50, Physical Interface Summary (Maintenance Access = No) | `PACKAGE_REGISTER.csv` PKG-098 InterfaceTypes list (does NOT include Maintenance Access — consistent) | Specification §Scope/Covered interface list | None — confirmed consistent on re-read; entry retained for traceability. | n/a (no conflict) |
| CT-04 | Authoritative governing standard for hydrotest (API 650 §) is referenced indirectly only; clause-level requirements not locally accessible. | `26020-Package_Requirements.docx` heading 50 Major Included Equipment ("modified API 650") | API 650 text — not locally accessible | Specification R-03, R-06; Procedure hydrotest step | PROPOSAL: cite "vendor procedure governs; API 650 §-level — location TBD." | TBD |
| CT-05 | Underlying RFQ source `26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` is cited by PACKAGE_REGISTER but not directly read; could contain CWP-relevant constraints (delivery split, FAT scope, freight basis). | `PACKAGE_REGISTER.csv` PKG-098 Source field | Local filesystem search of `_Sources/` returns docx itself only (not separately resolved) | All four documents | PROPOSAL: open RFQ docx in a follow-up enrichment pass; treat absent slices as TBD. | TBD |
