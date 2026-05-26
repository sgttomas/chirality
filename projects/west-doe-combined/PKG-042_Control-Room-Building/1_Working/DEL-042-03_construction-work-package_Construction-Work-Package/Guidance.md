# Guidance: DEL-042-03 — Construction Work Package (Control Room Building)

## Purpose

DEL-042-03 is the mandatory Gate 5 EPC Integrator anchor deliverable for PKG-042. It exists so the EPC Integrator owns, and can demonstrate, how the vendor-supplied Control Room Building is physically installed, inspected, tied into facility systems, and turned over for operation. (SourceRef: _CONTEXT.md Notes; DELIVERABLE_REGISTER.csv DEL-042-03.)

## Principles

- **Responsibility boundary respected.** The CWP describes Integrator construction integration work. It does not duplicate, second-guess, or substitute for Package Vendor engineering/design/vendor documentation. (SourceRef: PACKAGE_REGISTER.csv PKG-042 ResponsibilityModel.)
- **Interface-complete.** All eleven applicable interface types for PKG-042 must be addressed by installation/tie-in steps. None of the eleven is optional in the source register. (SourceRef: INTERFACE_REGISTER.csv PKG-042.)
- **Workbook authority.** Workbook row 44 is authoritative for package identity, scope, and interface applicability. The CWP should not contradict it. (SourceRef: SCOPE_LEDGER.csv SOW-0043 Notes; PACKAGE_REGISTER.csv.)
- **Turnover orientation.** The end state defined by the deliverable scope is "physically installed, built, inspected, turned over, and tied into the larger facility systems." Construction work that does not contribute to this end state belongs outside the CWP. (SourceRef: DELIVERABLE_REGISTER.csv DEL-042-03.)

## Considerations

- **Control Room Building characteristics (Discipline=Electrical) imply specific construction sensitivities** — orderly grounding/bonding, sequenced energization, clean termination of I&C and communications cabling, and HVAC commissioning ahead of energized electronics. The accessible registers identify these as applicable interface types but do not state design conditions; design-level sensitivities should be drawn from package design sources when available (location TBD).
- **Sequencing relative to other PKG-042 deliverables.** The CWP relies on inputs that originate in DEL-042-01 (scope of work), DEL-042-02 (package datasheet), DEL-042-04 (vendor-engineered equipment package) and DEL-042-05 (vendor document turnover). Construction work cannot mobilize before that information is ready. (SourceRef: SCOPE_LEDGER.csv SOW-0043 deliverable list.)
- **Permit-to-work, HSE, and QC frameworks.** The accessible source registers do not name the governing project-level construction execution standards. These must be confirmed by the project before construction execution detail is hardened. Treat current Specification requirement R-042-03-08 as an ASSUMPTION until confirmed.

## Trade-offs

- **Workface-plan granularity vs maintainability.** Highly granular workface plans give certainty at construction time but become brittle when vendor schedules change. Recommend a layered plan: coarse turnover-oriented sequence at CWP level, with detailed workface packets refreshed against the current vendor and site schedule.
- **Pre-vendor-data drafting vs deferred drafting.** Drafting CWP content before DEL-042-02 / DEL-042-05 are mature risks rework. Drafting only after they are mature risks late mobilization. Recommend drafting the scope/sequence/interface skeleton early (this Pass 1) and marking dimension-, weight-, lift-, and termination-specific items `TBD` until vendor data lands.

## Examples

No worked examples are reproducible from accessible source registers alone. Worked examples (e.g., a sample tie-in packet for "Electrical Power" or "Grounding / Bonding") should be added in a later pass once vendor data and project-standard templates are available. TBD.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-042-03-01 | _CONTEXT.md "Supports Objectives" lists OBJ-002, OBJ-004..OBJ-010 (eight objectives). DELIVERABLE_REGISTER.csv DEL-042-03 lists OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (eight objectives — identical set). | `_CONTEXT.md` Supports Objectives | DELIVERABLE_REGISTER.csv DEL-042-03 row | Specification R-042-03-07; objective trace matrix | No conflict — confirms alignment. Listed only for audit; may be removed when human confirms. | TBD |
