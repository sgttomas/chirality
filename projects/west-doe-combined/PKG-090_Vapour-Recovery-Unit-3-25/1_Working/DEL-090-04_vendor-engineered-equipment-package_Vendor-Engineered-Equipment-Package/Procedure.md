# Procedure — DEL-090-04 Vendor Engineered Equipment Package (PKG-090 Vapour Recovery Unit 3-25)

> Operational view. This Procedure describes the steps to **produce** and turn over the Vendor Engineered Equipment Package artifact set, plus high-level use/operate prerequisites that the vendor must reflect in its design. Source-grounded where possible; inferences are labeled `ASSUMPTION`; unresolved items are `TBD`.

## Purpose

Define the bounded steps by which the Package Vendor executes engineering, design, fabrication/supply, and physical equipment delivery for the PKG-090 VRU, and the steps by which the EPC Integrator verifies and accepts that scope. This Procedure realizes the requirements in `Specification.md` and reflects the guidance in `Guidance.md` for PKG-090. (Sources: `_CONTEXT.md`; `Specification.md`; `Guidance.md`; PACKAGE_REGISTER.csv row 100; DELIVERABLE_REGISTER.csv row 567.)

## Prerequisites

### Declared upstream dependencies

`_DEPENDENCIES.md` declares no upstream dependencies during PREPARATION. The following deliverables are nonetheless required by `_CONTEXT.md` and the decomposition as **anchoring inputs** (not yet promoted to declared dependencies — `ASSUMPTION` pending dependency-extract):

- `DEL-090-01` — EPC Scope of Work (anchor input). (`_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv row 564.)
- `DEL-090-02` — EPC Package Datasheet (anchor input). (`_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv row 565.)

### Required references

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 PROJECT_DECOMP snapshot, in particular `PACKAGE_REGISTER.csv` row 100 and `DELIVERABLE_REGISTER.csv` row 567.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — §"Vapour Recovery" L434–L438, tables L523–L597, L20–L40, L66.
- `26020-Package_Requirements.docx` package heading 43 — required but not locally readable this pass (`location TBD`).
- `26020-Packages_Interfaces_4_export.xlsx` — required for interface register cross-check (`location TBD`).
- `Bid Docs/Budgetary/26020-03-PT-RFQ-12-001_VRU_1_R0.docx` — RFQ basis (`location TBD`).

### Personnel / capability prerequisites

- Package Vendor with sour-service VRU rotary-vane compressor experience and Canadian regulatory / CRN capability (`ASSUMPTION`).
- EPC Integrator engineering lead with mechanical, process, electrical/I&C, and HSE oversight.

## Steps

### Step 1 — Confirm package basis

1. Receive and review `DEL-090-01` Scope of Work and `DEL-090-02` Package Datasheet from the EPC Integrator. (`_CONTEXT.md` Notes.)
2. Reconcile package basis against `PACKAGE_REGISTER.csv` row 100 (configuration, model, driver, service, building, interface set). Record any discrepancies as Conflict Table entries in `Guidance.md`.
3. Confirm the SCA-002 discharge-routing basis (VRU discharge to 04-25 SOC suction; no local 03-25 SOC). (DBM L36, L66, L436.)

### Step 2 — Develop vendor design basis

1. Produce vendor design basis covering: configuration (2 x 100% lead-lag, single building), sour-service materials approach, recycle valve sizing case (100% flow at minimum driver speed and lowest discharge pressure), make-up/blanket regulator sizing case (maximum turndown), and LP flare bypass arrangement. (REQ-090-04-001..007.)
2. Capture VRU-specific inlet composition, pressures, temperatures, and flows. Values currently `TBD` until pulled from `DEL-090-02` Package Datasheet and `26020-Package_Requirements.docx` heading 43.
3. Document recycle / control-valve fail action explicitly. Carry inlet-compressor analogue (fail-open with final TBC) only as `ASSUMPTION` until VRU-specific basis is confirmed. (DBM L334.)

### Step 3 — Engineer the package

1. Mechanical: compressor selection (Ro-Flo 12S/212M two-stage rotary vane), packaging, skid structural design, vessel and piping design for sour service. (REQ-090-04-002, -013.)
2. Process: P&IDs, line list, recycle/bypass/make-up arrangement, instrument schedule. (REQ-090-04-004..007.)
3. Electrical: 200 HP VFD motor specification, power distribution within package, area classification (`TBD` pending classification study). (REQ-090-04-003.)
4. I&C: package PLC, local HMI, safety devices, F&G interfaces. Interface boundaries per PACKAGE_REGISTER.csv row 100. (REQ-090-04-010.)
5. Building: single building housing both trains; HVAC, F&G coverage, lighting, noise/vibration, maintenance access — all sized for both trains simultaneously even though only one runs in normal lead-lag. (`Guidance.md` Considerations.)

### Step 4 — Interface coordination with EPC Integrator

1. Establish package boundary battery limits for each interface type listed in `REQ-090-04-010` (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports).
2. Submit interface data to the EPC Integrator for inclusion in the project interface register. Cross-check against `26020-Packages_Interfaces_4_export.xlsx` (`location TBD`).
3. Resolve any conflict between vendor-standard package layout and EPC site/plot constraints prior to fabrication release.

### Step 5 — Produce vendor documentation set

1. Produce the documentation list required by `26020-Package_Requirements.docx` heading 43 (`location TBD` — full list to be confirmed). Expected items (`ASSUMPTION` based on package-vendor industry practice): GA drawings, P&IDs, datasheets (compressor, motor, vessels, valves, instruments), sizing calculations, electrical/I&C drawings, ITP, FAT/SAT plans, O&M manuals, spare parts list, certifications (CRN, NACE/ISO 15156 traceability), QA/QC records.
2. Issue documentation per the project document-control workflow. Vendor turnover scope (delivery of the final accepted document set to the EPC Integrator) is governed separately under `DEL-090-05`. (DELIVERABLE_REGISTER.csv row 568.)

### Step 6 — Fabricate and FAT

1. Fabricate per approved-for-construction vendor drawings, applying sour-service material traceability and CRN/registration where applicable.
2. Execute FAT against the agreed ITP, including compressor performance demonstration at 100% per train, turndown demonstration, recycle valve operation across the sizing case, and instrumentation/safety device function tests.
3. Document FAT results in the vendor documentation set.

### Step 7 — Ship and field receipt

1. Apply modularization / shipping splits per vendor standard (`ASSUMPTION`; explicit VRU modularization plan not located in accessible DBM slice — DBM L294 is for inlet compressor packages).
2. EPC Integrator receives the package on site. Construction activities (installation, tie-ins, commissioning) are not in vendor scope and are covered under `DEL-090-03` and `DEL-090-06`. (`Specification.md` Out of scope.)

### Step 8 — EPC Integrator package review and acceptance hand-off

1. Provide the engineered package and documentation set into `DEL-090-06` EPC Vendor Package Review and Acceptance for integration-side acceptance. (DELIVERABLE_REGISTER.csv row 569 — `ASSUMPTION` pending row confirmation; deliverable cross-referenced in `_CONTEXT.md`/`Specification.md`.)
2. Address any acceptance findings before declaring the deliverable complete.

## Verification

| Step | Verification |
|---|---|
| Step 1 | Sign-off that `DEL-090-01` and `DEL-090-02` are received and reconciled against `PACKAGE_REGISTER.csv` row 100. |
| Step 2 | Vendor design basis issued and reviewed by EPC Integrator engineering lead. |
| Step 3 | Discipline drawings/calculations issued for review (IFR); comments resolved before IFC release. |
| Step 4 | Interface register entries closed for each interface type in `REQ-090-04-010`. |
| Step 5 | Documentation register cross-checked against `26020-Package_Requirements.docx` heading 43 (`location TBD`). |
| Step 6 | FAT report signed by vendor and EPC witness; performance and turndown demonstrated; recycle/bypass/make-up function verified. |
| Step 7 | Receipt inspection complete; transportation damage report (if any) raised. |
| Step 8 | `DEL-090-06` acceptance record issued. |

## Records

The following records are produced and retained:

- Vendor design basis document set.
- Vendor package datasheet set (compressor, motor, vessels, valves, instruments, building services).
- Approved-for-construction drawings (GA, P&ID, electrical, I&C, structural, HVAC).
- Sizing calculations (recycle valve, blanket regulator, vessel/PSV, electrical loads, HVAC).
- Material traceability records (sour-service / NACE / ISO 15156) — `ASSUMPTION` for code citation pending source confirmation.
- Pressure equipment registration evidence (e.g., CRN) — `ASSUMPTION` for code citation pending source confirmation.
- FAT and ITP records.
- Vendor O&M manuals, spare parts list, certifications.
- Interface register entries for each interface in `REQ-090-04-010`.
- Conflict Table updates (in `Guidance.md`) for any unresolved source ambiguities.

Final documentation turnover to the EPC Integrator is governed by `DEL-090-05 Vendor Document Turnover Package`. Final integration acceptance is governed by `DEL-090-06 EPC Vendor Package Review and Acceptance`.
