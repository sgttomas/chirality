# Procedure: DEL-106-05 — Vendor Document Turnover Package

Pass: P1 (initial draft) — Source-grounded against GATE-07 Final Published PROJECT_DECOMP snapshot.

This Procedure describes the steps to **produce** the Vendor Document Turnover Package artifact for PKG-106 (Yard Lighting). Operational use is governed downstream by DEL-106-06 (EPC Vendor Package Review and Acceptance).

## Prerequisites

- Read and current: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`. (Source: deliverable folder; PREPARATION baseline.)
- Access to the accepted upstream snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`. (Source: `_REFERENCES.md`.)
- Access to PKG-106 source materials in `_Sources/` (notably `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx`). (Source: `_REFERENCES.md` shared source root.)
- Identified Package Vendor for PKG-106 (responsible party). (Source: DELIVERABLE_REGISTER.csv.)
- Sibling deliverable products available as inputs where mature:
  - DEL-106-01 EPC Scope of Work (defines what vendor must document against)
  - DEL-106-02 EPC Package Datasheet (carries interface facts and handoff basis)
  - DEL-106-04 Vendor Engineered Equipment Package (technical basis being documented)
  (Source: DELIVERABLE_REGISTER.csv; ARTIFACT_REGISTER.csv.)
- Declared dependencies: none currently declared in `_DEPENDENCIES.md`. ASSUMPTION: the four siblings above are de facto upstream context even though not formally declared.

## Steps

1. **Establish the Vendor Document Register skeleton.**
   - Open `_Sources/26020-Package_Requirements.docx` and `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 12) to extract any source-listed required vendor documents for PKG-106. (Source: `_REFERENCES.md`; PACKAGE_REGISTER.csv.)
   - If the source enumerates required vendor documents, seed those rows into the register with title, expected revision, responsible vendor function, and submittal milestone.
   - If the source does not enumerate (currently the case per ART-182773E33C), seed a minimal placeholder register flagged TBD and proceed to Step 2.

2. **Resolve content gaps.**
   - Engage the Package Vendor and EPC Integrator to confirm the project's default vendor document list for an Electrical area-lighting package (e.g., GA drawings, wiring diagrams, photometric calculations, fixture/luminaire datasheets, control system documentation, test reports, O&M manuals, spare parts list, certificates of compliance). Mark all such project-default entries as ASSUMPTION until confirmed.
   - Record any items requiring human ruling in the Conflict Table in `Guidance.md`.

3. **Align with package scope and interfaces.**
   - Cross-check the register against DEL-106-01 (Scope of Work) for completeness against tagged equipment and package function. (Source: ARTIFACT_REGISTER.csv ART-1D00D7FAE6, ART-508A45C565, ART-C1764AFD92.)
   - Cross-check against DEL-106-02 interface facts: Electrical Power (IFC-6FCF1B30D6), Grounding / Bonding (IFC-DA0D60681B), Area / Exterior Lighting (IFC-ED86F51087). Confirm at least one vendor document addresses each interface. (Source: INTERFACE_REGISTER.csv.)

4. **Collect vendor submittals.**
   - For each register entry, obtain the vendor submittal at the contractual revision.
   - Verify document control fields (title, document number, revision, date, vendor identification) and that titles match the register.

5. **Carry source vendor-document table rows as artifacts.**
   - Where Workbook Packages row 12 lists specific vendor documents as rows in the source workbook, capture those rows as artifacts of this deliverable (not as separate deliverables). (Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv.)
   - If no source rows exist (current case), record the absence with reference to ART-182773E33C.

6. **Prepare turnover records.**
   - Assemble the turnover transmittal listing all submittals included, their revisions, and acceptance status from EPC Integrator review (executed under DEL-106-06).
   - Include any vendor close-out certificates as required by the project's turnover convention (ASSUMPTION; specifics TBD).

7. **Hand off to EPC Integrator review.**
   - Submit the register, submittals, source-row artifacts, and turnover records to the EPC Integrator for review under DEL-106-06. (Source: DELIVERABLE_REGISTER.csv DEL-106-06; ARTIFACT_REGISTER.csv ART-DE7811332B.)
   - Capture review comments and update submittals as required; iterate until acceptance.

8. **Close out.**
   - Once EPC Integrator acceptance is recorded under DEL-106-06 (ART-6A9AFD2292), advance this deliverable's `_STATUS.md` per the project state model.

## Verification

| Check | Verifies | Notes |
|---|---|---|
| Register completeness vs. source rows | REQ-106-05-01, REQ-106-05-03 | If source rows absent (current case), verification reduces to confirming the gap is recorded via ART-182773E33C. |
| Each register entry has a matching submittal at the listed revision | REQ-106-05-02 | Manual inspection of register vs. submittal set. |
| Each declared PKG-106 interface (Electrical Power; Grounding/Bonding; Area/Exterior Lighting) is addressed by at least one vendor document | REQ-106-05-06 | Cross-reference vendor documents to DEL-106-02 interface artifacts. |
| Turnover record lists all included submittals | REQ-106-05-04 | Transmittal vs. register reconciliation. |
| Responsible-party split honored (Vendor produces; EPC Integrator reviews under DEL-106-06) | REQ-106-05-05 | Trace authoring/review signatures. |
| Traceability to SOW-0011 and objectives recorded | REQ-106-05-07 | Recorded in `_CONTEXT.md`; ASSUMPTION flag preserved. |

## Records

- Vendor Document Register (with revision history)
- Vendor document submittals (each at controlled revision)
- Carried source-row artifacts (none for PKG-106 in current snapshot)
- Turnover transmittal(s) and acceptance evidence (the latter captured under DEL-106-06)
- Run records for this deliverable in `_run_records/`
