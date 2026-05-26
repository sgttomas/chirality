# Procedure — Vendor Engineered Equipment Package (DEL-091-04)

## Purpose

Operational procedure for **producing** the vendor-engineered equipment package deliverable — i.e., how the Package Vendor and EPC Integrator interact to advance the package from EPC handoff to integration-ready vendor package. The procedure for **operating** the physical equipment is a downstream vendor manual and is out of scope here (it is normally part of `DEL-091-05_vendor-document-turnover-package`).

## Prerequisites

- EPC Scope of Work (`DEL-091-01`) issued.
- EPC Package Datasheet (`DEL-091-02`) issued (binding sizing and interface basis).
- Locally accessible references in `_REFERENCES.md` reviewed:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (3-25 facility design basis).
  - PROJECT_DECOMP Gate 7 snapshot (`PACKAGE_REGISTER.csv` row 84; `DELIVERABLE_REGISTER.csv` row 471).
- Source slices not yet locally accessible (must be resolved before requirement freeze): `26020-Package_Requirements.docx` heading 44; `26020-Packages_Interfaces_4_export.xlsx` row 84; `26020-03-PT-RFQ-18-002-Tank Farm Pumps.docx`. (Status: `location TBD`.)
- Declared upstream dependencies: none declared (per `_DEPENDENCIES.md`); update via `TASK + dependency-extract` once binding edges are confirmed.

## Steps

1. **Confirm package boundary and equipment list.** Reconcile the Datasheet Attributes table against PACKAGE_REGISTER row 84 and the EPC Package Datasheet. Open variances in the Conflict Table (`Guidance.md`).
2. **Issue vendor package design basis.** Vendor produces design basis grounded in EPC Package Datasheet, DBM 3-25, and EPC SOW. Include sizing rationale for water transfer pumps (R3, R4), sour-condensate pumps, sweetening feed pumps (R5), and drain pump.
3. **Issue vendor pump datasheets and major-component datasheets.** Include rated flow/head, NPSHr, motor sizing, materials of construction, area classification, seal plan, control philosophy.
4. **Coordinate interface termination points.** For each interface type listed in `Datasheet.md` Construction, define the package termination, owner of next pipe/cable/structure, and tie-in elevation/coordinate. Submit interface drawings to EPC Integrator.
5. **Vendor design review.** Internal vendor IDR, then submit to EPC Integrator for integration review under `DEL-091-06`. Resolve comments; update the design basis and datasheets accordingly.
6. **Fabrication and FAT.** Fabricate per approved design; execute factory acceptance testing per the vendor ITP. Record test results and any nonconformances.
7. **Vendor documentation turnover.** Hand off vendor document register, submittals, and turnover records under `DEL-091-05`.
8. **Shipment and field handoff.** Ship the physical package to site; field handoff to construction (`DEL-091-03`) and EPC Integrator acceptance (`DEL-091-06`).
9. **Update deliverable-local state.** When the vendor design basis and pump datasheets are first issued, propose `_STATUS.md` advance from `INITIALIZED` to the appropriate downstream state via the human-authorized state change pathway. `TASK` runs do not unilaterally advance state past `INITIALIZED`.

## Verification

- Step 1: Equipment list matches PACKAGE_REGISTER row 84 — verified by document compare.
- Step 2: Design basis cites EPC Package Datasheet and DBM 3-25 — verified by reference audit.
- Step 3: Pump datasheets cover all four pump services and the drain pump; performance values traceable to source — verified by traceability matrix.
- Step 4: Each interface type in `Datasheet.md` Construction has one defined termination — verified by interface matrix.
- Step 5: EPC integration review comments dispositioned — verified under `DEL-091-06`.
- Step 6: FAT acceptance per ITP — verified by FAT reports.
- Step 7: Vendor document register complete — verified under `DEL-091-05`.

## Records

- Vendor package design basis document.
- Vendor pump datasheets (per service) and major-component datasheets.
- Interface drawings / interface matrix.
- IDR minutes and EPC integration review comment log.
- FAT reports, ITP records, nonconformance reports.
- Vendor document register and turnover records (handed to `DEL-091-05`).
- EPC acceptance evidence (handed to `DEL-091-06`).
