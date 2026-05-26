# Guidance — DEL-070-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package is the single Package Vendor production unit that consolidates the vendor document register, the as-issued vendor document submittals, the source-required vendor documentation set, and the turnover records for PKG-070 Mole Sieve Drier Unit (NGL). It exists so that EPC Integrator review, regulatory closure, and operations handoff have one auditable inventory and one closure surface for vendor-furnished documentation. Source: DELIVERABLE_REGISTER.csv row 412; _CONTEXT.md.

## Principles

- One register, one closure surface. The vendor document register is the authoritative inventory. Source rows from 26020-Package_Requirements.docx remain artifacts/evidence, not separate deliverables. Source: DELIVERABLE_REGISTER.csv row 412 Notes.
- Source-anchored scope. The source vendor document table (Mole Sieve "Vendor Engineering Deliverables") sets the floor for register contents; vendor additions are permitted, omissions are not. Source: 26020-Package_Requirements.docx §Mole Sieve.
- Document control before content review. DOC-008 governs revision and submittal mechanics; technical review attaches to controlled revisions only.
- Turnover is acceptance, not transmittal. Final closures (PRQ-016, MEC-023, QLT-021) require accepted-state evidence per row, not just delivery receipts.
- Separate vendor execution from EPC acceptance. Vendor authors documents; EPC reviews and accepts them through DEL-070-06. This deliverable does not absorb EPC acceptance evidence.

## Considerations

- Discipline grouping in the source vendor document table (core vendor / core package engineering / static pressure / heat transfer / process / relief-flare / piping / drainage / electrical / I&C / F&G / structural) is meaningful: it maps directly to discipline reviewers on the EPC side.
- Interface-bearing vendor documents (CTL-026, PIP-004, INS-018, ELE-028) need coordinated review with facility-level interface owners; their turnover state can lag if interfaces remain unresolved.
- Regulatory interfaces (REG-022 Pressure Equipment Registration Package) drive jurisdictional close-out timing; sequence turnover to avoid late jurisdictional findings.
- The package source explicitly states "Interface Coordination Notes: TBD." Treat published interface notes as authoritative when they appear; do not invent interim coordination conventions here.
- Heated/enclosed-building scope drives an additional documentation subset (enclosure structural, electrical, HVAC). Source: 26020-Package_Requirements.docx §Mole Sieve / Major Included Equipment.

## Trade-offs

- Wide register vs. narrow register. The source table is intentionally broad; trimming risks regulatory or operability gaps, but a fully populated register increases EPC review workload. Resolve by enforcing R-8 (preserve discipline grouping; all source rows present) rather than negotiating omissions.
- Early-issued documents vs. final-as-built closures. Some rows (e.g., PRO-028 Process As-Built PFD/P&ID, PIP-028 Piping As-Built) are inherently late; turnover cannot close until they revise to as-built. Plan turnover phasing rather than back-pressuring early issues.
- Single Vendor Data Book vs. parallel closures. PRQ-016, MEC-023, and QLT-021 overlap. Treat them as complementary closures (commercial / mechanical / manufacturing) rather than alternatives.

## Examples

- Adding a vendor-internal calculation report not listed in the source table: permitted (vendor additions). Add to register with a clear "vendor-added" provenance tag.
- Removing INS-016 Control Valve Data Sheets because the package has no control valves: not permitted. Mark "N/A — no control valves in package" with engineering justification; keep the row to preserve the source-to-register mapping. ASSUMPTION: register-completeness convention; not stated in accessible source.
- Treating an individual vendor data sheet as its own deliverable: not permitted. Source: DELIVERABLE_REGISTER.csv row 412 Notes.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Interface coordination notes for this package are stated as "TBD." in source. | 26020-Package_Requirements.docx §Mole Sieve / Interface Coordination Notes | DELIVERABLE_REGISTER.csv row 412 (implies interface review scope) | Specification R-14, R-15; Guidance Considerations | Defer to future published interface notes; do not invent. | TBD |
| C-2 | Register attribute set (revision/status/dates/EPC review/turnover state in R-9) is not explicitly enumerated by accessible source. | _REFERENCES.md (no source slice on register attributes) | DELIVERABLE_REGISTER.csv row 412 (implies submittal/turnover tracking) | Specification R-9 | Adopt as ASSUMPTION until human/source confirms. | TBD |
| C-3 | Whether "N/A — not applicable" rows preserve register-source mapping (Example 2) is unstated by accessible source. | 26020-Package_Requirements.docx (table-only, no convention) | _CONTEXT.md (scope: source-required documentation) | Guidance Examples; Specification R-8 | Preserve mapping with explicit N/A justification. | TBD |
