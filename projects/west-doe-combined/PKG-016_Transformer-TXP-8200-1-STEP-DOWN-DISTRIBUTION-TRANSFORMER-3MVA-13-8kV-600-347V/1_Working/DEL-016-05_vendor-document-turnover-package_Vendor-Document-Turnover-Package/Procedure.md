# Procedure: DEL-016-05_vendor-document-turnover-package

## Purpose

Produce and turn over the controlled vendor document register, the vendor document submittals, the source-required vendor documentation, and the turnover records for `PKG-016` (transformer TXP-8200-1, 13.8 kV / 600 V, 3 MVA step-down distribution transformer), with EPC Integrator interface/integration review.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are present in the deliverable folder.
- The Gate 7 published PROJECT_DECOMP snapshot is accessible.
- `DEL-016-01_scope-of-work` and `DEL-016-02_package-datasheet` are available as anchoring inputs (EPC Integrator deliverables). Status: not declared as upstream dependencies for `DEL-016-05`; treated as advisory anchors.
- `DEL-016-04_vendor-engineered-equipment-package` is the engineering/design source feeding the vendor document content. Status: not declared as upstream dependency; treated as advisory.
- Project document control standard and project turnover standard. Status: TBD; not present in accessible references.
- Source slice of `_Sources/26020-Package_Requirements.docx` for `PKG-016`. Status: TBD; not yet extracted.

## Steps

1. **Initialize the vendor document register.**
   - Create the register controlling artifact for `PKG-016` (TXP-8200-1).
   - Field set: TBD pending the project document control standard. Use the source-required list (when extracted from `26020-Package_Requirements.docx`) and the interface set in `INTERFACE_REGISTER.csv` for `PKG-016` as initial seeding.

2. **Enumerate source-required vendor documents.**
   - When the package-specific slice of `_Sources/26020-Package_Requirements.docx` is extracted, populate the register with the required document IDs and titles.
   - Until then, mark these rows TBD and surface as a missing input.

3. **Map declared interfaces to required submittals.**
   - For each `PKG-016` row in `INTERFACE_REGISTER.csv` (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports), confirm at least one register row covers it; flag gaps.

4. **Produce vendor submittals.**
   - Vendor engineering output (from `DEL-016-04`) is packaged into the submittals listed in the register.
   - Each submittal carries unique document identity and revision.
   - Submittal mechanics (status codes, transmittal IDs, review cycle days): TBD pending project document control standard.

5. **Submit through the EPC review workflow.**
   - Each submittal is routed to the EPC Integrator for interface/integration review.
   - Review evidence is recorded under `DEL-016-06_epc-vendor-package-review-and-acceptance`, not under this deliverable.

6. **Compile turnover records.**
   - Compile the turnover record set per the project turnover standard (record types TBD).
   - Likely set for a medium-voltage step-down distribution transformer, pending confirmation: factory routine test reports (ratio, polarity, no-load loss, load loss, impedance, insulation resistance), factory type test reports (dielectric/impulse where applicable), nameplate data, as-built marked drawings, spares list, oil test certificate (if liquid-filled) or dry-type insulation certificate, warranty/maintenance documentation, operating and maintenance manual. Treat this likely set as ASSUMPTION until the turnover standard is added to `_REFERENCES.md`.

7. **Issue the controlled deliverable.**
   - Issue the register, submittals, source-required vendor documentation, and turnover records as the deliverable for `PKG-016`.
   - Confirm consistency with `DEL-016-01` SOW and `DEL-016-02` Package Datasheet, including transformer service identity (13.8 kV / 600 V / 3 MVA, HRG-grounded LV system).

## Verification

| Check | How |
|---|---|
| Register exists and is current | Inspect register controlling artifact. |
| Register field set matches the project document control standard | Compare against the standard once available; otherwise record TBD. |
| Every declared `PKG-016` interface has at least one submittal | Trace `INTERFACE_REGISTER.csv` rows to register rows. |
| All source-required vendor documents present | Compare register against the extracted `PKG-016` slice of `26020-Package_Requirements.docx`. |
| All submittals carry EPC review evidence | Cross-reference with `DEL-016-06`. |
| Turnover record set complete | Compare against the project turnover standard. |
| Consistency with SOW and Package Datasheet | Compare against `DEL-016-01` and `DEL-016-02`; check transformer service identity. |
| Individual source document rows treated as artifacts, not deliverables | Confirm no sibling deliverables were created for source document rows. |

## Records

- Vendor document register (controlled artifact).
- Vendor document submittals (one per controlled document, all revisions).
- Source-required vendor documentation (as enumerated by the source basis).
- Turnover records (set; types per the project turnover standard, currently TBD).
- Run records: `_run_records/TASK_RUN_*.md` in this deliverable folder.

All records are governed by `ARTIFACT_REGISTER.csv` rows for `DEL-016-05_vendor-document-turnover-package`.
