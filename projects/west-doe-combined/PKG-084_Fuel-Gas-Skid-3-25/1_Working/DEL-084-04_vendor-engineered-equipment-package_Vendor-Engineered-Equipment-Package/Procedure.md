# Procedure: DEL-084-04 — Vendor Engineered Equipment Package (Fuel Gas Skid)

> Pass 1/2 draft. Procedure describes the steps to **produce** this deliverable
> (the engineered and supplied vendor package). Operating procedure for the installed
> skid is downstream and out of scope here; relevant operating considerations are
> captured in `Guidance.md`.

## Purpose

Define the bounded steps the Package Vendor (with EPC Integrator oversight) follows
to engineer, design, fabricate, FAT, and turn over the fuel-gas skid package for
`PKG-084`, satisfying the requirements in `Specification.md` and grounded in the
source basis in `Datasheet.md`.

## Prerequisites

- Accepted upstream decomposition snapshot:
  `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Accessible source materials:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- Sibling deliverables (ASSUMPTION — not declared in `_DEPENDENCIES.md`):
  - `DEL-084-01` Scope of Work (defines vendor scope envelope)
  - `DEL-084-02` Package Datasheet (defines EPC-side performance / interface basis)
- Open items to be resolved before final issue:
  - CONFLICT C-01 (package location reconciliation), C-02 (buyback inclusion),
    C-03 (slop-tank destination) — see `Guidance.md`.
  - `26020-Package_Requirements.docx` heading 37 — parse and reconcile against this draft.

## Steps

### Step 1 — Receive and Confirm Vendor Inputs
- Receive EPC Scope of Work (`DEL-084-01`) and EPC Package Datasheet (`DEL-084-02`).
- Confirm scope boundaries (battery limits, tie-in points, supply pressures, demand
  profile) against `Specification.md` R-FG-01 and R-FG-02.
- Identify and log any inconsistencies for EPC Integrator ruling. (Where source basis
  remains `TBC`/`TBD`, request closure or accept the open item with documented
  conservatism.)

### Step 2 — Vendor Design Basis
- Issue a vendor package design basis document covering: service definition, sizing
  basis (R-FG-01), pressure/source basis (R-FG-02), environmental basis (R-FG-06),
  material governance (R-FG-07), code applicability, and assumed interfaces.
- Cross-reference each design value back to the EPC inputs and DBM source slices
  cited in `Datasheet.md` / `Specification.md`.

### Step 3 — Equipment and Controls Design
- Heater (R-FG-03): SCR-controlled electric resistance heater sized for max
  sales-compressor discharge pressure and winter ambient buyback gas conditions; include
  skin-temperature thermocouple override and gas-outlet-temperature control.
- Scrubber (R-FG-04): designed for system design flow at design operating pressure,
  K factor max 0.35 Imperial with operating-pressure derating; drain to designated
  slop tank per resolution of CONFLICT C-03.
- Regulators and filtration (R-FG-05): 2 x 100% main regulators with individual
  isolation and outlet pressure-test connection; pilot-isolation provisions where
  pilots are external; quick-acting internally sensing start-gas regulator; local
  particulate filter at emergency generator supply.
- Generator supply (R-FG-02.3, R-FG-01.3): supply pressure < 66 psig; piping/vessels
  accommodate simultaneous start-gas (3.6 MMSCFD for 30 s) and design operating cases.
- Hazard provisions (R-FG-07.2): purge / vent / analyzer layout reflecting methyl
  mercaptan toxicity and odour considerations.

### Step 4 — Skid Integration
- General arrangement and footprint that fits the EPC layout envelope (envelope `TBD`).
- Structural / foundation loading information for civil interface.
- Winterization, heat tracing, insulation, building / enclosure (as applicable) per
  R-FG-06.
- Electrical area classification, grounding, and instrumentation per project basis
  (`location TBD`).

### Step 5 — Documentation Package
- Produce P&IDs, PFDs, cause-and-effect / functional description, datasheets, GA
  drawings, structural drawings, and instrument index.
- Compile material test reports (MTRs), weld records, NDE records, hydrotest records,
  and code stamping documentation.
- Prepare turnover index sized for downstream `DEL-084-05` consumption (ASSUMPTION).

### Step 6 — Factory Acceptance Test (FAT)
- Execute FAT against the FAT plan referenced in `Specification.md` "Verification".
- Verify R-FG-03 (heater skin-T override, outlet-T control, stagnant-gas behaviour),
  R-FG-04 (scrubber drain), R-FG-05 (regulator sparing, isolation, start-gas response).
- Generate FAT report; capture punchlist for closure prior to shipment.

### Step 7 — EPC Integrator Review
- Submit completed package and documentation to `DEL-084-06` (EPC Vendor Package
  Review and Acceptance) for review and acceptance prior to shipment.
- Resolve EPC comments; reissue documentation as needed.

### Step 8 — Shipment and Turnover
- Ship the engineered skid in accordance with packing / preservation requirements
  (preservation requirements `TBD`).
- Transfer turnover documentation to `DEL-084-05` (Vendor Document Turnover Package).

## Verification

| Step | Verification Check |
|---|---|
| 1 | Recorded EPC inputs match Scope of Work and Package Datasheet revisions in effect; open items list maintained |
| 2 | Vendor design basis is approved by EPC Integrator |
| 3 | Calculations exist and are signed for each requirement R-FG-03 through R-FG-05 |
| 4 | GA, foundation loading, electrical area, and winterization drawings are issued |
| 5 | Document index complete; MTRs and NDE records assembled and indexed |
| 6 | FAT report signed; punchlist either closed or carried to site with EPC concurrence |
| 7 | EPC acceptance documented in `DEL-084-06` evidence record |
| 8 | Turnover document index transferred to `DEL-084-05`; shipment release issued |

## Records

The procedure shall produce, at minimum:

- Vendor package design basis document.
- Datasheet set (heater, scrubber, regulators, instrumentation, electrical, controls,
  structural).
- P&IDs / PFDs / general arrangement / structural drawings.
- Calculations (pressure design, heater duty, scrubber sizing, regulator sizing,
  PSV sizing).
- MTRs, weld records, NDE records, hydrotest records, code stamping documentation.
- FAT plan and FAT report.
- EPC review correspondence and acceptance evidence (input to `DEL-084-06`).
- Shipment release and preservation records.
- Turnover document index (input to `DEL-084-05`).

Records not enumerated in the accessible source set are labeled `ASSUMPTION` based on
standard vendor-package convention and shall be reconciled with
`26020-Package_Requirements.docx` heading 37 once parsed.
