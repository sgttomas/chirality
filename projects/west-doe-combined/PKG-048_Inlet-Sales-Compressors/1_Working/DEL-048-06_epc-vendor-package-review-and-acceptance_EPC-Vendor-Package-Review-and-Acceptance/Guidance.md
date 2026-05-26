# Guidance — DEL-048-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's review-and-acceptance evidence for the Inlet/Sales Compressor package (PKG-048). Per SOW-0115, the Package Vendor owns engineering, design, and equipment; the EPC Integrator owns facility integration. This deliverable closes the loop between vendor outputs (DEL-048-04 engineered equipment package, DEL-048-05 turnover package) and EPC integration acceptance, generating the durable evidence trail used downstream for commissioning and operations handoff. Source: `_CONTEXT.md`; SCOPE_LEDGER SOW-0115.

## Principles

- **EPC review is integration-focused.** The EPC Integrator does not re-do vendor design; it verifies that the vendor's delivered package conforms to the EPC SOW, Datasheet, and Construction Work Package and is integrable with the broader facility. Source: SOW-0115.
- **Evidence over assertion.** Acceptance is recorded via review logs, checklists, and test/inspection records — not by narrative attestation. Source: ARTIFACT_REGISTER ART-F8E220700B/ART-7862D9EB63/ART-00AE5AE3CA.
- **Scope-split discipline.** "By-others" items in SOW-0118 must be excluded from vendor acceptance and tracked under their owning deliverables. Source: SOW-0118.
- **Traceability to objectives.** All review findings should trace to one of OBJ-001, OBJ-003..OBJ-010 to support project closure. Source: OBJECTIVE_DELIVERABLE_MAP.

## Considerations

- **Source binary limitations.** The authoritative `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` were not directly readable during initial drafting; the GATE-07 SCOPE_LEDGER extractions were the accessible source surrogate. Reviewers SHOULD open the original .docx to confirm clause-level details for any acceptance decision relying on specific values.
- **Internal value inconsistency in source slices.** Driver rated power values disagree between SOW-0117 and SOW-0118 (see Conflict Table CFLT-1). The 26,100 kW connected load supports the 5,220 kW / 7,000 HP interpretation. Reviewers SHOULD obtain a human ruling before issuing nameplate acceptance.
- **NEMA MG 1 reference is rating-context.** The standard reference appears tied to motor enclosure/rating; treat as a baseline reference rather than a stand-alone compliance gate unless the SOW or Datasheet explicitly invokes a clause.
- **Preferred vs. mandatory.** The SOW language "preferred WEG motor" and "KBZ Frame" should be treated as preferences (ASSUMPTION) unless the Package Datasheet (DEL-048-02) elevates these to acceptance criteria.

## Trade-offs

- **Depth of vendor design re-verification vs. schedule.** Deep re-verification of vendor calculations (pulsation, vibration, performance) duplicates vendor scope and slows acceptance. Lean toward sampling and exception-driven deep dives unless red flags appear in the review log.
- **Acceptance vs. punchlist.** Some non-conforming items may be acceptable with a tracked punchlist if they do not block integration or commissioning safety. Reviewers SHOULD distinguish acceptance-blockers from punch items in the checklist.

## Examples

- Vendor data sheet specifies a motor enclosure of WPII; spec allows TEFC or WPII → conformant; record in review log with cross-reference to SOW-0117.
- Vendor states air cooler with split frames per service; spec calls for one common frame → non-conformant; raise as acceptance-blocker pending ruling.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFLT-1 | Driver rated motor power per unit: 5,000 kW / 6,700 HP vs. 5,220 kW / 7,000 HP | GATE-07 SCOPE_LEDGER SOW-0117 (26020-Package_Requirements.docx, heading 3, Major Included Equipment) | GATE-07 SCOPE_LEDGER SOW-0118 (26020-Package_Requirements.docx, heading 3, Scope Notes) | Datasheet "Driver" row; Specification REQ-8 and REQ-9 | PROPOSAL: prefer SOW-0118 value (5,220 kW / 7,000 HP) because the same row's 26,100 kW total connected load is internally consistent (5 × 5,220 = 26,100). | TBD |
| CFLT-2 | "Preferred WEG motor / KBZ Frame" — preference vs. acceptance criterion | SCOPE_LEDGER SOW-0118 | DEL-048-02 Package Datasheet (not read; location TBD) | Specification REQ-7 | PROPOSAL: treat as preference unless DEL-048-02 elevates; mark non-binding. | TBD |
