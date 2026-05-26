# Procedure — Vendor Document Turnover Package (DEL-085-05)

> Operational steps for the Package Vendor (with EPC Integrator interface/integration review) to produce, maintain, and hand over the vendor document turnover package for PKG-085 Flare Stack (High Pressure).

## Purpose

Provide a repeatable sequence for assembling the vendor document register, controlling submittals, preserving source-row evidence, obtaining EPC Integrator interface/integration review, and executing the turnover for PKG-085.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in the deliverable folder (confirmed for DEL-085-05).
- Access to the Package Requirements source slice for this package: `26020-Package_Requirements.docx`, heading 38 (`26020-02-PT-25-001 — Flare Stack (High Pressure)`).
- Access to the Packages/Interfaces workbook: `26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 58.
- Project Document Control Procedure (governing status codes and turnover record format) — `TBD` (not in `_REFERENCES.md`).
- Declared upstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`). Operational dependency on `DEL-085-04` (vendor engineered content) and on `DEL-085-06` (EPC review/acceptance) is `ASSUMPTION` from peer deliverables under PKG-085.

## Steps

### Step 1 — Initialize the vendor document register
1. Create the register for PKG-085 with columns sufficient to satisfy SPEC-085-05-R2: Document ID, Title, Revision, Status (vocabulary `TBD`), Transmittal Reference, EPC Integrator review disposition, Source SOW row (one of SOW-0087…SOW-0090), Interface Domain(s).
2. Seed the register with one row per anticipated vendor document, drawing from the active interface domains in workbook row 58 (Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports). Mark unknown rows `TBD`.

### Step 2 — Receive and log vendor submittals
1. For each Package Vendor transmittal, add or update a register row.
2. Attach or link the submitted document(s); preserve the native vendor format.
3. Where the source vendor document table provides a row for the submittal, preserve that row as artifact-level evidence (per `_CONTEXT.md` Notes) and link it from the register entry. (`TBD` where source rows are not available.)

### Step 3 — EPC Integrator interface/integration review
1. Route each submittal to the EPC Integrator for **interface/integration** review (mandated by `_CONTEXT.md` ResponsibleParty).
2. Record the disposition (Accepted / Accepted with comments / Rejected — vocabulary `TBD`) in the register.
3. For dispositions other than Accepted, track the resubmittal cycle until a terminal disposition is reached.

### Step 4 — Resolve TBD carry-overs from source
1. Inventory items marked `TBD` or empty in `26020-Package_Requirements.docx` heading 38 (`Vendor Engineering Deliverables` empty; `Interface Coordination Notes` `TBD`).
2. For each, either obtain the missing vendor content and add it to the register, or formally record acceptance of the `TBD` carry-over with rationale (per SPEC-085-05-R9).

### Step 5 — Coverage check against active interface domains
1. Verify the register contains at least one document addressing each of the eight active interface domains identified in workbook row 58 (per SPEC-085-05-R5).
2. Record gaps; do not close the turnover until each gap is either filled or formally accepted.

### Step 6 — Assemble turnover record
1. Snapshot the register at a defined cut-off and produce the turnover record per the Project Document Control Procedure (format `TBD`).
2. Include: register snapshot, transmittal references, EPC Integrator review dispositions, any accepted `TBD` carry-overs, and signatories.

### Step 7 — Execute turnover
1. Transfer custody of the assembled documentation set to the receiving party (EPC Integrator / Owner per project document control; `TBD`).
2. File the turnover record and the register snapshot in the project document control system.
3. Update `_STATUS.md` according to project lifecycle rules (this Procedure does not itself set deliverable lifecycle state; that is governed by `WORKING_ITEMS` / human ruling).

## Verification

| Check | Method |
|---|---|
| Register exists and is current | Inspect register file; confirm last-updated date and revision history. |
| All transmittals logged | Sample audit: compare a sample of transmittals from the Package Vendor against register rows. |
| EPC Integrator review present | Inspect register for review disposition on every submittal prior to turnover. |
| Interface domain coverage | Cross-check register against workbook row 58 active set. |
| TBD carry-overs resolved or accepted | Inspect disposition log against the source-derived `TBD` inventory. |
| Turnover record complete | Inspect turnover record contents against Step 6 list. |

## Records

- Vendor document register (file; format `TBD`).
- Vendor document submittal files (attached / linked from register).
- Source vendor document table rows preserved as evidence (where available).
- EPC Integrator interface/integration review records (cross-referenced to `DEL-085-06`).
- Turnover record (final handover record).
- `TBD` disposition log (resolutions and accepted carry-overs).
