# Procedure — DEL-056-01 Scope of Work (PKG-056 Inlet Separators 4-25)

This Procedure describes how to **produce** the EPC Scope of Work artifact for `PKG-056 Inlet Separators 4-25`. It does not describe operation of the physical equipment; operation is governed by vendor and operations documents outside this deliverable.

## Purpose

Produce a source-grounded EPC Scope of Work covering package identity, tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative, suitable as the anchor for `DEL-056-02` through `DEL-056-06`.

## Prerequisites

| Prerequisite | Source | Status |
|---|---|---|
| Read `_CONTEXT.md` for deliverable identity, parent package, discipline, type, responsible party, covered scope items, supported objectives | `_CONTEXT.md` | Available |
| Read `_REFERENCES.md` for authoritative basis pointers | `_REFERENCES.md` | Available |
| Read `_DEPENDENCIES.md` for declared upstream/downstream constraints | `_DEPENDENCIES.md` | Available — no declared edges at preparation |
| Read package row in `PACKAGE_REGISTER.csv` (row 68, PKG-056) | Gate-7 snapshot | Available |
| Read deliverable row in `DELIVERABLE_REGISTER.csv` (row 372) | Gate-7 snapshot | Available |
| Read DBM slice for inlet separator system | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Available |
| Read package source heading 11 in `26020-Package_Requirements.docx` | `_Sources/26020-Package_Requirements.docx` | TBD — binary; not rendered locally for this run |
| Read RFQ `26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` | `Bid Docs/Budgetary/` | TBD — not opened in this run |

No declared upstream deliverable dependencies were identified at preparation (`_DEPENDENCIES.md`).

## Steps

### Step 1 — Lock package identity

1. Copy `DeliverableID`, `Name`, `ParentPackageID`, `ParentWorkbookID`, `PackageName`, `Discipline`, `Type`, `ResponsibleParty` from `_CONTEXT.md` into the Scope of Work identity block.
2. Cross-check against `DELIVERABLE_REGISTER.csv` row 372 and `PACKAGE_REGISTER.csv` row 68.
3. Resolve any mismatch by surfacing it in the Conflict Table; do not edit `_CONTEXT.md`.

### Step 2 — Establish tagged equipment list

1. From the DBM equipment listing (`4-25_Deepcut_DBM.md` row 2540 and adjoining rows), list the inlet separator equipment tags currently named: `V-1600-1` (Inlet Separators 2 — Unit 1) and `V-1700-1` (Inlet Separators 2 — Unit 2).
2. State the installed-quantity position from current DBM body: two installed plus plot provision for a third. Cite the conflicting legacy four-package reference in the Conflict Table.

### Step 3 — Draft package function narrative

1. State the package function from `PACKAGE_REGISTER.csv` row 68: receive raw inlet gas; separate into sour natural gas (vapour), sour raw condensate (light liquid), sour water (heavy liquid).
2. Add the role from `4-25_Deepcut_DBM.md` §Inlet separator system: slug handling and liquid separation upstream of MPFF and stabilizer.

### Step 4 — Anchor source basis

1. Cite Workbook Packages row 68 and `26020-Package_Requirements.docx` package heading 11.
2. Cite the Word Source Basis: `26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` and `4-25_Deepcut_DBM.md`.
3. Where a cited source text is not locally rendered, mark "location TBD" and do not derive clause-level requirements from it.

### Step 5 — Declare boundaries and interfaces

1. List the eleven applicable interface types verbatim from `PACKAGE_REGISTER.csv` row 68.
2. Declare the boundary between Package Vendor authority and EPC Integrator authority.
3. Identify upstream (inlet ESDV station; drive-gas tie-in) and downstream (MPFF; gas processing train) interfaces from the DBM.

### Step 6 — Write the whole-facility integration narrative

1. Locate the package in the West Doe Deepcut (04-25) front-end process flow per `4-25_Deepcut_DBM.md` §Front-end process basis.
2. Describe how inlet separation feeds MPFF, stabilizer overheads compression, amine, TEG, drive-gas, flare, and drain systems.
3. State the unit-isolation principle.

### Step 7 — Produce the responsibility assignment record

1. Capture EPC Integrator responsibilities (integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) and Package Vendor responsibilities (package engineering, package design, vendor documentation, physical equipment package).
2. Cross-check against `PACKAGE_REGISTER.csv` row 68 narrative.

### Step 8 — Trace to scope items

1. Verify the Scope of Work content traces to `SOW-0127`, `SOW-0128`, `SOW-0129`, `SOW-0130` (collectively).
2. If individual SOW-item text is needed for line-level mapping, mark TBD and surface a missing-source note.

### Step 9 — Final consistency sweep

1. Confirm the four deliverable-local documents agree on entity names, values, tag identities, and quantities.
2. Confirm every non-trivial claim has a citation, a `TBD`, or an explicit `ASSUMPTION`.
3. Confirm the Conflict Table in `Guidance.md` is complete and consistent with `Datasheet.md` and `Specification.md`.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| Identity block matches `_CONTEXT.md` | Side-by-side | All identity fields match exactly |
| Equipment tags match DBM rows 2540, 2596–2597 | Side-by-side | Tags listed verbatim |
| Quantity conflict preserved | Read Conflict Table | C-056-01-01 present, ruling = TBD |
| Source citations resolve | Path resolution | Each citation resolves to an extant file/row, or is marked "location TBD" |
| Interface-type list verbatim | Side-by-side | Eleven interface types listed exactly as in `PACKAGE_REGISTER.csv` row 68 |
| Cross-document terminology consistent | Re-read | "Inlet separator", "MPFF", "stabilizer", "drive gas", "Package Vendor", "EPC Integrator" used identically across the four documents |
| No edits to `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` | File hash / diff | Files unchanged |

## Records

The following deliverable-local records constitute evidence that this procedure was followed:

- `Datasheet.md` — identity, attributes, conditions, construction context, references, open items.
- `Specification.md` — scope, requirements (R1–R7), standards, verification, documentation.
- `Guidance.md` — purpose, principles, considerations, trade-offs, examples, Conflict Table.
- `Procedure.md` — this document.
- `_run_records/TASK_RUN_*.md` — TASK run record (skill: four-documents).
- `_STATUS.md` — safe-update lifecycle record (`OPEN → INITIALIZED` when authorized).
