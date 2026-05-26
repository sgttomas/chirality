# Procedure — DEL-056-04 Vendor Engineered Equipment Package

**Pass:** P1/P2 | **DECOMP_VARIANT:** PROJECT | **Skill:** four-documents

## Purpose

This procedure describes the steps to **produce** the Vendor Engineered Equipment Package for Inlet Separators 4-25 (PKG-056), from receipt of EPC anchor documents through vendor delivery and EPC integration handoff. It also covers procedural points for **using/operating** the package at vendor factory acceptance (final-product checks before EPC integration).

## Prerequisites

- **Upstream deliverable inputs (declared in `_DEPENDENCIES.md` as: none declared; ASSUMPTION on usage):**
  - DEL-056-01 Scope of Work (EPC Integrator) — accepted version.
  - DEL-056-02 Package Datasheet (EPC Integrator) — accepted version, including package interface requirements matrix.
- **Reference materials available:**
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - `_Sources/26020-Package_Requirements.docx` package heading 11 (clause-level slice location TBD)
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 68 (location TBD)
- **Open items to be resolved or carried as TBD/CONFLICT during execution:**
  - CONF-01..CONF-08 from `Guidance.md` Conflict Table.
- **Sour-service materials, coating procedures (Devchem 253), and pressure-vessel code regime confirmed against SEC-04 of the project DBM (clause-level slice TBD).**

## Steps

### Step 1 — Receipt and review of EPC anchor documents

1.1 Receive accepted DEL-056-01 (Scope of Work) and DEL-056-02 (Package Datasheet) from EPC Integrator.
1.2 Cross-walk EPC Package Datasheet against this deliverable's `Specification.md` requirements R1-R12.
1.3 Raise clarifications via EPC Integrator (DEL-056-06 channel) for any divergence; do not silently reconcile.

### Step 2 — Vendor package design basis

2.1 Draft vendor package design basis referencing:
   - Current authority separator quantity (two installed + plot for third) per CONF-01 ruling (carry as TBD if unruled).
   - Sour-service regime per SEC-04 (location TBD).
   - Pressure ratings R4.1-R4.3.
2.2 Submit design basis for EPC Integrator review (DEL-056-06).

### Step 3 — Vendor datasheet set

3.1 Produce vessel datasheets (9 ft ID x 40 ft S/S nominal; Devchem 253 internal coating; sour service; manway, drainage, venting, inspection per R2).
3.2 Produce internals datasheets (manually adjustable weir; vertical mesh/vane mist eliminator) per R3.
3.3 Produce inlet PCV datasheets per R5 (>=2 parallel, balanced globe, hardened trim, dP <= 5 psid at design).
3.4 Produce produced-water LCV datasheets per R6 (>=2 parallel per package).
3.5 Produce liquid outlet heater datasheet per R7, leaving outlet temperature target, duty, and medium TBD pending EPC process simulation closure.
3.6 Produce skid-edge inlet isolation and outlet manual isolation datasheets per R5.2/R5.3.
3.7 Produce methanol injection and drive-gas metering datasheets per R9.
3.8 Produce package building datasheet per R11 (self-framing, instrumentation enclosure; ASSUMPTION on configuration from MPFF narrative).
3.9 Issue vendor datasheet set for EPC Integrator review.

### Step 4 — Process and instrumentation alignment

4.1 Align vendor process datasheet against EPC Package Datasheet (DEL-056-02) process basis.
4.2 Confirm interface points per R12 with EPC Integrator (gas overhead, heated hydrocarbon liquid outlet to MPFF, LP fuel gas purge/drive, HP flare, methanol, closed hydrocarbon drain, produced-water handling, package controls).
4.3 Document outstanding TBD/TBC items (heater duty/medium, methanol capacities, HIPPS requirement, slug capacity precise value, ESDV shutdown setpoints).

### Step 5 — Fabrication and FAT

5.1 Manufacture per vendor datasheet set and accepted design basis (shop-built per Deepcut DBM tag table).
5.2 Apply Devchem 253 internal coating per qualified procedure; record film thickness and holiday-test results.
5.3 Pressure-test vessels per applicable code; document.
5.4 Factory acceptance test (FAT):
   - Verify mist eliminator and weir configuration matches accepted internals.
   - Verify PCV trim, count, and dP envelope per R5.1.
   - Verify LCV count per R6.1.
   - Verify isolation configuration per R5.2/R5.3.
   - Verify package building integration per R11.
   - Witness by EPC Integrator (per DEL-056-06).

### Step 6 — Delivery and handoff

6.1 Deliver vendor engineered physical equipment package to site per EPC schedule.
6.2 Submit vendor design basis and datasheet set as part of vendor documentation per DEL-056-05.
6.3 Support EPC Integrator review and acceptance (DEL-056-06).

### Step 7 — Operating/use checks at handoff (final-product verification)

7.1 Confirm package isolation philosophy per R10: full unit isolation possible while other unit operates.
7.2 Confirm drive gas metering per R9.2: separate meter per package upstream of plant inlet meters.
7.3 Confirm ESDV interfaces per R8 (facility inlet ESDV is interface, not vendor scope; shutdown setpoints per CONF-03 ruling or carry TBD).
7.4 Confirm methanol injection layout per R9.1, with capacities TBC.

## Verification

| Step | Verification |
|---|---|
| 1 | EPC anchor document acceptance receipts; clarification log. |
| 2 | EPC Integrator review of vendor design basis (DEL-056-06). |
| 3 | Vendor datasheet set issued and EPC-reviewed. |
| 4 | Interface alignment record against DEL-056-02. |
| 5 | Pressure-test certificates; coating QA records; FAT report countersigned by EPC. |
| 6 | Delivery receipts; DEL-056-05 turnover entries. |
| 7 | Handoff verification checklist countersigned by EPC Integrator. |

## Records

- Vendor package design basis (signed)
- Vendor datasheet set (signed)
- Interface alignment record vs. DEL-056-02
- Pressure-test certificates
- Coating QA records (Devchem 253 film thickness, holiday test)
- FAT report
- Clarification log against EPC anchor documents
- Delivery receipts and vendor documentation submittals (feeding DEL-056-05)
- Open TBD/TBC log for items deferred to detailed engineering (heater duty/medium, methanol capacities, HIPPS, slug capacity precise value, ESDV setpoints, separator quantity ruling)
