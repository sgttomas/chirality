# Procedure — DEL-087-01 Scope of Work (PKG-087 Incinerator)

> Pass: P1_P2. Operational procedure for producing the EPC Scope of Work artifact for the Incinerator package. Interpretation rule: this procedure describes the steps required to **produce** the Scope of Work deliverable artifact, not the steps to operate the incinerator (operation belongs to the Package Vendor's documentation set under `DEL-087-04` / `DEL-087-05`).

## Purpose

Produce a source-grounded EPC Scope of Work for `PKG-087 Incinerator` that satisfies the Specification requirements (R-01..R-10) and is consistent with the Datasheet and Guidance.

## Prerequisites

- Read `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts).
- Read `_REFERENCES.md` (authoritative basis pointers).
- Read `_DEPENDENCIES.md` (no declared upstream/downstream dependencies as of 2026-05-24).
- Access the Gate-7 accepted decomposition snapshot:
  - `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 64,
  - `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 348,
  - `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_SCOPE_MAP.csv` PKG-087 rows.
- Access locally available source materials:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`,
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Note unavailable sources to mark as `location TBD`:
  - `_Sources/26020-Package_Requirements.docx` package heading 40 (not locally accessible in markdown form),
  - `_Sources/Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx` (not locally accessible in markdown form),
  - OGAOM Sec. 9.6.15 (cited via DBM-Deepcut; full standard text not locally accessible).

## Steps

1. **Confirm identity and ownership.** Confirm `_CONTEXT.md` identity fields (DeliverableID, ParentPackageID, ResponsibleParty = EPC Integrator) match `DELIVERABLE_REGISTER.csv` row 348. Record any deviation in the Conflict Table (Guidance.md).

2. **Lift the package definition verbatim from the accepted decomposition snapshot.** From `PACKAGE_REGISTER.csv` row 64, copy:
   - Package name, discipline, WBS,
   - the EPC/Vendor responsibility split (verbatim into Specification R-03),
   - the four supplied-items list (verbatim into Datasheet §Construction),
   - the twelve applicable interface types (into Specification R-04),
   - the source basis list (into the References sections).

3. **Cross-check tags against the DBM tag-detail.** From `DBM-Deepcut` Tag-Detail row 32, lift the four tags (`B-6920-1`, `FL-6920-1`, `P-6900-1`, `V-6900-1`) into Datasheet §Attributes. Map `V-6900-1` and `P-6900-1` to the knockout drum and transfer pump by name match. Mark `B-6920-1` and `FL-6920-1` mapping as `ASSUMPTION` and add Conflict CONF-02.

4. **Reconcile facility location.** Compare `DBM-Deepcut` line 1570 ("physically located at the 3-25 facility … services the 4-25 NGL mercaptan treating system") against `PACKAGE_REGISTER.csv` row 64 (WBS 02, facility 4-25 Deepcut). If they disagree (they do), record Conflict CONF-01 and use the Gate-7 snapshot as the package-identity authority while carrying the 03-25/04-25 service split as an open interface item.

5. **Lift the process-function narrative.** From `DBM-Deepcut` line 1570 ("Vapours from the spent caustic storage tank and DSO off-gas flow to the incinerator. … A knock-out drum is included upstream of the incinerator …"), write Specification R-02 and the Guidance §Purpose narrative.

6. **Lift the inlet-side backflash-protection facts.** From `DBM-Comp_and_Liquids` line 402 and `DBM-Deepcut` lines 1562, 1564, populate Specification R-10 and Datasheet §Conditions.

7. **Lift spacing rules.** From `DBM-Deepcut` lines 280 and 296, populate Specification R-09 and Datasheet §Conditions; cite OGAOM Sec. 9.6.15 as the underlying authority.

8. **Mirror open items.** From `DBM-Deepcut` lines 1572, 1890, 2244-2246, 2294-2295, propagate `TBD`/`TBC` status into Specification R-07 and Datasheet §Conditions; do not invent values.

9. **Map scope items and objectives.** From `DELIVERABLE_REGISTER.csv` row 348 and `OBJECTIVE_SCOPE_MAP.csv` PKG-087 rows, record SOW-0111..SOW-0114 and OBJ-002/004/005/006/007/008/009/010 in Specification R-08 and Datasheet §Identification. Objective association is `PACKAGE_HEURISTIC` (per the brief's `OBJECTIVE_ASSOCIATION_MODE`) and is recorded as `ASSUMPTION (best-effort mapping)` consistent with the four-documents skill rules.

10. **Cross-document consistency sweep (Pass 2).** Run the Step-5 checks from the four-documents skill: Datasheet ↔ Specification (tags and conditions reflected in requirements); Specification ↔ Guidance (each requirement has rationale); Specification ↔ Procedure (each requirement has a verification hook); terminology and values consistent across documents.

11. **Update `_STATUS.md`.** If current state is `OPEN`, set state to `INITIALIZED` via `tools/scaffolding/write_status.sh` (or by direct safe edit) with the actor `TASK+four-documents`. Do not regress state.

12. **Write a run record** at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with the required frontmatter and body headings.

## Verification

- Tag list in Datasheet matches `PACKAGE_REGISTER.csv` row 64 and `DBM-Deepcut` Tag-Detail row 32 (4 tags / 4 supplied items).
- EPC/Vendor responsibility text in Specification R-03 matches the `PACKAGE_REGISTER.csv` row 64 wording.
- All twelve interface types appear in Specification R-04.
- Conflict Table contains CONF-01 (03-25/04-25 location/service) and CONF-02 (tag-to-item mapping).
- Scope items SOW-0111..SOW-0114 and objectives OBJ-002/004/005/006/007/008/009/010 are present in Specification R-08.
- No design value asserted without a cited source slice or an explicit `TBD`/`ASSUMPTION`.
- `_STATUS.md` is either unchanged or moved `OPEN → INITIALIZED` with no regression.
- Run record exists under `_run_records/` and includes Tools Used, Outputs Produced, Applied Changes, and Needs Human Ruling sections.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file) — the four documents under this deliverable.
- `_STATUS.md` — safe-updated to `INITIALIZED` when Pass 1/2 ran from `OPEN`.
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` — audit record of this run.
- Conflict Table entries (Guidance.md) — open items for human ruling.
