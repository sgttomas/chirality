# Specification — Construction Work Package (DEL-074-03)

> Normative requirements that the as-delivered Construction Work Package (CWP) for PKG-074 (Caustic Treating — NGL Mercaptan Removal) must satisfy. Requirements are derived from the decomposition `_CONTEXT.md` scope statement, the EPC Construction Work Package artifact convention, and the source basis in the West Doe 04-25 Deep Cut DBM. Items not anchored to source are labelled `ASSUMPTION` or `TBD`.

## Scope

### In scope
- Specification of the EPC-Integrator-issued Construction Work Package documenting how PKG-074 (the non-regenerative NGL caustic mercaptan treating unit) is to be physically installed, built, inspected, turned over, and tied into the larger 04-25 / 03-25 facility systems.
- The installation and tie-in workface plan and the construction interface and turnover checklist that the `_CONTEXT.md` lists as anticipated artifacts inside this CWP.

### Out of scope
- Process design and detailed engineering of the caustic treating unit (covered by `DEL-074-02_package-datasheet` and `DEL-074-04_vendor-engineered-equipment-package`).
- Vendor document submittal and turnover register (covered by `DEL-074-05_vendor-document-turnover-package`).
- Operational procedures for the running unit (covered by Procedure documents downstream of operations readiness, not by this CWP).

## Requirements

### R-CWP-1 — Document set
The CWP shall contain, at minimum, the three artifacts identified in `_CONTEXT.md`:
- a Construction Work Package narrative,
- an installation and tie-in workface plan, and
- a construction interface and turnover checklist.

Verification: documentary review — `_CONTEXT.md` artifact list.

### R-CWP-2 — Package identification and traceability
The CWP shall identify the package by `DeliverableID` (`DEL-074-03_construction-work-package`), parent `PKG-074`, package name (Caustic Treating — NGL Mercaptan Removal), the covered scope items (`SOW-0059`..`SOW-0062`), and the accepted decomposition snapshot (`GATE-07_Final_Published_2026-05-24`).

Verification: identification block present and matches `_CONTEXT.md`.

### R-CWP-3 — Source-grounded equipment list
The CWP shall list the equipment to be installed and shall be consistent with the equipment basis in the 04-25 DBM "NGL Mercaptan Treating Equipment and Utilities" section (caustic NGL contactor; 2 × 100 % caustic outlet filters; pressurized caustic drain drum; water-wash equipment; 1 × 400 bbl fresh caustic tank, 1 × 400 bbl spent caustic tank, 1 × 400 bbl DSO tank; associated pumps; MTU building).

Verification: equipment list cross-referenced to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "NGL Mercaptan Treating Equipment and Utilities".

### R-CWP-4 — Building and material constraints
The CWP shall reflect that:
- caustic-containing equipment is installed indoors inside the Mercaptan Treating Unit (MTU) building (freeze/crystallization risk);
- no aluminum is to be installed in the MTU caustic building;
- insulation cladding/straps in caustic exposure areas are stainless steel;
- caustic storage tanks use polymer or other caustic-compatible material (final selection TBD);
- the MTU building shall contain water safety showers, with shower activation producing a discrete control-room alert.

Verification: construction-issue drawings, material take-offs, and inspection checklists reflect these constraints.

Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "NGL Mercaptan Treating Equipment and Utilities" (lines ~1552, ~1566).

### R-CWP-5 — Tie-in inventory
The CWP shall identify, at minimum, the following construction tie-ins:
- process inlet from the de-ethanizer outlet path (cooled C3+ NGL);
- treated-NGL outlet to NGL filtration / water wash / molecular-sieve dehydration;
- rich caustic outlet to caustic heating and spent-caustic handling;
- spent caustic and DSO truck-out connections;
- vapour tie-in from spent caustic and DSO tanks to the incinerator header located at the 03-25 facility;
- LP fuel gas (blanket and incinerator dilution);
- process water make-up;
- produced water drain;
- HP and LP electrical, instrument air, heat tracing, and instrumentation tie-ins.

Each tie-in shall be identified by tag (TBD where not yet assigned), unit boundary, and the design conditions carried in `DEL-074-02_package-datasheet`.

Verification: tie-in list reconciled against piping P&IDs, electrical one-lines, and utility distribution schematics.

Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Current-Scope NGL Mercaptan Treating" and § "Incinerator Interface".

### R-CWP-6 — Cross-facility tie (03-25 incinerator)
The CWP shall include the cross-facility vapour tie from the 04-25 MTU spent-caustic and DSO tanks to the 03-25 incinerator and shall identify operational-responsibility and shared-facility coordination items, recognizing that "supplemental fuel gas rate, incinerator flow basis, and shared-facility operational responsibility remain TBD" in the available basis.

Verification: cross-facility interface sheet included; open items carried into the construction interface and turnover checklist.

Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Incinerator Interface".

### R-CWP-7 — Construction interface and turnover checklist
The CWP shall provide a construction interface and turnover checklist that:
- enumerates every tie-in identified in R-CWP-5/R-CWP-6 with construction completion, mechanical completion, and pre-commissioning sign-off lines;
- enumerates safety-critical items (safety showers, control-room alert, fire and gas devices, ESD interfaces, no-aluminum verification);
- enumerates documentation handoff to `DEL-074-05_vendor-document-turnover-package` and `DEL-074-06_epc-vendor-package-review-and-acceptance`.

Verification: checklist completeness review against R-CWP-3 through R-CWP-6.

### R-CWP-8 — Installation and tie-in workface plan
The CWP shall provide a workface plan that breaks the installation into work packages with prerequisite logic (e.g., MTU building enclosure prior to caustic-equipment installation, tank foundations and erection prior to vapour-tie-in, hydrotest prior to chemical introduction).

Verification: workface package list with dependency diagram or precedence table.

ASSUMPTION: The detailed work-package decomposition (count, duration, crew sizing) is determined by the EPC execution plan and is `TBD` at this gate.

### R-CWP-9 — Winter / cold-weather execution provisions
The CWP shall reflect the -40 °C winter design basis: freeze protection during construction, winterization of tanks/lines before chemical introduction, and module-delivery / lift-window constraints driven by winter operation.

Verification: winterization plan section present.

Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696 (winter operation and -40 °C basis).

### R-CWP-10 — Hazard, ESD, and detection coordination
The CWP shall coordinate construction and pre-commissioning of fire and gas, LEL, H2S, methyl-mercaptan, ESD, and unit-shutdown interfaces with BPCS, remote I/O, package controls, and HAZOP/SIL outcomes. Detector quantity, tag list, set points, voting logic, and placement remain `TBD` until detailed design and safety studies close.

Verification: detection and ESD construction punch list issued for HAZOP/SIL closeout.

Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` § "LEL, H2S, Methyl Mercaptan, and Fire Detection" (line ~836-838).

### R-CWP-11 — Inspection and testing
The CWP shall identify required inspections and tests, including: piping NDE per applicable code (governing code TBD), hydrotest pressures consistent with design pressures in R-CWP-3, electrical loop checks, instrument calibration, safety-shower activation and control-room-alert verification, leak testing, and PSV verification.

Verification: ITP (Inspection and Test Plan) present and reconciled to the equipment list and tie-in inventory.

### R-CWP-12 — Turnover
The CWP shall define turnover (mechanical completion → care-custody-and-control transfer) requirements, including punch-list classes, sign-off authorities (EPC Integrator and downstream operator), and the handoff into `DEL-074-06_epc-vendor-package-review-and-acceptance`.

Verification: turnover protocol section present.

## Standards

| Standard | Application | Status |
|---|---|---|
| Owner construction execution / EPC contract specifications | Governing CWP form and content | Specific document TBD (not present in accessible source set) |
| API and CSA piping / pressure-equipment codes | Hydrotest, NDE, PSV | location TBD; specific code revisions to be confirmed at detailed engineering |
| API 2510 | LPG-spacing descriptor retained from DBM context only; not a governing CWP construction standard for this NGL caustic unit | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 274 |
| HAZOP / SIL outputs | Govern fire & gas, ESD, and shutdown construction completion (per R-CWP-10) | Outputs not yet produced; TBD |
| Provincial OH&S construction requirements (BC) | Govern site construction practice | location TBD |

## Verification (summary)

| Requirement | Verification approach |
|---|---|
| R-CWP-1 | Document existence check |
| R-CWP-2 | Identification-block review |
| R-CWP-3 | Equipment list cross-walked to DBM SEC-07 |
| R-CWP-4 | Drawings, MTOs, and inspection sheets reviewed |
| R-CWP-5 | P&ID and one-line reconciliation |
| R-CWP-6 | Cross-facility interface sheet present; open items tracked |
| R-CWP-7 | Checklist completeness audit |
| R-CWP-8 | Workface plan present with precedence |
| R-CWP-9 | Winterization plan present |
| R-CWP-10 | Detection/ESD construction punch list issued |
| R-CWP-11 | ITP present and reconciled |
| R-CWP-12 | Turnover protocol section present |

## Documentation (anticipated artifacts inside this deliverable)

- Construction Work Package (governing narrative).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Inspection and Test Plan (ITP). [ASSUMPTION — standard CWP companion]
- Punch-list register and turnover certificates. [ASSUMPTION — standard CWP companion]
