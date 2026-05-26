# Procedure: DEL-050-03 — Construction Work Package

**Interpretation:** This procedure describes how the EPC Integrator **produces** the Construction Work Package deliverable for `PKG-050 Stabilizer Overheads Compressors`. Field execution procedures (installation method statements) are downstream artifacts of the work package, not this deliverable.

## Prerequisites

- DEL-050-01 Scope of Work (sibling) — accepted or in-progress with stable scope (referenced for SOW-0173..0176 coverage).
- DEL-050-02 Package Datasheet (sibling) — required for technical inputs to construction planning; resolve to current draft state. (No formal Upstream/Downstream declared in `_DEPENDENCIES.md` — these are method-level inputs, not hard constraints.)
- Access to GATE-07 PROJECT_DECOMP snapshot:
  - `DELIVERABLE_REGISTER.csv` (row DEL-050-03)
  - `PACKAGE_REGISTER.csv` (row PKG-050)
  - `INTERFACE_REGISTER.csv` (location TBD — slice not extracted)
- Access to project-level construction standards, HSE plan, and area classification documents — location TBD; not in deliverable-local scope.

## Steps

1. **Establish scope and identity.**
   - Confirm DeliverableID, ParentPackageID, ResponsibleParty from `_CONTEXT.md`.
   - Confirm covered scope items SOW-0173..0176 and supported objectives OBJ-001/003/004/005/006/007/008/009/010 from DELIVERABLE_REGISTER row DEL-050-03.

2. **Capture process and equipment basis.**
   - Record equipment configuration: 2x100% induction motor-driven separable reciprocating compressors (PACKAGE_REGISTER row PKG-050).
   - Record pressure step (50 psig suction → 1100 psig discharge) and downstream routing (amine inlet filter coalescer; first-stage recycle).

3. **Enumerate interfaces.**
   - For each of the 13 applicable interface types listed in PACKAGE_REGISTER row PKG-050 (InterfaceTypes), open a construction interface section.
   - For each interface: identify counterparty (EPC discipline or vendor), boundary point, governing document (TBD where not yet defined), and construction sequence anchor.

4. **Draft the installation and tie-in workface plan.**
   - For each train (2x), define the construction sequence from foundation through mechanical completion.
   - Identify enabling utilities (electrical power, EHT, grounding, F&G, control cabling) and sequence them relative to process tie-ins.
   - Note pre-commissioning checks (alignment, torque, hydro/pneumatic test boundaries) — specific procedures TBD per project ITP.

5. **Build the construction interface and turnover checklist.**
   - Use the 13 interface types as the checklist spine.
   - For each interface: list inspection points, hold/witness/review points, and the acceptance evidence required to support DEL-050-06.

6. **Cross-check coverage.**
   - Traceability matrix: every SOW-0173..0176 row mapped to one or more sections of the work package.
   - Coverage check: every InterfaceType has at least one workface-plan entry and one turnover-checklist entry.

7. **Identify open items and assumptions.**
   - Surface every TBD (area classification, standards, ambient envelope, etc.) and every ASSUMPTION (e.g., skid-mounted vendor scope on EPC foundations) as a tracked open item.
   - Update Conflict Table in `Guidance.md` if new conflicts emerge.

8. **Produce the master Construction Work Package document.**
   - Compile scope statement, equipment basis, interface sections, workface plan, turnover checklist, traceability matrix, and open-items log into the master artifact.
   - Apply project document control numbering — TBD.

9. **Internal QA review.**
   - Verify all requirements in `Specification.md` are reflected in the work package.
   - Verify terminology and values (interface names, pressure values, train count) are consistent with Datasheet and Specification.

10. **Hand off to DEL-050-06 review.**
    - Package the master document with the workface plan and turnover checklist; route to EPC Vendor Package Review and Acceptance.

## Verification

- Step 3 produces an interface section per InterfaceType (13/13 coverage).
- Step 5 produces a turnover checklist with traceable acceptance evidence rows.
- Step 6 traceability matrix shows complete SOW-0173..0176 coverage.
- Step 9 QA review confirms cross-document consistency with Datasheet and Specification.
- No fabricated requirements: every requirement traces to PACKAGE_REGISTER, DELIVERABLE_REGISTER, `_CONTEXT.md`, or is labeled ASSUMPTION/TBD.

## Records

- Construction Work Package master document
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Traceability matrix to SOW-0173..0176
- Open items / assumptions / TBD log
- Internal QA review record
- Run records under `_run_records/` (this run and successors)
