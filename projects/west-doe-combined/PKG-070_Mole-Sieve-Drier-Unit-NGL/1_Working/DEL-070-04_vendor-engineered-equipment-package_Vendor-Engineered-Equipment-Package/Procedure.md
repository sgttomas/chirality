# Procedure — DEL-070-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, NGL)

This procedure describes how the Package Vendor produces the equipment package and how the EPC Integrator integrates and accepts it. Operating procedures for the running unit are out of scope here — they will be authored by Operations against the as-built vendor package documentation.

## Purpose

To take the EPC Integrator's Scope of Work (`DEL-070-01`) and Package Datasheet (`DEL-070-02`) and produce a fabricated, tested, documented NGL Mole Sieve Drier Unit equipment package ready for EPC integration review (`DEL-070-06`) and vendor document turnover (`DEL-070-05`).

## Prerequisites

- `DEL-070-01` Scope of Work accepted (declared upstream dependency — none declared in `_DEPENDENCIES.md` during PREPARATION; the EPC SoW relationship is project-level and carried as ASSUMPTION until written into the dependency view).
- `DEL-070-02` Package Datasheet accepted (same status as above — ASSUMPTION pending dependency-view update).
- Available references:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-07 lines 1574-1623 (process basis).
  - `_Sources/26020-Package_Requirements.docx`, package heading 24 (binary, location TBD for slice-level citation).
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` in this deliverable folder.
- Open TBCs from the basis acknowledged and tracked (cycle times, regen-gas source tie-in, pressure envelopes, governing outlet water spec).

## Steps

### Stage A — Vendor engineering

| Step | Action | Verification | Records |
|---|---|---|---|
| A1 | Receive `DEL-070-02` Package Datasheet from EPC Integrator | Datasheet rev controlled; TBC items listed | Receipt log |
| A2 | Produce vendor process design basis (cycle times R-3.5; adsorbent selection R-1.12/R-1.13; sulphur stewardship R-1.14) | EPC Integrator process review | Vendor design basis document |
| A3 | Produce vessel, exchanger, filter, scrubber, aerial-cooler datasheets (R-2.1-R-2.5) | EPC Integrator mechanical review | Datasheets, rev-controlled |
| A4 | Produce skid GA and P&ID within vendor battery limit (tag set per R-2.6) | EPC Integrator P&ID alignment vs. `DEL-070-02` | GA, P&IDs |
| A5 | Produce instrument schedule and analyzer specification (R-4.1-R-4.3) | EPC Integrator I&C review | I&C schedule |
| A6 | Issue jurisdictional registration packages for pressure-retaining components | ABSA/BCSA acknowledgement (jurisdiction confirmed via `DEL-070-02`) | Registration certificates |

### Stage B — Vendor fabrication and FAT

| Step | Action | Verification | Records |
|---|---|---|---|
| B1 | Fabricate vessels, exchangers, scrubber, cooler, skid steel | Mill certs; weld procedures; NDE per code | MTRs, NDE reports |
| B2 | Hydrotest pressure-retaining components | Hydrotest acceptance per code | Hydrotest reports |
| B3 | Assemble skid; install instruments and analyzers | Loop checks at FAT | FAT report |
| B4 | Adsorbent supply and packaging | Adsorbent supplier certificate; lifecycle warranty per R-5.1 | Adsorbent certificates |
| B5 | Issue FAT report and shipping documentation | EPC Integrator FAT witness (TBC) | FAT dossier, shipping docs |

### Stage C — Site receipt and integration

| Step | Action | Verification | Records |
|---|---|---|---|
| C1 | Receive package at site; perform preservation check | Preservation walk-down | Receipt and preservation record |
| C2 | Install skid; complete tie-ins per EPC P&IDs (regen-gas source per R-3.1; outlet to product storage; drains to produced water and SOC paths per R-2.5) | EPC Integrator construction walk-down | Punch list |
| C3 | Loop checks and instrument calibration on site (R-4.1, R-4.2) | Loop-check sign-off | Loop check records |
| C4 | Adsorbent loading per vendor procedure | Loading witness; bed level checks | Loading record |

### Stage D — Commissioning and performance test

| Step | Action | Verification | Records |
|---|---|---|---|
| D1 | First-fill / displacement; pressure leak test of assembled package | Leak-test acceptance | Commissioning log |
| D2 | First adsorption cycle on saturated NGL feed | Outlet moisture trend toward R-1.7/R-1.8/R-1.9 target via MA-6800-1 | Cycle log |
| D3 | First regeneration cycle with confirmed regen-gas source | Heater outlet 460 deg F (TBC); cooler outlet 110 deg F at design; scrubber drain functional | Regen cycle log |
| D4 | Confirm contamination-handling path (blow-down to flare) is operable | Simulated isolation/blow-down test (procedure TBD) | Contamination-handling test record |
| D5 | Performance test over full cycle | Outlet water content vs. R-1.9 (TBC governing); bed dP vs. R-1.10/R-1.11 | Performance test report |

### Stage E — Turnover

| Step | Action | Verification | Records |
|---|---|---|---|
| E1 | Compile vendor document register and submit to `DEL-070-05` Vendor Document Turnover Package | Document register completeness | Turnover dossier |
| E2 | EPC Integrator performs review and acceptance via `DEL-070-06` | Acceptance checklist closed | Acceptance record |

## Verification (rolled up)

- All `R-1.x` requirements verified by vendor process documentation and performance test (Stages A2, D2, D5).
- All `R-2.x` requirements verified by mechanical documentation, mill certs, hydrotest, and FAT (Stages A3, B1, B2, B3).
- All `R-3.x` requirements verified by commissioning regeneration cycle (Stage D3) and contamination-handling test (Stage D4).
- All `R-4.x` requirements verified by loop checks and analyzer calibration (Stages B3, C3).
- All `R-5.x` requirements verified by vendor sparing statement and adsorbent supplier warranty (Stages A2, B4).

## Records (outputs)

- Vendor package design basis and datasheet set.
- Vessel/exchanger/filter/scrubber/cooler datasheets.
- Skid GA, P&ID, I&C schedule.
- Jurisdictional registration certificates; mill certs; hydrotest, NDE, FAT reports.
- Adsorbent supply certificates and lifecycle warranty.
- Loop check, commissioning, regeneration cycle, and performance test records.
- Vendor document register and turnover dossier (handed to `DEL-070-05`).
- EPC Integrator acceptance record (consumed by `DEL-070-06`).
