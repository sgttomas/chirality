# Procedure — DEL-086-04 Vendor Engineered Equipment Package

Procedure is interpreted here as the steps to **produce** the Vendor Engineered Equipment Package artifact set (per skill `four-documents` interpretation rule). Operational use steps for the physical flare stack belong to operations and are out of this deliverable's scope.

## Prerequisites

- Accepted upstream PROJECT_DECOMP snapshot: GATE-07_Final_Published_2026-05-24. (`_REFERENCES.md` — FACT)
- EPC anchor deliverables initialized and at maturity ≥ INITIALIZED:
  - `DEL-086-01` Scope of Work
  - `DEL-086-02` Package Datasheet
  (`PACKAGE_REGISTER.csv` row 59 — FACT; declared upstream linkage not yet entered in `_DEPENDENCIES.md` — see Records below.)
- Locally accessible reference:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Named-but-not-locally-accessible references (location TBD):
  - `26020-Package_Requirements.docx` package heading 39
  - `Bid Docs/Budgetary/brief.md`
  - `Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf` (budgetary go-by only — not authority)
  - `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy

## Steps

1. **Receive EPC inputs.** Receive `DEL-086-01` Scope of Work and `DEL-086-02` Package Datasheet from the EPC Integrator. Confirm package tag 26020-02-PT-25-002 and PKG-086 identity. (Verifies R-01.)
2. **Confirm package boundaries.** Reconcile vendor-vs-EPC boundaries per PACKAGE_REGISTER row 59 (PrimaryResponsibilities), and identify shared-system items — particularly the HP/Cryo + LP dual flare stack 03-25/04-25 service-split open interface. (Verifies R-06.)
3. **Establish service-mix design basis.** Document LP flare service set (TEG regeneration, VRU, compressor seal-pot) and the 508 mm/20 in LP relief header tie-in basis. Flag LP stack OD as TBD pending vendor sizing. (Verifies R-02, R-03, R-07.)
4. **Perform vendor sizing and selection studies.**
   - Stack: OD, height, mechanical type (self-supported vs alternative). The budgetary self-supported pdf is go-by only.
   - Burner tip and pilot/ignition. (Verifies R-07, R-15.)
   - Associated LP flare stack blower sizing and selection. (Verifies R-13.)
5. **Coordinate blowdown alignment.** Align vendor sizing with staggered blowdown intent (DBM line 501) and ingest sequencing inputs from W242510-PRC-REP-000003-001 when accessible. (Verifies R-04, R-05.)
6. **Develop vendor design basis and datasheets.** Produce the vendor package design basis and the package datasheet set as anticipated artifacts. (Verifies R-14.)
7. **Develop the engineered equipment package.** Mechanical, structural/foundation, electrical, instrumentation, fire & gas, drain/vent tie-in details coordinated with civil/electrical/controls/I&C disciplines. (Verifies R-09, R-12.)
8. **Apply isolation and sour-service philosophy.** Skid-edge isolation, double block/bleed where required, sour-service materials/coating decisions. (Verifies R-10, R-11.)
9. **Compile vendor deliverable register content.** Datasheets, cause-and-effect inputs, utility load summary, relief/load data, field tie-in list, operating/design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item list, vendor document register. (Verifies R-08.)
10. **Confirm interface alignment.** Map vendor scope against PKG-086 applicable interface types (Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports). (Verifies R-16.)
11. **Issue for EPC review.** Hand the engineered equipment package over to `DEL-086-06` (EPC Vendor Package Review and Acceptance). Vendor document turnover routes via `DEL-086-05`.

## Verification

| Step | Verification Check |
|---|---|
| 1 | EPC SOW/Datasheet receipt logged; PKG/tag identity confirmed. |
| 2 | Vendor/EPC boundary documented; shared-stack service-split status carried as open. |
| 3 | Service mix and 508 mm/20 in LP header tie-in documented; LP stack OD flagged TBD with provenance. |
| 4 | Vendor sizing studies cite source slices; budgetary go-by explicitly excluded from authority. |
| 5 | Blowdown alignment documented; pending-source W242510 dependency flagged. |
| 6 | Vendor design basis and datasheets present and reviewed. |
| 7 | Multi-discipline interface review minutes captured. |
| 8 | Isolation and sour-service decisions traceable to DBM lines 605–611. |
| 9 | Vendor deliverable register content matches DBM line 617 list. |
| 10 | Interface mapping cross-checked against `INTERFACE_REGISTER.csv`. |
| 11 | Handover record into `DEL-086-06` exists; turnover content routed to `DEL-086-05`. |

## Records

Records expected from this procedure:

- Vendor package design basis (vendor-issued, EPC-accepted).
- Vendor package datasheet set.
- Vendor sizing study outputs (stack OD/height, tip, blower).
- Vendor deliverable register and document submittals (turnover routed via `DEL-086-05`).
- Interface alignment matrix referencing PACKAGE_REGISTER row 59 and INTERFACE_REGISTER entries.
- Open-issue log carrying CFL-01..CFL-04 from `Guidance.md` Conflict Table forward until ruled.
- Dependency declaration update: `_DEPENDENCIES.md` upstream entries for `DEL-086-01` and `DEL-086-02` should be added in a separate `dependency-extract` run (out of scope for this skill; current `_DEPENDENCIES.md` declares none — FACT).
