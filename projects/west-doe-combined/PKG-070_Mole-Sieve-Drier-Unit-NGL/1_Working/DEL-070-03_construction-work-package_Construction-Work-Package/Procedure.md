# Procedure — DEL-070-03 Construction Work Package (Mole Sieve Drier Unit, NGL)

**Interpretation:** This Procedure covers how to *produce* the Construction Work Package deliverable artifact set (CWP narrative, installation and tie-in workface plan, construction interface and turnover checklist). It does not replace the field execution procedures (those will be issued under vendor MEC-025 IOM, PIP-024 hydrotest, PIP-025 flushing/cleaning/drying, ELE-029 FAT/SAT, etc.).

## Prerequisites

- **Declared upstream dependencies:** None declared in `_DEPENDENCIES.md` at the time of drafting. (Operationally, this deliverable depends on DEL-070-01 Scope of Work and DEL-070-02 Package Datasheet, and consumes vendor outputs from DEL-070-04; these are not yet declared in the dependency view.) — ASSUMPTION until human ruling on `_DEPENDENCIES.md`.
- **Authoritative source slice available:** `_Sources/26020-Package_Requirements.docx` heading `26020-01-PT-22-003 - Mole Sieve Drier Unit (NGL)`, including Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, and Vendor Engineering Deliverables. Confirmed accessible.
- **Authority snapshot:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER.csv row 410).
- **Vendor deliverables expected as inputs (status TBD):** MEC-016 General Arrangement, MEC-017 Installation/Setting Drawings, MEC-018 Lifting/Handling Study, PIP-004 Tie-In List, PIP-024 Hydrotest packages, PIP-025 Flushing/Cleaning/Drying Procedure, MEC-025 IOM. Drafting may proceed with TBD placeholders before these are issued.
- **Local reference reads:** `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` complete.

## Steps

1. **Confirm package identity and scope envelope.**
   - Reconcile `_CONTEXT.md` Identity block with DELIVERABLE_REGISTER.csv row 410 and the source heading title. Record any divergence as CONFLICT.
2. **Extract source scope slice into the CWP scope register.**
   - Capture Basic Scope, Major Included Equipment, Scope Notes / Open Items, and Physical Interface Summary verbatim under traceable IDs.
   - Carry by-others scope as explicit exclusions (per source Scope Notes / Open Items).
3. **Build the interface and tie-in table.**
   - One row per interface category in the source Physical Interface Summary.
   - Set CWP Applicability = source Applicability. Flag CT-01 (heated enclosure vs. Building HVAC/Services) for human ruling.
   - For each Applicability=Yes row, link to vendor deliverable IDs (e.g., process piping → PIP-004, PIP-007, PIP-008; electrical → ELE-016, ELE-027, ELE-028; I&C → INS-005, INS-006, INS-008; F&G → TSF-004; structural → STR-006, STR-011, STR-013).
4. **Draft the installation and tie-in workface plan.**
   - Anchor sequence to vendor MEC-017 setting drawings and MEC-018 lifting study (mark TBD where revision is not yet available).
   - Sequence: site preparation and foundations (STR-005/006, STR-013, CIV-014) → equipment receipt and setting (MEC-017, MEC-018) → tie-in piping and supports (PIP-004, PIP-007, PIP-008, STR-011) → electrical and EHT (ELE-016/017/018/027/028, PIP-020/021) → I&C cabling and hook-up (INS-005/006/008/009/010/011) → fire and gas (TSF-004) → hydrotest (PIP-024) → flushing/cleaning/drying (PIP-025) → sieve loading and bed conditioning (vendor procedure, TBD) → pre-commissioning and FAT/SAT (MEC-021/022, ELE-029/030) → turnover.
   - Mark each sequence node TBD where vendor input is required.
5. **Draft the construction interface and turnover checklist.**
   - One section per Applicability=Yes interface category; rows for: prerequisite documents, witness points, hold points, sign-off authority, evidence record location.
   - Reference QLT-003 ITP, QLT-020 Inspection Release Certificate, QLT-021 Manufacturing Record Book, and PRO-028 Process As-Built package as turnover evidence sources.
6. **Cross-check against Specification and Datasheet.**
   - Verify every R-CWP-* requirement maps to at least one verification activity and at least one turnover-checklist line where applicable.
   - Verify Datasheet Construction attributes are reflected in the workface plan and turnover checklist.
7. **Capture open items and CONFLICTs.**
   - Record CT-01 (heated enclosure / HVAC), CT-02 (API-661 applicability), and any further conflicts in `Guidance.md` Conflict Table.
   - Carry vendor-dependent unknowns as TBD with the responsible vendor deliverable ID.
8. **Issue for review.**
   - Set `_STATUS.md` per safe-update rules (OPEN → INITIALIZED for initial Pass 1/2 draft).
   - Surface NEEDS_HUMAN_RULING items in the run record.

## Verification

| Step | Verification |
|---|---|
| 1 | Identity block matches register row 410 and source heading; no unresolved naming conflict. |
| 2 | Every source Major Included Equipment item and every source by-others item appears in the CWP scope register or exclusions. |
| 3 | Interface table row count equals source Physical Interface Summary row count; Applicability values match source (with CT-01 flagged). |
| 4 | Workface plan covers all in-scope interface categories and references the corresponding vendor deliverable IDs; TBDs are explicit. |
| 5 | Turnover checklist has at least one row per in-scope interface category with named evidence record. |
| 6 | All R-CWP-* requirements traced to verification rows and (where applicable) checklist rows. |
| 7 | All TBD/CONFLICT items have provenance (source path + section ref or "location TBD"). |
| 8 | `_STATUS.md` update obeys safe-update rules (no state regression). |

## Records

Records produced by executing this Procedure:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in this deliverable folder.
- `_STATUS.md` state transition entry (OPEN → INITIALIZED) when authorized.
- `_run_records/TASK_RUN_<timestamp>.md` capturing inputs, tools, outputs, and ruling items.

Records consumed (not produced here) at field-execution time include: vendor MEC-017 setting reports, MEC-018 lifting sign-off, PIP-024 hydrotest packages, PIP-025 flushing/cleaning/drying records, QLT-003 ITP signed records, QLT-020 Inspection Release Certificates, QLT-021 Manufacturing Record Book, ELE-029/030 FAT/SAT and energization records, INS-029 / PIP-028 / PRO-028 as-built packages.
