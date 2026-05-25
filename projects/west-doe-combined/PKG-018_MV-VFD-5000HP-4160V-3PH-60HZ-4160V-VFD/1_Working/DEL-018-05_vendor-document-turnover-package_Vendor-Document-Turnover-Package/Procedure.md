# Procedure — DEL-018-05 Vendor Document Turnover Package

## Purpose

Define how the Package Vendor assembles, submits, and turns over the documentation set for `PKG-018` (MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD), with EPC Integrator interface/integration review, so that `DEL-018-06` can perform package acceptance.

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` rows `DEL-018-05`/`DEL-018-06`.

## Prerequisites

- Accepted upstream snapshot: Gate 7 PROJECT_DECOMP at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (no declared upstream dependencies for `DEL-018-05`; source: `_DEPENDENCIES.md`).
- Identified driven-equipment basis from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Electric Driver and Starting Basis; MV service row).
- Access to `PKG-018/26020-Package_Requirements.docx` for clause-level submittal conventions (`location TBD` — see Conflict Table CT-3 in `Guidance.md`).
- `DEL-018-04` (Vendor Engineered Equipment Package) work artifacts available for documentation extraction (ASSUMPTION: documentation derives from vendor engineering work).

## Steps

1. **Establish package identity baseline.** Confirm `PKG-018` identity from `PACKAGE_REGISTER.csv` row (tag `26020-02-30-009`, MV VFD, 4160V LRG basis, WBS 02, Electrical). Record any title-vs-source mismatches as inputs to `Guidance.md` Conflict Table.
2. **Initialize vendor document register.** Create a register seeded with the source-required document classes from the DBM mechanical-packages organization paragraph (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, tie-in lists, operating/design envelopes, sparing philosophy, materials/coating, maintenance access, shipped-loose lists). Apply numbering/revision conventions from `26020-Package_Requirements.docx` (TBD if not yet accessible).
3. **Map source rows to register entries.** Where a source vendor document table row exists for `PKG-018`, attach it as artifact evidence per `DELIVERABLE_REGISTER.csv` Notes. Where no source row exists, mark provenance `TBD`.
4. **Populate submittals.** Collect controlled vendor submittals from the vendor engineering/supply workstream (`DEL-018-04`). Each submittal carries package identity, revision, and date.
5. **Verify electrical-basis alignment.** Cross-check submittals against:
   - 4,160 V, 3φ, 3-wire, 60 Hz LRG MV system,
   - 250–5,500 hp inverter-drive envelope,
   - SCA-001 VE #34 (starting VFD requirement),
   - SCA-001 VE #37 (no capacitor banks where VFDs present),
   - -40 °C minimum ambient.
   Flag mismatches for resolution.
6. **EPC interface/integration review.** Submit register + submittals to EPC Integrator for interface/integration review across Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports. Incorporate review comments via revisioned resubmittal.
7. **Compile turnover records.** Assemble the turnover dossier (register + final-rev submittals + review log + acceptance acknowledgements) for handoff to `DEL-018-06`.
8. **Issue and hand off.** Issue the turnover package, log the handoff, and confirm receipt by the EPC Integrator (input to `DEL-018-06`).

## Verification

| Step | Verification |
|---|---|
| 1 | Identity baseline recorded; mismatches captured in Conflict Table. |
| 2 | Register contains the source-required document class floor; numbering convention recorded (or TBD with reason). |
| 3 | Source-row evidence attached to each applicable register entry; entries without source rows flagged. |
| 4 | Each submittal has package identity, revision, and date; controlled copies traceable. |
| 5 | Cross-check matrix completed; mismatches resolved or escalated. |
| 6 | EPC review log shows each comment dispositioned and re-issued as needed. |
| 7 | Turnover dossier complete: register + submittals + review log + acknowledgements. |
| 8 | Turnover handoff record signed/acknowledged; `DEL-018-06` notified. |

## Records

- Vendor document register (final issue).
- Controlled vendor submittals (final revisions).
- EPC interface/integration review log with dispositions.
- Turnover handoff record (signed/acknowledged).
- Cross-check matrix evidencing alignment with DBM electrical basis and SCA constraints.
- Conflict Table resolution log (from `Guidance.md`).

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-018-05`.
