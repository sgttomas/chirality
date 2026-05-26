# Procedure — Vendor Engineered Equipment Package (DEL-076-04)

> Operational procedure for **producing** the vendor-engineered Lube Oil Supply utility package as a deliverable (vendor-side engineering and supply path) with EPC Integrator review. Steps for **operating** the package (oil transfer, day-tank refill, used-oil handling) are deferred to vendor O&M manuals at turnover.
>
> Source-grounded against DBM-Deepcut SEC-08 / SEC-05 / SEC-02 / SEC-16 and the deliverable's `_CONTEXT.md` / `_DEPENDENCIES.md`. Operational details not in the DBM are marked `TBD`.

## Purpose

Produce, fabricate, and deliver the PKG-076 vendor-engineered Lube Oil Supply utility package such that the EPC Integrator can accept it for installation, tie-in, and commissioning at the 04-25 facility, with reliable heated bulk storage of compressor cylinder lube oil (400 bbl) and compressor crank-case lube oil (200 bbl) and transfer pumping (P-9240-1, P-9250-1) to compressor frame day tanks.

## Prerequisites

| Prerequisite | Source |
|---|---|
| Accepted EPC Scope of Work (DEL-076-01) | DELIVERABLE_REGISTER (PKG-076 deliverable rows) |
| Accepted EPC Package Datasheet (DEL-076-02) | DELIVERABLE_REGISTER (PKG-076 deliverable rows) |
| Accepted Design Basis Memorandum SEC-08 §"Lube Oil Storage and Pump Basis" | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2059–L2072 |
| Accepted Packages register row for PKG-076 (line-item basis) | DBM SEC-16 L2602 |
| Site design ambient envelope confirmed: −40 °C to +35 °C | DBM SEC-02 L198 |
| Compressor-vendor cylinder-oil and crank-case-oil grade rulings (per compressor service) | DBM SEC-08 L2072 — **TBC**; vendor should request these before final tank sizing if multi-grade build is being considered |
| Authoritative reference: `26020-Package_Requirements.docx` h.30 | `_REFERENCES.md` (location TBD — not locally parseable) |
| Declared upstream dependencies in `_DEPENDENCIES.md` | None declared at PREPARATION; vendor should request explicit upstream-dependency declaration before detailed design starts |

## Steps

### Step 1 — Vendor onboarding and brief
1.1 Receive and acknowledge EPC SOW (DEL-076-01) and EPC Package Datasheet (DEL-076-02).
1.2 Confirm scope split per Specification §Scope; raise Conflict C-005 if used-oil collection is in scope.
1.3 Confirm service performance targets per Specification R-1.

### Step 2 — Service design
2.1 Confirm storage capacities: cylinder oil 400 bbl, crank-case oil 200 bbl (R-2.1, R-2.2). Reference: DBM SEC-08 L2067, L2069.
2.2 Confirm heated-storage method and design service temperature (R-1.2, R-2.6 — currently TBD). Reference: DBM SEC-08 L1835, L2059.
2.3 Confirm pump duty: intermittent fill of compressor frame day tanks as needed (R-1.3). Reference: DBM SEC-08 L2068, L2070.
2.4 Confirm pump sparing (Conflict C-002) with EPC: 1 × 100% (DBM line-item basis) vs. vendor-proposed 2 × 100%.
2.5 Confirm initial-build oil-grade strategy (Conflict C-004) with EPC and (where available) compressor manufacturers.
2.6 Document open items C-003 (tank tags) and C-005 (additional storage) and resolve with EPC.

### Step 3 — Mechanical equipment design
3.1 Issue equipment datasheets for each item in Specification R-2 (cylinder tank, crank-case tank, P-9240-1, P-9250-1, heating system, instrumentation).
3.2 Confirm pump selection (type, drive, materials, mechanical seal arrangement) against viscosity, suction conditions, and heat-traced piping route (R-2.5).
3.3 Confirm tank construction standard (R-2.1, R-2.2): API 650 atmospheric heated tank is the assumption; alternative selections require EPC concurrence. Reference: SEC-16 L2556, L2557 analogs.
3.4 Confirm tank instrumentation and alarms (R-2.6): level transmitter, high-/low-level alarms, vent, fill, drain, sample, heating control.
3.5 Confirm secondary containment basis (R-3.3) with EPC civil design.

### Step 4 — Package / skid engineering
4.1 Develop storage-tank-area layout for both tanks and pump skid(s).
4.2 Apply minimum spacing criteria (DBM SEC-02 §2.5).
4.3 Apply cold-climate provisions (winterization, heat tracing on suction/discharge piping, insulation, motor selection) per DBM SEC-02 L198.
4.4 Coordinate Module / area placement with EPC layout designer; tanks are basis-located "in the storage tank area" (DBM SEC-08 L2067, L2069).
4.5 Coordinate distribution-piping interface to compressor frame day tanks (R-4.1, R-4.2) — scope-split to be confirmed with EPC.

### Step 5 — Fabrication and shop assembly
5.1 Fabricate tanks to API 650 (ASSUMPTION — confirm against `26020-Package_Requirements.docx` h.30).
5.2 Fabricate and FAT-test pump skid(s) (controls, instrumentation, motor).
5.3 Register any pressure equipment (filter housings, etc.) for BC CRN if applicable (ASSUMPTION — confirm against EPC site standards).
5.4 Perform shop hydrotest and NDE per ITP for pressure parts; tank hydrotest per API 650 / project ITP.
5.5 Conduct shop FAT for controls, instrumentation, and pumps.

### Step 6 — Documentation and turnover preparation
6.1 Assemble vendor document set per Specification §Documentation.
6.2 Coordinate with DEL-076-05 (Vendor Document Turnover Package) for register and submittal flow.
6.3 Prepare cause-and-effect for tank level controls and pump permissives (R-4.5).

### Step 7 — Shipping
7.1 Ship tanks per EPC modularization plan (likely site-erected for 400 bbl / 200 bbl class — confirm with EPC).
7.2 Ship pump skid(s) shop-assembled where feasible.

### Step 8 — EPC integration review and acceptance handoff
8.1 Support EPC Integrator review under DEL-076-06.
8.2 Provide commissioning support: tank fill, heating commissioning, transfer-pump duty trial to a representative compressor frame day tank.
8.3 Hand over O&M manuals (oil-grade compatibility, changeout, cleaning procedures).

## Verification

| Step | Verification |
|---|---|
| Step 2 | EPC review of service-design narrative against DBM SEC-08 envelope; resolution of C-002, C-003, C-004, C-005. |
| Step 3 | EPC review of equipment datasheets against Specification R-2. |
| Step 4 | EPC review of skid/tank GAs, spacing, and distribution-piping interface. |
| Step 5 | Witness/hold points per ITP; FAT acceptance; tank hydrotest acceptance. |
| Step 6 | DEL-076-05 vendor document register completion. |
| Step 8 | DEL-076-06 acceptance evidence (review log, acceptance checklist, test/inspection evidence, turnover evidence). |

## Records

- Vendor design narrative and equipment datasheet revisions (issued for review, issued for fabrication, as-built)
- Tank hydrotest reports and NDE records (pressure parts)
- FAT reports (pump skid, controls)
- Vendor document register (linked to DEL-076-05)
- Cause-and-effect issued and approved
- Commissioning records (tank fill, heating commissioning, transfer-pump duty trial)
- EPC acceptance evidence (linked to DEL-076-06)
