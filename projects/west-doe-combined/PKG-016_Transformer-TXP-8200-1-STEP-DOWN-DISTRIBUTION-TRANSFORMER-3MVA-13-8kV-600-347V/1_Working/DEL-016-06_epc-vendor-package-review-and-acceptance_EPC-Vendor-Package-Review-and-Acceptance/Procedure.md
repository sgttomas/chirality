# Procedure: DEL-016-06_epc-vendor-package-review-and-acceptance

## Purpose

Produce the EPC Integrator's review and acceptance evidence (vendor document review log, package acceptance checklist, test/inspection evidence record, turnover evidence record) for the PKG-016 vendor package (13.8 kV / 600 V, 3 MVA distribution transformer TXP-8200-1), against the EPC Scope of Work (DEL-016-01), the EPC Package Datasheet (DEL-016-02), and the EPC Construction Work Package (DEL-016-03), with input from the Vendor Engineered Equipment Package (DEL-016-04) and the Vendor Document Turnover Package (DEL-016-05).

## Prerequisites

### EPC reference set available

- DEL-016-01 EPC Scope of Work — issued (or current working draft frozen for acceptance use).
- DEL-016-02 EPC Package Datasheet — issued.
- DEL-016-03 EPC Construction Work Package — issued.

### Vendor inputs available

- DEL-016-04 Vendor Engineered Equipment Package — vendor design basis, datasheets, and physical package data.
- DEL-016-05 Vendor Document Turnover Package — vendor document register, submittals, and turnover records.

### Decomposition and source references

- Gate 7 PROJECT_DECOMP snapshot (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (System Voltages; Incoming Power and Transformers; Area Classification; 600V MCC and Standby Power; Electrical Buildings, Raceways…; site basis).
- Workbook Packages row 18.

### Declared dependencies

- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md`.
- Declared downstream dependencies: none recorded in `_DEPENDENCIES.md`.
- Practical sequencing: DEL-016-01/-02/-03 issuance must precede acceptance against them; DEL-016-04 and DEL-016-05 vendor outputs must be received before the corresponding line items can be dispositioned.

## Steps

1. **Establish the acceptance file index.** Create the four artifacts in this deliverable folder (or referenced subfolders): `Vendor_Document_Review_Log`, `Package_Acceptance_Checklist`, `Test_Inspection_Evidence`, `Turnover_Evidence`. Record their location in this deliverable's working notes.
2. **Build the vendor document review log.**
   - Import the DEL-016-05 vendor document register as the master list.
   - For each register entry, record receipt status (received / outstanding), reviewer, review date, and per-document disposition (accept / accept-with-comment / reject-and-resubmit).
   - Record gaps as REJECT-AND-RESUBMIT entries against the missing document(s).
3. **Build the package acceptance checklist.**
   - Seed line items from `INTERFACE_REGISTER.csv` rows for `PKG-016`: Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports.
   - Seed additional line items from Specification REQ-016-06-05 through REQ-016-06-11 (facility-electrical conformance, area classification, grounding, raceway/maintenance access).
   - Seed a line item per CT-016-06-NN conflict from `Guidance.md` for explicit resolution.
   - Disposition each line item with traceability back to the EPC reference clause and/or source slice it was compared against.
4. **Compile test/inspection evidence.**
   - Receive vendor factory test reports for the transformer (routine, type, and special tests as applicable to the governing standard once cited).
   - Verify nameplate against DEL-016-02 primary/secondary voltage, capacity, impedance, vector group (where stated), and any auxiliary data.
   - Record site inspection observations (anchorage to foundation drawing; bushing access; radiator/oil clearance for oil-filled units; cabinet heating; gasketing for cold-weather basis).
   - Capture energization checks where applicable (insulation resistance, ratio, polarity) as either witnessed-and-passed or deferred to commissioning with reason.
5. **Compile turnover evidence.**
   - Confirm installation, operation, and maintenance documentation per DEL-016-05.
   - Confirm spare-parts list per DEL-016-05.
   - Confirm protective-device settings basis where in vendor scope, or formally record that settings are EPC/commissioning scope.
   - Confirm any vendor cold-weather declaration meets the -40 deg C minimum ambient site basis (or exceeds it).
6. **Reconcile and surface conflicts.**
   - Update `Guidance.md` Conflict Table when new disagreements emerge between vendor data and the EPC reference set or source materials. Do not silently choose between conflicting sources.
   - Where information is missing rather than conflicting, mark the affected line item `TBD` and identify the source document needed.
7. **Produce a closure summary.**
   - For each requirement REQ-016-06-NN in `Specification.md`, record VERIFIED / PARTIAL / TBD and cite the artifact line that supports the determination.
   - Record overall integration-acceptance state (e.g., "Accepted for handoff", "Accepted with comments", "Acceptance pending vendor resubmittal"). This is a record of EPC Integrator disposition, not a binding approval (K-AUTH-1).

## Verification

| Check | What confirms it |
|---|---|
| Four acceptance artifacts exist and are populated | File index in `{DELIVERABLE_PATH}` |
| Every PKG-016 interface row has at least one disposition line item | Cross-reference checklist line items against `INTERFACE_REGISTER.csv` for `PKG-016` |
| Every Specification requirement (REQ-016-06-01 … -16) has a recorded verification outcome | Closure summary (Step 7) |
| Every `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`-derived requirement (system voltages, incoming power, area classification, site basis, raceways) is checked against vendor data | Test/inspection evidence and acceptance checklist entries |
| Vendor document register (DEL-016-05) is fully accounted for | Vendor document review log reconciliation |
| Each Conflict Table entry (CT-016-06-NN) has either a recorded resolution or remains TBD with the responsible party identified | `Guidance.md` Conflict Table and acceptance checklist line items |
| No binding approval or certification language appears in any acceptance artifact | Self-check before closure summary publication |

## Records

- Vendor document review log (full per-document disposition with date and reviewer).
- Package acceptance checklist (interface and requirement-level dispositions with traceability).
- Test/inspection evidence record (factory tests, nameplate verification, site inspection observations, energization checks where applicable).
- Turnover evidence record (IO&M documentation receipt, spare-parts list receipt, protective-device settings basis disposition, cold-weather conformance record).
- Closure summary (per-requirement verification state and overall EPC disposition).
- TASK run records under `_run_records/` for each invocation of this deliverable's drafting/enrichment cycles.
