# Procedure: DEL-081-06 — EPC Vendor Package Review and Acceptance

This procedure describes how the EPC Integrator performs and records vendor package review and acceptance for PKG-081 (Flare KO Drum High Pressure 3-25). It produces the four artifacts listed in `_CONTEXT.md` Anticipated Artifacts: Vendor Document Review Log, Package Acceptance Checklist, Test/Inspection Evidence, and Turnover Evidence.

## Prerequisites

- Acceptance basis available at usable maturity:
  - DEL-081-01 — EPC Scope of Work (PKG-081)
  - DEL-081-02 — Package Datasheet (PKG-081)
  - DEL-081-03 — Construction Work Package (PKG-081)
- Vendor inputs available for review:
  - DEL-081-04 — Vendor Engineered Equipment Package
  - DEL-081-05 — Vendor Document Turnover Package
- Decomposition reference: GATE-07 Final Published PROJECT_DECOMP snapshot (`_REFERENCES.md`).
- Reference materials accessible:
  - `PACKAGE_REGISTER.csv` row PKG-081
  - `INTERFACE_REGISTER.csv` rows for PKG-081
  - `SCOPE_LEDGER.csv` SOW-0071..SOW-0074
  - `OBJECTIVE_REGISTER.csv` rows OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010
  - `26020-Package_Requirements.docx` package heading 34 source slice — **TBD** (binary not text-accessible; required for clause-level R-9 acceptance criteria)
- Declared dependency edges: none declared at PREPARATION (`_DEPENDENCIES.md`). Sibling-deliverable dependencies are implied by content and noted under Prerequisites above.

## Steps

1. **Confirm acceptance basis.** Verify DEL-081-01, DEL-081-02, DEL-081-03 are at sufficient maturity for acceptance use. Record any gaps as `TBD`. (Satisfies R-1 prerequisite.)
2. **Resolve scope-conflict open item entry.** Open or update an open-item register entry for SOW-0074 (flare-system equipment in/out boundary). Carry through Steps 3-7; do not close without owner/engineering ruling. (Satisfies R-8.)
3. **Build the Package Acceptance Checklist.** Populate the checklist with sections for: scope, responsibility split, interfaces (one row per category listed in `INTERFACE_REGISTER.csv` for PKG-081), safety/sour-service/regulatory carry-through (OBJ-009), handoff readiness (OBJ-010), and clause-level criteria (R-9; mark `TBD` until source slice is accessible). (Satisfies R-1, R-2, R-3, R-6, R-7, R-9.)
4. **Review the Vendor Document Turnover Package.** Walk the vendor document register from DEL-081-05; for each document record review status, comments, disposition, and close-out reference in the Vendor Document Review Log. Flag missing or incomplete vendor documents as open items. (Satisfies R-4.)
5. **Review the Vendor Engineered Equipment Package.** Walk the vendor scope from DEL-081-04: engineering, design, fabrication, supply. For each major equipment item (V-4100-2, V-4150-2, P-4100-2, P-4150-2, liquid transfer to condensate slop tank, truck-out provision, package interfaces — per SOW-0073) verify alignment with the EPC acceptance basis. Capture inspection releases, FAT/SAT records, NDE, pressure-test results, and any vendor QA/QC records as Test/Inspection Evidence. (Satisfies R-5.)
6. **Per-interface integration review.** For each interface category — Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports — confirm that vendor outputs match the EPC interface definitions from DEL-081-02 and DEL-081-03, and that the responsible discipline reviewer has signed off. Record evidence in the Package Acceptance Checklist (interface section). (Satisfies R-3; supports OBJ-005, OBJ-006, OBJ-007, OBJ-008.)
7. **Safety, sour-service, and regulatory carry-through review.** Trace OBJ-009 items (relief, flare/blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory, codes, standards) through the vendor outputs and acceptance checklist. Record any gaps as open items. Re-check SOW-0074 disposition. (Satisfies R-6, R-8.)
8. **Handoff readiness review.** Trace OBJ-010 items (operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, controlled open-item closure) through the vendor outputs and into Turnover Evidence. Identify mechanical-completion, punch-list, and commissioning records. (Satisfies R-7.)
9. **Open-item closure cycle.** For each open item raised in Steps 2-8, record source, disposition path, ruling required, and target close-out date. Acceptance sign-off requires either closure or an explicit human ruling to carry forward.
10. **Assemble acceptance evidence package.** Combine Vendor Document Review Log, Package Acceptance Checklist, Test/Inspection Evidence, and Turnover Evidence into a single acceptance evidence set with cross-references back to DEL-081-01..05 and to the GATE-07 PROJECT_DECOMP snapshot.
11. **EPC Integrator acceptance ruling.** A human EPC Integrator reviewer issues the acceptance ruling (accept / accept-with-conditions / reject) against the assembled evidence. (Per K-AUTH-1, only humans author binding approval records.)

## Verification

| Check | Method | Evidence |
|---|---|---|
| All four anticipated artifacts produced | File presence; cross-reference to `_CONTEXT.md` Anticipated Artifacts | Vendor Document Review Log; Package Acceptance Checklist; Test/Inspection Evidence; Turnover Evidence |
| All ten declared interface categories reviewed | Inspect Package Acceptance Checklist interface section | One row per `INTERFACE_REGISTER.csv` PKG-081 entry |
| SOW-0074 carried as open item with ruling status | Inspect open-item register | Entry referencing SOW-0074 with current ruling state |
| OBJ-009 carry-through traced | Inspect safety/regulatory section of Package Acceptance Checklist | Trace lines to OBJ-009 items |
| OBJ-010 handoff readiness traced | Inspect Turnover Evidence | Sparing, isolation, winterization, commissioning, turnover records |
| Responsibility split preserved | Inspect responsibility section of Package Acceptance Checklist | No EPC encroachment on vendor design; no vendor encroachment on facility integration |
| Source-grounded clause checks (R-9) | If `26020-Package_Requirements.docx` package heading 34 source slice is available, clause-level checks applied; otherwise items marked `TBD` | TBD until source slice accessible |
| Human acceptance ruling issued | Inspect ruling record | Signed ruling by EPC Integrator reviewer |

## Records

The following records constitute the deliverable evidence set:

- Vendor Document Review Log (R-4 evidence)
- Package Acceptance Checklist (R-1, R-2, R-3, R-6, R-7 evidence)
- Test / Inspection Evidence file set (R-5 evidence)
- Turnover Evidence file set (R-7 evidence; OBJ-010 carry-through)
- Open-item register entries (R-8 evidence; SOW-0074 and any others raised)
- EPC Integrator acceptance ruling record (acceptance authority; K-AUTH-1 compliant)

All records shall cite their basis: DEL-081-01 / DEL-081-02 / DEL-081-03 (acceptance basis), DEL-081-04 / DEL-081-05 (vendor inputs), `26020-Package_Requirements.docx` package heading 34 (source — location TBD), and the GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
