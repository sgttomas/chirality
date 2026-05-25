# Procedure: DEL-036-05_vendor-document-turnover-package

## Purpose

Procedure for producing the Vendor Document Turnover Package for `PKG-036` (6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)): the vendor document register, vendor document submittals, source-derived vendor document artifacts where available, and turnover records, with EPC Integrator review interfaces. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-036-05`.)

## Prerequisites

- Declared upstream dependencies: none in `_DEPENDENCIES.md` (declared posture). Substantive context dependencies (advisory, not declared):
  - `DEL-036-02_package-datasheet` — EPC package datasheet (technical handoff) is available to bound vendor scope. (Source: `DELIVERABLE_REGISTER.csv` row `DEL-036-02`.)
  - `DEL-036-04_vendor-engineered-equipment-package` — the vendor-engineered physical equipment package that this documentation describes. (Source: `DELIVERABLE_REGISTER.csv` row `DEL-036-04`.)
- Required references:
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
  - Gate 7 registers under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical-systems and electrical-buildings sections; lines 2811-2813, 2935, 2955, 2973, 2985).
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (package deliverables paragraph, line 617).
  - `_Sources/26020-Package_Requirements.docx` (no PKG-036 match found; recheck on each pass).
- Confirmed authorship model: Package Vendor authors documents; EPC Integrator reviews. (Source: `DELIVERABLE_REGISTER.csv` row `DEL-036-05`.)

## Steps

1. **Confirm identity and scope.** Read `_CONTEXT.md`, `PACKAGE_REGISTER.csv` row `PKG-036`, and `DELIVERABLE_REGISTER.csv` row `DEL-036-05`. Confirm package name, WBS, CoA number, discipline, and responsibility model. Surface the 830-1 building-name discrepancy (Conflict Table HRR-036-05-002) for human ruling.
2. **Resolve source basis.** Re-search `_Sources/26020-Package_Requirements.docx` and other Bid Docs / RFQ material for any PKG-036-specific vendor document requirements. If a match is found, supersede the artifact register's `ART-462B18445D` "gap" note and ground subsequent steps in the new source slice. If no match is found, retain the gap as TBD.
3. **Construct the vendor document register.**
   - List all documents the Package Vendor will submit for the package.
   - Use a column structure that captures, at minimum: document number, title, type, revision, status, planned submittal date, related interface(s), turnover-required flag, EPC review pointer.
   - Mark each row with a source basis (specific source slice, general DBM expectation, or TBD).
4. **Map interface coverage.** For each of the twelve PKG-036 interfaces (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports), identify the register rows that carry the package-side data for that interface; surface gaps as TBD on the register.
5. **Embed source-grounded MV-electrical facts.** Confirm submittal scope reflects the 6.9 kV / 3 phase / 3 wire / 60 Hz / low-resistance-grounded basis and the 100 A / 10 s neutral grounding resistor per 6.9 kV transformer; for any MCC in package scope, confirm the Ethernet/PLC interface description. (Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2935, 2955, 2985.)
6. **Stage vendor document submittals.** As vendor documents arrive, file them under this deliverable folder with a status field referencing the register; do not modify the register row authority — record submittal events as a submittal log.
7. **Carry source-derived vendor document table rows as artifacts.** Where source material exposes vendor document table rows for the package, add them as artifact entries (or update existing artifact register rows) rather than minting new deliverables; cite source.
8. **Assemble turnover records.** Compile the turnover record set for the package using the categories enumerated as illustrative in `Guidance.md` (FAT, breaker tests, relay settings/coordination, grounding records, arc-flash inputs, HVAC commissioning, fire-and-gas certificates, manuals, certifications, spares, drawings). Cite source for any field that is bound by source; mark TBD otherwise.
9. **Cross-check with EPC review and acceptance.** Coordinate the register, submittals, and turnover records with `DEL-036-06_epc-vendor-package-review-and-acceptance`. Submittals enter EPC review; review comments come back through `ART-FB61C5F7B1`; final acceptance/turnover checklist is `ART-8F50EF826E`; factory/shop test evidence is `ART-2E1BDD099B`. (Source: `ARTIFACT_REGISTER.csv` rows for `DEL-036-06`.)
10. **Re-run consistency sweep.** Confirm terminology and counts in `Datasheet.md`, `Specification.md`, and `Guidance.md` remain consistent with this procedure and with the register/submittals/turnover content. Resolve, mark TBD, or escalate via the Conflict Table.
11. **Status update.** If this is a `P1_P2` run and `_STATUS.md` current state is `OPEN`, transition to `INITIALIZED`; otherwise leave `_STATUS.md` unchanged. (Source: skill Step 7.)

## Verification

| Step | Verification |
|---|---|
| 1 | Identity fields in `Datasheet.md` match `_CONTEXT.md` and Gate 7 registers; building-name discrepancy is recorded in Conflict Table. |
| 2 | Search result for `26020-Package_Requirements.docx` is recorded (found/not found); if found, source slice cited in `Specification.md`. |
| 3 | Vendor document register exists with the minimum column set; every row has a source basis or TBD. |
| 4 | Interface coverage map exists; each of the twelve declared PKG-036 interfaces has either at least one register row or an explicit TBD. |
| 5 | Submittal scope includes single-line, grounding, and protection documents that reflect the 6.9 kV/grounding-resistor basis; MCC documents include Ethernet/PLC description. |
| 6 | Submittals folder/log reconciles to register rows. |
| 7 | No source-derived vendor document rows are minted as separate deliverables. |
| 8 | Turnover record set covers the illustrative categories; TBDs are explicit. |
| 9 | EPC review and acceptance linkage to `DEL-036-06` is referenced in `Datasheet.md`, `Specification.md`, and `Guidance.md`. |
| 10 | Cross-document consistency holds (terminology, IDs, interface list). |
| 11 | `_STATUS.md` History line added only when transition was authorized. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this deliverable).
- Vendor document register (artifact, structure defined here; content TBD pending source closure).
- Vendor document submittal log and submittal artifacts (as received).
- Source-derived vendor document table rows carried as artifacts (none locally available for PKG-036 at this pass).
- Turnover record set for the package (structure defined here; content TBD pending vendor scope).
- `_STATUS.md` History line for the transition, when authorized.
- TASK run record at `_run_records/TASK_RUN_2026-05-24_1910.md`.
