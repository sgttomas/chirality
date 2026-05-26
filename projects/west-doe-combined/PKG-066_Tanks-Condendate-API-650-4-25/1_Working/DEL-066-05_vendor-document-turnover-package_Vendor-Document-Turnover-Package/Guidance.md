# Guidance — DEL-066-05 Vendor Document Turnover Package

## Purpose

This deliverable exists so the project receives a complete, auditable, and accepted set of vendor documentation for the 4-25 condensate storage tank package (26020-01-PT-19-004; tanks TK-9110-1..TK-9150-1) — from engineering through fabrication, hydrotest, site erection, commissioning, and final turnover. It is the **documentary backbone** that supports the EPC Integrator's package acceptance (DEL-066-06), supports construction execution (DEL-066-03), and supports operations and maintenance after handover.

Without this package, the physical tanks (DEL-066-04) cannot be safely or legally placed into service: API 650 erection records, hydrotest reports, PVRV/EPRV settings, blanket-gas connection records, grounding/cathodic-protection records, and the Final Vendor Data Book are all required artifacts.

## Principles

1. **Index-first.** Establish PRQ-009 (Vendor Document Index) early and treat it as the single source of truth for what the vendor owes and the status of each item.
2. **Source-fidelity.** Document classes are fixed by the package source specification (26020-Package_Requirements.docx §26020-01-PT-19-004 "Vendor Engineering Deliverables"). Do not silently expand or contract that list; if scope changes, route through change control. The source explicitly states the 4-25 scope is an **analog** of the 3-25 condensate tank package — analog-vs-actual differences must be tracked.
3. **Status discipline.** Every submittal carries an explicit status code (work-from / approved / not-approved / for-info) and a revision. Status codes drive whether downstream consumers (construction, commissioning) may rely on the document.
4. **Provenance preserved.** Transmittals, revision history, and review markups are part of the turnover record; the Final Vendor Data Book is assembled from accepted final-revision documents.
5. **Separation of authoring vs acceptance.** This deliverable produces and routes documents (vendor authoring, EPC review). Final EPC acceptance authority lives in DEL-066-06.
6. **No agent self-certification.** No automated process certifies vendor documentation; humans (EPC Integrator reviewers and vendor responsible engineers) approve.

## Considerations

- **Analog basis vs as-RFQ'd basis (see Conflict Table).** The 4-25 package source explicitly uses the 3-25 condensate tank package as the nearest analog and lists multiple open items (tank count, tags, capacity, inlet/outlet sources, mercaptan treating bypass, VRU/blanket gas, design conditions). The DBM indicates 5 condensate tanks at 4-25 (TK-9110-1..TK-9150-1), while the 3-25 analog uses 4 x 3,800 bbl tanks. Vendor documentation must be issued against the as-RFQ'd 4-25 basis (when the RFQ is issued) — not silently against the 3-25 analog.
- **Tank count and capacity confirmation.** The DBM line 2625 records 5 condensate tanks at 4-25; the local-storage narrative (line 1633) describes 4 x 3,800 bbl. Vendor must align tank count, capacity, and dimensions before issuing MEC-011 Storage Tank Data Sheets.
- **Tank venting philosophy.** The DBM (line 1663) states condensate tanks connect to the VRU suction header and require blanket gas to prevent vacuum in winter, with API 2000 governing blanket-gas rates. PVRV/EPRV sizing, off-spec overhead venting, tank isolation philosophy with possible sour vapours, vacuum-truck rate, and thermal-expansion handling are explicitly flagged as detailed-engineering review items. Vendor documents (PRO-014..PRO-018; INS-016/017) must show these calculations.
- **Inlet/outlet cascade arrangement.** The DBM (line 1661) describes a specific inlet/outlet cascade arrangement (inlet tanks receive stabilizer bottoms; internal pipe stand cascades to outlet tanks; common truck-out connection). MEC-011, PRO-008 P&IDs, and PIP-006 GA must reflect this arrangement.
- **Jurisdictional registration.** API 650 atmospheric tanks may or may not fall under provincial pressure-equipment registration scope. Reviewers should confirm jurisdictional treatment before vendor proceeds.
- **Interface coverage.** The Physical Interface Summary in the source declares: Process Piping (Yes); Utility Piping (No); Relief/Flare/Vent (Yes); Drain/Containment (Yes); Electrical Power (No); Area/Exterior Lighting (Yes); EHT (No); Grounding/Bonding (Yes); Cathodic Protection (Yes); I&C/Control Cabling (Yes); Communications/Network (No); HVAC (No); F&G (No); Maintenance Access (No); Grading/Drainage/Spill Containment (Yes); Structural/Foundations/Supports (Yes); Product Loading (No); Pipeline/Pigging (No). Items declared "No" do not require interface documentation.
- **Interface Coordination Notes.** The source explicitly marks "Interface Coordination Notes — TBD." Vendor and EPC Integrator must populate these as engineering progresses; the absence today is a known gap.

## Trade-offs

- **Early vs accurate.** Pushing vendors for early submittals improves construction planning but risks higher revision churn — especially acute here because the 4-25 scope is currently analog-based. The status-coding discipline mitigates this when followed.
- **Native files vs PDF only.** Native files (CAD, calculation source) preserve future modification capability; PDF only is faster to assemble but limits owner reuse. The source does not specify a position; assume both are required for engineering documents (ASSUMPTION).
- **Single VDB vs split mechanical/quality VDBs.** Source enumerates both PRQ-016 (Final Supplier Documentation) and MEC-023 (Mechanical Final Documentation). This implies a structured, multi-volume VDB rather than a single monolithic file (ASSUMPTION pending RFQ confirmation).

## Examples

- A typical Vendor Document Index entry: `MEC-011 / Storage Tank Data Sheet — TK-9120-1 / Rev B / Status: Approved / Transmittal VTX-014 / 2026-09-12`.
- A typical Conflict Table entry would be raised when vendor-submitted MEC-011 shows a different tank count or capacity than the DBM roster — see C-01 / C-02 below.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Tank count: 5 condensate tanks at 4-25 vs 4 x 3,800 bbl analog at 3-25 | 4-25_Deepcut_DBM.md line 2625 "5 — TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1" | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Major Included Equipment" ("3-25 analog uses four 3,800 bbl tanks") and DBM line 1633 ("four 3,800 bbl condensate product storage tanks") | Datasheet Identification/Construction; Specification R-11 | DBM tank roster (5 tanks, TK-9110-1..TK-9150-1) governs 4-25 vendor scope; analog count retained as design-intent context only | TBD — confirm final 4-25 tank count with Process/Mechanical leads |
| C-02 | Tank capacity / dimensions: 4-25 capacity not explicitly stated; 3-25 analog uses 3,800 bbl | 4-25_Deepcut_DBM.md (no explicit 4-25 capacity figure in accessible slice) | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Scope Notes" ("confirm…capacity, inlet/outlet sources…design conditions match the 3-25 3,800 bbl tank basis") | Datasheet Conditions; Specification R-11 | 4-25 capacity will be set by RFQ; assume 3,800 bbl as analog baseline until vendor MEC-011 is issued | TBD — confirm capacity at RFQ issue |
| C-03 | Jurisdictional registration for API 650 modified condensate tanks not stated in accessible source | 26020-Package_Requirements.docx §26020-01-PT-19-004 (no jurisdictional registration entry) | (no second source) | Specification Standards; Procedure step for any jurisdictional submission | West Doe site location implies Alberta; jurisdictional pressure scope of atmospheric API 650 tanks varies; ASSUMPTION pending confirmation | TBD — confirm jurisdictional applicability with EPC Integrator |
| C-04 | Electrical power: source declares "Electrical Power = No" for vendor scope, but tank instrumentation will require power | 26020-Package_Requirements.docx §26020-01-PT-19-004 Physical Interface Summary (Electrical Power = No) | Implicit need from I&C/Control Cabling = Yes (INS scope) and CTL-026 Package Vendor Interface Specification | Specification R-15; ELE-* document submittals | EPC/site supplies bulk electrical; vendor scope is limited to instrument loop power per CTL-026 interface spec | TBD — confirm power-supply interface ownership in Tie-In List (PIP-004) and CTL-026 |
