# Procedure — DEL-089-06 EPC Vendor Package Review and Acceptance (PKG-089)

## Purpose

Operational steps for the EPC Integrator to review, accept, and turn over the PKG-089 vendor pig-receiver package, producing the four anticipated artifacts identified in `_CONTEXT.md`.

## Prerequisites

- Vendor package issued for review (drawings, datasheets, calculations, ITP, certificates).
- EPC SOW and project QA/QC plan available to reviewers (`location TBD` for slice access).
- Package Datasheet (this deliverable's `Datasheet.md`) and Specification (`Specification.md`) accepted as the review datum.
- Construction Work Package (CWP) reference available (referenced by `_CONTEXT.md`; not locally accessible — `location TBD`).
- Access to authoritative DBM slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-04.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` at INITIALIZED state (TBD; may be extracted later via `TASK + dependency-extract`).

## Steps

### Step 1 — Initialize the vendor document review log

1. Inventory all vendor documents received. Record document ID, revision, date, and type.
2. Establish a row per document in the **Vendor Document Review Log**.
3. Identify reviewer assignments by discipline (mechanical, materials, controls/ESDV, NDE/QA).

### Step 2 — Review against the Specification

For each document, verify alignment with the Specification requirements (R-1 through R-5). For each finding, record:

- Requirement reference (e.g., R-2.3)
- Observation
- Disposition (Approved / Approved with Comments / Revise and Resubmit / Rejected) — **ASSUMPTION** on class names per project QA plan
- Hold point or RFI ID where applicable

Key DBM-anchored configuration checks (Source: DBM 3-25 SEC-04):

- Single combined three-phase receiver (not split/duplicate)
- Structural steel, non-enclosed skid
- Sweet-gas purge tie-in
- HP flare vent tie-in
- Inlet ESDV: full-port, piggable, position transmitters

### Step 3 — Confirm open DBM items as hold points

Document each open item as a hold point on the **Package Acceptance Checklist**:

- HP-01: Receiver size (DBM: TBD)
- HP-02: Delivery-point ESDV shutdown pressure (DBM: TBC; 635 psig at inlet separator ESDV is reference only)
- HP-03: Final inlet pipeline configuration (DBM: to be confirmed during detailed design)
- HP-04: Inlet temperature reconciliation (DBM separator basis 8.3 deg C; receiver-specific value TBD)

### Step 4 — Witness/Review test and inspection evidence

1. Review pressure-test records against applicable code (R-4.1; CSA Z662 applicability `ASSUMPTION: likely applicable`).
2. Review NDE/NDT records, MTRs, weld maps; perform PMI verification where applicable to sour service.
3. Witness or review ESDV functional and stroke tests; verify position-transmitter calibration records (R-4.3).
4. Record evidence pointers in the **Test/Inspection Evidence** binder index.

### Step 5 — Integration walk-down

1. Verify tie-in geometry vs. EPC isometrics (R-3.1, R-3.2).
2. Verify purge and flare header connectivity (line numbers, ratings, faces).
3. Verify lease-boundary first-flange handoff vs. Doe field pipeline contractor scope.
4. Record observations and punch items.

### Step 6 — Compile turnover evidence

1. Assemble the **Turnover Evidence** package: as-builts, vendor manuals, spare parts list, lubrication schedule (if applicable), training records, punch-list closure log.
2. Confirm completeness against the project turnover index (`location TBD`).

### Step 7 — Issue acceptance proposal to human authority

1. Compile the **Package Acceptance Checklist** with all hold points either closed or carried with explicit conditional language.
2. Route the checklist plus the four artifacts to the responsible operating authority for sign-off (K-AUTH-1).
3. Record the human ruling and date in `MEMORY.md` (deliverable-local) once issued.

## Verification

| Check | Method |
|---|---|
| Spec R-2.x configuration matches DBM 3-25 SEC-04 | Cross-walk: Spec → vendor GA → DBM table |
| All hold points (HP-01 through HP-04) carried explicitly | Acceptance Checklist row audit |
| Pressure/NDE/ESDV evidence complete | Binder index review |
| Turnover binder complete | Turnover index audit |
| Human authority countersignature present | Signature audit |

## Records

- Vendor document review log (with per-document dispositions and review evidence)
- Package acceptance checklist (with hold-point disposition and signatures)
- Test/inspection evidence binder (hydrotest, NDE, ESDV stroke, calibration)
- Turnover evidence package (as-builts, manuals, spares, training, punch-list closure)
- Conflict Table entries (`Guidance.md`) closed by human ruling, captured in `MEMORY.md`
