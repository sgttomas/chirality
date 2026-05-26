# Guidance — DEL-049-05 Vendor Document Turnover Package

## Purpose

This deliverable exists so the project receives a complete, auditable, and accepted set of vendor documentation for the Sales Gas Booster Compressor package (26020-01-PT-12-004) — from engineering through manufacturing, FAT, shipping, installation, commissioning, and final turnover. It is the **documentary backbone** that supports the EPC Integrator's package acceptance (DEL-049-06), supports construction execution (DEL-049-03), and supports operations and maintenance after handover.

Without this package, the physical compressor (DEL-049-04) cannot be safely or legally placed into service: pressure equipment registration, motor energization records, ITP sign-offs, and the Final Vendor Data Book are all required artifacts.

## Principles

1. **Index-first.** Establish PRQ-009 (Vendor Document Index) early and treat it as the single source of truth for what the vendor owes and the status of each item.
2. **Source-fidelity.** Document classes are fixed by the package source specification (26020-Package_Requirements.docx §26020-01-PT-12-004 "Vendor Engineering Deliverables"). Do not silently expand or contract that list; if scope changes, route through change control.
3. **Status discipline.** Every submittal carries an explicit status code (work-from / approved / not-approved / for-info) and a revision. Status codes drive whether downstream consumers (construction, commissioning) may rely on the document.
4. **Provenance preserved.** Transmittals, revision history, and review markups are part of the turnover record; the Final Vendor Data Book is assembled from accepted final-revision documents.
5. **Separation of authoring vs acceptance.** This deliverable produces and routes documents (vendor authoring, EPC review). Final EPC acceptance authority lives in DEL-049-06.
6. **No agent self-certification.** No automated process certifies vendor documentation; humans (EPC Integrator reviewers and vendor responsible engineers) approve.

## Considerations

- **Driver rating mismatch (see Conflict Table).** The DBM and the RFQ basis state two different driver ratings. The vendor document set (motor data sheet, motor starting study, electrical load list, single-line diagrams) must align with the **as-built/as-RFQ'd** rating, not the original DBM number. Reviewers should flag this on first electrical submittal.
- **Jurisdictional pressure equipment registration.** REG-022 must be issued to the applicable provincial/state authority. The accessible sources do not name the jurisdiction; reviewers must confirm before vendor proceeds with registration package preparation.
- **Interface coverage.** The Physical Interface Summary in the source declares which physical interfaces exist (process piping, utility piping, relief/flare/vent, drain/containment, electrical power, area/exterior lighting, EHT, grounding, I&C, fire & gas, maintenance access, structural). The vendor document set must include each interface's discipline document package. Items declared "No" in the source do not require interface documentation.
- **Open items from source.** The source explicitly notes "By others: Shipping compressor package to site, installation on piles, tie-in piping, electrical connections. Mounting platform and stairs." Vendor documentation must clearly delineate where vendor scope ends and EPC/installation contractor scope begins; the Tie-In List (PIP-004) is a key boundary artifact.
- **Spare parts (PRQ-015 SPIR).** Vendor RFQ governs commissioning vs operating spares scope. EPC Integrator should issue spares review well before shipping window.

## Trade-offs

- **Early vs. accurate.** Pushing vendors for early submittals improves construction planning but risks higher revision churn. The status-coding discipline mitigates this when followed.
- **Native files vs PDF only.** Native files (CAD, calculation source) preserve future modification capability; PDF only is faster to assemble but limits owner reuse. The source does not specify a position; assume both are required for engineering documents (ASSUMPTION).
- **Single VDB vs split mechanical/electrical/quality VDBs.** Source enumerates both PRQ-016 (Final Supplier Documentation) and MEC-023 (Mechanical Final Documentation). This implies a structured, multi-volume VDB rather than a single monolithic file (ASSUMPTION pending RFQ confirmation).

## Examples

- A typical Vendor Document Index entry: `MEC-008 / Compressor Data Sheet — Cylinder 1 / Rev B / Status: Approved / Transmittal VTX-024 / 2026-09-12`.
- A typical Conflict Table entry would be raised when vendor-submitted motor data sheet (ELE-020) shows different kW than ELE-002 Load List — see C-01 below.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Driver rating: 6,700 hp / 4,000 V vs 1,000 kW (~1,340 hp) / 4,000 V | 4-25_Deepcut_DBM.md "Sales Gas Booster Compressor Basis" (6,700 hp, 4,000 V) | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Driver" (1,000 kW / 1,340 hp / 4,000 V / 891 rpm) | Specification R-11/R-18; Datasheet Construction (rotating equipment); Procedure verification of ELE-011 Motor Starting Study | RFQ basis (Package_Requirements) governs vendor scope; DBM value retained as design intent for capacity check but not for vendor motor rating | TBD — confirm with Process/Mechanical leads which driver rating is correct as-RFQ'd |
| C-02 | Compressor frame: Ariel KBK/4 vs Ariel KBX/X | 4-25_Deepcut_DBM.md "Sales Gas Booster Compressor Basis" (Ariel KBK/4) | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Major Included Equipment" (Ariel KBX/X) | Datasheet attributes; Specification R-11 | RFQ basis (Package_Requirements) governs vendor scope | TBD — confirm vendor-selected frame model |
| C-03 | Pressure equipment registration jurisdiction not stated in accessible source | 26020-Package_Requirements.docx — REG-022 line item | (no second source) | Specification "Standards"; Procedure step covering REG-022 submission | West Doe site location implies Alberta (ABSA); ASSUMPTION pending confirmation | TBD — confirm jurisdiction with EPC Integrator |
