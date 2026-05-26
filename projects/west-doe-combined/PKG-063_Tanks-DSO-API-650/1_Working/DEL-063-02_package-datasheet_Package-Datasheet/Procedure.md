# Procedure — DEL-063-02 Package Datasheet (PKG-063 Tanks, DSO (API 650))

**Interpretation:** This procedure describes how the EPC Integrator **produces** the Package Datasheet artifact (DEL-063-02). It does not describe operation of the DSO storage tank itself (that is downstream vendor / operations scope).

## Prerequisites

- **Declared upstream dependencies:** None declared in `_DEPENDENCIES.md` (Coordination Mode: DECLARED). Treat the following as informational inputs only.
- **Reference materials required (per `_REFERENCES.md`):**
  - Accepted Gate-7 PROJECT_DECOMP snapshot (`_GateSnapshots/GATE-07_Final_Published_2026-05-24/`) including DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv.
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"Disulphide Oil, Spent Caustic, and Waste Amine"; major-equipment table; off-gas / blanket-gas description.
  - `_Sources/26020-Package_Requirements.docx` — package heading 18 ("Tanks, DSO" section). Binary file; extraction tooling required for clause-level verification; `location TBD` for specific modifications-to-API-650 list.
  - `_Sources/Bid Docs/_Budgetary/26020-01-PT-RFQ-19-001_Tanks_DSO_R0.docx` — listed in PACKAGE_REGISTER.csv as Word Source Basis; **not locally accessible during this pass** — `location TBD`.
- **Companion deliverable read-only inputs:** DEL-063-01 (Package Scope of Work) for PKG-063 should be consulted for the source-of-truth on package identity and SOW row alignment.
- **State precondition:** `_STATUS.md` must be in `OPEN` or `INITIALIZED` before this skill overwrites the four documents (per `ALLOW_OVERWRITE_STATES=OPEN,INITIALIZED`).

## Steps

1. **Confirm identity.** Read `_CONTEXT.md` and the matching `DELIVERABLE_REGISTER.csv` row to confirm DeliverableID, ParentPackageID, PackageName, Discipline, and Type. (Verification — Identification block of `Datasheet.md`.)
2. **Pull package basis.** Extract the PKG-063 row from `PACKAGE_REGISTER.csv` for package description, process function, responsibility split, and the listed applicable interface types. Confirm the Word and Workbook source-basis pointers.
3. **Pull artifact evidence rows.** From `ARTIFACT_REGISTER.csv`, collect every row where `DeliverableID = DEL-063-02_package-datasheet`. These supply the Major Included Equipment text, the vendor-handoff basis, the interface fact rows, and the documentation list.
4. **Pull interface facts.** From `INTERFACE_REGISTER.csv`, collect every row where `PackageID = PKG-063` and `Applicable = YES`. There are nine such rows for PKG-063; each becomes a numbered REQ in `Specification.md` and a row in the Datasheet "Construction" interface table.
5. **Pull design narrative.** Read `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` for the DSO tank narrative (atmospheric / heated / insulated / truck-out / incinerator-header / flame-arrestor / fuel-gas blanket / SG 1.75 TBC) and quote the exact source slice when transcribing values.
6. **Authority hierarchy check.** When the decomposition narrative and the DBM source disagree, source wins. When the Word heading 18 contains text not in DBM, treat it as authoritative for the package-specific value once the Word slice is extracted; mark `location TBD` until then.
7. **Draft `Datasheet.md`.** Populate Identification, Attributes (one row per source-supported mechanical attribute), Conditions (process function, fluid, operating envelope), Construction (interface table + construction notes), References (full source pointer list).
8. **Draft `Specification.md`.** Convert each datasheet attribute and each declared interface into a numbered REQ-063-02-NN with a source citation. Mark all unsupported values `TBD` and labeled inferences `ASSUMPTION`. Carry Standards, Verification mapping, and Documentation lists.
9. **Draft `Guidance.md`.** Capture Purpose, Principles, Considerations, Trade-offs, Examples, and (if any) Conflict Table for human ruling.
10. **Draft `Procedure.md`.** Capture this production procedure with Prerequisites, Steps, Verification, Records.
11. **Pass 2 cross-reference sweep.** Compare values, terminology, and references across all four documents per the checklist in `## Verification` below; fix any inconsistency; capture unresolved disagreements in the Conflict Table.
12. **Update `_STATUS.md`.** If current state is `OPEN`, transition `OPEN → INITIALIZED` with annotation `TASK+four-documents` (Step 7 of skill method). If state is not `OPEN`, do not modify `_STATUS.md` (no state regression).
13. **Write run record.** Persist `_run_records/TASK_RUN_<timestamp>.md` capturing input echo, resolved state, tools used (`none`), outputs, and any TBD/NEEDS_HUMAN_RULING items.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| All four documents exist | Filesystem listing of `{DELIVERABLE_PATH}` | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all present |
| Default schema sections present | Header scan per skill `SKILL.md` defaults | Datasheet has Identification/Attributes/Conditions/Construction/References; Specification has Scope/Requirements/Standards/Verification/Documentation; Guidance has Purpose/Principles/Considerations/Trade-offs/Examples; Procedure has Purpose (implicit in scope)/Prerequisites/Steps/Verification/Records |
| Source grounding | Every non-trivial datasheet value carries a source citation or is marked `TBD` / `ASSUMPTION` | No silent assertions; K-PROV-1 satisfied |
| Cross-document consistency | Pass 2 sweep against the matrix below | No unresolved conflicts; or conflicts captured in Guidance Conflict Table |
| Interface coverage | Count of REQ-063-02 interface rows in `Specification.md` equals count of `PKG-063` rows in `INTERFACE_REGISTER.csv` with `Applicable=YES` | 9 = 9 |
| Status discipline | `_STATUS.md` transition is `OPEN → INITIALIZED` only when state was `OPEN` | No state regression |

**Cross-document consistency matrix:**

| Pair | What to verify |
|---|---|
| Datasheet ↔ Specification | Every mechanical/process attribute in Datasheet appears as a numbered REQ in Specification, with the same value and unit. |
| Specification ↔ Guidance | Each REQ with material trade-offs (heater setpoint, coating, CP scope split) is addressed in Guidance Considerations / Trade-offs. |
| Specification ↔ Procedure | Each REQ has a verification entry in Specification §Verification and/or a step in Procedure §Steps. |
| Terminology | "DSO", "Disulphide Oil", "DSO storage tank", "PKG-063", "Tanks, DSO (API 650)" used consistently. |
| Values | 400 bbl, 32 oz design / 1 oz vacuum, 32.2 °C (90 °F), SG 1.75 (TBC), nine interfaces — identical across documents. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in the deliverable folder.
- `_STATUS.md` updated to `INITIALIZED` with date and `TASK+four-documents` annotation.
- `_run_records/TASK_RUN_<timestamp>.md` capturing input echo, resolved state, outputs, missing items, and rulings needed.
- Downstream consumers (DEL-063-03, DEL-063-04, DEL-063-05, DEL-063-06) reference this artifact set as their EPC anchor.
