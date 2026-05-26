# Procedure — DEL-042-02 Package Datasheet (PKG-042 Control Room Building)

> Operational document. Steps to produce, review, issue, and maintain the Package Datasheet artifact. Steps requiring discipline judgment that the source set does not resolve are marked `TBD`.

## Purpose

Define the sequence of activities that an EPC Integrator follows to produce and issue the Control Room Building Package Datasheet from accepted upstream basis material.

## Prerequisites

- Accepted EPC Scope of Work: `DEL-042-01_scope-of-work` at `INITIALIZED` (or later) state. (ASSUMPTION: SOW logically precedes datasheet content; no explicit upstream edge declared in `_DEPENDENCIES.md`.)
- Accepted Gate 7 project decomposition snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (per `_REFERENCES.md`).
- Locally accessible reference materials in `_Sources/` (DBM-Deepcut, DBM-Comp_and_Liquids, package requirements docx, packages/interfaces xlsx).
- This deliverable's `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` present.
- A workstation with text/CSV/markdown access to source files. (xlsx/docx extraction tools required for full source coverage — see Step 2.)

## Steps

### Step 1 — Confirm Identity and Scope
1.1 Read `_CONTEXT.md` and confirm: `DeliverableID = DEL-042-02_package-datasheet`, `PackageID = PKG-042`, package name "Control Room Building", `ScopeItem = SOW-0043`.
1.2 Confirm `DELIVERABLE_REGISTER.csv` row for this deliverable matches `_CONTEXT.md`.
1.3 If any mismatch: stop and surface to ORCHESTRATOR (no in-place reconciliation).

### Step 2 — Stage Source Slices
2.1 List sources in `_REFERENCES.md`.
2.2 Extract authoritative package-row data from `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 44). (Tools TBD: docx-to-md and xlsx-to-csv extraction; this run did not perform extraction — values remain TBD.)
2.3 Re-read source slices from accessible DBMs:
- `DBM-Deepcut/4-25_Deepcut_DBM.md` §3119, §3121, §3141, §3165, §3184, §3262, §3293, §3025, §254, §298, §2759, §2810
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §75, §658, §671, §700, §704, §796
2.4 For each cited standard (API 2510, OGAOM, CEC), attempt to retrieve primary text. If not accessible, record `location TBD` against the citation.

### Step 3 — Resolve Facility Binding
3.1 Open Conflict C-001 (Guidance Conflict Table) and request human ruling on whether PKG-042 binds to Deepcut, Comp_and_Liquids, or both.
3.2 Until ruled: treat PKG-042 datasheet content as facility-agnostic where DBMs agree, and call out divergences explicitly.

### Step 4 — Populate Datasheet Sections
4.1 Identification — from `_CONTEXT.md`.
4.2 Attributes — Functional Role, Equipment Hosted, Building Envelope, Spacing, Alarm Interfaces — from source slices.
4.3 Conditions — area classification, environmental criteria, staffing — from source slices; otherwise `TBD`.
4.4 Construction — fabrication mode, foundation basis, coordination items — from source slices.
4.5 Interface Requirements Matrix — populate every row from `_CONTEXT.md` "Anticipated Artifacts" and DBM coordination lists; mark unknown values `TBD` but never delete the row.
4.6 References — list every cited source with path; mark each `location` if not directly accessed.

### Step 5 — Source-Grounding Audit
5.1 For each non-trivial value in the Datasheet, verify a citation (SourcePath + SectionRef or `location TBD`) exists.
5.2 For each inferred value, verify `ASSUMPTION:` label exists.
5.3 For each unresolved discrepancy, verify Conflict Table row exists.

### Step 6 — Cross-Document Consistency Sweep
6.1 Verify Datasheet entities/values are reflected in Specification requirements.
6.2 Verify Specification requirements have verification hooks (this Procedure §7).
6.3 Verify Guidance rationale does not overstate what sources support.
6.4 Verify terminology and numeric values match across all four documents.

### Step 7 — Verification
7.1 Document review against the requirement-to-verification table in `Specification.md §Verification`.
7.2 Plot-plan spacing review against R-9 (API 2510, OGAOM §9.6.15).
7.3 Wiring method check against R-8 (CEC, area classification, conduit size).
7.4 Server/workstation count and configuration check against R-3, R-4, R-5 source slices.
7.5 Interface Matrix completeness check (R-13).

### Step 8 — Issue and Status
8.1 When all checks pass and Conflict Table items have human rulings (or are accepted as carried-forward TBDs), the EPC Integrator authorizes issue.
8.2 Lifecycle transition (managed outside this skill): `INITIALIZED → SEMANTIC_READY` or further per project gate rules. This skill only safely transitions `OPEN → INITIALIZED`.
8.3 Record changes and rulings in `MEMORY.md` (create if needed) for future passes.

## Verification

| Check | Pass Criterion | Source |
|---|---|---|
| Identification matches register | `_CONTEXT.md` ↔ `DELIVERABLE_REGISTER.csv` row 235 | This procedure §1 |
| All source-anchored values cite source | 100% non-trivial values have citation or `location TBD` | `four-documents/QA_CHECKS.md` |
| Spacing minima carried | 50 ft (API 2510) and 82 ft (OGAOM) present | DBM-Deepcut §254, §298 |
| Wiring requirements carried | EMT permitted in control room; min 21 mm conduit; CEC compliance | DBM-Deepcut §3025 |
| Server/workstation config carried | Two fault-tolerant primary hosts in control room; secondary in MCC; three workstation sets initial design basis | DBM-Deepcut §3165, §3184 |
| Beacon group on control room exterior carried | Present | DBM-Deepcut §3262, §3293 |
| Interface Matrix complete | All anticipated interfaces have row (values may be TBD) | Spec R-13 |
| Conflict Table populated for unresolved items | C-001..C-004 present until ruled | This run record |

## Records

- `Datasheet.md` (this deliverable)
- `Specification.md`, `Guidance.md` (companion documents)
- Conflict Table entries (in `Guidance.md`)
- Run records under `_run_records/`
- `MEMORY.md` (when human rulings or durable decisions are recorded; not created in this run — no rulings recorded yet)
- `_STATUS.md` transition history
