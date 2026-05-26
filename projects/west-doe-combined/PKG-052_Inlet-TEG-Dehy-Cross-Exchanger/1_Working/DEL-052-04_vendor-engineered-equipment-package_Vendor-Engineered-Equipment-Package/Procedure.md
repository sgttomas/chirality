# Procedure — DEL-052-04 Vendor Engineered Equipment Package (Inlet / TEG Dehy Cross Exchanger)

## Purpose

Produce the Vendor Engineered Equipment Package for the Inlet / TEG Dehy Cross Exchanger (E-5718-1): vendor engineering and design output, fabricated equipment package, and the vendor design basis / datasheet set, executed against the EPC Scope of Work (DEL-052-01) and EPC Package Datasheet (DEL-052-02). [Source: `_CONTEXT.md` Scope; Anticipated Artifacts.]

## Prerequisites

- Issued EPC Scope of Work (sibling DEL-052-01) — TBD (sibling deliverable not yet initialized).
- Issued EPC Package Datasheet (sibling DEL-052-02), including resolution of the warm-side stream identity (Conflict C-1) — TBD.
- Accessible source basis: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Inlet / TEG Dehy Cross Exchanger" (lines 595-606).
- Package Requirements reference: `26020-Package_Requirements.docx` heading 7 (location TBD; text not extracted to markdown).
- Declared upstream dependencies: none declared during PREPARATION (see `_DEPENDENCIES.md`). ASSUMPTION: DEL-052-01 and DEL-052-02 are de-facto upstream by deliverable type even though not yet declared.

## Steps

### Step 1 — Receive and confirm EPC handoff
Receive the EPC Scope of Work (DEL-052-01) and EPC Package Datasheet (DEL-052-02). Confirm that the warm-side stream identity (Conflict C-1 in `Guidance.md`) is ruled. If not, raise the conflict to the EPC Integrator before proceeding with material selection. [Source: Specification R-5.]

### Step 2 — Vendor design basis
Produce the vendor package design basis covering process conditions (duty, flows, pressures, temperatures on both sides — TBD until EPC Package Datasheet is issued), mechanical design conditions (design pressure 9,756 kPag / 1,415 psig; design temperature 66 deg C), code and standards stack (R-7), and materials philosophy (R-8). [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 603-604.]

### Step 3 — Thermal/hydraulic design
Perform thermal/hydraulic design of the shell-and-tube exchanger (BEM as described in DBM source) against the EPC Package Datasheet duty and approach targets. Confirm the unit preserves the heat-integration intent (Specification R-6). Issue vendor thermal datasheet for EPC review. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 601-606.]

### Step 4 — Mechanical design
Perform mechanical design to ASME BPVC Section VIII Division 1 and TEMA Class R (ASSUMPTION pending EPC confirmation), including nozzles, supports, flange ratings, MDMT, and corrosion allowance (TBD). Issue vendor mechanical datasheet and general-arrangement drawing for EPC review.

### Step 5 — Materials selection and sour-service qualification
Select materials against the ruled warm-side identity (Step 1) and the sour-service envelope declared in the EPC Package Datasheet. Qualify against NACE MR0175 / ISO 15156 where applicable (ASSUMPTION). Document MTR requirements.

### Step 6 — Fabrication, NDE, and pressure test
Fabricate the exchanger under an approved Inspection and Test Plan. Perform NDE per code and the vendor ITP. Hydrostatically test to 1.3 x design pressure (ASME VIII Div 1 default; verify in vendor ITP). Stamp and complete the Manufacturer's Data Report (Form U-1). [Source: ASSUMPTION based on code R-7; location TBD.]

### Step 7 — Package assembly and shipping preparation
Complete integral package items (supports, lifting lugs, nameplates, painting, insulation/heat-tracing per EPC Package Datasheet — TBD), prepare preservation and shipping per vendor practice and EPC shipping requirements.

### Step 8 — Handover for EPC review
Issue the vendor engineered physical equipment package and the vendor design basis / datasheet set to the EPC Integrator. Vendor documents are turned over via the sibling deliverable DEL-052-05 (Vendor Document Turnover Package); EPC review and acceptance occur via DEL-052-06.

## Verification

| Step | Verification |
|---|---|
| 1 | Warm-side identity recorded in vendor datasheet revision history; conflict C-1 closed in EPC Package Datasheet. |
| 2 | Vendor package design basis approved by EPC Integrator. |
| 3 | Thermal design report shows duty, approach, and pressure drop within EPC Package Datasheet targets. |
| 4 | Mechanical design report and GA drawing endorsed by EPC Integrator; calculations available for AHJ submission. |
| 5 | MTRs and NACE/ISO compliance certificates filed. |
| 6 | Hydro test record and Form U-1 in turnover package; nameplate witnessed. |
| 7 | Pre-shipping inspection record. |
| 8 | EPC Vendor Package Review and Acceptance evidence (DEL-052-06). |

## Records

- Vendor package design basis document.
- Vendor thermal datasheet, mechanical datasheet, GA drawing, nozzle schedule.
- Material test reports; NACE/ISO certificates.
- ITP; NDE records; hydro test record; Form U-1; nameplate rubbing.
- Preservation, painting, and shipping records.
- Vendor document register entry per DEL-052-05.
[Source: `_CONTEXT.md` Anticipated Artifacts; Specification "Documentation" section.]
