# Procedure — DEL-069-05 Vendor Document Turnover Package

## Purpose

This procedure describes how to produce and maintain the Vendor Document Turnover Package for PKG-069 Mole Sieve Drier Unit (Gas) through its lifecycle (register establishment, submittal management, EPC integration review, and final turnover). Performed by the Package Vendor with EPC Integrator review per `_CONTEXT.md` ResponsibleParty.

## Prerequisites

- **Upstream inputs (currently undeclared in `_DEPENDENCIES.md`; see Guidance > Conflict Table CONF-VDT-03):**
  - DEL-069-01 Scope of Work — vendor scope basis.
  - DEL-069-02 Package Datasheet — design conditions and equipment list.
  - Workbook Packages row 73 — authoritative required vendor document list (currently **TBD**, source is binary `.xlsx`).
- **References available:**
  - `_CONTEXT.md`, `_REFERENCES.md` in this deliverable.
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — accessible source for equipment scope and design basis.
- **Project document control procedure** — TBD (not in accessible sources).
- **EPC Integrator review interface and reviewer assignments** — TBD.

## Steps

### Step 1 — Establish Vendor Document Register
1. Extract the authoritative required-document list from Workbook Packages row 73. *(Currently blocked — source is binary; treat as TBD until extracted.)*
2. Compose the Vendor Document Register with columns at minimum: document number, title, current revision, status, transmittal reference, turnover status. Project-specific column set TBD.
3. Cross-reference each register row to a tag or function in the PKG-069 equipment list (DBM equipment-by-package row 56): AC-6180-1, K-6190-1, K-6195-1, F-5910-1, F-5920-1, F-6151-1, F-6155-1, E-6170-1, V-6160-1, V-6130-1, V-6140-1, V-6150-1, V-6185-1.
4. Issue the initial register for EPC Integrator review.

### Step 2 — Issue Vendor Submittals
1. For each document on the register, the Package Vendor prepares the submittal in accordance with project document control conventions (TBD).
2. Submittals for adsorber vessels and other pressure-containing equipment include code certifications appropriate to the 900# flange rating service (DBM line 628).
3. Submittals for the adsorbent include grade confirmation (3A; silica gel layer present) and material certification (DBM lines 1269, 1270).
4. Submittals for the regeneration gas heater include datasheet aligned with the project-confirmed regeneration temperature basis (see Guidance Conflict Table CONF-VDT-01; current DBM range 450 deg F to 460 deg F).
5. Submittals for controls and protection align with the molecular-sieve dehydration controls basis (operator-initiated HMI blowdown, 50 psi/min depressurization rate limit, regen compressor automated blowdown on start, seal vent to flare, regen compressor bypass for reverse-rotation protection) (DBM line 1361).
6. Each transmittal is logged in the register; status is updated as submittals progress.

### Step 3 — EPC Integrator Review and Comment Resolution
1. EPC Integrator reviews each submittal for interface/integration consistency with the package datasheet (DEL-069-02), surrounding units (TEG dehydration upstream, BAHX/cryogenic downstream — see DBM "Interfaces" section), heat-medium loop changes (note: mole sieve regeneration gas heating is on a separate direct-fired heater, not the unified heat medium loop — DBM line 1947), and ESD/safety interfaces.
2. Comments are issued back to the vendor; revised submittals re-enter the register at incremented revision.
3. Cycle continues until each document reaches "Approved" or "Approved with Comments" status.

### Step 4 — Retain Source Vendor Document Table Rows as Artifacts
1. Where source vendor document table rows exist (per `_CONTEXT.md` Anticipated Artifacts), preserve them in the deliverable's artifact set.
2. Do not promote source rows to standalone deliverables (per `_CONTEXT.md` Notes).
3. Distinguish source-row artifacts from formal vendor submittals in the register.

### Step 5 — Compile Turnover Records
1. At mechanical completion, the vendor compiles the final turnover record set, including: as-built drawings, vendor operating and maintenance manuals, vendor data books, spare parts and consumables lists, certificates of conformity, inspection and test reports, FAT/SAT records, welding/NDE records as applicable.
2. The turnover index references each item by register document number and provides physical/logical location in the turnover binder set.
3. The register is updated so that every required document has turnover status = "Turned Over" before mechanical completion certification.

### Step 6 — Hand Off to EPC Integrator Review & Acceptance (DEL-069-06)
1. The completed turnover package is transmitted to the EPC Integrator as the input to DEL-069-06 (EPC Vendor Package Review and Acceptance).
2. Any items remaining open at handover (TBC values, deferred submittals, deferred certifications) are listed in a punch list within the turnover index.

## Verification

| Verification | Method |
|---|---|
| Register completeness vs. Workbook Packages row 73 | Document control audit (blocked until row 73 is extracted — currently TBD). |
| Equipment scope completeness | Tag-by-tag check against DBM equipment-by-package row 56. |
| Adsorbent grade and protective media | Material certificate review for 3A grade + silica gel layer. |
| Regeneration loop temperature basis | Heater datasheet review confirms a single value consistent with the project-ruled basis (Guidance CONF-VDT-01). |
| Controls philosophy | SAFE chart / cause-and-effect review against DBM molecular-sieve controls row. |
| Turnover-set usability | Operations/maintenance walkthrough of the turnover index at mechanical completion. |
| No standalone duplicate deliverables | Artifact-set audit — source rows preserved as artifacts only. |

## Records

The following records are produced and retained:

- Final Vendor Document Register (issued for turnover).
- Approved vendor submittals (drawings, datasheets, calculations, manuals, certifications, test reports).
- Source vendor document table rows preserved as artifacts.
- Turnover index and turnover binders (physical and/or electronic).
- Punch list of items open at turnover (if any).
- Transmittal log and review-comment register (close-out evidence).

Specific record numbering and storage locations are **TBD** pending project document control procedure.
