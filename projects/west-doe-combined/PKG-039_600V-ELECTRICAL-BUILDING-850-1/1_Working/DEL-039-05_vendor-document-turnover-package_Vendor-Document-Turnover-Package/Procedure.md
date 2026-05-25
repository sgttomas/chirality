# Procedure: DEL-039-05_vendor-document-turnover-package

## Purpose

Define the working procedure for producing the Vendor Document Turnover Package for `DEL-039-05_vendor-document-turnover-package`, covering the vendor document register, vendor document submittals, source-required vendor documentation carried as artifacts where available, and turnover records for `PKG-039`. Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05`.

## Prerequisites

| Prerequisite | Basis | Status |
|---|---|---|
| Accepted Gate 7 PROJECT_DECOMP snapshot | Decomposition basis for package, deliverable, artifact, interface, and objective registers. | Available |
| Deliverable context files | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, and `_SEMANTIC.md` define local identity and constraints. | Available |
| Package and deliverable register rows | `PACKAGE_REGISTER.csv` row `PKG-039`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05`. | Available |
| Artifact register rows | `ART-A64A8A25DC` identifies the vendor documentation gap evidence; `ART-3910447327`, `ART-AA4BFB86C9`, and `ART-0156F0196A` identify related EPC review/acceptance artifacts. | Available |
| Interface register rows | Twelve `PKG-039` interface rows identify the interface topics requiring vendor-document coverage or explicit `TBD`. | Available |
| Electrical-building DBM source basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section and related grounding/cabling/receptacle sections. | Available |
| Project-wide vendor document control standard | Required for final numbering, revision, transmittal, native-file, and review-cycle rules. | TBD |
| Package-specific vendor document table | Required for final mandatory document list. | TBD; `ARTIFACT_REGISTER.csv` row `ART-A64A8A25DC` records the source gap |

No upstream or downstream dependencies were declared during PREPARATION. Source: `_DEPENDENCIES.md`.

## Steps

1. Confirm deliverable identity.
   - Verify that the working folder is for `DEL-039-05_vendor-document-turnover-package`.
   - Confirm parent package `PKG-039`, package name `600V ELECTRICAL BUILDING (850-1)`, discipline `Electrical`, and responsible party assignment.
   - Sources: `_CONTEXT.md`; `PACKAGE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv`.

2. Establish the vendor document register shell.
   - Create or update a register index for vendor documents, submittals, and turnover records.
   - Include traceability to package, interface topic, source basis, review status, and turnover status where supported.
   - Mark document numbering, revision code, transmittal number, required native-file format, and review-cycle fields as `TBD` until the project document-control source is identified.

3. Populate register coverage from decomposition artifacts.
   - Include the vendor document register evidence row `ART-A64A8A25DC`.
   - Reference related `DEL-039-06` review/acceptance artifacts as downstream review evidence, not as vendor-produced documents in this deliverable.
   - Sources: `ARTIFACT_REGISTER.csv` rows for `PKG-039`.

4. Populate interface coverage.
   - For each `PKG-039` interface type, identify the vendor document or turnover record expected to carry package-side data.
   - Interface topics to cover are Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports.
   - If a vendor document is not yet known for an interface topic, record `TBD` rather than inventing a document title or number.

5. Check DBM electrical-building technical coverage.
   - Confirm that the register or submittal set addresses the DBM electrical-building features applicable to the actually-installed 850-1 subset: prefabricated/modular building basis, climate-controlled HVAC sized n + 1, bottom-entry power cables, elevated building on piles, TECK/ACIC wiring, EMT for adjacent equipment, outdoor GFI receptacle, and door/removable-transom provisions for equipment removal.
   - Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section.

6. Assemble vendor document submittals.
   - Attach or reference each vendor document submittal listed in the register.
   - Confirm each submittal has a register entry and a source/status basis.
   - Where the source-required document list is unavailable, carry the missing item as a `TBD` gap tied to `ART-A64A8A25DC`.

7. Assemble turnover records.
   - Compile final certified vendor data, completed test/inspection records, operating and maintenance documentation, shipped-loose/spares records, and as-built/marked-up content where available.
   - Treat acceptance criteria and checklist fields as `TBD` until the governing turnover or vendor document control source is available.
   - Coordinate handoff evidence with `DEL-039-06` without moving EPC review evidence into this vendor deliverable.

8. Perform cross-document consistency review.
   - Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and this procedure use the same package identity, deliverable identity, interface list, and source-gap statements.
   - Confirm unsupported values remain `TBD` and inferences remain labelled as **ASSUMPTION**.
   - Confirm the conflict table in `Guidance.md` captures the vendor-document requirements gap.

9. Prepare for EPC Integrator review.
   - Submit the register, submittals, and turnover record set for EPC Integrator interface/integration review.
   - Ensure review comments, acceptance checklist evidence, and factory/shop test acceptance evidence are routed to `DEL-039-06`.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity check | Deliverable ID, parent package, package name, discipline, and responsible party match `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, and `DELIVERABLE_REGISTER.csv`. |
| Four-document consistency | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` use consistent scope, terminology, interface list, and source-gap treatment. |
| Register existence | Vendor document register is present or explicitly marked `TBD` with source-gap reference to `ART-A64A8A25DC`. |
| Interface coverage | Each of the twelve `PKG-039` interface topics has a document/submittal/turnover reference or explicit `TBD`. |
| DBM coverage | Applicable DBM electrical-building features are represented in the register/submittal set or marked `TBD`. |
| Document-control gap handling | Numbering, revision, transmittal, and review-cycle mechanics are not invented. |
| Review boundary | EPC review and acceptance evidence is referenced as `DEL-039-06` scope, not included as Package Vendor output in this deliverable. |

## Records

The completed turnover package should retain or reference:

- Vendor document register for `PKG-039`.
- Vendor document submittals listed in the register.
- Source-required vendor documentation rows where available.
- Interface coverage matrix or equivalent register fields for all twelve applicable `PKG-039` interface topics.
- Turnover records for final vendor data, test/inspection records, O&M/manual content, shipped-loose/spares records, and marked-up/as-built content where available.
- `TBD`/gap list for unresolved project document-control and package-specific vendor-document requirements.
- EPC Integrator review handoff reference to `DEL-039-06_epc-vendor-package-review-and-acceptance`.
