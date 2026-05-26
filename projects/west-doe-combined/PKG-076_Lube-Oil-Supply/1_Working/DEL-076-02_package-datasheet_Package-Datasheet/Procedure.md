# Package Datasheet Procedure — PKG-076 Lube Oil Supply

This procedure describes how the EPC Integrator produces the Package Datasheet artifact (`Datasheet.md`) for PKG-076 Lube Oil Supply from the accepted upstream decomposition and the locally accessible source DBMs. It is a production procedure for the deliverable artifact, not an operating procedure for the lube oil supply equipment.

## Purpose

Produce a source-grounded EPC Package Datasheet for PKG-076 that satisfies REQ-076-02-01 through REQ-076-02-11 in `Specification.md` and is suitable for handoff to the Package Vendor under DEL-076-04.

## Prerequisites

- Accepted upstream decomposition snapshot present:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`).
- Deliverable-local metadata present and not modified:
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, `_STATUS.md`.
- Locally accessible source materials:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` at the time of this run.
- TBD: locally accessible text extraction of `26020-Package_Requirements.docx` (heading 30) and `26020-Packages_Interfaces_4_export.xlsx`. Without text extraction the binary sources cannot be cited at clause level.
- TBD: project hazardous-material list referenced by `3-25_Comp_and_Liquids_DBM.md`.

## Steps

1. Read `_CONTEXT.md` to confirm DeliverableID, ParentPackageID, Discipline, Type, ResponsibleParty, Scope, Anticipated Artifacts, Covers Scope Items, Supports Objectives, and Decomposition Reference.
2. Read `_REFERENCES.md` to identify the authoritative source set and the shared `_Sources` root.
3. Read the DEL-076-02 row of `DELIVERABLE_REGISTER.csv` for the canonical description, anticipated artifacts list, SOW coverage (SOW-0135…SOW-0138), and supported objectives (OBJ-001, 004-010).
4. Read `4-25_Deepcut_DBM.md`:
   - §"Utility System Summary" lube oil row;
   - §"Lube Oil Storage and Pump Basis" (full section);
   - §"Package Line-Item Requirements" row 51 (Lube Oil Supply Pumps; tags P-9240-1, P-9250-1);
   - SEC-09 sparing register entry for "Lube Oil Transfer Pump";
   - §"Open Design Development Requirements" lube oil row;
   - SEC-05 compressor sections (§828, §928, §967, §1027) for the served-compressor side of the interface;
   - §2.5 "Atmospheric Tank and General Plant Spacing" for layout/spacing applicability.
5. Read `3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers" for the hazardous-material list reference.
6. Populate `Datasheet.md` Identification, Attributes, Conditions, Construction, Interface Summary, and References sections strictly from the source slices above. Where a value is absent from source, record `TBD`. Where a value is inferred from source pattern (e.g. heating implies trace), label `ASSUMPTION`.
7. Where source slices disagree, do not silently reconcile. Record an entry in the `Guidance.md` Conflict Table with the two source pointers and a proposed authority.
8. Cross-check `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md` for terminology, tag, and value consistency:
   - Pump tags P-9240-1 and P-9250-1 spelled identically in all four documents.
   - Tank capacities (400 bbl cylinder, 200 bbl crank-case) consistent.
   - Design SG (1.00 (TBC)) consistent.
   - Same TBD/ASSUMPTION labels used for the same items.
9. Update `_STATUS.md` from OPEN to INITIALIZED only if the current state is `OPEN`; otherwise leave `_STATUS.md` unchanged and report skip. Use the `tools/scaffolding/write_status.sh` helper if available, otherwise update inline within `_STATUS.md` only.
10. Persist a run record under `_run_records/TASK_RUN_<timestamp>.md` echoing inputs, resolved state, outputs, missing items, and conflicts surfaced.

## Verification

| Check | Pass criterion |
|---|---|
| Four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` are present in the deliverable folder. |
| Default schema sections present | Datasheet: Identification, Attributes, Conditions, Construction, References. Specification: Scope, Requirements, Standards, Verification, Documentation. Guidance: Purpose, Principles, Considerations, Trade-offs, Examples. Procedure: Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | At least one locally accessible source was read from `_REFERENCES.md` and is cited in `Datasheet.md` References. |
| TBD/ASSUMPTION discipline | Every non-source-supported field is labelled TBD or ASSUMPTION; no invented values. |
| Cross-document consistency | Tags, capacities, and design SG are identical across documents; the SEC-08 vs SEC-09 pump-count conflict is surfaced in `Guidance.md` Conflict Table and referenced in `Specification.md` REQ-076-02-09. |
| Status discipline | `_STATUS.md` only transitioned from OPEN to INITIALIZED; no state regression. |
| Scope discipline | No writes outside the deliverable folder. No modifications to `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md`. |

## Records

- `Datasheet.md` — Package datasheet artifact (primary deliverable).
- `Specification.md` — Datasheet content requirements.
- `Guidance.md` — Principles, considerations, trade-offs, and Conflict Table for human ruling.
- `Procedure.md` — This procedure.
- `_STATUS.md` — Lifecycle state record (INITIALIZED after this run if precondition OPEN met).
- `_run_records/TASK_RUN_<timestamp>.md` — Auditable run record for this invocation.
