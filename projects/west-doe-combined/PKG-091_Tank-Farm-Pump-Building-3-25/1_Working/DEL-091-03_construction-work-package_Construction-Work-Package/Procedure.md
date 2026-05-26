# Procedure — DEL-091-03 Construction Work Package

This procedure describes the operational steps to **produce** the Construction Work Package deliverable artifact set for PKG-091 Tank Farm Pump Building 3-25. (Per the skill interpretation rule, Procedure may describe steps to produce and/or operate the deliverable; here the artifact is the CWP document set, so the producing procedure is primary.)

## Prerequisites

### Declared upstream dependencies

- None declared in `_DEPENDENCIES.md` at PREPARATION (DECLARED mode, no explicit upstream edges yet).

### Required references (accessed)

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row 470; `SCOPE_LEDGER.csv` rows 186–189 (SOW-0185..0188); `PROJECT_DECOMP.md`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`

### Required references (cited; not directly slice-read in this run)

- Workbook Packages row 84 (`location TBD` — binary `26020-Packages_Interfaces_4_export.xlsx`)
- `26020-Package_Requirements.docx` package heading 44 (`location TBD` — binary)

### Logical upstream artifacts (not yet drafted — `TBD` until siblings are produced)

- DEL-091-01 Scope of Work
- DEL-091-02 Package Datasheet
- DEL-091-04 Vendor Engineered Equipment Package (vendor design basis)

## Steps

1. **Confirm deliverable identity and scope.** Re-read `_CONTEXT.md` and confirm `DeliverableID`, `ParentPackageID`, scope items, and anticipated artifacts.
2. **Load authoritative source slices.**
   - Read SOW-0185 through SOW-0188 from `SCOPE_LEDGER.csv` (rows 186–189).
   - Read `DELIVERABLE_REGISTER.csv` row 470 for the deliverable narrative.
   - Read DBM §Site and §Liquids Hub slices for siting and adjacent-system context.
   - Mark binary-source slices (workbook row 84, `26020-Package_Requirements.docx` heading 44) as `location TBD` where the binary cannot be read directly.
3. **Inventory equipment.** Build the authoritative pump list (tag, service, type, motor/duty) directly from SOW-0187. Cross-check duty values against SOW-0188; record `TBC` items from SOW-0188 as `TBD`.
4. **Identify boundary cuts.** Capture the "By Others" exclusions verbatim from SOW-0188 (DCS integration, foundations, electrical supply to MCC) and reflect them in Specification §Scope and §Requirements.
5. **Draft Specification requirements.** Issue one requirement per material installation, integration, or boundary obligation traceable to a source slice. Label inferred requirements `ASSUMPTION`.
6. **Map verification approaches.** For each requirement, write one verification approach and one record type. Use `TBD` where source data does not support a specific method.
7. **Draft Guidance.** Capture purpose, principles, considerations, and trade-offs traceable to source content or labelled `ASSUMPTION`.
8. **Cross-document consistency sweep.** Confirm pump tags, duties, motor ratings, scope boundaries, and standards (API-682) appear consistently across `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md`.
9. **Capture conflicts.** If source slices disagree or contradict the decomposition narrative, log a row in `Guidance.md` §Conflict Table. (None captured this pass.)
10. **Update `_STATUS.md`.** If current state is `OPEN`, transition to `INITIALIZED` via `tools/scaffolding/write_status.sh`.
11. **Write the run record.** Persist `_run_records/TASK_RUN_<timestamp>.md` with input echo, resolved state, tools used, outputs produced, missing items, and dependency notes.

## Construction-execution steps (when the CWP is later used to build the package)

The following high-level on-site sequence is `ASSUMPTION` from package type plus SOW-0186/0187 content; detailed sequencing belongs in the not-yet-issued installation and tie-in workface plan (anticipated artifact):

a. Confirm foundations complete and accepted (By Others — SOW-0188).
b. Confirm 600 V MCC energized and feeders pulled to package boundary (By Others — SOW-0188).
c. Receive and inspect vendor-supplied pump skids/building (Vendor — DEL-091-04).
d. Set, align, and grout pumps per vendor IOM (REQ-091-03-001).
e. Make pneumatic supply and drain tie-in for P-9295-2 (REQ-091-03-004).
f. Make produced-water suction/bag-filter/discharge tie-ins for P-9290/9293-2 (REQ-091-03-005).
g. Make sour condensate suction/discharge tie-ins for P-9215/9216-2 to P-9210/9220-2 (REQ-091-03-006).
h. Install and verify API-682 Plan 14/52 seal plans (REQ-091-03-007).
i. Install sealless diaphragm pumps including the P-9240-2 inlet basket strainer (REQ-091-03-008).
j. Terminate motor feeders; install/verify HOA/On-Off local controls; verify starter type per pump (REQ-091-03-002).
k. Walk down cold-weather provisions (heat tracing, insulation) — scope split `TBD` (REQ-091-03-003).
l. Loop-check field instrumentation to the package edge; DCS integration handoff (By Others — SOW-0188).
m. Hydrotest, flush, pre-commission per the construction interface and turnover checklist (REQ-091-03-009).
n. Close the workface plan (REQ-091-03-010) and turn over to commissioning under DEL-091-06.

## Verification

- **Document set complete.** `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md` exist in the deliverable folder with default schema sections.
- **Source-grounding.** Each non-trivial claim cites a source (SOW-####, GATE-07 register row, DBM section, or explicit `location TBD`).
- **Boundary discipline.** "By Others" exclusions appear in Specification §Scope and §Requirements and are not contradicted in Datasheet or Procedure.
- **Status transition safe.** `_STATUS.md` is only modified `OPEN → INITIALIZED` via the scaffolding helper.
- **Run record persisted.** `_run_records/TASK_RUN_<timestamp>.md` written with the required frontmatter and body headings.

## Records

- The four document files (this folder).
- `_run_records/TASK_RUN_2026-05-25_0513.md` (this run).
- `_STATUS.md` updated to `INITIALIZED` with provenance line.
- (Downstream, when the CWP is executed) the installation and tie-in workface plan, construction interface and turnover checklist, electrical/instrument termination records, hydrotest/line-check records, mechanical completion certificate.
