# Procedure — DEL-087-06 EPC Vendor Package Review and Acceptance

> Operational document. Describes the steps the EPC Integrator follows to assemble, review, and disposition the PKG-087 Incinerator vendor package acceptance evidence set. Procedure is for **producing** the deliverable artifact (acceptance evidence) and recording the disposition.

## Purpose

To produce, in deliverable-local scope, the consolidated evidence and disposition that establish whether the PKG-087 Incinerator vendor package satisfies the EPC scope of work (DEL-087-01), package datasheet (DEL-087-02), and construction work package (DEL-087-03), per the requirements in `Specification.md`.

## Prerequisites

- DEL-087-01 (EPC Scope of Work) at state `INITIALIZED` or later. Status: **TBD (location TBD)** — confirm via `_Decomposition` package register.
- DEL-087-02 (Package Datasheet) at state `INITIALIZED` or later. Status: **TBD**.
- DEL-087-03 (Construction Work Package) at state `INITIALIZED` or later. Status: **TBD**.
- DEL-087-04 (Vendor Engineered Equipment Package) vendor deliverable in a state where vendor submittals exist for review. Status: **TBD**.
- DEL-087-05 (Vendor Document Turnover Package) vendor deliverable populated. Status: **TBD**.
- Locally accessible source slices:
  - 26020-Package_Requirements.docx heading 40 — **text slice TBD (binary at `_Sources/`)**
  - 26020-Packages_Interfaces_4_export.xlsx row 64 — **text slice TBD (binary at `_Sources/`)**
  - DBM-Deepcut: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — available
- Project document-control retention policy: **TBD (location TBD)**.

## Steps

1. **Confirm prerequisite state.** Check the GATE-07 deliverable register and `_Decomposition` status for DEL-087-01 through DEL-087-05. Record current state and `Last Updated` for each.
2. **Extract source slices.** Convert/extract 26020-Package_Requirements.docx heading 40 and 26020-Packages_Interfaces_4_export.xlsx row 64 to text slices, store under `_Sources/` derivatives, and update `_REFERENCES.md` pointers. (Out-of-scope for this deliverable folder; coordinate with the source-extraction workflow.)
3. **Build the package acceptance checklist (R-AC-02).** For each SOW row (SOW-0111..SOW-0114), each Datasheet attribute, and each CWP step, create a checklist line with: requirement source, acceptance criterion, evidence pointer slot, disposition slot. Initial dispositions are blank; criterion values that depend on Step 2 slices are entered as `TBD (location TBD)`.
4. **Assemble the vendor document review log (R-AC-01).** From DEL-087-05's vendor document register, list every required submittal with revision, EPC review code, comment-resolution status, and disposition date.
5. **Compile test and inspection evidence (R-AC-03).** Index vendor FAT, SAT, NDE, pressure-test, performance-test, and nameplate-verification records, with cross-references back to the checklist lines they satisfy. Specific acceptance thresholds: **TBD (location TBD)**.
6. **Verify safety-significant interfaces.**
   - Verify upstream knock-out drum exists and is correctly tied to spent caustic and DSO off-gas headers (R-AC-08).
   - Verify flame arrestors are installed on the spent caustic tank and DSO tank off-gas to the incinerator header (R-AC-08).
   - Verify flare/incinerator spacing of at least 25 m (82 ft) from nearest plant equipment and 25 m (82 ft) from any fired heater (R-AC-07; DBM-Deepcut lines ~280, ~296).
   - Verify thermal-radiation boundary calculation has been performed and complies with applicable regulatory requirements (R-AC-07; DBM-Deepcut line ~316).
7. **Reconcile open design parameters (R-AC-09).** For each DBM-Deepcut TBC (supplemental fuel gas rate, incinerator flow basis, dilution/enrichment gas rate, 03-25/04-25 operational responsibility), record either the resolved value with source, or a documented deviation with closure path and target date.
8. **Compile turnover evidence (R-AC-04).** Mechanical completion certificate, A/B punchlists, preservation records, training records (if applicable), and the system handover certificate. Verify completeness.
9. **Resolve non-conformances (R-AC-05).** Walk the NCR/concession log; confirm each NCR is either closed or carried as a documented deviation with engineering disposition.
10. **Cross-check interfaces (R-AC-06).** Map each row of 26020-Packages_Interfaces_4_export.xlsx row 64 (once available) to the package acceptance checklist. Specific interface entries: **TBD (location TBD)**.
11. **Compile objective traceability appendix (R-AC-12).** Map acceptance checklist outcomes to OBJ-002, OBJ-004..OBJ-010. Mapping criteria are package-grouped and recorded as ASSUMPTION; explicit per-objective acceptance criteria: **TBD (location TBD)**.
12. **Draft acceptance disposition (R-AC-10).** Prepare the proposed disposition — Accepted / Accepted with Conditions / Rejected — with the per-line justification, the list of carried-forward conditions, and the supporting evidence-record references.
13. **Obtain human acceptance signature (R-AC-10).** EPC Integrator authority signs the acceptance disposition. Agents do not sign acceptance.
14. **Snapshot and retain (R-AC-11).** Snapshot the entire evidence set at the moment of disposition, register it in the project document-control system per the retention policy (**TBD**), and update `_STATUS.md` per the project lifecycle (out of scope for this skill run — handled by a later WORKING_ITEMS dispatch).

## Verification

- Verify that every requirement R-AC-01 through R-AC-12 has at least one corresponding evidence record pointer in the assembled dossier (or an explicit `TBD (location TBD)` if the dependent source slice is still unavailable).
- Verify the acceptance disposition is human-signed and dated.
- Verify the Conflict Table in `Guidance.md` has either a closed disposition or a carried-forward `TBD` for each entry (currently C-01 and C-02).
- Verify safety-significant items (R-AC-07, R-AC-08) have walk-down evidence, not paper-only evidence.

## Records

The following records are produced or referenced under this deliverable and form the acceptance evidence dossier:

- Vendor document review log (R-AC-01)
- Package acceptance checklist (R-AC-02)
- Test/inspection evidence dossier (R-AC-03)
- Turnover evidence dossier (R-AC-04)
- NCR / deviation log with engineering dispositions (R-AC-05)
- Interface acceptance cross-check (R-AC-06)
- Spacing and thermal-radiation verification record (R-AC-07)
- KO drum and flame arrestor inspection record (R-AC-08)
- Open-parameter (TBC) resolution log (R-AC-09)
- Acceptance disposition record, human-signed (R-AC-10)
- Document-control retention metadata record (R-AC-11)
- Objective traceability appendix (R-AC-12)
