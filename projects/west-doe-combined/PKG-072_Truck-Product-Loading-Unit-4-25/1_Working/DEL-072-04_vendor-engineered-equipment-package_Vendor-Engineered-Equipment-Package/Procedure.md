# Procedure — DEL-072-04 Vendor Engineered Equipment Package

This procedure describes how the deliverable is **produced** (vendor engineering, design, fabrication/supply of the physical package and its design basis / datasheet set), not how the equipment is operated in service. Operation/maintenance procedures are vendor documentation handled in DEL-072-05.

## Prerequisites

- DEL-072-01 (Scope of Work) issued or at least sufficient to convey vendor scope (sibling deliverable; not formally declared as upstream in `_DEPENDENCIES.md` — DECLARED mode lists none).
- DEL-072-02 (Package Datasheet) issued or sufficient to convey package technical handoff (sibling deliverable; not formally declared).
- Access to source basis: `26020-Package_Requirements.docx` heading 26 and `DBM-Deepcut/4-25_Deepcut_DBM.md` (locations carried in `_REFERENCES.md`; deliverable-local source slices not copied — TBD).
- Resolved vendor identification (Package Vendor for PKG-072) — TBD; not stated in accessible registers at this pass.

ASSUMPTION: Upstream prerequisite list above follows the natural sequence implied by DELIVERABLE_REGISTER.csv ordering (DEL-072-01 → DEL-072-02 → DEL-072-04). `_DEPENDENCIES.md` declares no upstream edges yet; treat the list as best-effort guidance pending dependency extraction.

## Steps

### Step 1 — Ingest source basis and EPC anchor deliverables

1.1 Read the EPC Scope of Work (DEL-072-01) and Package Datasheet (DEL-072-02) outputs.
1.2 Open the source basis package requirements at `26020-Package_Requirements.docx` heading 26 (location TBD locally) and the relevant Design Basis Memorandum at `DBM-Deepcut/4-25_Deepcut_DBM.md`.
1.3 Reconcile any divergence between EPC anchors and source basis; record conflicts in the Guidance Conflict Table (re-open in this deliverable if needed).

### Step 2 — Establish package design basis

2.1 Lock the source-fixed conditions (Specification REQ-072-04-05 through REQ-072-04-11): service, design flow, outlet temperature, operating pressure, ambient and design temperature ranges, control voltage class.
2.2 Identify open values (heater capacity, MAWP, Final Flow) and assign a vendor design point for each with a documented basis. Where the source carries TBD, the vendor's chosen value becomes a PROPOSAL pending EPC review (DEL-072-06).
2.3 Identify governing standards (pressure equipment, electrical, area classification, SCR control) and record applicable clauses. **location TBD** at this pass.

### Step 3 — Engineer the equipment

3.1 Heater: size against design flow and outlet temperature; configure SCR (600 V) control with skin-temperature thermocouple override (REQ-072-04-02, REQ-072-04-03).
3.2 Scrubber: size with k = 0.35 (imperial) maximum and operating-pressure de-ration (REQ-072-04-04).
3.3 Skid: configure for the heater + scrubber arrangement and the applicable interface terminations (REQ-072-04-01, REQ-072-04-13).
3.4 Produce the vendor package design basis and the datasheet set (ART-071DC1CCEF, ART-0BA5F8C575, ART-9A43B6880A).

### Step 4 — Coordinate interfaces (package-side)

4.1 For each interface type listed in PACKAGE_REGISTER.csv row 99 / INTERFACE_REGISTER.csv (Process Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Product Loading), define the package-side termination point, format, and design data.
4.2 Submit interface package to EPC Integrator for facility-side tie-in alignment (DEL-072-03 scope).

### Step 5 — Fabricate / supply

5.1 Procure long-lead items per the vendor design.
5.2 Fabricate the skid, integrate the heater and scrubber, integrate package-side instrumentation and controls.
5.3 Confirm shipping-prep posture; note that "shipping packages to site, installation, tie-in piping, electrical tie-in etc." are explicitly **by others** (SOW-0248) and outside this deliverable's responsibility.

### Step 6 — Compile vendor turnover-ready evidence

6.1 Compile the vendor package design basis and datasheet set for handoff into DEL-072-05 (Vendor Document Turnover Package).
6.2 Submit the package and its evidence to EPC Integrator review (DEL-072-06).

## Verification

| Check | What is Verified | Where Recorded |
|---|---|---|
| Source-basis fidelity | All equipment, conditions, and control choices map back to a source slice (SOW-0246..0248) or are explicitly carried as TBD/ASSUMPTION | Vendor package design basis (ART-071DC1CCEF) |
| Datasheet-set sufficiency | Each major equipment item has a datasheet covering at least: service, design conditions, materials, control basis, applicable standards (clauses TBD where not source-derivable) | Vendor datasheet set (ART-071DC1CCEF) |
| Interface coverage | Every applicable interface type in PACKAGE_REGISTER row 99 has a package-side termination definition | Vendor interface submittal |
| Open-value disposition | Heater capacity, MAWP, and Final Flow each carry a PROPOSAL with stated basis | Vendor design basis open-items log |
| Sibling alignment | DEL-072-04 outputs are consistent with DEL-072-02 Package Datasheet | EPC review record (DEL-072-06) |

## Records

- Vendor package design basis document (ART-071DC1CCEF).
- Vendor datasheet set (ART-071DC1CCEF).
- Major included equipment evidence (ART-9A43B6880A): skid, heater, scrubber.
- Vendor engineered physical equipment package evidence (ART-0BA5F8C575).
- Interface termination submittals (one per applicable interface type).
- Open-items log capturing the disposition of source-side TBDs (heater capacity; MAWP; Final Flow) and standards-clauses TBD.

These records flow into DEL-072-05 (Vendor Document Turnover Package) and are evaluated by DEL-072-06 (EPC Vendor Package Review and Acceptance).
