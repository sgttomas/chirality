# Procedure — DEL-055-04 Vendor Engineered Equipment Package (LP Flare KO Drum, 4-25)

> Operational procedure for **producing** the vendor engineered equipment
> package deliverable. Steps describe how the Package Vendor and the EPC
> Integrator move from accepted upstream documents (DEL-055-01 Scope of Work,
> DEL-055-02 Package Datasheet) to a fabricated, documented, and
> ready-for-acceptance package. Procedure for **operating** the LP flare KO
> drum in service is not in scope of this deliverable; it is captured by
> facility operations documentation outside PKG-055.

## Prerequisites

| Item | Source / Owner |
|---|---|
| Accepted Scope of Work for PKG-055 | DEL-055-01 (sibling deliverable) |
| Accepted Package Datasheet (process / mechanical / I&C battery limits) | DEL-055-02 (sibling deliverable) |
| Accepted 4-25 Deepcut DBM source slices for flare system, equipment list, and module list | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| PROJECT_DECOMP Gate 7 final-published snapshot | `_REFERENCES.md` |
| Package register entry for PKG-055 (interface types, scope split) | `PACKAGE_REGISTER.csv` row PKG-055 |
| Vendor RFQ package issued by EPC (covering this deliverable's scope) | EPC Integrator; routing TBD |
| Identified Package Vendor with sour-service flare KO experience | Procurement; TBD |
| EPC Integrator area classification and plot-plan basis sufficient to bound skid envelope | EPC Integrator; basis TBD |

If any of `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, or `_STATUS.md`
is missing or inconsistent with the live PROJECT_DECOMP snapshot, halt and
escalate before issuing the vendor RFQ.

## Steps

### Step 1 — Confirm package boundaries
1. Confirm Scope of Work (DEL-055-01) and Package Datasheet (DEL-055-02) are
   accepted and current relative to the Gate 7 PROJECT_DECOMP snapshot.
2. Re-validate the interface type list against PACKAGE_REGISTER row PKG-055:
   Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical
   Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control
   Cabling; Maintenance Access; Structural / Foundations / Supports.
3. Resolve conflict items in `Guidance.md` Conflict Table where they affect
   RFQ content (drum/pump quantity, EHT scope split, sour-service directive).

### Step 2 — Issue vendor RFQ and select vendor
1. EPC Integrator issues an RFQ containing the accepted Package Datasheet,
   relevant DBM extracts, applicable codes/standards (`Specification.md`
   Standards), and the documentation deliverable list (`Specification.md`
   Documentation).
2. Bidders return technical proposals; EPC Integrator evaluates against
   `Specification.md` REQ-055-04-* and the Package Datasheet.
3. Award the vendor purchase order. Record the awarded vendor identity in
   `MEMORY.md` (if/when created).

### Step 3 — Vendor design development
1. Vendor finalizes process datasheet for `V-3900-1` and `P-3900-1` against
   the accepted Package Datasheet and any updated relief load data.
2. Vendor performs mechanical design calculations for the drum (pressure,
   temperature, MDMT, corrosion allowance, nozzle loads, supports).
3. Vendor selects materials consistent with sour-service `ASSUMPTION`
   (NACE MR0175 / ISO 15156) until or unless overridden by EPC.
4. Vendor produces general arrangement, skid layout, P&ID extract, I&C
   schedules, and EHT/insulation design (per Specification REQ-055-04-14
   scope split).
5. Vendor issues design package for EPC review at agreed hold points.

### Step 4 — Pressure-vessel registration
1. Vendor submits the drum design to the BC Safety Authority (or equivalent
   jurisdiction) for CRN registration (`ASSUMPTION`: ASME Section VIII Div. 1
   with CRN — confirm at design freeze).
2. Vendor incorporates registrar comments and obtains CRN.

### Step 5 — Fabrication of module 390-1
1. Vendor fabricates the drum and pump skid in shop per the accepted design
   set. [`4-25_Deepcut_DBM.md` line 2783]
2. Vendor applies welding, NDE, PWHT, and hardness controls consistent with
   the sour-service `ASSUMPTION` and applicable code.
3. Vendor applies external protective coatings and insulation/EHT per the
   accepted design.
4. Vendor mounts pump, piping, junction boxes, and interface terminations on
   the skid per the accepted general arrangement.

### Step 6 — Inspection and test (shop)
1. Vendor executes the accepted Inspection and Test Plan (ITP).
2. Vendor performs hydrostatic / pneumatic pressure test of the drum and
   piping within vendor scope.
3. Vendor performs pump performance test and any required NPSH verification.
4. Vendor performs visual / NDE coverage per code and ITP.
5. EPC Integrator (or third-party inspector on EPC's behalf) witnesses
   nominated ITP items.

### Step 7 — Documentation turnover preparation
1. Vendor compiles the documentation set listed in `Specification.md` for the
   turnover package (handed off through DEL-055-05).
2. Vendor delivers preliminary O&M, ITP records, material certificates, NDE
   records, CRN, and design calculation set.
3. Hand-off of finalized turnover content is owned by DEL-055-05.

### Step 8 — Shipment and site receipt
1. Vendor packages the module for transport with shipping-loose items
   identified.
2. Vendor coordinates shipment with EPC Integrator.
3. EPC Integrator receives, inspects-on-receipt, and records any transit
   damage.

### Step 9 — EPC Vendor Package Review and Acceptance
1. EPC Integrator executes the acceptance review owned by DEL-055-06 against
   the requirements in `Specification.md` and the documentation actually
   produced.
2. Outstanding items (`TBD`, `ASSUMPTION`, Conflict Table entries) are
   resolved or carried forward with explicit dispositions.
3. Acceptance is recorded; deliverable transitions out of vendor ownership.

## Verification

| Step | Verification |
|---|---|
| 1 | Documented confirmation that DEL-055-01 and DEL-055-02 are current vs Gate 7 PROJECT_DECOMP; Conflict Table dispositions logged. |
| 2 | RFQ package issued; bid evaluation matrix and award decision recorded. |
| 3 | Vendor design package reviewed and stamped; hold-point sign-offs by EPC. |
| 4 | CRN certificate received and on file. |
| 5 | Shop fabrication records: weld logs, NDE coverage reports, coating reports, EHT installation records. |
| 6 | Hydrotest / pneumatic test reports; pump performance curve; ITP closeout matrix. |
| 7 | Turnover documentation index reviewed by DEL-055-05 owner. |
| 8 | Shipment manifest and on-receipt inspection report. |
| 9 | DEL-055-06 acceptance record; package state transitions per EPC governance. |

## Records

Records produced through this procedure (handed off via DEL-055-05 for
turnover and reviewed via DEL-055-06):

- Approved Package Vendor design package (drum + pump datasheets,
  calculations, GA drawings, P&ID extract, I&C, EHT design).
- CRN certificate (drum).
- Material certificates, mill test reports, NACE MR0175 / ISO 15156 compliance
  documentation (sour-service `ASSUMPTION` until ruled).
- Weld and NDE records.
- Inspection and Test Plan with sign-offs.
- Hydrotest / pneumatic test certificates.
- Pump performance test record.
- Coating, insulation, and EHT records.
- Shipping manifest and on-receipt inspection record.
- O&M manual draft (final O&M owned by DEL-055-05).
- Spare parts list / commissioning spares list.
- Conflict Table dispositions (closing out items raised in `Guidance.md`).
